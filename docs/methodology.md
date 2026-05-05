# MiHUB Patientenpfad — Methodik & Gap-Analyse

> Begleitdokument zur strukturierten Erhebung von Datenelementen entlang des onkologischen Patientenpfads (Lungenkarzinom).
> Stand 2026-05-04 · Status der initialen Befüllung: Author Draft v0.1 · Sprache Deutsch (Inhalte) / Englisch (Feldnamen).

## 1 Zweck

Das Repository erhebt die Datenelemente, die im Verlauf des onkologischen Patientenpfads (Lungenkarzinom: NSCLC, SCLC) intersektoral dokumentiert und ausgetauscht werden müssen — über *alle* Versorgungsphasen hinweg (Prävention, Diagnostik, Staging, Therapie, Nachsorge, Surveillance, Palliativversorgung, Rehabilitation, Übergänge). Die Erhebung folgt einer expliziten Systematik der Medizininformatik, ist nachvollziehbar versionierbar und legt den Grundstein für das nachgelagerte vollständige Profile-Authoring (FHIR-IG, oBDS-Mapping, ePA-MIO etc.).

Initial befüllt sind die drei Versorgungsphasen **Onkologische Nachsorge, Verlaufsbeobachtung/Surveillance, Palliativversorgung**. Weitere Phasen werden additiv ergänzt; das Schema bleibt dabei stabil.

## 2 Methodik der Datenerhebung

Die Erhebung folgt einem **dreistufigen, iterativen Vorgehen je Versorgungsphase**:

1. **Standards-/Referenzarchitektur-Sichtung.** Sichten der einschlägigen Normen und Referenzarchitekturen mit dem Ziel, die Struktur (Header/Metadaten) für jedes Datenelement von etablierten internationalen Mustern abzuleiten — *nicht* eine eigene Vorlage zu erfinden.
2. **Leitlinien-Auswertung.** Pro Phase werden die einschlägigen nationalen Leitlinien (S3-Leitlinien des Leitlinienprogramms Onkologie, AWMF-Leitlinien, Onkopedia-Leitlinien der DGHO) sowie ergänzend internationale Leitlinien (ESMO, ASCO, NCCN, OCP) und versorgungsforscherische Primärquellen ausgewertet.
3. **Konsolidierung.** Ableitung der Datenelemente in YAML pro Element (Single Source of Truth), Aggregation als CSV-Data-Dictionary, lesbare Phasenübersicht in Markdown — alles aus dem YAML autogeneriert.

Validierung gegen JSON-Schema; Konsistenzprüfung CSV ↔ YAML automatisiert (CI).

Ergänzend zum dreistufigen Vorgehen wird pro Datenelement eine **Re-Verifikation gegen die Primärquelle** durchgeführt (Belegtext mit Kapitel/Empfehlungs-Nr./Tabellenverweis).

## 3 Vorlagenstruktur — Herleitung aus Standards

### 3.1 ISO 13972:2022 — Clinical Information Models

Die Norm beschreibt **klinische Informationsmodelle (CIM)** als Bausteine semantisch interoperabler Versorgung. Sie liefert in §6.6 die Pflichtangaben pro Datenelement und in Tabelle 2 (§7) den vollständigen Metadaten-Kanon. Die Repository-Vorlage übernimmt diese Strukturen 1:1.

