#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Aggregiert alle YAML-Datenelemente zu catalog/data-dictionary.csv (Semicolon-CSV)."""
from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "catalog" / "data-dictionary.csv"

# CSV-Spalten mit Pflicht-Markern: * = mandatory (Schema-Pflicht), + = recommended,
# (ohne) = optional. Die Marker stehen direkt im Header, damit Reviewer:innen sofort
# erkennen, welche Spalten leer bleiben dürfen.
COLUMNS = [
    ("id*", "id"),
    ("phase*", "phase"),
    ("tumor_entity+", "tumor_entity"),
    ("label_de*", "label_de"),
    ("name*", "name"),
    ("datatype*", "datatype"),
    ("cardinality*", "cardinality"),
    ("unit", "unit"),
    ("value_set_system+", "value_set_system"),
    ("value_set_code_example+", "value_set_code_example"),
    ("binding_strength+", "binding_strength"),
    ("standard_binding_status", "standard_binding_status"),
    ("standard_mapping_primary+", "standard_mapping_primary"),
    ("standard_mapping_resource+", "standard_mapping_resource"),
    ("trigger+", "trigger"),
    ("frequency_pattern+", "frequency_pattern"),
    ("responsible_role+", "responsible_role"),
    ("care_process_data_flows", "care_process_data_flows"),
    ("guideline_source+", "guideline_source"),
    ("guideline_section+", "guideline_section"),
    ("recommendation_grade", "recommendation_grade"),
    ("evidence_level", "evidence_level"),
    ("iso13972_type+", "iso13972_type"),
    ("version*", "version"),
]
HEADER = [c[0] for c in COLUMNS]
KEYS = [c[1] for c in COLUMNS]


def first_coding(doc: dict[str, Any]) -> tuple[str, str]:
    vs = doc.get("value_set") or {}
    codings = vs.get("codings") or []
    if codings:
        c = codings[0]
        return c.get("system", ""), c.get("code", "")
    return "", ""


def first_guideline(doc: dict[str, Any]) -> dict[str, str]:
    refs = (doc.get("evidence") or {}).get("guideline_references") or []
    if refs:
        return refs[0]
    return {}


def first_standard_mapping(doc: dict[str, Any]) -> tuple[str, str]:
    sm = doc.get("standard_mappings") or []
    if sm:
        primary = sm[0]
        return f"{primary.get('standard','')}:{primary.get('profile_or_url','')}", primary.get("resource", "")
    return "", ""


def data_flows_summary(cp: dict[str, Any]) -> str:
    """Flacht care_process.data_flows[] zu 'System/Rolle:Nutzung; …' (eine CSV-Zelle)."""
    parts: list[str] = []
    for fl in cp.get("data_flows") or []:
        seg = fl.get("system_label") or fl.get("system", "")
        if fl.get("actor_role"):
            seg += f"/{fl['actor_role']}"
        if fl.get("usage_type"):
            seg += f":{fl['usage_type']}"
        if seg:
            parts.append(seg)
    return " · ".join(parts)


def row(doc: dict[str, Any]) -> dict[str, str]:
    vs = doc.get("value_set") or {}
    cp = doc.get("care_process") or {}
    g = first_guideline(doc)
    sys_, code = first_coding(doc)
    md = doc.get("iso13972_metadata") or {}
    sm_primary, sm_resource = first_standard_mapping(doc)
    return {
        "id": doc.get("id", ""),
        "phase": doc.get("phase", ""),
        "tumor_entity": ",".join(doc.get("tumor_entity", []) or []),
        "label_de": doc.get("label_de", ""),
        "name": doc.get("name", ""),
        "datatype": doc.get("datatype", ""),
        "cardinality": doc.get("cardinality", ""),
        "unit": doc.get("unit", ""),
        "value_set_system": sys_,
        "value_set_code_example": code,
        "binding_strength": vs.get("binding_strength", ""),
        "standard_binding_status": vs.get("standard_binding_status", ""),
        "standard_mapping_primary": sm_primary,
        "standard_mapping_resource": sm_resource,
        "trigger": cp.get("trigger", ""),
        "frequency_pattern": cp.get("frequency_pattern", ""),
        "responsible_role": cp.get("responsible_role", ""),
        "care_process_data_flows": data_flows_summary(cp),
        "guideline_source": g.get("source", ""),
        "guideline_section": g.get("section", ""),
        "recommendation_grade": g.get("recommendation_grade", ""),
        "evidence_level": g.get("evidence_level", ""),
        "iso13972_type": md.get("type", ""),
        "version": md.get("version_number", ""),
    }


def md_escape(value: str) -> str:
    """Escape Markdown-Tabellen-Zellinhalt (Pipe + Newlines)."""
    if value is None:
        return ""
    s = str(value)
    s = s.replace("|", "\\|").replace("\n", " ").replace("\r", " ")
    return s.strip()


