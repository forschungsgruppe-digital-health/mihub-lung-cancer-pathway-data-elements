# Aktualitätsprüfung der Primärquellen, Abgleich und Repo-Review — 2026-11-25

> **Momentaufnahme (datiert, unveränderlich).** Auftrag der Maintainer:in: Aktualität der Primärquellen
> (z. B. S3-Leitlinien) prüfen, neue Fassungen aufnehmen und die Datenelemente damit abgleichen; passende
> Codes über den MII TermServ vorschlagen; danach das gesamte Repo auf Vollständigkeit, Konsistenz,
> Korrektheit und Verständlichkeit prüfen, aufräumen und offene Punkte zusammenstellen.
> **KI-Unterstützung:** Claude Code (Opus 5.5) mit Read-only-Recherche- und Prüfagenten. Jede inhaltliche
> Element-Änderung wurde von der Maintainer:in datenelementweise freigegeben (AGENTS.md Regel 1).
> Audit-Eintrag: [`docs/audit-log.md`](../audit-log.md) §16.

## 1 Ergebnis in Kürze

- **Klinische Primärquellen:** alle Pins aktuell. Keine neue Fassung der S3-LL Lungenkarzinom (5.1), der
  S3-LL Palliativmedizin (3.0), der S3-LL Psychoonkologie (2.1), von Onkopedia NSCLC (April 2025), SCLC
  (August 2026) und „Impfungen“ (Mai 2026) oder des OCP Lung (2nd ed., Update 07/2025). Die S3-LL Rauchen und
  Tabakabhängigkeit (2021, gültig bis 31.12.2025) hat weiterhin keine Nachfolgefassung.
- **Standards:** neu ist der **oBDS 3.1.0** (XML-Schema vom 14.10.2026; Annahme durch die Landeskrebsregister
  geplant ab 01.04.2027). Er ergänzt abwärtskompatibel ICD-O-4, TNM-9-Werte und CTCAE 6.0. Die 17
  oBDS-Mappings sind abgeglichen.
- **Neue Quellen (freigegeben):** S3-LL Supportive Therapie 2.1 (Juni 2026), G-BA Krebsfrüherkennungs-Richtlinie
  (LDCT-Screening, GKV-Leistung seit April 2026) und STIKO-Empfehlungen 2026. Sie sind in 9 Elementen
  eingearbeitet, mit 11 wörtlichen, maschinell gegen die Quelltexte geprüften Zitaten.
- **Terminologie:** Die 434 Codings ergeben 338 OK, 31 lokal und 65 nicht verifizierbar. Kein Code ist
  unbekannt oder inaktiv. **Neu:** Die KDL ist auf dem MII TermServ nicht mehr abrufbar; ihre 58 Codings sind
  daher derzeit nicht verifizierbar (am 2026-10-15 noch OK). Alle SNOMED-Codes sind auch in der neuen SNOMED CT
  Germany Edition 20261115 aktiv. Vier Codes kamen dazu.
- **Repo-Review:** 28 Elemente geändert. 86 Doku-Stellen in 19 Dateien korrigiert (u. a. falsche Setup-Befehle,
  widersprüchliche Verifikationsaussagen, veraltete Pins, ein falscher LOINC-Beispielcode im Issue-Formular).
  Neu sind ein Issue-Formular für Rückmeldungen zu bestehenden Elementen, Schnellstart- und Reifegrad-Hinweise
  im README, eine Lesehilfe im Glossar (§21) und ein CI-Drift-Check über alle generierten Sichten.

## 2 Aktualität der Quellen (Stand 2026-11-25)

