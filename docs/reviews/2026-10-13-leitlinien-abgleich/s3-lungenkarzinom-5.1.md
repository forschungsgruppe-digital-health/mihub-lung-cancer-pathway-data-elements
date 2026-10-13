# S3-Leitlinie Lungenkarzinom (AWMF 020-007OL) — Versionsstand, Nachsorge-Extraktion und Abgleich mit dem MiHUB-Datenelemente-Katalog

> **Momentaufnahme vor der Umsetzung (2026-10-13).** Read-only-Abgleich des Katalogstands `0.1.0-rc.2` (51 Elemente) gegen die Leitlinie; die daraus abgeleiteten Änderungen sind in `docs/audit-log.md` §13 dokumentiert und im zugehörigen Pull Request umgesetzt. Zeilen- und Elementangaben beziehen sich auf den Stand **vor** dem Update. Erstellt KI-gestützt (Claude Code, Fable 5.1) mit Live-Abruf der Quellen; mit **UNSICHER** markierte Punkte sind nicht verifiziert.

Stand der Recherche: **2026-10-13** · Read-only (keine Repository-Änderung) · Berichtssprache Deutsch.

Geprüfte Repo-Artefakte: `catalog/data-dictionary.csv` (51 Elemente), `docs/phases-overview.md`, `docs/audit-log.md` (§2, §8, §13), `elements/follow-up/*.yaml`, `elements/surveillance/*.yaml`, `README.md` Z. 233, `docs/methodology.md` Z. 215/233, `GLOSSARY.md` (17 Stellen „v5.01"). 25 YAMLs referenzieren `source: S3-LL Lungenkarzinom`, alle mit `version: 5.01 (Konsultationsfassung 04/2026, AWMF 020-007OL)`.

## 0 Verifikationsstatus — was online geprüft wurde, was nicht

| Quelle | Status | Bemerkung |
| --- | --- | --- |
| Leitlinienprogramm-Onkologie-Seite `…/leitlinien/lungenkarzinom/` | **online verifiziert** | Download-Box „Version 5, 2026": Langversion **5.1** (`S3_LL_Lungenkarzinom_Langversion_5.1.pdf`, 9 MB), Leitlinienreport 5.0, Evidenzbericht AMNOG, 2 Methodenberichte CGS; Archiv: Langversion 5.0 (Juni 2026), 4.0 (April 2025), 3.0, 2.2 (letzte **Kurzversion**), 2.1, 2.0, 1.0 |
| Langversion **5.1** (PDF, 691 S., PDF-Erstellung 2026-07-17) | **vollständig heruntergeladen + textextrahiert** | Titel: „Version 5.1 - Juli 2026", Kap. 16 (S. 491–500), Tab. 44, Kap. 4.2, Kap. 15, Kap. 11/12, Empf. 8.6/8.77, Kap. 7, Kap. 19.3/Tab. 48, Kap. 2.1.3/2.2 |
| Langversion **5.0** (PDF, 691 S., 2026-06-29) | **heruntergeladen + Volltext-Diff gegen 5.1** | 154 geänderte Zeilen von ~41 000; keine im Bereich Kap. 15/16 |
| Langversion **4.0** (PDF, 661 S., 2025-04-07) | **heruntergeladen** | zur Klärung der Repo-Annotationen „geprüft 2025 / B" und der Tabellen-Nummerierung (Tab. 42) |
| **Leitlinienreport 5.0** (PDF, 199 S., 2026-06-15) | **heruntergeladen** | belegt Konsultationsphase 03.04.–02.05.2026 der „Konsultationsfassung Version 5.01" |
| AWMF-Register-Asset `020-007OLl_…_2026-07.pdf` | **online verifiziert** (HTTP 200, 10,3 MB, 691 S., identischer PDF-Zeitstempel 2026-07-17, Titelseite „Version 5.1 - Juli 2026") | Kurzversion-/Report-/Patientenleitlinien-Assets mit Suffix `2026-07` nicht vorhanden (HTTP 500) |
| AWMF-Register-Detailseite (SPA) | **UNSICHER** | rendert ohne JavaScript nur die Hülle; Register-Metadaten (Status, „gültig bis") nicht auslesbar. Die Langversion selbst nennt Gültigkeit „maximal 5 Jahre (Mai 2031)" |
| Konsultationsfassung **5.01** (04/2026) | **nicht mehr online — UNSICHER** | Aussagen über 5.01 nur indirekt (Leitlinienreport 5.0: Konsultation ergab „redaktionelle Korrekturen, keine erneute Abstimmung nötig") und über die Repo-Zitate in `audit-log.md` §8 |
| Deutsches Ärzteblatt 22.06.2026 „S3-Leitlinie zum Lungenkarzinom aktualisiert" | online verifiziert | Sekundärbestätigung der Veröffentlichung (DGP + DKG, 29 weitere Organisationen); nennt keine Versionsnummer |
| Repo-Zitate (`audit-log.md` §2) zu Empf. 16.1/16.4/16.5/16.7/16.8 und 16.3 | **gegen 5.1 gegengeprüft** | Wortlaut stimmt überein; **die Grad-Annotationen „B, geprüft 2025" stimmen nicht** (s. § 1.4) |

Alle Zitate in § 2 stammen aus der Textextraktion der Langversion 5.1 (Juli 2026); Seitenangaben beziehen sich auf die gedruckte Paginierung der 5.1.

## 1 Quelle + Versionsstand

### 1.1 Aktuelle Version (Oktober 2026)

- **Aktuell publiziert: Langversion 5.1 – Juli 2026** (final, keine Konsultationsfassung). Offizielle Zitierweise (Kap. 1.5): „Leitlinienprogramm Onkologie (Deutsche Krebsgesellschaft, Deutsche Krebshilfe, AWMF): Prävention, Diagnostik, Therapie und Nachsorge des Lungenkarzinoms, Langversion 5.1, 2026, AWMF-Registernummer: 020-007OL, https://www.leitlinienprogramm-onkologie.de/leitlinien/lungenkarzinom/".
- Gültigkeit (Kap. 2.1.3): „bis zur nächsten Aktualisierung gültig, maximal jedoch 5 Jahre (Mai 2031)"; Living Guideline mit jährlicher Überprüfung.
- Federführung: DGP + DKG; Methodik: Oxford 2009 (Altbestand), Oxford 2011 und seit 2025 bevorzugt GRADE (Tab. 4); Empfehlungsgrade A/B/0 (Tab. 5), EK ohne Buchstaben (Kap. 2.2.4).
- Zusatzdokumente zur Version 5: Leitlinienreport 5.0 (Juni 2026), Evidenzbericht AMNOG, 2 Methodenberichte. **Keine Kurzversion** zur Version 5 auffindbar (Kap. 1.9 kündigt sie an; letzte publizierte Kurzversion ist 2.2 vom Juli 2023) — UNSICHER, ob sie unter anderem Datum existiert.

### 1.2 Hat eine finale v5.x die Konsultationsfassung 5.01 abgelöst? — **Ja, zweimal.**

| Schritt | Datum | Beleg |
| --- | --- | --- |
| Konsultationsfassung **5.01** | 04/2026, Kommentierung 03.04.–02.05.2026 | Leitlinienreport 5.0 Kap. 7 („Konsultationsfassungen … innerhalb von 4 Wochen (03.04.2026 – 02.05.2026) … kommentiert"; Kommentartabelle verweist mehrfach auf „Konsultationsfassung Version 5.01") |
| Bearbeitung der Kommentare | Mai 2026 | Leitlinienreport 5.0 Tab. Prozess: „redaktionelle Korrekturen — keine erneute Abstimmung nötig" |
| **Finale Langversion 5.0** | Juni 2026 (PDF 29.06.2026; Dateiname `…_5.0_16.062026.pdf`) | Archiv der LL-Programm-Seite; Ärzteblatt 22.06.2026 |
| **Langversion 5.1** | Juli 2026 (PDF 17.07.2026) | Download-Box LL-Programm; AWMF-Asset `…_2026-07.pdf`. Kap. 1.6 „Versionsänderungen — Version 5.1 – Juli 2026: Änderungen zum Medikament Lurbinectedin bezüglich EU-Zulassung; Änderungen zum Medikament Tarlatamab bezüglich EU-Zulassung; Korrektur veralteter URL's" |

Volltext-Diff 5.0 → 5.1 (eigene Prüfung): nur Kap. 1 (Einfügung von 1.6 und Nummernverschiebung 1.6→1.7 … 1.10→1.11), eine URL in Kap. 3.7.5 (Radon), Kap. 9.6 (Lurbinectedin/Tarlatamab, Zulassungsfußnoten entfernt), Tab.-48-Zeilen zu 9.x/10.x (Layout). **Kap. 15 und Kap. 16 sind in 5.0 und 5.1 zeichenidentisch.**

### 1.3 Was hat sich im Nachsorge-relevanten Teil gegenüber 5.01 / 4.0 geändert?

Da 5.01 nicht mehr abrufbar ist, wird der Wandel über (a) Tab. 48 „Übersicht Änderungen in Version 5" (v4.0 → v5.0), (b) den Diff 5.0 ↔ 5.1 und (c) den Vergleich mit v4.0 belegt:

1. **Kap. 16 Nachsorge/Verlauf/Follow-Up: inhaltlich unverändert seit v4.0.** Tab. 48 enthält **keine** Zeile zu 15.x oder 16.x. Alle neun Empfehlungen tragen in 5.x den Stempel „geprüft 2026" (v4.0: „geprüft 2025", 16.9 „modifiziert 2025"). Wortlaut identisch (gegengeprüft).
2. **Evidenzlevel-Notation in Kap. 16 geändert** (einzige Abweichung zu v4.0): 16.3 „2b" → „**3**", 16.5 „1a" → „**2**", 16.6 „1a" → „**2**". Lesart: Umstellung von Oxford-2009-Buchstaben auf die Oxford-2011-Ziffernskala (Tab. 4 „1-5 (Oxford 2011)") — die Leitlinie erläutert die Umstellung für Kap. 16 nicht explizit → Interpretation **UNSICHER**, die Werte selbst sind verifiziert.
3. **Tabellen-Umnummerierung:** die Nachsorge-Indikationstabelle ist in v4.0 „Tabelle 42", in 5.0/5.1 „**Tabelle 44**: Indikationen zu diagnostischen Maßnahmen in der Nachsorge des Lungenkarzinoms" (S. 499). „Tabelle 42" bezeichnet in 5.x „Dimensionen und Outcomes von Atemnot und ihre Erfassungsinstrumente" (Kap. 14). Tab. 48 bleibt die Änderungsübersicht (in v4.0 war das Tab. 46). Inhalt der Tabelle unverändert.
4. **Kap. 15 Rehabilitation: „Kapitel derzeit wegen laufender Überarbeitung ausgesetzt"** (Überschrift); Empf. 15.1–15.5 tragen den Stempel „**ausgesetzt 2026**" (Altgraduierung 2010: B/B/C/D/D).
5. **Kap. 4.2 Tabakrauchen komplett überarbeitet:** 4.1–4.4 „modifiziert 2026", 4.5 „neu 2026"; alle Grad **A, Evidenzlevel 1**. Inhalte: E-Zigarette + Passivrauch (4.1), regelmäßige Erfassung/Dokumentation des Konsums von Tabak-/E-Zigaretten „sowie verwandter Produkte" (4.2), ABC-Schema + Vermittlung (Kurse, Telefonberatung, DiGA) (4.3), Pharmakotherapie für alle Rauchenden (4.4), Screening-Opt-out (4.5). Die Repo-Beschreibung in `methodology.md` Z. 233 trifft für 5.1 zu.
6. **Weitere 2026-Änderungen mit Nachsorge-Bezug:** Empf. 3.1 (EK, modifiziert 2026: Risikofaktoren inkl. Familienanamnese „sollen" erfragt werden); Statement 8.6 (EK, modifiziert 2026: standardisiertes Symptomassessment regelmäßig + frühzeitige Palliativberatung); Empf. 8.77 (EK, geprüft 2026: Reha, Psychoonkologie, Sozialberatung, Selbsthilfe, frühe palliative Therapie ansprechen); Kap. 7 „Aktualisierung Kommunikation" (Empf. 7.1–7.10, alle „geprüft 2026").
7. **Empfehlungsnummern in Kap. 16 haben sich in v5 NICHT verschoben** (die in `audit-log.md` §8 erwähnte Verschiebung 8.11→8.10 betrifft Kap. 8).

### 1.4 Befund zur Repo-Annotation „Empfehlungen 16.1–16.9 Aufwertung EK→B (2025)"

`audit-log.md` §8 (Analyzer-Lauf 2026-05-05) hat für 16.1, 16.4, 16.7, 16.8, 16.9 eine „Aufwertung EK → B" in 5.01 angenommen und `recommendation_grade` in 7 Elementen auf B gesetzt. Befund:

- In **v4.0 (April 2025)** sind 16.1, 16.2, 16.4, 16.7, 16.8, 16.9 **EK** (Konsensbasierte Empfehlung), 16.3 B/2b, 16.5 A/B/1a, 16.6 A/1a.
- In **5.0 und 5.1** sind 16.1, 16.2, 16.4, 16.7, 16.8, 16.9 ebenfalls **EK**; 16.3 B/3, 16.5 A/B/2, 16.6 A/2.
- Laut Leitlinienreport 5.0 löste die Konsultation nur redaktionelle Korrekturen ohne erneute Abstimmung aus; eine Rückstufung B→EK zwischen 5.01 und 5.0 ist damit praktisch ausgeschlossen.
- **Schlussfolgerung:** Die Annotationen „(B, geprüft 2025)" / „(B, modifiziert 2025)" und die Grade B in `structuredFollowUpPlan`, `followUpInterval`, `brainMriHighRisk`, `recurrenceOrSecondPrimary`, `ctThoraxFinding`, `restagingImagingDate`, `recistResponse` sowie das B/1a in `firstFollowUpVisitDate` sind mit hoher Wahrscheinlichkeit ein Analyzer-Artefakt (UNSICHER nur insofern, als 5.01 selbst nicht mehr einsehbar ist). Korrektur → § 4.2 / § 6. Hinweis: EK-Empfehlungen tragen per Kap. 2.2.4 keinen Buchstaben; die Stärke folgt der Formulierung („sollte" ≙ B-Stärke) — das erklärt vermutlich die Fehlzuordnung.

## 2 Empfehlungen & Nachsorge-Tabelle (Langversion 5.1, Juli 2026)

### 2.1 Kap. 16 „Nachsorge/Verlauf/Follow-Up" — Empfehlungen 16.1–16.9

| Nr. | Typ · Status | Wortlaut (Kurzzitat) | Grad | Evidenzlevel (5.1 / v4.0) | Population | Konsens |
| --- | --- | --- | --- | --- | --- | --- |
| 16.1 | Konsensbasierte Empf. · geprüft 2026 | „Nach Abschluss einer multimodalen Therapie (Stadium I-IIIC, OMD), die ein lokal ablatives Verfahren (OP, RTx, CTx/RTx) beinhaltet, sollte für jeden Patienten ein strukturierter Nachsorgeplan erstellt werden. Der strukturierte Nachsorgeplan sollte geeignet sein, Rezidive, Zweitkarzinome, Komplikationen und Toxizitäten der Therapie und den Bedarf an Psychoonkologie und Sozialberatung zu erkennen" | EK | — | kurativ/lokal-ablativ behandelt, Stadium I–IIIC + OMD | starker Konsens |
| 16.2 | Konsensbasierte Empf. · geprüft 2026 | „Im Verlauf einer systemischen Therapie (Stadium IVA, IVB) sollte für jeden Patienten ein strukturierter Verlaufsplan/Follow-up-Plan erstellt werden … geeignet sein, Progression/Rezidive, Zweitkarzinome, Komplikationen und Toxizitäten der Therapie und den Bedarf an Psychoonkologie, Palliativmedizin und Sozialberatung zu erkennen." | EK | — | Stadium IVA/IVB unter Systemtherapie | starker Konsens |
| 16.3 | Evidenzbasierte Empf. · geprüft 2026 | „Patienten mit Lungenkarzinom sollten nachhaltig motiviert werden, mit dem Tabakrauchen aufzuhören. Zur Unterstützung sollten die Patienten wirksame Hilfen zur Raucherentwöhnung erhalten." | **B** | **3** / 2b | alle Patienten mit Lungenkarzinom | starker Konsens |
| 16.4 | Konsensbasierte Empf. · geprüft 2026 | „Bei Patienten nach ablativer lokaler Therapie (Operation im Stadium I-II und III, Strahlentherapie/Strahlenchemotherapie im Stadium I und II) sollten die posttherapeutischen Komplikationen … erfasst und behandelt werden. Typischerweise erfolgt dies im Rahmen einer Vorstellung innerhalb von 8 Wochen nach Abschluss der lokalen Therapie." | EK | — | nach OP (I–III) bzw. RT/RCT (I–II) | starker Konsens |
| 16.5 | Evidenzbasierte Empf. · geprüft 2026 | „Bei Patienten mit NSCLC im Stadium III nach ablativer lokaler Therapie (Strahlentherapie/Strahlenchemotherapie) sollten die posttherapeutischen Komplikationen … erfasst und behandelt werden. Die erste klinische Vorstellung nach Abschluss der Strahlentherapie soll innerhalb von 8 Wochen erfolgen." | **A/B** | **2** / 1a | NSCLC Stadium III nach RT/RCT | Konsens |
| 16.6 | Evidenzbasierte Empf. · geprüft 2026 | „Nach lokal ablativer Therapie des NSCLC im Stadium III soll zum Ausschluss einer Progression ein CT-Thorax durchgeführt werden (zwecks Beginn des Einsatzes von Durvalumab)." | **A** | **2** / 1a | NSCLC Stadium III (vor Durvalumab-Konsolidierung) | starker Konsens |
| 16.7 | Konsensbasierte Empf. · geprüft 2026 | „Nach abgeschlossener multimodaler Therapie (inklusive OP oder CTx/RTx) sollten die Patienten in den ersten 2 Jahren vierteljährlich (alle 3 Monate), ab dem 3. Jahr halbjährlich untersucht und nach 5 Jahren in ein Screeningprogramm eingeschlossen werden. Diese Intervalle beginnen mit der Erstvorstellung innerhalb von 8 Wochen nach Abschluss der Therapie. Bei diesen Nachsorgeterminen sind eine dezidierte Anamnese, eine körperliche Untersuchung und geeignete bildgebende Verfahren (Röntgen Thorax, Sonografie Abdomen oder CT-Untersuchungen) durchzuführen." | EK | — | nach multimodaler Therapie (kurativ) | starker Konsens |
| 16.8 | Konsensbasierte Empf. · geprüft 2026 | „Bei Hochrisikopatienten (z.B. EGF-R+, ALK+, ROS-1+, Adenokarzinome mit Stadium III) sollte, nach Maßgabe des interdisziplinären Behandlungsteams, regelmäßig ein Schädel-MRT durchgeführt werden." | EK | — | Hochrisiko (EGFR/ALK/ROS1, Adeno Stadium III) | starker Konsens |
| 16.9 | Konsensbasierte Empf. · geprüft 2026 (v4.0: modifiziert 2025) | „Unter einer Systemtherapie im Stadium IVA/B sollten Ansprechen, Nebenwirkungen und Beschwerdebild einen Monat nach Abschluss der Behandlung durch das den Patienten betreuende Team evaluiert werden. Als Basis sind dabei Anamnese, körperliche Untersuchung, CT-Thorax/Abdomen/Becken und je nach Beschwerdebild geeignete bildgebende Verfahren (MRT Schädel bei Verdacht auf Hirnmetastasen) durchzuführen. Danach sollten festgelegte Wiedervorstellungen bei laufender Erhaltungstherapie (NSCLC, SCLC) mindestens alle 3-6 Wochen erfolgen. Bei Patienten unter laufender Systemtherapie sind CT Kontrollen im Verlaufsintervall von 6 bis 9 Wochen sinnvoll." | EK | — | Stadium IVA/B unter Systemtherapie (NSCLC, SCLC) | starker Konsens |

### 2.2 Statements und tragende Hintergrundaussagen in Kap. 16

Kap. 16 enthält **keine formalen Statements** (nur Empfehlungen). Nachsorge-relevante Hintergrundaussagen mit Evidenzangabe:

| Fundstelle | Aussage | Evidenz |
| --- | --- | --- |
| 16.1 Nr. 1 (S. 491) | Ziel der Nachsorge kurativ Behandelter: frühzeitige Diagnose von Rezidiv-/Zweittumoren zur Erhaltung der Heilungschance; Rezidiv-/Fernmetastasenraten nach Stadium (IA LR 10 %/FM 15 % … III LR 15 %/FM 60 %); Rezidivrisiko in den ersten 2 Jahren am höchsten, Zweitkarzinome nehmen mit Abstand zur OP zu | 2b / 1a / 1b |
| 16.1 Nr. 2 (S. 491 f.) | Stadium IV: Begriff „Follow-up/Verlaufsbeobachtung" statt Nachsorge; real-world-Ergebnisse signifikant ungünstiger als in Studien mit festen Bildgebungskontrollen („Formal: Evidencegrad IIa") | IIa |
| 16.3 (S. 493) | Nachsorge umfasst Erfassung posttherapeutischer Komplikationen (Post-Pneumonektomiesyndrom, Strahlenfibrose, **immun-bezogene Komplikationen**), Nachsorgeintervall, Kosten-Nutzen, Untersuchungsintensität; „Survivorship-Analysen … bisher extrem selten … dringend zu fordern" | — |
| 16.3.1 (S. 493) | Komplikationen nach OP (Schmerz, Infektion, Lungenfunktionsverlust) und RT (Ösophagitis, Pneumonitis, Haut, Herz, Rückenmark) | 1b |
| 16.3.2 (S. 494) | Fester Zeitplan vs. symptomorientiert kontrovers; IFCT-Studie: nach 4–5 Jahren signifikant mehr Zweittumoren entdeckt; LDCT-Screening-Daten (NLST, NELSON) übertragbar | 2b / 1a |
| 16.3.3 (S. 494 f.) | Röntgen-Thorax „nicht die relevante Untersuchung"; LDCT im randomisierten Vergleich effektiv; keine deutschen Kosten-Nutzen-Analysen | 2b |
| 16.3.4 (S. 495 f.) | Intensive Nachsorge (Labor, Rö-Thorax, jährliche Bronchoskopie + CT) ohne Überlebensvorteil (Virgo); **Tumormarker in der Nachsorge nicht empfohlen** (1a); **Hirnmetastasen-Screening ohne Risikoindikation nicht empfohlen**; ED-SCLC bei Watch-and-Wait statt PCI: „MUSS … ein MRT Schädel alle drei Monate durchgeführt werden"; NSCLC IV mit EGFR/ALK/ROS1: hohes kumulatives Hirnmetastasenrisiko | 2b / 1a |
| 16.4 (S. 498) | Stadium IV: Standard Chemoimmuntherapie 4–5 Zyklen + Erhaltung; in Studien CT-Thorax und CT Abdomen/Becken alle 6–9 Wochen — in der Praxis „so eng wie möglich adaptieren" | — |
| 16.5 (S. 500) | Pflege-geleitetes Follow-up (Moore): gleiche OS/Kosten, bessere Zufriedenheit, weniger Arztkontakte/Bildgebung — „eher als supportiv und nicht als alternativ" | RCT |
| 16.6 (S. 500) | Forschungsbedarf: a) Integration LDCT nach 3–4 Jahren, b) Intervalle in den ersten 3 Jahren, c) Kosteneffektivität inkl. Langzeittoxizität unter Checkpoint-Inhibitoren, d) **Lebensqualität bei verschiedenen Nachsorgestrategien**, e) Vereinfachung des Follow-up im Stadium IV | — |

### 2.3 Tabelle 44 (= Tab. 42 in v4.0 / 5.01): Indikationen zu diagnostischen Maßnahmen in der Nachsorge

| Diagnostische Methode | Indikation (Wortlaut) |
| --- | --- |
| Bronchoskopie | Hohes Lokalrezidivrisiko (z.B. Ma[n]schettenresektion) |
| PET-CT | Ausschluss von Metastasen vor erneutem thoraxchirurgischem Eingriff |
| MRT | Hirn- und Knochenmetastasen |
| Röntgen Thorax | Tumorkinetik |
| Thorax CT | Tumorkinetik und lokale Ausdehnung |
| Abdomensonographie | Leber und Nebennierenmetastasen, paraaortale Lymphome |
| Abdomen CT | Abdominelle Metastasen |
| Lungenfunktionsprüfung, CO-Diffusionskapazität | Lungenfunktionseinschränkung, Pneumonitis |
| Laborparameter | Nach Maßgabe des Behandlers |

**Wichtig:** Tab. 44 ist eine reine **Indikationstabelle ohne Zeitachse**. Jahresintervalle stehen ausschließlich in Empf. 16.7 (kurativ) und 16.9 (Stadium IV); modalitätsspezifische Jahrespläne (wie Onkopedia Tab. 12/Tab. 9) gibt die S3-LL nicht vor. Daraus abgeleiteter Untersuchungsplan:

| Maßnahme | Jahr 1–2 | Jahr 3–5 | ab Jahr 6 | Beleg |
| --- | --- | --- | --- | --- |
| Erstvorstellung nach Therapieende | ≤ 8 Wochen (Startpunkt der Intervalle) | — | — | 16.4 (EK), 16.5 (A/B, 2), 16.7 (EK) |
| Dezidierte Anamnese + körperliche Untersuchung | alle 3 Monate | alle 6 Monate | Screeningprogramm (Intervall nicht spezifiziert — UNSICHER, ob jährlich) | 16.7 (EK) |
| Bildgebung: Röntgen Thorax **oder** Sonografie Abdomen **oder** CT | an jedem Termin „geeignete" Verfahren | dto. | LDCT-Screening | 16.7 (EK); Tab. 44; Hintergrund 16.3.3 favorisiert CT |
| CT-Thorax einmalig vor Durvalumab (NSCLC III nach RCT) | einmalig nach Abschluss RCT | — | — | 16.6 (A, 2) |
| Schädel-MRT | Hochrisiko „regelmäßig" (kein Intervall); ED-SCLC Watch-and-Wait alle 3 Monate | nach Maßgabe | — | 16.8 (EK); 16.3.4 |
| Lungenfunktion/DLCO, Bronchoskopie, PET-CT, Abdomen-CT, MRT Knochen, Labor | indikationsbezogen | indikationsbezogen | — | Tab. 44 |
| Tumormarker | **nicht empfohlen** | | | 16.3.4 (1a) |
| Stadium IV unter Systemtherapie | Basisevaluation 1 Monat nach Abschluss (Anamnese, körperliche Untersuchung, CT Thorax/Abdomen/Becken, MRT Schädel bei Verdacht); Wiedervorstellung alle 3–6 Wochen; CT alle 6–9 Wochen | | | 16.9 (EK), Kap. 16.4 |

### 2.4 Kap. 4.2 Tabakrauchen und Lungenkarzinom (S. 61–65)

| Nr. | Status | Wortlaut (Kurzzitat) | Grad | LoE | Population |
| --- | --- | --- | --- | --- | --- |
| 4.1 | modifiziert 2026 | „Aktives Tabakrauchen, das Rauchen der E-Zigarette und eine Passivrauchexposition sollen konsequent vermieden werden." | A | 1 | allgemein |
| 4.2 | modifiziert 2026 | „Bei Patienten mit Lungenkarzinom soll der Konsum von Tabak- und E-Zigaretten sowie verwandter Produkte regelmäßig erfragt und dokumentiert werden." | A | 1 | Patienten mit Lungenkarzinom |
| 4.3 | modifiziert 2026 | „Rauchende Patienten mit Lungenkarzinom sollen strukturiert (z.B. nach ABC-Schema) beraten und an ein professionelles Angebot zur Tabakentwöhnung vermittelt werden (z.B. Tabakentwöhnungskurse, Telefonberatung oder DiGA)." | A | 1 | rauchende Patienten |
| 4.4 | modifiziert 2026 | „Allen rauchenden Patienten mit Lungenkarzinom soll eine pharmakologische Therapie (z.B. eine Nikotinersatztherapie oder Vareniclin) angeboten werden." | A | 1 | rauchende Patienten |
| 4.5 | neu 2026 | „Rauchenden, die sich einem Lungenkarzinom-Screening unterziehen, soll eine Tabakentwöhnung mit Beratung (z.B. ABC-Ansatz) und pharmakologischer Unterstützung angeboten werden (opt out Ansatz)." | A | 1 | Screening-Teilnehmende (Phase `screening`, nicht Nachsorge) |

Hintergrund 4.2.1: ABC = Ask (Rauchstatus erfragen + dokumentieren) – Brief Advice – Cessation Support; Befragung „im Sinne eines opt-out-Ansatzes – vor allem bei Erstkontakt, aber auch wiederholt im Verlauf"; E-Zigarette „weder zur Tabakentwöhnung noch … Harm Reduction empfohlen"; G-BA-Erstattung NET/Vareniclin seit 20.08.2025 (Fagerström ≥ 6 bzw. tabakassoziierte chronische Lungen-/Herzerkrankung; 3 Monate, Wiederholung erst nach 3 Jahren); Cytisin in Deutschland nicht vertrieben. Ergänzend Empf. 3.1 (EK, modifiziert 2026): Risikofaktoren (Rauchen, berufliche Noxen, Familienanamnese) „sollen" erfragt werden.

### 2.5 Kap. 15 Rehabilitation — „Kapitel derzeit wegen laufender Überarbeitung ausgesetzt" (S. 487–490)

| Nr. | Status | Kernaussage | Grad (Altschema 2010) | LoE |
| --- | --- | --- | --- | --- |
| 15.1 | ausgesetzt 2026 | Einzelne nicht-medikamentöse/pflegerische Reha-Maßnahmen verbessern Lebensqualität (inkl. psychische Befindlichkeit) oder Luftnot → im Rahmen ambulanter/stationärer Reha empfohlen | B | 1a |
| 15.2 | ausgesetzt 2026 | Aerobe Ausdauertrainingsprogramme während onkologischer Therapie empfohlen | B | 1b |
| 15.3 | ausgesetzt 2026 | Stationäre onkologische Reha nach Primärtherapie bei erfüllten BAR-Qualitätsanforderungen; Dauer flexibel, Ziele „Reha vor Rente/Pflege" | C | — |
| 15.4 | ausgesetzt 2026 | Ambulante Reha nur bei vergleichbaren Anforderungen; pneumologische Fachkompetenz; Primärbehandler bei Klinikauswahl beteiligen | D | — |
| 15.5 | ausgesetzt 2026 | Operierte und Patienten nach eingreifender Therapie (RCT) mit ausgeprägten Folgestörungen sollten in Bezug auf Kontextfaktoren (berufliche Situation, häusliche Versorgung, Freizeit) einer Reha zugeführt werden | D | — |

Nachsorge-relevante Reha-Bausteine (Kapiteltext): sozialmedizinische Beurteilung, strukturierte Raucherentwöhnung, „Initiierung von Nachsorgemaßnahmen (u.a. ambulante Lungensportgruppen, Fortführung der Raucherentwöhnung)", Anregung berufsfördernder Leistungen. Ferner Empf. 8.77 (EK, geprüft 2026): „Neben der medizinischen Behandlung sollten die Möglichkeiten zur Rehabilitation, psychoonkologischen Unterstützung, Sozialberatung bzw. Unterstützung durch Selbsthilfegruppen und der frühen palliativen Therapie angesprochen werden." Kap. 7.3.2 (Hintergrund): Nachsorge- und Reha-Möglichkeiten „sollen ebenfalls angesprochen werden … Bei Bedarf sind entsprechende Kontakte zu vermitteln."

### 2.6 Psychoonkologie/Distress, Sozialberatung, Survivorship/Übergabe an Hausärzt:innen

- **Kap. 11 Psychoonkologische Versorgung (S. 469 f.)**: reiner Verweis auf die S3-LL Psychoonkologie (Themen u.a. „Diagnostik → Screening", „Sektorenübergreifende Koordination der psychoonkologischen Versorgung"). Das Wort „Distress" kommt in der Lungenkarzinom-LL nicht vor; **kein eigenes Screening-Instrument empfohlen**. Operativer Anker: Empf. 16.1/16.2 („Bedarf an Psychoonkologie [, Palliativmedizin] und Sozialberatung zu erkennen"), 8.77 (EK), Statement 8.6 (EK, modifiziert 2026: standardisiertes Symptomassessment regelmäßig), Empf. 7.7/7.8 (A: Advance Care Planning bei nicht heilbarer Erkrankung).
- **Kap. 12 Supportive Behandlung (S. 471)**: Verweis auf S3-LL Supportive Therapie; Themenliste ohne Impfungen.
- **Survivorship / Übergabe an die Hausarztpraxis: keine Empfehlung.** „Survivorship" nur als Forschungsdesiderat (16.3, 16.3.1); „Hausarzt" nur in Früherkennung/Diagnoseverzögerung (Kap. 5/6). Kein Survivorship Care Plan, kein Abschlussbericht, kein Medikations-/Impfplan, keine AU-Regelung (Begriff „Arbeitsunfähig" nur in der Karnofsky-Tabelle Kap. 6.2). Kontext aus v4.0 Tab. 46: die bis v3 in Empf. 16.1 enthaltene Formulierung „In diesen Nachsorgeplan sollten alle im stationären und ambulanten Sektor Verantwortlichen eingebunden sein" wurde 2024 gestrichen — die sektorenübergreifende Komponente ist seitdem nicht mehr Gegenstand einer Empfehlung.

### 2.7 Qualitätsindikatoren (Kap. 18, Tab. 45)

Finales Set 15 QI (QI 4 unbesetzt): **kein QI zu Nachsorge, Tabakentwöhnung oder Psychoonkologie**.

## 3 Abdeckungs-Matrix (S3-LL 5.1 → Repo, Phasen `followup` / `surveillance`)

| Leitlinien-Item | Status | Repo-Element(e) | Lücke / Abweichung |
| --- | --- | --- | --- |
| Empf. 16.1 strukturierter Nachsorgeplan (EK) | COVERED | `structuredFollowUpPlan` | Grad B → **EK**; „geprüft 2025" → „geprüft 2026"; Population (Stadium I–IIIC, OMD, lokal ablatives Verfahren) nicht im Trigger |
| Empf. 16.1 Ziele: Rezidive/Zweitkarzinome erkennen | COVERED | `recurrenceOrSecondPrimary`, `ctThoraxFinding`, `brainMriFinding` | Grad B → EK (16.1); `ctThoraxFinding`: Tab. 42 → **Tab. 44** |
| Empf. 16.1/16.2 Bedarf Psychoonkologie erkennen | PARTIAL | `psychoOncologyReferral` (nur followup); `distressThermometerScore` (Quelle S3 Palliativ) | Fehlt in `surveillance`; S3-Lung-Beleg für Distress-Instrument gibt es nicht (nur Kap. 11 → S3-LL Psychoonkologie) → Referenz-Hinweis ergänzen |
| Empf. 16.1/16.2/8.77 Bedarf **Sozialberatung** erkennen | MISSING | — | neues Element `socialCounsellingReferral` (§ 4.1) |
| Empf. 16.2 strukturierter Verlaufsplan Stadium IV (EK) | MISSING | — (kein Pendant in `surveillance`) | neues Element `structuredSurveillancePlan` |
| Empf. 16.2 Bedarf Palliativmedizin erkennen; Statement 8.6 Symptomassessment | PARTIAL | `earlyPalliativeReferral` (Quelle S3 Palliativ; Definition laut audit-log um 8.6 erweitert), `symptomAssessmentInstrument` (nur `palliative`) | S3-Lung-Referenz (16.2 EK; 8.6 Statement EK, modifiziert 2026) fehlt im `evidence`-Block; standardisiertes Symptomassessment unter Systemtherapie ohne Element |
| Empf. 16.3 Rauchstopp-Motivation + wirksame Hilfen (B, LoE 3) | COVERED | `smokingStatus`, `tobaccoCessationCounselling` | LoE 2b → **3**; Primärbeleg sollte Empf. 4.2 bzw. 4.3/4.4 (A, 1) sein |
| Empf. 4.2 Konsum Tabak-/E-Zigaretten/verwandte Produkte regelmäßig erfragen + dokumentieren (A, 1) | PARTIAL | `smokingStatus` (E-Zigarette + Passivrauch bereits kodiert; `1..1`, per-encounter) | Referenz 4.2 fehlt im YAML (nur 16.3 + S3 Tabakentwöhnung 2021); „verwandte Produkte" (z.B. Tabakerhitzer, Nikotinbeutel — UNSICHER, LL nennt keine Beispiele) ohne Coding |
| Empf. 4.3 ABC-Schema, Vermittlung (Kurse/Telefon/DiGA) (A, 1) | PARTIAL | `tobaccoCessationCounselling` (Definition + SNOMED 386516008) | Referenz 4.3 fehlt im `evidence`-Block |
| Empf. 4.4 Pharmakotherapie allen Rauchenden anbieten (A, 1) | PARTIAL | `tobaccoCessationCounselling` (ATC N07BA01/N07BA03 als Codings) | Referenz 4.4 fehlt; kein Status „angeboten/abgelehnt/verordnet" |
| Empf. 4.5 Screening-Opt-out (A, 1, neu 2026) | MISSING (bewusst) | — | gehört zur Phase `screening` (audit-log §8) |
| Empf. 16.4 Komplikationen nach lokaler Therapie, Vorstellung ≤ 8 Wo (EK) | COVERED | `postTherapyComplication`, `firstFollowUpVisitDate` | `firstFollowUpVisitDate` B/1a → EK (16.4) + A/B, LoE 2 (16.5); `postTherapyComplication` LoE 1a → **2** |
| Empf. 16.5 NSCLC III nach RT: Komplikationen, Vorstellung ≤ 8 Wo (A/B, 2) | COVERED | dto. | LoE-Update; Population „NSCLC III nach RT/RCT" im Trigger ergänzen |
| Empf. 16.6 CT-Thorax NSCLC III vor Durvalumab (A, 2) | PARTIAL | `ctThoraxScan` (zitiert 16.6 für den gesamten Nachsorge-Rhythmus) | 16.6 ist ein **einmaliges** CT in Stadium III; der Nachsorge-Rhythmus stützt sich auf 16.7 (EK)/Tab. 44 → Referenz aufteilen; LoE 1a → 2; Tab. 42 → 44 |
| Empf. 16.7 Intervalle Q3M (J1–2), Q6M (J3–5), Screening ab J6 (EK) | PARTIAL | `followUpInterval` (Q3M-Y1-Y2; Q6M-Y3-Y5; Q12M-PostY5) | Grad B → EK; `Q12M-PostY5` nicht aus der LL ableitbar (nur „Screeningprogramm") — UNSICHER; Startpunkt „Erstvorstellung ≤ 8 Wo" ist über `firstFollowUpVisitDate` abgebildet |
| Empf. 16.7 Inhalt je Termin: dezidierte Anamnese | MISSING | — | neues Element (§ 4.1) |
| Empf. 16.7 Inhalt: körperliche Untersuchung | MISSING | — | neues Element |
| Empf. 16.7 Inhalt: Röntgen Thorax / Sonografie Abdomen / CT (Optionen) | PARTIAL | `ctThoraxScan` (nur CT) | Rö-Thorax, Sono Abdomen, CT Abdomen fehlen |
| Empf. 16.8 Schädel-MRT Hochrisiko (EK) | COVERED | `brainMriHighRisk`, `brainMriFinding` | Grad B → EK; Intervall „Q6-9M-Y1-Y3" stammt nicht aus der S3-LL („regelmäßig … nach Maßgabe des interdisziplinären Behandlungsteams") → Onkopedia als Intervallquelle kennzeichnen; Population EGFR/ALK/ROS1/Adeno III in Trigger |
| Kap. 16.3.4 ED-SCLC Watch-and-Wait: MRT alle 3 Mo | COVERED | `brainMriUnderTherapy`, `brainMriFinding` | Statement-Typ korrekt (Hintergrundtext); Empf. 16.9 („MRT Schädel bei Verdacht") als zweite Referenz |
| Kap. 16.3.4 Tumormarker nicht empfohlen (1a) | COVERED (durch Nicht-Existenz) | — | kein Element anlegen; bei `laboratoryTestFollowUp` (§ 4.1) als Ausschluss vermerken |
| Empf. 16.9 Basisevaluation 1 Monat nach Abschluss (EK) | MISSING | — | neues Element `postInductionEvaluationDate` |
| Empf. 16.9 Anamnese + körperliche Untersuchung unter Systemtherapie | MISSING | `ecogPerformanceStatusSurveillance` (nur indirekt) | neue Elemente (phase `surveillance`) |
| Empf. 16.9 CT Thorax/Abdomen/Becken alle 6–9 Wo (EK) | PARTIAL | `restagingImagingDate` (Q6-9W), `recistResponse` | Grad B/„modifiziert 2025" → EK/„geprüft 2026"; Körperregion (Thorax/Abdomen/Becken) nicht abgebildet |
| Empf. 16.9 Wiedervorstellung alle 3–6 Wo unter Erhaltungstherapie | MISSING | — | neues Element `surveillanceVisitDate` |
| Empf. 16.9 Nebenwirkungen/Toxizitäten | COVERED | `adverseEventCtcae`, `adverseEventCtcaeGrade`, `immuneRelatedAdverseEvent` | `immuneRelatedAdverseEvent`: Zitat „Kap. 16.3.1 (immun-bezogene Komplikationen)" → Begriff steht in der Einleitung 16.3; LoE 1b in 16.3.1 betrifft OP-/RT-Komplikationen → LoE auf n/a (UNSICHER) |
| Empf. 16.9 Ansprechen; Kap. 16.4 Systemtherapiekonzept | COVERED | `recistResponse`, `systemicTherapyRegimen` | nur Versions-/Grad-Update |
| Kap. 16.1 real-world vs. Studie (IIa) | COVERED | `therapyLineNumber` | Hintergrundtext, kein formales Statement — Typ „Statement" tolerierbar, im `section` vermerken |
| Kap. 16.6 Forschungsbedarf QoL | COVERED | `qolEortcQlqC30` | — |
| Tab. 44 Lungenfunktion/DLCO | COVERED | `pulmonaryFunctionTest`, `fev1PercentPredicted`, `dlcoPercentPredicted` | Tab. 42 → **44**; Grad „EK" ist für eine Indikationstabelle nicht vergeben → `n/a` empfohlen |
| Tab. 44 Bronchoskopie (hohes Lokalrezidivrisiko) | MISSING | — | neues Element (ad hoc) |
| Tab. 44 PET-CT (vor erneuter Thoraxchirurgie) | MISSING | — | neues Element (ad hoc) |
| Tab. 44 MRT Knochenmetastasen | MISSING | (`brainMri*` nur Schädel) | neues Element oder generisches Bildgebungs-Element |
| Tab. 44 Röntgen Thorax | MISSING | — | neues Element |
| Tab. 44 Abdomensonographie | MISSING | — | neues Element |
| Tab. 44 Abdomen-CT | MISSING | — | neues Element |
| Tab. 44 Laborparameter | MISSING | — | neues Element (ad hoc, ohne Tumormarker) |
| Kap. 16.5 Pflege-assoziiertes Follow-up | MISSING (optional) | `smokingStatus` (Rolle Pflege) | kein eigenes Element nötig; `responsible_role` der Visit-Elemente um „Pflege (supportiv)" erweitern |
| Kap. 15 Reha (ausgesetzt), Empf. 15.5, 8.77 | MISSING | — | neues Element `rehabilitationReferral` |
| Empf. 7.7/7.8 ACP (A) | COVERED (Phase `palliative`) | `advanceCarePlanning` (Quelle S3 Palliativ) | S3-Lung 7.7 (A) als Zweitreferenz optional |
| Survivorship Care Plan / Übergabe Hausarzt | MISSING in S3 (Repo COVERED aus Fremdquellen) | `survivorshipCarePlan` (AG LONKO, Klein 2026, OCP) | keine S3-Referenz eintragen; ggf. Empf. 16.1 als „nächstliegend" vermerken |

### 3.1 Elemente mit nicht mehr passender Empfehlungsnummer / Grad / Evidenzlevel (gegen 5.1)

| Element | Aktuell im Repo (`section` · grade · LoE) | Korrekt nach 5.1 |
| --- | --- | --- |
| `structuredFollowUpPlan` | Empf. 16.1 (Konsensbasiert, B, geprüft 2025) · B · n/a | Empf. 16.1 (EK, geprüft 2026) · **EK** · n/a |
| `recurrenceOrSecondPrimary` | Empf. 16.1 (B, geprüft 2025); Kap. 16.3.4 · B | Empf. 16.1/16.2 (EK, geprüft 2026); Kap. 16.3.4 · **EK** |
| `followUpInterval` | Empf. 16.7 (B, geprüft 2025) · B | Empf. 16.7 (EK, geprüft 2026) · **EK** |
| `brainMriHighRisk` | Empf. 16.8 (B, geprüft 2025) · B | Empf. 16.8 (EK, geprüft 2026) · **EK** |
| `ctThoraxFinding` | Tab. 42 …; Empf. 16.7 (geprüft 2025) · B | **Tab. 44**; Empf. 16.7 (EK, geprüft 2026) · **EK** |
| `ctThoraxScan` | Tab. 42 / Empf. 16.6 (A, 1a) · A · 1a | Tab. 44 + Empf. 16.7 (EK) für den Rhythmus; Empf. 16.6 (A, **2**) nur für das einmalige CT NSCLC III |
| `firstFollowUpVisitDate` | Empf. 16.4/16.5 (EK / B), geprüft 2025 · B · 1a | Empf. 16.4 (EK) / 16.5 (**A/B**, LoE **2**), geprüft 2026 |
| `postTherapyComplication` | Empf. 16.4 (EK), 16.5 (A/B, 1a) · A · 1a | Empf. 16.4 (EK), 16.5 (A/B, **2**); Kap. 16.3.1 · A/B · 2 |
| `smokingStatus` | Empf. 16.3 (B, 2b) · B · 2b | Empf. 16.3 (B, **3**); zusätzlich **Empf. 4.2 (A, 1, modifiziert 2026)** |
| `tobaccoCessationCounselling` | Empf. 16.3 (B) · B · 2b | Empf. 16.3 (B, 3); zusätzlich **Empf. 4.3 + 4.4 (A, 1, modifiziert 2026)** |
| `recistResponse`, `restagingImagingDate` | Empf. 16.9 (B, modifiziert 2025) · B | Empf. 16.9 (EK, geprüft 2026) · **EK** |
| `pulmonaryFunctionTest`, `fev1PercentPredicted`, `dlcoPercentPredicted` | Tab. 42 · EK | **Tab. 44** · n/a (Indikationstabelle) |
| `immuneRelatedAdverseEvent` | Kap. 16.3.1 (immun-bezogene Komplikationen) · EK · 1b | Kap. 16.3 (Einleitung) / 16.3.1 · EK · n/a (UNSICHER) |
| `brainMriFinding`, `adverseEventCtcae`, `adverseEventCtcaeGrade`, `ecogPerformanceStatusSurveillance`, `systemicTherapyRegimen`, `psychoOncologyReferral`, `brainMriUnderTherapy`, `therapyLineNumber`, `qolEortcQlqC30` | Grad/Sektion stimmen | nur Versions-String (§ 6) |

Dokumente: `README.md` Z. 233 („Empfehlungen 16.1–16.9 Aufwertung EK→B", „Tab. 42, Tab. 48"), `docs/methodology.md` Z. 215/233 (dto.), `GLOSSARY.md` Z. 182–185 („Empf. 16.7 (B)"), Z. 22–118 („v5.01") → anpassen (§ 6).

## 4 Vorgeschlagene neue oder zu ändernde Datenelemente

Konventionen wie im Katalog (`frequency_pattern`-Vokabular, Rollen). `version` in allen Referenzen = `5.1 (Juli 2026, AWMF 020-007OL)`; `source` = `S3-LL Lungenkarzinom`. Codings bewusst offen gelassen (Validator-Lauf), bis auf zwei sichere SNOMED-Kandidaten.

### 4.1 Neue Elemente

| label_de | name · phase | definition_de | datatype · cardinality | trigger | frequency_pattern | responsible_role | guideline reference |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Nachsorgetermin (Datum) | `followUpVisitDate` · followup | Datum jedes regulären Nachsorgetermins nach kurativer multimodaler Therapie; Basis für die Prüfung der Intervalltreue (3-/6-monatlich) gegenüber dem Nachsorgeplan. | dateTime · 0..* | jeder Nachsorgetermin gemäß Nachsorgeplan, beginnend mit der Erstvorstellung ≤ 8 Wochen | Q3M-Y1-Y2;Q6M-Y3-Y5 | Onkologe / Pneumologe / Thoraxchirurg | {section: "Empf. 16.7 (EK, geprüft 2026)", recommendation_grade: "EK", evidence_level: "n/a"} |
| Anamnese-Befund Nachsorge | `followUpAnamnesisFinding` · followup | Ergebnis der dezidierten Anamnese am Nachsorgetermin: neue oder persistierende Symptome (z.B. Husten, Dyspnoe, Schmerz, Gewichtsverlust, neurologische Symptome) bzw. „unauffällig". Ergänzt `smokingStatus` (Rauchanamnese) und `postTherapyComplication`. | CodeableConcept · 0..* | jeder Nachsorgetermin | per-encounter | Onkologe / Pneumologe / Pflege (supportiv) | {section: "Empf. 16.7 (EK, geprüft 2026); Kap. 16.5", recommendation_grade: "EK", evidence_level: "n/a"} |
| Körperliche Untersuchung Nachsorge | `physicalExaminationFinding` · followup (Kopie für surveillance) | Befund der körperlichen Untersuchung am Nachsorge-/Verlaufstermin (auffällig/unauffällig, Befundkategorien). | CodeableConcept · 0..* | jeder Nachsorge- bzw. Verlaufstermin | per-encounter | Onkologe / Pneumologe | followup: {section: "Empf. 16.7 (EK)"}; surveillance: {section: "Empf. 16.9 (EK)"}; grade EK, LoE n/a |
| Röntgen Thorax in der Nachsorge | `chestXrayFollowUp` · followup | Datum einer Röntgen-Thorax-Aufnahme als bildgebende Option des Nachsorgetermins (Tumorkinetik), wenn kein CT erfolgt. Hinweis: Hintergrundtext 16.3.3 bewertet das Röntgen als der LDCT unterlegen. SNOMED-Kandidat 399208008 (Plain chest X-ray). | dateTime · 0..* | Nachsorgetermin ohne CT, gemäß Nachsorgeplan | per-imaging-event | Radiologie | {section: "Empf. 16.7 (EK); Tab. 44 (Röntgen Thorax: Tumorkinetik)", recommendation_grade: "EK", evidence_level: "n/a"} |
| Sonografie Abdomen in der Nachsorge | `abdominalUltrasoundFollowUp` · followup | Datum einer Abdomensonographie als bildgebende Option des Nachsorgetermins (Leber-/Nebennierenmetastasen, paraaortale Lymphome). SNOMED-Kandidat 45036003 (Ultrasonography of abdomen). | dateTime · 0..* | Nachsorgetermin gemäß Nachsorgeplan | per-imaging-event | Radiologie / Pneumologie | {section: "Empf. 16.7 (EK); Tab. 44 (Abdomensonographie)", recommendation_grade: "EK", evidence_level: "n/a"} |
| CT Abdomen in der Nachsorge | `ctAbdomenFollowUp` · followup | Datum eines Abdomen-CT bei Verdacht auf oder zum Ausschluss abdomineller Metastasen; alternativ zur Sonografie gemäß Nachsorgeplan. | dateTime · 0..* | indikationsbezogen bzw. als CT-Option des Nachsorgetermins | per-imaging-event | Radiologie | {section: "Tab. 44 (Abdomen CT: Abdominelle Metastasen); Empf. 16.7 (EK)", recommendation_grade: "n/a (Indikationstabelle)", evidence_level: "n/a"} |
| Bronchoskopie in der Nachsorge | `bronchoscopyFollowUp` · followup | Datum einer Bronchoskopie in der Nachsorge; nur bei hohem Lokalrezidivrisiko (z.B. Manschettenresektion), nicht als Routine. | dateTime · 0..* | hohes Lokalrezidivrisiko (z.B. Manschettenresektion) | ad-hoc | Pneumologie | {section: "Tab. 44 (Bronchoskopie); Kap. 16.3.4", recommendation_grade: "n/a (Indikationstabelle)", evidence_level: "n/a"} |
| PET-CT in der Nachsorge | `petCtFollowUp` · followup | Datum eines PET-CT in der Nachsorge; indiziert ausschließlich zum Ausschluss von Metastasen vor erneutem thoraxchirurgischem Eingriff (kein Vorteil als Routine-Nachsorge, Kap. 6.3.1). | dateTime · 0..* | geplanter erneuter thoraxchirurgischer Eingriff bei Rezidiv/Zweittumor | ad-hoc | Nuklearmedizin / Radiologie / Thoraxchirurgie | {section: "Tab. 44 (PET-CT); Kap. 6.3.1", recommendation_grade: "n/a (Indikationstabelle)", evidence_level: "n/a"} |
| MRT Skelett bei Verdacht auf Knochenmetastasen | `skeletalMriFollowUp` · followup | Datum einer MRT zur Abklärung von Knochenmetastasen in der Nachsorge (symptomgetriggert). Alternative Modellierung: generisches `followUpImagingProcedure` mit Modalitäts- und Körperregions-Coding statt Einzelelementen. | dateTime · 0..* | klinischer Verdacht (Schmerz, Labor) | ad-hoc | Radiologie | {section: "Tab. 44 (MRT: Hirn- und Knochenmetastasen)", recommendation_grade: "n/a (Indikationstabelle)", evidence_level: "n/a"} |
| Laborparameter in der Nachsorge | `laboratoryTestFollowUp` · followup | Laboruntersuchung am Nachsorgetermin „nach Maßgabe des Behandlers" (Panel/Parameter als Coding); Tumormarker sind in der Nachsorge ausdrücklich nicht empfohlen und dürfen nicht als Routinewert erfasst werden. | CodeableConcept · 0..* | nach Maßgabe des Behandlers (z.B. Pneumonitis-, Toxizitätsverdacht) | ad-hoc | Onkologe / Pneumologe | {section: "Tab. 44 (Laborparameter); Kap. 16.3.4 (Tumormarker nicht empfohlen, LoE 1a)", recommendation_grade: "n/a (Indikationstabelle)", evidence_level: "n/a"} |
| Übergang in Screeningprogramm | `screeningProgramEnrolment` · followup | Dokumentation, dass die Patientin/der Patient nach Abschluss des 5. Nachsorgejahres in ein (LDCT-)Lungenkrebs-Früherkennungsprogramm eingeschlossen wurde (Datum/Status). Intervall des Programms nicht Teil der S3-Nachsorgeempfehlung (UNSICHER, ob jährlich). | dateTime · 0..1 | Ende des 5. Nachsorgejahres | once | Onkologe / Pneumologe / Hausarzt | {section: "Empf. 16.7 (EK, geprüft 2026); Kap. 5.1.5", recommendation_grade: "EK", evidence_level: "n/a"} |
| Sozialberatung angeboten/vermittelt | `socialCounsellingReferral` · followup + surveillance | Erkannter Bedarf an Sozialberatung (sozialrechtliche, berufliche, finanzielle Fragen) und erfolgte Vermittlung an Sozialdienst/Krebsberatungsstelle. | CodeableConcept · 0..1 | Bedarf im Nachsorge-/Verlaufsplan erkannt; Erstvorstellung | ad-hoc | Sozialdienst / Onkologe | {section: "Empf. 16.1/16.2 (EK: Bedarf an Sozialberatung erkennen); Empf. 8.77 (EK, geprüft 2026)", recommendation_grade: "EK", evidence_level: "n/a"} |
| Rehabilitation eingeleitet | `rehabilitationReferral` · followup | Status der onkologisch-pneumologischen Rehabilitation (AHB/Reha beantragt, angetreten, abgelehnt; ambulant/stationär) nach OP oder eingreifender Therapie mit Folgestörungen. Kap. 15 ist in 5.1 ausgesetzt — Referenz als vorläufig kennzeichnen. | CodeableConcept · 0..1 | Therapieabschluss (OP, RCT) mit Folgestörungen; Erstvorstellung | once-per-treatment-completion | Lead-Clinician / Sozialdienst | {section: "Empf. 15.5 (D, ausgesetzt 2026); Empf. 8.77 (EK)", recommendation_grade: "EK (8.77) / D (15.5, ausgesetzt)", evidence_level: "n/a"} |
| Strukturierter Verlaufsplan (Stadium IV) | `structuredSurveillancePlan` · surveillance | Vorhandensein eines strukturierten Verlaufs-/Follow-up-Plans unter Systemtherapie im Stadium IVA/IVB, der Progression/Rezidive, Zweitkarzinome, Komplikationen/Toxizitäten sowie Bedarf an Psychoonkologie, Palliativmedizin und Sozialberatung adressiert. | boolean · 1..1 | Beginn der Systemtherapie im Stadium IVA/B; Aktualisierung bei Linienwechsel | per-line | Onkologe | {section: "Empf. 16.2 (EK, geprüft 2026)", recommendation_grade: "EK", evidence_level: "n/a"} |
| Basisevaluation nach Abschluss der Induktion | `postInductionEvaluationDate` · surveillance | Datum der Evaluation von Ansprechen, Nebenwirkungen und Beschwerdebild einen Monat nach Abschluss der (Induktions-)Behandlung, mit Anamnese, körperlicher Untersuchung und CT Thorax/Abdomen/Becken. | dateTime · 0..1 | 1 Monat nach Abschluss der Induktionstherapie | once-per-line | Onkologe | {section: "Empf. 16.9 (EK, geprüft 2026)", recommendation_grade: "EK", evidence_level: "n/a"} |
| Verlaufstermin unter Erhaltungstherapie | `surveillanceVisitDate` · surveillance | Datum der festgelegten Wiedervorstellung unter laufender Erhaltungstherapie (mindestens alle 3–6 Wochen). | dateTime · 0..* | laufende Erhaltungstherapie NSCLC/SCLC | Q3-6W | Onkologe | {section: "Empf. 16.9 (EK, geprüft 2026)", recommendation_grade: "EK", evidence_level: "n/a"} |
| Anamnese-Befund unter Systemtherapie | `surveillanceAnamnesisFinding` · surveillance | Beschwerdebild/Symptome am Verlaufstermin (Anamnese) als Basis der Toxizitäts- und Progressbewertung; ergänzt CTCAE-Elemente. | CodeableConcept · 0..* | jeder Verlaufstermin | per-encounter | Onkologe / Pflege | {section: "Empf. 16.9 (EK)", recommendation_grade: "EK", evidence_level: "n/a"} |
| Standardisiertes Symptomassessment (Systemtherapie) | `symptomAssessmentInstrumentSurveillance` · surveillance | Eingesetztes standardisiertes Symptomassessment-Instrument unter Systemtherapie (z.B. MIDOS/ESAS/IPOS) zur bedarfsorientierten Integration der Palliativversorgung; Spezialisierung des palliativen Elements. | CodeableConcept · 0..* | regelmäßig unter Systemtherapie Stadium IV | per-encounter | Onkologe / Palliativ-Team | {section: "Statement 8.6 (EK, modifiziert 2026); Empf. 16.2 (EK)", recommendation_grade: "EK", evidence_level: "n/a"} |

### 4.2 Änderungen an Bestandselementen

| Element | Änderung |
| --- | --- |
| alle 25 S3-referenzierenden YAMLs | `evidence.guideline_references[].version` → `5.1 (Juli 2026, AWMF 020-007OL)`; URL kann bleiben (optional direkter PDF-Link `…/Version_5/S3_LL_Lungenkarzinom_Langversion_5.1.pdf`) |
| `structuredFollowUpPlan`, `followUpInterval`, `brainMriHighRisk`, `recurrenceOrSecondPrimary`, `ctThoraxFinding`, `recistResponse`, `restagingImagingDate` | `recommendation_grade: B → EK`; `section`: „(B, geprüft 2025)"/„(B, modifiziert 2025)" → „(EK, geprüft 2026)"; `ctThoraxFinding` zusätzlich Tab. 42 → Tab. 44 |
| `firstFollowUpVisitDate` | `section: "Empf. 16.4 (EK) / 16.5 (A/B, LoE 2), geprüft 2026"`; `recommendation_grade: EK` (Hauptbeleg 16.4) oder A/B mit Trigger-Split „≤ 8 Wochen; bei NSCLC III nach RT: soll"; `evidence_level: 2` nur für den 16.5-Anteil |
| `postTherapyComplication` | `evidence_level: 1a → 2`; `recommendation_grade: A → A/B`; Trigger um Population (OP I–III, RT/RCT I–II; NSCLC III nach RCT) ergänzen |
| `ctThoraxScan` | Referenz aufteilen: (1) Tab. 44 + Empf. 16.7 (EK) für den Nachsorge-Rhythmus (CT als eine der Optionen), (2) Empf. 16.6 (A, LoE 2) nur für das einmalige CT bei NSCLC III vor Durvalumab (optional eigenes Element `ctThoraxPostRadiochemotherapy`, once); `frequency_pattern` bleibt, Trigger-Text „Tab. 12 Onkopedia" kennzeichnen als Intervallquelle |
| `smokingStatus` | zusätzliche Referenz `Empf. 4.2 (A, LoE 1, modifiziert 2026)` als Primärbeleg; 16.3 LoE 2b → 3; Trigger „bei jeder Vorstellung (opt-out, bei Erstkontakt und wiederholt im Verlauf)"; `definition_de` Verweis „v5.01" → „v5.1"; „verwandte Produkte" als Coding-Prüfauftrag |
| `tobaccoCessationCounselling` | zusätzliche Referenzen `Empf. 4.3 (A, 1)` (ABC, DiGA) und `Empf. 4.4 (A, 1)` (Pharmakotherapie); 16.3 LoE 2b → 3; `instruction_de`: G-BA-Erstattung NET/Vareniclin seit 20.08.2025 (Fagerström ≥ 6 bzw. tabakassoziierte chronische Lungen-/Herzerkrankung) |
| `brainMriHighRisk` | Trigger: „EGFR+, ALK+, ROS1+, Adenokarzinom Stadium III; nach Maßgabe des interdisziplinären Teams"; `frequency_pattern` als Onkopedia-/Zentrumsvorgabe kennzeichnen (S3 ohne Intervall) |
| `brainMriUnderTherapy` | zweite Referenz `Empf. 16.9 (EK)` („MRT Schädel bei Verdacht auf Hirnmetastasen") |
| `followUpInterval` | Wert `Q12M-PostY5` im Value-Set-Kommentar als „Screeningprogramm; Intervall nicht aus S3-LL" kennzeichnen |
| `psychoOncologyReferral` | Phase auch `surveillance` (Empf. 16.2) oder Zweitelement; Referenzen `Empf. 16.2 (EK)`, `Empf. 8.77 (EK, geprüft 2026)`, `Kap. 11 (Verweis S3-LL Psychoonkologie)` |
| `distressThermometerScore` | Hinweis-Referenz `Kap. 11 (Verweis auf S3-LL Psychoonkologie — Screening)`; S3-Lung nennt kein Instrument |
| `earlyPalliativeReferral` | Referenz `Statement 8.6 (EK, modifiziert 2026)` und `Empf. 16.2 (EK)` in den `evidence`-Block aufnehmen (derzeit nur in `definition_de` erwähnt) |
| `pulmonaryFunctionTest`, `fev1PercentPredicted`, `dlcoPercentPredicted` | `section: Tab. 42 → Tab. 44`; `recommendation_grade: EK → n/a` (Indikationstabelle) |
| `immuneRelatedAdverseEvent` | `section: "Kap. 16.3 (Einleitung: immun-bezogene Komplikationen); Kap. 16.3.1"`; `evidence_level: 1b → n/a` |
| `restagingImagingDate` | Körperregion ergänzen (Thorax/Abdomen/Becken, z.B. als `bodySite`-Coding) oder `definition_de` präzisieren „CT-Thorax/Abdomen/Becken" |
| `ecogPerformanceStatusSurveillance` | `section` präzisieren: „Empf. 16.9 (EK; Beschwerdebild/körperliche Untersuchung — ECOG nicht explizit)" |
| `survivorshipCarePlan` | keine S3-Referenz ergänzen; optional Kommentar „S3-LL Lungenkarzinom 5.1: keine Empfehlung, Survivorship nur Forschungsbedarf (Kap. 16.3)" |

### 4.3 Dokumentationsänderungen (ohne Elementbezug)

`README.md` Z. 233, `docs/methodology.md` Z. 215/233: Versionsstring, Streichung „Aufwertung EK→B", „Tab. 42" → „Tab. 44", Hinweis „Kap. 15 ausgesetzt 2026". `GLOSSARY.md`: „v5.01" → „v5.1" (17 Stellen), Z. 182–185 „Empf. 16.7 (B)" → „(EK)". `docs/audit-log.md`: neuer Abschnitt (z.B. §14) als Erratum zu §8 (Grad-Rückkorrektur, Versionsablösung), §13 Limitationen um „Konsultationsfassungen sind nach Finalisierung nicht mehr abrufbar" ergänzen. `derived/fhir-logical-model/` und `catalog/*` nach dem Validator-Lauf regenerieren.

## 5 Bewertung der Kliniker-Kandidaten (gegen Empf. 16.7/16.9 und Tab. 44 der Langversion 5.1)

| Kandidat | Phase | Bewertung | S3-Referenz (5.1) | Repo-Status | Hinweis |
| --- | --- | --- | --- | --- | --- |
| Anamnese | follow-up | **ja** | Empf. 16.7 (EK): „dezidierte Anamnese" an jedem Nachsorgetermin | MISSING → § 4.1 `followUpAnamnesisFinding` | Rauchanamnese bereits über `smokingStatus` (4.2, A) |
| Körperliche Untersuchung | follow-up | **ja** | Empf. 16.7 (EK) | MISSING → `physicalExaminationFinding` | — |
| Röntgen Thorax | follow-up | **bedingt** | Empf. 16.7 (EK) nennt es als eine von drei Optionen („Röntgen Thorax, Sonografie Abdomen oder CT"); Tab. 44 „Tumorkinetik" | MISSING → `chestXrayFollowUp` | Hintergrund 16.3.3: Röntgen „nicht die relevante Untersuchung", LDCT-Evidenz; Onkopedia Tab. 12 plant CT → als Alternative modellieren, nicht als Standard |
| Sonografie Abdomen | follow-up | **bedingt** | Empf. 16.7 (EK, Option); Tab. 44 (Leber-/Nebennierenmetastasen, paraaortale Lymphome) | MISSING → `abdominalUltrasoundFollowUp` | — |
| Bronchoskopie | follow-up | **bedingt** (nur hohes Lokalrezidivrisiko, z.B. Manschettenresektion) | Tab. 44; 16.3.4 (intensive Nachsorge mit Bronchoskopie ohne Überlebensvorteil) | MISSING → `bronchoscopyFollowUp` (ad hoc) | keine Routine |
| PET-CT | follow-up | **nein als Routine / bedingt** (nur vor erneuter Thoraxchirurgie) | Tab. 44; Kap. 6.3.1 (kein Vorteil vs. KM-CT in 2-Jahres-Nachsorge) | MISSING → `petCtFollowUp` (ad hoc) | — |
| Abdomen-CT | follow-up | **bedingt** | Tab. 44 (abdominelle Metastasen); 16.7 „CT-Untersuchungen" als Option | MISSING → `ctAbdomenFollowUp` | — |
| Laborparameter | follow-up | **bedingt** („nach Maßgabe des Behandlers") | Tab. 44; 16.3.4: Tumormarker nicht empfohlen (LoE 1a) | MISSING → `laboratoryTestFollowUp` (ad hoc, ohne Tumormarker) | — |
| Anamnese | surveillance | **ja** | Empf. 16.9 (EK) | MISSING → `surveillanceAnamnesisFinding` | — |
| Körperliche Untersuchung | surveillance | **ja** | Empf. 16.9 (EK) | MISSING → `physicalExaminationFinding` (phase surveillance) | — |
| CT-Thorax | surveillance | **ja** | Empf. 16.9 (EK): Basis-CT 1 Monat nach Abschluss, danach CT alle 6–9 Wochen; Kap. 16.4 | PARTIAL `restagingImagingDate` (Region nicht differenziert) | Region ergänzen (§ 4.2) |
| CT-Abdomen | surveillance | **ja** | Empf. 16.9 „CT-Thorax/Abdomen/Becken"; Kap. 16.4 | PARTIAL (dto.) | — |
| CT Becken | surveillance | **ja** | Empf. 16.9; Kap. 16.4 („CT Abdomen/Becken") | PARTIAL (dto.) | — |
| Survivorship Care Plan / Abschlussbericht | Übergabe | **nein** (keine S3-Empfehlung) | nächstliegend Empf. 16.1 (EK, strukturierter Nachsorgeplan); „Survivorship" nur Forschungsbedarf (16.3/16.3.1) | COVERED `survivorshipCarePlan` (AG LONKO / Klein 2026 / OCP) | Fremdquellen beibehalten; sektorenübergreifende Formulierung 2024 aus 16.1 gestrichen |
| Impfstatus | Übergabe | **nein** | 0 Treffer „Impf" in 5.1; Kap. 12 verweist auf S3-LL Supportive Therapie (Themenliste ohne Impfungen) | MISSING | mögliche Quellen STIKO/Onkopedia „Impfungen" — nicht geprüft (UNSICHER) |
| Medikationsplan | Übergabe | **nein** | 0 Treffer | MISSING | Rechtsgrundlage bundeseinheitlicher Medikationsplan (§ 31a SGB V) außerhalb der LL |
| Kontaktdaten Mitbehandler | Übergabe | **nein** (nur indirekt) | Kap. 7.3.2 Hintergrund („Bei Bedarf sind entsprechende Kontakte zu vermitteln"); Empf. 8.77 (EK); Kap. 11 → S3-LL Psychoonkologie „sektorenübergreifende Koordination" | MISSING | eher FHIR `CareTeam`/Verwaltungsdatum als klinisches Datenelement |
| Arbeitsunfähigkeit | Übergabe | **nein** (bedingt über Reha-Kontext) | „Arbeitsunfähig" nur in Karnofsky-Tabelle (Kap. 6.2); Kap. 15 (ausgesetzt): sozialmedizinische Beurteilung, „Reha vor Rente", berufsfördernde Leistungen | MISSING | Quelle wäre DRV/BAR-Rahmenempfehlung; Element nur mit `rehabilitationReferral`-Kontext sinnvoll |

## 6 Versions-Pin-Empfehlung

**Neuer Versionsstring** für `evidence.guideline_references[].version` in allen 25 YAMLs (Ersatz für `5.01 (Konsultationsfassung 04/2026, AWMF 020-007OL)`):

```
5.1 (Juli 2026, AWMF 020-007OL)
```

Quellenliste (`README.md` Z. 233, `docs/methodology.md` Z. 233, `GLOSSARY.md`): „S3-Leitlinie Lungenkarzinom, Langversion **5.1** (Juli 2026, final; AWMF 020-007OL) — löst die Konsultationsfassung 5.01 (04/2026, Konsultation 03.04.–02.05.2026) und die Erstfassung 5.0 (Juni 2026) ab; 5.0 → 5.1 nur Arzneimittelzulassungen (Lurbinectedin, Tarlatamab) und URL-Korrekturen, Kap. 15/16 unverändert. Kap. 4.2 (Empf. 4.1–4.5, A/1, modifiziert/neu 2026), Kap. 15 (ausgesetzt 2026), Kap. 16 (Empf. 16.1–16.9, geprüft 2026; 16.1/16.2/16.4/16.7/16.8/16.9 EK, 16.3 B/3, 16.5 A/B/2, 16.6 A/2), **Tab. 44** (Nachsorge-Indikationen), Tab. 48 (Änderungsübersicht v5). Zitierweise nach Kap. 1.5." Die Kurzversion zur Version 5 ist nicht publiziert und darf nicht zitiert werden. Für die Konsultationsgeschichte den Leitlinienreport 5.0 (Juni 2026) als Beleg führen.

**Welche Referenzen sich über den Versionsstring hinaus ändern:**

| Änderungstyp | Elemente |
| --- | --- |
| Nur Versionsstring | `brainMriFinding`, `adverseEventCtcae`, `adverseEventCtcaeGrade`, `ecogPerformanceStatusSurveillance`, `systemicTherapyRegimen`, `qolEortcQlqC30`, `therapyLineNumber`, `psychoOncologyReferral` (+ optionale Zusatzreferenzen), `brainMriUnderTherapy` (+ optional 16.9) — 9 Elemente |
| Grad B → EK, Stempel „geprüft 2026" | `structuredFollowUpPlan`, `followUpInterval`, `brainMriHighRisk`, `recurrenceOrSecondPrimary`, `ctThoraxFinding`, `recistResponse`, `restagingImagingDate` — 7 Elemente |
| Grad/LoE-Umstellung (1a→2, 2b→3; B/1a → EK + A/B/2) | `firstFollowUpVisitDate`, `postTherapyComplication`, `ctThoraxScan`, `smokingStatus`, `tobaccoCessationCounselling` — 5 Elemente (bei `smokingStatus`/`tobaccoCessationCounselling` zusätzlich Empf. 4.2 bzw. 4.3/4.4 als A/1-Referenzen) |
| Tabellennummer Tab. 42 → Tab. 44 | `ctThoraxFinding`, `ctThoraxScan`, `pulmonaryFunctionTest`, `fev1PercentPredicted`, `dlcoPercentPredicted` — 5 Elemente (Lungenfunktions-Trio zusätzlich Grad EK → n/a) |
| Sektionstext präzisieren | `immuneRelatedAdverseEvent` (16.3 statt 16.3.1; LoE n/a), `ecogPerformanceStatusSurveillance` |
| Nicht betroffen | Elemente mit Quellen S3-LL Palliativmedizin 3.01 (Konsultationsfassung 03/2026 — ebenfalls auf Finalisierung zu prüfen, außerhalb dieses Auftrags), Onkopedia, OCP, AG LONKO |

Empfohlener Ablauf: `data-element-analyzer`-Lauf mit der 5.1-PDF als Eingabe → datenelementweise Bestätigung → `data-element-validator` (Patches, Schema, Katalog/FSH-Regeneration) → Audit-Log-Erratum zu §8.

## Anhang — Fundstellen in der Langversion 5.1 (Seitenzahlen der Druckpaginierung)

Kap. 1.5 Zitierweise S. 11 · Kap. 1.6 Versionsänderungen S. 12 · Kap. 1.9 Weitere Dokumente S. 13 · Kap. 2.1.3 Gültigkeit S. 29 · Kap. 2.2 Methodik/Tab. 4–6 S. 29–31 · Empf. 3.1 S. 33 · Kap. 4.2 / Empf. 4.1–4.5 S. 61–65 · Kap. 6.3.1 PET/CT-Nachsorge-Hinweis (Staging-Abschnitt) · Kap. 7 Empf. 7.1–7.10 S. 190–199 · Statement 8.6 (vor Tab. 31, S. 206) · Empf. 8.77/8.78 Kap. 8.6.1 S. 287 f. · Kap. 11 S. 469 f. · Kap. 12 S. 471 · Kap. 15 / Empf. 15.1–15.5 S. 487–490 · Kap. 16 S. 491–500 (Empf. 16.1/16.2 S. 492, 16.3 S. 493, 16.4–16.6 S. 497, 16.7/16.8 S. 498, 16.9 + Tab. 44 S. 499, 16.5/16.6 S. 500) · Kap. 18 QI/Tab. 45 S. 504 · Kap. 19.3 / Tab. 48 S. 518 ff.