def write_markdown(rows: list[dict], total: int) -> Path:
    """Schreibt 1:1-Markdown-Spiegelung der CSV (gleiche Spalten, gleiche Reihenfolge)."""
    md_path = OUT.with_suffix(".md")
    lines: list[str] = []
    lines.append("# Data Dictionary — Markdown-Mirror der `data-dictionary.csv`")
    lines.append("")
    lines.append("> **Auto-generiert** durch `scripts/build-catalog.py`. 1:1-Spiegelung der CSV in Markdown-Form für GitHub-PR-Diffs, Web-UI-Suche und Element-Direktverlinkung.")
    lines.append("")
    lines.append(f"> **Zielgruppe:** technische Nutzer:innen (volles Data-Dictionary, {len(HEADER)} Spalten). Lesefreundliche Phasen-Übersicht für Klinik-Reviewer:innen unter `docs/phases-overview.md` (kuratierte Untermenge).")
    lines.append("")
    lines.append("Pflicht-Marker im Header: `*` = mandatory · `+` = recommended · (kein Suffix) = optional. Stand: " + str(total) + " Datenelemente.")
    lines.append("")
    lines.append("| " + " | ".join(HEADER) + " |")
    lines.append("| " + " | ".join(["---"] * len(HEADER)) + " |")
    for r in rows:
        cells = [md_escape(r[k]) for k in KEYS]
        lines.append("| " + " | ".join(cells) + " |")
    lines.append("")
    md_path.write_text("\n".join(lines), encoding="utf-8")
    return md_path


def write_phases_overview(files: list[Path]) -> Path:
    """Schreibt die kuratierte Phasen-Übersicht (8 Spalten, Klinik-Zielgruppe)."""
    phases = [
        ("follow-up", "Onkologische Nachsorge (kurativ behandelt)",
         "Datenelemente nach kurativ-intendierter multimodaler Therapie. "
         "Mit Ergebnis-Artefakten zu Bildgebung und Lungenfunktion."),
        ("surveillance", "Verlaufsbeobachtung / Surveillance (unter Systemtherapie)",
         "Datenelemente unter laufender palliativer Systemtherapie. "
         "Mit Ergebnis-Artefakten zu Mutationstest und CTCAE-Grad."),
        ("palliative", "Palliativversorgung",
         "Datenelemente in der spezialisierten und allgemeinen Palliativversorgung."),
    ]
    out: list[str] = []
    out.append("# Phasenübersicht — Datenelemente")
    out.append("")
    out.append("Lesefreundliche, kuratierte 8-Spalten-Sicht je Versorgungsphase. "
               "Quelle: `elements/<phase>/*.yaml` (autogeneriert durch `scripts/build-catalog.py`).")
    out.append("")
    out.append(f"Stand: **{len(files)} Datenelemente** · für die volle {len(HEADER)}-Spalten-Sicht "
               "siehe `catalog/data-dictionary.csv` bzw. `catalog/data-dictionary.md` (1:1-Mirror).")
    out.append("")
    for phase_dir, title, desc in phases:
        out.append(f"## {title}")
        out.append("")
        out.append(desc)
        out.append("")
        rows_md: list[dict] = []
        for fp in sorted((ROOT / "elements" / phase_dir).glob("*.yaml")):
            with fp.open(encoding="utf-8") as f:
                d = yaml.safe_load(f)
            codings = (d.get("value_set") or {}).get("codings") or []
            coding_str = ", ".join(
                [f"{c.get('system','')}:{c.get('code','')}" for c in codings[:3]]
            ) or "—"
            refs = (d.get("evidence") or {}).get("guideline_references") or []
            ref_str = "; ".join(
                [f"{r.get('source','')} {r.get('section','')}" for r in refs[:2]]
            ) or "—"
            cp = d.get("care_process") or {}
            rows_md.append({
                "label": d.get("label_de", ""),
                "name": d.get("name", ""),
                "datatype": d.get("datatype", ""),
                "card": d.get("cardinality", ""),
                "coding": coding_str,
                "trigger": cp.get("trigger", "") or "—",
                "freq": cp.get("frequency_pattern", "") or "—",
                "role": cp.get("responsible_role", "") or "—",
                "refs": ref_str,
            })
        out.append("| Bezeichnung (DE) | name | Datentyp · Card | Beispiel-Codings | "
                  "Trigger | Frequenz | Rolle | Quelle |")
        out.append("| --- | --- | --- | --- | --- | --- | --- | --- |")
        for r in rows_md:
            out.append(f"| {r['label']} | `{r['name']}` | {r['datatype']} · {r['card']} | "
                       f"{r['coding']} | {r['trigger']} | {r['freq']} | {r['role']} | "
                       f"{r['refs']} |")
        out.append("")
    overview_path = ROOT / "docs" / "phases-overview.md"
    overview_path.parent.mkdir(parents=True, exist_ok=True)
    overview_path.write_text("\n".join(out), encoding="utf-8")
    return overview_path


def main() -> int:
    files = sorted((ROOT / "elements").glob("*/*.yaml"))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []
    for fp in files:
        with fp.open(encoding="utf-8") as g:
            doc = yaml.safe_load(g)
        rows.append(row(doc))

    # 1) CSV
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(HEADER)
        for r in rows:
            w.writerow([r[k] for k in KEYS])
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(files)} elements)")

    # 2) 1:1-Markdown-Mirror (volle Spaltenzahl = len(HEADER))
    md_path = write_markdown(rows, len(files))
    print(f"Wrote {md_path.relative_to(ROOT)} ({len(files)} elements, mirror)")

    # 3) Kuratierte Phasen-Übersicht (8 Spalten, Klinik-Zielgruppe)
    overview_path = write_phases_overview(files)
    print(f"Wrote {overview_path.relative_to(ROOT)} ({len(files)} elements, kuratiert)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
