# Umsetzungsvorschlag zu den Kommentaren der Nachsorge-WG — 2026-11-25

> **Vorschlag, nicht umgesetzt.** Grundlage sind die fünf Reviewer-Kommentare der Nachsorge-WG zur Word-Fassung der
> Phasen-Übersicht v0.1 (2026-06-12; in der Erhebungsmappe Spalte „Anmerkungen/Beziehungen“, Auszug
> [`2026-10-13-erhebungen.md`](2026-10-13-erhebungen.md)) und der Absatz „Weitere Aspekte“ der Word-Fassung. Bestand und
> Umsetzungsstand: [`docs/audit-log.md`](../audit-log.md) §16.7. Jede Umsetzung braucht die datenelementweise Freigabe
> (AGENTS.md Regel 1); fachliche Fragen beantwortet das klinische Review.

**Vorgehen (KI-gestützt, Claude Code Opus 5.5):** je Thema zwei unabhängige Entwürfe (Perspektive klinische Praxis bzw.
Standards und Katalogregeln), Bewertung und Synthese durch eine Jury, adversariale Prüfung gegen die Element-Dateien,
Verdichtung mit Treueprüfung gegen die geprüfte Langfassung. Genannte Codes wurden stichprobenartig am MII TermServ
geprüft (ICD-10-GM Y57.98, Y84.9, R53.9; SNOMED CT 261665006; LOINC 80391-6; OPS 9-984.6–.b); als UNSICHER
markierte Angaben sind nicht verifiziert.

## Übersicht

