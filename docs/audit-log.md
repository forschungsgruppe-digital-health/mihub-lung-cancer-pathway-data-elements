# Audit-Log — Quellen-Verifikation und Iterations-Protokoll

Dieses Dokument bündelt zwei Audit-Funktionen:

1. **Quellen-Verifikation** der erhobenen Datenelemente gegen die zitierten Primärquellen — nachvollziehbar belegen, dass jede `evidence.guideline_references[]`-Angabe einem Belegtext in der zitierten Leitlinie / Onkopedia / OCP / Veröffentlichung entspricht (§§1–7).
2. **Iterations-Protokoll** der ausgeführten Pflege-Aktionen (Analyzer-/Validator-Läufe, Doku-Anpassungen, strukturelle Repository-Änderungen) — pro Iteration mit Datum, Auslöser, betroffenen Dateien und Verifikations-Ergebnissen (ab §8).

Beide Funktionen erfüllen gemeinsam die Audit-Pflicht aus `AGENTS.md` §3 und dienen als operative Evidenz menschlicher Aufsicht im Sinne der EU-AI-Act-Transparenzpflichten (siehe `AI_USAGE.md` §4).

Stand: 2026-10-13 · Iteration v0.2.0 · **112 Datenelemente** (51 aus v0.1 + 61 aus Klinik-Erhebungen und Leitlinien-Abgleich 2026-10; siehe §13). Historischer Stand v0.1 (2026-05-04): 51 Datenelemente (44 Erhebungs- + 7 Ergebnis-Artefakte).

## 1 Vorgehen

Für jedes Element wurde:

1. die zitierte Quelle geöffnet (PDF im Wissensbestand bzw. Onkopedia online),
2. die zitierte Sektion / Empfehlungs-Nr. / Tabelle aufgesucht,
3. der Belegtext mit der `definition_de` und dem `value_set`/`care_process` abgeglichen,
4. bei Abweichung die Quelle korrigiert oder ergänzt.

## 2 Ergebnisse je Phase

### Phase „Onkologische Nachsorge" (`elements/follow-up/`)

| Element | Quelle | Belegtext (Zitat-Eigenanteil) | Status |
| --- | --- | --- | --- |
| `structuredFollowUpPlan` | S3-LL Lung 4.0, Empf. 16.1 (EK) | „Nach Abschluss einer multimodalen Therapie ... sollte für jeden Patienten ein strukturierter Nachsorgeplan erstellt werden ... geeignet, Rezidive, Zweitkarzinome, Komplikationen ... zu erkennen." | belegt |
| `firstFollowUpVisitDate` | S3-LL Lung 4.0, Empf. 16.4 (EK) + 16.5 (B, 1a) | „Erste klinische Vorstellung nach Abschluss der Strahlentherapie soll innerhalb von 8 Wochen erfolgen." | belegt |
| `followUpInterval` | S3-LL Lung 4.0, Empf. 16.7 (EK) + Onkopedia NSCLC Tab. 12 + SCLC Tab. 9 | „in den ersten 2 Jahren vierteljährlich (alle 3 Monate), ab dem 3. Jahr halbjährlich ... nach 5 Jahren in ein Screeningprogramm" | belegt |
| `ctThoraxScan` | S3-LL Lung 4.0, Tab. 42 + Empf. 16.6 (A, 1a) | „Nach lokal ablativer Therapie des NSCLC im Stadium III soll zum Ausschluss einer Progression ein CT-Thorax durchgeführt werden" | belegt |
| `brainMriHighRisk` | S3-LL Lung 4.0, Empf. 16.8 (EK) + Onkopedia SCLC Tab. 9 | „Bei Hochrisikopatienten (z.B. EGF-R+, ALK+, ROS-1+, Adenokarzinome mit Stadium III) sollte ... regelmäßig ein Schädel-MRT durchgeführt werden." | belegt |
| `pulmonaryFunctionTest` | S3-LL Lung 4.0, Tab. 42 + Onkopedia NSCLC | „Lungenfunktionsprüfung, CO-Diffusionskapazität: Lungenfunktionseinschränkung, Pneumonitis." | belegt |
| `postTherapyComplication` | S3-LL Lung 4.0, Empf. 16.4/16.5 + Kap. 16.3.1 | „posttherapeutische Komplikationen ... erfasst und behandelt werden ... Pneumonitis, Ösophagitis, Strahlenfibrose ..." | belegt |
| `recurrenceOrSecondPrimary` | S3-LL Lung 4.0, Empf. 16.1 + Kap. 16.3.4 | „Rezidive, Zweitkarzinome, Komplikationen ... zu erkennen." | belegt |
| `smokingStatus` | S3-LL Lung 4.0, Empf. 16.3 (B, 2b) + S3-LL Tabakentw. | „Patienten mit Lungenkarzinom sollten nachhaltig motiviert werden, mit dem Tabakrauchen aufzuhören." | belegt |
| `tobaccoCessationCounselling` | S3-LL Lung 4.0, Empf. 16.3 (B) + S3-LL Tabakentw. | „Zur Unterstützung sollten die Patienten wirksame Hilfen zur Raucherentwöhnung erhalten." | belegt |
| `ecogPerformanceStatus` | **korrigiert** — neu: Onkopedia NSCLC Kap. 5.6 (Allgemeinzustand und Komorbidität) + S3-LL Palliativ Tab. 6 | „Der individuelle Allgemeinzustand wird in der Onkologie üblicherweise mit dem ECOG Performance Score (PS) angegeben." | korrigiert |
| `psychoOncologyReferral` | S3-LL Lung 4.0, Empf. 16.1 (EK) | „Bedarf an Psychoonkologie und Sozialberatung zu erkennen" | belegt |
| `distressThermometerScore` | S3-LL Palliativ Tab. 6 + OCP Principle 4 | „Distress-Thermometer mit Problemliste" | belegt |
| `survivorshipCarePlan` | AG LONKO; Klein 2026 | „Anamnese, Abschlussstatus, Epikrise, Spätfolgen, weiteres Prozedere, Diagnostik, Format" | belegt |

### Phase „Verlaufsbeobachtung / Surveillance" (`elements/surveillance/`)

| Element | Quelle | Status |
| --- | --- | --- |
| `systemicTherapyRegimen` | S3-LL Lung Empf. 16.9 + Onkopedia NSCLC Kap. 6 | belegt |
| `therapyLineNumber` | S3-LL Lung Kap. 16.1 (real-world vs. Studie) | belegt |
| `recistResponse` | S3-LL Lung Empf. 16.9 | belegt; **mCODE-Mapping ergänzt** (`CancerDiseaseStatus`) |
| `restagingImagingDate` | S3-LL Lung Empf. 16.9 | belegt |
| `adverseEventCtcae` | S3-LL Lung Empf. 16.9 | belegt |
| `immuneRelatedAdverseEvent` | S3-LL Lung Kap. 16.3.1 | belegt |
| `brainMriUnderTherapy` | S3-LL Lung Kap. 16.3.4 (NSCLC EGFR/ALK/ROS1; SCLC ED Watch-and-Wait, japanische Studie) | belegt |
| `patientReportedSymptomWeb` | Onkopedia NSCLC Kap. 8.2 (Denis 2017) | belegt |
| `qolEortcQlqC30` | **erweitert** — neu: OCP Step 5.4.1 + S3-LL Palliativ Tab. 9 (EORTC QLQ-C15-Pal) als zusätzliche Belege; S3-LL Lung Kap. 16.6 (Forschungsbedarf) zur Einordnung | korrigiert |
| `earlyPalliativeReferral` | S3-LL Palliativ Kap. 5.5 (Gleichzeitigkeit) + OCP Step 6 | belegt |
| `ecogPerformanceStatusSurveillance` | S3-LL Lung Empf. 16.9 | belegt |
| `weightChangePercent` | OCP Section 5.4 (malnutrition) | belegt |
| `molecularRetestingCtdna` | OCP Step 6.1 (re-biopsy / ctDNA) | belegt |

### Phase „Palliativversorgung" (`elements/palliative/`)

| Element | Quelle | Status |
| --- | --- | --- |
| `palliativeCareTier` | S3-LL Palliativ Kap. 5.4 (PBP/APV/SPV) | belegt |
| `complexityLevel` | S3-LL Palliativ Kap. 5.3 + Tab. 6 | belegt |
| `illnessPhase` | S3-LL Palliativ Kap. 5.3 + Tab. 6 (stabil/instabil/verschlechternd/sterbend) | belegt |
| `functionalStatus` | S3-LL Palliativ Tab. 6 (AKPS, ECOG, ADL, Barthel) | belegt |
| `symptomAssessmentInstrument` | S3-LL Palliativ Tab. 6 (MIDOS2, ESAS-r, IPOS, POS, Distress-Thermometer) | belegt |
| `dyspneaIntensityNrs` | S3-LL Palliativ Empf. 9.1 (A) + Tab. 9 (Dimensionen Atemnot) | belegt |
| `painIntensityNrs` | **klargestellt** — Kap. 10.2 als Hauptbeleg (Selbsteinschätzung NRS); Empf. 10.1 (A) explizit als Sonderfall Fremdeinschätzung getrennt | korrigiert |
| `painType` | S3-LL Palliativ Kap. 10.2 (Basisdiagnostik Schmerz) | belegt |
| `opioidDailyOmme` | S3-LL Palliativ Kap. 10.4 + 10.6 | belegt |
| `phq9DepressionScore` | S3-LL Palliativ Kap. 18.3 | belegt |
| `anxietyHadsScore` | S3-LL Palliativ Kap. 17.2 | belegt |
| `advanceCarePlanning` | S3-LL Palliativ Kap. 6.5 | belegt |
| `wishToDie` | S3-LL Palliativ Kap. 20.3 | belegt |
| `dyingPhaseDiagnosed` | S3-LL Palliativ Kap. 21.2 | belegt |
| `caregiverBurden` | S3-LL Palliativ Kap. 7.4 + Tab. 6 | belegt |
| `spiritualNeedsAssessment` | S3-LL Palliativ Kap. 19.3 + 19.5 | belegt |
| `advanceDirectiveDocument` | S3-LL Palliativ Kap. 6.5 | belegt |

## 3 Korrekturen v0.1 → v0.1.1

Drei Elemente wurden präzisiert (bei sonst unverändertem Inhalt — daher Patch-Version):

1. **`ecogPerformanceStatus.yaml` (followup)** — Hauptbeleg auf Onkopedia NSCLC Kap. 5.6 *Allgemeinzustand und Komorbidität* umgestellt; S3-LL Palliativ Tab. 6 als sekundärer Beleg behalten.
2. **`qolEortcQlqC30.yaml` (surveillance)** — OCP Step 5.4.1 und S3-LL Palliativ Tab. 9 (EORTC QLQ-C15-Pal) als Hauptbelege ergänzt; S3-LL Lung Kap. 16.6 (Forschungsbedarf) bleibt zur Einordnung.
3. **`painIntensityNrs.yaml` (palliative)** — Trennung der zwei Sachverhalte: §10.2 für Selbsteinschätzung NRS (Statement); Empf. 10.1 (A) ausdrücklich als Sonderfall „Fremdeinschätzung bei kognitiver/körperlicher Einschränkung".

Außerdem wurde **`recistResponse.yaml` (surveillance)** im Rahmen der Standards-Recherche um Multi-Standard-Mappings ergänzt (`obds`, `fhir-mii-kds`, `mcode`, `omop-cdm`).

## 4 v0.1.2 — Audit Ergebnisartefakte (Result-Datenelemente)

Audit entlang Akteur/Ziel-Achse identifizierte sieben Lücken bei Ergebnisartefakten — die zugehörigen Prozeduren waren erfasst, das Ergebnis fehlte. Sieben neue Datenelemente wurden ergänzt (Schema unverändert):