| Quelle | Pin im Katalog | Befund 2026-11-25 | Geprüft über |
| --- | --- | --- | --- |
| S3-LL Lungenkarzinom (AWMF 020-007OL) | 5.1 (Juli 2026) | aktuell; Download „Langversion_5.1“, Archiv nennt 5.0 (Juni 2026) | leitlinienprogramm-onkologie.de/leitlinien/lungenkarzinom |
| S3-LL Palliativmedizin (AWMF 128-001OL) | 3.0 (Juli 2026) | aktuell | leitlinienprogramm-onkologie.de/leitlinien/palliativmedizin |
| S3-LL Psychoonkologie (AWMF 032-051OL) | 2.1 (August 2023) | aktuell | leitlinienprogramm-onkologie.de/leitlinien/psychoonkologie |
| S3-LL Rauchen und Tabakabhängigkeit (AWMF 076-006) | 3.1 (2021) | keine neue Fassung gefunden; Gültigkeit abgelaufen, Aktualisierung angemeldet | leitlinienwatch.de, dg-sucht.de, Websuche (AWMF-Register wegen Bot-Schutz nicht direkt abgefragt) |
| Onkopedia NSCLC | Stand April 2025 | aktuell („aktuell gültige Version“); Tab. 12 unverändert (Monate 3/6/12/18/24/36/48/60) | onkopedia.com (HTML-Fassung) |
| Onkopedia SCLC | Stand August 2026 | aktuell; Änderungen ggü. 09/2025 nur Therapie (Tarlatamab, Lurbinectedin); Tab. 9 unverändert | onkopedia.com |
| Onkopedia „Impfungen bei malignen Erkrankungen …“ | Stand Mai 2026 | aktuell; Tab. 5 (solide Tumoren) wie zitiert | onkopedia.com |
| OCP Lung (Cancer Council Victoria) | 2nd ed. 2021, Update 07/2025 | keine neuere Fassung gefunden | cancer.org.au, Websuche |
| EORTC QLQ-C30 Scoring Manual, Klein et al. 2026, AG LONKO 2021 | — | unveränderliche Publikationen | — |
| oBDS | XSD 3.0.5 | **neu: XSD 3.1.0 (14.10.2026)**, siehe §4 | basisdatensatz.de/xml, plattform65c.de |
| MII KDS Onkologie | 2026.0.3 / 2027.0.0-ballot.1 | unverändert (kein 2027-Release) | simplifier.net |
| MII KDS Lungenfunktion | 2027.0.0-ballot | weiterhin nur Ballot | simplifier.net |
| gematik ISiK | 6.0.0 | aktuell | simplifier.net |
| HL7 mCODE STU4, Genomics Reporting STU3 | 4.0.0 / 3.0.0 | **nicht verifiziert** (Versionshistorie ohne Inhalt abrufbar) | hl7.org |
| KBV MIO Patientenkurzakte 1.0.0, Impfpass 1.1.0 | — | **nicht verifiziert** (mio.kbv.de-Seiten nicht abrufbar) | mio.kbv.de |
| NCI CTCAE | v5.0/v6.0 | v6.0 (22.07.2025) bereits referenziert; Ressourcen jetzt unter dctd.cancer.gov | dctd.cancer.gov |
| ICD-10-GM / OPS / ATC | 2026 | ICD-10-GM 2026 gilt laut BfArM voraussichtlich bis Ende 2028 (dreijähriger Turnus); OPS 2027 als Online-Fassung veröffentlicht, noch nicht auf dem MII TermServ; ATC 2026 aktuell | bfarm.de |
| SNOMED CT / LOINC | 20260701 / 2.83 | aktuell; zusätzlich Germany Edition 20261115 auf dem MII TermServ | MII TermServ |

## 3 Neue Quellen und Abgleich der Elemente

Freigabe der Maintainer:in: Quellen aufnehmen; je Element einzeln bestätigt.

| Quelle | Inhalt (geprüfte Fundstellen) | Elemente |
| --- | --- | --- |
| **S3-LL Supportive Therapie bei onkologischen PatientInnen 2.1** (Juni 2026, AWMF 032-054OL; neu in Version 2: Kap. 13 irAE, Kap. 14 Kardiotoxizität) | Empf. 13.2 (EK: Aufklärung über irAE, die auch nach Ende der ICI-Therapie auftreten können), 13.3 (B/LoE 5, Tab. 99: Labor vor jeder Verabreichung, TSH/fT4 vor jeder 2.), 13.11 (B/LoE 4: Diagnostik bei Verdacht), 13.12 (EK: ab Grad 2 interdisziplinär), Kap. 13.1.2.2 (Schweregrad nach CTCAE), Kap. 11.11 (radiogene Pneumonitis) | `immuneRelatedAdverseEvent` (Quellen, Definition und Auslöser erweitert, 3 Codes), `adverseEventCtcae`, `adverseEventCtcaeGrade`, `treatmentSideEffectOrComplication`, `laboratoryPanelSurveillance` (+ offener Punkt), `postTherapyComplication` |
| **G-BA Krebsfrüherkennungs-Richtlinie (KFE-RL)**, zuletzt geändert 18.12.2025, in Kraft 12.03.2026; Lungenkrebsfrüherkennung: Beschluss 18.06.2025, in Kraft 05.09.2025 | Abschnitt D III, § 38: Anspruch für 50- bis 75-Jährige mit Zigarettenkonsum nach LuKrFrühErkV, grundsätzlich alle 12 Monate (Abs. 1); eine CT aus anderem Grund innerhalb von 12 Monaten verschiebt den Anspruch (Abs. 2); Versicherte „in ärztlicher Behandlung oder Nachbehandlung“ wegen Lungenkrebs werden kurativ versorgt (Abs. 3) | `screeningProgramEnrolment` (Quelle + offener Punkt), `followUpInterval` (offener Punkt) |
| **STIKO-Empfehlungen 2026** (Epid Bull 4/2026, 22.01.2026); GKV-Umsetzung über die Schutzimpfungs-Richtlinie (zuletzt geändert 03.09.2026, in Kraft 29.10.2026) | Tab. 2: Indikationsimpfungen bei malignen Erkrankungen bzw. Immundefizienz (Pneumokokken PCV20, COVID-19, Herpes zoster ab 18 J.); RSV für 60- bis 74-Jährige mit schwerer Grunderkrankung (u. a. hämato-onkologisch); Kap. 4.9 Impfen bei Immundefizienz | `immunizationStatus` (Quelle, RSV in Definition, offene Punkte zusammengeführt) |

