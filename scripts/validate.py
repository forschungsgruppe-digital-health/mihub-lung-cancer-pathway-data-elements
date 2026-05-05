#!/usr/bin/env python3
"""Validiert alle YAML-Datenelemente gegen schemas/data-element.schema.json.

Aufruf:
  python scripts/validate.py                 # validiert alle elements/**/*.yaml
  python scripts/validate.py path/to.yaml    # validiert eine Datei
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml  # PyYAML
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schemas" / "data-element.schema.json"


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


def main(argv: list[str]) -> int:
    schema = load_schema()
    validator = Draft202012Validator(schema)
    files = collect_files(argv)
    if not files:
        print("Keine YAML-Dateien gefunden.")
        return 0
    failed = 0
    for f in files:
        errors = validate_file(validator, f)
        if errors:
            failed += 1
            print(f"FAIL  {f.relative_to(ROOT)}")
            for err in errors:
                print(f"      - {err}")
        else:
            print(f"OK    {f.relative_to(ROOT)}")
    print(f"\nValidiert: {len(files)} · OK: {len(files) - failed} · FAIL: {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