| ISO 13972 §/Element | Schema-Feld |
| --- | --- |
| §6.6.3 Data Element Name & Identifier | `name`, `id`, `uuid` |
| §6.6.4 Data Element descriptions | `definition_de`, `instruction_de` |
| §6.6.5 Semantic coding | `value_set.codings[]` |
| §6.6.6 Datatype | `datatype` (mappt auf ISO 21090 / FHIR-Typen) |
| §6.6.7 Value & §6.6.8 Value set expression | `value_set.uri`, `value_set.binding_strength` |
| §6.6.9 Relationships | `related_elements[]` |
| §6.9 Constraints | `constraints_de` |
| §6.10 Instructions for use | `instruction_de` |
| §6.11 Care process / dependence | `care_process.trigger`, `frequency_pattern`, `responsible_role` |
| §6.12 Issues | `issues[]` |
| §6.14 References & §6.5 Evidence base | `evidence.guideline_references[]` |
| Tab. 2 #1 Name | `label_de`, `label_en` |
| Tab. 2 #2 Type | `iso13972_metadata.type` |
| Tab. 2 #4 Keywords | `iso13972_metadata.keywords[]` |
| Tab. 2 #5 Authors | `iso13972_metadata.authors[]` |
| Tab. 2 #6/7 Endorsing authority | `iso13972_metadata.endorsing_authority` |
| Tab. 2 #8 Version number | `iso13972_metadata.version_number` (SemVer) |
| Tab. 2 #9–14 Datumsfelder | `creation_date`, `publication_date`, `expiration_date`, `next_revision_date` |
| Tab. 2 #15–17 Status | `iso13972_metadata.publication_status` |
| Tab. 2 #18 Publisher | `iso13972_metadata.publisher` |
| Tab. 2 #19 Language | `iso13972_metadata.language[]` (ISO 639) |

### 3.2 ISO 13606-2:2019 — Archetype interchange

Die Norm liefert die Anforderungen an Archetypen — insbesondere Versionsmanagement, Publikationsstatus und Audit-Trail. Das Schema übernimmt:

- **Publikationsstatus-Lebenszyklus** (§6.2.6.1: *Test → In development → Release candidate → Definitive → Deprecated → Rejected*) als `iso13972_metadata.publication_status`.
- **Identifikation** (§6.2.1.1: globally unique identifier) als `uuid`.
- **Provenance** (§6.2.6.3–.6: Person + Behörde + Review-Datum) als `provenance.created_by` + `reviewers[]`.
- **Beziehungen** (Spezialisierung, Vorgänger, Ersatz) als `related_elements[]` mit Relationen `specializes`, `supersedes`, `supersededBy`.

### 3.3 ISO 13940 — ContSys (Continuity of Care)

ISO 13940 definiert klinische Geschäftsprozesse. ISO 13972 §7.2 Tab. 2 bezieht sich explizit darauf: *„If ISO 13940 (ContSys) is used, then the type of Clinical Information Model will be identified from the business process as defined in that standard."* Das Repository nimmt das im Feld `care_process.trigger` (welches Ereignis im Geschäftsprozess löst die Erhebung aus) und `responsible_role` (welche Rolle erfasst es) auf.

### 3.4 ISO 23903 — Interoperability and Integration Reference Architecture

ISO 23903 trennt Domänen-Modell von Plattform/Implementierung (Generic Component Model). Das Repository ist deshalb **plattformneutral**: Das YAML beschreibt das Datenelement domänensemantisch; Standard-Bindings sind eine Liste (`standard_mappings[]`) und kein Kernfeld. Damit bleibt die Erhebung anschlussfähig an FHIR R4, openEHR, HL7 V2, gematik ePA, ePA-MIOs, oBDS, OMOP CDM — und für nachgelagertes Profile-Authoring auswählbar.

### 3.5 HL7 HSRA Edition 1 (2023)

HSRA katalogisiert die Service-Capabilities (Identification, Record Management, Healthcare Community Services & Provider Directory, **Common Terminology Service**, Decision Support, Consent Management, **Care Coordination**, Ordering, Event Pub/Sub, Data Mapping/Transformation, ...). Das Repository referenziert HSRA implizit über die `value_set`-Bindings (Common Terminology Service) und über `care_process.responsible_role` (Care Coordination). Die Datenelemente sind die *Inhalte*, die in den HSRA-Capabilities transportiert werden — die Capabilities selbst sind Aufgabe der MiHUB-Architektur (Zielbild).

### 3.6 Standard-Mappings — nationale & internationale Implementation Guides