| Neu | Phase | Datentyp | Begründung |
| --- | --- | --- | --- |
| `ctThoraxFinding` | followup | CodeableConcept | Befundkategorie zum CT Thorax (stable / recurrent / second primary / inconclusive) |
| `brainMriFinding` | followup | CodeableConcept | Befundkategorie zur Schädel-MRT (Hirnmet vorhanden / stabil / kein Befund / unklar) |
| `fev1PercentPredicted` | followup | decimal % | FEV1 als % vom Soll — Ergebnis der Lungenfunktionsprüfung |
| `dlcoPercentPredicted` | followup | decimal % | DLCO als % vom Soll — Pneumonitis-Marker |
| `molecularResistanceFinding` | surveillance | CodeableConcept | Resistenz-Mutation (T790M, KRAS G12C u. a.) — Ergebnis ctDNA/Re-Biopsie |
| `adverseEventCtcaeGrade` | surveillance | integer 1–5 | CTCAE-Grad zum Adverse Event |
| `caregiverBurdenScore` | palliative | integer | Score-Wert zum Instrument (Zarit ZBI 0–88) |

Alle ergänzenden Elemente verlinken via `related_elements: specializes` zum jeweiligen prozeduralen Element.

## 5 Codings-Verifikation (v0.1.2)

Stichproben-Audit der SNOMED-CT- und LOINC-Codes; eine Korrektur und eine Display-Verfeinerung notwendig:

| Element | Befund | Aktion |
| --- | --- | --- |
| `fev1PercentPredicted` | SNOMED 50834005 ist *Forced vital capacity* (FVC), **nicht FEV1** | Code korrigiert auf SNOMED **59328004** *Forced expired volume in 1 second (observable entity)* |
| `ctThoraxFinding` | LOINC 59776-5 — Display war "Procedure findings Document"; korrekt ist "Procedure findings Narrative" | Display-String korrigiert |
| `adverseEventCtcaeGrade` | SNOMED 442452003 *Life threatening severity (qualifier value)* — verifiziert | OK |
| Übrige SNOMED-/LOINC-Codings (44 vorhandene + 5 neue) | nicht stichprobenweise verifiziert; im Augenmaß plausibel, da aus etablierten Standardrefsets | **offen** — vollständige Terminologie-Server-Validierung in nachfolgender Iteration |

**Methodischer Hinweis:** Eine vollständige Code-Validierung (alle 75+ Codings) braucht einen aktiven SNOMED-CT-Browser (Snowstorm/IHTSDO) bzw. LOINC-Lookup. In der aktuellen Iteration wurden nur die hochrisikoreichen oder neu hinzugefügten Codes punktuell verifiziert. Die im YAML notierten Codes sind als Author-Draft-Vorschläge zu betrachten und im klinischen Review zu validieren.

## 6 v0.1.3 — KDL-Mapping (Klinische Dokumentenklassen-Liste)

KDL ist seit 01.01.2024 verbindlich für die einheitliche Klassifikation klinischer Dokumente in Deutschland (DVMD; OID `urn:oid:1.2.276.0.76.5.451`; gematik TI-Terminologie). Sie ist nicht für jedes Datenelement sinnvoll — nur dort, wo das Element ein Dokument *ist* oder klar in einem typisierten Bericht *enthalten ist*.

**20 Datenelemente erhielten ein zusätzliches `kdl`-Coding** in `value_set.codings[]` neben den bestehenden SNOMED/LOINC/ICD-Codings. Schema unverändert.

| KDL-Code | Bezeichnung | Anzahl Elemente | Beispiel-Element |
| --- | --- | --- | --- |
| `DG020103` | CT-Befund | 3 | `ctThoraxFinding` |
| `DG020107` | MRT-Befund | 3 | `brainMriFinding` |
| `DG060108` | Dokumentationsbogen Lungenfunktionsprüfung | 3 | `fev1PercentPredicted` |
| `PT130102` | Molekularpathologiebefund | 2 | `molecularResistanceFinding` |
| `AD060106` | Tumorkonferenzprotokoll | 2 | `recistResponse` |
| `SD150101` | Follow up-Bogen | 2 | `survivorshipCarePlan` |
| `AM160104` | Patientenverfügung | 1 | `advanceDirectiveDocument` |
| `SD110105` | Palliativmedizinische Komplexbehandlungsdokumentation | 3 | `palliativeCareTier` |
| `VL010103` | Schmerzerhebungsbogen | 1 | `painIntensityNrs` |

**Quellen:**

- DVMD KDL 2024: <https://simplifier.net/kdl>
- gematik TI-Terminologie KDL CodeSystem 2024: <https://gemspec.gematik.de/ig/fhir/terminology/1.0.5/CodeSystem-kdl-cs-2024.html>
- Implementierungsleitfaden: <https://simplifier.net/guide/KDL-Implementierungsleitfaden-2024/>

Der KDL-Code spielt im FHIR-Mapping in `DocumentReference.type` bzw. `Composition.type` und ist die offizielle DE-Konvention für IHE XDS classCode. Damit ist die `ihe-xds`-Mapping-Brücke implizit etabliert.

**Wichtig — KDL und FHIR-Resource-Trennung:** Bei Datenelementen, die *Werte* in einem Dokument sind (z. B. FEV1-Wert im Lungenfunktionsbefund), bezieht sich der KDL-Code auf das *enthaltende Dokument*. Im FHIR-Mapping wird der KDL-Code dort als `DocumentReference.type` gesetzt, während der FEV1-Wert selbst eine `Observation` mit LOINC `20150-9` ist. Diese Mehrebenenlogik ist im Logical Model durch das Coexistieren mehrerer Codings im selben `value_set.codings[]`-Array sauber abgebildet.

## 7 v0.1.4 — ICD-O-3 + ICF aufgenommen, Bestandselemente geprüft

Auf explizite Nachfrage zur Klassifikations-Abdeckung wurden zwei zusätzliche Coding-Systeme registriert und punktuell auf passende Bestandselemente angewendet:

### Neu registriert (in `scripts/build-fhir-logical-models.py` SYSTEM_URL)

| System | Kanonische URL | Begründung |
| --- | --- | --- |
| `icd-o-3` | `urn:oid:2.16.840.1.113883.6.43.1` | Onkologische Histologie/Topographie. **Pflicht im oBDS** für Tumor-Histologie (M-Codes) und Topographie (T-Codes). |
| `icf` | `http://fhir.de/CodeSystem/bfarm/icf` | Funktion / Aktivität / Partizipation. Anwendbar bei Funktions- und Symptom-Elementen. |

**Nicht aufgenommen:** ICD-11 — in DE nicht produktiv (oBDS bleibt mittelfristig auf ICD-10/ICD-O-3); aktuelle Aufnahme würde Verwirrung erzeugen.

### Bindings auf Bestandselemente (Auswahl-Logik: nur direkte fachliche Anwendbarkeit)

| Element | Phase | Neu ergänzte Codings |
| --- | --- | --- |
| `recurrenceOrSecondPrimary` | followup | ICD-O-3 M-Codes 8140/3 (Adeno), 8070/3 (Plattenepithel), 8041/3 (Kleinzeller), 8012/3 (Großzelliges); ICD-O-3 T-Code C34.9 (Topographie) |
| `functionalStatus` | palliative | ICF d4 (Mobilität), d5 (Selbstversorgung) |
| `dyspneaIntensityNrs` | palliative | ICF b440 (Funktionen der Atmung) |
| `painIntensityNrs` | palliative | ICF b280 (Schmerz) |
| `dyingPhaseDiagnosed` | palliative | ICD-10-GM Z51.5 (Palliativbehandlung) |
| `palliativeCareTier` | palliative | ICD-10-GM Z51.5 (Palliativbehandlung) |
| `tobaccoCessationCounselling` | followup | ICD-10-GM Z71.6 (Beratung bei Tabakkonsum) |

### Bewusst nicht aufgenommen

- `painType` (nozizeptiv/neuropathisch): ICD-10-GM-Diagnosen (M79.2, R52, F45.4) wären semantisch ein anderes Konzept (Diagnose vs. Klassifikation des Schmerztyps).
- `phq9DepressionScore`: PHQ-9 ist Score-Wert, nicht F32-Diagnose; ICD-10-GM nicht direkt anwendbar.
- ECOG/Karnofsky/Barthel: keine direkten ICF-Codes verfügbar.
- Symptom-/PROM-Elemente ohne direkten ICF-Bezug: keine künstlichen Mappings.

### Auswirkung auf Schema und Pipeline

- **Schema unverändert** (Felder bleiben gleich; `value_set.codings.system` ist `string`, nicht enum-restringiert).
- `SYSTEM_URL` im FSH-Generator erweitert; alle FSH-Instances tragen die korrekten kanonischen URLs.
- CSV + Markdown-Mirror neu erzeugt.

## 8 v0.1.5 — Analyzer-Lauf gegen LL Lungenkarzinom v5.01 (Konsultationsfassung)

**Lauf:** `data-element-analyzer` (`.claude/agents/data-element-analyzer.md`) · **Eingabe:** S3-LL Lungenkarzinom Langversion 5.01, Konsultationsfassung 04/2026 (AWMF 020-007OL, Kommentarfrist bis 2026-05-02) · **Datum:** 2026-05-05.

**Aktualitäts-Check:** v5.01 ist die aktuelle Konsultationsfassung; KDL/mCODE/oBDS unverändert seit letztem Lauf.

### Identifizierte Änderungen — User-Konsultation pro Element

| Element-ID(s) | Quelle (LL v5.01) | Vorschlag | User-Entscheidung |
| --- | --- | --- | --- |
| `structuredFollowUpPlan`, `firstFollowUpVisitDate`, `followUpInterval`, `brainMriHighRisk`, `postTherapyComplication`, `recurrenceOrSecondPrimary`, `restagingImagingDate`, `recistResponse` | Empf. 16.1, 16.4, 16.7, 16.8, 16.9 — geprüft/modifiziert 2025; **Aufwertung EK → B** | `recommendation_grade: EK → B` | **angenommen** — alle 8 Elemente updaten |
| 14 Elemente mit `evidence.guideline_references.source = S3-LL Lungenkarzinom` | LL-Versionssprung v4.0 → v5.01 | `version: "4.0 (April 2025)" → "5.01 (Konsultationsfassung 04/2026)"` | **angenommen** — auf v5.01 (Konsultationsfassung) aktualisieren |
| `smokingStatus` | Empf. 4.1 v5.01 modifiziert: aktives Rauchen + E-Zigarette + Passivrauch | Definition erweitern; Codings ergänzen: SNOMED 722497008 (Vaping), 43381005 (Passive smoker) | **angenommen** — Definition + Codings erweitern |
| `tobaccoCessationCounselling` | Empf. 4.3/4.4 v5.01: ABC-Schema + DiGA + pharmakologische Therapie | Definition erweitern; Coding SNOMED 386516008 (Brief intervention); Hinweis auf DiGA in `instruction_de` | **angenommen** — Codings + Definition erweitern |
| `earlyPalliativeReferral` | Empf. 8.6 v5.01 modifiziert 2026: standardisiertes Symptomassessment + frühzeitige Palliativberatung | Definition erweitern; `related_elements: dependsOn → symptomAssessmentInstrument` | **angenommen** — Definition + related_elements |
| (kein Element) | Empf. 4.5 NEU 2026: Tabakentwöhnung im LDCT-Screening (opt-out) | Hinweis-Eintrag — Element wird bei Befüllung Phase `screening` berücksichtigt | **angenommen** — Audit-Hinweis, keine Element-Anlage in v0.1 |

### Delegation an Validator-Agent

Die eigentlichen Schreib-Operationen wurden gemäß §6 der Analyzer-Agent-Spec **an den `data-element-validator`-Agenten delegiert**. Dieser führt aus:

1. Patch der 14+ YAMLs (recommendation_grade-Updates, evidence.version-Bump, Codings-Erweiterungen smokingStatus + tobaccoCessationCounselling, earlyPalliativeReferral-Definition + related_elements)
2. Schema-Validierung
3. Codings-Re-Verifikation (insbesondere SNOMED 722497008, 43381005, 386516008)
4. CSV + Markdown-Mirror regenerieren
5. FHIR Logical Model regenerieren
6. Methodology §7 Iterations-Log: Eintrag „v0.1 LL-v5.01-Sync"
7. README Quellen-Liste: v5.01-Erwähnung
8. Audit-Eintrag-Erweiterung in diesem Abschnitt mit Validator-Lauf-Details

### Validator-Lauf-Ergebnisse (Datum 2026-05-05)

