# MiHUB Patientenpfad — Datenelemente Lungenkarzinom

**Strukturierte, versionierbare Erhebung von Datenelementen entlang des gesamten onkologischen Patientenpfads** beim Lungenkarzinom (NSCLC, SCLC).

> Status: **Author Draft v0.1** · Sprache: Deutsch (Inhalte) / Englisch (Feldnamen) · Lizenz: CC-BY-4.0 (Inhalte) · Apache-2.0 (Skripte)

> ⚠️ **KI-gestützt erstellt** — siehe [`DISCLAIMER.md`](DISCLAIMER.md). Inhalte sind als Author Draft zu betrachten und vor produktivem Einsatz klinisch zu reviewen. Pflege erfolgt über konsens-basierte Sub-Agenten (siehe [`AGENTS.md`](AGENTS.md)).

## 1 Zweck

Das Repository dient der nachvollziehbaren, intersektoral abgestimmten Erhebung *aller* Datenelemente, die im Verlauf des onkologischen Patientenpfads (Lungenkarzinom) klinisch erforderlich, leitlinien-belegt und für den intersektoralen Austausch (Onkologie ↔ Hausarzt ↔ Palliativ-Team ↔ Forschung ↔ Krebsregister ↔ ePA) relevant sind.

Die Befüllung erfolgt **iterativ und phasenweise**. Initial sind drei Versorgungsphasen befüllt:

- Onkologische **Nachsorge** nach kurativer Therapie
- **Verlaufsbeobachtung / Surveillance** unter palliativer Systemtherapie
- **Palliativversorgung**

Weitere Phasen — z. B. **Prävention/Früherkennung, Diagnostik, Staging, Therapie (kurativ und palliativ), Rehabilitation, Übergänge sektorübergreifend** — können additiv ergänzt werden, ohne dass das Schema verändert werden muss (siehe `docs/howto-add-element.md` §D *Neue Versorgungsphase aufnehmen*).

Das Repository folgt etablierten Mustern der Medizininformatik:

- **ISO 13972:2022** *Clinical Information Models — Characteristics, structures and requirements* — Header/Metadaten-Satz pro Datenelement (§6.6 Data elements + §7 Tabelle 2).
- **ISO 13606-2:2019** *Archetype interchange specification* — Governance, Publikationsstatus, Versionsmanagement (§6.2.5–§6.2.7).
- **ISO 13940** (ContSys) — Bezug zum klinischen Geschäftsprozess pro Element (`care_process.trigger`).
- **ISO 23903** *Interoperability and Integration Reference Architecture* — Trennung Domänen-Modell ↔ Plattform/Implementierung; das Repo bleibt **plattformneutral** (kein FHIR-Lock-in).
- **HL7 HSRA Edition 1 (2023)** — die Datenelemente sind die Inhalte, die in den HSRA-Capabilities transportiert werden (Common Terminology Service, Record Management, Care Coordination).
- **Standards-Liste pro Datenelement** (`standard_mappings[]`) — parallele, gleichwertige Bindings auf nationale (DE) und internationale Implementation Guides (siehe §3).

## 2 Repository-Struktur

```
data-elements/
├── README.md                              ← dieses Dokument
├── DISCLAIMER.md                          ← KI-gestützte Erstellung, unterstützte Aufgaben
├── AGENTS.md                              ← Sub-Agenten-Übersicht (Cross-Tool-Konvention)
├── CONTRIBUTING.md                        ← Beitragsregeln (zwei Spuren)
├── docs/
│   ├── methodology.md                     ← Methodik, Gap-Analyse, Designentscheidungen, Iterations-Log
│   ├── github-workflow.md                 ← PR-/Review-/CI-Workflow
│   ├── howto-add-element.md               ← Anleitung Element hinzufügen
│   ├── verification-log.md                ← Audit-Trail (Quellen, Codings, Iterationen)
│   └── phases-overview.md                 ← Phasen-Übersicht (autogeneriert)
├── schemas/
│   ├── data-element.schema.json           ← JSON-Schema (Single Source of Truth)
│   └── TEMPLATE.element.yaml              ← Vorlage zum Kopieren
├── elements/
│   ├── follow-up/                         ← Onkologische Nachsorge
│   ├── surveillance/                      ← Verlaufsbeobachtung unter Systemtherapie
│   ├── palliative/                        ← Palliativversorgung
│   └── <weitere phasen>/                  ← additiv: diagnostics, treatment, rehab, …
├── catalog/                               ← autogenerierte Vollsicht (22 Spalten)
│   ├── data-dictionary.csv                ← CSV (Excel/REDCap-kompatibel)
│   └── data-dictionary.md                 ← 1:1-Markdown-Spiegel (für PR-Diffs, Web-UI)
├── requirements.txt                       ← Python-Abhängigkeiten (pyyaml, jsonschema)
├── scripts/
│   ├── validate.py                        ← Schema-Validierung
│   ├── build-catalog.py                   ← YAML → CSV Aggregator
│   └── build-fhir-logical-models.py       ← YAML → FHIR Logical Model (optional, on-demand)
└── .claude/agents/
    ├── data-element-analyzer.md           ← Sub-Agent: Doku-Analyse, datenelementweise Konsultation
    └── data-element-validator.md          ← Sub-Agent: YAML-Verifikation + Katalog-Regeneration
```

