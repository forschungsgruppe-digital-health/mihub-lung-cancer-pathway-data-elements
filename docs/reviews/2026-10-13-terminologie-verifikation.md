# Terminologie-Verifikation gegen den MII TermServ — 2026-10-13

> **Momentaufnahme.** Jedes `value_set.codings[]`-Element wurde per `CodeSystem/$lookup` gegen den MII TermServ (Ontoserver, mTLS mit TU-Dresden-Funktionszertifikat; SNOMED CT 20260701, LOINC 2.83, ICD-10-GM/OPS/ATC 2026, KDL, ICD-O-3) geprüft — Skript: `scripts/verify-terminology.py`. Ersatzcodes wurden per `ValueSet/$expand` (Textfilter) recherchiert und per `$lookup` bestätigt. Die Umsetzung ist in `docs/audit-log.md` §13.3 beschrieben.

## Ergebnis vor dem Update (51 Elemente, 141 Codings)

| Status | Anzahl |
| --- | --- |
| INACTIVE | 2 |
| NOT-FOUND | 38 |
| OK | 94 |
| UNVERIFIABLE (ICF, MedDRA) | 7 |

Nicht auffindbare Codes waren teils veraltete/fehlerhafte Codes, teils **semantisch falsche** Treffer (gefundener Code mit anderer Bedeutung), z. B. 385763009 = „Hospice care“ (gemeint: psychoonkologische Beratung), 410429000 = „Cardiac arrest“ (gemeint: nozizeptiver Schmerz), 89283-6 = „CT Neck+Chest+Abdomen+Pelvis“ (gemeint: Atemnot-NRS), 233604007 = „Pneumonia“ (gemeint: Pneumonitis), 85756007 = „Body tissue structure“ (gemeint: Fernmetastase), 736378000 = „Medication management plan“ (gemeint: Survivorship Care Plan), 419099009 = „Dead“ (gemeint: Sterbephase), 190787008 = „Abetalipoproteinemia“ (gemeint: Autoimmunhepatitis), 182840001 = „Drug treatment stopped“ (gemeint: Complete Response), 89200-0 = Labor-Resistenztestung (gemeint: IPOS), 89204-2 = PHQ-9 für Jugendliche (gemeint: PRO-Score), 73831-0 = Depressionsscreening Jugendliche (gemeint: EORTC QLQ-C30), 8341-0 = Trockengewicht (gemeint: Gewichtsverlust).

## Ergebnis nach dem Update (112 Elemente, 408 Codings)

| Status | Anzahl |
| --- | --- |
| LOCAL | 32 |
| OK | 369 |
| UNVERIFIABLE | 7 |

`UNVERIFIABLE` = Codesystem nicht auf dem Server (ICF, MedDRA); `LOCAL` = projekt-lokale Platzhalter (`local-no-standard-binding`). Kein Coding mehr mit Status NOT-FOUND oder INACTIVE.

## Code-Änderungen an Bestandselementen

