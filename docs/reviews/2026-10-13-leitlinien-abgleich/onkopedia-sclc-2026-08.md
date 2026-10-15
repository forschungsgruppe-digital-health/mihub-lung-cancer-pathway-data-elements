# Onkopedia-Leitlinie „Lungenkarzinom, kleinzellig (SCLC)“ — Nachsorge / Surveillance: Abgleich mit dem MiHUB-Datenelemente-Katalog

> **Momentaufnahme vor der Umsetzung (2026-10-13).** Read-only-Abgleich des Katalogstands `0.1.0-rc.2` (51 Elemente) gegen die Leitlinie; die daraus abgeleiteten Änderungen sind in `docs/audit-log.md` §13 dokumentiert und im zugehörigen Pull Request umgesetzt. Zeilen- und Elementangaben beziehen sich auf den Stand **vor** dem Update. Erstellt KI-gestützt (Claude Code, Fable 5.1) mit Live-Abruf der Quellen; mit **UNSICHER** markierte Punkte sind nicht verifiziert.

- **Erstellt:** 2026-10-13 (Read-only-Recherche; es wurde nichts im Repository verändert)
- **Scope:** Kap. 10 „Verlaufskontrolle und Nachsorge“ (Tab. 9), PCI-Nachsorge, MRT-Schädel-Überwachung (Watch-and-Wait), Verlaufskontrolle unter Therapie, Rehabilitation, Tabak, Psychoonkologie, Spätfolgen, Zweittumoren
- **Katalog-Stand:** `data-elements` Version `0.1.0-rc.2` (HEAD `8acb4f6`), `catalog/data-dictionary.csv` — 51 Elemente: `followup` 18 · `surveillance` 15 · `palliative` 18; **alle** Elemente tragen `tumor_entity = NSCLC,SCLC` (kein einziges Element ist SCLC-spezifisch)
- **Legende Status:** COVERED = Element vorhanden und SCLC-Logik passt · PARTIAL = Element vorhanden, aber Intervall/Trigger/Entität/Referenz bildet den SCLC-Plan nicht ab · MISSING = kein Element · **UNSICHER** = nicht verifizierbar bzw. Interpretation

---

## 1 Quelle + Version/Stand

| Feld | Wert |
| --- | --- |
| Titel | Lungenkarzinom, kleinzellig (SCLC) — Onkopedia (DGHO, ÖGHO, SGMO, AIO, DKR) |
| URL | https://www.onkopedia.com/de/onkopedia/guidelines/lungenkarzinom-kleinzellig-sclc/@@guideline/html/index.html |
| **Stand (aktuell gültig)** | **August 2026** („Dies ist die aktuell gültige Version des Dokuments“) |
| Archivierte Versionen | September 2025 · Januar 2023 · September 2019 · April 2017 · November 2012 |
| ICD-10 | C34.- |
| Autor:innen (21) | Bleckmann, Borrass, Eberhardt, Eichhorn, Frost, Früh, Gautschi, Griesinger, Hoffmann, John, Jost, Kiesewetter-Wiederkehr, Köstler, Kraywinkel, Loges, Pöttgen, Reck, Reinmuth, Schütte, Sebastian, Waller, Wolf |
| Kapitelstruktur Nachsorge | **Kap. 9 Rehabilitation** · **Kap. 10 Verlaufskontrolle und Nachsorge** → 10.1 „[Kapitel nicht relevant]“, **10.2 Nachsorge** mit **Tabelle 9 „Strukturierte Nachsorge nach kurativer Therapie“** (Nummerierung unverändert gegenüber der Katalog-Annahme „Kap. 10 / Tab. 9“) |

**Kap. 0 „Änderungen gegenüber Vorversion“ (gegenüber September 2025), vollständig:**
1. Einarbeitung des aktuellen Zulassungsstatus von Tarlatamab
2. Einarbeitung des aktuellen Zulassungsstatus von Lurbinectedin in Kombination mit Atezolizumab
3. Entfernung des Algorithmus zur Rezidivtherapie ohne Verfügbarkeit von Tarlatamab
4. Differenzierung des Algorithmus zur Rezidivtherapie (Abbildung 8)
5. Redaktionelle Korrekturen

→ Keine inhaltliche Änderung an Kap. 9/10 bzw. Tab. 9 ausgewiesen. Der Katalog zitiert „Onkopedia SCLC, Stand 09/2025“ (in `brainMriHighRisk`, `ctThoraxScan`, `followUpInterval`); die Zitate sind damit **versionsveraltet, inhaltlich aber vermutlich unverändert** — **UNSICHER**, da die Archivfassung 09/2025 nicht gegen 08/2026 gedifft wurde („Redaktionelle Korrekturen“ nicht ausgeschlossen).

**Nebenbefund S3-Leitlinie:** Das Onkopedia-Literaturverzeichnis zitiert „AWMF S3-Leitlinie … Lungenkarzinom, **Version 5.1, 2026**“; die Seite des Leitlinienprogramms Onkologie führt „Version 5, 2026“, Langversion 5.0 (Juni 2026) und ein PDF `…_Langversion_5.1.pdf`. Der Katalog zitiert durchgehend „S3-LL Lungenkarzinom 5.01 (Konsultationsfassung 04/2026)“ → **veraltet**; ob sich Nummerierung/Wortlaut von Kap. 16 / Empf. 16.x zwischen Konsultationsfassung und Publikation geändert haben, wurde hier **nicht geprüft (UNSICHER)**.

