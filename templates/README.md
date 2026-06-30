# Erhebungs-Vorlagen (Klinik-Spur ohne Git/YAML)

Dieses Verzeichnis enthält die **Excel-Vorlage**, mit der klinische Expert:innen neue
Datenelemente für den Lungenkrebs-Patientenpfad vorschlagen können — **ohne GitHub und
ohne YAML**. Sie ist eine von **drei gleichwertigen Beitrags-Spuren**; siehe
[`../CONTRIBUTING.md`](../CONTRIBUTING.md) für den Vergleich (Issue · Excel · YAML).

| Datei | Zweck |
| --- | --- |
| [`datenelement-erhebung.xlsx`](datenelement-erhebung.xlsx) | Ausfüll-Vorlage mit Blättern **Anleitung · Datenelemente · Datennutzung · Codes · Codelisten**. Selbsterklärend: Anleitung, Spalten-Kommentare (Mauszeiger über Kopfzeile), Pflicht-Markierung und eine **Beispielzeile**. Dropdowns sind aus dem JSON-Schema generiert. |

## Für klinische Beitragende

1. `datenelement-erhebung.xlsx` herunterladen und öffnen (Excel, LibreOffice oder Numbers).
2. Blatt **»Anleitung«** lesen. Jedes Blatt enthält oben eine **grau-kursive Beispielzeile**
   (lokale ID = `BEISPIEL`) — sie zeigt eine vollständige Erfassung und **wird beim Import
   ignoriert** (gerne überschreiben oder löschen).
3. Blatt **»Datenelemente«** ausfüllen (eine Zeile je Element; Pflichtspalten sind rosa hinterlegt
   und mit `*` markiert; Dropdown-Felder aus der Liste wählen; Spalten-Erklärung per Kommentar in
   der Kopfzeile). Je Zeile eine kurze **»lokale ID«** (z. B. `DE-001`) vergeben.
4. Optional Blatt **»Datennutzung«** (WO/System · WER/Rolle · WIE/Nutzung) und Blatt **»Codes«**
   (bekannte Codes inkl. **Terminologie-System** als Dropdown) je lokale ID befüllen.
5. Mappe per E-Mail an `digital-health@tu-dresden.de` senden oder an einem GitHub-Issue anhängen.

> Was Sie nicht wissen (z. B. SNOMED-Codes, Standard-Mapping), darf leer bleiben — das MI-Team
> recherchiert es. Bitte **keine** personenbezogenen oder realen Patientendaten eintragen — nur die
> abstrakte Datenelement-Definition. Beiträge erfolgen unter **CC BY 4.0**.

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
