#!/usr/bin/env python3
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
        "guideline_source": g.get("source", ""),
        "guideline_section": g.get("section", ""),
        "recommendation_grade": g.get("recommendation_grade", ""),
        "evidence_level": g.get("evidence_level", ""),
        "iso13972_type": md.get("type", ""),
        "version": md.get("version_number", ""),
    }


def main() -> int:
    files = sorted((ROOT / "elements").glob("*/*.yaml"))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(HEADER)
        for fp in files:
            with fp.open(encoding="utf-8") as g:
                doc = yaml.safe_load(g)
            r = row(doc)
            w.writerow([r[k] for k in KEYS])
    print(f"Wrote {OUT.relative_to(ROOT)} ({len(files)} elements)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
