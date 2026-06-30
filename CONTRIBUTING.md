# Mitwirken am MiHUB-Patientenpfad-Datenelement-Repository

Vielen Dank für Ihr Interesse, das Datenelement-Repository mit Ihrer klinischen oder
methodischen Expertise zu erweitern. Es gibt **drei gleichwertige Wege** beizutragen —
wählen Sie den, der zu Ihnen passt. Alle drei landen am Ende als Pull Request auf dem
`dev`-Branch und werden dort fachlich und technisch geprüft.

## Welcher Weg passt zu mir?

| Weg | Für wen? | Was Sie brauchen | Aufwand | Sie liefern … |
| --- | --- | --- | --- | --- |
| 🟢 **1. GitHub-Issue-Formular** | Klinische Expert:innen, einzelne Vorschläge | nur einen (kostenlosen) GitHub-Account | 10–20 min / Element | ein ausgefülltes Web-Formular |
| 🟡 **2. Excel-Vorlage** | Klinische Expert:innen, **viele** Elemente am Stück, auch offline / im Workshop | Excel/LibreOffice/Numbers | je nach Menge | eine ausgefüllte `.xlsx`-Mappe |
| 🔵 **3. YAML + Pull Request** | Medizininformatiker:innen / technisch Versierte | Git, Editor, Python ≥ 3.10 | variabel | fertige YAML-Datei(en) + PR |

> **Kein YAML, kein Git, keine Programmierung nötig für Weg 1 und 2.** Das MI-Team übernimmt die
> technische Umsetzung (Codes, FHIR-Mappings) und bittet Sie am Ende, das Ergebnis inhaltlich zu
> bestätigen. Es ist **keine Schande**, einen niederschwelligen Weg zu nutzen — sie sind genau
> dafür gedacht.

---

### 🟢 Weg 1 — GitHub-Issue-Formular (niederschwellig, online)

→ [Issues → New Issue → „📋 Neues Datenelement vorschlagen"](../../issues/new/choose).
Ein Web-Formular mit Auswahllisten führt Sie durch alle Felder (Phase, Definition, Datentyp,
Trigger, Rolle, **Datennutzung WO/WER/WIE**, Leitlinien-Bezug). Felder, die das MI-Team selbst
recherchiert (z. B. SNOMED-Codes), dürfen leer bleiben. Nach dem Absenden prüft eine
automatische **Dubletten-Prüfung** den Vorschlag und kommentiert mögliche Treffer.

### 🟡 Weg 2 — Excel-Vorlage (viele Elemente, auch im Workshop)

→ [`templates/datenelement-erhebung.xlsx`](templates/README.md) herunterladen, das Blatt
**„Anleitung"** lesen und ausfüllen. Eine Zeile je Datenelement; die Datennutzung (System ·
Rolle · Nutzung) tragen Sie im zweiten Blatt ein. Mappe an `digital-health@tu-dresden.de`
senden oder an ein Issue anhängen. Das MI-Team importiert sie automatisch
(`scripts/import-elicitation-workbook.py`) zu YAML-Entwürfen und prüft auf Dubletten.

### 🔵 Weg 3 — YAML + Pull Request (technisch)

→ Ausführliche Schritt-für-Schritt-Anleitung in [`docs/howto-add-element.md`](docs/howto-add-element.md) (§B).

```bash
cd data-elements
python3 -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt                       # pyyaml + jsonschema (+ openpyxl für die Excel-Vorlage)

python scripts/validate.py                            # YAML gegen das JSON-Schema prüfen
python scripts/build-catalog.py                       # CSV + Markdown + Phasen-Übersicht regenerieren
python scripts/check-duplicates.py --candidates <neu.yaml>   # vor Aufnahme: Dubletten prüfen
```

---

## Allgemeine Regeln (alle Wege)

- Pro Pull Request möglichst **ein** Datenelement (atomare Reviews).
- Jedes Element braucht **mindestens eine Leitlinien-/Quellen-Referenz** (`evidence.guideline_references`).
- Alle Pflichtfelder (im CSV mit `*` markiert) müssen befüllt sein, bevor der PR gemergt wird.
- **Dubletten vermeiden:** neue Kandidaten vor Aufnahme gegen den Bestand prüfen
  (`scripts/check-duplicates.py` bzw. Skill [`check-duplicate-data-element`](skills/check-duplicate-data-element/SKILL.md)).
- Statuswechsel (`AuthorDraft → CommitteeDraft → ApprovedForProductionUse`) erfolgen je Element einzeln.
- Versions-Bumps folgen SemVer (siehe `docs/howto-add-element.md` §C).
- **Branching:** Beiträge gehen per Pull Request gegen **`dev`** (Integrations-/Review-Branch).
  **`main`** ist die Release-Branch — nicht direkt auf `main` pushen.

## Verhaltenskodex & Lizenz

Es gilt der [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md). Beiträge erfolgen unter **CC BY 4.0**
(Inhalte) bzw. **Apache 2.0** (Skripte unter `scripts/`). Bitte **keine** personenbezogenen oder
realen Patientendaten eintragen — nur die abstrakte Datenelement-Definition. Sensible klinische
Sachverhalte (z. B. Todeswunsch, Sterbephase, Suizidalität) werden mit besonderer Sorgfalt und
vertraulich behandelt. Zweckbestimmung/Haftung: [`DISCLAIMER.md`](DISCLAIMER.md).

## Bei Fragen

→ Issue „❓ Frage" oder Direktkontakt MI-Lead via [`.github/CODEOWNERS`](.github/CODEOWNERS).