Pro Datenelement werden **mehrere parallele Bindings** in `standard_mappings[]` gehalten — kein FHIR-Lock-in. Notations-Konvention: **nationale Mapping-Ziele zuerst notieren**, dann internationale.

#### Nationale (DE) Mapping-Ziele

| Code | Standard | Geltungsraum / gesetzliche Verankerung |
| --- | --- | --- |
| `obds` | Onkologischer Basisdatensatz, Version 3.0 (03/2022, Plattform §65c) | gesetzlich §65c SGB V — Pflichtmeldung an klinische und epidemiologische Krebsregister; verbindlicher tumortyp-übergreifender Standard, mit organspezifischen Modulen |
| `gekid-adt` | ADT/GEKID-Tumorbasisdokumentation | historischer Vorgänger des oBDS; weiterhin in Bestandssystemen (Onkostar, GTDS, CREDOS) verbreitet |
| `gematik-epa-fhir` | gematik FHIR IGs für „ePA für alle" (TI Common, TI Terminologies, ePA Basic Functions, Medication Service, MHD Service) | gesetzliche ePA-Plattform; flächendeckender Patientenkontext |
| `gematik-erezept-fhir` | gematik eRezept FHIR IG | gesetzliche elektronische Verordnung |
| `kbv-mio` | KBV MIO-Bundles (Patientenkurzakte, Impfpass, Mutterpass, ZahnBonusheft, …) | Inhalte der ePA — strukturierte Übergabe Onko ↔ Hausarzt; relevant für Survivorship-Care-Plan-Übergabe (Klein 2026) |
| `fhir-mii-kds` | MII-Kerndatensatz (Module Person, Diagnose, Prozedur, Labor, Medikation, Bildgebung, Onkologie, …) | Forschung / FDPG / DSF |
| `fhir-isik` | gematik ISiK Stufen 1–4 | KIS/AIS-Primärsysteme |

#### Internationale Mapping-Ziele

| Code | Standard | Geltungsraum |
| --- | --- | --- |
| `mcode` | HL7 minimal Common Oncology Data Elements (mCODE) Implementation Guide, derzeit STU4 (~40 Profile in 6 Bereichen: Patient, Disease, Assessment, Genomics, Treatment, Outcome) | international, FHIR-basiert; zentral für Onkologie-Interop in Nordamerika, zunehmend in EU |
| `fhir-genomics` | HL7 FHIR Genomics IG | molekulare Diagnostik (EGFR, ALK, ROS1, KRAS, BRAF u. a.) |
| `openehr-archetype` | openEHR Clinical Knowledge Manager (CKM) | EHR-Archetypen, primär in Skandinavien, UK, Brasilien |
| `omop-cdm` | OHDSI OMOP Common Data Model inkl. Onkologie-Extension; FHIR↔OMOP-Mapping (mCODE↔OMOP) im Aufbau | Versorgungsforschung, internationale Kohortenstudien |
| `cdisc-sdtm` | CDISC SDTM/CDASH | klinische Studien, Regulatorik (FDA, EMA) |
| `fhir-r4-base` | FHIR R4 Vanilla | wenn kein Profil exakt passt |
| `hl7-v2` | HL7 V2 ADT / Labor / DALE-UV | Legacy-Schnittstellen |
| `dicom-sr` | DICOM Structured Report | strukturierte Bildbefunde |
| `hl7-cda` | HL7 CDA | eArztbrief, IHE-Inhalte |
| `ihe-xds` | IHE XDS Affinity Domains | Dokumenten-Container |

Beispiel-Mehrfach-Mapping siehe `elements/follow-up/recurrenceOrSecondPrimary.yaml` (FHIR-MII-KDS + oBDS + KBV-MIO). Vollständiges Profile-Authoring (StructureDefinitions, ValueSets, ConceptMaps) ist Aufgabe der nachgelagerten Implementierungsiteration; das Repository liefert die kanonische Spezifikation, gegen die diese Implementierungen erfolgen.

