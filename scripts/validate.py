#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Validiert alle YAML-Datenelemente gegen schemas/data-element.schema.json.

Aufruf:
  python scripts/validate.py                 # validiert alle elements/**/*.yaml
  python scripts/validate.py path/to.yaml    # validiert eine Datei

Zusätzlich zur Schema-Prüfung (Konsistenz über Dateien hinweg):
  - `id` = mihub.lung.<phase>.<name>.v<major>.<minor> (Phase und Name stimmen mit den Feldern überein)
  - Dateiname = `name`, Ordner passt zur Phase (follow-up, surveillance, palliative, primary-care, screening)
  - `id`, `name`, `uuid` sind katalogweit eindeutig
  - `related_elements[].target` ist die vollständige `id` eines existierenden Datenelements (keine Selbstreferenz)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml  # PyYAML
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schemas" / "data-element.schema.json"


def rel(path: Path) -> str:
    """Pfad relativ zum Repo-Root, sonst der unveränderte Pfad (z. B. Staging-Verzeichnisse)."""
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def load_schema() -> dict:
    with SCHEMA_PATH.open(encoding="utf-8") as f:
        return json.load(f)


def collect_files(args: list[str]) -> list[Path]:
    if args:
        return [Path(a) for a in args]
    return sorted((ROOT / "elements").glob("*/*.yaml"))


def validate_file(validator: Draft202012Validator, path: Path) -> list[str]:
    try:
        with path.open(encoding="utf-8") as f:
            doc = yaml.safe_load(f)
    except yaml.YAMLError as e:
        return [f"YAML parse error: {e}"]
    errors = list(validator.iter_errors(doc))
    return [f"{'.'.join(str(p) for p in e.absolute_path) or '<root>'}: {e.message}" for e in errors]


PHASE_DIRS = {"followup": "follow-up", "primarycare": "primary-care"}


def load_doc(path: Path) -> dict | None:
    try:
        with path.open(encoding="utf-8") as f:
            doc = yaml.safe_load(f)
    except (OSError, yaml.YAMLError):
        return None
    return doc if isinstance(doc, dict) else None


def catalog_index() -> dict[str, dict]:
    """id -> doc für alle Datenelemente unter elements/ (Grundlage der Verweisprüfung)."""
    index: dict[str, dict] = {}
    for fp in sorted((ROOT / "elements").glob("*/*.yaml")):
        doc = load_doc(fp)
        if doc and doc.get("id"):
            index[str(doc["id"])] = doc
    return index


def consistency_errors(path: Path, doc: dict | None, known_ids: set[str]) -> list[str]:
    if not doc:
        return []
    errs: list[str] = []
    phase, name, eid = doc.get("phase"), doc.get("name"), str(doc.get("id", ""))
    if phase and name and not eid.startswith(f"mihub.lung.{phase}.{name}.v"):
        errs.append(f"id: '{eid}' passt nicht zu phase '{phase}' und name '{name}'")
    vn = str((doc.get("iso13972_metadata") or {}).get("version_number", ""))
    m = re.search(r"\.v(\d+)\.(\d+)$", eid)
    if m and vn and ".".join(vn.split(".")[:2]) != f"{m.group(1)}.{m.group(2)}":
        errs.append(f"id-Suffix v{m.group(1)}.{m.group(2)} passt nicht zu version_number {vn} (Regel: docs/howto-add-element.md §C)")
    hist = (doc.get("provenance") or {}).get("history") or []
    if hist and vn and hist[-1].get("version") != vn:
        errs.append(f"provenance.history: letzter Eintrag {hist[-1].get('version')} ≠ version_number {vn}")
    try:
        inside = path.resolve().relative_to((ROOT / "elements").resolve())
    except ValueError:
        inside = None
    if inside is not None and len(inside.parts) == 2:
        if name and path.stem != name:
            errs.append(f"Dateiname '{path.name}' entspricht nicht name '{name}'")
        if phase and inside.parts[0] != PHASE_DIRS.get(phase, phase):
            errs.append(f"Ordner '{inside.parts[0]}' passt nicht zu phase '{phase}' (erwartet '{PHASE_DIRS.get(phase, phase)}')")
    for i, r in enumerate(doc.get("related_elements") or []):
        t = str((r or {}).get("target", ""))
        if t == eid:
            errs.append(f"related_elements.{i}.target: Selbstreferenz")
        elif t not in known_ids:
            errs.append(f"related_elements.{i}.target: '{t}' ist keine id eines existierenden Datenelements")
    return errs


def main(argv: list[str]) -> int:
    schema = load_schema()
    validator = Draft202012Validator(schema)
    files = collect_files(argv)
    if not files:
        print("Keine YAML-Dateien gefunden.")
        return 0
    index = catalog_index()
    docs = {f: load_doc(f) for f in files}
    known_ids = set(index) | {str(d["id"]) for d in docs.values() if d and d.get("id")}
    # katalogweite Eindeutigkeit (über alle Elemente + die geprüften Dateien)
    seen: dict[tuple[str, str], list[str]] = {}
    for d in list(index.values()) + [d for d in docs.values() if d]:
        for key in ("id", "name", "uuid"):
            if d.get(key):
                seen.setdefault((key, str(d[key])), [])
                if d.get("id") not in seen[(key, str(d[key]))]:
                    seen[(key, str(d[key]))].append(str(d.get("id")))
    dup = {k: v for k, v in seen.items() if len(v) > 1}
    failed = 0
    for f in files:
        errors = validate_file(validator, f) + consistency_errors(f, docs.get(f), known_ids)
        d = docs.get(f) or {}
        for key in ("id", "name", "uuid"):
            if d.get(key) and (key, str(d[key])) in dup:
                errors.append(f"{key}: '{d[key]}' ist nicht eindeutig (auch in {', '.join(x for x in dup[(key, str(d[key]))] if x != d.get('id'))})")
        if errors:
            failed += 1
            print(f"FAIL  {rel(f)}")
            for err in errors:
                print(f"      - {err}")
        else:
            print(f"OK    {rel(f)}")
    print(f"\nValidiert: {len(files)} · OK: {len(files) - failed} · FAIL: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
