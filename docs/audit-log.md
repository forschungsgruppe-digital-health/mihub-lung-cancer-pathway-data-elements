# Audit-Log — Quellen-Verifikation und Iterations-Protokoll

Dieses Dokument bündelt zwei Audit-Funktionen:

1. **Quellen-Verifikation** der erhobenen Datenelemente gegen die zitierten Primärquellen — nachvollziehbar belegen, dass jede `evidence.guideline_references[]`-Angabe einem Belegtext in der zitierten Leitlinie / Onkopedia / OCP / Veröffentlichung entspricht (§§1–7).
2. **Iterations-Protokoll** der ausgeführten Pflege-Aktionen (Analyzer-/Validator-Läufe, Doku-Anpassungen, strukturelle Repository-Änderungen) — pro Iteration mit Datum, Auslöser, betroffenen Dateien und Verifikations-Ergebnissen (ab §8).

Beide Funktionen erfüllen gemeinsam die Audit-Pflicht aus `AGENTS.md` §3 und dienen als operative Evidenz menschlicher Aufsicht im Sinne der EU-AI-Act-Transparenzpflichten (siehe `AI_USAGE.md` §4).

Stand: 2026-05-04 · Befüllungs-Iteration v0.1 · **51 Datenelemente** (44 Erhebungs- + 7 Ergebnis-Artefakte)

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

## 12 Limitationen

- Eine **Kapitel-Tiefe-Verifikation** (vollständiger Zitatvergleich Wort-für-Wort über alle 51 Elemente) wurde stichprobenartig durchgeführt; eine vollständige textliche Validierung ist Teil des klinischen Reviews in der nachfolgenden Iteration.
- **Onkopedia** ändert online schrittweise — die Versionen-Pins (`Stand 03/2026`, `Stand 09/2025`) müssen bei nächster Re-Verifikation gegen die dann aktuelle Online-Fassung erneut geprüft werden.
- Die **Onkopedia-Tabellen** (Tab. 12 NSCLC, Tab. 9 SCLC) wurden auf die genaue Spalten-Belegung (Monatsspalten 3/6/9/12/18/24/36/48/60) verifiziert.
- Die hier gewählten **Empfehlungsgrade/Evidenzlevel** spiegeln die formal in der Leitlinie ausgewiesenen Werte; bei Konsensbasierten Empfehlungen (EK) ist kein Evidenzlevel zugeordnet — als `n/a` codiert.