## 4 Format-Wahl & GitHub-Eignung

### 4.1 Drei kohärente Repräsentationen

Auf Basis der Anforderungen wurde eine **kombinierte Form** gewählt:

| Form | Zweck | Begründung |
| --- | --- | --- |
| YAML pro Element | kanonische Form | Atomare Reviews, klare Diff-Geschichte, ein Datenelement = ein PR-Artefakt |
| JSON-Schema | Vertragsdefinition | maschinelle CI-Validierung, Werkzeug-Anschluss (jsonschema, ajv) |
| CSV-Data-Dictionary (semicolon, autogeneriert) | flache Sicht | Excel-/REDCap-/MII-DataDict-kompatibel, einfach an Klinik-Reviewer:innen versendbar |
| Markdown-Phasenübersicht | lesefreundlich | Schneller Überblick je Phase für Klinik-Reviews |

Diese Kombination ist **nicht redundant**: CSV/Markdown werden aus dem YAML generiert und sind damit konsistent (Single Source of Truth = YAML).

### 4.2 GitHub-Eignung

GitHub ist gut geeignet, weil:

- YAML/JSON-Diffs in PRs sind exzellent reviewbar.
- Atomare PRs pro Element → fokussierte Diskussionen, klare Audit-Trails.
- Branch-Protection + CODEOWNERS bilden die ISO-13606-Governance ab.
- GitHub Actions validieren das Schema bei jedem Push.
- Releases mit SemVer + Zenodo-DOI machen Stände zitierbar (z. B. für Manuskripte).
- Issue-Tracker bietet Verknüpfung zu klinischen Diskussionen je Element.

Risiko und Mitigation:

- **Diff-Lärm bei großen Tabellen:** Wir erzeugen die CSV via CI; Reviewer:innen reviewen YAML, nicht CSV.
- **Mehrsprachigkeit:** Inhalte deutsch (`label_de`, `definition_de`); Feldnamen englisch — internationale Anschlussfähigkeit ohne Bruch in der Klinik-Sprache.
- **Sensible Inhalte (z. B. Todeswunsch):** als Element-`issues` markiert; Zugriffsschutz wird in der Architektur (Consent / DSF / Broad Consent) gelöst, nicht im Schema.

## 5 Umfang der initialen Befüllung (v0.1)

| Phase | YAMLs |
| --- | --- |
| Onkologische Nachsorge (`elements/follow-up/`) | 18 |
| Verlaufsbeobachtung / Surveillance (`elements/surveillance/`) | 15 |
| Palliativversorgung (`elements/palliative/`) | 18 |
| **GESAMT (initial)** | **51** |

Davon **44 Erhebungs-Datenelemente** (Prozeduren, Werte, Status, Pläne) plus **7 Ergebnis-Datenelemente** (Bildbefunde, Lungenfunktionswerte, Mutationsergebnis, CTCAE-Grad, Caregiver-Burden-Score) — siehe `verification-log.md` §4.

Diese Erhebung ist **bewusst kein vollständiger Datensatz**, sondern der **belegbare Kernsatz** aus den oben genannten LL-Quellen für die drei initial befüllten Phasen.

**Ausstehende Phasen** (Reihenfolge-Vorschlag):

1. Prävention / Früherkennung (z. B. Lungenkarzinom-Screening per LDCT, BRD-Screeningprogramm 2024)
2. Diagnostik & Staging (TNM 9th edition, Histologie, Molekularpathologie)
3. Therapie (kurativ + palliativ; OP, RTx, CTx, zielgerichtet, Immuntherapie)
4. Rehabilitation (S3-LL Lungenkarzinom Kap. 15; ESPEN-Ernährungsleitlinien)
5. Sektorenübergänge (Aufnahme/Entlassung/Verlegung; eArztbrief, ePA-Übergabe)

Erweiterungen erfolgen iterativ; das Schema bleibt stabil (Phasen-Enum wird ggf. erweitert — Minor-Schema-Bump).