**Befund mit Klärungsbedarf:** KFE-RL § 38 Abs. 3 steht in Spannung zu S3-LL Lungenkarzinom Empf. 16.7
(„nach 5 Jahren in ein Screeningprogramm eingeschlossen werden“). Offen ist, ob Patient:innen nach der
fünfjährigen Nachsorge noch als „in Nachbehandlung“ gelten. Als offener Punkt in `screeningProgramEnrolment`
und `followUpInterval` eingetragen.

Die Quell-PDFs liegen urheberrechtlich nicht im Repo. Die Zitate wurden mit `scripts/verify-quotes.py` gegen
eigene Textfassungen geprüft (`pdftotext`; Schlüssel `andere:Supportive`, `andere:KFE-RL`, `andere:STIKO`):
11/11 gefunden.

## 4 oBDS 3.0.5 → 3.1.0 (XSD-Vergleich)

Beide Schemata (basisdatensatz.de, Stand 22.09.2025 bzw. 14.10.2026) wurden zeilenweise verglichen. Für den
Katalog relevante Änderungen:

| Änderung in 3.1.0 | Betroffene Elemente |
| --- | --- |
| Nebenwirkung/Version (15.3): zusätzlicher Wert `6.0` (CTCAE v6.0) | `adverseEventCtcaeGrade` (Hinweis), `adverseEventCtcae` (offener Punkt) |
| `Morphologie_ICD_O_4` als Alternative zu `Morphologie_ICD_O` in Histologie und Tumorzuordnung (Code-Muster `\d\d\d\d[\dA-Z]/\d`, Version 40 = ICD-O-4 2026, b6 = WHO-Klassifikationen 6. Auflage); Meldung laut Plattform § 65c erst nach abgestimmter deutscher Übersetzung | `tumorHistology` |
| Topographie-Version (5.5): zusätzlicher Wert `40` (ICD-O-4, 2026) | `tumorLocalisation` |
| `TNM_Typ`: neues optionales Feld `LV` (LVX/LV0/LV1), Feld `B` (peripheres Blut) und UICC-Stadium `IB3`; B und IB3 für das Lungenkarzinom nicht einschlägig; TNM-Version 9 seit 3.0.4 | `tnmStage` |
| alle übrigen in den Mappings genannten Felder und XML-Namen | unverändert; Verweis auf XSD 3.1.0 umgestellt (12 weitere Elemente) |

## 5 Terminologie (MII TermServ, mTLS)

| Lauf | Codings | OK | lokal | nicht verifizierbar | nicht gefunden / inaktiv |
| --- | --- | --- | --- | --- | --- |
| 2026-10-15 (Audit-Log §14.5) | 430 | 392 | 31 | 7 (ICF 4, MedDRA 3) | 0 / 0 |
| 2026-11-25 vor den Änderungen | 430 | 334 | 31 | 65 (KDL 58, ICF 4, MedDRA 3) | 0 / 0 |
| 2026-11-25 nach den Änderungen | 434 | 338 | 31 | 65 | 0 / 0 |

- **KDL nicht mehr auf dem Server:** Keines der 169 CodeSystems und kein ValueSet des MII TermServ führt die KDL
  (`http://dvmd.de/fhir/CodeSystem/kdl`); `$lookup` liefert „could not be resolved“. Die KDL-Codings bleiben
  unverändert, Klärung mit dem TermServ-Betrieb bzw. der DVMD steht aus.
- **SNOMED CT Germany Edition 20261115:** Alle 173 SNOMED-Codes des Katalogs sind dort aktiv. 86 der 170
  bisherigen Codes haben eine deutsche Bezeichnung.
- **Übernommene Code-Vorschläge:** `structuredFollowUpPlan` + 736252007 „Cancer care plan“ (einheitlich mit
  `structuredSurveillancePlan`); `immuneRelatedAdverseEvent` + 1360081003 „Immunotherapy induced hypophysitis“,
  72527006 „Myocarditis caused by drug“, 439990003 „Drug-induced tubulointerstitial nephritis“;
  `palliativeCareTier`: Teilentsprechungen 395669003 und 395086005 nur als Hinweis.
- **Erneut geprüft, ohne neues Ergebnis:** Die Suche nach Codes für Distress-Thermometer, Zarit/HPS/CAREPAL,
  MIDOS, Krankheitsphasen, Komplexität, PCI, Therapielinie und Therapiestatus bestätigt die Befunde vom
  2026-10-14. Die neun in offenen Punkten vorgeschlagenen Codes sind weiterhin aktiv.

