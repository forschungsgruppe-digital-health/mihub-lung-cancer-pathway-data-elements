# SPDX-License-Identifier: Apache-2.0
"""Gemeinsame Definitionen für die Excel-Erhebungs-Vorlage (Klinik-Spur ohne Git/YAML).

Single source of truth für:
  - die Spalten der Erhebungs-Tabellen ("Datenelemente", "Datennutzung", "Codes"),
  - die (teils laienverständlichen) Dropdown-Werte und ihre Abbildung auf die Schema-Enums,
  - die Beispielzeile (wird beim Import ignoriert) und die Spalten-Hilfetexte.

Wird von `build-elicitation-workbook.py` (Vorlage erzeugen) UND
`import-elicitation-workbook.py` (ausgefüllte Vorlage → YAML-Entwürfe) importiert, damit beide
nie auseinanderlaufen. Die Schema-Enums werden zur Laufzeit direkt aus
`schemas/data-element.schema.json` gelesen — sie sind also nur an EINER Stelle gepflegt.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schemas" / "data-element.schema.json"

# Zeilen mit dieser lokalen ID (Präfix) sind BEISPIELE und werden beim Import ignoriert.
EXAMPLE_LOCAL_ID = "BEISPIEL"


def is_example(local_id: Any) -> bool:
    """True, wenn die Zeile eine Beispielzeile ist (local_id beginnt mit 'BEISPIEL')."""
    return str(local_id or "").strip().upper().startswith(EXAMPLE_LOCAL_ID)


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

# --- Vorschlagslisten (Dropdown UND Freitext erlaubt) ------------------------
# Terminologie-Systeme für das Blatt "Codes" (entspricht value_set.codings[].system).
TERMINOLOGY_SYSTEMS: list[str] = [
    "snomed-ct", "loinc", "icd-10-gm", "icd-o-3", "icf", "ops", "kdl",
    "atc", "ucum", "hl7-v3", "meddra", "local-no-standard-binding",
]
UNIT_SUGGESTIONS: list[str] = [
    "mg", "mg/d", "g", "mm", "cm", "%", "/min", "mo", "ml", "kg", "score", "Punkte",
    "mmHg", "µmol/L", "U/L", "Gy", "ng/mL",
]
FREQUENCY_SUGGESTIONS: list[str] = [
    "per-encounter", "ad-hoc", "einmalig", "weekly", "monthly",
    "Q3M", "Q6M", "Q12M", "Q3M-Y1-Y2;Q6M-Y3-Y5",
]
ROLE_SUGGESTIONS: list[str] = [
    "Onkolog:in", "Hausärzt:in", "Pflegefachperson", "Palliativteam",
    "Tumorboard / MDT", "Tumordokumentar:in", "Radiolog:in", "Patholog:in",
    "Patient:in (Selbsteinschätzung)",
]
EVIDENCE_LEVELS: list[str] = ["1a", "1b", "2a", "2b", "3", "4", "n/a"]

# Dropdowns, die zusätzlich Freitext erlauben (Vorschlag statt Zwang).
SUGGESTION_LISTS: set[str] = {
    "tumor_entity_multi", "unit_suggest", "frequency_suggest", "role_suggest",
    "evidence_levels", "terminology_system",
}


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


# --- Spalten der Erhebungs-Tabellen ------------------------------------------
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
    ("unit", "Einheit_UCUM", False, "unit_suggest"),
    ("trigger", "Wann_erfasst_Trigger*", True, None),
    ("frequency_pattern", "Erhebungsfrequenz", False, "frequency_suggest"),
    ("responsible_role", "Verantwortliche_Rolle*", True, "role_suggest"),
    ("binding_strength", "Binding-Stärke", False, "binding_strength"),
    ("standard_binding_status", "Standard-Bindungs-Status", False, "standard_binding_status"),
    ("standard_primary", "Standard-Mapping_(primär)", False, "standard"),
    ("guideline_source", "Leitlinien-Quelle*", True, "guideline_source"),
    ("guideline_section", "Kapitel/Empfehlung/Tabelle*", True, None),
    ("recommendation_grade", "Empfehlungsgrad", False, "recommendation_grade"),
    ("evidence_level", "Evidenzlevel", False, "evidence_levels"),
    ("notes", "Anmerkungen/Beziehungen", False, None),
    ("contact", "Kontakt_für_Rückfragen", False, None),
]

FLOW_COLUMNS: list[tuple[str, str, bool, str | None]] = [
    ("local_id", "lokale_ID_des_Datenelements*", True, None),
    ("label_hint", "Bezeichnung_(zur_Orientierung)", False, None),
    ("system", "System_WO*", True, "system_laymen"),
    ("system_label", "System_Klartext_(bei_Sonstiges)", False, None),
    ("actor_role", "Rolle_WER", False, "role_suggest"),
    ("usage_type", "Nutzung_WIE*", True, "usage_laymen"),
    ("sector", "Sektor", False, "sector_laymen"),
    ("mandatory", "Pflicht?", False, "ja_nein"),
    ("notes", "Hinweis", False, None),
]

# Blatt "Codes" — value_set.codings[]; mehrere Zeilen je Datenelement (über local_id verknüpft).
CODE_COLUMNS: list[tuple[str, str, bool, str | None]] = [
    ("local_id", "lokale_ID_des_Datenelements*", True, None),
    ("label_hint", "Bezeichnung_(zur_Orientierung)", False, None),
    ("terminology_system", "Terminologie-System*", True, "terminology_system"),
    ("code", "Code*", True, None),
    ("display", "Anzeigetext_(Display)", False, None),
]

# --- Spalten-Hilfetexte (werden als Zell-Kommentare in die Kopfzeile gesetzt) ---
HELP: dict[str, str] = {
    "local_id": "Kurze freie ID je Zeile (z. B. DE-001). Dient nur zur Verknüpfung mit den Blättern "
                "»Datennutzung« und »Codes«. Zeilen mit ID 'BEISPIEL' werden beim Import ignoriert.",
    "label_de": "Klinisch verständliche deutsche Kurzbezeichnung (z. B. 'Rauchstatus').",
    "definition_de": "Was genau wird gemessen/dokumentiert? 1–3 Sätze; Skala, Zeitraum, Ein-/Ausschluss.",
    "phase": "Versorgungsphase — aus der Liste wählen. 'Andere' → Spalte »Phase_falls_andere« nutzen.",
    "tumor_entity": "NSCLC, SCLC, lung_cancer_any oder 'NSCLC,SCLC'. Vorschlag — Freitext erlaubt.",
    "datatype": "Welcher Werttyp wird erfasst? Laienverständliche Auswahl; das MI-Team mappt auf FHIR-Typen.",
    "cardinality": "Wie oft pro Patient:in? Aus der Liste wählen.",
    "unit": "UCUM-Einheit, falls Zahl/Dosis (z. B. mg, mm, %). Vorschlag — Freitext erlaubt; sonst leer.",
    "trigger": "Wann/durch welches Ereignis wird erfasst? (z. B. 'bei jeder Vorstellung').",
    "frequency_pattern": "Erhebungsfrequenz. Vorschlag — Freitext erlaubt (z. B. per-encounter, Q3M).",
    "responsible_role": "Primär verantwortliche Rolle. Vorschlag — Freitext erlaubt. Mehrere Rollen/Systeme: Blatt »Datennutzung«.",
    "binding_strength": "Nur falls codierter Begriff: Verbindlichkeit der Codeliste. Im Zweifel leer (MI-Team).",
    "standard_binding_status": "Status der Standard-Codierung. Im Zweifel leer lassen (MI-Team).",
    "standard_primary": "Primäres Ziel-Standard-Mapping (z. B. fhir-mii-kds, obds, kbv-mio). Optional; MI-Team ergänzt.",
    "guideline_source": "Belegende Leitlinie/Quelle — aus der Liste wählen (Pflicht).",
    "guideline_section": "Kapitel / Empfehlungs-Nr. / Tabelle in der Quelle (Pflicht).",
    "recommendation_grade": "Empfehlungsgrad lt. Leitlinie (A/B/0/EK/Statement/n/a). Optional.",
    "evidence_level": "Evidenzlevel (1a…4, n/a). Vorschlag — Freitext erlaubt. Optional.",
    "notes": "Beziehungen zu anderen Elementen, Sensitivitäts-Hinweise, offene Fragen.",
    "contact": "Name + Klinik/Fachgesellschaft für Rückfragen. Optional.",
    "system": "WO wird das Datenelement genutzt (Systemklasse)? Aus der Liste wählen.",
    "system_label": "Konkreter Produktname, v. a. bei 'Sonstiges' (z. B. 'Onkostar').",
    "actor_role": "WER nutzt es in diesem System (Rolle)? Vorschlag — Freitext erlaubt.",
    "usage_type": "WIE wird es genutzt? (erfasst/gelesen/…). Aus der Liste wählen.",
    "sector": "Versorgungssektor dieses Datenflusses.",
    "mandatory": "Ist die Nutzung in diesem System verpflichtend (z. B. Meldepflicht)?",
    "terminology_system": "Codesystem des Codes — aus der Liste wählen (snomed-ct, loinc, icd-10-gm, …). "
                          "Unbekannt? Zeile leer lassen, das MI-Team recherchiert.",
    "code": "Der Code im gewählten Terminologie-System (z. B. SNOMED 77176002).",
    "display": "Klartext/Anzeigetext zum Code (z. B. 'Smoker').",
    "label_hint": "Nur zur Orientierung — welches Datenelement (Bezeichnung).",
}


def dropdown_lists(enums: dict[str, list[str]]) -> dict[str, list[str]]:
    """Anzeigewerte je Dropdown-Liste (für das 'Codelisten'-Blatt + Data-Validation)."""
    return {
        "phase": list(PHASE_LAYMEN.keys()),
        "tumor_entity_multi": list(enums["tumor_entity"]) + ["NSCLC,SCLC"],
        "datatype_laymen": list(DATATYPE_LAYMEN.keys()),
        "cardinality_laymen": list(CARDINALITY_LAYMEN.keys()),
        "binding_strength": list(enums["binding_strength"]),
        "standard_binding_status": list(enums["standard_binding_status"]),
        "standard": list(enums["standard"]),
        "guideline_source": list(enums["guideline_source"]),
        "recommendation_grade": list(enums["recommendation_grade"]),
        "system_laymen": list(SYSTEM_LAYMEN.keys()),
        "usage_laymen": list(USAGE_LAYMEN.keys()),
        "sector_laymen": list(SECTOR_LAYMEN.keys()),
        "ja_nein": list(JA_NEIN.keys()),
        "terminology_system": list(TERMINOLOGY_SYSTEMS),
        "unit_suggest": list(UNIT_SUGGESTIONS),
        "frequency_suggest": list(FREQUENCY_SUGGESTIONS),
        "role_suggest": list(ROLE_SUGGESTIONS),
        "evidence_levels": list(EVIDENCE_LEVELS),
    }


# --- Beispielzeile (wird beim Import ignoriert; demonstriert eine vollständige Erfassung) ---
EXAMPLE_ELEMENT: dict[str, str] = {
    "local_id": EXAMPLE_LOCAL_ID,
    "label_de": "Rauchstatus",
    "definition_de": "Aktueller Tabakkonsumstatus inkl. E-Zigarette und Passivrauchexposition.",
    "phase": "Onkologische Nachsorge (kurativ behandelt)",
    "phase_other": "",
    "tumor_entity": "NSCLC,SCLC",
    "datatype": "Codierter Begriff aus Liste (SNOMED/ICD/LOINC)",
    "cardinality": "Genau einmal (Pflicht)",
    "unit": "",
    "trigger": "bei jeder Vorstellung",
    "frequency_pattern": "per-encounter",
    "responsible_role": "Onkolog:in",
    "binding_strength": "required",
    "standard_binding_status": "mapped",
    "standard_primary": "fhir-mii-kds",
    "guideline_source": "S3-LL Lungenkarzinom",
    "guideline_section": "Empf. 16.3",
    "recommendation_grade": "B",
    "evidence_level": "2b",
    "notes": "BEISPIELZEILE — wird beim Import ignoriert; bitte überschreiben oder löschen.",
    "contact": "",
}

EXAMPLE_FLOWS: list[dict[str, str]] = [
    {"local_id": EXAMPLE_LOCAL_ID, "label_hint": "Rauchstatus",
     "system": "Primärverwaltungssystem / Praxis-VS (PVS)", "system_label": "",
     "actor_role": "Hausärzt:in", "usage_type": "erfasst / eingegeben",
     "sector": "ambulant", "mandatory": "Nein", "notes": "BEISPIEL — wird ignoriert"},
    {"local_id": EXAMPLE_LOCAL_ID, "label_hint": "Rauchstatus",
     "system": "Krankenhausinformationssystem (KIS/AIS)", "system_label": "",
     "actor_role": "Onkolog:in", "usage_type": "gelesen / eingesehen",
     "sector": "stationär", "mandatory": "Nein", "notes": ""},
]

EXAMPLE_CODES: list[dict[str, str]] = [
    {"local_id": EXAMPLE_LOCAL_ID, "label_hint": "Rauchstatus",
     "terminology_system": "snomed-ct", "code": "77176002", "display": "Smoker"},
    {"local_id": EXAMPLE_LOCAL_ID, "label_hint": "Rauchstatus",
     "terminology_system": "snomed-ct", "code": "8517006", "display": "Ex-smoker"},
]