## 6 Gap-Analyse

### 6.1 Was die Standards abdecken

| Frage | Standard | Bewertung |
| --- | --- | --- |
| Wie strukturiere ich ein Datenelement formal? | ISO 13972, ISO 13606-2 | vollständig |
| Wie versioniere und governe ich? | ISO 13606-2, ISO 13972 §7 | vollständig |
| Wie binde ich Terminologien? | HL7 HSRA Common Terminology, MII-KDS, SNOMED CT, LOINC | vollständig |
| Wie verbinde ich mit dem Versorgungsprozess? | ISO 13940 (ContSys), HSRA Care Coordination | rudimentär; nicht onkologie-spezifisch |
| Wie technisch implementieren? | ISO 23903, FHIR R4, MII-KDS | klar (nachgelagerte Iteration) |

### 6.2 Was die Standards **nicht** abdecken — onkologie-spezifische Lücken

| Lücke | Auswirkung | Repository-Lösung |
| --- | --- | --- |
| Keine standardisierte Liste **onkologie-spezifischer Datenelemente** je Versorgungsphase | LL-Empfehlungen werden nicht konsistent codiert; jede Klinik dokumentiert anders | LL-Empfehlungen als kanonisches Set codieren (initial 51 Elemente in 3 Phasen) |
| Kein international konsentiertes **Survivorship-Care-Plan-Schema** in deutscher Versorgung | Übergabe Onko ↔ Hausarzt fehleranfällig (Klein 2026 belegt Lücken) | Element `survivorshipCarePlan` mit Pflichtinhalten Anamnese/Therapie/Spätfolgen/Prozedere — anschlussfähig an AG-LONKO-Empfehlungen, `kbv-mio`-Mapping (Patientenkurzakte) |
| **PROM** (Patient-Reported Outcomes) sind in MII KDS unterspezifiziert | Web-basierte Symptomerfassung (Denis 2017, Greer 2024) nicht standardisierbar | Element `patientReportedSymptomWeb` mit Hinweis auf QuestionnaireResponse; perspektivisch mCODE-PROM-Integration |
| **Komplexitätsbewertung** der Palliativversorgung (low/medium/high + Krankheitsphasen) ist nicht in MII KDS | SPV-Indikation nicht maschinell auslesbar | Eigene Codes `complexityLevel` + `illnessPhase` (mihub-CodeSystem; SNOMED-Mapping in nachfolgender Iteration) |
| **Sensible Datenelemente** (Todeswunsch, Sterbephase, ACP) erfordern besondere Consent-/Access-Logik | Risiko der Fehlbehandlung bei Freigabeproblemen | Markierung in `issues[]`; Governance in Architektur (Broad Consent + dedizierter Palliativ-Modul-Consent) |
| **Onkopedia-Tabellen** sind nicht maschinenlesbar (HTML/PDF) | Nachsorgeintervalle für NSCLC/SCLC werden manuell übertragen | `followUpInterval` mit kontrolliertem Vokabular (Q3M-Y1-Y2 etc.) — direkt aus Onkopedia Tab. 12 / Tab. 9 abgeleitet |
| **CTCAE/MedDRA-Lizenz**-Restriktionen | irAE-Erfassung nur eingeschränkt frei codierbar | `extensible`-Binding mit Beispielcodes; vollständiges ValueSet erst in implementierender Einrichtung |
| **MII-KDS Modul Onkologie** deckt Stammdaten ab, aber **nicht** Verlauf/Surveillance/Palliativ-Domänen | Surveillance-Daten fragmentiert | Repository schließt diese Lücke explizit; `mcode`-Mapping bietet internationale Brücke (Disease, Assessment, Treatment, Outcome) |
| **oBDS** ist auf Krebsregister-Kernfelder fokussiert, nicht auf Verlauf/Symptome/PRO | Daten der laufenden Versorgung sind nicht in oBDS abbildbar | Repository ergänzt diese Domänen; oBDS bleibt Pflichtmeldungspfad für strukturierte Tumorhistorie |

