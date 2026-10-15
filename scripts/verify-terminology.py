#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Verifiziert alle `value_set.codings[]` der Datenelemente gegen einen FHIR-Terminologieserver.

Default-Ziel ist der MII TermServ (Ontoserver, mTLS mit Client-Zertifikat). Für jedes Coding wird
`CodeSystem/$lookup` aufgerufen; das Ergebnis (gefunden / nicht gefunden / inaktiv, Anzeigetext des
Servers vs. Anzeigetext im Repo) wird als Tabelle ausgegeben und optional als JSON gespeichert.
Codesysteme, die der Server nicht führt (z. B. ICF, MedDRA), werden als UNVERIFIZIERBAR gelistet.

Aufruf (Zertifikat + Schlüssel liegen NICHT im Repo; Pfade als Argumente übergeben):
  python scripts/verify-terminology.py --cert client.crt --key client.key
  python scripts/verify-terminology.py --cert client.crt --key client.key --json report.json
  python scripts/verify-terminology.py --base-url https://other.termserver/fhir elements/follow-up/ctThoraxScan.yaml

Nur Standardbibliothek + PyYAML; keine Schreibzugriffe auf `elements/`.
"""
from __future__ import annotations

import argparse
import json
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

# Repo-Systemkürzel → kanonische FHIR-CodeSystem-URL (wie auf dem MII TermServ hinterlegt).
SYSTEM_URL: dict[str, str] = {
    "snomed-ct": "http://snomed.info/sct",
    "loinc": "http://loinc.org",
    "icd-10-gm": "http://fhir.de/CodeSystem/bfarm/icd-10-gm",
    "ops": "http://fhir.de/CodeSystem/bfarm/ops",
    "atc": "http://fhir.de/CodeSystem/bfarm/atc",
    "kdl": "http://dvmd.de/fhir/CodeSystem/kdl",
    "ucum": "http://unitsofmeasure.org",
    "icd-o-3": "http://terminology.hl7.org/CodeSystem/icd-o-3",
    "icf": "http://fhir.de/CodeSystem/bfarm/icf",
    "meddra": "http://terminology.hl7.org/CodeSystem/mdr",
    "hl7-v3": "http://terminology.hl7.org/CodeSystem/v3-ActCode",
    "dicom-dcm": "http://dicom.nema.org/resources/ontology/DCM",
    "radlex": "http://radlex.org",
    "ncit": "http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl",
}
# Systeme ohne Repo-Schlüssel dürfen als vollständige kanonische URL angegeben werden (z. B. HL7-v3-Codesysteme).
LOCAL_SYSTEMS = {"local-no-standard-binding"}


def lookup(base_url: str, ctx: ssl.SSLContext | None, system: str, code: str, timeout: int) -> dict:
    params = urllib.parse.urlencode({"system": system, "code": code})
    req = urllib.request.Request(
        f"{base_url.rstrip('/')}/CodeSystem/$lookup?{params}",
        headers={"Accept": "application/fhir+json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            data = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        return {"status": "NOT-FOUND", "http": e.code}
    except Exception as e:  # noqa: BLE001 — Netzwerk-/TLS-Fehler sichtbar machen
        return {"status": "ERROR", "error": str(e)}
    display = None
    inactive = False
    for p in data.get("parameter", []):
        if p.get("name") == "display":
            display = p.get("valueString")
        if p.get("name") == "property":
            parts = {x.get("name"): x for x in p.get("part", [])}
            code_name = parts.get("code", {}).get("valueCode")
            if code_name == "inactive":
                inactive = bool(parts.get("value", {}).get("valueBoolean"))
            elif code_name == "status" and parts.get("value", {}).get("valueCode") in ("retired", "deprecated"):
                inactive = True
    return {"status": "INACTIVE" if inactive else "OK", "display": display}


def collect_files(args: list[str]) -> list[Path]:
    if args:
        return [Path(a) for a in args]
    return sorted((ROOT / "elements").glob("*/*.yaml"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("files", nargs="*", help="YAML-Dateien (Default: elements/**/*.yaml)")
    ap.add_argument("--base-url", default="https://ontoserver.mii-termserv.de/fhir")
    ap.add_argument("--cert", help="Client-Zertifikat (PEM) für mTLS")
    ap.add_argument("--key", help="privater Schlüssel (PEM) zum Client-Zertifikat")
    ap.add_argument("--json", help="Ergebnis zusätzlich als JSON speichern")
    ap.add_argument("--timeout", type=int, default=40)
    args = ap.parse_args()

    ctx = ssl.create_default_context()
    if args.cert:
        ctx.load_cert_chain(args.cert, args.key)

    rows: list[dict] = []
    for fp in collect_files(args.files):
        doc = yaml.safe_load(fp.read_text(encoding="utf-8")) or {}
        for c in (doc.get("value_set") or {}).get("codings") or []:
            system, code = str(c.get("system", "")), str(c.get("code", ""))
            row = {"element": doc.get("name"), "phase": doc.get("phase"), "system": system,
                   "code": code, "display_repo": c.get("display")}
            if system in LOCAL_SYSTEMS:
                row.update(status="LOCAL")
            elif system not in SYSTEM_URL and not str(system).startswith(("http://", "https://", "urn:")):
                row.update(status="UNKNOWN-SYSTEM")
            else:
                row.update(lookup(args.base_url, ctx, SYSTEM_URL.get(system, system), code, args.timeout))
            rows.append(row)

    # Codesysteme, die der Server gar nicht kennt → alle Codes darin als UNVERIFIZIERBAR markieren
    for system in {r["system"] for r in rows if r.get("status") == "NOT-FOUND"}:
        sys_rows = [r for r in rows if r["system"] == system]
        if sys_rows and all(r.get("status") == "NOT-FOUND" for r in sys_rows):
            for r in sys_rows:
                r["status"] = "UNVERIFIABLE"

    counts: dict[str, int] = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    width = max((len(r["element"] or "") for r in rows), default=10)
    for r in rows:
        if r["status"] in ("OK", "LOCAL"):
            continue
        print(f"{r['status']:13} {r['element']:{width}} {r['system']:10} {r['code']:18} "
              f"repo='{r.get('display_repo')}' server='{r.get('display')}'")
    print("\nZusammenfassung:", ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    if args.json:
        Path(args.json).write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"JSON: {args.json}")
    return 1 if counts.get("NOT-FOUND") or counts.get("INACTIVE") or counts.get("ERROR") else 0


if __name__ == "__main__":
    raise SystemExit(main())