---

## 2 Nachsorgeprogramm (Onkopedia SCLC, Stand 08/2026)

### 2.1 Tabelle 9 — wörtlich (aus dem HTML-Markup)

> **Tabelle 9: Strukturierte Nachsorge nach kurativer Therapie**

| Untersuchung | 3 Mo | 6 | 9 | 12 | 18 | 24 | 36 | 48 | 60 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Anamnese, körperliche Untersuchung | X | X | X | X | X | X | X | X | X |
| CT Thorax | X | X | X | X | X | X | X | X | X |
| Lungenfunktion | X | X | X | (X) | (X) | (X) | — | — | — |
| MRT Schädel bei LD ohne PCI | X | X | X | X | X | X | X | (X) | (X) |

Legende (wörtlich): „CT = Computertomographie, MRT = Magnetresonanztomographie, LD = Limited disease, PCI = prophylaktische Schädelbestrahlung nach Strahlentherapie“. Die Bedeutung von „(X)“ wird **nicht** erläutert — Lesart „fakultativ/individuell“ ist Interpretation (**UNSICHER**).

Fußnote (wörtlich): „Ergibt sich durch die Nachsorge Untersuchungen der V.a. ein lokalisiertes Rezidiv oder eine evtl. lokal behandelbare Rezidivsituation, ist die Diagnostik durch weitere Bildgebung ggf. einschließlich PET-CT und/oder Methoden zur histologischen Sicherung zu ergänzen.“

Einleitungstext 10.2 (wörtlich): „Ziele der Nachsorge sind die frühzeitige Diagnose eines Rezidivs mit dem Ziel der Verlängerung der Überlebenszeit, die frühzeitige Diagnostik einer Zweitneoplasie, die Erkennung von Nebenwirkungen der Therapie und Vorsorge. Dies betrifft Pat. in den lokalisierten Stadien. Eine strukturierte Nachsorge kann sich an den Empfehlungen für das NSCLC orientieren, siehe Tabelle 9.“

Abgeleitetes Intervallmuster (Katalog-Notation): **Q3M-Y1 (3/6/9/12) ; Q6M-Y2 (18/24) ; Q12M-Y3–Y5 (36/48/60)** — d. h. **9 Zeitpunkte**, ein Zeitpunkt mehr als Onkopedia-NSCLC Tab. 12 (3/6/12/18/24/36/48/60, lt. Katalog).

### 2.2 Vollständiges Programm (inkl. Items außerhalb Tab. 9)

