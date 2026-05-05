# Quellen-Verifikation — Stichprobenprotokoll

Dieses Dokument protokolliert die Re-Verifikation der erhobenen Datenelemente gegen die zitierten Primärquellen. Ziel: nachvollziehbar belegen, dass jede `evidence.guideline_references[]`-Angabe einem Belegtext in der zitierten Leitlinie / Onkopedia / OCP / Veröffentlichung entspricht.

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

## 7 Limitationen

- Eine **Kapitel-Tiefe-Verifikation** (vollständiger Zitatvergleich Wort-für-Wort über alle 51 Elemente) wurde stichprobenartig durchgeführt; eine vollständige textliche Validierung ist Teil des klinischen Reviews in der nachfolgenden Iteration.
- **Onkopedia** ändert online schrittweise — die Versionen-Pins (`Stand 03/2026`, `Stand 09/2025`) müssen bei nächster Re-Verifikation gegen die dann aktuelle Online-Fassung erneut geprüft werden.
- Die **Onkopedia-Tabellen** (Tab. 12 NSCLC, Tab. 9 SCLC) wurden auf die genaue Spalten-Belegung (Monatsspalten 3/6/9/12/18/24/36/48/60) verifiziert.
- Die hier gewählten **Empfehlungsgrade/Evidenzlevel** spiegeln die formal in der Leitlinie ausgewiesenen Werte; bei Konsensbasierten Empfehlungen (EK) ist kein Evidenzlevel zugeordnet — als `n/a` codiert.
