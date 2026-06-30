#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Erzeugt die Excel-Erhebungs-Vorlage für die Klinik-Spur (ohne Git/YAML).

Die Vorlage ist schema-getrieben: alle Dropdown-Werte stammen aus den Enums in
`schemas/data-element.schema.json` bzw. den laienverständlichen Abbildungen in
`scripts/_elicitation.py` — sie kann daher nicht vom Schema abdriften.

Aufruf:
  pip install openpyxl
  python scripts/build-elicitation-workbook.py                       # -> templates/datenelement-erhebung.xlsx
  python scripts/build-elicitation-workbook.py --out /pfad/x.xlsx --rows 80

Ausgefüllte Mappen werden mit `scripts/import-elicitation-workbook.py` zu YAML-Entwürfen.
"""
from __future__ import annotations

import argparse
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

import _elicitation as E

HEADER_FILL = PatternFill("solid", fgColor="1A5DAB")
HEADER_FONT = Font(bold=True, color="FFFFFF")
MAND_FILL = PatternFill("solid", fgColor="FCE8E6")  # zarte Markierung für Pflichtspalten
WRAP = Alignment(wrap_text=True, vertical="top")
TITLE_FONT = Font(bold=True, size=14)


def _style_header(ws, ncols: int) -> None:
    for c in range(1, ncols + 1):
        cell = ws.cell(row=1, column=c)
        cell.fill = HEADER_FILL
        cell.font = HEADER_FONT
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    ws.freeze_panes = "A2"
    ws.row_dimensions[1].height = 30


def _write_codelists(ws, lists: dict[str, list[str]]) -> dict[str, str]:
    """Schreibt jede Dropdown-Liste in eine Spalte; gibt {listname: range-formula} zurück."""
    ranges: dict[str, str] = {}
    for idx, (name, values) in enumerate(lists.items(), start=1):
        col = get_column_letter(idx)
        ws.cell(row=1, column=idx, value=name).font = Font(bold=True)
        for r, val in enumerate(values, start=2):
            ws.cell(row=r, column=idx, value=val)
        ranges[name] = f"=Codelisten!${col}$2:${col}${len(values) + 1}"
        ws.column_dimensions[col].width = max(18, min(48, max((len(v) for v in values), default=10) + 2))
    ws.sheet_state = "hidden"
    return ranges


def _add_table(wb, sheet_name: str, columns, rows: int, ranges: dict[str, str],
               extra_list_validations=None) -> None:
    ws = wb.create_sheet(sheet_name)
    for ci, (_key, header, mandatory, _list) in enumerate(columns, start=1):
        ws.cell(row=1, column=ci, value=header)
        width = 40 if header.startswith(("Klinische_Definition", "Anmerkungen")) else 22
        ws.column_dimensions[get_column_letter(ci)].width = width
        if mandatory:
            for r in range(2, rows + 2):
                ws.cell(row=r, column=ci).fill = MAND_FILL
    _style_header(ws, len(columns))
    last = rows + 1
    for ci, (_key, _header, _mandatory, listname) in enumerate(columns, start=1):
        if not listname:
            continue
        formula = ranges.get(listname) or (extra_list_validations or {}).get(listname)
        if not formula:
            continue
        dv = DataValidation(type="list", formula1=formula, allow_blank=True)
        col = get_column_letter(ci)
        dv.add(f"{col}2:{col}{last}")
        ws.add_data_validation(dv)
    return ws


def _write_intro(ws) -> None:
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 4
    ws.column_dimensions["B"].width = 110
    lines = [
        ("MiHUB Lungenkrebs — Datenelement-Erhebung (Klinik-Spur)", TITLE_FONT),
        ("", None),
        ("Mit dieser Mappe können klinische Expert:innen neue Datenelemente für den "
         "Lungenkrebs-Patientenpfad vorschlagen — ohne GitHub, ohne YAML.", None),
        ("Das MI-Team übernimmt anschließend die technische Umsetzung (Codes, FHIR-Mappings) "
         "und bittet Sie, das Ergebnis inhaltlich zu bestätigen.", None),
        ("", None),
        ("So füllen Sie die Mappe aus:", Font(bold=True, size=12)),
        ("1. Blatt »Datenelemente«: eine Zeile je Datenelement. Pflichtspalten sind rot "
         "hinterlegt und mit * markiert. Felder mit Dropdown bitte aus der Liste wählen.", None),
        ("2. Vergeben Sie je Zeile eine kurze »lokale ID« (z. B. DE-001) — sie dient nur dazu, "
         "die Datennutzung im zweiten Blatt zuzuordnen.", None),
        ("3. Blatt »Datennutzung«: WO (System) · WER (Rolle) · WIE (Nutzung) wird das "
         "Datenelement genutzt? Mehrere Zeilen je Datenelement sind möglich und erwünscht.", None),
        ("4. Felder, zu denen Sie nichts beitragen können (z. B. SNOMED-Codes), dürfen leer "
         "bleiben — das MI-Team recherchiert sie.", None),
        ("", None),
        ("Beispiel »Rauchstatus« (Datennutzung):", Font(bold=True, size=12)),
        ("   • PVS · Hausärzt:in · erfasst (ambulant)", None),
        ("   • KIS · Onkolog:in · gelesen (stationär)", None),
        ("   • Forschungs-DWH/DIZ · Forscher:in · Forschung/Sekundärnutzung", None),
        ("", None),
        ("Andere Wege beizutragen: GitHub-Issue-Formular (online) oder YAML+Pull-Request "
         "(technisch). Siehe CONTRIBUTING.md / docs/howto-add-element.md.", None),
        ("", None),
        ("Beiträge erfolgen unter CC BY 4.0. Bitte keine personenbezogenen / realen "
         "Patientendaten eintragen — nur die abstrakte Datenelement-Definition.", Font(italic=True)),
        ("Kontakt: digital-health@tu-dresden.de", None),
    ]
    r = 1
    for text, font in lines:
        cell = ws.cell(row=r, column=2, value=text)
        cell.alignment = WRAP
        if font:
            cell.font = font
        r += 1


def build(out_path: Path, rows: int) -> Path:
    enums = E.load_schema_enums()
    lists = E.dropdown_lists(enums)

    wb = Workbook()
    _write_intro(wb.active)
    wb.active.title = "Anleitung"

    code_ws = wb.create_sheet("Codelisten")  # zunächst leer; befüllt nach den Tabellen
    elem_ws = _add_table(wb, "Datenelemente", E.ELEMENT_COLUMNS, rows, {})
    # local_id vorbefüllen (DE-001 …) zur einfachen Verknüpfung
    for i in range(rows):
        elem_ws.cell(row=2 + i, column=1, value=f"DE-{i + 1:03d}")

    ranges = _write_codelists(code_ws, lists)
    # Datennutzung: local_id als Liste auf die vorbefüllten Datenelement-IDs
    id_range = {"element_ids": f"=Datenelemente!$A$2:$A${rows + 1}"}
    flow_ws = _add_table(wb, "Datennutzung", E.FLOW_COLUMNS, rows * 3, ranges,
                         extra_list_validations=id_range)
    dv = DataValidation(type="list", formula1=id_range["element_ids"], allow_blank=True)
    dv.add(f"A2:A{rows * 3 + 1}")
    flow_ws.add_data_validation(dv)

    # Data-Validation der Datenelemente-Dropdowns nachziehen (Codelisten gibt es jetzt)
    last = rows + 1
    for ci, (_k, _h, _m, listname) in enumerate(E.ELEMENT_COLUMNS, start=1):
        if listname and listname in ranges:
            d = DataValidation(type="list", formula1=ranges[listname], allow_blank=True)
            col = get_column_letter(ci)
            d.add(f"{col}2:{col}{last}")
            elem_ws.add_data_validation(d)

    wb.move_sheet("Codelisten", offset=len(wb.sheetnames))  # ans Ende
    out_path.parent.mkdir(parents=True, exist_ok=True)
    wb.save(out_path)
    return out_path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", default=str(E.ROOT / "templates" / "datenelement-erhebung.xlsx"))
    ap.add_argument("--rows", type=int, default=60, help="Anzahl Eingabezeilen im Blatt 'Datenelemente'")
    args = ap.parse_args()
    out = build(Path(args.out), args.rows)
    print(f"Wrote {out} (Datenelemente: {args.rows} Zeilen, Datennutzung: {args.rows * 3} Zeilen)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