| Aktion | Anzahl | Details |
| --- | --- | --- |
| `recommendation_grade: EK → B` | 7 Elemente | structuredFollowUpPlan, followUpInterval, brainMriHighRisk, recurrenceOrSecondPrimary, restagingImagingDate, recistResponse, ctThoraxFinding |
| `evidence.guideline_references[].version` v4.0 → v5.01 | 25 Elemente | alle YAMLs, die `S3-LL Lungenkarzinom` referenzieren |
| `section`-Text rewrite | 6 Elemente | „(EK)" → „(B, geprüft 2025)" / „(B, modifiziert 2025)" für die aufgewerteten Empfehlungen |
| `smokingStatus.definition_de` | 1 Element | Erweiterung um E-Zigarette + Passivrauchexposition |
| `smokingStatus.value_set.codings` | 1 Element | +SNOMED 722498003 (Smokes electronic cigarettes), +SNOMED 43381005 (Passive smoker) |
| `tobaccoCessationCounselling.definition_de` | 1 Element | Erweiterung um ABC-Schema + DiGA |
| `tobaccoCessationCounselling.value_set.codings` | 1 Element | +SNOMED 386516008 (Tobacco use cessation education) |
| `tobaccoCessationCounselling.instruction_de` | 1 Element | DiGA-Hinweis (BfArM-DiGA-Verzeichnis) |
| `earlyPalliativeReferral.definition_de` | 1 Element | Erweiterung um „standardisiertes Symptomassessment regelmäßig" |
| `earlyPalliativeReferral.related_elements` | 1 Element | dependsOn → symptomAssessmentInstrument |
| Schema-Validierung | 51/51 OK | nach allen Patches |
| `catalog/data-dictionary.csv` + `data-dictionary.md` | regeneriert | 51 Zeilen |
| `derived/fhir-logical-model/` (FSH) | regeneriert | Logical Model + 51 Instances |
| `README.md` §6 Quellenbasis | aktualisiert | Eintrag jetzt v5.01-Konsultationsfassung statt v4.0 |
| `docs/methodology.md` §7 Iterations-Log | aktualisiert | neue Zeile „v0.1 LL-v5.01-Sync (Analyzer + Validator)" |
| `docs/methodology.md` §9 Quellen | aktualisiert | Lungenkarzinom-Eintrag auf v5.01 umgeschrieben mit Hinweis auf Tab. 48 (Übersicht der Änderungen) |

**Codings-Verifikations-Hinweis:** Die neu hinzugefügten SNOMED-Codes (722498003, 43381005, 386516008) wurden via `WebSearch` im SNOMED-Browser-Ökosystem geprüft. Codes 722498003 und 43381005 sind in HL7-FHIR-US-Core-ValueSets sowie ISP-Coding-Empfehlungen referenziert (plausibel). 386516008 ist als „Tobacco use cessation education" geläufig. Eine **vollständige Terminologie-Server-Validierung** (Snowstorm/IHTSDO) bleibt im klinischen Review nachzuholen.

### Hinweise zur Konsultationsfassung

- v5.01 ist **nicht final** — Kommentarfrist bis 2026-05-02. Die Quellenangabe `(Konsultationsfassung 04/2026)` macht das transparent.
- Erneuter Analyzer-Lauf nach Veröffentlichung der finalen v5 ist empfohlen — insbesondere zur Prüfung, ob Empf. 4.5 (Screening + Tabakentwöhnung) zusammen mit der Phase `screening` befüllt wird.
- Empfehlungsnummern in v5.01 haben sich teilweise verschoben (z. B. 8.11→8.10) — semantisch wurde die Empfehlung erhalten; Sektion-Referenzen bleiben gültig, sind aber im Validator-Lauf zu prüfen.

## 9 v0.1.6 — README-Neufassung (Projektkontext-Anpassung)

Datum: 2026-05-06 · Auslöser: Nutzer-Anweisung zur Angleichung an die README-Struktur des Schwester-Repositorys [`mihub-lung-cancer-pathway`](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway) und Auswertung des MiHUB-Projektantrags (`MiHUB_final.pdf`).

### 9.1 Geänderte Datei

| Datei | Änderungs-Typ | Begründung |
| --- | --- | --- |
| `README.md` | Komplettüberarbeitung | Strukturelle Angleichung an das Pathway-Repo; explizite Verankerung im MiHUB-Projektantrag (drei strategische Use Cases, Palliativ-Anchor in AP3/AP7/AP8); Entfernung aller schnell veraltenden „Bezug zu diesem Repository"-Inhalte (konkrete Element-Listen, Phasen-Stückzahlen, hartcodierte YAML-Pfade) |
| `README.proposal.md` | gelöscht | Zwischenstand für Review; nach Freigabe in `README.md` übernommen |

### 9.2 Inhaltliche Verifikation gegen MiHUB-Projektantrag (`MiHUB_final.pdf`, 61 S.)

| Aussage in der README | Antrags-Beleg |
| --- | --- |
| Drei strategische Use Cases | §3 Overall Objectives: „Prevention/Lung Cancer Screening, Cooperative Cancer Care (including palliative care), Follow-up/Long-Term Survivors (including palliative care)" |
| Palliativversorgung in AP7 (kooperativ) | §8.8 WP7: „patients in **advanced and palliative** lung cancer care"; Task 7.2 „palliative care requirements"; Task 7.3 „focusing on palliative care" |
| Palliativversorgung in AP8 (Nachsorge) | Abbildung 1: „Aftercare > Palliative Care"; §8.9 Task 8.1 „through stakeholder workshops (with WP9)" |
| Palliativversorgung als Phase im AP3-Pfad | §8.4 WP3: Pfad umfasst „screening, treatment, follow-up, **palliative**, and primary care" |
| Konsortialpartner | §1.2: TUD/ZMI · MUL Carl Thiem Cottbus · Klinikum Chemnitz · HSMW Mittweida |
| Cross-Hub Use Case Lungenkrebs | §8.1 + Abbildung 1: „Cross-Hub Use Case: Digital Support in Complex Patient Journeys — Lung Cancer" |
| Deliverables D6.2, D7.1–7.3, D8.1–8.5 | §§8.7–8.9 entsprechend; Fälligkeiten verifiziert (M9, M12, M24, M32, M36) |
| AP9-Klammer (User-Centered Design / ISO 9241-210) | §8.10 WP9; AP8 Task 8.1 „with WP9" |

### 9.3 Bewusst nicht aus dem Antrag übernommen

- **Förderkennzeichen `01ZZ2506A`** — im Antrag nicht enthalten (wird erst nach Bewilligung vergeben). Aus dem Pathway-Repo-README übernommen; Bestätigung durch das Konsortium ausstehend.
- **Repo-Name** — als Platzhalter `<repo-name>` belassen, da der finale Repo-Name auf der MiHUB-GitHub-Organisation noch nicht festgelegt ist.

### 9.4 Wartungs-Hinweis

Die README ist nun bewusst **frei von zustandsabhängigen Inhalten** (Element-Anzahl, Phasen-Stückzahlen, konkrete YAML-Beispielpfade, einzelne Score-Namen pro AP). Aktuelle Element-Bestände finden Reviewer:innen über die generierten Sichten:

- `docs/phases-overview.md` (lesefreundlich, autogeneriert)
- `catalog/data-dictionary.csv` und `.md` (vollständig, autogeneriert)

Damit reduziert sich der README-Pflegebedarf bei künftigen Datenelement-Änderungen auf null — Updates fließen automatisch in die generierten Sichten.

## 10 v0.1.7 — Audit-Log-Rename + neuer Sub-Agent `ai-usage-curator`

Datum: 2026-05-06 · Auslöser: Nutzer-Anweisungen zur Begriffsangleichung und zur Separation of Concerns für KI-Nutzungs-Disklosure.

### 10.1 Rename `verification-log.md` → `audit-log.md`

| Aktion | Anzahl Treffer |
| --- | --- |
| Datei umbenannt | 1 (`docs/verification-log.md` → `docs/audit-log.md`) |
| Referenz-Updates in 8 Dateien | `README.md`, `AGENTS.md`, `DISCLAIMER.md`, `GLOSSARY.md`, `AI_USAGE.proposal.md`, `docs/methodology.md`, `.claude/agents/data-element-analyzer.md`, `.claude/agents/data-element-validator.md` |
| H1-Überschrift angepasst | „Quellen-Verifikation — Stichprobenprotokoll" → „Audit-Log — Quellen-Verifikation und Iterations-Protokoll" |
| Untertitel | erweitert um Doppelfunktion (1) Quellen-Verifikation, (2) Iterations-Protokoll; expliziter Verweis auf `AGENTS.md` §3 und `AI_USAGE.md` §4 |

**Begründung:** Der bisherige Titel deckte den faktischen Inhalt nicht mehr vollständig ab — das Dokument hat sich von einem reinen Quellen-Belegtext-Audit zu einem allgemeinen Iterations- und Pflege-Audit entwickelt (Validator-Läufe, README-Anpassungen, Glossar-Patches, strukturelle Repository-Änderungen). Der neutralere Name `audit-log.md` ist besser anschlussfähig an die Compliance-Sprache (EU AI Act §50, COPE).

### 10.2 Neuer Sub-Agent `ai-usage-curator`

| Aktion | Beleg |
| --- | --- |
| Datei `.claude/agents/ai-usage-curator.md` neu angelegt | YAML-Frontmatter + System-Prompt; Format konsistent mit Analyzer/Validator |
| `AGENTS.md` aktualisiert | „zwei" → „drei" Sub-Agenten; neue Tabellenzeile; neuer Abschnitt „Trennung der Konzerne (Separation of Concerns)" mit disjunkter Zuständigkeits-Matrix |
| `.claude/agents/data-element-analyzer.md` ergänzt | neue Sektion „Verknüpfung mit `ai-usage-curator`" — leichter Hinweis-Mechanismus, kein automatischer Aufruf |
| `.claude/agents/data-element-validator.md` ergänzt | analoge Sektion |

**Begründung (Separation of Concerns):**

- **Unterschiedliche Trigger-Ereignisse:** Analyzer/Validator reagieren auf klinisch-inhaltliche Quellen (LL-/Onkopedia-Updates); Curator reagiert auf werkzeug-/governance-bezogene Ereignisse (Modell-Releases, Maintainer-Wechsel, EU-Guidance, Backlog-Erledigung).
- **Unterschiedliche Audit-Ebenen:** Analyzer/Validator-Audit ist element-/iterations-spezifisch; Curator-Audit ist repo-weit-strukturell. Eine Vermischung würde die Konsultations-Disziplin der bestehenden Agenten verwässern.
- **Spezialisiertes Compliance-Wissen:** Curator muss EU AI Act Art. 50, COPE, ICMJE, Linux-Kernel-/Red-Hat-Konventionen kennen — diese Last bleibt von den klinisch-inhaltlichen Agenten getrennt.

**Verknüpfungs-Mechanismus:** Analyzer und Validator dürfen am Ende eines Laufs einen `**Curator-Hinweis:**`-Eintrag in ihren Bericht aufnehmen, wenn sie ein werkzeug-/governance-bezogenes Trigger-Ereignis bemerken. Ein automatischer Curator-Lauf erfolgt nicht — die Entscheidung bleibt bei der Nutzer:in.

### 10.3 Konsistenz-Check

| Datei | Status |
| --- | --- |
| `README.md` | aktualisiert (Verweis auf Audit-Log) |
| `AGENTS.md` | aktualisiert (drei Agenten + Trennungs-Abschnitt) |
| `DISCLAIMER.md` | aktualisiert (Verweis auf Audit-Log) |
| `GLOSSARY.md` | aktualisiert (Verweis auf Audit-Log) |
| `AI_USAGE.proposal.md` | aktualisiert (Verweis auf Audit-Log) |
| `docs/methodology.md` | aktualisiert (Verweis auf Audit-Log) |
| `.claude/agents/data-element-analyzer.md` | aktualisiert (Verweis + Curator-Hinweis-Sektion) |
| `.claude/agents/data-element-validator.md` | aktualisiert (Verweis + Curator-Hinweis-Sektion) |

Letzter Repo-weiter Grep auf `verification-log`: **0 Treffer**.

## 11 v0.1.8 — `AI_USAGE.md` final übernommen + `DISCLAIMER.md` entfernt