## 6 Geänderte Elemente (28)

| Element | Änderung |
| --- | --- |
| `immuneRelatedAdverseEvent` | Definition (weitere Organsysteme, „unter oder nach“ ICI), Auslöser, 3 SNOMED-Codes, 3 Quellen (S3 Supportive) |
| `immunizationStatus` | Definition (+ RSV), Quelle STIKO 2026, offene Punkte zusammengeführt |
| `adverseEventCtcae` | Quelle (S3 Supportive), `value_set.uri` → NCI „CTCAE and AE Reporting“, offener Punkt (oBDS 3.1.0) |
| `adverseEventCtcaeGrade` | 2 Quellen (S3 Supportive), `value_set.uri`, oBDS-Hinweis CTCAE 6.0 |
| `screeningProgramEnrolment` | Quelle G-BA KFE-RL § 38, offener Punkt |
| `followUpInterval` | offener Punkt (KFE-RL § 38 Abs. 3) |
| `laboratoryPanelSurveillance` | Quelle (S3 Supportive Empf. 13.3/Tab. 99), offener Punkt |
| `treatmentSideEffectOrComplication`, `postTherapyComplication` | Quelle (S3 Supportive) |
| `structuredFollowUpPlan` | Code 736252007, offener Punkt angepasst |
| `palliativeCareTier` | Hinweis auf SNOMED-Teilentsprechungen |
| `tumorHistology`, `tumorLocalisation`, `tnmStage` | oBDS-3.1.0-Hinweise (ICD-O-4, LV) |
| `brainMriFinding`, `ctThoraxFinding`, `curativeRecurrencePotential`, `curativeTreatmentModality`, `ecogPerformanceStatus`, `prophylacticCranialIrradiationStatus`, `recurrenceOrSecondPrimary`, `cancerDiagnosis`, `cancerTreatmentHistory`, `currentTumorStatus`, `treatmentIntent`, `tumorBoardDecision`, `molecularResistanceFinding`, `recistResponse` | oBDS-Mapping auf XSD 3.1.0 |

Versionierung: keine neuen Versionssprünge. Alle Änderungen sind nicht brechend und fallen in den noch nicht
veröffentlichten Sprung seit `v0.1.0-rc.2` (howto §C). Sie sind in `provenance.history` (letzter Eintrag) und
`provenance.verification` (Eintrag 2026-11-25) je Element vermerkt.

## 7 Repo-Review

Zwei unabhängige Read-only-Prüfagenten haben das Repo geprüft, einer auf Konsistenz und Links, einer auf
Verständlichkeit für klinische und technische Nutzer:innen. Automatisch geprüft: `validate.py` 112/112,
Katalog und Phasen-Übersicht aktuell, `skill-lint` OK, Dubletten-Bild unverändert (57 eigenständig,
54 Nah-Dublette, 1 verwandt), alle Quellen-URLs erreichbar (bekannte Ausnahme: smoking-status-ValueSet, als
offener Punkt geführt).

**Korrigiert (Freigabe „Fehler + kleine Verbesserungen“):** Setup-Befehle (`cd data-elements` → Repo-Name),
Commit-Anleitung und CI-Drift-Check auf alle generierten Sichten, §D „neue Phase“ (zehn statt acht Stellen),
Vorlage `TEMPLATE.element.yaml` (Phase `primarycare`, `category`, gültiges YAML), Issue-Formular (veraltete
Leitlinien-Platzhalter, falscher LOINC-Beispielcode 89283-6, fehlende Kardinalität „mindestens einmal“),
Excel-Beispielzeile (LoE 3 statt 2b), Methodik (vier- statt dreistufig, Stand, Reifestufen, oBDS-/ISiK-Pins,
`mihub`-CodeSystem → `local-no-standard-binding`), widersprüchliche Verifikationsaussagen (README, AI_USAGE,
Audit-Log §15, Glossar), AI_USAGE (drei Beitrags-Spuren, vier Sub-Agenten, PR-Template-Feld erledigt),
go-public-Checkliste (release-please setzt `CITATION.cff`), Workflow-Doku (release-please, `supersededBy`),
Skill-Texte (Terminologie-Prüfung per Skript, Katalog-Generator), Glossar (oBDS, ISiK, KDL, `pvs`,
Frequenz-Codes, Evidenzskalen, Regelwerke, ICD-O-4, LV, Germany Edition, §21 Lesehilfe).
Neu: Issue-Formular `change-data-element.yml`, README-Hinweise „Schnellstart“ und „Reifegrad“.

## 8 Offene Punkte

Die Liste steht in [`docs/audit-log.md`](../audit-log.md) §16.6.