### 6.3 Eigenes vs. importiertes Vokabular

Wo möglich, wurden **internationale Codes** (SNOMED CT, LOINC, ICD-10-GM, OPS, ATC, UCUM) verwendet. Wo kein passender Code existiert (z. B. Krankheitsphasen *stabil/instabil/verschlechternd/sterbend*, Komplexitätsstufen, Versorgungsstufen PBP/APV/SPV, Nachsorgeintervalle Q3M-Y1-Y2), wurde ein **`mihub`-CodeSystem** als Platzhalter eingeführt; das Mapping nach SNOMED CT (z. B. Refset oder `valueset-extension`) ist Aufgabe einer nachfolgenden Iteration.

## 7 Pflege-Lebenszyklus & Iteration

**Reife-Stufen:**

- **v0.1 (Author Draft)** — initiale Befüllung der drei Phasen Nachsorge/Surveillance/Palliativ
- **v0.2 (CommitteeDraft)** — nach interner Konsultation MiHUB-Konsortium / klinischen Reviewer:innen, Erweiterung um weitere Phasen
- **v1.0 (ApprovedForProductionUse)** — freigegeben für nachgelagertes Profile-Authoring (FHIR-IG-Generierung, oBDS-/MIO-Mapping)

Statuswechsel werden je Element einzeln im YAML gepflegt (`publication_status`) — das verhindert Big-Bang-Änderungen und erlaubt ein graduelles Reifen.

**Iterations-Log (Schema- und Inhalts-Änderungen während v0.1):**

| Iteration | Schema-Änderung | Inhalt |
| --- | --- | --- |
| v0.1 initial | Schema, ID-Pattern (camelCase erlaubt) | 44 Erhebungs-Elemente in 3 Phasen |
| v0.1 multi-standard | `fhir_mapping` (Single-Slot) → `standard_mappings[]` (Liste) | Beispiel-Multi-Mapping `recurrenceOrSecondPrimary` (FHIR-MII-KDS + oBDS + KBV-MIO) |
| v0.1 national-IGs | Standards-Enum erweitert: `obds`, `gekid-adt`, `gematik-epa-fhir`, `gematik-erezept-fhir`, `kbv-mio`, `mcode`, `fhir-genomics`, `omop-cdm`, `cdisc-sdtm` | nationale Mapping-Ziele bevorzugt notiert |
| v0.1 Standardlücken explizit | `value_set.standard_binding_status` und `value_set.notes` ergänzt | Pseudo-System `mihub` durch `local-no-standard-binding` + Begründung ersetzt (6 Elemente) |
| v0.1 CSV-Marker | CSV-Header mit Pflicht-Markern `*` (mandatory) / `+` (recommended) | — |
| v0.1 Ergebnisartefakte | unverändert | +7 Result-Datenelemente (Bildbefunde, Lungenfunktion, Mutation, CTCAE-Grad, Zarit-Score) → 51 |
| v0.1 KDL-Mapping | unverändert | +20 KDL-Codings (DG020103 CT-Befund, DG020107 MRT-Befund, DG060108 Lungenfunktion, PT130102 Molekularpathologiebefund, AD060106 Tumorkonferenzprotokoll, SD150101 Follow up-Bogen, AM160104 Patientenverfügung, SD110105 Palliativmed. Komplexbeh., VL010103 Schmerzerhebungsbogen) |

Detaillierter Audit-Trail je Element: `verification-log.md`.

## 8 Verbindung zum MiHUB-Zielbild

Die Datenelemente füttern die drei Säulen des MiHUB-Zielbilds:

