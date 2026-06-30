# HOWTO — Ein neues Datenelement aufnehmen

Diese Anleitung erklärt **Schritt für Schritt**, wie ein neu identifiziertes Datenelement in eine bestehende oder neue Versorgungsphase aufgenommen wird. Es gibt **drei gleichwertige Wege** — wählen Sie den für Sie passenden (Vergleichstabelle: [`../CONTRIBUTING.md`](../CONTRIBUTING.md)):

- **🟢 Klinik-Spur · Issue (niederschwellig):** Sie befüllen ein Web-Formular auf GitHub. Das MI-Team übernimmt die technische Umsetzung. → **Abschnitt A** unten.
- **🟡 Klinik-Spur · Excel (viele Elemente, auch offline/Workshop):** Sie füllen eine Excel-Mappe aus; das MI-Team importiert sie automatisch. → **Abschnitt A2** unten.
- **🔵 MI-Spur · YAML (vollständig):** Sie editieren das YAML direkt, validieren lokal und öffnen einen Pull Request. → **Abschnitt B** unten.

Welcher Weg genutzt wurde, ist im PR-Template festgehalten — **alle drei** sind legitim. Vor der
Aufnahme prüft das MI-Team neue Kandidaten auf **Dubletten** (`scripts/check-duplicates.py` bzw.
Skill [`check-duplicate-data-element`](../skills/check-duplicate-data-element/SKILL.md)).

---

## A · Klinik-Spur (ohne YAML, ohne Git)

**Voraussetzung:** GitHub-Account (kostenfrei). Sonst nichts.

### Schritt A1 — Issue „Neues Datenelement vorschlagen" anlegen

Im Repository **„Issues" → „New Issue" → Vorlage „📋 Neues Datenelement vorschlagen"** wählen. Es öffnet sich ein Web-Formular mit Pflichtfeldern:

- **Phase** (Auswahlliste: Nachsorge / Surveillance / Palliativ / *neue Phase*)
- **Bezeichnung (Deutsch)** — z. B. „Schluckbeschwerden (NRS)"
- **Klinische Definition** — Freitext, 1–3 Sätze
- **Tumorentität(en)** — NSCLC / SCLC / unspezifisch
- **Datentyp (laienverständlich)** — Auswahl: Ja/Nein, Skalenwert, Datum, Codierter Begriff, Freitext, Dosis, Verweis auf Dokument
- **Wann/wer erfasst es?** — Trigger + Frequenz + verantwortliche Rolle
- **Leitlinien-Bezug** — Quelle + Kapitel/Empfehlungs-Nummer (Pflicht!)
- **Optional:** Codierungs-Wunsch (SNOMED/LOINC/ICD), Beziehungen zu anderen Elementen, Hinweis auf MII/oBDS/MIO

### Schritt A2 — Triage durch MI-Team

Das MI-Team bekommt das Issue automatisch zugewiesen (CODEOWNERS), prüft Vollständigkeit, fragt nach, sucht passende Codes (SNOMED/LOINC/ICD), legt Standard-Mappings fest.

### Schritt A3 — Konvertierung Issue → YAML → PR

Das MI-Team konvertiert das Issue in ein valides YAML (siehe §B), öffnet einen PR, **markiert die Klinik-Spur-Person als Reviewer:in für inhaltliche Bestätigung**. Sie reviewen den Klartext-Diff, geben „Approve". Fertig.

> **Aufwand für Klinik-Person: 10–20 min pro Element (Formular ausfüllen + späteres Approve im PR).** Kein YAML, kein `git`, keine CLI.

---

## A2 · Excel-Spur (ohne Git, viele Elemente)

**Voraussetzung:** Excel, LibreOffice Calc oder Numbers. Kein GitHub-Account nötig.

Ideal, wenn Sie **mehrere Datenelemente am Stück** erheben (z. B. in einem Stakeholder-Workshop)
oder lieber offline arbeiten.

### Schritt A2.1 — Vorlage holen

`templates/datenelement-erhebung.xlsx` herunterladen (siehe [`../templates/README.md`](../templates/README.md)).
Die Dropdown-Listen sind aus dem Schema erzeugt — Sie wählen also immer gültige Werte.

### Schritt A2.2 — Ausfüllen

- Blatt **»Anleitung«** lesen. Jedes Blatt hat oben eine **grau-kursive Beispielzeile**
  (lokale ID = `BEISPIEL`), die eine vollständige Erfassung zeigt und **beim Import ignoriert wird**
  (überschreiben oder löschen). Spalten-Erklärungen erscheinen als Kommentar in der Kopfzeile.
- Blatt **»Datenelemente«**: eine Zeile je Element; Pflichtspalten sind rosa hinterlegt und mit `*`
  markiert; Dropdowns nutzen. Vergeben Sie je Zeile eine kurze **lokale ID** (z. B. `DE-001`).
