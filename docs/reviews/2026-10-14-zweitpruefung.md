# Zweitprüfung der Datenelemente gegen die Primärquellen (2026-10-14)

> **Zielgruppe:** klinische Reviewer:innen (Nachsorge-WG, Allgemeinmedizin, Palliativmedizin) und MI-Team.
> **Status:** Momentaufnahme der Prüfung vom 14./15.10.2026 (Branch `feat/guideline-resync-terminology-primarycare`, PR #15).
> Alle Elemente bleiben `AuthorDraft`; die Prüfung ersetzt kein klinisches Review. Offenlegung des KI-Einsatzes: [`AI_USAGE.md`](../../AI_USAGE.md).

## 1 Auftrag und Vorgehen

**Auftrag (Maintainer, 2026-10-14):** Die Datenelemente der Nachsorge-Phasen (Nachsorge nach kurativer Therapie, Surveillance, Palliativversorgung, hausärztliche Langzeitbegleitung von Langzeitüberlebenden) erneut anhand der Primärquellen verifizieren, auf semantische Korrektheit achten und Fehler korrigieren.

**Primärquellen (lokal beschafft, Volltext; Stand 2026-10-14):**

| Quelle | geprüfte Fassung | Befund zum Pin |
| --- | --- | --- |
| S3-LL Lungenkarzinom | Langversion 5.1 (Juli 2026, AWMF 020-007OL); PDF identisch mit der Leitlinienprogramm-Fassung | aktuell |
| S3-LL Palliativmedizin | Langversion **3.0** (Juli 2026, AWMF 128-001OL; gültig bis 20.07.2031) + Leitlinienreport 3.0 | Pin „3.01 (Konsultationsfassung 03/2026)“ **veraltet** → 3.0 |
| Onkopedia NSCLC / SCLC | Stand April 2025 / Stand August 2026 (Online-Fassung, „aktuell gültige Version“) | aktuell |
| OCP Lung (AU) | 2nd ed. (Juni 2021), Minor Update Juli 2025 (nur Screening-Programm) | aktuell |
| Klein A-A et al. 2026 | Die Onkologie 32(1):91–99, online 02.12.2025, Verlags-PDF + Zusatzmaterial Anhang 2 | aktuell; Titel im Repo gekürzt |
| AG LONKO (Nationaler Krebsplan) | Empfehlungspapiere UAG Daten (17.06.2021), UAG Versorgungsmodelle (18.06.2021), Glossar (10.11.2021) | „2021/2022“ teilweise unbelegt; mit Klein 2026 vermengt |
| S3-LL Rauchen und Tabakabhängigkeit | Version 3.1 (Stand 01/2021, Langversion 03/2021, AWMF 076-006; gültig bis 31.12.2025, Aktualisierung angemeldet 12/2024) | Pin „1.0“ **falsch** → 3.1 |

**Ablauf (Multi-Agenten-Workflow mit adversarialer Gegenprüfung):**

1. **Quellenbeschaffung** — je Quelle ein Agent: aktuelle Fassung ermitteln, Volltext lokal ablegen, Abschnitts-Index (Kapitel → Zeilen) erstellen, Pin bewerten.
2. **Verifizieren** — 22 Gruppen à 4–6 Elemente (alle 112 Elemente; 15 Elemente aus einem abgebrochenen ersten Lauf übernommen): je Element Quellentreue jeder Referenz (Wortlaut, Abschnitts-/Empfehlungsnummer, Grad, LoE), Semantik jedes Codings (offizielle Bedeutung, Hierarchie, Rolle im Element; Live-Lookup am MII TermServ) und Inhalt (Definition, Datentyp, Kardinalität, Trigger, Frequenz, Rolle, Kategorie) → normalisierte Änderungsvorschläge mit wörtlichem Beleg.
3. **Gegenprüfen** — je Gruppe zwei unabhängige Skeptiker mit unterschiedlicher Linse (*Quelle*: Lesart der Primärquelle; *Terminologie/Semantik/Modell*: Code-Existenz, Bedeutung, Datentyp, Konsistenz im Katalog). Standard: widerlegt, wenn nicht klar belegt. Ein Vorschlag überlebt **nur, wenn keine der beiden Linsen ihn widerlegt**.
4. **Zusammenführen** — überlebende Vorschläge mit Teilkorrektur („fix“) eines Skeptikers wurden je Gruppe von einem weiteren Agenten zu einer endgültigen Änderung zusammengeführt (übernehmen / korrigiert übernehmen / verwerfen).
5. **Mappings** — ein zentraler Agent prüfte alle `standard_mappings` gegen die publizierten Pakete (MII KDS inkl. Ballot 2027, ISiK 6.0.0, KBV MIO/eAU, gematik ePA, mCODE STU4, Genomics Reporting STU3, oBDS-XSD 3.0.5, Arztbrief Plus 3.12, OMOP CDM 5.4); daraus je Phase konkrete Ersetzungen mit eigener Gegenprüfung; jede neue FHIR-Canonical wurde zusätzlich maschinell gegen die `url` der StructureDefinitions in den Paketen geprüft.
6. **Anwenden** — jede Code-Änderung wurde beim Schreiben erneut live am MII TermServ (`CodeSystem/$lookup`) geprüft; der Anzeigetext kommt vom Server, nicht auffindbare oder inaktive Codes werden nie geschrieben.

## 2 Ergebnis in Zahlen

| Schritt | Ergebnis |
| --- | --- |
| Verifizierte Elemente | 112 (Gesamturteil der Verifizierer: 58 „major“, 52 „minor“, 2 „ok“) |
| Änderungsvorschläge | 687 |
| Von mindestens einer Linse widerlegt (verworfen) | 88 (34 von beiden Linsen, 33 nur Linse Quelle, 21 nur Linse Semantik) |
| Von beiden Linsen bestätigt | 599, davon 216 mit Teilkorrektur → zusammengeführt: 206 korrigiert übernommen, 7 unverändert, 3 verworfen (Dublette/überholt) |
| Angewendet | **597** Änderungen (inkl. 1 Folgeänderung); beim Schreiben vom TermServ abgelehnt: 0 |
| davon Referenzen | 129 ergänzt, 74 präzisiert (Abschnitt, Empfehlungsnummer, Grad, Evidenzlevel) |
| davon Felder | 140 (Definition, Trigger, Frequenz, Rolle, Einschränkungen, Hinweise, Value-Set-Notizen; 4 Modelländerungen) |
| davon Codings | 42 ersetzt, 48 ergänzt, 26 entfernt |
| davon offene Punkte | 80 neue `issues[]` für das klinische Review |
| davon Beziehungen | 46 ergänzt, 12 entfernt |
| Katalogweite Pin-Korrekturen | 50 Referenzen (Palliativ 3.0, Tabak 3.1, Klein-Zitat, OCP-Dokument-URL, AWMF-Grade bei nicht graduierenden Quellen) |
| Referenzen gesamt | 328 (vorher 199) |

## 3 Wesentliche Befunde

### 3.1 Quellen-Pins

- **S3-LL Palliativmedizin:** Die Konsultationsfassung 3.01 (03/2026) ist durch die finale Langversion **3.0 (Juli 2026)** abgelöst. Kapitel, Tab. 6 und Tab. 9 sind unverändert; zwei systematische Abweichungen: Die Empfehlungsnummern in Kap. 10 sind ab 10.2 um +1 verschoben (die Selbsteinschätzung der Schmerzintensität ist als neue Empf. 10.1 aufgenommen), und Konsensempfehlungen tragen in 3.0 durchgängig „EK“. Alle 48 Palliativ-Referenzen tragen jetzt Nummer, Grad und Evidenzlevel nach 3.0 (z. B. Empf. 6.11 A/LoE 2 und 6.14 A/LoE 1 bei `advanceCarePlanning`; Empf. 21.1 Grad 0/LoE 4 und 21.2 B/LoE 4 bei `dyingPhaseDiagnosed`; Empf. 9.1 EK bei `dyspneaIntensityNrs`; Empf. 10.1/10.2 EK bei `painIntensityNrs`).
- **S3-LL Rauchen und Tabakabhängigkeit:** Das Dokument nennt die Versions-Nr. **3.1** (Stand 01/2021, Langversion 03/2021), nicht „1.0“; die Gültigkeit ist am 31.12.2025 abgelaufen, eine Aktualisierung ist seit 12/2024 angemeldet.
- **AG LONKO und Klein 2026** waren in `survivorshipCarePlan` vermengt („2021/2022; Klein 2026“, Klein-DOI an der AG-LONKO-Referenz). Getrennt: AG LONKO = Empfehlungspapiere der UAG Daten (17.06.2021) und UAG Versorgungsmodelle (18.06.2021); Klein A-A et al. 2026 als eigene Referenz mit der Dos/Don'ts-Gliederung der Empfehlungsliste (Anhang 2). Der Klein-Titel ist in README und Methodik vervollständigt („… von Langzeitüberlebenden einer Krebserkrankung“).
- **Nicht graduierende Quellen:** Onkopedia, OCP und AG LONKO vergeben keine Empfehlungsgrade; AWMF-Kategorien („Statement“, LoE) sind dort entfernt (`n/a`).
- Neu als ergänzende Quellen: S3-LL Psychoonkologie 2.1 (Distress-Thermometer, Empf. 7.4 A/LoE 1b), Onkopedia „Impfungen bei malignen Erkrankungen und Immunsuppression“ (Stand Mai 2026), EORTC QLQ-C30 Scoring Manual (3rd ed.).

### 3.2 Semantik der Codings (Auswahl)

| Element | Befund | Korrektur |
| --- | --- | --- |
| `dyingPhaseDiagnosed` | ICD-10-GM Z51.5 „Palliativbehandlung“ ist ein Behandlungsanlass, kein Marker der Sterbephase | entfernt |
| `fev1PercentPredicted` | LOINC 20150-9 ist das absolute FEV1 (Liter), Einheit des Elements ist % | entfernt; SNOMED 313223002 „Percent predicted FEV1“ |
| `recurrenceOrSecondPrimary` | ICD-O-3-Morphologie- und Topographie-Codes als Rezidiv-Codes | entfernt |
| `tobaccoCessationCounselling` | ATC-Wirkstoffcodes und Z72.0 in einem Prozedur-Element | entfernt (Pharmakotherapie als Hinweis) |
| `anxietyHadsScore` | SNOMED 273524006 bezeichnet das Gesamtinstrument (beide Subskalen) neben dem HADS-A-Score | entfernt; Hinweis in den Value-Set-Notizen |
| `tnmStage` | SNOMED 405979002 liegt nicht im Staging-Typ der MII/mCODE-Profile | 399588009 „Pathologic TNM stage grouping“ |
| `tumorHistology` | Code-Paar für Histologie | LOINC 59847-4 „Histology and Behavior ICD-O-3 Cancer“; SNOMED 911750741000004104 (Kernmodul) |
| `adverseEventCtcae` | MedDRA-Codes außerhalb der CTCAE-Terminologie der MII | ersetzt nach MII-ValueSet `mii-vs-onko-nebenwirkung-art` (CTCAE v4.03; MedDRA nicht auf dem TermServ) |
| `administrativeGender` | LOINC 46098-0 „Sex“ statt administrativem Geschlecht | 107454-1 „Administrative gender“ |

### 3.3 Modelländerungen (von beiden Linsen bestätigt)

- `curativeTreatmentModality`: Kardinalität 1..1 → **1..\*** (multimodale Therapie = mehrere Komponenten; kein SNOMED-Kompositkonzept).
- `adverseEventCtcaeGrade`: Datentyp integer → **CodeableConcept** (oBDS/MII-Grade 1–5 plus U/K; MII `AdverseEvent.seriousness` required).
- `qolEortcQlqC30`: Datentyp integer → **decimal** (Globalskala in Schritten von 8,33).
- `responsiblePrimaryCarePhysician`: Kardinalität 1..1 → **0..1** (Patient:innen ohne Hausärzt:in; im klinischen Review rückzubestätigen).

### 3.4 Intervalle und Auslöser (Auswahl)

- `brainMriUnderTherapy`: SCLC ED unter Beobachtung statt PCI nach S3 Empf. 9.26 (Grad A) 3-monatlich im 1. Jahr, danach 6-monatlich (vorher unbefristet 3-monatlich); Intervalle für EGFR+, ROS1+/NTRK+/RET+/MET-Exon-14+ ergänzt.
- `restagingImagingDate`: „per-cycle“ für SCLC war falsch (Onkopedia SCLC: Ansprechensbeurteilung nach frühestens 2, i. d. R. 3–4 Zyklen); erste NSCLC-Kontrolle nach 2, spätestens 3 Zyklen (S3 Empf. 8.84/8.100).
- `dyingPhaseDiagnosed`: Re-Evaluation der Feststellung spätestens nach 72 h im multiprofessionellen Team (S3-LL Palliativmedizin 3.0, Kap. 21.2); „täglich“ betrifft die Überprüfung des Betreuungsplans (Tab. 6, Zeile d).

### 3.5 Standard-Mappings

Ein zentraler Agent prüfte alle 115 `standard_mappings`-Einträge (26 distinkte Ziele) gegen die publizierten Artefakte. **7 Ziele existierten nicht** — MII Onkologie und Bildgebung unter `…/fhir/core/…` statt `…/fhir/ext/modul-onko/…` bzw. `…/fhir/ext/modul-bildgebung/…`, ein Bildgebungs-Profil „imagingstudy“ (richtig: `mii-pr-bildgebung-bildgebungsstudie`), das MII-Profil „Raucher“ und die oBDS-Seite `/feldbeschreibung`. Weitere Einträge verwiesen auf HTML-Seiten oder IG-Startseiten statt auf kanonische Profil-URLs oder auf semantisch unpassende Profile (Labor-Einzelwert statt Laborbefund, einzelnes MedicationStatement statt Medikationsliste, ImagingStudy für Befunddokumente, Integer-Pfade in kodierten Profilen).

Je Phase formulierte ein Agent konkrete Operationen; eine Skeptiker:in prüfte jede gegen die lokal entpackten Pakete (151 Operationen, 2 widerlegt), Teilkorrekturen wurden gegen den aktuellen Stand der Elemente zusammengeführt (4 als Dublette/überholt verworfen). Jede geschriebene FHIR-Canonical existiert als `url` einer StructureDefinition in den Paketen (maschinell geprüft).

| Ergebnis | Wert |
| --- | --- |
| Angewendete Operationen | **145** in 57 Elementen: 74 Ersetzungen, 38 Ergänzungen, 33 offene Punkte (Repräsentationsunterschiede) |
| Mapping-Einträge | 115 → 153; distinkte Ziele 26 → 57; MII-KDS-Einträge 42 → 72 |
| Wichtigste Ziele | MII Onkologie (`mii-pr-onko-*`: TNM, Histologie, Verlauf, Nebenwirkung, ECOG, Systemtherapie, Tumorkonferenz), MII Bildgebung (Bildgebungsstudie, radiologischer Befund), MII Laborbefund (DiagnosticReportLab), MII Dokument, MII PRO (2026.7.0), MII Medikationsliste, ISiKRaucherStatus (statt „Raucher“), oBDS-Feldliste und XSD 3.0.5, mCODE STU4- und Genomics-STU3-Canonicals |
| Nur-Ballot-Profile | MII Lungenfunktion, Soziodemographie, Kardiologie (2027-Ballot) — in `notes` gekennzeichnet, stabile Alternative beibehalten |
| Offene Punkte, die eine Mapping-Korrektur verlangten | 9 aufgelöst oder auf die verbleibende Frage reduziert |

Die Bedeutung der Elemente wurde dabei nicht geändert: Wo ein Profil eine andere Repräsentation verlangt (z. B. ECOG als CodeableConcept im MII-Profil, CTCAE-Grad als MII-Code, PROM als QuestionnaireResponse), steht die Transformation in `notes`, die Entscheidung als offener Punkt.

## 4 Änderungen je Element

„übernommen“ = angewendete Änderungen, „verworfen“ = von mindestens einer Linse widerlegte Vorschläge. Die vollständigen Begründungen mit Fundstellen stehen in den Feldern der YAMLs (`evidence`, `value_set.notes`, `issues`).

### Nachsorge (follow-up)

| Element | übernommen | verworfen | wesentliche Änderungen |
| --- | --- | --- | --- |
| `abdominalUltrasoundFollowUp` | 1 | 2 | Feld `definition_de` |
| `brainMetastasisRiskProfile` | 10 | 0 | Feld `definition_de`; Anzeigetext local-no-standard-binding high-risk-molecular; Anzeigetext local-no-standard-binding high-risk-histology; Feld `value_set.notes`; − Beziehung dependsOn brainMriHighRisk; + Beziehung dependsOn tumorHistology; + Beziehung dependsOn tnmStage; Ref. S3-LL Lungenkarzinom präzisiert (EK/n/a); Ref. Onkopedia NSCLC präzisiert (n/a/n/a) · 1 offene(r) Punkt(e) |
| `brainMriFinding` | 7 | 3 | Feld `definition_de`; + Code snomed-ct 268910001; + Code snomed-ct 271299001; Code snomed-ct 260413007 → 260415000; Ref. S3-LL Lungenkarzinom präzisiert (EK/n/a); Feld `instruction_de` · 1 offene(r) Punkt(e) |
| `brainMriHighRisk` | 3 | 3 | Feld `care_process.trigger`; Feld `definition_de`; Ref. S3-LL Lungenkarzinom präzisiert (EK/n/a) |
| `bronchoscopyFollowUp` | 3 | 2 | Feld `definition_de`; Ref. S3-LL Lungenkarzinom präzisiert (n/a/n/a); Ref. Onkopedia SCLC präzisiert (n/a/n/a) |
| `chestXRayFollowUp` | 1 | 3 | Feld `definition_de` |
| `ctAbdomenFollowUp` | 3 | 2 | Ref. S3-LL Lungenkarzinom präzisiert (EK/n/a); + Beziehung dependsOn followUpVisitDate; − Beziehung dependsOn recurrenceOrSecondPrimary |
| `ctThoraxFinding` | 6 | 5 | Code loinc 59776-5 → 97509-4; Code snomed-ct 419984006 → 709137006; Feld `definition_de`; Ref. S3-LL Lungenkarzinom präzisiert (EK/n/a) · 2 offene(r) Punkt(e) |
| `ctThoraxScan` | 2 | 4 | Feld `care_process.frequency_pattern`; Ref. Onkopedia NSCLC präzisiert (n/a/n/a) |
| `curativeRecurrencePotential` | 4 | 1 | + Ref. S3-LL Lungenkarzinom (n/a/2b); + Ref. OCP Lung (AU) (n/a/n/a); Feld `value_set.notes` · 1 offene(r) Punkt(e) |
| `curativeTreatmentModality` | 11 | 1 | Ref. S3-LL Lungenkarzinom präzisiert (EK/n/a); + Ref. S3-LL Lungenkarzinom (A/2); + Ref. Onkopedia SCLC (n/a/n/a); Feld `definition_de`; Feld `cardinality`; Feld `value_set.notes`; Code snomed-ct 173171007 → 119746007; + Code ops 5-323; + Code ops 5-327; + Code icd-10-gm Z92.6; − Beziehung dependsOn structuredFollowUpPlan |
| `distressThermometerScore` | 6 | 0 | Ref. S3-LL Palliativmedizin präzisiert (n/a/n/a); + Ref. andere (A/1b); Feld `constraints_de`; Feld `value_set.notes`; Feld `care_process.trigger`; Ref. OCP Lung (AU) präzisiert (n/a/n/a) |
| `dlcoPercentPredicted` | 2 | 6 | Feld `definition_de`; + Ref. Onkopedia NSCLC (n/a/n/a) |
| `ecogPerformanceStatus` | 5 | 4 | Ref. S3-LL Palliativmedizin präzisiert (n/a/n/a); Ref. Onkopedia NSCLC präzisiert (n/a/n/a); + Ref. S3-LL Lungenkarzinom (EK/n/a) · 2 offene(r) Punkt(e) |
| `fev1PercentPredicted` | 4 | 4 | − Code loinc 20150-9; Code snomed-ct 59328004 → 313223002; Feld `definition_de`; Ref. S3-LL Lungenkarzinom präzisiert (n/a/n/a) |
| `firstFollowUpVisitDate` | 3 | 1 | Feld `definition_de`; + Code snomed-ct 390906007; + Beziehung hasPart postTherapyComplication |
| `followUpHistoryFinding` | 5 | 0 | Code snomed-ct 816160009 → 262285001; + Code snomed-ct 84387000; Ref. Onkopedia NSCLC präzisiert (n/a/n/a) · 2 offene(r) Punkt(e) |
| `followUpInterval` | 5 | 0 | − Code local-no-standard-binding Q6-9W; Anzeigetext local-no-standard-binding Q12M-PostY5; + Ref. S3-LL Lungenkarzinom (Statement/1); + Beziehung isPartOf structuredFollowUpPlan · 1 offene(r) Punkt(e) |
| `followUpVisitDate` | 2 | 0 | Feld `definition_de` · 1 offene(r) Punkt(e) |
| `laboratoryTestFollowUp` | 5 | 0 | − Code loinc 11502-2; Feld `value_set.notes`; Feld `definition_de`; Feld `constraints_de`; Ref. S3-LL Lungenkarzinom präzisiert (n/a/n/a) |
| `petCtFollowUp` | 4 | 1 | Feld `care_process.trigger`; Feld `definition_de`; Ref. S3-LL Lungenkarzinom präzisiert (n/a/n/a); + Code snomed-ct 1373815000 |
| `physicalExaminationFinding` | 3 | 0 | + Code snomed-ct 282332003; + Beziehung isPartOf postInductionEvaluationDate · 1 offene(r) Punkt(e) |
| `postTherapyComplication` | 8 | 0 | Ref. S3-LL Lungenkarzinom präzisiert (B/2); Code snomed-ct 51615001 → 405570007; + Code icd-10-gm J70.0; Feld `definition_de`; + Ref. S3-LL Lungenkarzinom (EK/n/a); + Beziehung specializes treatmentSideEffectOrComplication; + Beziehung dependsOn curativeTreatmentModality · 1 offene(r) Punkt(e) |
| `prophylacticCranialIrradiationStatus` | 9 | 0 | Ref. S3-LL Lungenkarzinom präzisiert (n/a/n/a); + Ref. S3-LL Lungenkarzinom (A/1); + Ref. S3-LL Lungenkarzinom (A/2); + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. S3-LL Lungenkarzinom (0/3); Ref. Onkopedia SCLC präzisiert (n/a/n/a); Feld `care_process.trigger`; + Beziehung dependsOn recistResponse · 1 offene(r) Punkt(e) |
| `psychoOncologyReferral` | 7 | 0 | Feld `definition_de`; Feld `care_process.trigger`; + Code snomed-ct 309625004; Ref. OCP Lung (AU) präzisiert; + Ref. S3-LL Lungenkarzinom (n/a/n/a); + Beziehung dependsOn distressThermometerScore; + Beziehung dependsOn structuredFollowUpPlan |
| `pulmonaryFunctionTest` | 5 | 1 | Code loinc 19911-7 → 81458-2; + Code ops 1-711; Feld `definition_de`; Feld `constraints_de` · 1 offene(r) Punkt(e) |
| `recurrenceOrSecondPrimary` | 12 | 2 | − Code icd-o-3 8140/3; − Code icd-o-3 8070/3; − Code icd-o-3 8041/3; − Code icd-o-3 8012/3; − Code icd-o-3 C34.9; − Beziehung dependsOn curativeRecurrencePotential; + Beziehung dependsOn ctThoraxFinding; + Beziehung dependsOn brainMriFinding; + Beziehung dependsOn tumorHistology; Ref. S3-LL Lungenkarzinom präzisiert; Ref. Onkopedia SCLC präzisiert · 1 offene(r) Punkt(e) |
| `rehabilitationAndSocialCounselling` | 6 | 1 | Feld `definition_de`; + Code snomed-ct 308440001; Ref. S3-LL Lungenkarzinom präzisiert (EK/n/a); + Ref. S3-LL Lungenkarzinom (n/a/n/a); − Beziehung hasPart rehabilitationMeasure · 1 offene(r) Punkt(e) |
| `rehabilitationMeasure` | 8 | 2 | Ref. S3-LL Lungenkarzinom präzisiert (n/a/n/a); + Ref. Onkopedia SCLC (n/a/n/a); + Code snomed-ct 413743008; + Code snomed-ct 15081005; − Beziehung isPartOf rehabilitationAndSocialCounselling; + Beziehung dependsOn rehabilitationAndSocialCounselling · 2 offene(r) Punkt(e) |
| `screeningProgramEnrolment` | 3 | 0 | + Ref. S3-LL Lungenkarzinom (Statement/1); + Beziehung dependsOn smokingStatus · 1 offene(r) Punkt(e) |
| `smokingStatus` | 7 | 0 | Feld `definition_de`; + Code snomed-ct 266927001; Feld `value_set.notes`; Ref. S3-LL Tabakentwöhnung präzisiert (A/1a); + Ref. S3-LL Lungenkarzinom (A/1); Feld `care_process.trigger` · 1 offene(r) Punkt(e) |
| `structuredFollowUpPlan` | 5 | 0 | Feld `definition_de`; Feld `care_process.trigger`; Ref. S3-LL Lungenkarzinom präzisiert; + Beziehung dependsOn curativeTreatmentModality · 1 offene(r) Punkt(e) |
| `survivorshipCarePlan` | 6 | 0 | Ref. AG LONKO / Survivorship präzisiert; + Ref. andere (n/a/n/a); Ref. OCP Lung (AU) präzisiert; Feld `definition_de` · 2 offene(r) Punkt(e) |
| `tobaccoCessationCounselling` | 10 | 0 | − Code icd-10-gm Z72.0; − Code atc N07BA03; − Code atc N07BA01; + Code snomed-ct 151159008; + Code snomed-ct 719591006; + Code snomed-ct 771155005; + Code snomed-ct 395700008; Feld `instruction_de`; Ref. S3-LL Tabakentwöhnung präzisiert (A/1a); + Beziehung dependsOn smokingStatus |

### Surveillance

| Element | übernommen | verworfen | wesentliche Änderungen |
| --- | --- | --- | --- |
| `adverseEventCtcae` | 7 | 0 | Code meddra 10025598 → 10061229; Code meddra 10037087 → 10035742; Code meddra 10010726 → 10010300; Feld `value_set.notes`; + Ref. S3-LL Lungenkarzinom (EK/n/a); + Beziehung hasPart adverseEventCtcaeGrade · 1 offene(r) Punkt(e) |
| `adverseEventCtcaeGrade` | 9 | 1 | Feld `datatype`; + Code snomed-ct 399166001; Feld `value_set.notes`; Feld `constraints_de`; − Beziehung specializes adverseEventCtcae; − Beziehung specializes immuneRelatedAdverseEvent; + Beziehung isPartOf adverseEventCtcae; + Beziehung isPartOf immuneRelatedAdverseEvent · 1 offene(r) Punkt(e) |
| `brainMriUnderTherapy` | 8 | 0 | Ref. S3-LL Lungenkarzinom präzisiert (EK/n/a); + Ref. S3-LL Lungenkarzinom (A/2); + Ref. S3-LL Lungenkarzinom (EK/n/a); Feld `care_process.frequency_pattern`; Feld `care_process.trigger`; Feld `definition_de`; Feld `label_de` · 1 offene(r) Punkt(e) |
| `consultationModality` | 4 | 0 | − Code snomed-ct 448337001; + Ref. S3-LL Lungenkarzinom (n/a/n/a); Feld `constraints_de` · 1 offene(r) Punkt(e) |
| `earlyPalliativeReferral` | 9 | 0 | Ref. S3-LL Palliativmedizin präzisiert (EK/n/a); Ref. OCP Lung (AU) präzisiert; + Ref. S3-LL Lungenkarzinom (A/3); + Ref. S3-LL Lungenkarzinom (B/3); + Ref. S3-LL Palliativmedizin (EK/n/a); + Ref. S3-LL Palliativmedizin (A/3); Feld `definition_de`; Feld `care_process.responsible_role`; + Beziehung dependsOn complexityLevel |
| `ecogPerformanceStatusSurveillance` | 4 | 0 | + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. OCP Lung (AU) (n/a/n/a); + Code snomed-ct 423740007; Feld `constraints_de` |
| `immuneRelatedAdverseEvent` | 10 | 2 | Ref. S3-LL Lungenkarzinom präzisiert (n/a/n/a); + Ref. Onkopedia NSCLC (n/a/n/a); + Ref. Onkopedia SCLC (n/a/n/a); + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. S3-LL Lungenkarzinom (n/a/n/a); Code snomed-ct 408335007 → 235876009; Code snomed-ct 205237003 → 427046006; + Code snomed-ct 237539004; + Code snomed-ct 28926001; + Beziehung specializes adverseEventCtcae |
| `laboratoryPanelSurveillance` | 2 | 2 | Feld `definition_de` · 1 offene(r) Punkt(e) |
| `molecularResistanceFinding` | 9 | 2 | Ref. OCP Lung (AU) präzisiert (n/a/n/a); + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. Onkopedia NSCLC (n/a/n/a); − Code snomed-ct 108369006; Code loinc 21702-6 → 69548-6; Code snomed-ct 55446002 → 124975008; Feld `definition_de`; Feld `instruction_de` · 1 offene(r) Punkt(e) |
| `molecularRetestingCtdna` | 7 | 1 | Ref. OCP Lung (AU) präzisiert; + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. Onkopedia NSCLC (n/a/n/a); Code snomed-ct 1285455002 → 405825005; Feld `care_process.trigger`; Feld `instruction_de` · 1 offene(r) Punkt(e) |
| `patientReportedSymptomWeb` | 5 | 0 | Ref. Onkopedia NSCLC präzisiert (n/a/n/a); − Code snomed-ct 162465004; Feld `care_process.trigger`; + Ref. OCP Lung (AU) (n/a/n/a) · 1 offene(r) Punkt(e) |
| `postInductionEvaluationDate` | 3 | 0 | Feld `care_process.trigger`; + Beziehung hasPart physicalExaminationFinding; + Beziehung hasPart brainMriUnderTherapy |
| `qolEortcQlqC30` | 8 | 0 | Feld `datatype`; Feld `definition_de`; Ref. OCP Lung (AU) präzisiert (n/a/n/a); Ref. S3-LL Lungenkarzinom präzisiert (n/a/n/a); Ref. S3-LL Palliativmedizin präzisiert; + Ref. andere (n/a/n/a); Feld `value_set.notes` · 1 offene(r) Punkt(e) |
| `recistResponse` | 5 | 1 | + Ref. S3-LL Lungenkarzinom (EK/n/a); Feld `care_process.frequency_pattern`; Feld `care_process.trigger`; + Beziehung dependsOn restagingImagingDate · 1 offene(r) Punkt(e) |
| `restagingImagingDate` | 3 | 1 | + Ref. S3-LL Lungenkarzinom (EK/n/a); Feld `care_process.trigger`; Feld `care_process.frequency_pattern` |
| `structuredSurveillancePlan` | 2 | 1 | + Code snomed-ct 736252007; + Ref. S3-LL Lungenkarzinom (EK/n/a) |
| `surveillanceVisit` | 5 | 2 | Feld `care_process.frequency_pattern`; Feld `care_process.trigger`; + Beziehung dependsOn structuredSurveillancePlan; + Beziehung hasPart adverseEventCtcae · 1 offene(r) Punkt(e) |
| `systemicTherapyRegimen` | 6 | 0 | + Code atc L01CB01; + Code atc L01FX33; + Ref. S3-LL Lungenkarzinom (A/⊕⊕⊕⊕); + Ref. S3-LL Lungenkarzinom (B/⊕⊕⊕⊕); Feld `definition_de`; Feld `value_set.notes` |
| `therapyLineNumber` | 7 | 0 | Ref. S3-LL Lungenkarzinom präzisiert (n/a); + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. Onkopedia NSCLC (n/a/n/a); Feld `constraints_de`; Feld `value_set.standard_binding_status`; Feld `value_set.notes`; + Beziehung dependsOn systemicTherapyRegimen |
| `weightChangePercent` | 4 | 0 | − Code loinc 107109-1; Ref. OCP Lung (AU) präzisiert; + Ref. Onkopedia NSCLC (n/a/n/a) · 1 offene(r) Punkt(e) |

### Palliativversorgung

| Element | übernommen | verworfen | wesentliche Änderungen |
| --- | --- | --- | --- |
| `advanceCarePlanning` | 7 | 0 | Ref. S3-LL Palliativmedizin präzisiert (A/2); + Ref. S3-LL Palliativmedizin (EK/n/a); + Ref. S3-LL Palliativmedizin (A/1); + Ref. S3-LL Lungenkarzinom (A/2); + Beziehung hasPart advanceDirectiveDocument · 2 offene(r) Punkt(e) |
| `advanceDirectiveDocument` | 6 | 0 | Ref. S3-LL Palliativmedizin präzisiert (EK/n/a); + Ref. S3-LL Lungenkarzinom (A/4); + Code kdl AM160103; − Code snomed-ct 425393008; + Beziehung isPartOf advanceCarePlanning · 1 offene(r) Punkt(e) |
| `anxietyHadsScore` | 6 | 0 | Ref. S3-LL Palliativmedizin präzisiert (0/3); + Ref. S3-LL Palliativmedizin (EK/n/a); − Code snomed-ct 273524006; Feld `constraints_de`; Feld `value_set.notes` · 1 offene(r) Punkt(e) |
| `caregiverBurden` | 9 | 0 | Ref. S3-LL Palliativmedizin präzisiert (EK/n/a); + Ref. S3-LL Lungenkarzinom (B/3); Feld `definition_de`; + Code local-no-standard-binding ZBI; Feld `value_set.notes`; Feld `care_process.trigger`; Feld `care_process.frequency_pattern`; Feld `label_de` · 1 offene(r) Punkt(e) |
| `caregiverBurdenScore` | 6 | 2 | Ref. S3-LL Palliativmedizin präzisiert (EK/n/a); Feld `definition_de`; Feld `constraints_de`; Feld `care_process.trigger`; Feld `care_process.frequency_pattern` · 1 offene(r) Punkt(e) |
| `complexityLevel` | 8 | 0 | Ref. S3-LL Palliativmedizin präzisiert (EK/n/a); + Ref. S3-LL Palliativmedizin (A/3); Feld `care_process.trigger`; Feld `care_process.responsible_role`; Feld `definition_de`; + Beziehung dependsOn symptomAssessmentInstrument; + Beziehung dependsOn caregiverBurden · 1 offene(r) Punkt(e) |
| `dyingPhaseDiagnosed` | 9 | 0 | Ref. S3-LL Palliativmedizin präzisiert (0/4); + Ref. S3-LL Palliativmedizin (B/4); + Ref. S3-LL Palliativmedizin (n/a/n/a); − Code icd-10-gm Z51.5; Feld `definition_de`; Feld `care_process.frequency_pattern`; Feld `care_process.responsible_role`; + Beziehung specializes illnessPhase · 1 offene(r) Punkt(e) |
| `dyspneaIntensityNrs` | 6 | 0 | Ref. S3-LL Palliativmedizin präzisiert (EK/n/a); Ref. S3-LL Lungenkarzinom präzisiert (EK/n/a); Feld `definition_de`; Feld `constraints_de`; Feld `value_set.notes` · 1 offene(r) Punkt(e) |
| `functionalStatus` | 7 | 1 | Ref. S3-LL Palliativmedizin präzisiert (EK/n/a); Code snomed-ct 273302005 → 725594005; + Code loinc 96761-2; Feld `definition_de`; Feld `value_set.notes`; + Ref. S3-LL Lungenkarzinom (n/a/n/a) · 1 offene(r) Punkt(e) |
| `illnessPhase` | 4 | 0 | Ref. S3-LL Palliativmedizin präzisiert (EK/n/a); Feld `definition_de`; Feld `value_set.notes` · 1 offene(r) Punkt(e) |
| `opioidDailyOmme` | 5 | 0 | Ref. S3-LL Palliativmedizin präzisiert (B/1-); + Ref. S3-LL Palliativmedizin (B/1-); Feld `constraints_de`; Feld `care_process.trigger` · 1 offene(r) Punkt(e) |
| `painIntensityNrs` | 4 | 0 | Ref. S3-LL Palliativmedizin präzisiert (EK/n/a); Ref. S3-LL Lungenkarzinom präzisiert (n/a/n/a) · 1 offene(r) Punkt(e) |
| `painType` | 5 | 0 | Ref. S3-LL Palliativmedizin präzisiert (n/a/n/a); + Ref. S3-LL Palliativmedizin (A/1+); + Ref. S3-LL Lungenkarzinom (n/a/n/a); Feld `value_set.notes` · 1 offene(r) Punkt(e) |
| `palliativeCareTier` | 7 | 0 | Ref. S3-LL Palliativmedizin präzisiert (EK/n/a); + Ref. S3-LL Palliativmedizin (A/3); Feld `care_process.responsible_role`; Feld `instruction_de`; + Beziehung dependsOn complexityLevel · 2 offene(r) Punkt(e) |
| `phq9DepressionScore` | 5 | 0 | Ref. S3-LL Palliativmedizin präzisiert (A/4); + Ref. S3-LL Palliativmedizin (B/1+); Feld `definition_de`; Feld `constraints_de` · 1 offene(r) Punkt(e) |
| `qualityOfLifeScore` | 8 | 0 | Ref. S3-LL Lungenkarzinom präzisiert (EK/n/a); Ref. S3-LL Palliativmedizin präzisiert (n/a/n/a); + Ref. S3-LL Palliativmedizin (n/a/n/a); + Ref. OCP Lung (AU) (n/a/n/a); Feld `unit`; Feld `value_set.notes` · 2 offene(r) Punkt(e) |
| `spiritualNeedsAssessment` | 7 | 0 | Code snomed-ct 424823000 → 105408001; Feld `iso13972_metadata.type`; Ref. S3-LL Palliativmedizin präzisiert (B/3); + Ref. S3-LL Palliativmedizin (EK/n/a); + Ref. S3-LL Lungenkarzinom (B/3); Feld `definition_de`; Feld `constraints_de` |
| `symptomAssessmentInstrument` | 9 | 0 | Ref. S3-LL Palliativmedizin präzisiert (EK/n/a); + Ref. S3-LL Lungenkarzinom (EK/n/a); − Code local-no-standard-binding ESAS-r; + Code snomed-ct 451021004; + Code snomed-ct 718973001; Feld `value_set.notes`; Feld `care_process.trigger`; Feld `care_process.frequency_pattern`; Feld `care_process.responsible_role` |
| `treatmentDecisionDocumentation` | 7 | 0 | Ref. S3-LL Lungenkarzinom präzisiert (EK/n/a); Ref. S3-LL Palliativmedizin präzisiert (n/a/n/a); + Ref. S3-LL Palliativmedizin (EK/n/a); Code snomed-ct 247583006 → 734163000; Feld `definition_de`; Feld `care_process.frequency_pattern` |
| `wishToDie` | 7 | 0 | Ref. S3-LL Palliativmedizin präzisiert (A/3); + Ref. S3-LL Lungenkarzinom (EK/n/a); Feld `care_process.trigger`; Feld `care_process.frequency_pattern`; Feld `definition_de` · 2 offene(r) Punkt(e) |

### Hausärztliche Versorgung

| Element | übernommen | verworfen | wesentliche Änderungen |
| --- | --- | --- | --- |
| `acuteIntercurrentIllness` | 1 | 2 | 1 offene(r) Punkt(e) |
| `administrativeGender` | 1 | 1 | Code loinc 46098-0 → 107454-1 |
| `birthYear` | 2 | 0 | + Code loinc 80904-6 · 1 offene(r) Punkt(e) |
| `bodyMassIndex` | 3 | 0 | + Ref. Onkopedia NSCLC (n/a/n/a); + Ref. OCP Lung (AU) (n/a/n/a); Feld `instruction_de` |
| `cancerDiagnosis` | 7 | 0 | Ref. andere präzisiert (n/a/n/a); + Ref. OCP Lung (AU) (n/a/n/a); Code snomed-ct 363358000 → 93880001; Feld `value_set.binding_strength`; Feld `value_set.notes`; Feld `definition_de` · 1 offene(r) Punkt(e) |
| `cancerTreatmentHistory` | 9 | 1 | − Code loinc 21946-9; − Code loinc 21943-6; + Code snomed-ct 119746007; + Code snomed-ct 1255831008; + Code icd-10-gm Z92.6; Ref. andere präzisiert (n/a/n/a); + Ref. OCP Lung (AU) (n/a/n/a); Feld `care_process.frequency_pattern` · 1 offene(r) Punkt(e) |
| `coTreatingProviderContact` | 3 | 1 | + Ref. andere (n/a/n/a); + Ref. OCP Lung (AU) (n/a/n/a); + Beziehung isPartOf survivorshipCarePlan |
| `comorbidity` | 6 | 0 | + Ref. andere (n/a/n/a); + Ref. OCP Lung (AU) (n/a/n/a); + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. AG LONKO / Survivorship (Statement/n/a); Feld `value_set.notes` · 1 offene(r) Punkt(e) |
| `currentMedicationPlan` | 4 | 0 | + Ref. andere (n/a/n/a); + Ref. OCP Lung (AU) (n/a/n/a); Code snomed-ct 713114000 → 721912009; Feld `value_set.notes` |
| `currentTumorStatus` | 5 | 0 | Ref. andere präzisiert (n/a/n/a); + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. OCP Lung (AU) (n/a/n/a) · 2 offene(r) Punkt(e) |
| `diagnosticReportDocument` | 10 | 0 | Ref. andere präzisiert (n/a/n/a); + Ref. Onkopedia NSCLC (n/a/n/a); + Ref. Onkopedia SCLC (n/a/n/a); + Code kdl DG020111; + Code kdl PT260102; Feld `care_process.frequency_pattern`; − Beziehung generalizes ctThoraxFinding; + Beziehung hasPart ctThoraxFinding; − Beziehung generalizes brainMriFinding; + Beziehung hasPart brainMriFinding |
| `dischargeOrVisitReport` | 4 | 0 | Ref. andere präzisiert (n/a/n/a); + Code kdl AD010111; + Ref. OCP Lung (AU) (n/a/n/a); + Beziehung hasPart recommendationsForPrimaryCare |
| `historyTakingPrimaryCare` | 1 | 2 | + Code loinc 11329-0 |
| `immunizationStatus` | 4 | 3 | + Ref. andere (n/a/n/a); + Ref. andere (A/I–IIu (AGIHO/ESCMID-Skala, nicht AWMF)); Feld `care_process.trigger` · 1 offene(r) Punkt(e) |
| `laboratoryResultsReport` | 5 | 1 | Code snomed-ct 15220000 → 4241000179101; Feld `constraints_de`; + Ref. S3-LL Lungenkarzinom (n/a/n/a); + Ref. andere (n/a/n/a) · 1 offene(r) Punkt(e) |
| `lastPracticeContactDate` | 0 | 0 | — |
| `mentalHealthStatus` | 4 | 1 | + Ref. S3-LL Palliativmedizin (A/4); + Ref. S3-LL Palliativmedizin (EK/n/a); + Ref. S3-LL Lungenkarzinom (EK/n/a) · 1 offene(r) Punkt(e) |
| `ongoingSupportiveServices` | 6 | 0 | Code snomed-ct 722138006 → 91251008; Code snomed-ct 417511005 → 90817005; + Ref. S3-LL Palliativmedizin (EK/n/a); + Ref. OCP Lung (AU) (n/a/n/a); + Ref. andere (n/a/n/a) · 1 offene(r) Punkt(e) |
| `patientContactMasterData` | 6 | 0 | Code loinc 54505-3 → 54899-0; Code snomed-ct 370157003 → 428996008; Feld `constraints_de`; + Ref. OCP Lung (AU) (n/a/n/a) · 2 offene(r) Punkt(e) |
| `patientGoalsAndPreferences` | 5 | 0 | Code loinc 52685-5 → 75773-2; − Code snomed-ct 1397166002; Feld `iso13972_metadata.type`; + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. S3-LL Palliativmedizin (EK/n/a) |
| `patientName` | 0 | 0 | — |
| `plannedFollowUpAppointment` | 3 | 0 | + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. OCP Lung (AU) (n/a/n/a) · 1 offene(r) Punkt(e) |
| `psychoOncologyContact` | 4 | 0 | + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. OCP Lung (AU) (n/a/n/a); + Code snomed-ct 413736002; + Beziehung dependsOn mentalHealthStatus |
| `reasonForEncounter` | 3 | 2 | + Ref. andere (n/a/n/a); Feld `value_set.notes`; + Beziehung dependsOn cancerTreatmentHistory |
| `recommendationsForPrimaryCare` | 6 | 0 | Ref. andere präzisiert (n/a/n/a); Code snomed-ct 424900004 → 427272008; − Code loinc 74156-1; − Code kdl VL040309; + Ref. OCP Lung (AU) (n/a/n/a); + Beziehung isPartOf dischargeOrVisitReport |
| `referralOrder` | 4 | 0 | + Code kdl AU050101; + Code kdl AM160301; + Ref. OCP Lung (AU) (n/a/n/a) · 1 offene(r) Punkt(e) |
| `responsiblePrimaryCarePhysician` | 2 | 1 | Feld `cardinality`; + Ref. OCP Lung (AU) (n/a/n/a) |
| `riskFactorAndAlert` | 3 | 0 | Code icd-10-gm Z88 → Z88.9; + Ref. OCP Lung (AU) (n/a/n/a) · 1 offene(r) Punkt(e) |
| `socialSituation` | 8 | 0 | Code snomed-ct 48176007 → 160476009; Code snomed-ct 133932002 → 184156005; Code icd-10-gm Z74 → Z74.9; + Ref. S3-LL Palliativmedizin (EK/n/a); + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. OCP Lung (AU) (n/a/n/a); + Ref. AG LONKO / Survivorship (Statement/n/a) · 1 offene(r) Punkt(e) |
| `standardizedAssessmentScore` | 5 | 1 | Code snomed-ct 446053003 → 718366000; Feld `unit`; + Ref. S3-LL Palliativmedizin (B/1+); + Ref. S3-LL Palliativmedizin (0/3) · 1 offene(r) Punkt(e) |
| `tnmStage` | 7 | 0 | + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. OCP Lung (AU) (n/a/n/a); Code snomed-ct 405979002 → 399588009; Feld `care_process.frequency_pattern`; Feld `care_process.trigger`; Feld `care_process.responsible_role` · 1 offene(r) Punkt(e) |
| `treatmentIntent` | 5 | 2 | − Code snomed-ct 395077000; + Ref. OCP Lung (AU) (n/a/n/a); + Ref. Onkopedia NSCLC (n/a/n/a); + Ref. Onkopedia SCLC (n/a/n/a); + Beziehung dependsOn tnmStage |
| `treatmentSideEffectOrComplication` | 9 | 1 | + Code snomed-ct 373865001; + Code snomed-ct 18846006; + Code icd-10-gm T88.7; + Code icd-10-gm J70.0; + Code icd-10-gm J70.4; + Ref. andere (n/a/n/a); + Ref. OCP Lung (AU) (n/a/n/a); + Beziehung dependsOn cancerTreatmentHistory · 1 offene(r) Punkt(e) |
| `treatmentStatus` | 6 | 0 | Feld `value_set.notes`; + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. OCP Lung (AU) (n/a/n/a); − Beziehung dependsOn therapyLineNumber; + Beziehung dependsOn cancerTreatmentHistory · 1 offene(r) Punkt(e) |
| `tumorBoardDecision` | 5 | 1 | Code snomed-ct 1268903003 → 399414003; + Ref. S3-LL Lungenkarzinom (EK/n/a); + Ref. OCP Lung (AU) (n/a/n/a); − Beziehung dependsOn curativeRecurrencePotential; + Beziehung hasPart curativeRecurrencePotential |
| `tumorHistology` | 5 | 3 | Code snomed-ct 250537006 → 911750741000004104; Code loinc 22036-8 → 59847-4; + Ref. S3-LL Lungenkarzinom (EK/n/a); Feld `definition_de`; Feld `instruction_de` |
| `tumorLocalisation` | 3 | 0 | Code snomed-ct 260716003 → 399687005; + Ref. S3-LL Lungenkarzinom (n/a/n/a) · 1 offene(r) Punkt(e) |
| `workIncapacityCertificate` | 3 | 1 | − Code icd-10-gm Z56; + Ref. AG LONKO / Survivorship (Statement/n/a) · 1 offene(r) Punkt(e) |

## 5 Offene Punkte für das klinische Review

Die offenen Punkte stehen jeweils in `issues[]` des Elements (80 aus der inhaltlichen Prüfung, 33 aus dem Mapping-Audit; im Katalog jetzt 120, vorher 11). Schwerpunkte: Instrumentenwahl (HADS vs. GAD-2/MIDOS, PHQ-9 vs. Whooley/HADS-D), Achsenmischung im Wertebereich (`smokingStatus`: Tabakstatus, E-Zigarette, Passivrauch), fehlende Standardcodes (Mischschmerz, oMME, Distress-Thermometer), Zeitpunkt des Survivorship Care Plan (OCP/AG LONKO vs. Klein 2026), Dokumentklassen (KDL) und Repräsentation in den nationalen Profilen (MII Onko, MII PRO, MII Dokument).

Zwei strukturelle Fragen für Maintainer:innen und Review:

- **Element-Versionierung:** Nach `docs/howto-add-element.md` §C wären die beiden Datentyp-Änderungen (`adverseEventCtcaeGrade`, `qolEortcQlqC30`) Major-Änderungen mit neuer ID und die Kardinalitätsänderungen mindestens Minor. Im AuthorDraft-Stadium wurde die Regel bisher nicht angewendet (alle 112 Elemente `0.1.0`, auch nach den Code-Korrekturen vom 13.10.). Vor dem Release 0.2.0-rc.1 zu entscheiden: Versionen jetzt anheben oder die Regel ab dem ersten klinischen Review anwenden.
- **`dependsOn`-Zyklen:** Vier Zyklen bestehen weiter (vorher sieben), alle um `recurrenceOrSecondPrimary` und die Bildgebung (Rezidivverdacht löst Bildgebung aus, Bildgebung liefert den Befund). Die Bedeutung von `dependsOn` (Auslöser vs. Datengrundlage) ist festzulegen.

## 6 Grenzen

- Prüfung und Gegenprüfung sind KI-gestützt. Die konservative Regel (verwerfen, sobald eine Linse widerlegt) kann berechtigte Korrekturen verworfen haben (88 Vorschläge); sie sind nicht angewendet und können im Review erneut aufgegriffen werden.
- Die Primärquellen lagen als Textfassungen der PDFs vor (Layout-Extraktion); Zitate wurden wörtlich geprüft, Tabellen- und Spaltenzuordnungen bleiben eine mögliche Fehlerquelle.
- MedDRA und ICF sind auf dem MII TermServ nicht verfügbar; MedDRA-Codes wurden gegen das MII-ValueSet der CTCAE-Terme geprüft.
- Onkopedia-Fassungen ändern sich online; die Pins sind bei der nächsten Prüfung erneut abzugleichen.