| Nr. | Kommentar / Aspekt | Empfehlung (Kurzform) | Versionsfolge | Issue |
| --- | --- | --- | --- | --- |
| 1 | `followUpInterval`: „Flexibel gestalten … zu Beginn eher wöchentlich oder monatlich, später jährlich“ | Leitlinienraster schärfen (S3-Gesamtcode, Soll-Regel, Modifikator Q6-8W nur zusätzlich), engmaschige Kontakte über die Termin-Elemente; Code „individuell“ erst nach Rückmeldung der WG | Patch im offenen Sprung (ID v0.1 bleibt) | [#28](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/28) |
| 2 | `postTherapyComplication`: „Für Hausarzt sehr allgemein … Komplikation zuordnen …“ | neues Teilelement „zugeordnete auslösende Tumortherapie“ (inkl. „Zuordnung nicht möglich“) für Nachsorge und Hausarzt, Mapping-Patches | neues Element 0.1.0; Bestand Patch | [#29](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/29) |
| 3 | Palliativversorgung: „Datenerhebung vs. Respekt vor dem Sterbenden“ | Grundsatz in der Methodik und Erhebungsregel je Palliativ-Element für die Sterbephase, gestuft; Schemafeld später | Patch je Element (IDs bleiben) | [#30](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/30) |
| 4 | `recurrenceOrSecondPrimary`: „Zwei unterschiedliche Dinge … Lokalisation relevant“ | aufteilen in Rezidiv, Fernmetastasen-Lokalisation und Zweitkarzinom; Verweise und `dependsOn`-Zyklen in derselben Änderung bereinigen | brechend: Nachfolger 0.2.0 (ID v0.2) | [#31](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/31) |
| 5 | „Weitere Aspekte“: Pflegebedarf/-grad | neues Element `careGrade` „Pflegegrad (SGB XI)“ in `primarycare`, gebunden an das ValueSet des deutschen Basisprofils | neues Element 0.1.0 | [#32](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/32) |

Der Kommentar „Definieren“ zu `smokingStatus` ist bereits umgesetzt (Definition 2026-10 neu gefasst, Version 0.2.0).

**Gemeinsame Randbedingungen:** Umsetzung vor oder nach dem Tag `v0.2.0-rc.1` abgestimmt mit PR #15/#16
([#27](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/27)); `dependsOn`-Semantik ([#21](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/21)) und Rolle der KDL-Codings ([#20](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/20)) berühren Nr. 1 und 4.
Der Erhebungsauszug nennt in der Anmerkungsspalte den Namen der kommentierenden Person (audit-log §16.6 Nr. 18).

### 1 followUpInterval: Leitlinienraster schärfen, individuelles Raster kennzeichnen, engmaschige Kontakte über die Termin-Elemente

GitHub-Issue: [#28](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/28)

**Kommentar der Nachsorge-WG** (Phasen-Übersicht v0.1, 2026-06-12; Erhebungsauszug `#wg-de-010`, audit-log §16.7): „Flexibel gestalten. Zu Beginn der Nachsorge eher 1x wöchentlich oder monatlich. Später 1x jährlich“. Dieselbe Zeile nennt das S3-Raster und „Genau einmal (Pflicht)“.

**Ausgangslage im Katalog**
- `followUpInterval` 0.1.1, ID v0.1 (0.1.0 in rc.1/rc.2 veröffentlicht): `code` 1..1, Bindung `example`, `no-standard-found`; kein `standard_mappings`, `instruction_de`, `constraints_de`.
- Sechs lokale Codes: S3-Phasencodes (`Q3M-Y1-Y2`, `Q6M-Y3-Y5`, `Q12M-PostY5`), Onkopedia-Gesamtraster NSCLC/SCLC, `Q6-8W-curative-recurrence`. Kein S3-Gesamtcode; der Modifikator Q6-8W steht gleichrangig.
- Offene Issues: Granularität, KFE-RL § 38 Abs. 3 zu `Q12M-PostY5`, Reviewer-Kommentar mit Varianten (a)/(b)/(c).
- Termine: `followUpVisitDate` und `plannedFollowUpAppointment` (je dateTime 0..*, PVS nur `read`). Stattgefundene hausärztliche Kontakte als Serie bildet kein Element ab.
- Auf `followUpInterval.v0.1` verweisen drei unveröffentlichte Elemente (0.1.0). Das Schema kennt keinen Datentyp `Timing`.
- Wöchentlich/monatlich belegt keine hinterlegte Quelle (S3 Empf. 16.7: Jahr 1–2 vierteljährlich); „später jährlich“ ab Jahr 3 nur Onkopedia NSCLC Tab. 12 / SCLC Tab. 9 (S3 nach Jahr 5 nur indirekt). Ein individueller Plan ist nicht kennzeichenbar.

**Optionen**

| Option | Kern | Versionierung (howto §C) | Pro | Contra |
|---|---|---|---|---|
| 1 – Raster schärfen (a + c) | Gesamtcode `Q3M-Y1-Y2;Q6M-Y3-Y5`, Soll-Regel, Verweis auf Termin-Elemente | nicht brechend, im offenen Sprung 0.1.0 → 0.1.1, ID v0.1 bleibt | kein Sprung, kein Schemaeingriff, löst Granularität | individueller Plan nicht gekennzeichnet |
| 2 – wie 1 + Code „individuell“ (b lokal + c) | Abweichungscode, Begründung im Plan-Dokument | wie 1; optionales Begründungselement ab 0.1.0 (112 → 113) | Abweichung zählbar, Option 3 nicht verbaut | Platzhalter, Begründung außerhalb des Katalogs |
| 3 – FHIR `Timing` 0..* | strukturiertes Intervall je Phase | brechend: Minor 0.1.0 → 0.2.0, ID v0.2, drei Ziel-IDs | „flexibel“ wörtlich, maschinenlesbare Soll-Termine | Schema und Skripte, hoher Erfassungsaufwand |

**Empfehlung**
- Option 2, gestuft; Stufe 1 sofort, vor dem Tag v0.2.0-rc.1.
- Codes: neuer Gesamtcode `Q3M-Y1-Y2;Q6M-Y3-Y5` (S3 Empf. 16.7); Phasencodes bleiben als „Teilraster“ (Datenkontinuität); Anzeige von `Q6-8W-curative-recurrence` nur um „zusätzlich zu einem Basisraster“ ergänzt.
- Kardinalität 0..* oder 1..*; `constraints_de` als Soll-Regel: ein Basisraster, `Q12M-PostY5` als Anschluss, Q6-8W nur zusätzlich und nur bei `curativeRecurrencePotential` = ja.
- Neu: `instruction_de` (Termine in `followUpVisitDate` bzw. `plannedFollowUpAppointment`), `standard_mappings` `CarePlan.activity.detail.scheduled[x] (scheduledTiming).code`; `frequency_pattern` angleichen; `definition_de` unverändert.
- Granularitäts-Issue schließen; Kommentar-Issue nur fortschreiben („(a)/(c) umgesetzt, (b) offen“).
- Stufe 2 nach WG-Rückmeldung: bei Variante (b) Code „individuell festgelegt“, Begründung im Plan-Dokument, Quellenangabe `#wg-de-010`; bei rein hausärztlichen/supportiven Kontakten Kommentar als „über die Termin-Elemente abgedeckt“ schließen, PVS-`capture` in `plannedFollowUpAppointment` vorziehen.
- Versionierung: nicht brechend, nur history-Text 0.1.1, ID v0.1 bleibt; Termin-Elemente bleiben 0.1.0; Schema und Zähler 16/35/61 unverändert, Issue-Zähler „125“ fortschreiben.
- Verworfen: Definition als „Mindestraster“ (im Zweifel Minor-Sprung), harte Muss-Regel für Q6-8W (brechend). Option 3 nicht jetzt, nur bei Bedarf an maschinenlesbaren Soll-Terminen; Entscheidung vor der Erstfreigabe 1.0.

**Umsetzungsschritte**
1. Rückfrage an Nachsorge-WG und Allgemeinmedizin über die Maintainer:in (gemeinte Kontakte, Zeitraum, Variante b).
2. Elementweise Freigabe (AGENTS.md Regel 1); Kardinalität, Phasencodes, Codename und `frequency_pattern` festlegen.
3. `followUpInterval` Stufe 1 umsetzen, inkl. `provenance.verification` und history-Text 0.1.1.
4. `instruction_de` in `followUpVisitDate` und `plannedFollowUpAppointment`; bei Letzterem Issue zur Lücke „stattgefundene hausärztliche Kontakte“.
5. Stufe 2 nur nach Bestätigung von (b): Code `individuell`, `constraints_de`, `evidence.guideline_references` mit allen Pflichtfeldern, ohne Personenbezug.
6. `GLOSSARY.md` §11 nach Rückfrage ergänzen (Gesamtcode, Modifikator, ggf. `individuell`).
7. `validate.py`, `verify-quotes.py`, `build-catalog.py`; Issue-Zähler und neuer audit-log-Abschnitt mit Verweis auf §16.7.
8. Personenbezug im Erhebungsauszug klären (audit-log §16.6 Nr. 18); PR gegen `dev` vor rc.1, abgestimmt mit PR #15/#16.

**Klinisch zu entscheiden**
- „1x wöchentlich oder monatlich“: fachärztliche Nachsorgetermine oder frühe hausärztliche/supportive Kontakte? Zählen telefonische, pflegegeleitete oder PROM-basierte Kontakte?
- „Zu Beginn“: bis zur Erstvorstellung binnen 8 Wochen oder das ganze Jahr 1? Nur Letzteres weicht vom S3-Raster ab.
- Individuelles Raster kennzeichnen (Variante b)? Begründung im Plan-Dokument oder als eigenes codiertes Element?
- Pflicht (1..*) oder optional (0..*)? NSCLC Jahr 3–5: S3 halbjährlich oder Onkopedia jährlich?
- Modifikator 6–8 Wochen behalten (nur Onkopedia NSCLC Kap. 8.1 belegt)? KFE-RL § 38 Abs. 3 nach fünf Jahren (Anzeigetext `Q12M-PostY5`)?
- Stattgefundene hausärztliche Kontakte als Serie erfassen? Braucht der Use Case maschinenlesbare Soll-Termine (nur dann Option 3)?

### 2 Komplikation der auslösenden Therapie zuordnen (`postTherapyComplication` / `treatmentSideEffectOrComplication`)

GitHub-Issue: [#29](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/29)

**Kommentar der Nachsorge-WG** zu `postTherapyComplication`: „Für Hausarzt sehr allgemein. Komplikation zuordnen zu Operation/Chemo/Strahlentherapie. Wenn das überhaupt möglich ist. Patient kommt mit Beratungsanlass Müdigkeit.“ (Erhebungsmappe Zeile DE-011, Spalte „Anmerkungen/Beziehungen“; audit-log §16.7)

**Ausgangslage im Katalog**
- `postTherapyComplication` (followup, ID v0.1, 0.1.1 unveröffentlicht): auf lokal-ablative Therapie begrenzt; CodeableConcept 0..*, extensible, 8 Codings, Ursache nur in Strahlen-Codes; kein Code für OP- oder Systemtherapie-Folgen; ohne instruction_de, value_set.notes, standard_mappings.
- `treatmentSideEffectOrComplication` (primarycare, 0.1.0, unveröffentlicht): Condition (MII KDS Diagnose, ohne path); Modalität nur in 18846006, J70.0, T66; Onkolog:in nur kis/read.
- `reasonForEncounter` (0.1.0, 1..*): verlangt Zusammenhangsprüfung, hat aber kein Ergebnisfeld.
- `cancerTreatmentHistory`/`curativeTreatmentModality` führen die TermServ-geprüften Modalitätscodes; ConceptMap ohne direktes Ziel für 870387009, 1345242003 und 703423002.
- `adverseEventCtcaeGrade` nennt AdverseEvent.suspectEntity (1..*); kein Element liefert die auslösende Therapie.
- Asymmetrisch: `firstFollowUpVisitDate` hasPart `postTherapyComplication` ohne isPartOf; `treatmentSideEffectOrComplication` generalizes `adverseEventCtcae` ohne specializes.

**Optionen**

| Option | Kern | Versionierung (howto §C) | Pro | Contra |
|---|---|---|---|---|
| 1 – Nur Patches | Hinweise, notes, Mappings; Ursache über Codes bzw. Y57.98!/Y84.9! | nicht brechend; vor Tag v0.2.0-rc.1 0.1.1/0.1.0, danach 0.1.2/0.1.1; 112 | minimal, Kodierroutine | trennt weder OP/RT noch Chemo/ICI; „nicht zuordenbar“ fehlt |
| 2 – Teilelement + Patches aus 1 (empfohlen) | CodeableConcept 0..*, isPartOf beider Elemente, Wert „nicht zuordenbar“ | neu 0.1.0; Eltern Patch; IDs bleiben; 113 | setzt Kommentar direkt um; passt zu S3, oBDS, suspectEntity | Modalität ≠ Therapieepisode; „nicht zuordenbar“ geht in FHIR verloren |
| 3 – Bewertung am Beratungsanlass | Teilelement an `reasonForEncounter` (HL7-Kausalität) | neu 0.1.0; übrige Patch; 113 | hausärztliche Frage | Kernwunsch nur in Klinik; kein nationales FHIR-Ziel |

**Empfehlung**
- Option 2 inkl. Patches aus Option 1; Option 3 zunächst nicht; Sicherheitsgrad geht ans klinische Review. Aufteilung nach Modalität verworfen (brechend, scheitert an multimodalen/unsicheren Fällen, droht Dublette mit `adverseEventCtcae`).
- Neu `mihub.lung.primarycare.complicationCausativeTreatment.v0.1` „Zugeordnete auslösende Tumortherapie“ (Name, Phase, category zu bestätigen): CodeableConcept 0..*, extensible; Variante Reference auf `cancerTreatmentHistory` offen.
- Codings 119746007, 1287742003, 703423002, 367336001, 870387009, 1255831008 + „nicht zuordenbar“ (Kandidat 261665006 bzw. HL7 Unassessable-Unclassifiable, zu prüfen).
- constraints_de: im Kontext `postTherapyComplication` Systemtherapie nur als Komponente lokal-ablativer Therapie. instruction_de: nur begründbar zuordnen; Vorschlag statt Automatik; „nicht zuordenbar“ ≠ leer; Müdigkeit → `reasonForEncounter`.
- Mappings: condition-dueTo (nicht für Arzneimittelfolgen), suspectEntity.instance (MedDRA, Grad required), Procedure.complication (UNSICHER), oBDS.
- Eltern: +hasPart, instruction_de (Sekundärkode nur am Primärkode), value_set.notes nach Ursache, Mappings, issues; `reasonForEncounter`: instruction_de, Mapping-notes zu reasonReference/diagnosis (UNSICHER).
- Vor dem Tag: neu 0.1.0, `postTherapyComplication` 0.1.1, `treatmentSideEffectOrComplication`/`reasonForEncounter` 0.1.0, ggf. `adverseEventCtcae`/`immuneRelatedAdverseEvent` 0.1.1; danach nächster Patch. IDs bleiben, solange die Definition von `postTherapyComplication` weder verengt noch so geändert wird, dass bereits erfasste Werte umgedeutet würden (sonst 0.2.0/v0.2); hasPart als Patch ist Auslegung.
- Zähler 112 → 113 (primarycare 38 → 39), neu ermitteln; nur nach datenelementweiser Freigabe.

**Umsetzungsschritte**
1. Klinische Grundsatzfragen klären; Zeitpunkt vor/nach Tag v0.2.0-rc.1 festlegen.
2. Datenelementweise Freigabe; Name, Phase, category, Datentyp festlegen.
3. Dublettenprüfung gegen `cancerTreatmentHistory`, `curativeTreatmentModality`, `adverseEventCtcae`, `immuneRelatedAdverseEvent`.
4. TermServ („nicht zuordenbar“, optional fünf Kandidaten aus issues[0]); UNSICHER-Punkte prüfen (Procedure.complication, dueTo in MII/ISiK/KBV, reasonReference, oBDS-Spätfolgen, Strahlentherapie unter Y84.9!).
5. YAML nach Template (Kurzzitate, aus der Mappe nur Kommentartext, verify-quotes.py); Eltern patchen.
6. validate.py, build-catalog.py, build-elicitation-workbook.py, optional FHIR.
7. Zähler (Stand PR #16) und offene Punkte nachziehen; GLOSSARY.md per Rückfrage.
8. Audit-Log-Nachtrag mit Verweis auf §16.7; Gegenrichtungs-Regel getrennt vorlegen; Doku-Konsistenz prüfen.

**Klinisch zu entscheiden**
- Erfasst die Hausarztpraxis selbst (PVS capture) oder liest sie die Klinik-Zuordnung (KIS capture, PVS read)?
- Granularität (OP/RT/systemisch/nicht zuordenbar oder systemisch aufgeteilt)? Mehrfachzuordnung, z. B. Pneumonitis nach Radiochemotherapie mit Durvalumab-Konsolidierung? 205237003/709073001 ohne Ursache belassen?
- Sicherheitsgrad nötig? „Nicht zuordenbar“ als eigener Wert? Vorschlag bei nur einer Modalität vertretbar?
- Fatigue nur Beratungsanlass (R53.9/R53.1) oder auch Komplikation? Modalität oder Therapieepisode?
- Folgen alleiniger Systemtherapie unter `postTherapyComplication` (brechend)? Abgrenzung zu `immuneRelatedAdverseEvent`/`adverseEventCtcae`?
- Gegenüberstellung Therapie ↔ Spätfolgen im Survivorship Care Plan (LoTeCaS-GP)?

### 3 Datenerhebung in der Sterbephase: Grundsatz in der Methodik und Erhebungsregel je Palliativ-Element (Katalogkonvention ohne Schemaänderung)

GitHub-Issue: [#30](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/30)

**Kommentar der Nachsorge-WG** (2026-06-12): „Wie letztens diskutiert. Datenerhebung vs. Respekt vor dem Sterbenden“. Laut Erhebungsauszug (Anker wg-de-047) gilt er dem Abschnitt Palliativversorgung (gesamt); notiert ist er in Zeile DE-047 (`advanceCarePlanning`).

**Ausgangslage im Katalog**
- `dyingPhaseDiagnosed` (0.1.1, ID v0.1): boolean 0..1, SNOMED CT 399069006, Re-Evaluation ≤ 72 h; ohne `instruction_de`/`standard_mappings`; offene Punkte: Konsistenz mit `illnessPhase`, WG-Kommentar.
- `illnessPhase` (0.1.1, 1..1): „per-encounter (täglich in Sterbephase)“ meint laut GLOSSARY §11 die Überprüfung des Betreuungsplans (deckt sich mit LL-Wortlaut), keinen Erhebungstakt.
- 10 von 20 Palliativ-Elementen „per-encounter“, Angehörigen-Scores „weekly“: Die Phasenübersicht zeigt HADS, PHQ-9, QoL bis zum Tod; dazu Portal/PROM (`qualityOfLifeScore`, `patientReportedSymptomWeb`, `qolEortcQlqC30`).
- Methodik §4.2/§6.2 regeln nicht, ob erhoben wird; §6.4 ist frei. `constraints_de`/`instruction_de` erscheinen nur im FHIR Logical Model.
- Katalog v0.1.0-rc.2, 0.2.0-rc.1 in Vorbereitung; Palliativ 13× 0.1.1, 5× 0.2.0, 2× 0.1.0.
- Leitlinie zieht in beide Richtungen: weniger erheben (Empf. 21.26, 21.29, 21.30), weiter dokumentieren (21.4, 21.6, 21.8; QI 4/5 vorläufig).

**Optionen**

| Option | Kern | Versionierung (howto §C) | Pro | Contra |
|---|---|---|---|---|
| 1 Schlanker Einstieg | Grundsatz in Methodik §6.4; nur `dyingPhaseDiagnosed`, `illnessPhase`, Glossar | Patch, IDs bleiben | geringster Aufwand, sofort in 0.2.0-rc.1 | Phasenübersicht widerspricht Grundsatz; PROM-Erinnerungen nicht ausdrücklich gestoppt |
| **2 Regel je Element (empfohlen)** | Zusatz „; Sterbephase: …“ (vier Regeln) in frequency_pattern; Hinweise in constraints_de/instruction_de | Patch, IDs bleiben | in Phasenübersicht ablesbar; leitlinienkonform beidseitig | 20–25 Einzelzustimmungen; Freitext unvalidiert; klinischer Konsens nötig |
| 3 Schemafeld (später) | `care_process.conditions[]` (when/kind/rule) | Elemente Patch; Schema Minor, braucht Versionsnummer | CI-prüfbar; deckt auch `brainMriHighRisk`/PCI | größter Eingriff; inhaltlich nichts Neues, verfrüht |

**Empfehlung**
- Option 2 in drei Stufen, Option 1 ist Stufe 1. Option 3 erst bei maschinellem Bedarf in KIS-/PVS-Formularen, nach Schema-Versionsnummer.
- Methodik §6.4: Auslöser `dyingPhaseDiagnosed` = true mit Zeitpunkt; nur dokumentieren, was der Versorgung dient (21.26, 21.29); keine Befragung allein für Dokumentation/QS/Forschung (Expert:innen-Festlegung); Entscheidungen weiter dokumentieren (21.4), Symptome per Fremdeinschätzung (21.6, 21.8).
- Kein Feld „nicht erhoben“: Fehlende Werte ausgesetzter Elemente nach Feststellung gelten als bewusst nicht erhoben; `dataAbsentReason = not-performed` nur automatisch.
- GLOSSARY §11: `Sterbephase: fortführen | bei Änderung | anlassbezogen | ausgesetzt`; „täglich in Sterbephase“ umformulieren.
- Stufe 1 (möglichst vor 0.2.0-rc.1): `dyingPhaseDiagnosed` (instruction_de, fhir-r4-base mit effective[x], Zitate 21.4/21.26); `illnessPhase` („Sterbephase: bei Änderung“); `treatmentDecisionDocumentation` (tägliche Überprüfung Betreuungsplan); `symptomAssessmentInstrument` (Fremdeinschätzung, IPOS-Staff 718967002/718971004 erst nach $lookup).
- Stufe 2 (übrige 16, Entwurf): ausgesetzt u. a. `anxietyHadsScore`, `phq9DepressionScore`, `qualityOfLifeScore` (inkl. Portal-Erinnerungen); anlassbezogen u. a. `painIntensityNrs`, `dyspneaIntensityNrs`, `wishToDie`; an bestehende issues anknüpfen.
- Stufe 3 (optional): `patientReportedSymptomWeb`, `qolEortcQlqC30`, `bodyMassIndex` aussetzen, `ecogPerformanceStatus` angleichen, `weightChangePercent` klinisch entscheiden; `plannedFollowUpAppointment` bleibt (Hausbesuche laufen weiter).
- Versionierung: Patch, IDs und Schema unverändert; vor dem Release ohne neue Nummer (history[].change + verification-Eintrag), danach Patch je Element (z. B. 0.1.1→0.1.2). Brechend, daher ausgeschlossen: Datentyp `dyingPhaseDiagnosed`, Definition `painIntensityNrs`, „nicht erhoben“ in integer-Elementen.

**Umsetzungsschritte**
1. Vor jeder Änderung klinische Klärung mit Nachsorge-WG, Allgemein- und Palliativmedizin.
2. Methodik §6.4 durch die Maintainer:in freigeben lassen; GLOSSARY §11 nach Rückfrage anpassen.
3. Stufe 1 datenelementweise freigeben; IPOS-Codes vorher per `verify-terminology.py` bestätigen.
4. Fundstellen der Langversion 3.0 ermitteln (UNSICHER/zu prüfen), per `verify-quotes.py` prüfen.
5. Stufe 2 und 3 nach klinischer Bestätigung je Element freigeben.
6. Versionierung nachziehen; `validate.py` und `build-catalog.py` laufen lassen.
7. Audit-Log: Folgeeintrag zu §16.7, Zähler offener Punkte (derzeit 125) aktualisieren; Doku-Konsistenz prüfen.
8. Lücken (Fremdeinschätzung Atemnot/Schmerz, Unruhe/Delir, Sterbedatum) erst nach `check-duplicate-data-element` aufnehmen.

**Klinisch zu entscheiden**
- Ergebnis der Diskussion? Regel nur ab Feststellung der Sterbephase oder für die ganze Palliativphase?
- Auslöser `dyingPhaseDiagnosed` = true oder `illnessPhase` = dying? `illnessPhase` 1..1 in PBP/APV realistisch (0..1 wäre nicht brechend)?
- Trägt die WG die Zuordnung je Element und die Übertragung von 21.30 auf Scores, PROMs, BMI, Gewicht als Expert:innen-Festlegung?
- `wishToDie`: weiter aktiv fragen (Empf. 20.3)? Angehörigen-Erhebung anlassbezogen oder aussetzen?
- IPOS-Personalversion als Standard? Eigene Elemente für Fremdeinschätzung von Atemnot, Schmerz, Unruhe/Delir?
- Wie erreicht die Feststellung Portal, PROM-Plattform und Hausarztpraxis? Genügt für Sekundärnutzung die Auswertungsregel (Datenschutz/Ethik)?

### 4 Rezidiv und Zweitkarzinom trennen, Lokalisation erfassen (`recurrenceOrSecondPrimary`)

GitHub-Issue: [#31](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/31)

**Kommentar der Nachsorge-WG** (zu DE-014 der WG-Mappe, Word-Fassung der Phasen-Übersicht v0.1; Wortlaut in audit-log §16.7): „Zwei unterschiedliche Dinge. Eher getrennt auflisten. Ebenso ist die Lokalisation relevant“. Status: Entscheidung offen.

**Ausgangslage im Katalog**
- `recurrenceOrSecondPrimary`: 0.1.0 veröffentlicht (v0.1.0-rc.1/-rc.2), 0.1.1 ausstehend; CodeableConcept 0..1, extensible; vereint Lokal-, Regionalrezidiv, Fernmetastasierung und metachrones Zweitkarzinom; keine Lokalisation.
- Codings: SNOMED 1259237005, 314954002, 399409002, 878806005; ICD-10-GM C34.9; KDL SD150103 (Dokumentklasse, kein Befundwert). Mappings: MII Diagnose Primärtumor (nur Zweitkarzinom), MII Verlauf, oBDS 17, KBV-MIO. `issues[0]`: „aufteilen oder Transformationsregeln“.
- Meldewege: Rezidiv = oBDS-Verlaufsmeldung (17.2 Y, 17.3–17.5 R, Menge_FM)/MII Verlauf; Zweitkarzinom = eigene Diagnosemeldung/MII Diagnose Primärtumor.
- Eingehend (0.1.0, unveröffentlicht): `bronchoscopyFollowUp`, `petCtFollowUp`, `curativeRecurrencePotential` (dependsOn), `currentTumorStatus` (generalizes). Alle vier dependsOn-Zyklen laufen über das Element; Semantik offen (audit-log §14.6 Nr. 6).
- Überschneidungen: `ctThoraxFinding` (0.2.0, ausstehend) führt 1259237005, 128462008, 878806005 als radiologische Kategorien; `cancerDiagnosis` (1..*) schließt Zweitkarzinome ein; `tumorLocalisation` nur C34.x, ohne Seite.

**Optionen**

| Option | Kern | Versionierung (howto §C) | Pro | Contra |
|---|---|---|---|---|
| 1 (empfohlen) | `recurrence` (Nachfolger) + `distantMetastasisLocalisation`, `secondPrimaryCancer` (neu) | brechend: 0.1.0 → 0.2.0, ID `…recurrence.v0.2`, uuid bleibt; neue Elemente 0.1.0; 114 Elemente | Kommentar voll umgesetzt; ein Meldeweg je Element; Zyklen 4 → 0 | 17 v0.2-IDs gegenlesen; §C-Zusatz nötig; neue Elemente ohne Zweitprüfung |
| 2 | wie 1, alle neu; Altelement `Superseded` | Altelement 0.1.1/v0.1 (Statuswechsel als Patch: UNSICHER); 115 Elemente; vorgezogener Major-Weg | alte ID im Katalog auflösbar | uneinheitlich zu den 16 v0.2-Elementen; Tooling-Änderungen nötig |
| 3 (Übergang) | ein Element, zwei Wertegruppen, Transformationsregeln, Teilelement Lokalisation | nicht brechend (0.1.1); 113 Elemente; Aufteilung später 0.3.0 | geringster Eingriff | Kommentar nur formal erfüllt; Mischmodell und Zyklen bleiben |

**Empfehlung**
- Option 1, vor dem Tag v0.2.0-rc.1.
- (a) `recurrence`: 0.1.0 → 0.2.0, ID `mihub.lung.followup.recurrence.v0.2`, uuid bleibt, `history[0].id` = alte ID, 0.1.1 geht in 0.2.0 auf; nur nach vorheriger Tumorfreiheit; 0..*; lokal 314954002, regionär (Code offen, UNSICHER), fern 399409002, o. n. A. 1259237005; entfernt 878806005, C34.9, SD150103; MII Verlauf/oBDS 17 mit 17.2 = Y; KBV-MIO gestrichen.
- (b) `distantMetastasisLocalisation` (0.1.0, isPartOf `recurrence`): 0..*, 12 oBDS-Lokalisationen nach MII-Mappingtabelle (Hinweis bei MAR 14016003, GEN 405843009); 385421009 nur in notes/Mapping, nach FSN-Prüfung; `mii-pr-onko-fernmetastasen` (Ressourcentyp, Bindung, Pfade UNSICHER/zu prüfen) bzw. oBDS Menge_FM.
- (c) `secondPrimaryCancer` (0.1.0): 0..*, ICD-10-GM ohne C77–C79; MII Diagnose Primärtumor, oBDS 5 inkl. 5.9; specializes `cancerDiagnosis`, hasPart `tumorHistology` (`tumorLocalisation` klinisch offen).
- Befüllen erst nach Tumorboard bzw. Histologie; radiologische Einordnung bleibt in `ctThoraxFinding`/`brainMriFinding` (Klarstellung im ausstehenden 0.2.0).
- dependsOn = „Datengrundlage“: `bronchoscopyFollowUp[0]`, `petCtFollowUp[0]`/`[1]`, `ctAbdomenFollowUp[0]` entfernen (Auslöser in `care_process.trigger`); `curativeRecurrencePotential` → `recurrence` + `secondPrimaryCancer`; `currentTumorStatus` generalizes nur `recurrence`. Ergebnis: 0 statt 4 Zyklen (reine Umstellung: 7).
- Zähler: 114 Elemente (Nachsorge 36), 17 × 0.2.0, 34 × 0.1.1, 63 × 0.1.0; Verweiser bleiben 0.1.0.
- Option 2, falls die alte ID auflösbar bleiben soll (Tooling-Änderungen nötig); Option 3 nur als Übergang, wenn vor dem Tag keine ID-Änderung mehr möglich ist.

**Umsetzungsschritte**
1. Freigaben: Option, Namen, §C-Zusatz, dependsOn-Semantik; klinische Fragen mit Nachsorge-WG/Allgemeinmedizin klären; ohne datenelementweise Freigabe keine Änderung.
2. Dublettenprüfung der drei Kandidaten (`check-duplicate-data-element`).
3. howto §C ergänzen (Aufteilung, Umbenennung, uuid).
4. `recurrence` überführen, zwei neue Elemente nach Template anlegen.
5. Verweise anpassen; Zyklenfreiheit ad hoc prüfen (`validate.py` prüft keine Zyklen).
6. Terminologie am MII TermServ, Profile (2026.0.3), Zitate, `validate.py`, `build-catalog.py`; alte FSH-Instanz mit Freigabe löschen, FHIR neu erzeugen.
7. Doku: audit-log, Release-Notes, README, AGENTS, methodology, GLOSSARY; fehlende Review-Datei aus §16.7 anlegen.
8. Merge mit dem Screening-PR abstimmen (§16.6 Nr. 19); Doku-Konsistenz prüfen.

**Klinisch zu entscheiden**
- Zwei Elemente (Option 1/2) oder getrennte Einträge in einem Element (Option 3)?
- Erfassung erst nach Tumorboard/Histologie oder eigener Zustand „neuer Herd, Zuordnung offen“?
- Reicht Rezidivart plus oBDS-Organ (PUL … GEN), oder feiner (Bronchusstumpf, ipsi-/kontralateral, LK-Station)? GEN nötig? Zweitkarzinom extrapulmonal: ICD-O-3-Topographie/Seite, D00–D09, `tumorLocalisation` erweitern?
- Rezidiv nur nach kompletter Tumorfreiheit (17.2 = Y)? Lokalisation neuer Fernmetastasen auch ohne diese (17.5 R/P)?
- Tumorboard: Kriterien zur Abgrenzung Zweitkarzinom vs. intrapulmonale Metastase (Histologie, IASLC; Onkopedia SCLC 6.1.2.1)? Davon hängt der Meldeweg ab.
- Allgemeinmedizin: `secondPrimaryCancer` in primarycare sichtbar oder genügt `cancerDiagnosis`? Feststellungsdatum als eigene Angabe?

### 5 Pflegegrad nach SGB XI: eigenes Element `careGrade`

GitHub-Issue: [#32](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway-data-elements/issues/32)

**Kommentar der Nachsorge-WG** (kommentierte Word-Fassung der Phasen-Übersicht v0.1 vom 2026-06-12, Absatz „Weitere Aspekte“): „Pflegebedarf/-stufe/-grad“ (laut Auftrag) bzw. „Pflegebedarf/-grad“ (Audit-Log §16.7); Wortlaut am Original zu prüfen. Kein Treffer im Erhebungsauszug, daher derzeit nicht per verify-quotes prüfbar.

**Ausgangslage im Katalog**
- `socialSituation` (0.1.0/v0.1, AuthorDraft, in keinem Release): Pflegegrad nur unspezifisch (301887005, Z74.9) oder als Text erfassbar; Value Set extensible/mapped; offene issues: Gliederung nach Rolle, Aufteilung in Teil-Elemente.
- `ongoingSupportiveServices` (Pflegedienst, SNOMED 90817005, auch ohne Pflegegrad möglich) ersetzt die Angabe nicht; `rehabilitationAndSocialCounselling` ist Beratung, kein Status.
- Kein Treffer für „Pflegegrad“, „Pflegestufe“, „9-984“, „80391“ (außer §16.7). Dubletten-Check: EIGENSTÄNDIG.
- Zähler: 112 Elemente (38 primarycare), 434 Codings (18 OPS), 339 Zitate, 125 offene issues.
- HL7-DE-Basisprofil `observation-de-pflegegrad` 1.6.0: LOINC 80391-6 (TRIAL), Wert OPS 9-984.6–.b, required; KBV Basis 1.10.0 leitet ab (value.coding max 1).
- KBV-MIO Überleitungsbogen 1.0.0: Core-Observation (kein Ableger des Basisprofils), OPS 9-984.6–.a (Version 2021), Antrag über Extension `beantragungsstatus`.

**Optionen**

| Option | Kern | Versionierung (howto §C) | Pro | Contra |
| --- | --- | --- | --- | --- |
| **1 – `careGrade` neu** (empfohlen) | eigenes Element, required an `pflegegrad-de`, vor Tag v0.2.0-rc.1 | `careGrade` 0.1.0/v0.1; `socialSituation` bleibt 0.1.0/v0.1 (nur history) | nationaler Standard; auswertbar; „Antrag gestellt“ sichtbar | 113 Elemente, Zähler/Doku; nicht zweitgeprüft |
| **2 – gestuft** | jetzt issue in `socialSituation`, `careGrade` im nächsten Release | jetzt 0.1.0 (nur history); später `socialSituation` Patch 0.1.1 | Release fast unberührt; kein ungeprüfter Code | bis dahin nicht auswertbar; zwei Schritte |
| **3 – Teilaspekt** (nicht empfohlen) | +6 OPS-Codes in `socialSituation` | spätere Herauslösung voraussichtlich brechend (v0.2) | kein neues Element | verschärft offene issues; required nicht erfüllbar |

**Empfehlung**
- Option 1, möglichst vor dem Tag: `mihub.lung.primarycare.careGrade.v0.1` „Pflegegrad (SGB XI)“; Name (`careGrade`/`careLevel`) wählt die Maintainer:in.
- CodeableConcept 0..*, category sozialanamnese; required an `http://fhir.de/ValueSet/pflegegrad-de`; codings nur OPS 9-984.6–.b; LOINC 80391-6 nur im Mapping und in value_set.notes.
- constraints_de: höchstens ein Pflegegrad je Gültigkeitszeitraum; 9-984.b allein bei Erstantrag, bei Höherstufung als zusätzlicher Eintrag; keine Punktgrenzen, Begutachtungsdetails, „Pflegestufe“; Abgrenzung zu `socialSituation`, `ongoingSupportiveServices`, `rehabilitationAndSocialCounselling`, `caregiverBurden`, `functionalStatus`, ECOG.
- Mappings: other → Basisprofil und KBV Basis; kbv-mio → ULB mit Regel 9-984.b → beantragungsstatus; fhir-r4-base Observation.
- frequency_pattern ad-hoc (Anamnese, Entlassung, Bescheid/Antrag, Progression, Palliativ-Übergang). Evidence: rollenbezogener Word-Auszug, § 15 SGB XI; S3-LL 16.1/16.2 nur optional, indirekt. „Kein Pflegegrad/abgelehnt/unbekannt“ zunächst als issue.
- `careGrade` isPartOf `socialSituation` (dort hasPart; Definition verweist auf `careGrade`, kein Ausschluss). Kein neues dependsOn.
- Versionierung: `careGrade` 0.1.0/v0.1; `socialSituation` bleibt 0.1.0/v0.1; keine neuen IDs, kein Schema-Bump. required bewusst jetzt: späteres Verschärfen wäre brechend (v0.2), Lockern auf extensible regelt howto §C nicht ausdrücklich.
- Zähler: Elemente 112 → 113, Codings 434 → 440 (nach TermServ-Lauf), Zitate 339 → 341 bzw. 342, offene Punkte 125 → 127. Rückfallebene ohne Votum vor dem Tag: Option 2 (125 → 126). UNSICHER/zu prüfen u. a.: OPS 2027, Canonical `pflegegrad-de`; TermServ-Prüfung steht aus.

**Umsetzungsschritte**
1. Datenelementweise Freigabe durch die Maintainer:in (inkl. Name, Zeitpunkt); klinisches Review (Nachsorge-WG, Allgemeinmedizin).
2. Wortlaut am Original prüfen; neuen rollenbezogenen Auszug ohne Namen anlegen (bestehender ist unveränderlich); Quellen-JSON für verify-quotes ergänzen.
3. `careGrade` aus dem Template anlegen (neue uuid, AuthorDraft); in provenance: keine Zweitprüfung, kein Mapping-Audit.
4. `socialSituation`: Verweis in definition_de, +hasPart, Zusatz im issue, Ergänzung in history.
5. Prüfen: check-duplicates, validate, verify-terminology (MII TermServ, mTLS; OPS 2026/2027), LOINC $lookup, verify-quotes.
6. Glossar per Rückfrage ergänzen; Katalog und Sichten neu erzeugen.
7. Audit-Log (neuer Unterabschnitt, z. B. §16.8; Kollision mit PR #16 prüfen); Zähler in README, AGENTS, Methodik, Release-Notizen; datierte Verlaufszeilen nicht umschreiben.
8. Issue und PR gegen dev legt die Maintainer:in an; keine git-Operationen durch Agenten.

**Klinisch zu entscheiden**
- Eigene Angabe (Option 1) oder vorerst soziale Situation (Option 2)? Votum vor dem Tag möglich?
- Bestätigt die WG den Wortlaut? Meint „Pflegebedarf“ mehr als den informellen Unterstützungsbedarf in `socialSituation`?
- Muss „kein Pflegegrad/abgelehnt/unbekannt“ von „nicht erfragt“ unterscheidbar sein? Dann ULB-Antragsstatus, Bindung extensible.
- Reicht 9-984.b für Erst- und Höherstufung, oder braucht die Palliativsituation (Eilbegutachtung) eine eigene Kennzeichnung? Gültig-ab- bzw. Antragsdatum erhebbar?
- Wer erfasst/liest (Hausarztpraxis, Sozialdienst, Nachsorge-Klinik)? Genügt primarycare? Prüfanlässe und Relation zu `rehabilitationAndSocialCounselling`?
- Indirekter S3-LL-Bezug als Beleg? Schwerbehinderung (GdB/Merkzeichen) mitbetrachten (nicht angefragt, MII-Profil nicht nachgeprüft)?