- Blatt **»Datennutzung«**: WO (System) · WER (Rolle) · WIE (Nutzung) — mehrere Zeilen je
  Datenelement, verknüpft über die lokale ID. Beispiel »Rauchstatus«: PVS · Hausärzt:in · erfasst;
  KIS · Onkolog:in · gelesen; Forschungs-DWH · Forscher:in · Forschung.
- Blatt **»Codes«** (optional): bekannte Codes je Element — **Terminologie-System** (SNOMED CT,
  LOINC, ICD-10-GM …) als Dropdown, dazu Code + Anzeigetext.
- Felder, die Sie nicht kennen (z. B. SNOMED-Codes, Standard-Mapping), dürfen leer bleiben.

### Schritt A2.3 — Abgeben

Mappe an `digital-health@tu-dresden.de` senden oder an ein GitHub-Issue anhängen.

### Schritt A2.4 — MI-Team: Import (technisch)

```bash
pip install openpyxl
python scripts/import-elicitation-workbook.py ausgefuellt.xlsx --validate   # -> elements/_incoming/*.yaml (Entwürfe)
python scripts/check-duplicates.py --candidates elements/_incoming/         # Dubletten prüfen
```

Die Entwürfe (`publication_status: AuthorDraft`) werden vom MI-Team um Codes/Mappings ergänzt,
dann nach `elements/<phase>/` verschoben und wie in §B per PR auf `dev` eingebracht.

> **Aufwand für Klinik-Person:** Mappe ausfüllen — kein `git`, kein YAML, keine CLI.

---

## B · MI-Spur (YAML + Git + PR)

**Voraussetzung:** Git-Grundlagen, Editor mit YAML-Highlighting (z. B. VS Code), Python ≥ 3.10.

### Schritt B1 — Repository klonen + Python-Umgebung einrichten

```bash
git clone <repo-url>
cd data-elements

# einmaliges Setup einer isolierten Python-Umgebung (.venv ist gitignored)
python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt      # pyyaml + jsonschema
```

Bei späteren Terminal-Sessions reicht `source .venv/bin/activate`.

### Schritt B2 — Branch anlegen

```bash
git checkout -b feat/<phase>/<elementName>
# Beispiel: git checkout -b feat/palliative/dysphagiaIntensity
```

### Schritt B3 — Vorlage kopieren

```bash
cp schemas/TEMPLATE.element.yaml elements/<phase>/<elementName>.yaml
```

`<phase>` ist `follow-up`, `surveillance`, `palliative` (oder eine neue Phase, siehe §D).
`<elementName>` ist der camelCase-Name aus dem Schema-Pattern, z. B. `dysphagiaIntensity`.

### Schritt B4 — Felder befüllen

Pflichtfelder (Schema `required`, im CSV mit `*` markiert):

| Feld | Was eintragen |
| --- | --- |
| `id` | `mihub.lung.<phase>.<elementName>.v0.1` |
| `uuid` | mit `uuidgen` neu erzeugen |
| `name` | technischer camelCase-Name (identisch mit Dateiname ohne `.yaml`) |
| `label_de` | klinisch verständliche deutsche Bezeichnung |
| `definition_de` | semantische Definition (1–3 Sätze) |
| `phase` | `followup`, `surveillance` oder `palliative` |
| `datatype` | aus dem Schema-Enum (z. B. `integer`, `CodeableConcept`, `Quantity`) |
| `cardinality` | `0..1`, `1..1`, `0..*`, `1..*` |
| `iso13972_metadata.version_number` | `0.1.0` für Erstanlage |
| `iso13972_metadata.creation_date` | heutiges Datum, ISO-Format `YYYY-MM-DD` |
| `iso13972_metadata.publication_status` | `AuthorDraft` für Erstanlage |
| `iso13972_metadata.publisher` | `MiHUB Konsortium AP8` |
| `iso13972_metadata.language` | `[de, en]` |
| `provenance.created_by` | Ihr Name |

Empfohlene Felder (im CSV mit `+` markiert):

- `tumor_entity` (NSCLC, SCLC oder lung_cancer_any)
- `value_set` mit mind. einem Beispiel-Coding (SNOMED CT bevorzugt; LOINC für Skalen; ICD-10-GM für Diagnosen)
- `standard_mappings` — mind. ein Eintrag (`fhir-mii-kds`, `fhir-r4-base`, `obds`, `kbv-mio`, `openehr-archetype`, …)
- `care_process` (`trigger`, `frequency_pattern`, `responsible_role`)
- `care_process.data_flows[]` — **WO/WER/WIE**: je Eintrag `system` (PVS/KIS/…), `actor_role`, `usage_type` (capture/read/…), optional `sector`/`mandatory`. Mehrere Einträge je Element (z. B. Hausarzt erfasst im PVS, Onkolog:in liest im KIS). Beispiel: `elements/follow-up/smokingStatus.yaml`.
- `evidence.guideline_references` mit mind. einer LL-Quelle + Kapitel/Empfehlungs-Nr.
- `iso13972_metadata.type` (`observation`, `procedure`, `evaluation`, `plan`, `condition`, `medication`, `social`)