| Nr | Maßnahme | Intervall / Zeitpunkt | Zielpopulation | Empfehlungswortlaut (Kurzzitat) | Referenz |
| --- | --- | --- | --- | --- | --- |
| N1 | Anamnese + körperliche Untersuchung | Mo 3, 6, 9, 12, 18, 24, 36, 48, 60 (alle „X“) | lokalisierte Stadien (VLD/LD) nach kurativer Therapie | Tabellenzeile; „kann sich an den Empfehlungen für das NSCLC orientieren“ | Kap. 10.2, Tab. 9 |
| N2 | CT Thorax | Mo 3–60, alle 9 Zeitpunkte „X“ | wie N1 | Tabellenzeile | Tab. 9 |
| N3 | Lungenfunktion | „X“ Mo 3, 6, 9; „(X)“ Mo 12, 18, 24; keine ab Mo 36 | wie N1 (nicht auf Bestrahlte eingeschränkt) | Tabellenzeile | Tab. 9 |
| N4 | MRT Schädel | „X“ Mo 3–36 (3, 6, 9, 12, 18, 24, 36); „(X)“ Mo 48, 60 | **LD ohne PCI** | „MRT Schädel bei LD ohne PCI“ | Tab. 9 |
| N5 | Diagnostik-Eskalation bei Rezidivverdacht | ad hoc | Pat. mit V. a. lokalisiertes / lokal behandelbares Rezidiv | „weitere Bildgebung ggf. einschließlich PET-CT und/oder Methoden zur histologischen Sicherung“ | Tab. 9 Fußnote; Kap. 6.1.2.1 (PET-CT + MRT Schädel vor Re-Resektion/CRT) |
| N6 | Nachsorgeziele (Rezidiv, Zweitneoplasie, Therapie-Nebenwirkungen, Vorsorge) | — | lokalisierte Stadien | siehe Zitat 10.2 | Kap. 10.2 |
| N7 | PCI im Stadium LD — Nachsorge **nach** PCI | **kein** Routine-MRT in Tab. 9 (nur „ohne PCI“); kein neurokognitives Instrument empfohlen | LD nach simultaner CT-RT | „Die PCI ist daher etablierter Therapiebestandteil für Pat. nach simultaner CT-RT.“ · „Die PCI kann mit Einschränkungen der kognitiven Fähigkeit verbunden sein.“ | Kap. 6.1.1.3; 8.2.2 — **Lücke in der LL (UNSICHER, was nach PCI zu tun ist)** |
| N8 | ED: PCI **vs.** MRT-Überwachung (Watch-and-Wait) | Intervall von Onkopedia **nicht** festgelegt; „alle 3 Monate“ ist ausschließlich das Studiendesign des Kontrollarms (Takahashi 2017, Lancet Oncol) | ED nach Response auf Erstlinien-Systemtherapie, ohne Hirnmetastasen | „In selektionierten Pat. kann die PCI nach Response auf Systemtherapie als Alternative zur Überwachung mit MR-Verlaufskontrollen angeboten und sollte individuell erörtert werden.“ · „Eine PCI bei ED kann eine Option zu sein, wenn keine regelmäßigen MRT-Schädel-Kontrollen durchgeführt werden.“ · Studienbeschreibung: „Hier erfolgte alle 3 Monate eine MRT Schädel-Untersuchung im Kontrollarm“ | Kap. 6.1.1.5; 8.2.2 |
| N9 | Verlaufskontrolle unter Erstlinien-Chemo-Immuntherapie (ED) | Ansprechensbeurteilung „nach frühestens 2 Therapiezyklen, in der Regel nach 3 bis 4 Zyklen“; 4 (max. 6) Zyklen; Modalität/Intervall unter Erhaltung **nicht** spezifiziert | ED | „Das Ansprechen auf die Chemo- und Immuntherapie kann nach frühestens 2 Therapiezyklen, in der Regel nach 3 bis 4 Zyklen, beurteilt werden.“ | Kap. 6.1.1.4.1.7 |
| N10 | Immun-Erhaltung (ED) | „für mindestens 2 Jahre oder bis zum Progress“ | ED nach Chemo-Immuntherapie | Kap. 6.1.1.4.1.6; Therapiedauer-Absatz („anschließend wird die Immuntherapie bis zur Progression fortgeführt“) | Kap. 6.1.1.4.1.6 |
| N11 | Durvalumab-Konsolidierung (LD) | 2 Jahre; Verlaufskontroll-Intervalle **nicht** spezifiziert | LD, nicht progredient nach platinbasierter RCT | „wird eine Konsolidierung mit Durvalumab für 2 Jahre empfohlen“ | Kap. 1 (Zusammenfassung), 6.1.1.2.1 |
| N12 | Rehabilitation + sozialrechtliche Beratung | „frühzeitig“ | alle SCLC-Pat. mit Therapiefolgestörungen | „Die Pat. sollen über die Möglichkeiten ambulanter und stationärer Rehabilitationsmaßnahmen sowie weiterer Ansprüche, die sich aus dem Sozialrecht ergeben, frühzeitig informiert werden. … Wünsche der Pat. berücksichtigt werden (§9 SGB IX). Dennoch sollte eine Empfehlung für eine Klinik mit onkologischem Schwerpunkt abgegeben werden“ | Kap. 9 |
| N13 | Tabak | keine explizite Entwöhnungsempfehlung in Kap. 9/10; „Vorsorge“ als Nachsorgeziel | — | „Das Vermeiden von Rauchen ist die entscheidende Präventionsmaßnahme“ | Kap. 3.1; 10.2 („Vorsorge“) |
| N14 | Psychoonkologie / psychosozial | nicht explizit | — | Kap. 9: „rehabilitative Maßnahmen im somatischen und psychosozialen Bereich“; Kap. 8.4: „Behandlung körperlicher und psychischer Beschwerden“ | Kap. 9; 8.4 |
| N15 | Spätfolgen / Therapiefolgestörungen | per Visite (implizit) | — | 10.2 „Erkennung von Nebenwirkungen der Therapie“; Kap. 9 „Therapiefolgestörungen unterschiedlichen Schwergrades“; PCI-Kognition (6.1.1.3); Lungenfunktion (Tab. 9) | Kap. 9; 10.2; 6.1.1.3 |
| N16 | Zweittumor | ad hoc | nach Resektion + adjuvanter CTx | „muss an die Möglichkeit eines Zweittumors auch anderer Histologie gedacht werden“ | Kap. 6.1.2.1; 10.2 |
| N17 | PRO / Symptom-Selbsterfassung | **kein Item** in Onkopedia SCLC | — | — | — |
| N18 | Labor / Tumormarker (NSE, CEA) | **kein Item** in der Nachsorge (nur Erstdiagnostik Tab. 2: „Blutbild, Elektrolyte, Harnsäure, Nierenparameter, Leberparameter, LDH, Gerinnung, NSE ± CEA“) | — | — | Tab. 2 (Kap. 5.2.1) |
| N19 | Geriatrisches Assessment (ältere Pat.) | Therapieentscheidung, nicht Nachsorge | ältere Pat. | „wird bei älteren Pat. die Verwendung von Instrumenten des Geriatrischen Assessment empfohlen“ | Kap. 5.6 |

---

## 3 Abdeckungs-Matrix (Katalog-Phasen `followup` / `surveillance`)