| Element | Aktion | System | alt | neu | Begründung |
| --- | --- | --- | --- | --- | --- |
| `brainMriFinding` | replace | snomed-ct | 94225009 | 94225005 | 94225009 nicht auf SNOMED CT 20260701; korrekt: Metastatic malignant neoplasm to brain |
| `brainMriHighRisk` | add | ops | — | 3-800 | native MRT Schädel ergänzt (3-820 = mit Kontrastmittel) |
| `ctThoraxFinding` | replace | snomed-ct | 417798001 | 1259237005 | 417798001 nicht auf SNOMED CT 20260701; korrekt: Recurrent malignant neoplasm |
| `ctThoraxFinding` | add | snomed-ct | — | 878806005 | Zweitkarzinom als eigenes Konzept (Second primary cancer) |
| `ctThoraxScan` | replace | loinc | 30688-4 | 24627-2 | 30688-4 nicht in LOINC 2.83; korrekt: CT Chest |
| `ctThoraxScan` | add | ops | — | 3-222 | CT Thorax mit Kontrastmittel ergänzt (3-202 = nativ) |
| `distressThermometerScore` | remove | loinc | 63994-4 | — | 63994-4 nicht in LOINC 2.83; kein LOINC-/SNOMED-CT-Konzept für das NCCN Distress-Thermometer auf dem MII TermServ gefunden |
| `dlcoPercentPredicted` | replace | loinc | 17129-7 | 98130-8 | 17129-7 nicht in LOINC 2.83; korrekt: Diffusion capacity.carbon monoxide/Predicted |
| `dlcoPercentPredicted` | replace | snomed-ct | 252464004 | 36421003 | 252464004 nicht auf SNOMED CT 20260701; korrekt: Carbon monoxide diffusing capacity measurement |
| `fev1PercentPredicted` | replace | loinc | 75889-0 | 20152-5 | 75889-0 nicht in LOINC 2.83; korrekt: FEV1 measured/predicted |
| `followUpInterval` | replace | local-no-standard-binding | Q6-9M | Q6-9W | Code sagte Monate, Display Wochen — Einheit korrigiert (konsistent zu restagingImagingDate) |
| `followUpInterval` | add | local-no-standard-binding | — | Q3M-Y1;Q6M-Y2;Q12M-Y3-Y5 · M3;M6;… · Q6-8W-curative-recurrence | Onkopedia-SCLC-/NSCLC-Raster und verkürztes Intervall als Codes ergänzt |
| `postTherapyComplication` | replace | snomed-ct | 233604007 | 84004001 | 233604007 = Pneumonia (falsches Konzept); korrekt: Radiation pneumonitis |
| `postTherapyComplication` | add | snomed-ct | — | 205237003 | Pneumonitis (unspezifisch) ergänzt |
| `postTherapyComplication` | replace | snomed-ct | 16348002 | 235605005 | 16348002 nicht auf SNOMED CT 20260701; korrekt: Radiation esophagitis |
| `postTherapyComplication` | add | snomed-ct | — | 51615001 | Strahlenfibrose (Fibrosis of lung) ergänzt — Onkopedia NSCLC Kap. 6.2.2.1 |
| `postTherapyComplication` | add | snomed-ct | — | 709073001 | neurokognitive Störung nach Ganzhirnbestrahlung/PCI ergänzt — Onkopedia NSCLC 6.1.6.1, SCLC 6.1.1.3 |
| `psychoOncologyReferral` | replace | snomed-ct | 385763009 | 428997004 | 385763009 = Hospice care (falsches Konzept); korrekt: Psychosocial counseling about cancer |
| `pulmonaryFunctionTest` | replace | loinc | 20143-5 | 19911-7 | 20143-5 nicht in LOINC 2.83; korrekt: Diffusion capacity.carbon monoxide |
| `pulmonaryFunctionTest` | replace | ops | 1-712 | 1-710 | 1-712 = Spiroergometrie (falsches Konzept); korrekt: Ganzkörperplethysmographie |
| `recurrenceOrSecondPrimary` | replace | snomed-ct | 417798001 | 1259237005 | 417798001 nicht auf SNOMED CT 20260701; korrekt: Recurrent malignant neoplasm |
| `recurrenceOrSecondPrimary` | replace | snomed-ct | 20003000 | 314954002 | 20003000 nicht auf SNOMED CT 20260701; korrekt: Local recurrence of malignant neoplasm of lung |
| `recurrenceOrSecondPrimary` | replace | snomed-ct | 85756007 | 399409002 | 85756007 = Body tissue structure (falsches Konzept); korrekt: Distant metastasis present |
| `recurrenceOrSecondPrimary` | replace | snomed-ct | 128462008 | 878806005 | 128462008 = Metastatic malignant neoplasm (Display 'Second primary' falsch); korrekt: Second primary cancer |
| `recurrenceOrSecondPrimary` | replace | kdl | AD060106 | SD150103 | KDL AD060106 ist deprecated; aktiver Nachfolger SD150103 |
| `smokingStatus` | replace | snomed-ct | 722498003 | 722499006 | 722498003 = Electronic cigarette (Produkt); korrekt für den Status: Electronic cigarette user |
| `survivorshipCarePlan` | remove | snomed-ct | 736378000 | — | 736378000 = Medication management plan (falsches Konzept) |
| `survivorshipCarePlan` | add | loinc | — | 74156-1 | Oncology Plan of Care and Summary Note (Abschlussbericht/Survivorship-Plan) ergänzt |
| `tobaccoCessationCounselling` | replace | snomed-ct | 171055004 | 225323000 | 171055004 nicht auf SNOMED CT 20260701; korrekt: Smoking cessation education |
| `tobaccoCessationCounselling` | replace | snomed-ct | 386516008 | 702388001 | 386516008 nicht auf SNOMED CT 20260701; korrekt: Tobacco use cessation education |
| `tobaccoCessationCounselling` | replace | icd-10-gm | Z71.6 | Z72.0 | Z71.6 existiert in ICD-10-GM 2026 nicht; korrekt: Z72.0 Probleme mit Bezug auf Tabakkonsum |
| `advanceCarePlanning` | replace | snomed-ct | 713600000 | 713603004 | 713600000 nicht auf SNOMED CT 20260701; korrekt: Advance care planning |
| `advanceDirectiveDocument` | replace | snomed-ct | 470611000124106 | 425393008 | 470611000124106 (US-Extension) nicht auf dem Server; Vorsorgevollmacht: Active Durable Power of Attorney for Healthcare |
| `advanceDirectiveDocument` | add | loinc | — | 42348-3 | Advance Healthcare Directives (Dokumentklasse) ergänzt |
| `anxietyHadsScore` | remove | loinc | 62106-6 | — | 62106-6 nicht in LOINC 2.83 |
| `anxietyHadsScore` | add | snomed-ct | — | 401319005 | HAD scale: anxiety score (HADS-A) |
| `anxietyHadsScore` | add | snomed-ct | — | 273524006 | Hospital anxiety and depression scale (Instrument) |
| `caregiverBurden` | remove | loinc | 62133-0 | — | 62133-0 nicht in LOINC 2.83; kein LOINC-/SNOMED-Konzept für das Zarit Burden Interview auf dem MII TermServ |
| `caregiverBurdenScore` | remove | loinc | 62133-0 | — | 62133-0 nicht in LOINC 2.83 |
| `dyingPhaseDiagnosed` | replace | snomed-ct | 419099009 | 399069006 | 419099009 = Dead (falsches Konzept); korrekt: Dying process |
| `dyspneaIntensityNrs` | remove | loinc | 89283-6 | — | 89283-6 = CT Neck+Chest+Abdomen+Pelvis W contrast IV (falsches Konzept); kein LOINC-Code für Atemnot-NRS 0–10 gefunden (PROMIS 92149-4 ist ein T-Score) |
| `functionalStatus` | replace | snomed-ct | 373802001 | 761869008 | 373802001 = WHO performance status finding (nicht Karnofsky); korrekt: KPS score |
| `functionalStatus` | remove | loinc | 70924-1 | — | 70924-1 nicht in LOINC 2.83; kein Code für AKPS gefunden |
| `functionalStatus` | replace | snomed-ct | 65488-5 | 273302005 | 65488-5 nicht in LOINC 2.83; Barthel-Index als SNOMED CT 273302005 |
| `functionalStatus` | add | snomed-ct | — | 423740007 | ECOG performance status (SNOMED) ergänzt |
| `functionalStatus` | add | loinc | — | 89243-0 | Karnofsky Performance Status score (LOINC) ergänzt |
| `opioidDailyOmme` | remove | snomed-ct | 412130007 | — | 412130007 nicht auf SNOMED CT 20260701; kein Konzept für 'oral morphine equivalent' gefunden |
| `painType` | replace | snomed-ct | 410429000 | 735644008 | 410429000 = Cardiac arrest (falsches Konzept); korrekt: Chronic nociceptive pain |
| `painType` | remove | snomed-ct | 278860009 | — | 278860009 = Chronic low back pain (falsches Konzept); für Mischschmerz kein SNOMED-CT-Konzept gefunden |
| `spiritualNeedsAssessment` | replace | snomed-ct | 248058001 | 424823000 | 248058001 nicht auf SNOMED CT 20260701; korrekt: Expresses spiritual concerns |
| `symptomAssessmentInstrument` | remove | loinc | 89200-0 | — | 89200-0 = Phenotypic lab test method … (falsches Konzept) |
| `symptomAssessmentInstrument` | remove | loinc | 63994-4 | — | 63994-4 nicht in LOINC 2.83 |
| `symptomAssessmentInstrument` | add | snomed-ct | — | 718975008 | IPOS Patient Version (1 week recall) als SNOMED CT |
| `wishToDie` | replace | snomed-ct | 224943005 | 225876004 | 224943005 nicht auf SNOMED CT 20260701; korrekt: Wanting to die |
| `brainMriUnderTherapy` | add | snomed-ct | — | 241601008 | MRI of head (SNOMED) ergänzt |
| `brainMriUnderTherapy` | add | ops | — | 3-800 | native MRT Schädel ergänzt |
| `brainMriUnderTherapy` | add | ops | — | 3-820 | MRT Schädel mit Kontrastmittel ergänzt |
| `immuneRelatedAdverseEvent` | replace | snomed-ct | 1217138004 | 62014003 | 1217138004 nicht auf SNOMED CT 20260701; generisch: Adverse reaction to drug |
| `immuneRelatedAdverseEvent` | replace | snomed-ct | 233604007 | 205237003 | 233604007 = Pneumonia (falsches Konzept); korrekt: Pneumonitis |
| `immuneRelatedAdverseEvent` | replace | snomed-ct | 190787008 | 408335007 | 190787008 = Abetalipoproteinemia (falsches Konzept); korrekt: Autoimmune hepatitis |
| `immuneRelatedAdverseEvent` | add | snomed-ct | — | 1345085000 | Immune checkpoint inhibitor therapy induced enterocolitis (Beispiel irAE) ergänzt |
| `molecularResistanceFinding` | replace | loinc | 21678-9 | 21665-5 | 21678-9 nicht in LOINC 2.83; korrekt: EGFR gene mutations found [Identifier] … |
| `molecularResistanceFinding` | replace | loinc | 81238-6 | 21702-6 | 81238-6 nicht in LOINC 2.83; korrekt: KRAS gene mutations found [Identifier] … |
| `molecularResistanceFinding` | replace | snomed-ct | 55342001 | 108369006 | 55342001 = Neoplastic disease (Display 'morphologic abnormality' falsch); korrekt: Neoplasm (morphologic abnormality) |
| `molecularRetestingCtdna` | replace | loinc | 84141-0 | 107453-3 | 84141-0 nicht in LOINC 2.83; korrekt: Circulating tumor DNA [Interpretation] Narrative |
| `molecularRetestingCtdna` | replace | snomed-ct | 765168009 | 1285455002 | 765168009 nicht auf SNOMED CT 20260701; Liquid Biopsy: Detection of neoplasm in blood |
| `patientReportedSymptomWeb` | replace | snomed-ct | 364712001 | 162465004 | 364712001 nicht auf SNOMED CT 20260701; korrekt: Symptom severity |
| `patientReportedSymptomWeb` | replace | loinc | 89204-2 | 89194-5 | 89204-2 = PHQ-9 Teens (falsches Konzept); korrekt: Patient reported outcome measure score |
| `patientReportedSymptomWeb` | add | snomed-ct | — | 840297006 | Assessment of patient reported outcome measures ergänzt |
| `qolEortcQlqC30` | remove | loinc | 73831-0 | — | 73831-0 = Adolescent depression screening assessment (falsches Konzept); EORTC QLQ-C30 nicht in LOINC 2.83 |
| `qolEortcQlqC30` | add | snomed-ct | — | 273446001 | EORTC Quality of Life questionnaire (SNOMED) |
| `qolEortcQlqC30` | add | snomed-ct | — | 709503007 | Assessment of quality of life (SNOMED) |
| `recistResponse` | replace | snomed-ct | 182840001 / 268910001 / 359746009 / 271879005 | 260415000 / 268910001 / 359746009 / 271299001 / 709137006 | 182840001 = Drug treatment stopped (falsch), 271879005 nicht existent; ValueSet auf mCODE ConditionStatusTrend umgestellt (CR→Not detected, PR→improved, SD→stable, PD→worsened, NE→undetermined) |
| `recistResponse` | replace | kdl | AD060106 | SD150103 | KDL AD060106 deprecated → SD150103 |
| `restagingImagingDate` | replace | ops | 3-225 ('Native CT, Thorax/Abdomen/Becken') | 3-222 / 3-225 / 3-226 | 3-225 ist 'CT Abdomen mit Kontrastmittel'; Körperregionen Thorax/Abdomen/Becken als eigene OPS- und SNOMED-Codes |
| `restagingImagingDate` | add | snomed-ct | — | 169070004 / 169071000 | CT of abdomen / CT of pelvis ergänzt |
| `systemicTherapyRegimen` | replace | atc | L01XC18 | L01FF02 | ATC-Restrukturierung 2024 (L01XC → L01FF PD-1/PD-L1-Inhibitoren; L01XE → L01E Proteinkinase-Inhibitoren); Altcode nicht in ATC 2026 |
| `systemicTherapyRegimen` | replace | atc | L01XC32 | L01FF05 | ATC-Restrukturierung 2024 (L01XC → L01FF PD-1/PD-L1-Inhibitoren; L01XE → L01E Proteinkinase-Inhibitoren); Altcode nicht in ATC 2026 |
| `systemicTherapyRegimen` | replace | atc | L01XC44 | L01FF03 | ATC-Restrukturierung 2024 (L01XC → L01FF PD-1/PD-L1-Inhibitoren; L01XE → L01E Proteinkinase-Inhibitoren); Altcode nicht in ATC 2026 |
| `systemicTherapyRegimen` | replace | atc | L01XE13 | L01EB03 | ATC-Restrukturierung 2024 (L01XC → L01FF PD-1/PD-L1-Inhibitoren; L01XE → L01E Proteinkinase-Inhibitoren); Altcode nicht in ATC 2026 |
| `systemicTherapyRegimen` | replace | atc | L01XE35 | L01EB04 | ATC-Restrukturierung 2024 (L01XC → L01FF PD-1/PD-L1-Inhibitoren; L01XE → L01E Proteinkinase-Inhibitoren); Altcode nicht in ATC 2026 |
| `systemicTherapyRegimen` | replace | atc | L01XE36 | L01ED03 | ATC-Restrukturierung 2024 (L01XC → L01FF PD-1/PD-L1-Inhibitoren; L01XE → L01E Proteinkinase-Inhibitoren); Altcode nicht in ATC 2026 |
| `weightChangePercent` | remove | loinc | 8341-0 | — | 8341-0 = Dry body weight Measured (falsches Konzept) |
| `weightChangePercent` | add | snomed-ct | — | 248349002 | Percentage weight loss (SNOMED) ergänzt |
| `weightChangePercent` | add | loinc | — | 107109-1 | Weight loss 3 months (LOINC) ergänzt |

