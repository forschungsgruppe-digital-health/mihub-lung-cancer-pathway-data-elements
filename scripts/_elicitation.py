# SPDX-License-Identifier: Apache-2.0
"""Gemeinsame Definitionen für die Excel-Erhebungs-Vorlage (Klinik-Spur ohne Git/YAML).

Single source of truth für:
  - die Spalten der beiden Erhebungs-Tabellen ("Datenelemente", "Datennutzung"),
  - die laienverständlichen Dropdown-Werte und ihre Abbildung auf die Schema-Enums.

Wird von `build-elicitation-workbook.py` (Vorlage erzeugen) UND
`import-elicitation-workbook.py` (ausgefüllte Vorlage → YAML-Entwürfe) importiert,
damit beide nie auseinanderlaufen. Die Schema-Enums werden zur Laufzeit direkt aus
`schemas/data-element.schema.json` gelesen — sie sind also nur an EINER Stelle gepflegt.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schemas" / "data-element.schema.json"


# --- Schema-Enums (zur Laufzeit aus dem JSON-Schema gelesen) -----------------

def load_schema_enums(schema_path: Path = SCHEMA_PATH) -> dict[str, list[str]]:
    """Liest die für die Erhebung relevanten Enums aus dem JSON-Schema."""
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    p = schema["properties"]
    cp = p["care_process"]["properties"]["data_flows"]["items"]["properties"]
    gref = p["evidence"]["properties"]["guideline_references"]["items"]["properties"]
    return {
        "phase": p["phase"]["enum"],
        "tumor_entity": p["tumor_entity"]["items"]["enum"],
        "datatype": p["datatype"]["enum"],
        "binding_strength": p["value_set"]["properties"]["binding_strength"]["enum"],
        "standard_binding_status": p["value_set"]["properties"]["standard_binding_status"]["enum"],
        "standard": p["standard_mappings"]["items"]["properties"]["standard"]["enum"],
        "iso_type": p["iso13972_metadata"]["properties"]["type"]["enum"],
        "guideline_source": gref["source"]["enum"],
        "recommendation_grade": gref["recommendation_grade"]["enum"],
        "df_system": cp["system"]["enum"],
        "df_usage_type": cp["usage_type"]["enum"],
        "df_sector": cp["sector"]["enum"],
    }


# --- Laienverständliche Dropdown-Werte -> Schema-Codes ------------------------
# Reihenfolge = Reihenfolge im Dropdown. Schlüssel = Anzeigetext, Wert = Schema-Code.

PHASE_LAYMEN: dict[str, str] = {
    "Onkologische Nachsorge (kurativ behandelt)": "followup",
    "Verlaufsbeobachtung / Surveillance (unter Systemtherapie)": "surveillance",
    "Palliativversorgung": "palliative",
    "Andere / neue Phase (rechts benennen)": "other",
}

DATATYPE_LAYMEN: dict[str, str] = {
    "Ja/Nein": "boolean",
    "Zahl (ganzzahlig, z. B. Score, Anzahl)": "integer",
    "Zahl (mit Dezimalstellen)": "decimal",
    "Datum": "date",
    "Datum + Uhrzeit": "dateTime",
    "Zeitraum (von–bis)": "Period",
    "Codierter Begriff aus Liste (SNOMED/ICD/LOINC)": "CodeableConcept",
    "Freitext (kurz)": "string",
    "Freitext (lang)": "text",
    "Dosis/Menge mit Einheit (z. B. mg)": "Quantity",
    "Verweis auf Dokument/Befund": "Reference",
}

CARDINALITY_LAYMEN: dict[str, str] = {
    "Genau einmal (Pflicht)": "1..1",
    "Höchstens einmal (optional)": "0..1",
    "Mehrfach möglich, mind. einmal": "1..*",
    "Mehrfach möglich (optional)": "0..*",
}

SYSTEM_LAYMEN: dict[str, str] = {
    "Primärverwaltungssystem / Praxis-VS (PVS)": "pvs",
    "Krankenhausinformationssystem (KIS/AIS)": "kis",
    "Tumordokumentationssystem": "tumordokumentation",
    "Klinisches/Epidemiologisches Krebsregister": "krebsregister",
    "Labor-/Pathologie-IS (LIS)": "lis-patho",
    "Radiologie (RIS/PACS)": "ris-pacs",
    "Elektronische Patientenakte (ePA)": "epa",
    "Patientenportal / PRO-App": "patientenportal",
    "Forschungs-DWH / DIZ / FDPG": "forschung-dwh-diz",
    "Vernetzungs-/Kooperationsplattform": "vernetzungsplattform",
    "Sonstiges (bitte System benennen)": "other",
}

USAGE_LAYMEN: dict[str, str] = {
    "erfasst / eingegeben": "capture",
    "gelesen / eingesehen": "read",
    "aktualisiert / korrigiert": "update",
    "geprüft / freigegeben": "validate",
    "übermittelt / ausgetauscht": "transmit",
    "gespeichert / archiviert": "store",
    "abgeleitet / berechnet": "derive",
    "Forschung / Sekundärnutzung": "secondary-use",
    "im Patientenportal angezeigt": "display-to-patient",
    "durch Patient:in selbst erfasst": "patient-entered",
    "Sonstiges": "other",
}

SECTOR_LAYMEN: dict[str, str] = {
    "ambulant": "ambulant",
    "stationär": "stationaer",
    "sektorenübergreifend": "sektorenuebergreifend",
    "häuslich / zuhause": "haeuslich",
}

JA_NEIN: dict[str, bool] = {"Ja": True, "Nein": False}


def map_value(raw: Any, mapping: dict[str, Any], *, default: Any = None) -> Any:
    """Bildet einen Dropdown-Anzeigetext (oder bereits einen Code) auf den Schema-Code ab."""
    if raw is None or str(raw).strip() == "":
        return default
    s = str(raw).strip()
    if s in mapping:
        return mapping[s]
    if s in mapping.values():  # bereits ein gültiger Code
        return s
    # tolerant: Anzeigetext-Präfix (z. B. nur "erfasst")
    for label, code in mapping.items():
        if s.lower() == label.split(" / ")[0].split(" (")[0].strip().lower():
            return code
    return default if default is not None else s


# --- Spalten der beiden Erhebungs-Tabellen -----------------------------------
# (key, Header, Pflicht?, dropdown-Listenname|None)  — Header mit * = Pflicht.

ELEMENT_COLUMNS: list[tuple[str, str, bool, str | None]] = [
    ("local_id", "lokale_ID*", True, None),
    ("label_de", "Bezeichnung_DE*", True, None),
    ("definition_de", "Klinische_Definition*", True, None),
    ("phase", "Versorgungsphase*", True, "phase"),
    ("phase_other", "Phase_falls_andere", False, None),
    ("tumor_entity", "Tumorentität", False, "tumor_entity_multi"),
    ("datatype", "Datentyp*", True, "datatype_laymen"),
    ("cardinality", "Häufigkeit*", True, "cardinality_laymen"),
    ("unit", "Einheit_UCUM", False, None),
    ("trigger", "Wann_erfasst_Trigger*", True, None),
    ("frequency_pattern", "Erhebungsfrequenz", False, None),
    ("responsible_role", "Verantwortliche_Rolle*", True, None),
    ("codings", "Codierungs-Vorschläge", False, None),
    ("binding_strength", "Binding-Stärke", False, "binding_strength"),
    ("standards_hint", "Standard-Anbindung_Hinweis", False, None),
    ("guideline_source", "Leitlinien-Quelle*", True, "guideline_source"),
    ("guideline_section", "Kapitel/Empfehlung/Tabelle*", True, None),
    ("recommendation_grade", "Empfehlungsgrad", False, "recommendation_grade"),
    ("evidence_level", "Evidenzlevel", False, None),
    ("notes", "Anmerkungen/Beziehungen", False, None),
    ("contact", "Kontakt_für_Rückfragen", False, None),
]

FLOW_COLUMNS: list[tuple[str, str, bool, str | None]] = [
    ("local_id", "lokale_ID_des_Datenelements*", True, None),
    ("label_hint", "Bezeichnung_(zur_Orientierung)", False, None),
    ("system", "System_WO*", True, "system_laymen"),
    ("system_label", "System_Klartext_(bei_Sonstiges)", False, None),
    ("actor_role", "Rolle_WER", False, None),
    ("usage_type", "Nutzung_WIE*", True, "usage_laymen"),
    ("sector", "Sektor", False, "sector_laymen"),
    ("mandatory", "Pflicht?", False, "ja_nein"),
    ("notes", "Hinweis", False, None),
]


def dropdown_lists(enums: dict[str, list[str]]) -> dict[str, list[str]]:
    """Anzeigewerte je Dropdown-Liste (für das 'Codelisten'-Blatt + Data-Validation)."""
    return {
        "phase": list(PHASE_LAYMEN.keys()),
        "tumor_entity_multi": list(enums["tumor_entity"]) + ["NSCLC,SCLC"],
        "datatype_laymen": list(DATATYPE_LAYMEN.keys()),
        "cardinality_laymen": list(CARDINALITY_LAYMEN.keys()),
        "binding_strength": list(enums["binding_strength"]),
        "guideline_source": list(enums["guideline_source"]),
        "recommendation_grade": list(enums["recommendation_grade"]),
        "system_laymen": list(SYSTEM_LAYMEN.keys()),
        "usage_laymen": list(USAGE_LAYMEN.keys()),
        "sector_laymen": list(SECTOR_LAYMEN.keys()),
        "ja_nein": list(JA_NEIN.keys()),
    }