| Leitlinien-Item | Status | Repo-Element(e) | Lücke |
| --- | --- | --- | --- |
| N1 Anamnese + körperliche Untersuchung (9 Zeitpunkte) | **PARTIAL** | `firstFollowUpVisitDate` (nur Erstvorstellung, `once`), `ecogPerformanceStatus`, `postTherapyComplication`, `smokingStatus` (alle `per-encounter`), `followUpInterval` (Plan) | Kein Element bildet die **Nachsorge-Visite selbst** (Datum/Durchführung von Anamnese + körperlicher Untersuchung je Zeitpunkt) ab; `per-encounter`-Elemente setzen eine Visite voraus, die nirgends dokumentiert ist. Keine Onkopedia-SCLC-Referenz. |
| N2 CT Thorax | **PARTIAL** | `ctThoraxScan` (`Q3M-Y1-Y2;Q6M-Y3-Y5`; Trigger nennt „Tab. 9 SCLC“; Ref. Onkopedia SCLC Stand 09/2025 Tab. 9), `ctThoraxFinding` | Intervall ≠ Tab. 9 (SCLC: Q3M-Y1; Q6M-Y2; Q12M-Y3–Y5 — Jahr 2 und Jahre 3–5 weichen ab); Version 09/2025 → 08/2026. |
| N3 Lungenfunktion | **PARTIAL** | `pulmonaryFunctionTest` (`Q3M-Y1; ab Y2 individuell`; Trigger „Nach Strahlentherapie/Radiochemotherapie“), `fev1PercentPredicted`, `dlcoPercentPredicted` | Tab. 9: obligat Mo 3/6/9, fakultativ 12/18/24, **Ende nach Mo 24** — nicht codiert; Trigger auf Bestrahlte verengt (Tab. 9 nicht); **keine** Onkopedia-SCLC-Referenz (nur S3 + Onkopedia NSCLC Tab. 12). |
| N4 MRT Schädel bei LD ohne PCI | **PARTIAL** | `brainMriHighRisk` (`Q3M-Y1 (SCLC LD ohne PCI)`; Ref. Onkopedia SCLC 09/2025 Tab. 9), `brainMriFinding` | Tab. 9 sieht MRT **bis Mo 36 obligat, 48/60 fakultativ** vor — Katalog endet nach Jahr 1; Trigger „ohne PCI“ ist nicht auswertbar, weil **kein Element den PCI-Status** erfasst (siehe § 4 A); Version veraltet. Entität-Vermischung NSCLC/SCLC in einem Element (Hochrisiko-Genotyp vs. LD ohne PCI) ist zulässig, aber das `frequency_pattern` ist dadurch ein Freitext-Doppel. |
| N5 Diagnostik-Eskalation (PET-CT / histologische Sicherung) | **MISSING** | — (`molecularRetestingCtdna` / `molecularResistanceFinding` betreffen Resistenztestung unter zielgerichteter NSCLC-Therapie, nicht die Rezidivsicherung) | Kein Element für PET-CT bzw. histologische Sicherung bei Rezidivverdacht (Tab. 9 Fußnote; 6.1.2.1). |
| N6 Nachsorgeziele: Rezidiv / Zweitneoplasie | **COVERED** | `recurrenceOrSecondPrimary` (Second primary + ICD-O-M-Codes inkl. 8041/3) | Nur Referenz ergänzen (Kap. 10.2; 6.1.2.1 „Zweittumor auch anderer Histologie“). |
| N6 Nachsorgeziele: Nebenwirkungen der Therapie | **COVERED** (allgemein) | `postTherapyComplication`; unter Therapie `adverseEventCtcae`, `adverseEventCtcaeGrade`, `immuneRelatedAdverseEvent` | SCLC-spezifische Spätfolge **kognitive Einschränkung nach PCI** (6.1.1.3) nicht im ValueSet. |
| N6 Nachsorgeplan / Population „lokalisierte Stadien“ | **COVERED** | `structuredFollowUpPlan` (Definition „Stadium I–IIIC, OMD“), `survivorshipCarePlan` | Für SCLC heißt die Population VLD/LD (Kap. 10.2) — Definition/Referenz ergänzen; sonst passend. |
| N7 Nachsorge nach PCI (LD) | **MISSING** (LL selbst unspezifisch) | — | Kein PCI-Status-Element; kein Element für neurokognitive Folgen. Die LL gibt **keine** Maßnahme nach PCI vor → jedes Element wäre „abgeleitet“ (**UNSICHER**). |
| N8 ED: PCI vs. MRT-Überwachung | **PARTIAL** | `brainMriUnderTherapy` (surveillance; Trigger „… ODER SCLC ED Watch-and-Wait“; `Q3M (SCLC ED W&W)`; Ref. **nur** S3-LL Kap. 16.3.4) | Keine Onkopedia-SCLC-Referenz (6.1.1.5 / 8.2.2); das 3-Monats-Intervall stammt in Onkopedia nur aus dem Takahashi-Studiendesign — Herkunft im Katalog transparent machen; die **Entscheidung** PCI vs. Überwachung („sollte individuell erörtert werden“) ist nirgends dokumentierbar. |
| N9 Verlaufskontrolle unter Erstlinien-Chemo-Immuntherapie | **PARTIAL** | `restagingImagingDate` (`Q6-9W`), `recistResponse` (`Q6-9W`), `ecogPerformanceStatusSurveillance` (`per-cycle`) | SCLC-Logik ist **zyklusbasiert** („nach frühestens 2, i. d. R. 3–4 Zyklen“), nicht wochenbasiert; keine Onkopedia-SCLC-Referenz; Restaging-Modalität/Intervall unter Erhaltung von Onkopedia nicht vorgegeben (**UNSICHER**, S3 Empf. 16.9 bleibt Basis). |
| N10/N11 Immun-Erhaltung (ED ≥ 2 J.) / Durvalumab-Konsolidierung (LD 2 J.) | **COVERED** | `systemicTherapyRegimen` (ATC L01XC18/L01XC32 …), `therapyLineNumber` | Keine Onkopedia-SCLC-Referenz; Konsolidierungs-/Erhaltungs-Ende (2-Jahres-Horizont) nicht als Zeitpunkt modelliert (optional). |
| N12 Rehabilitation + Sozialrecht | **MISSING** | — (`structuredFollowUpPlan` erwähnt „Sozialberatung“ nur in der Definition) | Kein Element für Reha-Information/-Empfehlung oder sozialrechtliche Beratung (Kap. 9: „sollen … frühzeitig informiert werden“). |
| N13 Tabak | **COVERED** (Basis S3) | `smokingStatus` (1..1, per-encounter), `tobaccoCessationCounselling` | Onkopedia SCLC liefert nur Kap. 3.1 / „Vorsorge“ — optional als Zweitreferenz. |
| N14 Psychoonkologie | **COVERED** (Basis S3/OCP) | `distressThermometerScore`, `psychoOncologyReferral` | Onkopedia SCLC nicht explizit — kein Handlungsbedarf aus dieser LL. |
| N15 Spätfolgen | **PARTIAL** | `postTherapyComplication`, `pulmonaryFunctionTest`, `dlcoPercentPredicted`, `fev1PercentPredicted` | PCI-Kognition fehlt (s. o.). |
| N16 Zweittumor | **COVERED** | `recurrenceOrSecondPrimary` | Referenz ergänzen. |
| N17 PRO | — (kein LL-Item) | `patientReportedSymptomWeb`, `qolEortcQlqC30` (Quellen NSCLC/OCP) | Keine Lücke gegenüber Onkopedia SCLC. |
| N18 Labor/Tumormarker | — (kein LL-Item) | — | Korrekt **kein** Element; nicht aufnehmen (siehe § 5). |
| N19 Geriatrisches Assessment | **MISSING** (außerhalb Nachsorge-Scope) | `ecogPerformanceStatus` | Nur relevant, falls `surveillance` die Therapieentscheidung mit abbilden soll — hier nicht weiterverfolgt. |
| Nachsorgeintervall Tab. 9 (9 Zeitpunkte) | **PARTIAL** | `followUpInterval` (ValueSet `Q3M-Y1-Y2`, `Q6M-Y3-Y5`, `Q12M-PostY5`, `Q6-9M`; `section` nennt korrekt „SCLC: 3,6,9,12,18,24,36,48,60 Mo“) | **Kein SCLC-Code** im ValueSet (das Muster Q3M-Y1;Q6M-Y2;Q12M-Y3–Y5 ist nicht wählbar); Version 09/2025 veraltet; **Defekt:** Code `Q6-9M` (Monate) hat Display „alle 6–9 Wochen“ — Surveillance-Elemente nutzen `Q6-9W`. |