### Schritt B5 — Lokal validieren

```bash
python scripts/validate.py elements/<phase>/<elementName>.yaml
```

Ergebnis muss `OK` sein. Bei `FAIL` zeigt das Skript den Pfad und die Schema-Verletzung.

### Schritt B6 — Catalog regenerieren

```bash
python scripts/build-catalog.py
```

Aktualisiert `catalog/data-dictionary.csv` (24 Spalten). **Diese CSV gehört in den Commit** — die CI bricht sonst ab.

### Schritt B6.5 — Dubletten prüfen

```bash
python scripts/check-duplicates.py --candidates elements/<phase>/<elementName>.yaml
```

Bei Einstufung `DUBLETTE`/`NAH-DUBLETTE`: bestehendes Element verfeinern statt neu anlegen; bei
`VERWANDT`: per `related_elements[]` verlinken. (Heuristik — Letztentscheidung beim Menschen.)

### Schritt B7 — Commit & Push & PR (gegen `dev`)

```bash
git add elements/<phase>/<elementName>.yaml catalog/data-dictionary.csv
git commit -m "feat(<phase>): add <elementName> (Quelle: <LL>)"
git push -u origin feat/<phase>/<elementName>
```

Auf GitHub einen **Pull Request gegen den `dev`-Branch** öffnen (nicht `main`), PR-Template
ausfüllen, klinische:n Reviewer:in markieren. **`main`** ist die Release-Branch.

---

## C · Bestehendes Element ändern

Drei Fälle:

| Änderung | Versions-Bump | Status |
| --- | --- | --- |
| Tippfehler / Doku-Klarstellung | `0.1.0 → 0.1.1` (Patch) | gleich |
| Neues Coding / neues Standard-Mapping / `binding_strength` lockern | `0.1.0 → 0.2.0` (Minor, additive) | ggf. weiter |
| Datentyp/Bezeichnung/Definition geändert (semantischer Bruch) | `0.1.0 → 1.0.0` (Major) | neue ID, alte als `Superseded` markieren, mit `related_elements: [{relation: supersededBy, target: ...}]` verlinken |

Major-Änderungen erzeugen **immer ein neues Element** mit neuer ID (`...v1.0`), weil bestehende Daten gegen `v0.x` weiter auflösbar bleiben müssen.

---

## D · Neue Versorgungsphase aufnehmen

Wenn z. B. eine Phase „Rehabilitation" oder „Diagnostik" ergänzt werden soll, sind **fünf Stellen** zu ändern:

1. `schemas/data-element.schema.json` — Enum `phase` und `tumor_entity` ergänzen, ID-Pattern erweitern.
2. `elements/<neue-phase>/` Ordner anlegen.
3. `scripts/build-catalog.py` & `docs/phases-overview.md` — Generator kennt automatisch alle Unterordner; nur ggf. Beschreibungstext der neuen Phase im Phasen-Overview-Generator pflegen.
4. `.github/CODEOWNERS` — Reviewer:in für die neue Phase eintragen.
5. `README.md` — Repository-Struktur-Tabelle aktualisieren.

Schritt 1 ist die einzige Stelle, an der das Schema selbst betroffen ist — daher ist eine Phasen-Erweiterung eine **Minor-Schema-Version** (alle alten YAMLs bleiben gültig).

---

## E · Hilfsmittel & Tipps

- **VS Code mit YAML-Erweiterung:** Im YAML oben eine Zeile `# yaml-language-server: $schema=../../schemas/data-element.schema.json` ergänzen — VS Code zeigt dann Tooltips, Validierung in Echtzeit und Autocomplete für Enums.
- **Beispiel-Element als Vorlage:** Der einfachste Einstieg ist `cp elements/follow-up/smokingStatus.yaml elements/<phase>/<neu>.yaml` und dann anpassen — das Element ist „typisch" und enthält alle wichtigen Strukturen.
- **Codes nachschlagen:** SNOMED CT via [browser.ihtsdotools.org](https://browser.ihtsdotools.org/) (Edition: Germany), LOINC via [loinc.org/search](https://loinc.org/search/), ICD-10-GM via [BfArM](https://www.bfarm.de/DE/Kodiersysteme/Klassifikationen/ICD/ICD-10-GM/_node.html).
- **Bei Unsicherheit „extensible" wählen:** Das `binding_strength` `extensible` ist die robusteste Default-Wahl, wenn kein etabliertes ValueSet exakt passt.

---

## F · Was passiert, wenn ich es trotzdem nicht hinkriege?

→ Issue eröffnen mit der Klinik-Spur-Vorlage (§A). Das MI-Team übernimmt. Es ist **keine** Schande, die Klinik-Spur zu nutzen — sie ist explizit für klinische Expertise gedacht, nicht für YAML-Akrobatik.
