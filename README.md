# Datenelemente Lungenkrebs (MiHUB)

> **Strukturiertes, versionierbares Repository der klinischen Datenelemente entlang der Lungenkrebs-Patient Journey** im Rahmen des Medical Informatics Hub (MiHUB). Die Datenelemente operationalisieren den in [`mihub-lung-cancer-pathway`](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway) (AP3) modellierten BPMN-Patientenpfad und werden in den Use-Case-Arbeitspaketen **AP6 (Krebsfrüherkennung)**, **AP7 (Kooperative Krebsversorgung _einschließlich Palliativversorgung_)** und **AP8 (Nachsorge und Langzeitbegleitung _einschließlich Palliativversorgung_)** erhoben — in der Wortwahl der drei strategischen Use-Cases des MiHUB-Antrags.

[![Lizenz Inhalte: CC BY 4.0](https://img.shields.io/badge/Lizenz%20Inhalte-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Lizenz Skripte: Apache 2.0](https://img.shields.io/badge/Lizenz%20Skripte-Apache%202.0-lightgrey.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Projekt: MiHUB](https://img.shields.io/badge/Projekt-MiHUB-blue)](https://mihubx.de/mihub/)
[![Projekt: MII](https://img.shields.io/badge/Projekt-MII-blue)](https://www.medizininformatik-initiative.de/)
[![Erstellung: KI-gestützt](https://img.shields.io/badge/Erstellung-KI--gest%C3%BCtzt-yellow)](AI_USAGE.md)

> ⚠️ **Author Draft v0.1 — KI-gestützt erstellt.** Inhalte sind als Entwurf zu betrachten und vor produktivem Einsatz klinisch zu reviewen — siehe [`AI_USAGE.md`](AI_USAGE.md). Pflege erfolgt über konsens-basierte, werkzeug-unabhängige Skills/Sub-Agenten — siehe [`AGENTS.md`](AGENTS.md).

> ⚠️ **Hinweis zur Zweckbestimmung / Haftungsausschluss.** Diese Datenelemente sind ein **Forschungs-, Lehr- und Interoperabilitäts-Referenzartefakt** (klinisches Informationsmodell / Datenkatalog), **nicht klinisch validiert** und **nicht** für die unmittelbare Patient:innenversorgung oder klinische Entscheidungsfindung bestimmt. Die Autor:innen weisen ihnen **keine medizinische Zweckbestimmung** im Sinne der EU-MDR (2017/745) zu. Es gelten [`DISCLAIMER.md`](DISCLAIMER.md) und Abschnitt 5 der [`LICENSE`](LICENSE).
>
> _These data elements are a research, education and interoperability-reference artifact — an author draft, **not** clinically validated and **not** for direct patient care. No medical intended purpose under EU MDR 2017/745. See [`DISCLAIMER.md`](DISCLAIMER.md)._

---

## Projektkontext

Dieses Repository ist Teil des [**Medical Informatics Hub (MiHUB)**](https://mihubx.de/mihub/), einem Digitalen FortschrittsHub (DigiHub) der [Medizininformatik-Initiative (MII)](https://www.medizininformatik-initiative.de/) des Bundesministeriums für Forschung, Technologie und Raumfahrt (BMFTR). MiHUB hat das Ziel, eine intersektorale, serviceorientierte Infrastruktur zur Verbesserung der sektorenübergreifenden Versorgung und Forschung in der Onkologie aufzubauen. Das übergreifende Anwendungsszenario ist die **Versorgung von Lungenkrebspatient:innen** entlang einer vollständigen Patient Journey – von der Früherkennung über Diagnostik und Behandlung bis hin zu Nachsorge und Langzeitbegleitung.

Konsortialführer ist die Technische Universität Dresden (Zentrum für Medizinische Informatik, ZMI). Weitere Konsortialpartner sind die Medizinische Universität Lausitz – Carl Thiem (Cottbus), das Klinikum Chemnitz und die Hochschule Mittweida. MiHUB kooperiert eng mit anderen DigiHubs im Rahmen des Cross-Hub Use Case _„Digitale Unterstützung in komplexen Patientenpfaden"_ am Beispiel Lungenkrebs.

Die Entwicklung folgt **drei strategischen Use Cases** (MiHUB-Antrag, §3 Overall Objectives):

1. **Prävention / Lungenkrebsfrüherkennung** (AP6)
2. **Kooperative Krebsversorgung — einschließlich Palliativversorgung** (AP7; explizit für Patient:innen in fortgeschrittener und palliativer Lungenkrebsversorgung)
3. **Nachsorge / Langzeitbegleitung — einschließlich Palliativversorgung** (AP8)

Diese drei Use Cases adressieren unterschiedliche Stadien der übergreifenden Patient Journey. **Palliativversorgung** ist im Antrag explizit in beiden Use-Case-Strängen verankert (Abbildung 1: „Treatment > Palliative Care" und „Aftercare > Palliative Care") und ist zudem als eine der modellierten Phasen des AP3-Pfads (_„screening, treatment, follow-up, palliative, and primary care"_) Teil der Patient-Journey-Modellierung.

Während das Schwester-Repository [`mihub-lung-cancer-pathway`](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway) die Patient Journey **prozessual** als BPMN-Modell beschreibt, beschreibt **dieses** Repository die **inhaltliche** Seite — also welche klinischen Daten an den Aktivitäten und Übergängen des Pfads erhoben, ausgetauscht und sekundär genutzt werden. Beide Artefakte sind komplementär: Der BPMN-Pfad legt fest *wann und durch wen* etwas geschieht; die Datenelemente legen fest *was dabei dokumentiert wird*.

---

## Arbeitspakete mit Bezug zur Datenelement-Erhebung

Die Datenelemente bilden die strukturierte Datenseite des in AP3 modellierten Patientenpfads. Sie werden in den Use-Case-Arbeitspaketen AP6, AP7 und AP8 erhoben, verfeinert und in den jeweiligen Versorgungsphasen verankert. AP3 stellt den methodischen und prozessualen Rahmen.

### AP3 – Übergreifende Patientenpfade (Rahmen)

AP3 entwickelt den integrierten Lungenkrebs-Patientenpfad — laut Antrag (§8.4) ausdrücklich für die Phasen **„screening, treatment, follow-up, palliative, and primary care"** — und überführt ihn in HL7-FHIR-Spezifikationen (siehe Schwester-Repository [`mihub-lung-cancer-pathway`](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway)). Palliativversorgung ist somit **integraler Bestandteil** des AP3-Pfades, nicht nachgelagerter Zusatz. Die hier gepflegten Datenelemente werden so strukturiert, dass sie **plattform-neutral** an die in AP3 entstehenden FHIR-Profile bindbar sind (Aufgabe 3.2 — *Computerinterpretierbare Spezifikation*, M10–M16); eine on-demand-FHIR-Logical-Model-Generierung ist als technischer Brückenkopf vorgesehen.

### AP9 – Stakeholder Involvement & User-Centered Design (begleitend)

AP9 unterstützt AP6/7/8 methodisch — insbesondere Aufgabe 8.1 (Anforderungsanalyse / Stakeholder-Workshops zur Datenelement-Erhebung) erfolgt explizit „gemeinsam mit WP9" (Antrag §8.9). Anforderungen aus Patient:innen-, Behandler- und Forscher:innen-Perspektive werden über User-Centered Design (ISO 9241-210) erhoben und prägen die klinische Definition und Erhebungs-Trigger einzelner Datenelemente.

### AP6 – Use Case: Krebsfrüherkennung

AP6 leitet den in AP3 entwickelten Patientenpfad domänenspezifisch für die Hochrisiko-Identifikation und Lungenkrebsfrüherkennung ab.

**Aufgabe 6.2 – Datenanalyse und Spezifikation (M7–M12)**
Definition von Datenelementen zur Patient:innen­identifikation gemäß Lungenkrebsfrüherkennungsverordnung; partizipative Verfeinerung mit hausärztlichen Praxen.

| ID   | Beschreibung       | Fälligkeit |
| ---- | ------------------ | ---------- |
| D6.2 | Datenspezifikation | M12        |

### AP7 – Use Case: Kooperative Krebsversorgung (einschließlich Palliativversorgung)

AP7 fokussiert Patient:innen in **fortgeschrittener und palliativer Lungenkrebsversorgung** (Antrag §8.8): Vermeidung von Informationsverlusten zwischen Versorgungssettings, Zugang zu Expertenwissen und neuartigen Therapien (insb. molekulare Diagnostik und zielgerichtete Therapien), aktive Einbindung von Patient:innen und Bezugspersonen, umfassende Datenerhebung. Pilotiert wird ein integrierter Ansatz, der das CCC NCT/UCC Dresden mit weiteren Versorger:innen im Großraum Dresden verbindet (Vorarbeiten: nNGM, DigiNET, MiHUBx).

**Aufgabe 7.1 – Erhebung der Patient Journey und Definition von Teilpfaden (M1–M9)**
In Zusammenarbeit mit AP3 wird die Patient Journey für die Behandlungsepisode detailliert; Patient:innenportal-Nutzung und Datenpfad werden spezifiziert.

**Aufgabe 7.2 – Anpassung & Implementierung Patient:innenportal (M13–M48)**
Erweiterung des Portals um nNGM-/MASTER-basierte molekulare Stratifikation und **explizite Palliativversorgungs-Anforderungen** (PROMs, Erinnerungen, Care-/Family-Support-Funktionen).

**Aufgabe 7.3 – Integration der Vernetzungsplattform (M10–M36)**
Integration der kooperativen Versorgungsplattform mit **Schwerpunkt Palliativversorgung**.

| ID   | Beschreibung                                  | Fälligkeit |
| ---- | --------------------------------------------- | ---------- |
| D7.1 | Verfeinerte Patient Journey und Patientenpfad | M9         |
| D7.2 | Prototypischer Einsatz und Test-Version       | M24        |
| D7.3 | Portal Kooperative Krebsversorgung            | M36        |

### AP8 – Use Case: Nachsorge und Langzeitbegleitung (einschließlich Palliativversorgung)

AP8 stärkt die hausärztliche und ambulante onkologische Versorgung durch verbesserte Kommunikation und Datenaustausch (Antrag §8.9). Schwerpunkte sind die **frühzeitige Erkennung von Rezidiven und schwerwiegenden klinischen Komplikationen (SCC)**, **mentale Gesundheit** und **Vital-Status-Erhebung**. KI-Modelle und Continuous Remote Patient Monitoring (CRPM) werden integriert und mit regionalen Partner:innen pilotiert; ELSI-Aspekte werden adressiert.

**Aufgabe 8.1 – Anforderungsanalyse (M1–M6)**
Erhebung notwendiger Datenelemente, digitaler Unterstützungsoptionen und gewünschter Prozesse für die Patient:innen-Nachsorge in Stakeholder-Workshops **gemeinsam mit AP9** (Stakeholder Involvement & User-Centered Design). Definition von Kohorten und Forschungsfragen für vertiefende Studien.

**Aufgabe 8.5 – Mentales Selbstbeurteilungs-Werkzeug (M9–M32)**
Partizipative Entwicklung mit Hausärzt:innen und Patient:innen — datenseitig anschlussfähig an die Erhebungs-Items zu psychischer Belastung in den Phasen Nachsorge und Palliativversorgung.

**Aufgaben 8.6–8.8 – CRPM-Studienpaket (M7–M48)**
Continuous Remote Patient Monitoring; sicherer, interoperabler Vital-Daten-Gateway sowie Studien-Support-Werkzeuge. Datenseitig liefert dieser Strang weitere Anknüpfungspunkte für Symptom- und Vital-Selbsterhebung in der Nachsorge.

| ID   | Beschreibung                                       | Fälligkeit |
| ---- | -------------------------------------------------- | ---------- |
| D8.1 | Anforderungsspezifikation                          | M6         |
| D8.2 | Systemarchitektur für digitale Nachsorge-Unterstützung | M12    |
| D8.3 | Digital Toolset                                    | M24, M36   |
| D8.5 | Mental Self-Evaluation Tool                        | M32        |

---

## Artefakte in diesem Repository

Die Datenelemente werden als **YAML-Single-Source-of-Truth** geführt; abgeleitete Sichten (CSV, Markdown, FHIR) werden aus den YAML-Quellen generiert. Die Erhebung erfolgt **iterativ und phasenweise**: Pro Versorgungsphase existiert ein eigenes Verzeichnis unter `elements/`; weitere Phasen können additiv ergänzt werden, ohne Schema-Bruch — siehe [`docs/howto-add-element.md`](./docs/howto-add-element.md) §D.

Eine aktuelle, autogenerierte Übersicht über alle befüllten Phasen und Datenelemente liefert [`docs/phases-overview.md`](./docs/phases-overview.md). Die maschinenlesbare Vollsicht steht unter [`catalog/data-dictionary.csv`](./catalog/data-dictionary.csv) bzw. als Markdown-Spiegel [`catalog/data-dictionary.md`](./catalog/data-dictionary.md) zur Verfügung.

Jedes Datenelement ist eine eigene `.yaml`-Datei mit standardisiertem Header (ISO 13972 / ISO 13606), klinischer Definition, Coding-Bindings (u. a. SNOMED CT, LOINC, ICD-10-GM, ICD-O-3, ICF, KDL), parallelen Standard-Mappings (u. a. oBDS, KBV-MIO, MII-KDS, mCODE, openEHR), der **Datennutzung entlang des Pfads** (`care_process.data_flows[]` — WO/System · WER/Rolle · WIE/Nutzung; z. B. erfasst der Hausarzt im PVS, liest die Onkolog:in im KIS) und Quellenbelegen aus den verwendeten Leitlinien und Fachpublikationen (siehe Abschnitt *Vorarbeiten und Grundlagen*).

### Schema und Vorlagen

| Datei                                                                                              | Beschreibung                                       |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| [`schemas/data-element.schema.json`](./schemas/data-element.schema.json)                           | JSON-Schema (Single Source of Truth, CI-validiert) |
| [`schemas/TEMPLATE.element.yaml`](./schemas/TEMPLATE.element.yaml)                                 | Vorlage zum Kopieren für neue Datenelemente        |
| [`templates/datenelement-erhebung.xlsx`](./templates/README.md)                                   | Excel-Erhebungs-Vorlage (Klinik-Spur, ohne Git/YAML) |

### Aggregierte Sichten (autogeneriert)

| Datei                                                                              | Beschreibung                                              |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------- |
| [`catalog/data-dictionary.csv`](./catalog/data-dictionary.csv)                     | Vollsicht (24 Spalten, inkl. `care_process_data_flows`); Excel-/REDCap-kompatibel |
| [`catalog/data-dictionary.md`](./catalog/data-dictionary.md)                       | 1:1-Markdown-Spiegel der CSV (für PR-Diffs, Web-Browsing) |
| [`docs/phases-overview.md`](./docs/phases-overview.md)                             | Lesefreundliche Phasen-Übersicht (8 Spalten, gruppiert)   |
| [`docs/methodology.md`](./docs/methodology.md)                                     | Methodik, Gap-Analyse, Designentscheidungen               |
| [`docs/audit-log.md`](./docs/audit-log.md)                           | Audit-Trail (Quellen, Codings, Iterationen)               |
| [`GLOSSARY.md`](./GLOSSARY.md)                                                     | Akronyme, Skalen, Frequenz-Codes, Standard-Identifier     |

### Skripte

| Datei                                                                                              | Funktion                                                        |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| [`scripts/validate.py`](./scripts/validate.py)                                                     | YAML gegen JSON-Schema validieren                                |
| [`scripts/build-catalog.py`](./scripts/build-catalog.py)                                           | YAML → CSV + Markdown + Phasen-Übersicht aggregieren            |
| [`scripts/build-fhir-logical-models.py`](./scripts/build-fhir-logical-models.py)                   | YAML → FHIR Logical Model (FSH, on-demand, projekt-agnostisch)  |
| [`scripts/build-elicitation-workbook.py`](./scripts/build-elicitation-workbook.py)                 | Excel-Erhebungs-Vorlage erzeugen (schema-getrieben; benötigt `openpyxl`) |
| [`scripts/import-elicitation-workbook.py`](./scripts/import-elicitation-workbook.py)               | Ausgefüllte Excel-Mappe → YAML-Entwürfe (`elements/_incoming/`) |
| [`scripts/check-duplicates.py`](./scripts/check-duplicates.py)                                      | Dubletten-/Ähnlichkeitsprüfung neuer Kandidaten gegen den Bestand |

### Agent Skills (werkzeug-unabhängig)

Die spezialisierten Fähigkeiten liegen als portable **Agent Skills** in [`skills/`](./skills) (eine
Quelle, [agentskills.io](https://agentskills.io/specification)) und werden für jedes Werkzeug
bereitgestellt: Claude Code (`.claude/skills` + `.claude/agents`), Codex/Cursor/Gemini
(`.codex/skills`), GitHub Copilot (Brücke [`.github/copilot-instructions.md`](./.github/copilot-instructions.md)).
Vendor-neutraler Katalog + Mechanik: [`AGENTS.md`](./AGENTS.md) · [`skills/SKILLS_SETUP.md`](./skills/SKILLS_SETUP.md).

| Skill | Zweck |
| --- | --- |
| [`data-element-analyzer`](./skills/data-element-analyzer/SKILL.md) | Leitlinien/Onkopedia/Publikationen → datenelementweise Änderungsvorschläge (Konsultations-Pflicht). |
| [`data-element-validator`](./skills/data-element-validator/SKILL.md) | YAML verifizieren (Schema, Codings, Konsistenz), Catalog + Phasen-Übersicht regenerieren. |
| [`check-duplicate-data-element`](./skills/check-duplicate-data-element/SKILL.md) | Neue Kandidaten (Issue/Excel/YAML) vor Aufnahme auf Dubletten/Ähnlichkeit prüfen (read-only). |
| [`ai-usage-curator`](./skills/ai-usage-curator/SKILL.md) | KI-Nutzungs-Disklosure `AI_USAGE.md` pflegen (EU AI Act Art. 50). |

---

## Verwendung

### Drei Wege beizutragen (klinisch wie technisch)

Sie müssen **weder programmieren noch Git/YAML kennen**, um beizutragen. Vollständiger Vergleich
in [`CONTRIBUTING.md`](./CONTRIBUTING.md):

- **🟢 GitHub-Issue-Formular** — niederschwellig, online, ohne Git/YAML → [Neues Datenelement vorschlagen](../../issues/new/choose).
- **🟡 Excel-Vorlage** — für viele Elemente / Workshops, ohne Git/YAML → [`templates/`](./templates/README.md).
- **🔵 YAML + Pull Request** — technisch → [`docs/howto-add-element.md`](./docs/howto-add-element.md).

Neue Kandidaten werden vor Aufnahme auf **Dubletten** geprüft (`scripts/check-duplicates.py`).
Beiträge gehen per Pull Request gegen **`dev`** (Integrations-/Review-Branch); **`main`** ist die
Release-Branch.

### Voraussetzungen (für die YAML-/MI-Spur)

- Python ≥ 3.10
- Empfohlen: VS Code mit YAML-Erweiterung (Schema-Autocompletion, Echtzeit-Validierung)

### Einmaliges Setup

```bash
git clone https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements
cd mihub-lung-cancer-pathway-data-elements

python3 -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements.txt      # pyyaml + jsonschema (+ openpyxl für die Excel-Vorlage)
```

### Tägliche Nutzung

```bash
# Validierung eines Datenelements gegen das Schema
python scripts/validate.py <pfad/zur/datei.yaml>

# Aggregat-Sichten regenerieren (CSV + Markdown + Phasen-Übersicht)
python scripts/build-catalog.py

# Dubletten neuer Kandidaten gegen den Bestand prüfen
python scripts/check-duplicates.py --candidates <pfad/zur/datei.yaml>

# Excel-Erhebungs-Vorlage erzeugen bzw. ausgefüllte Mappe importieren (benötigt openpyxl)
python scripts/build-elicitation-workbook.py
python scripts/import-elicitation-workbook.py ausgefuellt.xlsx --validate

# Optional: FHIR Logical Model generieren (FSH; on-demand, projekt-agnostisch)
python scripts/build-fhir-logical-models.py --help
```

Vollständige Schritt-für-Schritt-Anleitung: [`docs/howto-add-element.md`](./docs/howto-add-element.md).
PR-/CI-/CODEOWNERS-Workflow: [`docs/github-workflow.md`](./docs/github-workflow.md).
Drei Beitrags-Wege (Issue · Excel · YAML): [`CONTRIBUTING.md`](./CONTRIBUTING.md).

---

## Vorarbeiten und Grundlagen

### Standards der Medizininformatik

Das Repository folgt etablierten Mustern der klinischen Modellierung:

| Standard                       | Funktion im Repository                                                                                |
| ------------------------------ | ----------------------------------------------------------------------------------------------------- |
| **ISO 13972:2022**             | Header/Metadaten-Satz pro Datenelement (§6.6 + §7 Tabelle 2 — Clinical Information Models)            |
| **ISO 13606-2:2019**           | Governance, Publikationsstatus, Versionsmanagement (§6.2.5–§6.2.7 — Archetype Interchange)            |
| **ISO 13940 (ContSys)**        | Bezug zum klinischen Geschäftsprozess pro Element (`care_process.trigger`)                            |
| **ISO 23903**                  | Plattformneutralität — Trennung Domänen-Modell ↔ Implementierung                                       |
| **HL7 HSRA Edition 1 (2023)**  | Datenelemente als Inhalte der HSRA-Capabilities (Common Terminology Service, Care Coordination …)     |

### Klinische Quellen (initiale Befüllung)

- **S3-Leitlinie Lungenkarzinom**, Langversion **5.01** (Konsultationsfassung 04/2026, AWMF 020-007OL); Kapitel 4 (Tabakentwöhnung), Kapitel 15 (Rehabilitation), Kapitel 16 (Nachsorge / Verlauf / Follow-up; Empfehlungen 16.1–16.9 Aufwertung EK→B); Tab. 42, Tab. 48.
- **S3-Leitlinie Palliativmedizin**, Langversion **3.01** (Konsultationsfassung 03/2026).
- **AWMF S3-LL Rauchen / Tabakabhängigkeit** (076-006l, 03/2021).
- **Onkopedia** Lungenkarzinom NSCLC (03/2026, Kap. 8 Nachsorge, Tab. 12) und SCLC (09/2025, Kap. 10 Nachsorge, Tab. 9).
- **Optimal Care Pathway for People with Lung Cancer**, Cancer Council Victoria, 2nd ed. (2021, Update 07/2025).
- **Klein A-A et al. (2026).** _Relevante Informationen aus der Onkologie für die hausärztliche Versorgung von Langzeitüberlebenden — Empfehlungen zum Verfassen von onkologischen Abschlussberichten._ Die Onkologie 32:91–99.
- **AG LONKO** (Nationaler Krebsplan): Empfehlungspapiere zur Datenerhebung und zu bedarfsgerechten Versorgungsmodellen.

### Verwandte MiHUB-Artefakte

| Repository / Quelle | Bezug |
| --- | --- |
| [`mihub-lung-cancer-pathway`](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway) | BPMN-Modell der übergreifenden Patient Journey (AP3) — strukturelle Klammer dieses Repositorys |
| [INA Arbeitskreis Fachanwender Journey Onkologie (gematik)](https://www.ina.gematik.de/community-hub/vernetzen-mitwirken/arbeitskreise/fachanwender-journey-onkologie) | Vorarbeit zu Datenflüssen und Schnittstellen entlang der onkologischen Versorgung (CC-Lizenz) |
| [CraNE Joint Action WP6](https://crane4health.eu/wp6-organization-of-comprehensive-high-quality-cancer-care-in-comprehensive-cancer-care-networks-cccns/) | EU-Standard für Lungenkrebsversorgung in Comprehensive Cancer Care Networks (EU4Health, CC BY 4.0) |

> **Attribution INA:** Interop Council / INA – Interoperabilitäts-Navigator der gematik (2023). Fachanwender Journey Onkologie.
>
> **Attribution CraNE:** CraNE Joint Action WP6 (2024). Standard for Lung Cancer Care / Patient Pathway for Lung Cancer Patients. Funded by the European Union (EU4Health Programme).
>
> _Funded by the European Union. Views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or HaDEA. Neither the European Union nor the granting authority can be held responsible for them._

---

## Lizenz

Dieses Repository steht unter zwei abgestimmten Lizenzen:

- **Inhalte** (YAML-Datenelemente, Markdown-Dokumentation, Glossar, Catalog) — **[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)** → [`LICENSE`](./LICENSE)
- **Skripte** (`scripts/*.py`) — **[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)** → [`LICENSE-APACHE-2.0.txt`](./LICENSE-APACHE-2.0.txt)

[![CC BY 4.0](https://licensebuttons.net/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

Zweckbestimmung/Haftung (kein Medizinprodukt, kein klinischer Einsatz): [`DISCLAIMER.md`](./DISCLAIMER.md).

### Attribution

Bei Weiterverwendung bitte folgende Angabe verwenden:

> _Forschungsgruppe Digital Health (FGDH), Technische Universität Dresden (2026). Lungenkrebs-Datenelemente – MiHUB. GitHub: https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements. Lizenzen: CC BY 4.0 (Inhalte) / Apache 2.0 (Skripte)._

### Zitieren / Citation

Maschinenlesbare Metadaten in [`CITATION.cff`](./CITATION.cff) (GitHub-Schaltfläche „Cite this
repository"). _Hinweis:_ Der **Zenodo-Concept-DOI** wird mit der ersten archivierten Release
ergänzt (siehe [`docs/go-public-checklist.md`](./docs/go-public-checklist.md)).

---

## Förderhinweis

Dieses Artefakt ist im Rahmen des Verbundprojekts **Medical Informatics Hub/MiHUB** als Teil der **Medizininformatik-Initiative (MII)** entstanden und wird gefördert durch das **Bundesministerium für Forschung, Technologie und Raumfahrt (BMFTR)**, Förderkennzeichen: 01ZZ2506A.

<p align="middle">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/BMFTR_Logo.svg/1280px-BMFTR_Logo.svg.png" width="500" />
  <img src="https://mihubx.de/wp-content/uploads/2026/01/FortschrittsHubs_rgb_mihub.png" width="300" />
</p>

---

## Kontakt

E-Mail: digital-health@tu-dresden.de\
Webseite: https://tu-dresden.de/bu/wirtschaft/winf/digital-health

Technische Universität Dresden\
Fakultät Wirtschaftswissenschaften\
Forschungsgruppe Digital Health\
01062 Dresden

Für Fragen und Beiträge bitte ein [GitHub Issue](../../issues) erstellen oder die Beitragsspuren in [`CONTRIBUTING.md`](./CONTRIBUTING.md) nutzen.