**Bilanz:** 19 Leitlinien-Items → COVERED 6 · PARTIAL 8 · MISSING 4 (N5, N7, N12, N19) · kein LL-Item 2 (N17, N18). Querschnittsbefund: **kein** Katalog-Element verweist auf den aktuellen Stand 08/2026; nur 3 Elemente zitieren Onkopedia SCLC überhaupt.

---

## 4 Vorgeschlagene neue oder zu ändernde Datenelemente

Konventionen gemäß `schemas/data-element.schema.json` (Phase-Enum, `tumor_entity`-Enum, `iso13972_metadata.type`, Quelle-Enum enthält bereits `Onkopedia SCLC`). Codes sind **nicht** vorgegeben — Terminologie-Mapping bleibt Aufgabe des MI-Teams (Validator-Skill). Alle Vorschläge tragen `publication_status: AuthorDraft`.

### 4.1 Neue Elemente

**A · `prophylacticCranialIrradiationStatus`** (Phase `followup`; `tumor_entity: [SCLC]`)
- **label_de:** Prophylaktische Schädelbestrahlung (PCI) — Status
- **definition_de:** Dokumentiert, ob nach Abschluss der Erstlinientherapie eine prophylaktische Schädelbestrahlung durchgeführt wurde, nicht durchgeführt wurde (z. B. zugunsten einer MRT-Überwachung) oder vom Pat. abgelehnt wurde, inkl. Datum. Steuert die Bedingung „MRT Schädel bei LD ohne PCI“ in Tab. 9.
- **datatype:** CodeableConcept (Wertebereich: durchgeführt · nicht durchgeführt – MRT-Überwachung · nicht durchgeführt – keine Überwachung · abgelehnt; Datum als `Period`/Erweiterung) · **cardinality:** 1..1 (bei SCLC)
- **trigger:** Abschluss der simultanen Radiochemotherapie (LD) bzw. Response-Beurteilung nach Erstlinien-Chemo-Immuntherapie (ED) · **frequency_pattern:** once-per-treatment-completion · **responsible_role:** Strahlentherapie / Onkologe
- **guideline reference:** {source: "Onkopedia SCLC", version: "Stand 08/2026", section: "Kap. 6.1.1.3 (PCI LD: „etablierter Therapiebestandteil“); 6.1.1.5 + 8.2.2 (PCI ED „Alternative zur Überwachung mit MR-Verlaufskontrollen“); Tab. 9 (Bedingung „LD ohne PCI“)"}
- **related_elements:** `brainMriHighRisk` dependsOn A; `brainMriUnderTherapy` dependsOn A
- **iso13972 type:** procedure · Mapping-Kandidat: `fhir-mii-kds` Modul Onkologie (Strahlentherapie) / `obds` Strahlentherapie-Modul