## Anzeigetext-Synchronisation (Display = TermServ-Anzeigetext)

| Element | System | Code | Display alt | Display neu (TermServ) |
| --- | --- | --- | --- | --- |
| `brainMriFinding` | snomed-ct | 359746009 | Stable disease (finding) | Patient's condition stable |
| `brainMriFinding` | snomed-ct | 260413007 | None (qualifier value) | None |
| `brainMriFinding` | snomed-ct | 419984006 | Inconclusive (qualifier value) | Inconclusive |
| `brainMriHighRisk` | snomed-ct | 241601008 | MRI of brain (procedure) | MRI of head |
| `brainMriHighRisk` | ops | 3-820 | MRT Schädel | Magnetresonanztomographie des Schädels mit Kontrastmittel |
| `ctThoraxFinding` | snomed-ct | 359746009 | Stable disease (finding) | Patient's condition stable |
| `ctThoraxFinding` | snomed-ct | 128462008 | Secondary malignant neoplastic disease | Metastatic malignant neoplasm |
| `ctThoraxFinding` | snomed-ct | 419984006 | Inconclusive (qualifier value) | Inconclusive |
| `ctThoraxScan` | snomed-ct | 169069000 | CT of thorax (procedure) | CT of chest |
| `ctThoraxScan` | ops | 3-202 | Native CT, Thorax | Native Computertomographie des Thorax |
| `ecogPerformanceStatus` | loinc | 89262-0 | ECOG Performance Status | ECOG Performance Status [Interpretation] |
| `ecogPerformanceStatus` | snomed-ct | 423740007 | Eastern Cooperative Oncology Group performance status finding | ECOG performance status |
| `fev1PercentPredicted` | snomed-ct | 59328004 | Forced expired volume in 1 second (observable entity) | Forced expired volume in 1 second |
| `postTherapyComplication` | icd-10-gm | T66 | Strahlenschäden, nicht näher bezeichnet | Nicht näher bezeichnete Schäden durch Strahlung |
| `postTherapyComplication` | icd-10-gm | J70.1 | Chronische pulmonale Manifestation Strahlentherapie | Chronische und sonstige Lungenbeteiligung bei Strahleneinwirkung |
| `pulmonaryFunctionTest` | snomed-ct | 23426006 | Pulmonary function test (procedure) | Measurement of respiratory function |
| `recurrenceOrSecondPrimary` | icd-10-gm | C34.9 | Bösartige Neubildung der Bronchien und der Lunge, n.n.b. | Bösartige Neubildung: Bronchus oder Lunge, nicht näher bezeichnet |
| `recurrenceOrSecondPrimary` | icd-o-3 | 8140/3 | Adenokarzinom (M-Code) | Adenokarzinom o.n.A. |
| `recurrenceOrSecondPrimary` | icd-o-3 | 8070/3 | Plattenepithelkarzinom (M-Code) | Plattenepithelkarzinom o.n.A. |
| `recurrenceOrSecondPrimary` | icd-o-3 | 8041/3 | Kleinzelliges Karzinom (M-Code) | Kleinzelliges Karzinom o.n.A. |
| `recurrenceOrSecondPrimary` | icd-o-3 | 8012/3 | Großzelliges Karzinom (M-Code) | Großzelliges Karzinom o.n.A. |
| `recurrenceOrSecondPrimary` | icd-o-3 | C34.9 | Lunge, n.n.b. (T-Code, Topographie) | Lunge o.n.A. |
| `smokingStatus` | snomed-ct | 43381005 | Passive smoker (finding) | Passive smoker |
| `tobaccoCessationCounselling` | atc | N07BA01 | Nikotinersatz | Nicotin |
| `advanceDirectiveDocument` | snomed-ct | 371538006 | Advance directive | Advance directive report |
| `dyspneaIntensityNrs` | snomed-ct | 267036007 | Dyspnea (finding) | Dyspnea |
| `functionalStatus` | loinc | 89262-0 | ECOG Performance Status | ECOG Performance Status [Interpretation] |
| `opioidDailyOmme` | atc | N02A | Opioide | OPIOIDE |
| `painIntensityNrs` | loinc | 72514-3 | Pain severity NRS | Pain severity - 0-10 verbal numeric rating [Score] - Reported |
| `phq9DepressionScore` | loinc | 44261-6 | PHQ-9 total score | Patient Health Questionnaire 9 item (PHQ-9) total score [Reported] |
| `adverseEventCtcaeGrade` | snomed-ct | 255604002 | Mild (severity modifier) | Mild |
| `adverseEventCtcaeGrade` | snomed-ct | 6736007 | Moderate (severity modifier) | Moderate severity |
| `adverseEventCtcaeGrade` | snomed-ct | 24484000 | Severe (severity modifier) | Severe |
| `ecogPerformanceStatusSurveillance` | loinc | 89262-0 | ECOG Performance Status | ECOG Performance Status [Interpretation] |