- **Intersektoraler Datenraum** — die in `phase: …` codierten Elemente sind Inhalte, die zwischen DIZ-Knoten, Onkologie, Hausarztpraxis, Palliativ-Team, Krebsregister (`obds`) und ePA (`gematik-epa-fhir` / `kbv-mio`) ausgetauscht werden.
- **Patientenportal** — `patientReportedSymptomWeb`, `distressThermometerScore`, EORTC QLQ-C30 sind Patient-zugängliche Inhalte.
- **Forschungs-Service-Portal** — alle Elemente sind durch `value_set`-Bindings + LL-Quellen FDPG/MII-anbindungsfähig; OMOP-Brücke perspektivisch über `omop-cdm`.

## 9 Quellen

### Klinische Leitlinien (initiale Befüllung)

- S3-Leitlinie **Lungenkarzinom** (Langversion 4.0, 04/2025) — insbesondere Kap. 16 *Nachsorge / Verlauf / Follow-up* (Empfehlungen 16.1–16.9, Tabelle 42), Kap. 15 Rehabilitation.
- S3-Leitlinie **Palliativmedizin** (Langversion 3.01, Konsultationsfassung 03/2026) — Kap. 5, 6, 9, 10, 17, 18, 19, 20, 21; Tabellen 6 und 9.
- S3-Leitlinie **Tabakentwöhnung** AWMF 076-006l, 03/2021.
- **Onkopedia** Lungenkarzinom NSCLC, Stand 03/2026, Kap. 8 Nachsorge, Tab. 12. Onkopedia SCLC, Stand 09/2025, Kap. 10 Nachsorge, Tab. 9.
- Cancer Council Victoria: **Optimal Care Pathway for People with Lung Cancer**, 2nd ed. 2021 (Update 07/2025) — Steps 5–7.
- Klein A-A et al. (2026). *Relevante Informationen aus der Onkologie für die hausärztliche Versorgung von Langzeitüberlebenden — Empfehlungen zum Verfassen von onkologischen Abschlussberichten.* Die Onkologie 32:91–99. doi:10.1007/s00761-025-01867-1.
- AG LONKO im Nationalen Krebsplan: Empfehlungspapiere *Datenerhebung und Datenanalyse* sowie *Bedarfsgerechte Versorgungsmodelle* (2021).

### Standards & Referenzarchitekturen

- **ISO 13972:2022** *Health informatics — Clinical information models — Characteristics, structures and requirements*.
- **ISO 13606-2:2019** *EHR communication — Archetype interchange specification*.
- ISO 13940 (Konzept ContSys), ISO 23903 (Interoperability and Integration Reference Architecture).
- **HL7 Health Services Reference Architecture (HSRA)** Edition 1 STU, September 2023.

### Implementation Guides — National (DE)

- **Onkologischer Basisdatensatz (oBDS)** v3.0.0 (03/2022), Plattform §65c SGB V — `https://www.basisdatensatz.de/`
- **ADT/GEKID Tumorbasisdokumentation** — `https://www.gekid.de/adt-gekid-basisdatensatz`
- **gematik FHIR Implementation Guides** für „ePA für alle" (TI Common, TI Terminologies, ePA Basic Functions, Medication Service, MHD Service) — `https://gemspec.gematik.de/ig/fhir/`
- **gematik eRezept FHIR IG**.
- **KBV MIO** Patientenkurzakte u. a. — `https://mio.kbv.de/`
- **MII Kerndatensatz** Module — `https://www.medizininformatik-initiative.de/`
- **gematik ISiK** Stufen 1–4.

### Implementation Guides — International

- **HL7 mCODE** — minimal Common Oncology Data Elements Implementation Guide STU4 — `https://hl7.org/fhir/us/mcode/` und `https://build.fhir.org/ig/HL7/fhir-mCODE-ig/`
- **HL7 FHIR Genomics** Implementation Guide.
- **OHDSI OMOP Common Data Model** inkl. Onkologie-Extension; FHIR-OMOP-Mapping (HL7 ballot).
- **CDISC SDTM/CDASH** für klinische Studien.
- **openEHR Clinical Knowledge Manager (CKM)**.
- **DICOM Structured Report**, **HL7 V2**, **HL7 CDA**, **IHE XDS**.