**B · `cnsSurveillanceDecisionEd`** (Phase `surveillance`; `tumor_entity: [SCLC]`) — *optional, falls die Entscheidung getrennt vom Status A dokumentiert werden soll*
- **label_de:** ZNS-Strategie nach Ansprechen (ED): PCI oder MRT-Verlaufskontrollen
- **definition_de:** Ergebnis der individuellen Erörterung nach Response auf die Erstlinien-Systemtherapie bei Extensive Disease ohne Hirnmetastasen: PCI oder regelmäßige MRT-Schädel-Kontrollen (Watch-and-Wait). Das Kontrollintervall ist von der LL nicht festgelegt (3-monatlich entspricht dem Kontrollarm der japanischen Studie).
- **datatype:** code (PCI · MRT-Überwachung · keine · nicht entschieden) · **cardinality:** 0..1
- **trigger:** Response-Beurteilung nach 2–4 Zyklen Chemo-Immuntherapie · **frequency_pattern:** once · **responsible_role:** Onkologe + Strahlentherapie (gemeinsam mit Pat.)
- **guideline reference:** {source: "Onkopedia SCLC", version: "Stand 08/2026", section: "Kap. 6.1.1.5 („sollte individuell erörtert werden“); 8.2.2 („wenn keine regelmäßigen MRT-Schädel-Kontrollen durchgeführt werden“)"}
- **iso13972 type:** plan

**C · `followUpVisitDate`** (Phase `followup`; `tumor_entity: [NSCLC, SCLC]`)
- **label_de:** Nachsorge-Visite (Anamnese, körperliche Untersuchung) — Datum
- **definition_de:** Datum jeder strukturierten Nachsorge-Visite mit Anamnese und körperlicher Untersuchung nach kurativer Therapie. Ergänzt `firstFollowUpVisitDate` (nur Erstvorstellung) um die Folgezeitpunkte und ist der Anker für alle `per-encounter`-Elemente der Phase.
- **datatype:** dateTime · **cardinality:** 0..*
- **trigger:** Nachsorgezeitpunkte gemäß Tab. 9 (SCLC) bzw. Tab. 12 (NSCLC) · **frequency_pattern:** SCLC: Q3M-Y1;Q6M-Y2;Q12M-Y3-Y5 (Mo 3/6/9/12/18/24/36/48/60) · **responsible_role:** Onkologe / Pneumologe / Hausarzt
- **guideline reference:** {source: "Onkopedia SCLC", version: "Stand 08/2026", section: "Kap. 10.2, Tab. 9 Zeile „Anamnese, körperliche Untersuchung“"} (+ S3-LL Empf. 16.7 als Zweitreferenz)
- **iso13972 type:** observation · Mapping: `fhir-r4-base` Encounter.period.start (wie `firstFollowUpVisitDate`)

**D · `rehabilitationCounselling`** (Phase `followup`; `tumor_entity: [NSCLC, SCLC]`)
- **label_de:** Information/Beratung zu Rehabilitation und sozialrechtlichen Ansprüchen
- **definition_de:** Dokumentiert, dass der/die Pat. frühzeitig über ambulante und stationäre Rehabilitationsmaßnahmen sowie sozialrechtliche Ansprüche informiert wurde, inkl. ausgesprochener Empfehlung einer Klinik mit onkologischem Schwerpunkt und Berücksichtigung des Patientenwunsches (§ 9 SGB IX).
- **datatype:** CodeableConcept (informiert ambulant · informiert stationär · Sozialrechtsberatung erfolgt · Reha-Antrag gestellt · onkologische Schwerpunktklinik empfohlen · abgelehnt) · **cardinality:** 0..*
- **trigger:** frühzeitig, spätestens bei Therapieabschluss / Erstvorstellung in der Nachsorge · **frequency_pattern:** once-per-treatment-completion (Aktualisierung ad-hoc) · **responsible_role:** Onkologe / Sozialdienst
- **guideline reference:** {source: "Onkopedia SCLC", version: "Stand 08/2026", section: "Kap. 9 Rehabilitation („sollen … frühzeitig informiert werden“; „Empfehlung für eine Klinik mit onkologischem Schwerpunkt“)"}
- **iso13972 type:** procedure · Mapping-Kandidat: `fhir-r4-base` ServiceRequest/Procedure; `kbv-mio` Reha-Verordnung (zu prüfen)

**E · `recurrenceWorkup`** (Phase `followup`; `tumor_entity: [NSCLC, SCLC]`)
- **label_de:** Rezidivdiagnostik bei Verdacht (PET-CT / histologische Sicherung)
- **definition_de:** Bei Verdacht auf ein lokalisiertes oder lokal behandelbares Rezidiv in der Nachsorge durchgeführte Zusatzdiagnostik: weitere Bildgebung (insb. PET-CT, MRT Schädel) und/oder Methoden der histologischen Sicherung (z. B. Bronchoskopie mit Biopsie, transthorakale Biopsie). Ergebnisartefakt ist `recurrenceOrSecondPrimary`.
- **datatype:** CodeableConcept (PET-CT · MRT Schädel · CT Abdomen · Bronchoskopie/Biopsie · transthorakale Biopsie · EBUS/EUS · andere) mit Datum · **cardinality:** 0..*
- **trigger:** V. a. Rezidiv in einer Nachsorge-Untersuchung (Tab. 9) · **frequency_pattern:** ad-hoc · **responsible_role:** Onkologe / Radiologie / Pneumologie / Pathologie
- **guideline reference:** {source: "Onkopedia SCLC", version: "Stand 08/2026", section: "Tab. 9 Fußnote („weitere Bildgebung ggf. einschließlich PET-CT und/oder Methoden zur histologischen Sicherung“); Kap. 6.1.2.1 (PET-CT + MRT Schädel vor Re-Resektion / simultaner CRT)"}
- **iso13972 type:** procedure · Mapping: `fhir-mii-kds` Modul Bildgebung (ImagingStudy) / Modul Pathologie