Datum: 2026-05-06 · Auslöser: Nutzer-Anweisung zur finalen Übernahme der `AI_USAGE.proposal.md` und Entfernung redundanter, ausschließlich referenzierender Dokumente. Erledigt damit das Backlog-Item §11.3 aus dem AI_USAGE-Vorschlag.

### 11.1 Geänderte Dateien

| Aktion | Datei | Beleg |
| --- | --- | --- |
| `AI_USAGE.md` final überschrieben | `AI_USAGE.md` | aus `AI_USAGE.proposal.md` übernommen; §10 (DISCLAIMER-Subsumierungs-Tabelle) und §11.3 (DISCLAIMER-Backlog-Item) entfernt, da nicht mehr aktuell; Pflege-Hinweis im Header auf `ai-usage-curator`-Sub-Agent verweist |
| `DISCLAIMER.md` gelöscht | `DISCLAIMER.md` | inhaltlich vollständig in `AI_USAGE.md` aufgegangen — siehe Subsumierungs-Mapping aus dem Proposal-Stand v1 |
| `AI_USAGE.proposal.md` gelöscht | `AI_USAGE.proposal.md` | Zwischenstand für Review, nach Übernahme nicht mehr benötigt |
| `README.md` Badge umgelinkt | `README.md` | `[![Erstellung: KI-gestützt](…)](DISCLAIMER.md)` → `(AI_USAGE.md)`; Subtitle-Text analog |
| `AGENTS.md` Disclaimer-Sektion neu | `AGENTS.md` | Heading „Disclaimer" → „KI-Nutzungs-Disklosure"; Verweis auf `AI_USAGE.md` + `ai-usage-curator`; Curator-Tabellenzeile von DISCLAIMER-Cross-Konsistenz-Erwähnung bereinigt |
| `ai-usage-curator.md` bereinigt | `.claude/agents/ai-usage-curator.md` | Frontmatter-Description, §2 Konsultations-Pflicht und §3 Cross-Konsistenz: alle DISCLAIMER-Erwähnungen entfernt; README-Badge-Bullet vereinfacht („zeigt auf AI_USAGE.md") |

### 11.2 Konsistenz-Befund (Repo-weiter Grep)

| Pattern | Treffer | Status |
| --- | --- | --- |
| `verification-log` (lebende Refs) | 0 | ✓ vollständig migriert (siehe §10) |
| `DISCLAIMER` in Live-Doku | 0 | ✓ entfernt |
| `DISCLAIMER` in Audit-Log (historisch) | 3 | ✓ bewusst belassen (§10 Iterationshistorie, §11 vorliegender Eintrag) |
| `AI_USAGE.proposal` | 0 | ✓ entfernt |

### 11.3 Backlog-Stand `AI_USAGE.md` §11

| # | Maßnahme | Status nach diesem Lauf |
| --- | --- | --- |
| ehem. 3 | DISCLAIMER.md auf AI_USAGE.md umlenken oder entfernen | **erledigt** — Backlog-Item entfernt |
| 1 (neu) | PR-Template KI-Disclosure-Feld | offen |
| 2 (neu) | `Assisted-by:`-Commit-Trailer in CONTRIBUTING.md | offen |
| 3 (neu) | GitHub-Repo-Topic `ai-assisted` | offen |
| 4 (neu) | Datei-Header-Konvention für Markdown | offen |
| 5 (neu) | `git notes`-Rückannotation prüfen | offen |
| 6 (neu) | Klinisches Review-Board konstituieren | offen |
| 7 (neu) | EU-Guidance Q2 2026 gegenprüfen | laufend |

## 12 v0.1.9 — Datennutzung (`data_flows`), Erhebungs-/Dubletten-Tooling, vendor-neutrale Skills, Go-public-Artefakte

**Datum:** 2026-06-30 · **Auslöser:** Maintainer-Auftrag (Vorbereitung Veröffentlichung privat → öffentlich) · **KI-Unterstützung:** Claude Code (Opus 4.8).

**Schema (additive Minor-Erweiterung; alle 51 YAMLs bleiben gültig):**

| Änderung | Detail |
| --- | --- |
| `care_process.data_flows[]` | je Datenelement WO (System) · WER (Rolle) · WIE (`usage_type`) + optional `sector`/`mandatory`/`notes`; kontrollierte Vokabulare (System-Klassen, Nutzungsarten, Sektoren) im Schema-Enum + `GLOSSARY.md` §19 |
| Beispiel-Befüllung | `elements/follow-up/smokingStatus.yaml`: PVS/Hausärzt:in/capture · KIS/Onkolog:in/read · KIS/Pflege/update · DIZ/Forscher:in/secondary-use |
| Catalog | `build-catalog.py`: neue Spalte `care_process_data_flows` (CSV nun **24 Spalten**); Spaltenzahl in den generierten Doku-Texten dynamisch (`len(HEADER)`) — behebt einen bestehenden „22 Spalten"-Off-by-one |
| Issue-Formular | `.github/ISSUE_TEMPLATE/new-data-element.yml`: Feld „Datennutzung (WO/WER/WIE)" |

**Werkzeuge / Governance:**

| Artefakt | Zweck |
| --- | --- |
| `scripts/build-elicitation-workbook.py` + `import-elicitation-workbook.py` + `templates/datenelement-erhebung.xlsx` + `scripts/_elicitation.py` | Excel-Erhebungs-Vorlage (Klinik-Spur, Weg 2, schema-getrieben) + Import zu YAML-Entwürfen (`elements/_incoming/`, gitignored) |
| `scripts/check-duplicates.py` + Skill `check-duplicate-data-element` (+ `.github/workflows/duplicate-check.yml`) | Dubletten-/Ähnlichkeitsprüfung neuer Kandidaten vor Aufnahme |
| `skills/` als einzige Quelle + `.claude/skills`/`.claude/agents`/`.codex/skills`-Symlinks + `.github/copilot-instructions.md` + `.github/scripts/validate-agent-skills.py` + `skill-lint.yml`; `AGENTS.md` als vendor-neutraler Katalog | werkzeug-unabhängige Skill-/Sub-Agent-Bereitstellung; die 3 bestehenden Agenten nach `skills/` migriert |
| `DISCLAIMER.md`, `LICENSE` (CC BY 4.0), `LICENSE-APACHE-2.0.txt`, `CITATION.cff`, `CODE_OF_CONDUCT.md`, `.gitattributes`, `docs/go-public-checklist.md` | fehlende Go-public-Artefakte ergänzt (Disclaimer **DRAFT**, ausstehend Justiziariat/DPO) |
| Branches `dev` (Integration) / `main` (Release) | Beitrags-/Release-Workflow |

**Verifikation:** `validate.py` (51/51 OK), `build-catalog.py` (Drift-frei), `skill-lint` (4 Skills + 4 Agenten OK), Excel-Round-trip (Vorlage → Import → valides YAML), `check-duplicates.py` (bekannte Dublette „Rauchstatus"→`smokingStatus` NAH-DUBLETTE; Negativfall EIGENSTÄNDIG).

**Doku-Konsistenz:** README, CONTRIBUTING, `docs/howto-add-element.md`, `docs/github-workflow.md`, `docs/methodology.md`, `GLOSSARY.md`, `AI_USAGE.md` aktualisiert (3 Beitrags-Wege, 24 Spalten, `dev`/`main`, Skills, Disclaimer/Lizenz/Zitat).

## 13 v0.2.0 — Leitlinien-Resync (S3 5.1, Onkopedia 04/2025 + 08/2026), Terminologie-Verifikation (MII TermServ), Klinik-Erhebungen (Nachsorge-WG + Allgemeinmedizin), neue Phase `primarycare`

**Datum:** 2026-10-13 · **Auslöser:** Maintainer-Auftrag (Acht-Punkte-Prüfung: Repo-Stand, Excel-Erhebungen, MII-Repos/TermServ/MCP, Excel-Abdeckung, Leitlinien-Abdeckung, Zertifikat-Nutzbarkeit, Terminologie-Abgleich, Umsetzung + PR) · **KI-Unterstützung:** Claude Code (Fable 5.1) mit drei Read-only-Recherche-Agenten (je Leitlinie) · **Werkzeuge:** MII TermServ (Ontoserver, FHIR-API, mTLS mit TU-Dresden-Funktionszertifikat) und AskMIIAnything MCP-Server v0.9.0 (Live-Test der Werkzeuge `lookup_code`, `validate_code`, `expand_valueset` über stdio).

Der zusammengeführte Updateplan (A Excel-Erhebung → Repo · B Leitlinien-Abdeckung · C Terminologie) wurde in einem Pull Request gegen `dev` umgesetzt; die vollständigen Recherche-Berichte liegen als Momentaufnahmen unter [`docs/reviews/2026-10-13-leitlinien-abgleich/`](reviews/2026-10-13-leitlinien-abgleich/) und [`docs/reviews/2026-10-13-terminologie-verifikation.md`](reviews/2026-10-13-terminologie-verifikation.md).

### 13.1 Erratum zu §8 — Empfehlungsgrade und Versionsablösung der S3-LL Lungenkarzinom

- **Aktuell publiziert ist die Langversion 5.1 (Juli 2026, AWMF 020-007OL)**; sie löst die Konsultationsfassung 5.01 (04/2026, Konsultation 03.04.–02.05.2026, laut Leitlinienreport 5.0 nur redaktionelle Korrekturen) und die Erstfassung 5.0 (Juni 2026) ab. 5.0 → 5.1 änderte ausschließlich Arzneimittelzulassungen (Lurbinectedin, Tarlatamab) und URLs; **Kap. 15 und 16 sind in 5.0 und 5.1 zeichenidentisch** und seit v4.0 inhaltlich unverändert (Tab. 48 enthält keine 16.x-Zeile). Neuer Versions-Pin in allen 25 S3-referenzierenden YAMLs: `5.1 (Juli 2026, AWMF 020-007OL)`.
- **Die in §8 angenommene „Aufwertung EK → B“ der Empf. 16.1/16.4/16.7/16.8/16.9 ist nicht belegt:** in v4.0, 5.0 und 5.1 sind 16.1, 16.2, 16.4, 16.7, 16.8 und 16.9 Konsensbasierte Empfehlungen (EK); 16.3 B/LoE 3, 16.5 A/B/LoE 2, 16.6 A/LoE 2 (Evidenzlevel-Notation in 5.x von Oxford-2009-Buchstaben auf Oxford-2011-Ziffern umgestellt). Die Fehlzuordnung erklärt sich vermutlich aus der „sollte“-Formulierung (≙ B-Stärke) der EK-Empfehlungen. **Korrigiert:** Grad B → EK in `structuredFollowUpPlan`, `followUpInterval`, `brainMriHighRisk`, `recurrenceOrSecondPrimary`, `ctThoraxFinding`, `recistResponse`, `restagingImagingDate`; LoE 1a → 2 bzw. 2b → 3 in `firstFollowUpVisitDate` (jetzt 16.4 EK + 16.5 A/2 getrennt), `postTherapyComplication`, `ctThoraxScan` (16.6 nur noch für das einmalige CT NSCLC Stadium III vor Durvalumab; Nachsorge-Rhythmus über 16.7/Tab. 44), `smokingStatus`, `tobaccoCessationCounselling`.
- **Tabellen-Umnummerierung:** die Nachsorge-Indikationstabelle ist in 5.x **Tab. 44** (v4.0/5.01: Tab. 42; „Tab. 42“ bezeichnet in 5.x die Atemnot-Instrumente in Kap. 14) → korrigiert in `ctThoraxFinding`, `ctThoraxScan`, `pulmonaryFunctionTest`, `fev1PercentPredicted`, `dlcoPercentPredicted` (Lungenfunktions-Trio zusätzlich Grad EK → n/a, da Indikationstabelle ohne Grad).
- **Kap. 15 Rehabilitation** ist in 5.1 „wegen laufender Überarbeitung ausgesetzt“ (Empf. 15.1–15.5 „ausgesetzt 2026“) — Reha-Referenzen als vorläufig gekennzeichnet; **Kap. 4.2 Tabakrauchen** vollständig überarbeitet (Empf. 4.1–4.4 modifiziert, 4.5 neu; alle A/LoE 1) → Empf. 4.2 (Erfassung), 4.3 (ABC-Schema/DiGA) und 4.4 (Pharmakotherapie) als Primärbelege an `smokingStatus` bzw. `tobaccoCessationCounselling`; G-BA-Erstattung NET/Vareniclin seit 20.08.2025 in `instruction_de`.
- **Onkopedia-Pins:** NSCLC `Stand 03/2026` existiert online nicht (weder gültig noch archiviert) → `Stand April 2025` (7 YAMLs + Doku); SCLC `Stand 09/2025` → `Stand August 2026` (Kap. 0 nennt nur Therapieänderungen; Kap. 9/10, Tab. 9 unverändert; Archiv nicht gedifft → UNSICHER). Die Behauptung in §13-alt/Limitationen, NSCLC Tab. 12 habe eine Monatsspalte 9, war falsch (nur SCLC Tab. 9).

### 13.2 Leitlinien-Abdeckung (Nachsorge/Surveillance) — Bilanz und umgesetzte Änderungen

| Leitlinie (Stand) | Items geprüft | COVERED | PARTIAL | MISSING | Bericht |
| --- | --- | --- | --- | --- | --- |
| S3-LL Lungenkarzinom 5.1 (Juli 2026) | Empf. 16.1–16.9, Tab. 44, Kap. 4.2, 15, 11, Stmt. 8.6, Empf. 8.77 | 15 | 12 | 12 | [`s3-lungenkarzinom-5.1.md`](reviews/2026-10-13-leitlinien-abgleich/s3-lungenkarzinom-5.1.md) |
| Onkopedia NSCLC (April 2025) | 19 (Kap. 7, 8.1, 8.2, Tab. 12, 6.1.6.2.1.1, 6.2.2.1) | 4 | 12 | 3 | [`onkopedia-nsclc-2025-04.md`](reviews/2026-10-13-leitlinien-abgleich/onkopedia-nsclc-2025-04.md) |
| Onkopedia SCLC (August 2026) | 19 (Kap. 9, 10.2, Tab. 9, 6.1.1.3/6.1.1.5/8.2.2) | 6 | 8 | 4 (+2 kein LL-Item) | [`onkopedia-sclc-2026-08.md`](reviews/2026-10-13-leitlinien-abgleich/onkopedia-sclc-2026-08.md) |

Umgesetzt (Bestandselemente): quellenspezifische Intervalle statt eines gemischten Rasters (`ctThoraxScan`, `pulmonaryFunctionTest`, `brainMriHighRisk`, `followUpInterval` — S3 Q3M/Q6M vs. Onkopedia NSCLC Tab. 12 vs. Onkopedia SCLC Tab. 9 mit 9 Zeitpunkten), Onkopedia-Kapitel als Zusatzreferenzen (NSCLC 8.1/8.2/6.1.6.2.1.1/6.2.2.1/7; SCLC 10.2/6.1.2.1/6.1.1.5/8.2.2/6.1.1.4.1.7/9), Pneumonitis-Risikofenster 6–24 Monate (`constraints_de`), ALK+-MRT-Raster 3–6 Monate, zyklusbasierte SCLC-Ansprechensbeurteilung, Population der PRO-Web-Nachsorge (Denis 2017), Psychoonkologie-/Palliativ-Referenzen (Empf. 16.2, 8.77, Stmt. 8.6, Kap. 11), Defekt `Q6-9M` → `Q6-9W` behoben. **Lücken → neue Elemente** (§13.5): Nachsorgetermin/Anamnese/körperliche Untersuchung, PCI-Status (Steuerbedingung „LD ohne PCI“), kurative Therapiemodalität (Steuerbedingung „nach RT“), ZNS-Risikoprofil, kuratives Rezidivpotenzial (6–8-Wochen-Intervall), Reha-/Sozialberatung + Reha-Maßnahme, Screening-Übergang nach Jahr 5, strukturierter Verlaufsplan Stadium IV (16.2), Basisevaluation nach Induktion (16.9), Verlaufskontroll-Visite 3–6 Wochen, Kontaktform (Video), Basislabor unter Systemtherapie, konditionale Nachsorge-Untersuchungen aus Tab. 44 (Röntgen Thorax, Sonografie Abdomen, Bronchoskopie, PET-CT, Abdomen-CT, Labor).

### 13.3 Terminologie-Verifikation gegen den MII TermServ

**Zugang:** Das Funktionszertifikat (GÉANT S/MIME, EKU TLS Web Client Authentication, gültig bis 2028-07-16) ist für die mTLS-Authentifizierung am MII TermServ (`https://ontoserver.mii-termserv.de/fhir`) nutzbar — `metadata`, `CodeSystem/$lookup`, `ValueSet/$expand` (POST mit Inline-ValueSet + Textfilter) funktionieren; die implizite Expansion `?fhir_vs` nur für SNOMED CT. Verfügbare Systeme: SNOMED CT 20260701, LOINC 2.83, ICD-10-GM 2026, OPS 2026, ATC 2026, KDL, ICD-O-3 (deutsche Displays); **nicht verfügbar:** ICF, MedDRA, HL7-Core-ValueSets (z. B. `smoking-status`). Der MCP-Server **AskMIIAnything v0.9.0** (`medizininformatik-initiative/AskMIIAnything`) wurde mit demselben Zertifikat (`TERMINOLOGY_CLIENT_CERT`/`_KEY`) erfolgreich gegen den TermServ getestet; er pinnt `mcp[cli]>=1.0.0`, importiert aber `mcp.server.fastmcp` (in mcp 2.x umbenannt) — lauffähig nur mit `mcp<2` (Upstream-Befund). In der MII-GitLab-Gruppe `mii-termserv` (96 Projekte: Terminologie-NPM-Pakete, `txq`-Browser, Packager) existiert **kein** MCP-Server/-Client.

**Ergebnis (vor dem Update, 51 Elemente, 141 Codings):** 94 gefunden · 2 inaktiv (KDL AD060106 → Nachfolger SD150103) · 38 nicht auffindbar · 7 nicht verifizierbar (ICF, MedDRA). Davon **13 semantisch falsche Codes** (existierender Code mit anderer Bedeutung), u. a. 385763009 = „Hospice care“ (`psychoOncologyReferral`), 410429000 = „Cardiac arrest“ (`painType`), 89283-6 = CT-Untersuchung (`dyspneaIntensityNrs`), 233604007 = „Pneumonia“ (Pneumonitis), 85756007 = „Body tissue structure“ (Fernmetastase), 736378000 = „Medication management plan“ (Survivorship Care Plan), 419099009 = „Dead“ (Sterbephase), 190787008 = „Abetalipoproteinemia“ (Autoimmunhepatitis), 182840001 = „Drug treatment stopped“ (Complete Response), 73831-0 = Depressionsscreening Jugendliche (EORTC QLQ-C30), 8341-0 = Trockengewicht (Gewichtsverlust). **ATC 2024-Restrukturierung** (L01XC → L01FF, L01XE → L01E) betraf 6 Codes; OPS-Fehler: 1-712 = Spiroergometrie (→ 1-710 Ganzkörperplethysmographie), 3-225 = CT Abdomen mit KM (Region ergänzt), 3-820 = MRT Schädel mit KM (+ 3-800 nativ).

**Umgesetzt (85 Coding-Änderungen: 48 ersetzt, 24 ergänzt, 13 entfernt; 34 Anzeigetexte synchronisiert — vollständige Tabelle im Review-Dokument):** alle nicht auffindbaren/falschen Codes durch verifizierte Konzepte ersetzt; `recistResponse` auf das mCODE-ValueSet ConditionStatusTrend (SNOMED CT) umgestellt; Display-Texte auf die TermServ-Anzeigetexte gesetzt (Regel: `display` = Anzeigetext des Servers, Stand 2026-10-13). **Ohne Standard-Code** (Status `pending-mapping` + `notes`): NCCN Distress-Thermometer, Zarit-Score, Atemnot-NRS (LOINC kennt nur PROMIS-T-Score/MRC-Grad), MIDOS2/ESAS-r; ohne Konzept: AKPS, oMME, Mischschmerz, PCI-Prozedur, Vorsorgevollmacht-Dokumentklasse (SNOMED 425393008 als Ersatz). ICF- und MedDRA-Codes bleiben unverändert mit Vermerk „nicht verifizierbar“.

**Ergebnis nach dem Update (112 Elemente, 408 Codings):** 369 OK · 32 lokal · 7 nicht verifizierbar · **0 nicht auffindbar · 0 inaktiv** (`scripts/verify-terminology.py`, neu).

### 13.4 Excel-Erhebungen — Abgleich und Entscheidungen

| Mappe | Zeilen | Bestand bestätigt | zusammengeführt (Dublette) | neu |
| --- | --- | --- | --- | --- |
| Nachsorge-WG (`datenelement-erhebung_Nachsorge_WG_ak.xlsx`, 2026-07-30; Vorlage um Spalte »Kategorie (optional)« erweitert, Definitionsspalte entfernt) | 78 | 51 (DE-001…018, 027…041, 047…064 — Labels identisch mit dem Katalog; Zusatzreferenzen waren bereits vorhanden; Kategorie je Element übernommen) | DE-044/045/046 → `restagingImagingDate` (CT Thorax/Abdomen/Becken), DE-067 → `painIntensityNrs`, DE-068 → `dyspneaIntensityNrs` (je S3-LL-Lungenkarzinom-Referenz Kap. 14 ergänzt, Wortlaut-Verifikation ausstehend), DE-011 → Label-Ergänzung „Schmerz“ bereits in `definition_de` enthalten | 22 Zeilen → 22 Elemente (DE-019/020 + DE-042/043 → Visite/Anamnese/Untersuchung je Phase; DE-021…026 → 6 konditionale Untersuchungen; DE-065/066 → 2 Palliativ-Elemente; DE-069…078 „Übergreifende Datenelemente — LoTeCaS-GP“ → Phase `primarycare`) |
| Allgemeinmedizin (`datenelement-erhebung (1)-Amed.xlsx`, 2026-10-13, Kontakt AK) | 38 (DE-001…039 ohne DE-024) | — (hausärztliche Perspektive, bislang nicht im Katalog) | Befund/Bildgebung/Diagnostik → `diagnosticReportDocument`; Therapiebarkeit/Tumorboard/Therapieplanung → `tumorBoardDecision` + `treatmentIntent`; Komplikationen/Nebenwirkungen → `treatmentSideEffectOrComplication`; Laborwerte/Auffälligkeiten → `laboratoryResultsReport`; Stammdaten/Kontakt → 4 Stammdaten-Elemente (gemeinsam mit LoTeCaS-GP) | 38 Elemente in `elements/primary-care/` |

Tooling-Befund: beide Mappen wichen von der Vorlage ab (eingefügte Spalte, fehlende Definitionsspalte, leere Definitionen) → Importer und Dubletten-Check ordnen Spalten jetzt **über die Kopfzeile** zu (robust gegen eingefügte/umsortierte Spalten; Klammerzusätze wie „(optional)“ ignoriert) und erzeugen bei fehlender Definition einen Entwurf mit Platzhalter + `issues`-Hinweis statt die Zeile zu verwerfen. Round-trip verifiziert: WG-Mappe → 78 Entwürfe (Kategorien erkannt), Allgemeinmedizin → 38 Entwürfe, Vorlage → 0 (nur Beispielzeile).

### 13.5 Neue Elemente (61) — Übersicht

| Phase | name | Bezeichnung | Kategorie | Quellen |
| --- | --- | --- | --- | --- |
| followup | `followUpVisitDate` | Nachsorgetermin — Datum (Anamnese und körperliche Untersuchung) | kontakt-visite | S3-LL Lungenkarzinom; Onkopedia NSCLC; Onkopedia SCLC; Expert:innen-Erhebung MiHUB |
| followup | `followUpHistoryFinding` | Nachsorge-Anamnese — Befund | befund | S3-LL Lungenkarzinom; Onkopedia NSCLC; Onkopedia SCLC; Expert:innen-Erhebung MiHUB |
| followup | `physicalExaminationFinding` | Körperliche Untersuchung — Befund | befund | S3-LL Lungenkarzinom; Onkopedia NSCLC; Onkopedia SCLC; Expert:innen-Erhebung MiHUB |
| followup | `curativeTreatmentModality` | Kurative Therapiemodalität (Eingangsgröße des Nachsorgeplans) | prozedur | Onkopedia NSCLC; S3-LL Lungenkarzinom |
| followup | `brainMetastasisRiskProfile` | Individuelles Risiko für zerebrale Metastasierung | assessment | S3-LL Lungenkarzinom; Onkopedia NSCLC |
| followup | `curativeRecurrencePotential` | Kuratives Potenzial bei Rezidiv / Zweitkarzinom | versorgungsplanung | Onkopedia NSCLC; Onkopedia SCLC |
| followup | `rehabilitationAndSocialCounselling` | Information/Beratung zu Rehabilitation und sozialrechtlichen Ansprüchen | mitbetreuung | Onkopedia NSCLC; Onkopedia SCLC; S3-LL Lungenkarzinom |
| followup | `rehabilitationMeasure` | Rehabilitationsmaßnahme (Setting, onkologischer Schwerpunkt) | prozedur | Onkopedia NSCLC; S3-LL Lungenkarzinom |
| followup | `prophylacticCranialIrradiationStatus` | Prophylaktische Schädelbestrahlung (PCI) — Status | prozedur | Onkopedia SCLC; S3-LL Lungenkarzinom |
| followup | `screeningProgramEnrolment` | Übergang in ein Lungenkrebs-Früherkennungsprogramm | versorgungsplanung | S3-LL Lungenkarzinom |
| followup | `chestXRayFollowUp` | Röntgen Thorax in der Nachsorge | bildgebung | S3-LL Lungenkarzinom; Expert:innen-Erhebung MiHUB |
| followup | `abdominalUltrasoundFollowUp` | Sonografie Abdomen in der Nachsorge | bildgebung | S3-LL Lungenkarzinom; Expert:innen-Erhebung MiHUB |
| followup | `bronchoscopyFollowUp` | Bronchoskopie in der Nachsorge | prozedur | S3-LL Lungenkarzinom; Onkopedia SCLC; Expert:innen-Erhebung MiHUB |
| followup | `petCtFollowUp` | PET-CT in der Nachsorge | bildgebung | S3-LL Lungenkarzinom; Onkopedia SCLC; Expert:innen-Erhebung MiHUB |
| followup | `ctAbdomenFollowUp` | CT Abdomen in der Nachsorge | bildgebung | S3-LL Lungenkarzinom; Expert:innen-Erhebung MiHUB |
| followup | `laboratoryTestFollowUp` | Laborparameter in der Nachsorge | laborbefund | S3-LL Lungenkarzinom; Expert:innen-Erhebung MiHUB |
| surveillance | `surveillanceVisit` | Verlaufskontroll-Visite unter Systemtherapie (Anamnese und körperliche Untersuchung) | kontakt-visite | S3-LL Lungenkarzinom; Onkopedia NSCLC; Expert:innen-Erhebung MiHUB |
| surveillance | `postInductionEvaluationDate` | Basisevaluation nach Abschluss der Induktionsbehandlung | kontakt-visite | S3-LL Lungenkarzinom; Onkopedia SCLC |
| surveillance | `consultationModality` | Kontaktform der Verlaufskontrolle (Präsenz / Video / Telefon) | kontakt-visite | Onkopedia NSCLC |
| surveillance | `laboratoryPanelSurveillance` | Basislabor unter Systemtherapie | laborbefund | Onkopedia NSCLC; S3-LL Lungenkarzinom |
| surveillance | `structuredSurveillancePlan` | Strukturierter Verlaufsplan vorhanden (Stadium IV) | versorgungsplanung | S3-LL Lungenkarzinom |
| palliative | `qualityOfLifeScore` | Lebensqualität (Selbsteinschätzung) in der Palliativversorgung | prom | S3-LL Lungenkarzinom; S3-LL Palliativmedizin; Expert:innen-Erhebung MiHUB |
| palliative | `treatmentDecisionDocumentation` | Dokumentation der Entscheidungen und Maßnahmen zur Behandlung | dokument | S3-LL Lungenkarzinom; S3-LL Palliativmedizin; Expert:innen-Erhebung MiHUB |
| primarycare | `patientName` | Name der Patient:in | stammdaten | Expert:innen-Erhebung MiHUB; Expert:innen-Erhebung MiHUB |
| primarycare | `birthYear` | Geburtsjahr | stammdaten | Expert:innen-Erhebung MiHUB |
| primarycare | `administrativeGender` | Geschlecht | stammdaten | Expert:innen-Erhebung MiHUB |
| primarycare | `patientContactMasterData` | Kontakt-, Adress- und Sprachangaben der Patient:in | stammdaten | Expert:innen-Erhebung MiHUB |
| primarycare | `lastPracticeContactDate` | Letzter Kontakt in der Hausarztpraxis | kontakt-visite | Expert:innen-Erhebung MiHUB |
| primarycare | `plannedFollowUpAppointment` | Geplante Wiedervorstellung / Verlaufskontrolle | kontakt-visite | Expert:innen-Erhebung MiHUB |
| primarycare | `cancerDiagnosis` | Krebsdiagnose(n) | diagnose | Expert:innen-Erhebung MiHUB; Expert:innen-Erhebung MiHUB; andere Empfehlungen |
| primarycare | `tumorLocalisation` | Tumorlokalisation | diagnose | Expert:innen-Erhebung MiHUB |
| primarycare | `tumorHistology` | Histologie | befund | Expert:innen-Erhebung MiHUB |
| primarycare | `tnmStage` | TNM-Stadium / UICC-Stadiengruppe | befund | Expert:innen-Erhebung MiHUB |
| primarycare | `currentTumorStatus` | Aktueller Tumorstatus | befund | Expert:innen-Erhebung MiHUB; andere Empfehlungen |
| primarycare | `comorbidity` | Komorbiditäten / weitere Diagnosen | diagnose | Expert:innen-Erhebung MiHUB; Expert:innen-Erhebung MiHUB |
| primarycare | `acuteIntercurrentIllness` | Akute (interkurrente) Erkrankung | diagnose | Expert:innen-Erhebung MiHUB |
| primarycare | `cancerTreatmentHistory` | Erfolgte Tumortherapie | prozedur | Expert:innen-Erhebung MiHUB; Expert:innen-Erhebung MiHUB; andere Empfehlungen |
| primarycare | `treatmentStatus` | Therapiestatus | versorgungskontext | Expert:innen-Erhebung MiHUB |
| primarycare | `immunizationStatus` | Impfstatus | medikation | Expert:innen-Erhebung MiHUB |
| primarycare | `currentMedicationPlan` | Aktuelle Medikation / Medikationsplan (BMP/eMP) | medikation | Expert:innen-Erhebung MiHUB; Expert:innen-Erhebung MiHUB |
| primarycare | `coTreatingProviderContact` | Kontaktdaten der Mitbehandler:innen | administrativ | Expert:innen-Erhebung MiHUB; Expert:innen-Erhebung MiHUB |
| primarycare | `ongoingSupportiveServices` | Laufende Therapien und Anbindungen (Physio, Ergo, Pflegedienst, SAPV …) | mitbetreuung | Expert:innen-Erhebung MiHUB |
| primarycare | `diagnosticReportDocument` | Befundbericht Diagnostik (Bildgebung, Endoskopie, Biopsie) | dokument | Expert:innen-Erhebung MiHUB; andere Empfehlungen |
| primarycare | `dischargeOrVisitReport` | Entlassbrief / Arztbrief | dokument | Expert:innen-Erhebung MiHUB; andere Empfehlungen |
| primarycare | `tumorBoardDecision` | Tumorboardbeschluss (inkl. Therapiebarkeit und Therapieplanung) | versorgungsplanung | Expert:innen-Erhebung MiHUB |
| primarycare | `treatmentIntent` | Therapieintention | versorgungsplanung | Expert:innen-Erhebung MiHUB |
| primarycare | `recommendationsForPrimaryCare` | Empfehlungen / weiteres Prozedere für die Hausarztpraxis | versorgungsplanung | Expert:innen-Erhebung MiHUB; andere Empfehlungen |
| primarycare | `patientGoalsAndPreferences` | Zielsetzungen und Wünsche der Patient:in | versorgungsplanung | Expert:innen-Erhebung MiHUB |
| primarycare | `psychoOncologyContact` | Psychoonkologische Gespräche / Unterstützung | mitbetreuung | Expert:innen-Erhebung MiHUB |
| primarycare | `mentalHealthStatus` | Mentale und psychische Situation | assessment | Expert:innen-Erhebung MiHUB |
| primarycare | `referralOrder` | Überweisung | administrativ | Expert:innen-Erhebung MiHUB |
| primarycare | `reasonForEncounter` | Beratungsanlass / Symptome | befund | Expert:innen-Erhebung MiHUB |
| primarycare | `historyTakingPrimaryCare` | Hausärztliche Anamnese | prozedur | Expert:innen-Erhebung MiHUB |
| primarycare | `laboratoryResultsReport` | Laborbefund (inkl. Auffälligkeiten) | laborbefund | Expert:innen-Erhebung MiHUB |
| primarycare | `treatmentSideEffectOrComplication` | Nebenwirkung / Komplikation der Tumortherapie (als Diagnose) | diagnose | Expert:innen-Erhebung MiHUB |
| primarycare | `socialSituation` | Soziale Situation | sozialanamnese | Expert:innen-Erhebung MiHUB |
| primarycare | `standardizedAssessmentScore` | Standardisiertes Assessment (Score) | assessment | Expert:innen-Erhebung MiHUB |
| primarycare | `responsiblePrimaryCarePhysician` | Zuständige Hausarztpraxis | administrativ | Expert:innen-Erhebung MiHUB |
| primarycare | `workIncapacityCertificate` | Arbeitsunfähigkeit (AU) | administrativ | Expert:innen-Erhebung MiHUB |
| primarycare | `riskFactorAndAlert` | Risikofaktoren / Warnhinweise | diagnose | Expert:innen-Erhebung MiHUB |
| primarycare | `bodyMassIndex` | Body-Mass-Index (BMI) | messwert | Expert:innen-Erhebung MiHUB |

Alle neuen Elemente: `publication_status: AuthorDraft`, `version_number: 0.1.0`, `creation_date: 2026-10-13`, Codings gegen den MII TermServ verifiziert (lokale Platzhalter nur bei `no-standard-found`), `related_elements` zu den Bestandselementen gesetzt. Klinik-elizitierte Elemente tragen die Quelle `Expert:innen-Erhebung MiHUB` mit Mappe + Zeilen-ID (`DE-0xx`) in `section`; Elemente mit Kliniker-Fundstellen, deren Wortlaut nicht gegengeprüft wurde (S3 Kap. 14.x, Empf. 14.7/14.8), sind entsprechend gekennzeichnet.

### 13.6 Schema und Tooling

| Änderung | Detail |
| --- | --- |
| `phase` Enum + ID-Pattern | + `primarycare` (Hausärztliche Versorgung / sektorenübergreifende Basisdaten); Ordner `elements/primary-care/`; `build-catalog.py`, FSH-Generator (PhasesCS), CODEOWNERS (`@mihub-ap8/lead-primarycare`), Issue-Formular, Excel-Vorlage nachgezogen |
| `category` (optional) | 17 klinische Kategorien der Nachsorge-WG (befund, bildgebung, assessment, messwert, kontakt-visite, versorgungsplanung, mitbetreuung, prozedur, diagnose, sozialanamnese, dokument, laborbefund, prom, medikation, versorgungskontext, stammdaten, administrativ); in allen 112 Elementen gesetzt; CSV-Spalte `category` (jetzt **25 Spalten**), Phasen-Übersicht 9 Spalten, FSH `category` + CategoryCS/VS, Excel-Spalte »Kategorie«, Issue-Dropdown; `GLOSSARY.md` §20 |
| `evidence.guideline_references[].source` | + `Expert:innen-Erhebung MiHUB` (Klinik-/Hausarzt-Erhebungen ohne Leitlinienbeleg) |
| `scripts/verify-terminology.py` | neu: `$lookup` je Coding gegen einen FHIR-Terminologieserver (Default MII TermServ, mTLS per `--cert/--key`), Statusbericht + JSON; Exit-Code ≠ 0 bei NOT-FOUND/INACTIVE |
| `scripts/_elicitation.py`, `import-elicitation-workbook.py`, `check-duplicates.py` | kopfzeilenbasierte Spaltenzuordnung (`rows_by_header`), Platzhalter bei fehlender Definition, Kategorie-Mapping |

### 13.7 Verifikation

`validate.py` 112/112 OK · `build-catalog.py` drift-frei (CSV 25 Spalten, 112 Zeilen; Phasen-Übersicht 4 Phasen) · `verify-terminology.py`: 369 OK / 32 lokal / 7 nicht verifizierbar / 0 nicht auffindbar · Excel-Round-trip (beide Kliniker-Mappen + Vorlage) · `check-duplicates.py` Self-Mode (Treffer ausschließlich über gemeinsame KDL-Dokumentklassen bzw. beabsichtigte Phasen-Pendants, z. B. `ecogPerformanceStatus` ↔ `ecogPerformanceStatusSurveillance`) · `skill-lint` 4 Skills + 4 Agenten OK · FSH-Generator 112 Instanzen (lokal, gitignored).

### 13.8 Offene Punkte (für das klinische Review)

1. Wortlaut-Verifikation der Kliniker-Fundstellen S3-LL Lungenkarzinom Kap. 14.1 / 14.3.2 / Empf. 14.7 / 14.8 (Palliativ-Elemente).
2. Bedeutung von „(X)“ in Onkopedia Tab. 12/Tab. 9 ist in den Leitlinien nicht legendiert (Lesart: fakultativ).
3. S3-LL Palliativmedizin: Pin `3.01 (Konsultationsfassung 03/2026)` — Finalisierung noch zu prüfen (außerhalb dieses Laufs). → **erledigt 2026-10-14:** finale Fassung 3.0 (Juli 2026), siehe §14.1.
4. Nachsorge **nach** PCI (MRT? Neurokognition?) — Onkopedia SCLC macht keine Vorgabe; `postTherapyComplication` enthält den Spätfolgen-Code.
5. Röntgen Thorax / Sonografie Abdomen in der Nachsorge: S3-Option (Empf. 16.7), von Onkopedia nicht vorgesehen — Aufnahme auf Wunsch der Nachsorge-WG, klinisch zu bestätigen.
6. Kodierungslücken (Distress-Thermometer, Zarit, Atemnot-NRS, AKPS, oMME, Mischschmerz, PCI, „verwandte Tabakprodukte“) → SNOMED-CT-/LOINC-Anträge oder lokales ValueSet im `mihub`-Namensraum.
7. Dubletten-Heuristik gewichtet gemeinsame KDL-Dokumentklassen-Codes hoch (viele NAH-DUBLETTE-Treffer im Self-Mode) — Gewichtung prüfen.
8. Die 38 `primarycare`-Elemente stammen aus einer Einzelerhebung (Allgemeinmedizin, Kontakt AK) — Konsentierung mit weiteren Hausärzt:innen / LoTeCaS-GP ausstehend; Datenschutz-Hinweis für Stammdaten (personenbezogen) ist als `constraints_de` vermerkt.

## 14 v0.2.0 (Fortsetzung) — Zweitprüfung gegen die Primärquellen, Mapping-Audit, Konsistenzprüfungen

**Datum:** 2026-10-14/15 · **Auslöser:** Maintainer-Auftrag „Datenelemente zur Nachsorge (aftercare, palliativ, long term survivors) nochmals anhand der Primärquellen verifizieren und ggf. korrigieren; auf semantische Korrektheit achten“ sowie Vorbereitung des Nachsorge-Releases · **KI-Unterstützung:** Claude Code (Opus 5.5) mit Multi-Agenten-Workflows (Verifizierer, je zwei Skeptiker mit unterschiedlicher Linse, Zusammenführung) · **Werkzeuge:** MII TermServ (mTLS, `$lookup`/`$expand`), lokal entpackte FHIR-Pakete (MII KDS 2025–2027-Ballot, ISiK 6.0.0, KBV MIO/eAU, gematik ePA, mCODE STU4, Genomics Reporting STU3), oBDS-XSD 3.0.5. Bericht mit Kennzahlen, Befunden und Änderungstabelle je Element: [`docs/reviews/2026-10-14-zweitpruefung.md`](reviews/2026-10-14-zweitpruefung.md).

### 14.1 Quellen und Pins

| Quelle | Ergebnis |
| --- | --- |
| S3-LL Palliativmedizin | Pin `3.01 (Konsultationsfassung 03/2026)` → **`3.0 (Juli 2026, AWMF 128-001OL)`** (final, gültig bis 20.07.2031). Kap.-10-Empfehlungsnummern ab 10.2 um +1 verschoben; Konsensempfehlungen in 3.0 als EK. Erledigt damit §13.8 Nr. 3. |
| S3-LL Rauchen und Tabakabhängigkeit | Version „1.0“ nicht belegt → **3.1** (Stand 01/2021, Langversion 03/2021; Gültigkeit bis 31.12.2025 abgelaufen, Aktualisierung angemeldet 12/2024). |
| AG LONKO / Klein 2026 | In `survivorshipCarePlan` vermengt → getrennte Referenzen; „2022“ nicht belegt (AG-LONKO-Papiere Stand 17./18.06.2021). Klein-Titel in README/Methodik vervollständigt. |
| S3-LL Lungenkarzinom 5.1, Onkopedia NSCLC 04/2025 und SCLC 08/2026, OCP 2nd ed. (Update 07/2025) | Pins bestätigt (aktuell). OCP-Referenzen zeigen auf das Dokument statt auf die Übersichtsseite. |
| Nicht graduierende Quellen | AWMF-Grade („Statement“, LoE) bei Onkopedia, OCP und AG LONKO entfernt (`n/a`). |
| Neu (je ein Element, Quelle `andere`) | S3-LL Psychoonkologie 2.1 (`distressThermometerScore`), Onkopedia „Impfungen bei malignen Erkrankungen“ (`immunizationStatus`), EORTC QLQ-C30 Scoring Manual (`qolEortcQlqC30`). |

### 14.2 Inhaltliche Zweitprüfung (alle 112 Elemente)

687 Änderungsvorschläge aus 22 Verifizierer-Gruppen; 88 von mindestens einer Linse widerlegt und verworfen; 599 von beiden Linsen bestätigt, davon 216 mit Teilkorrektur zusammengeführt (206 korrigiert übernommen, 7 unverändert, 3 verworfen). **597 Änderungen angewendet** (Referenzen 129 ergänzt/74 präzisiert, 140 Felder, Codings 42 ersetzt/48 ergänzt/26 entfernt, 80 offene Punkte, Beziehungen 46/12); jede Code-Änderung beim Schreiben live am MII TermServ geprüft (0 abgelehnt). Modelländerungen: `curativeTreatmentModality` 1..*, `adverseEventCtcaeGrade` CodeableConcept, `qolEortcQlqC30` decimal, `responsiblePrimaryCarePhysician` 0..1. Manuell: Zeilenverweise lokaler Textfassungen aus zwei Issue-Texten entfernt, überholter Kurz-Issue in `painType` durch den zusammengeführten Issue ersetzt, Folgeänderung `value_set.notes` in `anxietyHadsScore`.

### 14.3 Standard-Mappings

Zentrale Prüfung aller 115 Mapping-Einträge (26 distinkte Ziele) gegen die publizierten Pakete: 7 Ziele existierten nicht (MII Onkologie/Bildgebung unter `core/` statt `ext/`, Profil „imagingstudy“, MII-Profil „Raucher“, oBDS-Seite `/feldbeschreibung`), weitere zeigten auf HTML-/IG-Startseiten oder semantisch unpassende Profile. 151 Operationen formuliert und gegen die lokalen Pakete gegengeprüft (2 widerlegt, 4 beim Zusammenführen verworfen) → **145 angewendet** in 57 Elementen (74 ersetzt, 38 ergänzt, 33 offene Punkte zu Repräsentationsunterschieden). Jede geschriebene FHIR-Canonical existiert als StructureDefinition-`url` in den Paketen (maschinell geprüft). Mapping-Einträge 115 → 153, distinkte Ziele 26 → 57. Nur-Ballot-Profile gekennzeichnet. 9 offene Punkte, die eine Mapping-Korrektur verlangten, aufgelöst bzw. reduziert.

### 14.4 Schema, Validator und Verweise

| Änderung | Detail |
| --- | --- |
| `related_elements[].target` | Konvention vereinheitlicht: vollständige Element-ID (`mihub.lung.<phase>.<name>.v<maj>.<min>`); Schema-Pattern; bisher 98 Ziele als bloßer Name, 13 als ID → alle normalisiert (134 Namen umgestellt, 0 unaufgelöst). |
| `scripts/validate.py` | Katalogweite Konsistenz: `id` beginnt mit `mihub.lung.<phase>.<name>.v`, Dateiname = `name`, Ordner passt zur Phase, Verweisziele existieren (keine Selbstverweise), `id`/`name`/`uuid` katalogweit eindeutig. |
| `CITATION.cff`, README | Zenodo-Concept-DOI 10.5281/zenodo.21083229 und Versions-DOIs der Release Candidates eingetragen. |

### 14.5 Verifikation

`validate.py` (inkl. neuer Konsistenzprüfungen) 112/112 OK · `build-catalog.py` neu erzeugt (CSV 25 Spalten, 112 Zeilen) · `verify-terminology.py` gegen den MII TermServ: 430 Codings — 392 OK, 31 lokal, 7 nicht verifizierbar (ICF, MedDRA), 0 nicht auffindbar, 0 inaktiv, keine Anzeigetext-Abweichung · MedDRA-Codes gegen das MII-ValueSet `mii-vs-onko-nebenwirkung-art` (CTCAE v4.03) geprüft · `check-duplicates.py` Self-Mode: 57 eigenständig, 54 Nah-Dublette, 1 verwandt (vorher 52/57/3; Treffer weiterhin über gemeinsame KDL-Klassen und Phasen-Pendants, keine neue Dublette) · `skill-lint` 4 Skills + 4 Agenten OK · FSH-Generator 112 Instanzen · `dependsOn`-Zyklen 7 → 4.

### 14.6 Offene Punkte (für das klinische Review)

1. 80 neue `issues[]` aus der Zweitprüfung und 33 aus dem Mapping-Audit (Repräsentation in den nationalen Profilen); Schwerpunkte im Bericht, Abschnitt 5.
2. 88 verworfene Vorschläge sind nicht angewendet; sie können im Review erneut aufgegriffen werden (Liste in den Arbeitsdaten der Prüfung).
3. Modelländerung `responsiblePrimaryCarePhysician` 0..1 klinisch rückbestätigen (Erhebung Allgemeinmedizin hatte Pflichtangabe gesetzt).
4. Nur-Ballot-Profile (MII Lungenfunktion, Soziodemographie, Kardiologie 2027-Ballot) sind als solche gekennzeichnet; bei Release der Module erneut prüfen.
5. **Element-Versionierung:** Nach `docs/howto-add-element.md` §C wären die Datentyp-Änderungen (`adverseEventCtcaeGrade`, `qolEortcQlqC30`) Major- und die Kardinalitätsänderungen mindestens Minor-Änderungen; im AuthorDraft-Stadium wurde die Regel bisher nicht angewendet (alle Elemente `0.1.0`). → **erledigt 2026-10-15:** Regel neu gefasst und angewendet, siehe §14.7.
6. **`dependsOn`-Zyklen:** vier Zyklen um `recurrenceOrSecondPrimary` und die Bildgebung; Semantik von `dependsOn` (Auslöser vs. Datengrundlage) festlegen.

### 14.7 Element-Versionierung

Die Regeln in `docs/howto-add-element.md` §C waren in sich widersprüchlich (ID-Suffix `v<major>.<minor>`, aber Minor-Sprung ohne neue ID; `1.0.0` schon für Entwürfe) und wurden im Entwurfsstadium nie angewendet (alle 112 Elemente `0.1.0`, auch nach den Änderungen seit `v0.1.0-rc.2`). Neu gefasst: Bezugspunkt ist die zuletzt veröffentlichte Fassung; im Entwurfsstadium (`0.x`) nicht brechend → Patch (ID gleich), brechend → Minor mit neuem ID-Suffix; ab der Erstfreigabe `1.0.0` gelten Major-Sprünge mit neuem Element. `validate.py` prüft, dass ID-Suffix und `version_number` übereinstimmen und der letzte `provenance.history`-Eintrag der aktuellen Version entspricht.

Anwendung auf die 51 in `v0.1.0-rc.1/-rc.2` veröffentlichten Elemente (Vergleich gegen den Tag `v0.1.0-rc.2`):

| Ergebnis | Elemente |
| --- | --- |
| **brechend nach fester Regel** (Datentyp; Codes aus `required`-Bindung entfernt/ersetzt) → `0.2.0`, ID `v0.2` | `adverseEventCtcaeGrade`, `anxietyHadsScore`, `distressThermometerScore`, `dyspneaIntensityNrs`, `painType`, `qolEortcQlqC30`, `recistResponse`, `smokingStatus` |
| **brechend nach Urteil** (Definition geändert; zwei unabhängige Prüfer, Linsen klinische Bedeutung und Datenkompatibilität; einig oder bei geteiltem Urteil konkrete Umdeutung bestehender Werte) → `0.2.0`, ID `v0.2` | `brainMriFinding`, `brainMriUnderTherapy`, `caregiverBurdenScore`, `ctThoraxFinding`, `molecularResistanceFinding`, `psychoOncologyReferral`, `spiritualNeedsAssessment`, `structuredFollowUpPlan` |
| nicht brechend → `0.1.1`, ID unverändert | 35 Elemente (u. a. 16, deren Definition die Prüfer übereinstimmend als Präzisierung einstuften) |
| neu seit dem letzten Release → `0.1.0` (Erstveröffentlichung mit 0.2.0-rc.1) | 61 Elemente |

Die früheren IDs der 16 Elemente stehen in `provenance.history[0].id`; Verweise im Katalog zeigen auf die neuen IDs.

### 14.8 Herkunft und Nachprüfbarkeit je Element

Bisher ließ sich eine Fundstelle nur durch eigenes Suchen in der Quelle nachprüfen; Entstehung, Versionen und Prüfläufe eines Elements standen nur im Audit-Log. Neu (optionale Schemafelder, Minor-Schema-Änderung):

| Feld | Inhalt | Stand |
| --- | --- | --- |
| `evidence.guideline_references[].quote` | wörtliches Kurzzitat, das die Fundstelle belegt | **328/328** Referenzen; maschinell gegen die Textfassungen der Quellen (S3-LL Lungenkarzinom 5.1, S3-LL Palliativmedizin 3.0, S3-LL Tabak 3.1, Onkopedia NSCLC/SCLC, OCP, AG LONKO, Klein 2026, S3-LL Psychoonkologie 2.1, Onkopedia Impfungen, EORTC-Manual) bzw. den Mappen-Auszug geprüft — 328 gefunden |
| `…[].locator`, `…[].accessed` | präziser Fundort (Kapitel/Empfehlung/Tabelle/Seite) bzw. Anker im Mappen-Auszug; Prüfdatum | alle Referenzen |
| `provenance.origin` | Herkunftsart (Erstbefüllung aus Leitlinien, Leitlinien-Abgleich, Expert:innen-Erhebung mit Mappe und Zeile, Quellenrecherche), Datum, Verweis | alle 112 Elemente |
| `provenance.history` | Versionen mit Datum, Änderung und Verweis (frühere ID bei brechenden Änderungen) | alle 112 Elemente |
| `provenance.verification` | Prüfläufe (Terminologie 2026-10-13 und -15, Zweitprüfung, Mapping-Audit, Zitatprüfung) mit Ergebnis je Element und Bericht | alle 112 Elemente |

Neu: [`docs/reviews/2026-10-13-erhebungen.md`](reviews/2026-10-13-erhebungen.md) — Auszug der beiden Klinik-Erhebungsmappen (116 Zeilen, ohne Kontaktspalte) mit Ankern je Zeile als Herkunftsnachweis der 56 Referenzen `Expert:innen-Erhebung MiHUB`. Neu: `scripts/verify-quotes.py` — prüft die Zitate gegen eigene Textfassungen der Quell-PDFs (die Quellen liegen urheberrechtlich nicht im Repo); Toleranz nur für Silbentrennung und eingeschobenen Spaltentext des PDF-Layouts.

## 15 Vorbereitung der Phase `screening` (Datenelement-Erhebung)

**Datum:** 2026-10-14/15 · **Auslöser:** Maintainer-Auftrag „Screening-Episode für die Datenelementerhebung vorbereiten; passende Quellen suchen“ (Ausgangspunkt: Arbeitsnotiz „Vorarbeiten für das Teilmodul Früherkennung: Raucheranamnese und Eignungsprüfung“, Stand 06.10.2026) · **KI-Unterstützung:** Claude Code (Opus 5.5), Multi-Agenten-Recherche mit Gegenprüfung · **Ergebnis:** [`docs/screening/`](screening/).

### 15.1 Quellenrecherche und Kandidaten

Sechs Recherche-Perspektiven (Recht, Leitlinien, Befundung, Standards, Evidenz, Prozess entlang des BPMN-Modells `lung-cancer-screening-pathway`) lieferten 309 Kandidaten und rund 160 Quellenfunde; die Konsolidierung ergab 77 Kandidaten in 13 Prozessgruppen und 40 Quellen. Je Kandidat prüften ein Quellen-Skeptiker (Fundstelle, Wortlaut, Verbindlichkeit) und ein Dubletten-/Scope-Skeptiker (Abgleich mit den 112 Bestandselementen): **53 behalten, 24 verworfen** (21 Dublette/Scope, 1 Quelle, 2 beide). Verbindlichkeit der behaltenen Kandidaten nach Gegenprüfung: 16 Pflicht nach Norm, 7 bedingt, 6 mittelbar, 1 Soll-Vorschrift, 1 geteilt, 13 Leitlinie, 9 keine. Zehn Kandidaten sollen Bestandselemente spezialisieren (u. a. `smokingStatus`, `referralOrder`, `ctThoraxScan`), statt sie zu duplizieren.

### 15.2 Umgesetzt (dieser Schritt)

| Änderung | Detail |
| --- | --- |
| Phase `screening` | Schema-Enum + ID-Pattern, Ordner `elements/screening/` (noch leer), `build-catalog.py`, Excel-Dropdown, FSH `PhasesCS`, Issue-Formular, CODEOWNERS (`@mihub-ap8/lead-screening`) — Minor-Schema-Änderung |
| Quellen-Enum | + `LuKrFrühErkV`, `G-BA KFE-RL` (Minimalvariante; erweiterte Variante = Entscheidung E23 im Dossier) |
| `docs/screening/` | Dossier (Quellen, Prozessmatrix, 53 Einzelblätter, verworfene Kandidaten, Umsetzungsvorschlag U1–U10, Entscheidungsfragen E1–E24), vorbefüllte Erhebungsmappe (DE-S01 … DE-S53; Round-trip über den Importer für alle 53 Zeilen validiert), `quellen.json`, Einstiegsseite |
| GLOSSARY §21 | Screening-Begriffe wörtlich aus LuKrFrühErkV §§ 1–5 (Packungsjahr, Zulässigkeit, Befundkategorien, Erst-/Zweitbefundung u. a.) |

### 15.3 Codes, Profile und Herkunft der Kandidaten (2026-10-15)

Je Gruppe ermittelte ein Agent die Codes am MII TermServ, ein zweiter die Profilziele über alle Standards (MII KDS, ISiK, IPS, KBV, Basisprofil DE, gematik, mCODE, DICOM SR, IHE, openEHR); je eine Skeptiker:in prüfte Codes bzw. Profile (314/317 Codes und 293/300 Ziele bestätigt, 122 Teilkorrekturen), ein dritter Schritt führte die Korrekturen zusammen. Ergebnis: 53 schema-valide Entwürfe unter `docs/screening/entwuerfe/` (nicht im Katalog). Abschließende maschinelle Prüfung: 294/294 Standard-Codes am MII TermServ gefunden und aktiv (61 lokale Platzhalter), 214/214 FHIR-Canonicals in den Paketen, 151/151 Zitate wörtlich in den beschafften Quelltexten (ein als Zitat ausgewiesener paraphrasierter Satz wurde durch den Wortlaut des Whitepaper-Supplements ersetzt). `scripts/verify-terminology.py` kennt jetzt DICOM DCM, RadLex, NCIt und vollständige System-URLs. Vorbefüllte Mappe neu aus den Entwürfen erzeugt (Round-trip 53/53). Prüfprotokoll: `docs/screening/pruefprotokoll.json`.

### 15.4 Offene Punkte

1. Entscheidungsfragen E1–E24 (Dossier, Abschnitt 7) mit Praxis, Radiologie, Datenschutz/Justiziariat und MI-Team klären — mindestens E1–E3 (Raucheranamnese, Packungsjahre), E12 (Lung-RADS neben den §-Kategorien), E21–E23 (Modellierung).
2. ~~Codes gegen den MII TermServ prüfen~~ → erledigt 2026-10-15 (§15.3); offen bleiben die 61 lokalen Platzhalter (Konzeptbedarf).
3. DPIA-Berührungspunkte (Einwilligungen, Portal-Selbstauskunft, Rückkanal aus der Abklärung) vor der Aufnahme der Gruppen G5/G11/G12 klären.
4. Befunde am BPMN-Screeningmodell (Dossier, Abschnitt 8.4) an die Modellierer:innen des Pfad-Repositorys geben.

## 16 Limitationen

- Eine **Kapitel-Tiefe-Verifikation** (vollständiger Zitatvergleich Wort-für-Wort über alle 51 Elemente) wurde stichprobenartig durchgeführt; eine vollständige textliche Validierung ist Teil des klinischen Reviews in der nachfolgenden Iteration.
- **Onkopedia** ändert online schrittweise — die Versionen-Pins (seit 2026-10-13: NSCLC `Stand April 2025`, SCLC `Stand August 2026`) müssen bei nächster Re-Verifikation gegen die dann aktuelle Online-Fassung erneut geprüft werden; die SCLC-Archivfassung 09/2025 wurde nicht gegen 08/2026 gedifft (Kap. 0 nennt keine Nachsorge-Änderung).
- Die **Onkopedia-Tabellen** wurden 2026-10-13 aus dem HTML-Markup verifiziert: NSCLC Tab. 12 hat die Monatsspalten 3/6/12/18/24/36/48/60 (**keine** Spalte 9 — frühere Angabe korrigiert), SCLC Tab. 9 die Spalten 3/6/9/12/18/24/36/48/60; „(X)“ ist in beiden Leitlinien nicht legendiert.
- Die hier gewählten **Empfehlungsgrade/Evidenzlevel** spiegeln die formal in der Leitlinie ausgewiesenen Werte; bei Konsensbasierten Empfehlungen (EK) ist kein Evidenzlevel zugeordnet — als `n/a` codiert.
- **Konsultationsfassungen** (z. B. S3-LL 5.01) sind nach Finalisierung nicht mehr abrufbar; Annahmen über ihren Inhalt bleiben UNSICHER — daher werden nur finale Fassungen gepinnt (§13.1).
- **Terminologie-Verifikation** belegt die Existenz und den Anzeigetext eines Codes, nicht die klinische Eignung der Zuordnung; ICF und MedDRA sind auf dem MII TermServ nicht verfügbar und bleiben unverifiziert.
- Die **Kliniker-Fundstellen** der Excel-Erhebung (S3-LL Kap. 14.x, Empf. 14.7/14.8) wurden ohne Wortlautprüfung übernommen und sind in den YAMLs entsprechend gekennzeichnet.
- Die **Zweitprüfung vom 2026-10-14** ist KI-gestützt (Verifizierer und je zwei Skeptiker); die konservative Regel „verwerfen, sobald eine Linse widerlegt“ kann berechtigte Korrekturen verworfen haben (88 Vorschläge, nicht angewendet). Die Primärquellen lagen als Textfassungen der PDFs vor; Tabellen- und Spaltenzuordnungen bleiben eine mögliche Fehlerquelle.
- **Mapping-Ziele** wurden gegen lokal geladene Paketstände geprüft (MII KDS bis 2027-Ballot, ISiK 6.0.0 u. a.); neuere Paketversionen können Canonicals oder Bindungen ändern.
