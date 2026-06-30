# Erhebungs-Vorlagen (Klinik-Spur ohne Git/YAML)

Dieses Verzeichnis enthält die **Excel-Vorlage**, mit der klinische Expert:innen neue
Datenelemente für den Lungenkrebs-Patientenpfad vorschlagen können — **ohne GitHub und
ohne YAML**. Sie ist eine von **drei gleichwertigen Beitrags-Spuren**; siehe
[`../CONTRIBUTING.md`](../CONTRIBUTING.md) für den Vergleich (Issue · Excel · YAML).

| Datei | Zweck |
| --- | --- |
| [`datenelement-erhebung.xlsx`](datenelement-erhebung.xlsx) | Ausfüll-Vorlage (Anleitung + Datenelemente + Datennutzung + Codelisten). Dropdowns sind aus dem JSON-Schema generiert. |

## Für klinische Beitragende

1. `datenelement-erhebung.xlsx` herunterladen und öffnen (Excel, LibreOffice oder Numbers).
2. Blatt **»Anleitung«** lesen, dann **»Datenelemente«** ausfüllen (eine Zeile je Element;
   Pflichtspalten sind rot hinterlegt und mit `*` markiert; Dropdown-Felder aus der Liste wählen).
3. Im Blatt **»Datennutzung«** je Datenelement eintragen, **wo** (System), **wer** (Rolle) und
   **wie** (erfasst/gelesen/…) es genutzt wird — verknüpft über die »lokale ID« (z. B. `DE-001`).
4. Mappe per E-Mail an `digital-health@tu-dresden.de` senden oder an einem GitHub-Issue anhängen.

> Bitte **keine** personenbezogenen oder realen Patientendaten eintragen — nur die abstrakte
> Datenelement-Definition. Beiträge erfolgen unter **CC BY 4.0**.

## Für das MI-Team (technisch)

Die Vorlage ist **schema-getrieben** — alle Dropdowns stammen aus
[`../schemas/data-element.schema.json`](../schemas/data-element.schema.json) bzw. den
laienverständlichen Abbildungen in [`../scripts/_elicitation.py`](../scripts/_elicitation.py)
und können daher nicht vom Schema abdriften.

```bash
pip install openpyxl                                  # einmalig (nicht in der CI nötig)

# Vorlage (neu) erzeugen — z. B. nach Schema-Änderungen:
python scripts/build-elicitation-workbook.py         # -> templates/datenelement-erhebung.xlsx

# Ausgefüllte Mappe -> YAML-Entwürfe (Staging, gitignored unter elements/_incoming/):
python scripts/import-elicitation-workbook.py ausgefuellt.xlsx --validate

# Dubletten gegen den Bestand prüfen, BEVOR Entwürfe übernommen werden:
python scripts/check-duplicates.py --candidates elements/_incoming/
```

Die importierten YAMLs sind **Entwürfe** (`publication_status: AuthorDraft`): Codes,
Standard-Mappings und die finale Definition ergänzt das MI-Team, bevor die Datei nach
`elements/<phase>/` wandert und per Pull Request auf `dev` geht.