### 4.2 Änderungen an bestehenden Elementen

| Element (Datei) | Änderung | Referenz |
| --- | --- | --- |
| `followUpInterval` (`elements/follow-up/followUpInterval.yaml`) | ValueSet um SCLC-Code ergänzen, z. B. `Q3M-Y1;Q6M-Y2;Q12M-Y3-Y5` (Display „alle 3 Mo Jahr 1, alle 6 Mo Jahr 2, jährlich Jahr 3–5 — SCLC Tab. 9“); **Display-Defekt** `Q6-9M` → „Wochen“ korrigieren (Code `Q6-9W` oder Display „Monate“ — Abgleich mit `restagingImagingDate`); Onkopedia-SCLC-Version 09/2025 → 08/2026 | Tab. 9 |
| `ctThoraxScan` | `frequency_pattern` für SCLC: `Q3M-Y1;Q6M-Y2;Q12M-Y3-Y5` (9 Zeitpunkte); Version 08/2026 | Tab. 9 |
| `brainMriHighRisk` | SCLC-Teil des `frequency_pattern`: `Q3M-Y1;Q6M-Y2;Q12M-Y3` obligat, `Y4–Y5 fakultativ` (Tab. 9 „(X)“ 48/60); `related_elements: dependsOn` → Element A; Version 08/2026 | Tab. 9 |
| `brainMriUnderTherapy` | Zweitreferenz Onkopedia SCLC Kap. 6.1.1.5 / 8.2.2 ergänzen; `notes`: Intervall Q3M = Studiendesign Takahashi 2017 (Onkopedia legt kein Intervall fest; S3-Kap. 16.3.4-Wortlaut hier **nicht** verifiziert — UNSICHER); `dependsOn` → Element A/B | Kap. 6.1.1.5; 8.2.2 |
| `pulmonaryFunctionTest` | SCLC-Schema codieren: obligat Mo 3/6/9, fakultativ Mo 12/18/24, **kein** Routine-Termin ab Mo 36; Trigger nicht auf Bestrahlte verengen; Referenz Onkopedia SCLC Tab. 9 ergänzen | Tab. 9 |
| `restagingImagingDate`, `recistResponse` | Trigger-Variante SCLC: „nach frühestens 2, i. d. R. nach 3–4 Zyklen Chemo-Immuntherapie“ (zyklusbasiert); Referenz Kap. 6.1.1.4.1.7 ergänzen; Hinweis, dass Onkopedia SCLC Modalität/Intervall unter Erhaltung nicht vorgibt | Kap. 6.1.1.4.1.7 |
| `recurrenceOrSecondPrimary` | Referenz Onkopedia SCLC Kap. 10.2 + 6.1.2.1 ergänzen; `related_elements: dependsOn` → Element E | Kap. 10.2; 6.1.2.1 |
| `postTherapyComplication` | ValueSet um **kognitive Einschränkung nach PCI** erweitern (SNOMED-Code durch MI-Team); Referenz Kap. 6.1.1.3 / 8.2.2 (LL benennt Nebenwirkung, empfiehlt **kein** Messinstrument → abgeleitet, UNSICHER) | Kap. 6.1.1.3; 8.2.2 |
| `structuredFollowUpPlan` | Definition um SCLC-Population „lokalisierte Stadien (VLD/LD) nach kurativer Therapie“ ergänzen; Referenz Kap. 10.2 | Kap. 10.2 |
| `systemicTherapyRegimen` | Referenz Onkopedia SCLC Kap. 6.1.1.4.1.6 (Erhaltung ≥ 2 J.) / 6.1.1.2.1 (Durvalumab-Konsolidierung 2 J.) optional ergänzen | Kap. 6.1.1.4.1.6; 1 |
| alle Elemente mit S3-LL-Referenz | Versionsstring „5.01 (Konsultationsfassung 04/2026)“ gegen publizierte Version 5.0 (06/2026) / 5.1 prüfen (**UNSICHER**, ob Kap.-16-Nummerierung stabil) | Onkopedia Lit. [1] |

### 4.3 Nicht aufzunehmen (Begründung in § 5)
Röntgen Thorax, Sonografie Abdomen, Laborparameter/Tumormarker, CT Abdomen / CT Becken als **Routine**-Nachsorgeelemente — ohne Grundlage in Onkopedia SCLC Tab. 9.

---

## 5 Bewertung der Kliniker-Kandidaten (SCLC-Nachsorge / Surveillance)