## 3 Standard-Mappings — nationale & internationale Ziele

Pro Datenelement werden **mehrere parallele Bindings** in `standard_mappings[]` gepflegt — kein Lock-in. Notations-Konvention: **nationale Mapping-Ziele zuerst**.

| Standard | Domäne | Geltungsraum | Anwendung |
| --- | --- | --- | --- |
| `obds` | Onkologie / Krebsregistermeldung | DE — gesetzlich §65c SGB V | Pflichtmeldung an klinisches & epidemiologisches Krebsregister; aktuelle Version oBDS 3.0 (03/2022) |
| `gekid-adt` | Onkologie / Tumorbasisdokumentation | DE — historisch / Vorgänger oBDS | Bestandsdaten in Tumordokumentationssystemen (Onkostar, GTDS u. ä.) |
| `gematik-epa-fhir` | ePA-Plattform | DE — gesetzlich („ePA für alle") | gematik FHIR IGs: ePA Basic Functions, Medication Service, MHD Service, TI Common, TI Terminologies |
| `gematik-erezept-fhir` | Verordnung | DE — gesetzlich | gematik eRezept FHIR IG |
| `kbv-mio` | ePA-Inhalte (Module) | DE | KBV MIO-Bundles (Patientenkurzakte, Impfpass, Mutterpass, ZahnBonusheft …) |
| `fhir-mii-kds` | Forschung / Sekundärnutzung | DE | MII Kerndatensatz; FDPG-Pfad; DSF |
| `fhir-isik` | Primärsysteme (KIS/AIS) | DE | gematik ISiK Stufen 1–4 |
| `fhir-r4-base` | FHIR R4 Vanilla | international | Wenn kein Profil exakt passt |
| `mcode` | Onkologie / Common Elements | international | HL7 minimal Common Oncology Data Elements IG STU4 (~40 Profile, 6 Bereiche) |
| `fhir-genomics` | Molekulare Diagnostik | international | HL7 FHIR Genomics IG; relevant für EGFR/ALK/ROS1/KRAS/BRAF |
| `openehr-archetype` | EHR / Archetypen | international | openEHR CKM |
| `omop-cdm` | Versorgungsforschung | international | OHDSI OMOP CDM inkl. Onkologie-Extension; FHIR-OMOP-Brücke (mCODE↔OMOP) |
| `cdisc-sdtm` | klinische Studien | international | CDISC SDTM/CDASH |
| `hl7-v2` | Legacy ADT/Labor | international | DALE-UV, Labor-LDT, ADT-Schnittstellen |
| `dicom-sr` | Bildbefunde | international | DICOM Structured Report |
| `hl7-cda` | Dokumente | international | eArztbrief, IHE-Inhalte |
| `ihe-xds` | Dokumenten-Container | international | XDS Affinity Domains |

Konvention: pro Element möglichst **mindestens ein nationales und ein internationales Ziel** notieren. Volles Profile-Authoring ist Aufgabe der nachgelagerten Implementierungs-Iteration.

## 4 Format-Entscheidung

Drei kohärente Repräsentationen desselben Inhalts (Single Source of Truth = YAML):

| Artefakt | Zweck | Eignung GitHub |
| --- | --- | --- |
| **YAML pro Element** (`elements/<phase>/<id>.yaml`) | kanonische Form, ein Datenelement = eine Datei → klare Diff-Geschichte, fokussierte PRs | sehr gut |
| **JSON-Schema** (`schemas/data-element.schema.json`) | Vertragsdefinition, CI-Validierung | sehr gut |
| **CSV-Data-Dictionary** (`catalog/data-dictionary.csv`) | flache Vollsicht für Domänenexpert:innen (Excel/REDCap); Pflicht-Marker `*` (mandatory) / `+` (recommended) im Header; 22 Spalten | gut (semicolon-separiert, stabil im Diff) |
| **Markdown-Mirror der CSV** (`catalog/data-dictionary.md`) | 1:1-Markdown-Spiegelung der CSV — gleiche 22 Spalten, gleiche Reihenfolge — für GitHub-PR-Diffs (rendert nativ), Web-UI-Suche, Direktverlinkung | sehr gut |
| **Markdown-Phasenübersicht** (`docs/phases-overview.md`) | lesefreundliche, kuratierte Untermenge (8 Spalten) je Phase, gruppiert + erläutert; **Zielgruppe Klinik-Reviewer:innen** | sehr gut |

## 5 Mitwirken / Datenelement hinzufügen

**Zwei Beitrags-Spuren** — siehe [`CONTRIBUTING.md`](CONTRIBUTING.md):

- **Klinik-Spur** (kein YAML/Git): Web-Formular „📋 Neues Datenelement vorschlagen" auf GitHub Issues. → [Anleitung §A](docs/howto-add-element.md#a-klinik-spur-ohne-yaml--ohne-git)
- **MI-Spur** (YAML + PR): klassische Pull-Request-Mechanik. → [Anleitung §B](docs/howto-add-element.md#b-mi-spur-yaml--git--pr)

Schnellstart MI-Spur:

```bash
cp schemas/TEMPLATE.element.yaml elements/<phase>/myNewElement.yaml
$EDITOR elements/<phase>/myNewElement.yaml
python scripts/validate.py elements/<phase>/myNewElement.yaml
python scripts/build-catalog.py    # regeneriert catalog/data-dictionary.csv
```

Optional — FHIR Logical Model (FSH) on-demand erzeugen:

```bash
python scripts/build-fhir-logical-models.py    # → derived/fhir-logical-model/ (gitignored)
```

Der Generator ist self-contained (Logical Model + ValueSets sind im Skript embedded), erzeugt ein Schema unter `_schema/` und je Datenelement eine FSH-Instance unter `instances/<phase>/`. Hintergrund-Doku zur Eignungsanalyse FHIR Logical Model vs. YAML ist archiviert unter `MiHUB Patientenpfad/.archive/fhir-logical-model/`.

Vollständige Schritt-für-Schritt-Anleitung: [`docs/howto-add-element.md`](docs/howto-add-element.md).
PR-/CI-/CODEOWNERS-Workflow: [`docs/github-workflow.md`](docs/github-workflow.md).

## 6 Quellenbasis (initiale Befüllung der drei Phasen)

- Leitlinienprogramm Onkologie: **S3-Leitlinie Lungenkarzinom**, Langversion **5.01**, Konsultationsfassung 04/2026 (AWMF 020-007OL, Kommentarfrist bis 2026-05-02; bisherige finale Version 4.0 04/2025 ist abgelöst). Kapitel 4 *Tabakentwöhnung* (modifiziert/neu 2026), Kapitel 16 *Nachsorge / Verlauf / Follow-up* (Empfehlungen 16.1–16.9 Aufwertung EK→B 2025), Kapitel 15 Rehabilitation; Tabelle 42; Tabelle 48 (Übersicht der Änderungen v4 → v5).
- Leitlinienprogramm Onkologie: **S3-Leitlinie Palliativmedizin**, Langversion 3.01 Konsultationsfassung 03/2026.
- AWMF: **S3-LL Rauchen / Tabakabhängigkeit** 076-006l, 03/2021.
- **Onkopedia** Lungenkarzinom NSCLC (Stand 03/2026, Kap. 8 Nachsorge, Tab. 12) und SCLC (Stand 09/2025, Kap. 10 Nachsorge, Tab. 9).
- Cancer Council Victoria: **Optimal Care Pathway for People with Lung Cancer**, 2nd ed. 2021 (Update 07/2025).
- Klein A-A et al. (2026). *Relevante Informationen aus der Onkologie für die hausärztliche Versorgung von Langzeitüberlebenden — Empfehlungen zum Verfassen von onkologischen Abschlussberichten.* Die Onkologie 32:91–99.
- AG LONKO (Nationaler Krebsplan): Empfehlungspapiere *Datenerhebung und Datenanalyse* sowie *Bedarfsgerechte Versorgungsmodelle*.

Quellen für die übergreifenden Standards: ISO 13606-2/-5, ISO 13972, HL7 HSRA, mCODE FHIR IG, gematik ePA FHIR IGs, KBV MIO, oBDS, OMOP CDM (siehe `docs/methodology.md` §3).