| Kandidat | Bewertung | Begründung + Referenz (Onkopedia SCLC, Stand 08/2026) | Katalog-Konsequenz |
| --- | --- | --- | --- |
| Anamnese | **JA** | Tab. 9 Zeile 1, alle 9 Zeitpunkte (Mo 3–60) | Element C neu |
| Körperliche Untersuchung | **JA** | Tab. 9 Zeile 1 (gemeinsam mit Anamnese), alle 9 Zeitpunkte | Element C (gemeinsam) |
| Röntgen Thorax | **NEIN** (Routine) | Nicht in Tab. 9; Standard ist CT Thorax. Röntgen Thorax erscheint nur in Tab. 2 Stufe 1 (Erstdiagnostik: „Röntgen Thorax Übersicht in 2 Ebenen“) | nicht aufnehmen |
| Sonografie Abdomen | **NEIN** (Routine) | Nicht in Tab. 9; in Tab. 2 Stufe 3 nur „alternativ Sonographie Oberbauch bei zweifelsfreiem Nachweis einer abdominellen Metastasierung“ (Staging). Bei Rezidivverdacht unspezifisch unter „weitere Bildgebung“ subsumierbar | ggf. Wert in Element E |
| Bronchoskopie | **BEDINGT** | Keine Routine; bei Rezidivverdacht „Methoden zur histologischen Sicherung“ (Tab. 9 Fußnote); Tab. 2 Stufe 2 „Bronchoskopie mit Biopsie … bei bildgebendem Verdacht“ | Wert in Element E (ad-hoc) |
| PET-CT | **BEDINGT** | Tab. 9 Fußnote: „ggf. einschließlich PET-CT“ bei V. a. lokalisiertes / lokal behandelbares Rezidiv; Kap. 6.1.2.1: PET-CT vor Re-Resektion bzw. vor simultaner CRT beim lokoregionären Rezidiv. Keine Routine-PET-CT in der Nachsorge | Wert in Element E (ad-hoc) |
| Abdomen-CT / CT-Abdomen (Doppelnennung in der Kandidatenliste) | **NEIN** (Routine-Nachsorge) / **BEDINGT** (Restaging) | Tab. 9 nennt ausschließlich „CT Thorax“. Bedingt: Rezidivverdacht („weitere Bildgebung“) bzw. Verlaufskontrolle unter Systemtherapie — hierfür legt Onkopedia SCLC weder Modalität noch Intervall fest (**UNSICHER**; `restagingImagingDate` deckt Thorax/Abdomen/Becken via OPS 3-225 auf S3-Basis ab) | kein neues Element; Dublette bereinigen |
| Laborparameter | **NEIN** | Nicht in Tab. 9. Labor inkl. „NSE ± CEA“ nur in der Erstdiagnostik (Tab. 2 Stufe 1); keine Tumormarker-Nachsorge empfohlen. Unter Systemtherapie Toxizitätslabor klinisch üblich, aber von Onkopedia SCLC nicht spezifiziert (**UNSICHER**) | nicht aufnehmen |
| CT-Thorax | **JA** | Tab. 9 Zeile 2, alle 9 Zeitpunkte | `ctThoraxScan` anpassen (§ 4.2) |
| CT Becken | **NEIN** | Weder in Tab. 9 noch in Tab. 2 explizit (dort „CT Thorax / Abdomen“); nur als Teil eines Restagings unter Therapie denkbar — nicht LL-spezifiziert | nicht aufnehmen |
| Schädel-MRT | **JA — populationsabhängig (BEDINGT)** | (1) **LD ohne PCI:** Tab. 9 „X“ Mo 3–36, „(X)“ Mo 48/60. (2) **ED nach Response ohne PCI:** „Überwachung mit MR-Verlaufskontrollen“ (6.1.1.5; 8.2.2) — Intervall nicht festgelegt, 3-monatlich nur als Studiendesign (Takahashi 2017). (3) **Nach PCI:** kein Routine-MRT in Tab. 9 (**UNSICHER**, LL schweigt). (4) Bei lokalem Progress vor Resektion: MRT Schädel zum Ausschluss cerebraler Metastasierung (6.1.2.1) | `brainMriHighRisk` + `brainMriUnderTherapy` anpassen; Element A als Steuerbedingung |

---

## 6 Offene Punkte / UNSICHER (Sammelliste)
1. Bedeutung von „(X)“ in Tab. 9 ist in der LL nicht definiert (Lesart „fakultativ“).
2. Ob Tab. 9 zwischen Stand 09/2025 und 08/2026 wörtlich identisch ist (Kap. 0 nennt keine Nachsorge-Änderung; Archiv nicht gedifft).
3. Wortlaut von S3-LL Kap. 16.3.4 (SCLC ED Watch-and-Wait, „MRT alle 3 Mo“), auf den der Katalog das Q3M-Intervall stützt, wurde hier nicht verifiziert; Onkopedia SCLC selbst legt kein Intervall fest.
4. Versionsdrift S3-LL: Katalog „5.01 Konsultationsfassung 04/2026“ vs. publiziert 5.0 (06/2026) / 5.1 — Kapitel-/Empfehlungsnummern ungeprüft.
5. Nachsorge **nach** PCI (MRT? Neurokognition?) — die LL macht keine Vorgabe; jedes Element dazu ist abgeleitet.
6. Verlaufskontroll-Intervalle unter Durvalumab-Konsolidierung (LD) und Immun-Erhaltung (ED) sind in Onkopedia SCLC nicht spezifiziert.
