# Dossier: Quellen und Datenelement-Kandidaten für die Screening-Episode

**Lungenkrebs-Früherkennung mit Niedrigdosis-CT (LuKrFrühErkV / KFE-RL) – Phase `screening` des MiHUB-Datenelement-Katalogs**

| | |
|---|---|
| Stand | Quellenprüfung 14.10.2026 · Synthese 15.10.2026 |
| Status | Arbeitsmaterial für die Erhebung 2026-10; kein Katalog-Inhalt |
| Entstehung | KI-gestützte Multi-Agenten-Recherche (Claude Code, Opus 5.5; siehe `AI_USAGE.md`): sechs Recherche-Perspektiven, Konsolidierung, Gegenprüfung durch zwei Skeptiker je Kandidat, Synthese; Methode im Anhang |
| Repositorien (nur gelesen) | data-elements: Branch feat/guideline-resync-terminology-primarycare, Commit c4fb886 (112 Elemente; Stand vor bzw. während der Zweitprüfung vom 14.10.2026) · mihub-lung-cancer-pathway: Branch dev, HEAD 4e8f494, Screening-Modell zuletzt geändert in ac7e9c2 |
| Begleitdateien | [`datenelement-erhebung-screening.xlsx`](datenelement-erhebung-screening.xlsx) (vorbefüllte Erhebungsmappe, Zeilen DE-S01 … DE-S53 = Einzelblätter Nr. 1–53) · [`quellen.json`](quellen.json) (Quellen mit Verifikation und zitierenden Kandidaten) |

> **Nachtrag 2026-10-15:** Für alle 53 Kandidaten liegen jetzt YAML-Entwürfe mit MII-TermServ-geprüften Codes und Profilzielen über alle Standards vor ([`entwuerfe/`](entwuerfe/), Prüfprotokoll [`pruefprotokoll.json`](pruefprotokoll.json)). Die Code-Angaben in den Einzelblättern unten sind der Stand der Recherche (tx.fhir.org); maßgeblich sind die Entwürfe.

## Kurzfassung

- **Recherche:** sechs Perspektiven (Recht 45 Kandidaten/15 Quellen · Leitlinien 30 Kandidaten/12 Quellen · Befundung 70 Kandidaten/28 Quellen · Standards 45 Kandidaten/31 Quellen · Evidenz 45 Kandidaten/33 Quellen · Prozess 74 Kandidaten/26 Quellen), zusammen 309 Kandidaten.
- **Konsolidierung:** 77 deduplizierte Kandidaten in 13 Prozessgruppen (G1–G13) und 40 Quellen; 38 der 77 waren als „Pflicht nach Norm“ markiert.
- **Gegenprüfung:** je Kandidat ein Quellen- und ein Dubletten-/Scope-Skeptiker. **53 Kandidaten behalten** (beide Urteile „nicht widerlegt“), **24 verworfen**: 21 nur durch den Dubletten-/Scope-Skeptiker, 1 nur durch den Quellen-Skeptiker, 2 durch beide. Konfidenz der Urteile zu den behaltenen Kandidaten: 0,50 bis 0,92 (Mittel 0,73).
- **Verbindlichkeit nach Gegenprüfung** (behaltene Kandidaten): 16 Pflicht, 1 Pflicht (Information) / Leitlinie (Angebot), 1 Soll-Vorschrift, 7 bedingt, 6 mittelbar, 13 Leitlinie, 9 keine. Von den 29 in der Konsolidierung als Pflicht markierten bleiben 15 Pflicht; 7 sind bedingt, 5 mittelbar, 1 Soll-Vorschrift, 1 geteilt (Information Pflicht, Angebot Leitlinie). Von den 24 übrigen wurde ldctReferral als Pflicht (BMV-Ä § 13 Abs. 4) und smokingStatusScreening als mittelbar eingestuft.
- **Alle 53 behaltenen Kandidaten tragen Auflagen** aus der Gegenprüfung (Fundstellen, Datentypen, Codes). 10 sollen ein Bestandselement spezialisieren (u. a. smokingStatus, referralOrder, ctThoraxScan), 2 den neuen Kandidaten incidentalFinding; mehrere sollen als Attribut oder Teil eines anderen Elements umgesetzt werden (Abschnitt 5.3).
- **Codes:** 61 Codes an 44 Kandidaten (snomed-ct 34, loinc 10, ebm 6, dicom-dcm 3, ncit 3, kdl 2, radelement 2, openehr-archetype 1); 15 davon aus Systemen, die das Prüfskript des Repos nicht kennt. Gegen den MII-TermServ hat nur der Dubletten-Skeptiker der Gruppe 10 Codes geprüft.
- **Wichtigste Entscheidungen** (Abschnitt 7): Konsumabschnitte oder Jahresdurchschnitt (E1), Unterbrechungsregel und Rauchstopp (E2), Rechenweg der Packungsjahre (E3), PLCOm2012 nur optional (E4), Lung-RADS neben den §-Kategorien (E12), Zufallsbefunde (E14), Registerdaten nach § 7 und Monitoring (E18), Einwilligungen (E19), Phase und Quellen-Enum im Schema (E21–E23).

## 1 Zweck und Abgrenzung der Episode

### 1.1 Zweck

Das Dossier bereitet die neue Versorgungsphase `screening` im Datenelement-Katalog vor. Es hält fest, welche Quellen welche Daten fordern oder empfehlen, welche Kandidaten die Gegenprüfung überstanden haben, wie sie im Repository umgesetzt werden können und was die klinischen Fachleute vor der Erhebung entscheiden müssen. Es ist Arbeitsmaterial, kein Katalog-Inhalt. Die Repositorien wurden nur gelesen.

Gegenstand ist die Lungenkrebs-Früherkennung mit Niedrigdosis-CT (LDCT) für rauchende und ehemals rauchende Personen. Rechtsgrundlagen sind die Lungenkrebs-Früherkennungs-Verordnung (LuKrFrühErkV, in Kraft seit 01.07.2024) und Abschnitt D.III der Krebsfrüherkennungs-Richtlinie (KFE-RL, §§ 37–46, in Kraft seit 12.03.2026). Abgerechnet wird nach EBM seit 01.04.2026. Ein organisiertes Programm mit Einladungswesen nach § 25a SGB V gibt es nicht (S3-LL Kap. 5.1.4.9).

### 1.2 Rückgrat: BPMN-Modell des Screening-Pfads

Rückgrat ist `models/lung-cancer-screening-pathway.bpmn` im Repository mihub-lung-cancer-pathway (Branch `dev`, HEAD 4e8f494; letzte inhaltliche Änderung des Modells in Commit ac7e9c2, Stand 2026-06-25). Das Modell hat drei Pools mit 26 Tasks:

| Pool / Lane | Tasks | Rolle in diesem Dossier |
|---|---|---|
| Versicherte / Zu untersuchende Person | 3 | Zugang, Vorlage der Überweisung, Entscheidung; Portal-Selbstauskunft |
| Arbeitsmedizin / Allgemeinmedizin / Innere Medizin | 8 | Anspruchsprüfung, Raucheranamnese, Information, Bericht, Überweisung, Besprechung |
| Radiologische Praxis / Klinik (Lanes Erstbefunder, Zweitbefunder) | 15 | Indikation, Aufklärung, LDCT, Befundung, Ergebnis, Mitteilung, Qualitätsdaten |

Dazu kommen 5 Start-, 7 End- und 4 Zwischenereignisse, 14 Gateways, 8 Nachrichtenflüsse und 13 Textannotationen. Die Episode beginnt mit der Aufforderung durch die Praxis (Event_0qh7lu0) oder aus Eigeninitiative (Event_1hd295c). Sie endet mit „Teilnahme nicht möglich“, „Untersuchung abgeschlossen“, „Beratung abgeschlossen“, „Screening beendet“ oder mit der Überweisung zur weiteren Behandlung (Event_0nesy5q, Übergang in die Diagnostik). Für die Zuordnung der Kandidaten hat die Konsolidierung die Schritte in 13 Prozessgruppen (G1–G13) gebündelt; Abschnitt 3 ordnet jedem BPMN-Schritt die Datenelemente zu.

### 1.3 Abgrenzung

**Im Scope** sind Daten je versicherter Person entlang der Episode: Aufforderung oder Eigeninitiative, Raucheranamnese und Zulässigkeit, Information und Entscheidung, Bericht und Überweisung, rechtfertigende Indikation und Aufklärung, LDCT, Erst- und Zweitbefundung, Ergebnis, Empfehlung und Mitteilung bis zum Austritt. Die Abklärung abklärungsbedürftiger Befunde (G12) ist ein Grenzfall: Das BPMN endet mit der Überweisung, die S3-LL zählt das Management abklärungsbedürftiger Befunde aber zum Programm (Tab. 16, Schritt 7). Deshalb bleiben drei Rückmelde-Elemente als Kandidaten mit Scope-Vorbehalt (Entscheidung E20).

**Nicht im Scope** (bewusst ausgeschlossen, Begründung in Abschnitt 5):

- Stammdaten werden nur per Verweis genutzt (z. B. birthYear mit vollständigem Geburtsdatum für das Alterskriterium).
- Struktur- und Organisationsdaten (Qualifikation nach § 6 LuKrFrühErkV, KV-Genehmigungen, Fallzahlen, Kooperationsvereinbarungen) gehören in ein Practitioner- bzw. Organization-Modul.
- Aggregierte Qualitätskennzahlen (§ 7 Abs. 2 LuKrFrühErkV, Quartalsbericht nach § 44 KFE-RL) sind Auswertungen, keine Datenelemente.
- EBM-Ziffern werden nur als Abrechnungsbezug an den Prozess-Elementen geführt.
- Risikomodelle (PLCOm2012) sowie Familien- und Berufsanamnese sind nicht Teil von Inkrement 1 (Entscheidung E4).
- Diagnostik und Therapie nach der Abklärung werden über bestehende Elemente referenziert (cancerDiagnosis, tnmStage, tumorHistology, tumorBoardDecision).
- Das DGUV-Angebot EVA-Lunge (berufliche Asbestexposition) ist ein eigener Zugangsweg außerhalb der GKV-Episode (offene Frage E11).

### 1.4 Bezug zur Arbeitsnotiz „Raucheranamnese und Eignungsprüfung“ (Stand 06.10.2026)

Die Arbeitsnotiz „Vorarbeiten für das Teilmodul Früherkennung: Raucheranamnese und Eignungsprüfung“ verweist auf die Entscheidungsvorlage Spezifikationsmodule (MiHUB A3.2, Entwurf 0.3 vom 06.10.2026). Dort ist die Raucheranamnese das Querschnittsmodul **Q3**, das Screening, Behandlung und Nachsorge gemeinsam nutzen. Das Teilmodul Screening ist **Inkrement 1 des Moduls M1**. ISiKRaucherStatus ist der Vorschlag für die Profilbasis (Entscheidung E5 der Vorlage). Die Vorlage selbst wurde in diesem Lauf nicht gelesen.

Zuordnung der behaltenen Kandidaten:

- **Q3 Raucheranamnese** (7 Kandidaten, Gruppe G2): `smokingStatusScreening`, `cigaretteConsumptionPeriod`, `cigarettesPerDayInPeriod`, `smokingInterruptionPeriod`, `otherTobaccoNicotineProductUse`, `creditableSmokingDurationYears`, `packYearsCalculated`.
- **M1 Inkrement 1 Screening** (46 Kandidaten, Gruppen G1, G3, G5–G12).

Das Dossier übernimmt die Grundsätze der Notiz: Maßgeblich sind die Definitionen der Verordnung, nicht die KV-Vorlagen (jahrweise Packungsjahre, Unterbrechungsregel, nur Zigaretten). Der Bericht nach § 2 Abs. 1 Nr. 3 ist das Zielartefakt (Composition). Der Status wird über LOINC 72166-2 mit der Antwortliste LL2201-3 geführt, SNOMED CT und NCIt dienen als Mapping. smokingStatus wird in die Phase Screening übernommen; sein Mapping-Ziel wird korrigiert.

Die Recherche ergänzt oder korrigiert die Notiz in fünf Punkten:

1. Die KBV PraxisInfoSpezial liegt in der Fassung Oktober 2026 vor; Abschnitt 3 der Notiz nennt noch März 2026 (Abschnitt 7.1 bereits Oktober).
2. Die NHS-URL der Notiz [18] liefert Version 3 vom 03.02.2025 (PR1646), nicht das Protokoll von 2019.
3. Abschnitt 7.1 der Notiz sagt, die Tragenden Gründe nennten das Kriterium „Zeit seit Rauchstopp“ nicht ausdrücklich. Die TrG vom 18.06.2025 (Abschn. 2.1, S. 3) nennen es: „wobei der Zigarettenkonsum noch andauert oder vor weniger als 10 Jahren beendet wurde“ (mit Fn. 7 auf die Unterbrechungsregel).
4. Ein über die tatsächlichen Rauchjahre gemittelter Tageskonsum ergibt rechnerisch dieselbe Packungsjahrsumme wie die jahrweise Rechnung, solange keine vollständige Unterbrechung von zehn oder mehr Jahren vorliegt (Gegenprüfung zu cigaretteConsumptionPeriod). Konsumabschnitte sind deshalb nur bei Unterbrechungen zwingend; für NELSON-Auswertungen und die Erinnerungsqualität bleiben sie sinnvoll (Entscheidung E1). Die Aussage der Notiz, ein Jahresdurchschnitt über die gesamte Rauchdauer „genügt der Definition nicht“, ist entsprechend zu präzisieren: Das Defizit der KV-Vorlagen liegt weniger in der Mittelung als darin, dass sie Unterbrechungen nicht erfassen (Ausschluss des Konsums vor einer Unterbrechung von zehn oder mehr Jahren, Mitzählen kürzerer Unterbrechungen nur bei der Dauer).
5. Den Kick-off von EC-LuC am 08./09.10.2026 (Abschnitt 7.3 der Notiz) belegten die JRC-Seiten am 14.10.2026 nicht (UNSICHER).

## 2 Quellenverzeichnis

40 Quellen stammen aus der Konsolidierung (IDs Q01–Q40), 14 wurden in der Gegenprüfung, aus der Arbeitsnotiz oder im Synthese-Schritt ergänzt (IDs X01–X14). „Verifikation“ gibt wieder, wie die Recherche die Quelle geprüft hat; „UNSICHER“ heißt: nur Abstract oder Sekundärquelle. Die letzte Spalte zählt die behaltenen Kandidaten, die die Quelle wörtlich zitieren (Fundstelle oder Zusatzbeleg), und getrennt davon die Kandidaten mit weiterem Bezug (Code- oder Mapping-Beleg, Nennung in Verbindlichkeit oder Umsetzung); die Namen stehen in `sources.json` (Felder `zitiert_von`, `bezug_von`).

### 2.1 Recht und untergesetzliche Normen (Deutschland), Vorlagen (17)

| ID | Quelle | Herausgeber | Fassung/Datum | URL | Verifikation | Relevanz | Kandidaten (Zitat · weiterer Bezug) |
|---|---|---|---|---|---|---|---|
| Q01 | Lungenkrebs-Früherkennungs-Verordnung (LuKrFrühErkV), §§ 1–8 und Anlage | BMUV; amtlicher Text gesetze-im-internet.de (BMJ/BfJ) | 15.05.2024, BGBl. 2024 I Nr. 162, in Kraft 01.07.2024; am 14.10.2026 ohne Änderungsvermerk | <https://www.gesetze-im-internet.de/lukrfr_herkv/BJNR0A20A0024.html> | Volltext gelesen (fünf Linsen; prozess: live, byte-identisch); Konsolidierung: §§ 1–7 und Anlage gegengelesen, Zitate maschinell geprüft | Primärnorm: Packungsjahr, Unterbrechung, Befundkategorien, Zulässigkeit, Doppelbefundung, QS, Technik/CAD | 19 · 13 |
| Q02 | Krebsfrüherkennungs-Richtlinie (KFE-RL), § 2, §§ 37–46, Anlage I | Gemeinsamer Bundesausschuss (G-BA) | zuletzt geändert 18.12.2025 (BAnz AT 11.03.2026 B4), in Kraft 12.03.2026 | <https://www.g-ba.de/downloads/62-492-4074/KFE-RL_2025-12-18_iK-2026-03-12.pdf> | PDF-Volltext von allen Linsen gelesen; Aktualität über g-ba.de/richtlinien/17 geprüft (recht); Konsolidierung: Zitate geprüft | Anspruch, Information, Indikation, Befundung, 14-Tage-Bericht, Einwilligung, Quartalsbericht, Monitoring 2028 | 21 · 18 |
| Q03 | Tragende Gründe: Einführung der Lungenkrebsfrüherkennung mittels Niedrigdosis-CT bei Rauchern | G-BA | Beschluss 18.06.2025 (in Kraft 05.09.2025) | <https://www.g-ba.de/downloads/40-268-11634/2025-06-18_KFE-RL_Einf-Lungenkrebsfrueherkennung-Niedrigdosis-CT-Raucher_TrG.pdf> | Volltext gelesen (recht, befundung, standards, prozess); Konsolidierung: rund 20 Zitate geprüft | Auslegung: nur Zigaretten, Aktualitätsrückfrage, ePA, Einwilligungen, Befundbericht, Monitoring | 13 · 6 |
| Q04 | Versicherteninformation Lungenkrebs-Früherkennung (Beschluss Anlage I, Broschüre, Tragende Gründe, Zusammenfassende Dokumentation) | G-BA | Beschluss 18.12.2025, in Kraft 12.03.2026; Broschüre Stand Dezember 2025 (PDF 29.01.2026) | <https://www.g-ba.de/downloads/39-261-7628/2025-12-18_KFE-RL_Lungenkrebsfrueherkennung-Versicherteninfo.pdf> | Beschluss vollständig, ZD auszugsweise (recht); Broschüre 17-98-6054 und TrG 40-268-12220 live gelesen (prozess) | Patientensicht/Portal: Ablauf, Packungsjahr-Formular, Warnsymptome, Entscheidungshilfe 0–10 | 7 · 0 |
| Q05 | PraxisInfoSpezial Lungenkrebs-Früherkennung mit Niedrigdosis-CT | Kassenärztliche Bundesvereinigung (KBV) | Stand Oktober 2026 (PDF 02.10.2026) | <https://www.kbv.de/documents/infothek/publikationen/praxisinfo/praxisinfospezial-lungenkrebs-frueherkennung.pdf> | Volltext gelesen (fünf Linsen; prozess: live identisch); Arbeitsnotiz zitiert noch Fassung März 2026 | Ablauf, Berichtsinhalt, Selbsterklärung, Rauchstopp < 10 J., Fachgruppen ab 01.10.2026, GOP | 7 · 3 |
| Q06 | EBM-Beschlüsse: Erweiterter Bewertungsausschuss 87. Sitzung (GOP 01871–01881) und Bewertungsausschuss 854. Sitzung | (Erweiterter) Bewertungsausschuss KBV/GKV-Spitzenverband | EBA 11.03.2026, Wirkung 01.04.2026; BA 854, Wirkung 01.10.2026 | <https://www.gkv-spitzenverband.de/media/dokumente/krankenversicherung_1/aerztliche_versorgung/verguetung_und_leistungen/beschluesse_ba_eba_de_eg/87_sitzung_eba/EBA_87_Lungenkrebsfrueherkennung.pdf> | Volltexte gelesen (recht; befundung/prozess, live identisch); Konsolidierung: GOP-Titel, Frequenzen, Zitate geprüft | Obligate Leistungsinhalte, Kontrollintervall in Monaten, 14-Tage-Fristen, Arztgruppen | 5 · 5 |
| Q07 | Vereinbarung zur Strahlendiagnostik und -therapie (§ 135 Abs. 2 SGB V), §§ 13e–13g NDCT | KBV und GKV-Spitzenverband (Anlage 3 BMV-Ä) | in der ab 01.04.2026 geltenden Fassung | <https://www.kbv.de/documents/infothek/rechtsquellen/bundesmantelvertrag/anlage-03-qualitaetssicherung/qs-vereinbarung-strahlendiagnostik.pdf> | NDCT-Teile gelesen (recht, befundung, prozess; live byte-identisch) | Genehmigung, Dokumentationspflicht Erst-/Zweitbefund, 14-Tage-Bericht, Frequenzen | 2 · 3 |
| Q08 | Vorgaben der BÄK zu Fortbildungsmaßnahmen Lungenkrebsfrüherkennung gemäß § 43 KFE-RL | Bundesärztekammer | 1. Auflage, 12.12.2025 | <https://www.bundesaerztekammer.de/fileadmin/user_upload/BAEK/Themen/Aus-Fort-Weiterbildung/Fortbildung/20251212_Vorgaben_BAEK_FB_Lungenkrebs-Screening_gem.____43_KFE-RL.pdf> | Volltext (11 S.) gelesen (recht; befundung über dieselbe Kopie) | Angekündigte Berichtsvorlage, V-Lung-RADS als Fortbildungsschema | 0 · 1 |
| Q09 | Strahlenschutzgesetz §§ 5, 83–85 und Strahlenschutzverordnung §§ 119, 124, 127 | Bund, gesetze-im-internet.de | geltende Fassungen, Abruf 14.10.2026 | <https://www.gesetze-im-internet.de/strlschg/__85.html> | Einzelnormen als HTML gelesen (recht, prozess; live identisch); Konsolidierung: Zitate geprüft | Asymptomatik, rechtfertigende Indikation, Aufzeichnung, Befragung, Strahlenrisiko | 3 · 3 |
| Q10 | Bürgerliches Gesetzbuch § 630e (Aufklärungspflichten) | Bund, gesetze-im-internet.de | Abruf 14.10.2026 | <https://www.gesetze-im-internet.de/bgb/__630e.html> | Seite gelesen (prozess, live identisch); Zitat geprüft | Aufklärung vor LDCT durch Erstbefunder, Abschriften | 0 · 1 |
| Q11 | KV-Berichtsvorlagen: KVBW 'Bericht Lungenkrebs-Screening' und KVBB 'Musterbericht – Hinweise' | KV Baden-Württemberg; KV Brandenburg | KVBW Juni 2026; KVBB Mai 2026 | <https://www.kvbawue.de/api-file-fetcher?fid=5382> | Beide PDFs live abgerufen und gelesen (prozess); Zitate geprüft | De-facto-Mindestfelder des Berichts; Formfreiheit | 2 · 0 |
| X01 | Bundesmantelvertrag-Ärzte (BMV-Ä), § 13 Abs. 4 (Überweisungsvorbehalt) und § 24 Abs. 4 Nr. 4 | KBV und GKV-Spitzenverband | Fassung vom 01.04.2026 (Änderung vom 04.03.2026 gesondert geprüft) | <https://www.kbv.de/documents/infothek/rechtsquellen/bundesmantelvertrag/bmv-aerzte.pdf> | Volltext gelesen (Gegenprüfung, Quellen- und Dubletten-Skeptiker) | Überweisung zur LDCT und zur Zweitbefundung als GKV-Pflicht (ldctReferral, secondReadingRequest) | 1 · 1 |
| X02 | Bürgerliches Gesetzbuch §§ 630d (Einwilligung) und 630f (Dokumentation) | Bund, gesetze-im-internet.de | Abruf 14.10.2026 | <https://www.gesetze-im-internet.de/bgb/__630f.html> | Einzelnormen gelesen (Gegenprüfung); ergänzt Quelle Q10 (§ 630e) | Einwilligung vor der LDCT und deren Dokumentation (ldctInformedConsent, participationDecision) | 1 · 1 |
| X03 | G-BA-Versicherteninformation in Leichter Sprache „Lungen-Krebs früh erkennen“ | G-BA | 25.06.2026 (PDF 17-98-6130, 14 S.) | <https://www.g-ba.de/downloads/17-98-6130/2026-06-25_G-BA_VI_Lungenkrebsfrueherkennung_LS.pdf> | PDF abgerufen (Gegenprüfung); Link auf der G-BA-Themenseite im Synthese-Schritt bestätigt | Format der Aushändigung; offen, ob die Fassung Anlage I ersetzt (patientInformationLeafletProvided) | 0 · 1 |
| X04 | Arzneimittel-Richtlinie § 14a (Arzneimittel zur Tabakentwöhnung) | G-BA | Beschluss 15.05.2025, BAnz AT 19.08.2025 B1 | nicht dokumentiert (lokale Kopie der Gegenprüfung: screening/sources/skeptiker-quelle/k24-31/amrl-14a-beschluss.pdf) | Volltext gelesen (Gegenprüfung); Original-URL nicht festgehalten | Fagerström-Wert ≥ 6 als Erstattungsvoraussetzung (verworfen: nicotineDependenceScore) | 0 · 0 |
| X05 | KVBB-Musterbericht zur Aushändigung (Lungenkrebs-Früherkennung) | KV Brandenburg | PDF vom 12.05.2026 | <https://www.kvbb.de/fileadmin/user_upload/pdf/Genehmigungspflichtige_Leistungen/Lungenkrebs-Frueherkennung/Musterbericht_LDCT.pdf> | PDF gelesen (Gegenprüfung); ergänzt Quelle Q11 | Ankreuzfelder des Berichts (Kriterien, Lungenkrebs bekannt, Überweisung gewünscht, Selbsterklärung) | 3 · 0 |
| X06 | G-BA-Beschluss Mammographie-Screening (Widerspruchsrecht) | G-BA | Beschluss 16.10.2025, BAnz AT 15.01.2026 B2 | nicht dokumentiert | nur in einer Gegenprüfung erwähnt, URL und Wortlaut nicht dokumentiert = UNSICHER | Vorbild Widerspruch statt Einwilligung für ein künftiges Monitoring (screeningDataUseConsent) | 0 · 0 |

### 2.2 Leitlinien, Positionspapiere und Statements (8)

| ID | Quelle | Herausgeber | Fassung/Datum | URL | Verifikation | Relevanz | Kandidaten (Zitat · weiterer Bezug) |
|---|---|---|---|---|---|---|---|
| Q12 | S3-Leitlinie Prävention, Diagnostik, Therapie und Nachsorge des Lungenkarzinoms, Langversion | Leitlinienprogramm Onkologie (DKG, DKH, AWMF), AWMF 020-007OL | 5.1, Juli 2026 | <https://www.leitlinienprogramm-onkologie.de/fileadmin/user_upload/Downloads/Leitlinien/Lungenkarzinom/Version_5/S3_LL_Lungenkarzinom_Langversion_5.1.pdf> | Volltext Kap. 3.7, 4.2, 5, 6.3/6.4 gelesen (alle Linsen); Konsolidierung: Empf. 4.5, 5.2–5.13 gegengelesen | Zielgruppe, Eignungsprofil, Entwöhnung, V-Lung-RADS, Befundmanagement, QS, Einwilligung | 17 · 12 |
| Q13 | S3-Leitlinie Rauchen und Tabakabhängigkeit: Screening, Diagnostik und Behandlung | AWMF (DGPPN, DG-Sucht), AWMF 076-006 | Versions-Nr. 3.1, 03/2021, gültig bis 31.12.2025 | <https://register.awmf.org/assets/guidelines/076-006l_S3_Rauchen-_Tabakabhaengigkeit-Screening-Diagnostik-Behandlung_2021-03.pdf> | Kap. 3.2, 3.3, 4.1 gelesen (prozess); Überarbeitungsstand nicht verifiziert | Rauchanamnese, Fagerström/HSI, Kurzberatung | 1 · 0 |
| Q14 | Onkopedia-Leitlinie Lungenkarzinom, nicht-kleinzellig (NSCLC), Kap. 2 und 3.2 | DGHO | Stand April 2025 | <https://www.onkopedia.com/de/onkopedia/guidelines/lungenkarzinom-nicht-kleinzellig-nsclc/@@guideline/html/index.html> | Lokaler Text gelesen (alle Linsen); Kap. 3.2 zum Programmstart veraltet | Kontext (Risiken, Berufskrankheiten), keine Datenvorgaben | 0 · 1 |
| Q15 | Whitepaper Identifikation, Information und Eignungsprüfung (Blum, Vogel-Claussen, Hoffmann et al.) mit Online-Supplement | Thieme, Pneumologie | 2026;80(5):375–384, online 14.10.2025, DOI 10.1055/a-2697-6434; Erratum e1 | <https://doi.org/10.1055/a-2697-6434> | Haupttext (PMC13314295) und Supplement (24 S., Bildseiten visuell) gelesen (leitlinien, prozess); Zitate geprüft | Eignungsprüfung, Prüfbericht-Vorlage, Packungsjahr-Rechner, Opt-out, Recall | 1 · 1 |
| Q16 | DRG/DGP/DGT-Positionspapier nationales LDCT-Programm mit Supplement; DGP-Positionspapier Tabakentwöhnung (Rupp et al.) | Thieme (Pneumologie, RöFo) | Pneumologie 2024;78(1):15–34 / RöFo 2024;196(2):134–153; Pneumologie 2024;78(9):612–619 | <https://www.thieme-connect.de/media/roefo/202402/supmat/roefo-21782846_10-1055-a-2178-2846-s.pdf> | Supplement im Volltext (befundung); Hauptartikel und Rupp nur Abstract = UNSICHER (leitlinien) | V-Lung-RADS-Regeln, Messregeln, Kategorienzuordnung, Nebenbefunde; Opt-out | 5 · 2 |
| Q17 | ERS/ESTS/ESTRO/ESR/ESTI/EFOMP statement on incidental findings from LDCT screening (O'Dowd et al.) | Eur J Cardiothorac Surg (parallel Eur Respir J) | 2023;64(4):ezad302 | <https://pmc.ncbi.nlm.nih.gov/articles/PMC10876118/> | Volltext (JATS) gelesen (leitlinien, befundung); Zitate geprüft | Zufallsbefunde, Koronarkalk, Emphysem-Graduierung | 2 · 1 |
| Q19 | Europäische Statements: ESR/ERS White Paper 2015, ESR/ERS Statement 2020, European position statement 2017, ERS Technical Standard 2023 | ESR, ERS; Lancet Oncol; Eur Respir J | Eur Radiol 2015;25:2519; Eur Radiol 2020;30:3277; Lancet Oncol 2017;18:e754; Eur Respir J 2023;61:2300128 | <https://pmc.ncbi.nlm.nih.gov/articles/PMC4529446/> | 2015 Volltext (befundung); 2017, 2020, 2023 nur Abstract = UNSICHER (evidenz, befundung) | Europäische Mindestanforderungen (CAD, Volumetrie, Register) | 0 · 0 |
| X07 | ESMO-Leitlinien zum NSCLC (Zer A et al., Ann Oncol 2025;36(11):1245–1262; Postmus et al. 2017) | European Society for Medical Oncology | 2025 bzw. 2017 | <https://doi.org/10.1016/j.annonc.2025.08.003> | nicht geprüft: 2025 nur im Abonnement, 2017 nur über Sekundärquellen = UNSICHER; nicht als Kandidatenquelle genutzt | keine Datenvorgabe für die Screening-Episode belegt | 0 · 0 |

### 2.3 Befundung (Radiologie) (4)

| ID | Quelle | Herausgeber | Fassung/Datum | URL | Verifikation | Relevanz | Kandidaten (Zitat · weiterer Bezug) |
|---|---|---|---|---|---|---|---|
| Q18 | ESTI-Empfehlungen 2026: Snoeckx et al., Prokop et al., ESR Essentials (Revel et al.) | European Radiology (ESTI) | Eur Radiol 2026;36(1):135–147 und 122–134; 2026;36(3):2064–2073 | <https://pmc.ncbi.nlm.nih.gov/articles/PMC12711968/> | Volltexte (Europe PMC JATS) gelesen (befundung, evidenz); Zitate geprüft | Strukturierter Befund, Volumetrie/VDT, Software-Konstanz, Dosis | 1 · 0 |
| Q20 | ACR Lung-RADS v2022 (mit Summary of Changes) und LCSR & IPN Data Dictionary | American College of Radiology | Lung-RADS November 2022; Data Dictionary 28.05.2026 | <https://www.acr.org/Clinical-Resources/Reporting-and-Data-Systems/Lung-Rads> | PDF-Volltexte gelesen (befundung, standards, evidenz, prozess); Zitate geprüft | Kategorien 0–4X, S-Modifikator, Messregeln; Registerfelder | 9 · 6 |
| Q30 | DICOM PS3.16 Content Mapping Resource (TID 4100, 1500, 3905, 10013; CID 6135, 10033/10034; Annex D) | NEMA / DICOM Standards Committee | 2026d | <https://dicom.nema.org/medical/dicom/current/output/chtml/part16/> | HTML-Seiten gelesen (recht, befundung, standards, evidenz) | Dosis-, Technik-, CAD- und Kalk-Codes | 0 · 4 |
| Q31 | IHE RAD AI Results (AIR), RSNA RadElement CDEs (RDES267, RDES105, RDES212), RSNA RadReport-API | IHE International; RSNA/ACR | AIR Rev. 1.3 (08.08.2025); RDES267 Published 2023/2024; RadReport-Listing 14.10.2026 | <https://www.ihe.net/uploadedFiles/Documents/Radiology/IHE_RAD_Suppl_AIR.pdf> | AIR-PDF gelesen, RadElement- und RadReport-API ausgewertet (befundung, standards); keine LCS-RadReport-Vorlage | Rundherd-Ergebnissatz, Lung-RADS-CDEs | 0 · 2 |

### 2.4 Datenstandards und Terminologien (10)

| ID | Quelle | Herausgeber | Fassung/Datum | URL | Verifikation | Relevanz | Kandidaten (Zitat · weiterer Bezug) |
|---|---|---|---|---|---|---|---|
| Q32 | MII Kerndatensatz Bildgebung (2026.0.0, 2027.0.0-ballot.1), Base, Person, Onkologie | Medizininformatik-Initiative | bildgebung 2026.0.0; base 2026.0.1; person 2025.0.1; onkologie 2027.0.0-ballot.1 | <https://packages.simplifier.net/de.medizininformatikinitiative.kerndatensatz.bildgebung/2026.0.0> | Pakete ausgewertet (befundung, standards); Konsolidierung: kanonische URLs /fhir/ext/modul-bildgebung/ bestätigt | Mapping-Ziele Bildgebung; kein Rauch-/Screening-Profil | 0 · 4 |
| Q33 | FHIR-Profile Raucherstatus: ISiKRaucherStatus, IPS Tobacco Use, Basis DE, US Core Smoking Status | gematik; HL7 International; HL7 Deutschland | ISiK 5.1.3/6.0.0; IPS 2.0.1; Basis DE stable; US Core 9.0.0 | <https://packages.simplifier.net/de.gematik.isik> | Pakete/StructureDefinitions ausgewertet (standards) | Status (72166-2, LL2201-3); Packungsjahre als Quantity | 0 · 2 |
| Q34 | Litauische IGs lt.hl7.fhir.lung und lt.hl7.fhir.lifestyle; HL7 Europe Imaging R4 | HL7 Lithuania; HL7 Europe | lung 0.0.1 (Commit fe68a28, 03.10.2026); lifestyle 0.1.0 (855b5ce); eu.imaging 1.0.0-ballot | <https://build.fhir.org/ig/HL7LT/ig-lt-lung/> | Build-Artefakte und FSH-Quellen geprüft (befundung, standards) | Einzige FHIR-Modellierung LDCT-Screening (Lung-RADS, Rundherd, Empfehlung) | 0 · 0 |
| Q35 | openEHR-Archetyp tobacco_smoking_summary.v2 | openEHR Foundation, CKM | Revision 2.0.1 (24.04.2026) | <https://ckm.openehr.org/ckm/archetypes/1013.1.8284> | ADL über CKM-REST geladen (standards) | Episodenmodell für Konsumabschnitte/Unterbrechungen | 0 · 1 |
| Q36 | oBDS 3.0.4_RKI und KBV-MIO-Katalog | RKI (ZfKD); KBV | oBDS Commit af87c85 (10.09.2026); MIO-Katalog 14.10.2026 | <https://github.com/robert-koch-institut/Bundesweiter_klinischer_Krebsregisterdatensatz-Datenschema_und_Klassifikationen> | Schema bzw. Katalog durchsucht (standards); vollständiges oBDS-XSD nicht geprüft = UNSICHER | Kein Screening-/Diagnoseanlass-Feld, kein Screening-MIO | 0 · 0 |
| Q37 | Terminologien: SNOMED CT, LOINC, NCIt, KDL, ICD-10-GM/OPS | SNOMED International; Regenstrief; NCI EVS; DVMD; BfArM | SNOMED INT 20250201 (tx.fhir.org), INT-Modul in AU 20260930/INT 20260601 (Ontoserver); LOINC 2.82/2.83; NCIt 26.09d; KDL 2026.0.0; ICD-10-GM/OPS 2026 | <https://tx.fhir.org/r4> | $lookup/$expand je Code (alle Linsen); Konsolidierung: strittige Codes (Modul/effectiveTime) und KDL-Codes nachgeprüft; MII-TermServ nicht genutzt | Code-Belege aller Kandidaten | 0 · 38 |
| X09 | MII-Terminologieserver (SNOMED CT International 20260701) | Medizininformatik-Initiative | Abfragen vom 14.10.2026 (mTLS mit Funktionszertifikat) | nicht öffentlich (mTLS) | $lookup und ECL-Expansion für die Gruppe 10 der Gegenprüfung (u. a. 363358000, 363346000, 442754001, 444589003); alle übrigen Codes nicht dort geprüft | Codeprüfung workupOutcome und lungCancerDetectionMode | 0 · 1 |
| X10 | ICD-10-GM 2026, Blöcke Z55–Z65 und Z80–Z99 | BfArM | 2026 | <https://klassifikationen.bfarm.de/icd-10-gm/kode-suche/htmlgm2026/block-z80-z99.htm> | Seiten geprüft (Gegenprüfung) | Z80.1 und Z56/Z57 (verworfen: familyHistoryLungCancer, occupationalCarcinogenExposure) | 0 · 0 |
| X11 | FHIR R4 ValueSets consent-category und appointmentstatus | HL7 International | FHIR R4 (4.0.1) | <https://hl7.org/fhir/R4/valueset-consent-category.html> | ValueSet-Seiten bzw. JSON geprüft (Gegenprüfung) | LOINC 64292-6 als Consent-Kategorie; Terminstatus noshow (verworfen: ldctAppointment) | 0 · 1 |
| X12 | Gesundheits-IT-Interoperabilitäts-Governance-Verordnung (GIGV 2024), Anlage 1 lfd. Nr. 002 | Bund, gesetze-im-internet.de | 10.09.2024, zuletzt geändert 09.09.2026 (BGBl. 2026 I Nr. 259) | <https://www.gesetze-im-internet.de/gigv_2024/> | nur über die Arbeitsnotiz (Prüfung des Maintainers 06.10.2026), in diesem Lauf nicht erneut geprüft | Verbindlichkeit von ISiK Stufe 5 für Krankenhausinformationssysteme (Profilbasis ISiKRaucherStatus) | 0 · 0 |

### 2.5 Evidenz, Bewertungen und Programme (10)

| ID | Quelle | Herausgeber | Fassung/Datum | URL | Verifikation | Relevanz | Kandidaten (Zitat · weiterer Bezug) |
|---|---|---|---|---|---|---|---|
| Q21 | IQWiG-Berichte S19-02, S23-02 (Lungenkrebsscreening) und P24-03 (Tabakentwöhnung) | IQWiG | S19-02 v1.0 19.10.2020; S23-02 v1.1 19.06.2024; P24-03 v1.0 12.06.2025 | <https://www.iqwig.de/projekte/s19-02.html> | Volltexte (relevante Kapitel) gelesen (leitlinien, prozess) | Selbstauskunft, Risikomodelle, HANSE-Scores, Entwöhnungsinformation | 0 · 0 |
| Q22 | Lungenkrebsfrüherkennung mittels LDCT – Wissenschaftliche Bewertung gemäß § 84 Abs. 3 StrlSchG (BfS-35/21) | Bundesamt für Strahlenschutz | August 2021, geändert August 2023 | <https://nbn-resolving.org/urn:nbn:de:0221-2021082028027> | Volltext Kap. 3.3–3.9 gelesen (leitlinien, prozess); Zitate geprüft | Aufklärungsbogen, Zufallsbefund-Vereinbarung, Datentransfer, Aussetzen, QS | 0 · 0 |
| Q23 | Randomisierte Studien: NLST (2011), NELSON (de Koning 2020; Zhao 2011; van Iersel 2007), LUSI (2020) | N Engl J Med; Cancer Imaging; Int J Cancer | NEJM 2011;365:395; NEJM 2020;382:503; Cancer Imaging 2011;11:S79; Int J Cancer 2007;120:868; 2020;146:1503 | <https://doi.org/10.1056/NEJMoa1102873> | NLST und Zhao Volltext (evidenz, befundung); de Koning, van Iersel, LUSI nur Abstract = UNSICHER | Positivdefinition, Adhärenz, Komplikationen, Entdeckungswege, Volumetrie | 0 · 2 |
| Q24 | HANSE: Studiendesign (RöFo 2022), Ergebnisse (Lancet Oncol 2025), Registereintrag NCT04913155 | Thieme; Elsevier; ClinicalTrials.gov | RöFo 2022;194:1333; Lancet Oncol 2025;26(12):1541; Registerstand 03.10.2025 | <https://pmc.ncbi.nlm.nih.gov/articles/PMC9708322/> | Design Volltext (befundung, evidenz); Lancet nur Abstract = UNSICHER; Register-JSON gelesen | PLCOm2012-Schwelle 1,58 %, Zweitlesung, Agatston/Emphysem, Rauchstopp | 0 · 0 |
| Q25 | Selection criteria for lung-cancer screening (PLCOm2012; Tammemägi et al.) | N Engl J Med | 2013;368(8):728–736, PMC3929969 | <https://doi.org/10.1056/NEJMoa1211776> | Volltext (PMC) gelesen (evidenz); prozess nur Abstract | Modellvariablen und Kodierung | 0 · 1 |
| Q26 | NHS England Lung Cancer Screening Programme: Standard protocol v3, QA standards v3, LCSDS user guidance, NHS Data Dictionary | NHS England / NHS England Digital | Protokoll und QA v3 03.02.2025; LCSDS Stand 18.09.2026; Data Dictionary Juli 2026 | <https://www.england.nhs.uk/wp-content/uploads/2019/02/2502-B1646-standard-protocol-prepared-for-the-lung-cancer-screening-programme.pdf> | Protokoll/QA Volltext, per Prüfsumme bestätigt (evidenz, prozess); LCSDS nur via Spiegel = Stand UNSICHER | Risikomodell-Dokumentation, Nichterscheinen, QS-Standards, Minimum Dataset | 2 · 0 |
| Q27 | EU-Ebene: Council Recommendation 2022/C 473/01; EC-LuC; EUCanScreen; SOLACE | Rat der EU; EK/JRC; EUCanScreen-Konsortium; EIBIR/HaDEA | OJ C 473 13.12.2022; Seiten Abruf 14.10.2026; SOLACE 04/2023–03/2026 | <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022H1213(01)> | Council Rec. Volltext (evidenz); EC-LuC/EUCanScreen Seiten gelesen; SOLACE-Leitlinie nur Sekundärquelle = UNSICHER | Datensysteme/Indikatoren; kein europäisches Lungen-Datenformat verfügbar | 1 · 0 |
| Q28 | IARC Handbooks Vol. 21, Press Release Nr. 385 | IARC/WHO | 24.09.2026 | <https://www.iarc.who.int/wp-content/uploads/2026/09/pr385_E.pdf> | Pressemitteilung gelesen (evidenz); Handbook/NEJM-Report nicht gelesen | Group A; Stadium III–IV; Schadensliste | 0 · 0 |
| Q29 | Weitere Programme: Litauen-Pilot (Danila 2025), 4-IN-THE-LUNG-RUN (Hubert 2026; Walstra 2026), Cabrera 2026, Positionspapier Österreich (Wass 2026) | Cancers; BMC Public Health; Eur J Cancer; Int J Cancer; Wien Klin Wochenschr | 2025;17:1956; 2026;26:500; 2026;244:116909; 2026;158:2359; 2026;138 | <https://doi.org/10.3390/cancers17121956> | Litauen, Hubert, Wass Volltext (evidenz); Walstra, Cabrera nur Abstract = UNSICHER | Prozessindikatoren, Ablehnungsgründe, Zufallsbefundraten, Audit-Kennzahlen | 0 · 0 |
| X08 | Probability of cancer in pulmonary nodules detected on first screening CT (Brock/PanCan; McWilliams A et al.) | N Engl J Med | 2013;369(10):910–919, DOI 10.1056/NEJMoa1214726 | <https://doi.org/10.1056/NEJMoa1214726> | nur Abstract (Europe PMC) = UNSICHER | Malignitätsmodell für Rundherde; Emphysem als Prädiktor (noduleMalignancyProbability, emphysemaSeverity) | 0 · 2 |

### 2.6 Projektinterne Grundlagen (5)

| ID | Quelle | Herausgeber | Fassung/Datum | URL | Verifikation | Relevanz | Kandidaten (Zitat · weiterer Bezug) |
|---|---|---|---|---|---|---|---|
| Q38 | Arbeitsnotiz Vorarbeiten Teilmodul Früherkennung: Raucheranamnese und Eignungsprüfung | FGDH, TU Dresden (M. Susky) | Stand 06.10.2026 | nicht öffentlich (Arbeitsnotiz) | Gelesen; Kernaussagen gegen Primärquellen geprüft; Korrekturen: KBV-Fassung Okt. 2026, NHS-URL liefert v3 | Konsumabschnitt/Unterbrechung, ISiK-Profilbasis, Q3-Modul | 0 · 13 |
| Q39 | BPMN lung-cancer-screening-pathway und Quellenlisten des Pfad-Repos (pathway-clinical-sources.md, pathway-data-sources.md 2a) | FGDH / MiHUB (mihub-lung-cancer-pathway) | Branch dev, Modell-Commit ac7e9c2 (Stand 2026-06-25); Quellenliste Stand 2026-09-07 | <https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway/blob/dev/models/lung-cancer-screening-pathway.bpmn> | Modell-XML lokal gelesen, Element-IDs und Lanes im Konsolidierungsschritt extrahiert; Quellenlisten gelesen | process_step-Zuordnung; S3-Bezug im Modell fehlt (SEM-2) | 2 · 51 |
| Q40 | Bestandskatalog mihub-lung-cancer-pathway-data-elements (Elemente und Schema) | FGDH, TU Dresden | Commit c4fb886 (112 Elemente) | dieses Repository | Namen, Labels, Definitionen und Schema read-only gelesen (Konsolidierung) | overlaps_existing; Schema-Lücken | 0 · 28 |
| X13 | Entscheidungsvorlage Spezifikationsmodule entlang des Lungenkrebs-Patientenpfads (MiHUB A3.2) | MiHUB | Entwurf 0.3 vom 06.10.2026 | A3.2-Ordner (nicht im Repository) | nur über die Arbeitsnotiz (Abschnitt 8) belegt, nicht selbst gelesen | Raucheranamnese als Querschnittsmodul Q3, Screening als Inkrement 1 von M1, Entscheidung E5 (Profilbasis) | 0 · 0 |
| X14 | Worktree feat/screening-episode-preparation des Repositorys data-elements | FGDH, TU Dresden | Basis c4fb886 (Stand 14.10.2026) | Branch `feat/screening-episode-preparation` | git status und git diff im Synthese-Schritt gelesen | Vorarbeit für die Phase screening (Schema-Enum, ID-Pattern, Ordner, Skripte, CODEOWNERS) | 0 · 0 |

Ergänzende Hinweise: NELSON-Volumetrie und -Kriterien sind über Q23 (u. a. Zhao 2011, Volltext) und die S3-LL (Q12, Statement 5.2) belegt. Die ESMO-Leitlinien (X07) wurden nicht geprüft und nicht als Kandidatenquelle genutzt. Onkopedia NSCLC (Q14) beschreibt den Stand vor dem Programmstart (Kap. 3.2: „Der Start ist für 2025 geplant.“) und dient nur als Kontext.

## 3 Prozessschritt → Datenelement-Matrix

Die Zeilen folgen dem BPMN-Modell. „Datenelemente“ sind behaltene Kandidaten, „Bestand“ sind referenzierte Elemente des Katalogs. „Pflicht nach Norm“ fasst die Einstufung nach der Gegenprüfung für den Schritt zusammen; die Einstufung je Element steht in Abschnitt 4.

| Gruppe | BPMN-Schritt (ID) | Akteur | Datenelemente (behalten) | Bestand (Verweis) | Pflicht nach Norm |
|---|---|---|---|---|---|
| G1 Zugang | Person mit Risikofaktoren identifiziert (Event_1uilxb6) → Versichterte Person zu LKS auffordern (Activity_0o694d5, Annotation „Einmal jährlich“) → Aufforderung versendet (Event_1u8i3oa) → Aufforderung zum LKS erhalten (Event_0qh7lu0) | Praxis → Versicherte | `screeningInvitation` | – | keine: kein Einladungsverfahren (§ 25, nicht § 25a SGB V); KFE-RL § 43 Abs. 2 S. 2 Nr. 2 nennt die „Ansprache der versicherten Person“ nur als Fortbildungsinhalt |
| G1 Zugang | Aus Eigeninitiative an LKS interessiert (Event_1hd295c) → Arztpraxis kontaktieren (Activity_00yhsqy, Annotation „Einmal jährlich“) → Anfrage erhalten (Event_1d2c01e) | Versicherte → Praxis | `decisionAidResponse`<br>`screeningEpisode` | – | keine (Versicherteninformation S. 6 beschreibt den Ablauf) |
| G2 Raucheranamnese (Q3) · G3 Zulässigkeit/Eignung | Zulässigkeitsvoraussetzungen prüfen (§2) (Activity_0ya2ob0; Annotation § 2 Abs. 1 Nr. 1–3) | Praxis (berichterstellende Ärzt:in) | `smokingStatusScreening`<br>`cigaretteConsumptionPeriod`<br>`cigarettesPerDayInPeriod`<br>`smokingInterruptionPeriod`<br>`otherTobaccoNicotineProductUse`<br>`creditableSmokingDurationYears`<br>`packYearsCalculated`<br>`lastQualifyingChestCtDate`<br>`symptomAndLungCancerCareStatus`<br>`medicalSuitabilityProfile` | birthYear (Geburtsdatum für das Alterskriterium)<br>comorbidity<br>ecogPerformanceStatus<br>smokingStatus | Pflicht: Kriterien nach LuKrFrühErkV § 2 Abs. 1 Nr. 1–3 (Alter, 12-Monats-Regel, ≥ 25 Jahre und ≥ 15 Packungsjahre, Eignungsprofil); Erhebung nach KFE-RL § 39 Nr. 1; Anspruch KFE-RL § 38 |
| G3 Zulässigkeit/Eignung | Voraussetzungen erfüllt? (Gateway_1whuu15) → nein: Teilnahme nicht möglich (Event_0rhy6wb) → Absage (Message Flow) → Absage erhalten (Event_0i87qsx) → Teilnahme nicht möglich (Event_11uljw2) | Praxis → Versicherte | `eligibilityCheckResult` | – | Pflicht nur für die positive Bestätigung im Bericht (KFE-RL § 39 Nr. 1, § 40 S. 3); Absage und Absagegrund ohne Rechtsgrundlage |
| G3 Zulässigkeit/Eignung | erneute Prüfung des Eignungsprofils bei Folgerunden (im BPMN nicht modelliert; Wiedereintritt über Anfrage erhalten, Event_1d2c01e) | Praxis | `eligibilityProfileReviewDueDate`<br>`medicalSuitabilityProfile` | – | Leitlinie: S3 Empf. 5.6 (EK) |
| G5 Information/Entscheidung | Aufklärungsgespräch (§2 Abs.1 Nr.4) (Activity_0e82ewp; nach Parallel-Gateway Gateway_1aronx8) | Praxis (berichterstellende Ärzt:in) · Versicherte | `screeningInformationConsultation`<br>`patientInformationLeafletProvided`<br>`decisionAidResponse`<br>`participationDecision`<br>`screeningDataUseConsent` | patientGoalsAndPreferences<br>consultationModality | Pflicht: LuKrFrühErkV § 2 Abs. 1 S. 1 Nr. 4 und S. 2; KFE-RL § 40 S. 1 mit Anlage I; Entscheidung freiwillig (Versicherteninformation S. 2) |
| G5 Entwöhnung | Auf Rauchentwöhnungsprogramm hinweisen (Activity_0f2lkuk) | Praxis | `tobaccoCessationOfferScreening` | tobaccoCessationCounselling | Pflicht: Information über Entwöhnungsmöglichkeiten (KFE-RL § 40 S. 2, Bestätigung S. 3); Angebot und Reaktion: Leitlinie (S3 Empf. 4.5, 5.7) |
| G6 Bericht/Überweisung | Bericht erstellen (§2 Abs.1 Nr.3) (Activity_1npn3bx; Datenobjekt „Bericht gem. §2 Abs.1 Nr.3 PDF“; Annotation Qualifikation § 6 Abs. 3) | Praxis | `eligibilityReport`<br>`packYearsCalculated`<br>`creditableSmokingDurationYears`<br>`medicalSuitabilityProfile`<br>`eligibilityCheckResult` | comorbidity<br>historyTakingPrimaryCare | Pflicht: LuKrFrühErkV § 2 Abs. 1 S. 1 Nr. 3; KFE-RL § 39 Nr. 1, § 40 S. 3; Selbsterklärung § 43 Abs. 2 S. 3 |
| G6 Bericht/Überweisung | Überweisung ausstellen (Activity_1fi5rrl; Annotation § 2 Abs. 2) → Überweisung und Bericht übermitteln (Activity_17m122u) → Überweisung und Bericht eingegangen (Event_1hwpffc) → Überweisung der Radiologie vorlegen (Activity_16eirv7) → Überweisung erhalten (Event_11h9bwq) | Praxis → Versicherte → Radiologie | `ldctReferral`<br>`eligibilityReport` | referralOrder | Pflicht: Bericht an die Person (KFE-RL § 39 Nr. 1 S. 2); Überweisung über den Überweisungsvorbehalt (BMV-Ä § 13 Abs. 4 S. 1) |
| G7 Radiologie vor LDCT | Bericht lesen (Activity_1rd4qnc) → Rechtfertigende Indikation stellen und Voruntersuchung prüfen (§3 und §4 Abs.2) (Activity_0l9ecr6; Annotation § 4 Abs. 2) → Anforderungen erfüllt? (Gateway_0ofbhg1) | Erstbefunder | `eligibilityReport`<br>`justifyingIndication`<br>`priorScreeningImagesAvailability`<br>`lastQualifyingChestCtDate`<br>`eligibilityCheckResult`<br>`screeningExaminationType` | – | Pflicht: LuKrFrühErkV § 3 Nr. 1–2, § 4 Abs. 2; KFE-RL § 41 Abs. 1; StrlSchG § 83 Abs. 3, § 85 Abs. 1 S. 2 Nr. 1; StrlSchV § 119 Abs. 3 |
| G7 Radiologie vor LDCT | Aufklärung Niedrigdosis-CT durchführen (Activity_1uptzny) → Teilnahme durch Versicherte bestätigt? (Gateway_0jgpvd3; nein-Pfad ohne benanntes Endereignis) | Erstbefunder · Versicherte | `ldctInformedConsent`<br>`resultTransmissionConsentReferrer`<br>`screeningDataUseConsent` | – | Pflicht: KFE-RL § 41 Abs. 2; BGB §§ 630d, 630e, 630f Abs. 2; StrlSchV § 124 Abs. 1; Einwilligung zur Übermittlung an die Praxis bedingt (KFE-RL § 42 Abs. 2 S. 2) |
| G8 LDCT | Niedrigdosis-CT durchführen (§4, §5) (Activity_12qrin2; Annotation Anlage zu § 4; Datenobjekt „Bilddaten“, Datenspeicher PACS) | Erstbefunder (Strahlenschutzverantwortliche:r) | `ldctExamination`<br>`screeningExaminationType`<br>`ctdiVol`<br>`ldctAcquisitionParameters` | ctThoraxScan | Pflicht: KFE-RL § 44 S. 1; StrlSchG § 85 Abs. 1 S. 2 Nr. 2–3; Einhaltung LuKrFrühErkV § 1 Abs. 1, § 4 Abs. 1 mit Anlage |
| G9 Befundung | Erstbefundung ohne CAD-Software (§5 Abs.1) (Activity_1tdikdp) → Erstbefundung mit CAD-Software (§5 Abs.1) (Activity_1mvivag; Annotation CAD-Software § 1 Abs. 3) | Erstbefunder | `screeningReadingEvent`<br>`cadAnalysisReport`<br>`pulmonaryNoduleFinding`<br>`noduleSizeMeasurement`<br>`noduleVolumeDoublingTime`<br>`lungRadsCategory`<br>`incidentalFinding`<br>`coronaryArteryCalcification`<br>`emphysemaSeverity` | comorbidity | Pflicht: Verfahren und CAD-Auswertung (LuKrFrühErkV § 5 Abs. 1, Anlage zu § 4); Dokumentation KFE-RL § 44 S. 1, QS-Vereinbarung § 13f; Lung-RADS, Rundherd- und Nebenbefunddetails: Leitlinie |
| G9 Befundung | Kontroll- oder abklärungsbedürftiger Befund? (Gateway_0mk0bmb) → ja: Zweitbefundung anordnen (§5 Abs.2) und Überweisung ausstellen (Activity_1rsqdi6) | Erstbefunder | `readerAssessmentCategory`<br>`secondReadingRequest` | referralOrder | Pflicht: Erstbefund dokumentieren (QS-Vereinbarung § 13f); Zweitbefundung bedingt (LuKrFrühErkV § 5 Abs. 2; KFE-RL § 42 Abs. 1) |
| G9 Befundung | Zweitbefundung ohne CAD-Software (§5 Abs.2) (Activity_1ww2vbt) → Zweitbefundung mit CAD-Software (§5 Abs.2) (Activity_0mx6d87) | Zweitbefunder | `screeningReadingEvent`<br>`cadAnalysisReport`<br>`readerAssessmentCategory`<br>`lungRadsCategory`<br>`pulmonaryNoduleFinding` | – | bedingte Pflicht: bei kontroll- oder abklärungsbedürftigem Erstbefund (LuKrFrühErkV § 5 Abs. 2); Zweitbefund dokumentieren (KFE-RL § 44 S. 1) |
| G9 Befundung | Gemeinsame Beurteilung vornehmen (§5 Abs.3) (Activity_10riunt, Activity_0gyncma; Datenobjekt „Beurteilung“) | Erst- und Zweitbefunder | `screeningResultCategory`<br>`noduleMalignancyProbability` | – | bedingte Pflicht: LuKrFrühErkV § 5 Abs. 3; KFE-RL § 42 Abs. 1 S. 3, § 44 (Ergebnis der gemeinsamen Beurteilung) |
| G10 Ergebnis/Mitteilung | Befund kategorie? (Gateway_10udrva; unauffällig → Gateway_1g1kn3s, kontrollbedürftig → Activity_07i9gmj, abklärungsbedürftig → Activity_0es6xoa) | Erst- und Zweitbefunder | `screeningResultCategory`<br>`lungRadsCategory` | – | Pflicht: Kategorien nach LuKrFrühErkV § 1 Abs. 4/5; Dokumentation KFE-RL § 44 |
| G10 Ergebnis/Mitteilung | Empfehlung für (Zeitpunkt der) nächsten Untersuchung abgeben (§5 Abs.3) (Activity_07i9gmj) | Erst- und Zweitbefunder | `recommendedManagement`<br>`recommendedControlInterval` | recommendationsForPrimaryCare<br>plannedFollowUpAppointment | bedingte Pflicht: LuKrFrühErkV § 5 Abs. 3 S. 2; KFE-RL § 42 Abs. 3 Nr. 1, § 44 |
| G10 Ergebnis/Mitteilung | Klinische Abklärung anzeigen und Überweisung ausstellen (Activity_0es6xoa, Lane Zweitbefunder; Datenobjekt „Überweisung“) | Erstbefunder (laut EBA-Gründen/KBV; BPMN: Zweitbefunder) | `abnormalResultDiscussion`<br>`clarificationReferral`<br>`recommendedManagement` | referralOrder<br>consultationModality | bedingte Pflicht: KFE-RL § 42 Abs. 3 Nr. 2 (besprechen und unverzüglich einleiten) |
| G10 Ergebnis/Mitteilung | Qualitätsdaten erheben und dokumentieren (§7) (Activity_14vmlwn; Annotation QS § 7) | Erstbefunder | `ctdiVol`<br>`ldctAcquisitionParameters` | – | Pflicht als Aggregat: anonymisierte Zählung (LuKrFrühErkV § 7 Abs. 2), Quartalsbericht an die KV (KFE-RL § 44); kein eigenes Datenelement (quarterlyQualityReport verworfen) |
| G10 Ergebnis/Mitteilung | Rückmeldung übermitteln (Activity_12ef5s1; Datenobjekt „Rückmeldung Radiologie“) → Rückmeldung der Radiologie eingegangen (Event_1w13vdp Versicherte; Event_13jgib0 Praxis); Annotation „Ergebnis-mitteilung nach 4-5 Tagen“ (Flow_1996xd4) | Erstbefunder → Versicherte, Praxis | `structuredScreeningReport`<br>`resultCommunicationToPatient`<br>`resultTransmissionConsentReferrer`<br>`incidentalFinding` | diagnosticReportDocument | Soll-Vorschrift: strukturierter Befundbericht binnen 14 Tagen (KFE-RL § 42 Abs. 2 S. 1); an die Praxis nur bei Einwilligung (S. 2) |
| G11 Teilnahmeverlauf | Rückmeldung mit Versichertem besprechen (Activity_1ta6sej) → Beratung zum weiteren Vorgehen → Rückmeldung besprechen und Entscheidung treffen (Activity_0io1wvp) → Beratung abgeschlossen (Event_0z2esy1) | Praxis · Versicherte | `participationDecision`<br>`participantExperienceFeedback`<br>`tobaccoCessationOfferScreening`<br>`eligibilityProfileReviewDueDate` | – | keine eigene Pflicht |
| G11 Teilnahmeverlauf | Behandlung fortsetzen (Gateway_1dj77wn): ja → Überweisung zur weiteren Behandlung wird nachgegangen (Event_0nesy5q); nein → Screening beendet (Event_1fjvvjs); Untersuchung abgeschlossen (Event_10ae0lt) | Versicherte · Praxis | `screeningEpisode`<br>`screeningInvitation` | screeningProgramEnrolment | keine; Austrittsgründe normativ ableitbar (KFE-RL § 38 Abs. 1 und 3) |
| G12 Abklärung (Grenzfall) | Abklärung in spezialisierter Einrichtung nach Event_0nesy5q (im BPMN nicht modelliert; Rückkanal fehlt) | spezialisierte Einrichtung → Screening-Einheit | `screeningCaseConference`<br>`invasiveWorkupProcedure`<br>`workupOutcome` | tumorBoardDecision<br>cancerDiagnosis<br>tnmStage<br>tumorHistology | Leitlinie: S3 Empf. 5.9, 5.11, 5.12, 5.13; Monitoring nach KFE-RL § 46 Abs. 2 erst bis Ende 2028 |

**Lücken im BPMN-Modell, die die Datenzuordnung betreffen:**

- Kein Schritt für die Terminvereinbarung in der Radiologie und kein Nichterscheinen-/Absagepfad (ldctAppointment verworfen; plannedFollowUpAppointment nutzen).
- Keine Schritte für Einwilligungen (Übermittlung an die Praxis, Datenaustausch mit Zweitbefunder und Voreinrichtungen, Datennutzung nach S3 Empf. 5.13).
- Gateway_0jgpvd3 „Teilnahme durch Versicherte bestätigt?“: nein-Pfad ohne benanntes Abbruch-Endereignis.
- Rückmeldung an die Praxis (Event_13jgib0) unbedingt modelliert, rechtlich nur bei Einwilligung (KFE-RL § 42 Abs. 2 S. 2).
- Activity_0es6xoa (Besprechung und Überweisung bei abklärungsbedürftigem Befund) liegt in der Lane Zweitbefunder; EBA-Gründe und KBV sehen den Erstbefunder vor.
- Annotation „Ergebnis-mitteilung nach 4-5 Tagen“ (TextAnnotation_045vu1u, Pool Versicherte) weicht von der Soll-Frist ab (14 Tage nach Erstellung der Aufnahme, KFE-RL § 42 Abs. 2); Bezugsgröße unklar.
- Keine erneute Prüfung des Eignungsprofils (S3 Empf. 5.6), kein Opt-out-Ergebnis der Tabakentwöhnung (S3 Empf. 4.5), keine Konsensuskonferenz (EBM 01881), kein Rückkanal aus der Abklärung (G12).
- Die Dokumentation von Activity_0l9ecr6 („Rechtfertigende Indikation stellen …“) ist eine Kopie der Dokumentation von Activity_1fi5rrl („Die Praxis stellt eine Überweisung …“) – eigene Prüfung im Synthese-Schritt.
- S3-Bezug (Kap. 5) im Modell nicht referenziert (Quellenliste des Pfad-Repos, Kriterium SEM-2).

## 4 Kandidaten (Status „behalten“)

Alle 53 Kandidaten haben beide Gegenprüfungen bestanden. Die Werte der Konsolidierung (Datentyp, Kardinalität, Kategorie, Quelle mit Zitat, Codes, overlaps_existing) sind unverändert übernommen. Rolle, Trigger, die Verbindlichkeit nach der Gegenprüfung und die Umsetzungsempfehlung stammen aus dem Synthese-Schritt, der beide Urteile zusammenführt. Zusätzliche Zitate stammen aus den Urteilen der Gegenprüfung und sind wörtlich übernommen; ihre Fundstellen haben die Skeptiker im Volltext geprüft.

Legende Verbindlichkeit: **Pflicht** = Norm verlangt Angabe und Dokumentation · **bedingt** = nur in bestimmten Fällen · **mittelbar** = Rechengrundlage oder Voraussetzung, Erfassung selbst nicht vorgeschrieben · **Soll-Vorschrift** = Richtlinie mit „soll“ · **Leitlinie** = Empfehlung ohne Rechtspflicht · **keine** = lokal, optional oder internationales Vorbild.

### 4.1 Übersicht

| Nr. | name | label_de | Datentyp · Kard. | Kategorie | Gruppe | Pflicht (Konsol. → Gegenprüfung) | Umsetzungsform | overlaps_existing | Status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `screeningInvitation` | Aufforderung, Wiedereinladung, Erinnerung (Recall) | dateTime · 0..* | kontakt-visite | G1 | nein → keine | eigenständig, optional (pfad- und portalspezifisch) | – | behalten |
| 2 | `smokingStatusScreening` | Raucherstatus bei Anspruchsprüfung | CodeableConcept · 1..1 | sozialanamnese | G2 | nein → mittelbar | Spezialisierung von smokingStatus (followup) | smokingStatus (followup) – Phase screening ergänzen | behalten |
| 3 | `cigaretteConsumptionPeriod` | Konsumabschnitt Zigarettenrauchen | Period · 1..* | sozialanamnese | G2 | ja → mittelbar | eigenständig (Kopf-Element der Raucheranamnese Q3) | – | behalten |
| 4 | `cigarettesPerDayInPeriod` | Zigaretten pro Tag im Jahresdurchschnitt je Konsumabschnitt | Quantity · 1..* | sozialanamnese | G2 | ja → mittelbar | Teil von cigaretteConsumptionPeriod | – | behalten |
| 5 | `smokingInterruptionPeriod` | Vollständige Rauchunterbrechung | Period · 0..* | sozialanamnese | G2 | ja → mittelbar | eigenständig (Raucheranamnese Q3) | – | behalten |
| 6 | `otherTobaccoNicotineProductUse` | Weitere Tabak- und Nikotinprodukte (nicht anrechenbar) | CodeableConcept · 0..* | sozialanamnese | G2 | nein → Leitlinie | eigenständig (Raucheranamnese Q3) | smokingStatus (führt E-Zigarette als Status) | behalten |
| 7 | `creditableSmokingDurationYears` | Anrechenbare Dauer des Zigarettenkonsums (Jahre) | Quantity · 1..1 | sozialanamnese | G2 | ja → Pflicht | abgeleitet (aus Konsumabschnitten und Unterbrechungen) | – | behalten |
| 8 | `packYearsCalculated` | Packungsjahre (jahrweise nach § 1 Abs. 2 LuKrFrühErkV) | Quantity · 1..1 | sozialanamnese | G2 | ja → Pflicht | eigenständig (generalisiert; nimmt packYearsSelfEstimate auf) | – | behalten |
| 9 | `lastQualifyingChestCtDate` | Datum der letzten befundungsgeeigneten Thorax-CT | date · 0..1 | bildgebung | G3 | ja → Pflicht | Erweiterung von ctThoraxScan (Thorax-CT-Vorgeschichte) | ctThoraxScan | behalten |
| 10 | `symptomAndLungCancerCareStatus` | Asymptomatik und kein laufender Lungenkrebs-Behandlungskontext | CodeableConcept · 1..1 | befund | G3 | ja → mittelbar | eigenständig, reduziert auf Symptom- und Verdachtsstatus | cancerDiagnosis; currentTumorStatus; screeningProgramEnrolment | behalten |
| 11 | `medicalSuitabilityProfile` | Medizinisches Eignungsprofil | CodeableConcept · 1..1 | assessment | G3 | ja → Pflicht | eigenständig | comorbidity | behalten |
| 12 | `eligibilityProfileReviewDueDate` | Fälligkeit der erneuten Prüfung des Eignungsprofils | date · 0..1 | versorgungsplanung | G3 | nein → Leitlinie | abgeleitetes Attribut (Zusammenlegung mit medicalSuitabilityProfile prüfen) | – | behalten |
| 13 | `eligibilityCheckResult` | Ergebnis der Zulässigkeitsprüfung in der Praxis | CodeableConcept · 1..1 | assessment | G3 | ja → Pflicht | eigenständig (Gesamtergebnis; Rolle Erstbefunder über data_flows) | – | behalten |
| 14 | `screeningInformationConsultation` | Informations- und Beratungsgespräch (Erstberatung) | dateTime · 1..1 | kontakt-visite | G5 | ja → Pflicht | eigenständig (Anker des Informationsakts) | patientGoalsAndPreferences | behalten |
| 15 | `patientInformationLeafletProvided` | Aushändigung der G-BA-Versicherteninformation (Fassung, Format) | CodeableConcept · 1..1 | dokument | G5 | ja → Pflicht | Teil von screeningInformationConsultation | – | behalten |
| 16 | `decisionAidResponse` | Entscheidungshilfe der Versicherteninformation (Antworten) | Reference · 0..1 | prom | G5 | nein → keine | eigenständig, optional (Portal) | patientGoalsAndPreferences | behalten |
| 17 | `participationDecision` | Teilnahmeentscheidung der versicherten Person | CodeableConcept · 1..* | versorgungsplanung | G5 | nein → keine | eigenständig, auf die Entscheidung nach der Information begrenzt | patientGoalsAndPreferences | behalten |
| 18 | `tobaccoCessationOfferScreening` | Information über und Angebot einer Tabakentwöhnung (Opt-out) | CodeableConcept · 0..* | prozedur | G5 | ja → Pflicht (Information) / Leitlinie (Angebot) | Spezialisierung von tobaccoCessationCounselling (followup) | tobaccoCessationCounselling (followup) – um Phase screening erweitern | behalten |
| 19 | `eligibilityReport` | Bericht gemäß § 2 Abs. 1 Nr. 3 LuKrFrühErkV (Prüfbericht) | Reference · 1..1 | dokument | G6 | ja → Pflicht | eigenständig (Composition) | – | behalten |
| 20 | `ldctReferral` | Überweisung zur Niedrigdosis-CT an den Erstbefunder | Reference · 1..1 | administrativ | G6 | nein → Pflicht | Spezialisierung von referralOrder (primarycare) | referralOrder (Spezialisierung) | behalten |
| 21 | `justifyingIndication` | Rechtfertigende Indikation (§ 83 Abs. 3 StrlSchG) mit Zeitpunkt | dateTime · 1..1 | prozedur | G7 | ja → Pflicht | eigenständig | – | behalten |
| 22 | `priorScreeningImagesAvailability` | Vorliegen von Voraufnahmen und Vorbefunden (§ 4 Abs. 2) | CodeableConcept · 1..1 | bildgebung | G7 | ja → bedingt | eigenständig (lokales ValueSet) | – | behalten |
| 23 | `ldctInformedConsent` | Aufklärung durch den Erstbefunder und Einwilligung in die LDCT | CodeableConcept · 1..1 | prozedur | G7 | ja → Pflicht | eigenständig (Einwilligungsergebnis nur hier) | – | behalten |
| 24 | `resultTransmissionConsentReferrer` | Einwilligung in die Befundübermittlung an die berichterstellende Praxis | boolean · 1..1 | administrativ | G7 | ja → bedingt | eigenständig; Ausbau zum gemeinsamen Einwilligungselement (nimmt providerDataExchangeConsent auf) | – | behalten |
| 25 | `screeningDataUseConsent` | Einwilligung in zentrale Speicherung, Registerabgleich und Forschung | CodeableConcept · 0..* | administrativ | G7 | nein → Leitlinie | eigenständig, optional und vorausschauend | – | behalten |
| 26 | `ldctExamination` | Niedrigdosis-CT des Thorax zur Früherkennung (Durchführung) | dateTime · 1..1 | bildgebung | G8 | ja → Pflicht | Spezialisierung von ctThoraxScan (followup) | ctThoraxScan (Spezialisierung) | behalten |
| 27 | `screeningExaminationType` | Art der Früherkennungsuntersuchung und Runde | CodeableConcept · 1..1 | versorgungskontext | G8 | nein → keine | Attribut von ldctExamination (Zusammenlegung prüfen) | – | behalten |
| 28 | `ctdiVol` | Volumen-CT-Dosisindex (CTDIvol) der Spiral-LDCT | Quantity · 1..1 | messwert | G8 | ja → mittelbar | eigenständig (isPartOf ldctExamination) | – | behalten |
| 29 | `ldctAcquisitionParameters` | Aufnahme- und Rekonstruktionsparameter nach Anlage zu § 4 (mit Konformität) | Reference · 0..1 | bildgebung | G8 | nein → keine | eigenständig, reduziert auf Konformität und RDSR-Referenz | – | behalten |
| 30 | `screeningReadingEvent` | Befundungsvorgang (Rolle, ohne/mit CAD, Software, Person) | Reference · 1..* | prozedur | G9 | ja → Pflicht | eigenständig (Procedure je Befundung) | – | behalten |
| 31 | `cadAnalysisReport` | CAD-Auswertung als erweiterte Bilddokumentation | Reference · 0..* | dokument | G9 | ja → Pflicht | eigenständig | – | behalten |
| 32 | `pulmonaryNoduleFinding` | Lungenrundherd (Einzelbefund je Rundherd) | Reference · 0..* | befund | G9 | nein → Leitlinie | eigenständig (Klammerbefund; hasPart Größe, VDT, Malignitätswahrscheinlichkeit) | ctThoraxFinding; tumorLocalisation | behalten |
| 33 | `noduleSizeMeasurement` | Rundherdgröße (Volumen, mittlerer Durchmesser, solide Komponente) | Quantity · 0..* | messwert | G9 | nein → Leitlinie | Teil von pulmonaryNoduleFinding (Aufteilung empfohlen) | – | behalten |
| 34 | `noduleVolumeDoublingTime` | Volumenverdopplungszeit (VDT) des Rundherds | Quantity · 0..* | messwert | G9 | nein → Leitlinie | Teil von pulmonaryNoduleFinding | – | behalten |
| 35 | `noduleMalignancyProbability` | Malignitätswahrscheinlichkeit des Rundherds | Quantity · 0..* | assessment | G9 | nein → Leitlinie | Teil von pulmonaryNoduleFinding | – | behalten |
| 36 | `lungRadsCategory` | Lung-RADS-Kategorie (V-Lung-RADS 2022) mit Version und S-Modifikator | CodeableConcept · 1..* | assessment | G9 | nein → Leitlinie | eigenständig | – | behalten |
| 37 | `readerAssessmentCategory` | Befundkategorie je Befunder (Erst-/Zweitbefund) | CodeableConcept · 1..* | befund | G9 | ja → Pflicht | eigenständig (lokales CodeSystem gemeinsam mit screeningResultCategory) | ctThoraxFinding | behalten |
| 38 | `secondReadingRequest` | Veranlassung der Zweitbefundung (Konsiliarauftrag, Datenübermittlung) | Reference · 0..1 | mitbetreuung | G9 | ja → bedingt | Spezialisierung von referralOrder (primarycare) | referralOrder | behalten |
| 39 | `incidentalFinding` | Klinisch relevanter Nebenbefund mit Empfehlung | CodeableConcept · 0..* | befund | G9 | nein → Leitlinie | eigenständig (Befundgruppe) | comorbidity | behalten |
| 40 | `coronaryArteryCalcification` | Koronararterienverkalkung (visuell, optional Agatston) | CodeableConcept · 0..1 | befund | G9 | nein → Leitlinie | Spezialisierung von incidentalFinding | – | behalten |
| 41 | `emphysemaSeverity` | Lungenemphysem – Ausprägung | CodeableConcept · 0..1 | befund | G9 | nein → Leitlinie | Spezialisierung von incidentalFinding | comorbidity | behalten |
| 42 | `screeningResultCategory` | Abschließendes Ergebnis der Früherkennungsuntersuchung | CodeableConcept · 1..1 | befund | G10 | ja → Pflicht | eigenständig (nimmt jointAssessment auf) | ctThoraxFinding | behalten |
| 43 | `recommendedManagement` | Empfehlung für das weitere Vorgehen | CodeableConcept · 1..1 | versorgungsplanung | G10 | ja → bedingt | eigenständig (Spezialisierung von recommendationsForPrimaryCare) | recommendationsForPrimaryCare | behalten |
| 44 | `recommendedControlInterval` | Empfohlenes Kontrollintervall bis zur nächsten Untersuchung (Monate) | Quantity · 0..1 | versorgungsplanung | G10 | ja → bedingt | eigenständig | followUpInterval; plannedFollowUpAppointment | behalten |
| 45 | `abnormalResultDiscussion` | Besprechung eines abklärungsbedürftigen Befunds | dateTime · 0..1 | kontakt-visite | G10 | ja → bedingt | eigenständig | consultationModality | behalten |
| 46 | `clarificationReferral` | Einleitung der Abklärung: Überweisung an spezialisierte Einrichtung | Reference · 0..* | mitbetreuung | G10 | ja → bedingt | Spezialisierung von referralOrder (primarycare) | referralOrder; tumorBoardDecision | behalten |
| 47 | `structuredScreeningReport` | Strukturierter Befundbericht der Lungenkrebsfrüherkennung | Reference · 1..1 | dokument | G10 | ja → Soll-Vorschrift | Spezialisierung von diagnosticReportDocument (primarycare) | diagnosticReportDocument | behalten |
| 48 | `resultCommunicationToPatient` | Übermittlung des Befundberichts (Zeitpunkt, Weg, Empfänger) | dateTime · 1..* | kontakt-visite | G10 | nein → keine | eigenständig (Übermittlungsereignis) | – | behalten |
| 49 | `screeningEpisode` | Teilnahme-Episode und Status in der Früherkennung | Period · 1..1 | versorgungskontext | G11 | nein → keine | eigenständig (EpisodeOfCare) | screeningProgramEnrolment | behalten |
| 50 | `participantExperienceFeedback` | Rückmeldung der Teilnehmenden (PREM, Belastung) | Reference · 0..* | prom | G11 | nein → keine | eigenständig, optional (projektspezifisch) | qualityOfLifeScore; distressThermometerScore | behalten |
| 51 | `screeningCaseConference` | Interdisziplinäre Fallkonferenz zum abklärungsbedürftigen Befund | CodeableConcept · 0..1 | versorgungsplanung | G12 | nein → Leitlinie | Spezialisierung von tumorBoardDecision (primarycare); Grenzfall des Scopes | tumorBoardDecision | behalten |
| 52 | `invasiveWorkupProcedure` | Folge- und Abklärungsmaßnahme nach Screeningbefund (inkl. Komplikation) | CodeableConcept · 0..* | prozedur | G12 | nein → Leitlinie | eigenständig; Grenzfall des Scopes | postTherapyComplication; treatmentSideEffectOrComplication | behalten |
| 53 | `workupOutcome` | Ergebnis der Abklärung eines abklärungsbedürftigen Befunds | CodeableConcept · 0..1 | diagnose | G12 | nein → keine | eigenständig; Grenzfall des Scopes (Rückkanal) | cancerDiagnosis; tnmStage; tumorHistology | behalten |

### 4.2 Einzelblätter (vollständige Kandidatentabelle mit allen Feldern)

#### G1 Zugang

##### 1. `screeningInvitation` – Aufforderung, Wiedereinladung, Erinnerung (Recall)

| Feld | Inhalt |
|---|---|
| Definition | Aufforderung, Wiedereinladung oder Erinnerung mit Zeitpunkt, Kanal, auffordernder Stelle und Anlass (Erstaufforderung, Jahresrunde, Kontroll-LDCT, Neubewertung). |
| Datentyp · Kardinalität · Kategorie | dateTime · 0..* · kontakt-visite (Vorschlag: Reference (FHIR Communication) · 0..*) |
| BPMN | Event_1uilxb6 „Person mit Risikofaktoren identifiziert“; Activity_0o694d5 „Versichterte Person zu LKS auffordern“; Event_1u8i3oa „Aufforderung versendet“; Event_0qh7lu0 „Aufforderung zum LKS erhalten“ (process_step: G1 Zugang \| Praxis: Versichterte Person zu LKS auffordern (Activity_0o694d5)) |
| Rolle | Praxis (Allgemeinmedizin, Innere Medizin, Arbeitsmedizin); optional Patientenportal |
| Trigger | Person mit Risikofaktoren identifiziert; fällige Jahresrunde, Kontroll-LDCT oder Neubewertung des Eignungsprofils |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **keine**. Kein gesetzliches Einladungs- oder Recall-Verfahren (Maßnahme nach § 25, kein Programm nach § 25a SGB V). S3 Tab. 14 Nr. 1 gilt nur für ein künftiges § 25a-Programm; S3 Kap. 5.1.4.5 (Hintergrund) hält Erinnerungen für erforderlich. |
| Quellen mit Zitat | [Q12] S3-LL Lungenkarzinom, Tab. 14, Kernelement 1: „Einladung und regelmäßige Wiedereinladung der Versicherten“ (Konsolidierung)<br>[Q12] S3-LL Lungenkarzinom 5.1, Kap. 5.1.4.5, S. 90 (Hintergrund): „zentralisierte und strukturierte Terminbuchungen bzw. Erinnerungen für das jährlich wiederkehrende Niedrigdosis-CT sowie gegebenenfalls vorgezogene 3- und 6-Monats-Kontrollen“<br>[Q02] KFE-RL, § 43 Abs. 2 S. 2 Nr. 2 (Fortbildungsinhalt): „Maßnahmen zur Ansprache der versicherten Person und Prüfung der Zulässigkeitsvoraussetzungen“<br>[Q05] KBV PraxisInfoSpezial (Oktober 2026), S. 4: „wendet er sich dann wieder an den Allgemeinmediziner oder Internisten, der die Kriterien für die Teilnahme prüft“ |
| Codes (Beleg, Bewertung) | SNOMED CT 185534005 *Letter invite to screening (procedure)* – Beleg: tx.fhir.org, SNOMED CT INT 20250201: aktiv – Bewertung: nur Kanal Brief; als Kanalwert verwenden<br>SNOMED CT 185535006 *Telephone invite to screening* – Beleg: tx.fhir.org INT 20250201; ECL <<308535007 auf r4.ontoserver.csiro.au (Gegenprüfung) – Bewertung: vorgeschlagen (Kanal Telefon)<br>SNOMED CT 185536007 *Verbal invite to screening* – Beleg: tx.fhir.org INT 20250201 (Gegenprüfung) – Bewertung: vorgeschlagen (Kanal mündlich) |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn recommendedControlInterval (mihub.lung.screening.recommendedControlInterval.v0.1); dependsOn plannedFollowUpAppointment (mihub.lung.primarycare.plannedFollowUpAppointment.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,55) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,65); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Fälligkeit aus recommendedControlInterval bzw. 12 Monate nach ldctExamination. |
| Umsetzung (Synthese) | Als Übermittlungsereignis modellieren (Communication: sent, medium, sender, reasonCode) statt dateTime. Kanal über SNOMED 185534005/185535006/185536007, lokal ergänzt um Portal/App; Anlass lokal (Erstaufforderung, Jahresrunde, Kontroll-LDCT, Neubewertung). Anlässe belegen mit KFE-RL § 38 Abs. 1, § 42 Abs. 3 Nr. 1, S3 Empf. 5.6 und KFE-RL § 43 Abs. 2 S. 2 Nr. 2. Fälligkeit nicht hier speichern, sondern aus recommendedControlInterval bzw. plannedFollowUpAppointment ableiten. S3 Tab. 14 Nr. 1 nur als Ausblick zitieren; in notes festhalten, dass das heutige Programm kein Einladungsverfahren hat. |
| Status | **behalten** – eigenständig, optional (pfad- und portalspezifisch) |

#### G2 Raucheranamnese (Q3)

##### 2. `smokingStatusScreening` – Raucherstatus bei Anspruchsprüfung

| Feld | Inhalt |
|---|---|
| Definition | Status des Tabakrauchens (täglich, gelegentlich, ehemals, nie, unbekannt) bei Anspruchsprüfung und Folgekontakten; steuert Unterbrechungsregel und Entwöhnungsangebot. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..1 · sozialanamnese |
| BPMN | Activity_0ya2ob0 „Zulässigkeitsvoraussetzungen prüfen (§2)“ (process_step: G2 Raucheranamnese \| Praxis: Zulässigkeitsvoraussetzungen prüfen (§2) (Activity_0ya2ob0)) |
| Rolle | berichterstellende Ärzt:in (Praxis); Selbstauskunft der Versicherten im Portal möglich |
| Trigger | jede Anspruchsprüfung (vor jeder Runde) und Folgekontakte; steuert Unterbrechungsregel und Entwöhnungsangebot |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **mittelbar**. Der Status allein entscheidet nicht über den Anspruch. Operative Norm: KFE-RL § 38 Abs. 1 i. V. m. LuKrFrühErkV § 2 Abs. 1 Nr. 3 Buchst. a und § 1 Abs. 2; KFE-RL § 37 Abs. 1 ist Zielbestimmung. |
| Quellen mit Zitat | [Q02] KFE-RL, § 37 Abs. 1: „Personen mit erhöhtem Lungenkrebsrisiko aufgrund von derzeitigem oder ehemaligem starken Zigarettenkonsum“ (Konsolidierung)<br>[Q02] KFE-RL, § 37 Abs. 1 (Zielbestimmung): „Ziel der Früherkennungsuntersuchung auf Lungenkrebs ist die frühzeitige Entdeckung von Lungenkarzinomen bei Personen mit erhöhtem Lungenkrebsrisiko aufgrund von derzeitigem oder ehemaligem starken Zigarettenkonsum“<br>[Q03] G-BA Tragende Gründe 18.06.2025, Abschn. 2.1, S. 3: „wobei der Zigarettenkonsum noch andauert oder vor weniger als 10 Jahren beendet wurde“<br>[Q04] G-BA Versicherteninformation, S. 4: „Sie rauchen aktuell oder haben früher stark geraucht“ |
| Codes (Beleg, Bewertung) | LOINC 72166-2 *Tobacco smoking status* – Beleg: tx.fhir.org $lookup, LOINC 2.82: ACTIVE, Antwortliste LL2201-3 – Bewertung: Observation.code (in ISiKRaucherStatus fixiert)<br>LOINC LA15920-4 *Former smoker* – Beleg: tx.fhir.org, LOINC 2.82; Bestandteil von LL2201-3 – Bewertung: Wert aus LL2201-3<br>SNOMED CT 8517006 *Ex-smoker* – Beleg: tx.fhir.org, SNOMED CT INT 20250201: aktiv – Bewertung: nur Mapping |
| Bezug zum Bestand | overlaps_existing: smokingStatus (followup) – Phase screening ergänzen. Vorgeschlagene Relationen: specializes smokingStatus (mihub.lung.followup.smokingStatus.v0.2) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,65) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,70); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Nur mittelbar Pflicht. Profilbasis ISiKRaucherStatus (LL2201-3), IPS-kompatibel; NCIt als Mapping. |
| Umsetzung (Synthese) | Als Phasen-Pendant mit specializes mihub.lung.followup.smokingStatus.v0.2 anlegen (Präzedenz ecogPerformanceStatusSurveillance). Werte an die LOINC-Antwortliste LL2201-3 binden (ISiKRaucherStatus: required), SNOMED CT nur als Mapping. E-Zigarette und Passivrauch nicht im Status führen, sondern in otherTobaccoNicotineProductUse bzw. einem Expositionselement. Klarstellen, dass für Anspruch und Unterbrechungsregel der Zigarettenstatus zählt (nur Zigaretten, TrG S. 17). Das nicht existierende MII-Mapping (…/modul-person/StructureDefinition/Raucher) nicht übernehmen und in smokingStatus korrigieren. |
| Status | **behalten** – Spezialisierung von smokingStatus (followup) |

##### 3. `cigaretteConsumptionPeriod` – Konsumabschnitt Zigarettenrauchen

| Feld | Inhalt |
|---|---|
| Definition | Zeitraum (Beginn, Ende, mind. Jahr) mit annähernd gleichem Zigarettenkonsum; Abschnitte bilden die Raucheranamnese, erster Beginn = Rauchbeginn. |
| Datentyp · Kardinalität · Kategorie | Period · 1..* · sozialanamnese (Vorschlag: 1..*) |
| BPMN | Activity_0ya2ob0 „Zulässigkeitsvoraussetzungen prüfen (§2)“ (process_step: G2 Raucheranamnese \| Praxis: Activity_0ya2ob0; Selbstauskunft vorab (Portal)) |
| Rolle | berichterstellende Ärzt:in; Selbstauskunft der Versicherten (Portal) |
| Trigger | Erstprüfung; Aktualisierung vor jeder Runde |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **mittelbar**. Rechengrundlage nach LuKrFrühErkV § 1 Abs. 2 S. 2–4 und § 2 Abs. 1 S. 1 Nr. 3 Buchst. a Doppelbuchst. aa (Dauer); Erhebungspflicht KFE-RL § 39 Nr. 1. Die Abschnittsstruktur ist eine Modellentscheidung; ohne vollständige Unterbrechung genügt ein Abschnitt. |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 1 Abs. 2: „für jedes Jahr des Zigarettenkonsums die im Jahresdurchschnitt pro Tag gerauchte Anzahl der Zigaretten durch 20 zu …“ (Konsolidierung)<br>[Q01] LuKrFrühErkV, § 1 Abs. 2 S. 2: „Zur Ermittlung des Zigarettenkonsums in Packungsjahren ist für jedes Jahr des Zigarettenkonsums die im Jahresdurchschnitt pro Tag gerauchte Anzahl der Zigaretten durch 20 zu teilen.“<br>[Q02] KFE-RL, § 39 Nr. 1: „Erhebung der relevanten anamnestischen Daten“ |
| Codes (Beleg, Bewertung) | SNOMED CT 230056004 *Cigarette consumption (observable entity)* – Beleg: tx.fhir.org, SNOMED CT INT 20250201: aktiv – Bewertung: Näherung (Menge, kein Zeitraum); gemeinsamer Observation.code mit cigarettesPerDayInPeriod<br>SNOMED CT 228488005 *Age at starting smoking (observable entity)* – Beleg: tx.fhir.org, INT 20250201: aktiv – Bewertung: streichen (Alters-Observable, passt nicht zu Period)<br>openEHR at0064 *Per episode (tobacco_smoking_summary.v2)* – Beleg: ADL aus CKM-Mirror, Revision 2.0.1 (published) – Bewertung: als standard_mappings führen, nicht als Coding |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: hasPart cigarettesPerDayInPeriod (mihub.lung.screening.cigarettesPerDayInPeriod.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,75) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,80); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Pflicht mittelbar (Rechengrundlage § 1 Abs. 2); Episodenmodell nach openEHR, kein FHIR-Profil. |
| Umsetzung (Synthese) | Kopf-Element „Konsumabschnitt“ (Period 1..*, Beginn und Ende mindestens jahrgenau) mit hasPart cigarettesPerDayInPeriod; als eine FHIR Observation abbilden (code 230056004, effectivePeriod = Abschnitt, valueQuantity = Zigaretten pro Tag). openEHR tobacco_smoking_summary.v2 als standard_mapping (Pfad /data[at0001]/items[at0029]/items[at0064]), nicht als Coding. 228488005 streichen (Rauchbeginn ableitbar). constraints_de: nur Zigaretten (TrG zu § 39 Nr. 1), Abschnitte überlappungsfrei. Quellen ergänzen: § 2 Abs. 1 S. 1 Nr. 3 Buchst. a Doppelbuchst. aa und KFE-RL § 39 Nr. 1. |
| Status | **behalten** – eigenständig (Kopf-Element der Raucheranamnese Q3) |

##### 4. `cigarettesPerDayInPeriod` – Zigaretten pro Tag im Jahresdurchschnitt je Konsumabschnitt

| Feld | Inhalt |
|---|---|
| Definition | Im Jahresdurchschnitt pro Tag gerauchte Zigaretten je Konsumabschnitt; Basis der Packungsjahre (÷ 20), NELSON-Kriterien und PLCOm2012. |
| Datentyp · Kardinalität · Kategorie | Quantity · 1..* · sozialanamnese (Vorschlag: 1..1 je Abschnitt (insgesamt 1..*)) |
| BPMN | Activity_0ya2ob0 „Zulässigkeitsvoraussetzungen prüfen (§2)“ (process_step: G2 Raucheranamnese \| Praxis: Activity_0ya2ob0) |
| Rolle | berichterstellende Ärzt:in; Selbstauskunft (Portal) |
| Trigger | je Konsumabschnitt bei der Anspruchsprüfung |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **mittelbar**. LuKrFrühErkV § 1 Abs. 2 S. 2 (im Jahresdurchschnitt pro Tag gerauchte Zigaretten, geteilt durch 20); KFE-RL § 39 Nr. 1. S3 Statement 5.2 ist ein Statement (ST, LoE 1) mit NELSON-Schwellen, keine Empfehlung. |
| Quellen mit Zitat | [Q12] S3-LL Lungenkarzinom, Statement 5.2: „einer Raucheranamnese von ≥ 15 Zigaretten/Tag für mindestens 25 Jahre oder ≥ 10 Zigaretten pro Tag für mindestens …“ (Konsolidierung)<br>[Q01] LuKrFrühErkV, § 1 Abs. 2 S. 2: „für jedes Jahr des Zigarettenkonsums die im Jahresdurchschnitt pro Tag gerauchte Anzahl der Zigaretten durch 20 zu teilen“ |
| Codes (Beleg, Bewertung) | SNOMED CT 230056004 *Cigarette consumption (observable entity)* – Beleg: tx.fhir.org, INT 20250201: aktiv – Bewertung: Observation.code, gemeinsam mit dem Abschnitt<br>LOINC 8663-7 *Cigarettes smoked current (pack per day) - Reported* – Beleg: tx.fhir.org, LOINC 2.82 – Bewertung: nicht verwenden (aktueller Konsum in Packungen pro Tag)<br>SNOMED CT 1368921000168102 *Cigarettes per day* – Beleg: Ontoserver-ECL <<230056004: nur australische Extension – Bewertung: nicht verwenden (nicht in INT) |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: isPartOf cigaretteConsumptionPeriod (mihub.lung.screening.cigaretteConsumptionPeriod.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,65) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,75); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Einheit /d; LOINC 8663-7 nur aktueller Konsum; NELSON-Ableitungsregel offen. |
| Umsetzung (Synthese) | isPartOf cigaretteConsumptionPeriod; Einheit UCUM „/d“ bzw. „{Zigaretten}/d“, Jahresdurchschnitt in instruction_de erläutern. Primärquelle auf LuKrFrühErkV § 1 Abs. 2 S. 2 umstellen; S3 5.2 als Statement für die NELSON-Schwellen führen. NELSON-Ableitung (≥ 15 Zigaretten/Tag über ≥ 25 Jahre bzw. ≥ 10 über ≥ 30 Jahre) und Packungsjahre als abgeleitete Größen beim Packungsjahr-Element führen; die Ableitungsregel bei wechselnder Intensität ist offen (E1). Für PLCOm2012 wäre eine eigene Primärquelle nötig. |
| Status | **behalten** – Teil von cigaretteConsumptionPeriod |

##### 5. `smokingInterruptionPeriod` – Vollständige Rauchunterbrechung

| Feld | Inhalt |
|---|---|
| Definition | Zeitraum vollständiger Rauchunterbrechung; Konsum und Jahre davor sowie Unterbrechungsjahre zählen nur bei Unterbrechung unter zehn Jahren. |
| Datentyp · Kardinalität · Kategorie | Period · 0..* · sozialanamnese |
| BPMN | Activity_0ya2ob0 „Zulässigkeitsvoraussetzungen prüfen (§2)“ (process_step: G2 Raucheranamnese \| Praxis: Activity_0ya2ob0) |
| Rolle | berichterstellende Ärzt:in; Selbstauskunft (Portal) |
| Trigger | bei der Anspruchsprüfung, wenn der Zigarettenkonsum vollständig unterbrochen war oder beendet ist |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **mittelbar**. LuKrFrühErkV § 1 Abs. 2 S. 4 (Packungsjahre) und § 2 Abs. 1 S. 1 Nr. 3 Buchst. a Doppelbuchst. aa (Dauer). Laufende Abstinenz wie Unterbrechung: G-BA-Auslegung (TrG Abschn. 2.1 mit Fn. 7), kein Verordnungstext. |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 1 Abs. 2 S. 4: „Der Zigarettenkonsum vor einer vollständigen Unterbrechung des Rauchens ist nur dann mitzuzählen, wenn die …“ (Konsolidierung)<br>[Q01] LuKrFrühErkV, § 2 Abs. 1 S. 1 Nr. 3 Buchst. a Doppelbuchst. aa: „mit einer Dauer von mindestens 25 Jahren, wobei die Jahre vor einer vollständigen Unterbrechung des Rauchens und die Jahre der vollständigen Unterbrechung selbst nur mitgezählt werden, wenn die Unterbrechung weniger als zehn Jahre beträgt“<br>[Q04] G-BA Versicherteninformation, S. 4: „Rauchpausen innerhalb dieser Zeit dürfen nicht länger als 10 Jahre gewesen sein.“ |
| Codes (Beleg, Bewertung) | LOINC 107339-4 *Temporary smoking cessation [Time]* – Beleg: tx.fhir.org, LOINC 2.82: ACTIVE; Property Time, Scale Qn, Einheiten d/wk/mo/a – Bewertung: nur Mapping der Dauer, nicht des Zeitraums; deckt laufende Abstinenz nicht ab |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn cigaretteConsumptionPeriod (mihub.lung.screening.cigaretteConsumptionPeriod.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,75) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,60); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Kein SNOMED-Konzept; offen, ob laufende Abstinenz als Unterbrechung gilt. |
| Umsetzung (Synthese) | Period 0..*; eine laufende Unterbrechung ohne Ende zulassen. Konsistenzregel: keine Überlappung mit cigaretteConsumptionPeriod; dependsOn cigaretteConsumptionPeriod. LOINC 107339-4 nur als Mapping der Dauer verwenden (valueQuantity in a bzw. mo) oder weglassen. Notiz ersetzen: „Der G-BA wendet die 10-Jahres-Regel auch auf beendeten Konsum an (TrG 18.06.2025, Abschn. 2.1 mit Fn. 7); das ist Auslegung, nicht Verordnungstext.“ Offen (E2): Zählt das Rauchen anderer Produkte als Unterbrechung des „Rauchens“? |
| Status | **behalten** – eigenständig (Raucheranamnese Q3) |

##### 6. `otherTobaccoNicotineProductUse` – Weitere Tabak- und Nikotinprodukte (nicht anrechenbar)

| Feld | Inhalt |
|---|---|
| Definition | Konsum anderer Produkte als Zigaretten (Zigarre, Pfeife, Shisha, E-Zigarette, Tabakerhitzer, rauchloser Tabak, Nikotinbeutel); nicht anrechenbar. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 0..* · sozialanamnese |
| BPMN | Activity_0ya2ob0 „Zulässigkeitsvoraussetzungen prüfen (§2)“ (process_step: G2 Raucheranamnese \| Praxis: Activity_0ya2ob0) |
| Rolle | berichterstellende Ärzt:in; Selbstauskunft (Portal) |
| Trigger | Anspruchsprüfung und Folgekontakte |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. Nicht anrechenbar (Begründung zur LuKrFrühErkV, zitiert in den TrG, S. 17). Erfassungsempfehlung: S3-LL Rauchen und Tabakabhängigkeit Empf. 3.3.3.1 (A; Teil „verwandte Produkte“ als Konsenspunkt; Gültigkeit abgelaufen, in Überarbeitung). S3-LL Lungenkarzinom Empf. 4.2 gilt nur für Erkrankte. |
| Quellen mit Zitat | [Q03] G-BA Tragende Gründe KFE-RL, zu § 39 Nr. 1: „Von dem Begriff „Zigarettenkonsum“ wird nur der Konsum von Zigaretten, nicht aber von anderen Tabakprodukten, wie …“ (Konsolidierung)<br>[Q13] S3-LL Rauchen und Tabakabhängigkeit (AWMF 076-006), Empf. 3.3.3.1, S. 47: „Der Konsum von Tabak und verwandten Produkten soll in der Patientendokumentation erfasst werden.“ |
| Codes (Beleg, Bewertung) | LOINC 81228-9 *Tobacco product* – Beleg: tx.fhir.org, LOINC 2.82; Antwortliste LL3975-1 nur Cigarettes, Cigars, Pipe tobacco, Smokeless tobacco – Bewertung: nur Fragecode<br>SNOMED CT 722499006 *Electronic cigarette user* – Beleg: tx.fhir.org, INT 20250201: aktiv – Bewertung: Wert<br>SNOMED CT 1388653002 *Uses heated tobacco product* – Beleg: CSIRO Ontoserver: Modul 900000000000207008 (INT), effectiveTime 20260301, aktiv – Bewertung: Wert; setzt SNOMED CT INT ab 2026-03-01 voraus |
| Bezug zum Bestand | overlaps_existing: smokingStatus (führt E-Zigarette als Status). Vorgeschlagene Relationen: – |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,55) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,60); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Nikotinbeutel lokal; Tabakerhitzer-Konzept existiert seit INT 20260301 (Korrektur standards). |
| Umsetzung (Synthese) | Als 0..*-Produktelement behalten. LOINC 81228-9 nur als Fragecode, Werte über SNOMED CT (722499006, 1388653002; Nikotinbeutel lokal). Produktliste mit der Quelle abgleichen (Nikotinpflaster bewusst ein- oder ausschließen). E-Zigarette und Passivrauch aus dem Status nehmen (smokingStatusScreening, perspektivisch smokingStatus) und den smokingStatus-Issue „verwandte Produkte“ über related_elements hierauf auflösen. Fundstelle präzisieren: TrG „Zu § 39 Nr. 1 Satz 1 2. Halbsatz – Begriffserläuterung Zigarettenkonsum“, S. 17. |
| Status | **behalten** – eigenständig (Raucheranamnese Q3) |

##### 7. `creditableSmokingDurationYears` – Anrechenbare Dauer des Zigarettenkonsums (Jahre)

| Feld | Inhalt |
|---|---|
| Definition | Rauchdauer nach Zählregel § 2 Abs. 1 Nr. 3 a aa LuKrFrühErkV (Unterbrechungen < 10 Jahre zählen mit), aus Abschnitten abgeleitet; Kriterium ≥ 25 Jahre. |
| Datentyp · Kardinalität · Kategorie | Quantity · 1..1 · sozialanamnese (Vorschlag: 0..1) |
| BPMN | Activity_0ya2ob0 „Zulässigkeitsvoraussetzungen prüfen (§2)“; Activity_1npn3bx „Bericht erstellen (§2 Abs.1 Nr.3)“ (process_step: G2 Raucheranamnese \| Praxis: Activity_0ya2ob0 → Bericht erstellen (Activity_1npn3bx)) |
| Rolle | berichterstellende Ärzt:in (berechneter Wert) |
| Trigger | bei der Anspruchsprüfung abgeleitet; Inhalt des Berichts |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. Das Kriterium (mindestens 25 anrechenbare Jahre) muss aus dem Bericht hervorgehen: LuKrFrühErkV § 2 Abs. 1 S. 1 Nr. 3 Buchst. a Doppelbuchst. aa; KFE-RL § 38 Abs. 1, § 39 Nr. 1. Der Zahlenwert selbst ist eine Modellentscheidung. |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 2 Abs. 1 Nr. 3 a aa: „mit einer Dauer von mindestens 25 Jahren, wobei die Jahre vor einer vollständigen Unterbrechung des Rauchens und …“ (Konsolidierung)<br>[X05] KVBB-Musterbericht (PDF 12.05.2026), Ankreuzfeld: „Zeitraum: Dauer von min. 25 Jahren ☐“<br>[Q11] KVBW-Vorlage (Juni 2026), Ja/Nein-Feld: „mindestens 25 Jahre geraucht?“ |
| Codes (Beleg, Bewertung) | SNOMED CT 228487000 *Total time smoked (observable entity)* – Beleg: tx.fhir.org INT 20250201 und Ontoserver: aktiv – Bewertung: Näherung (tatsächlich gerauchte Zeit)<br>LOINC 88029-4 *Tobacco use duration* – Beleg: tx.fhir.org, LOINC 2.82: ACTIVE, UCUM a – Bewertung: Näherung (Tabak allgemein) |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn cigaretteConsumptionPeriod (mihub.lung.screening.cigaretteConsumptionPeriod.v0.1); dependsOn smokingInterruptionPeriod (mihub.lung.screening.smokingInterruptionPeriod.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,65); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Standardcodes meinen tatsächlich gerauchte Zeit → Zählregel kennzeichnen. |
| Umsetzung (Synthese) | Als abgeleiteten Wert führen (data_flows usage_type derive; dependsOn cigaretteConsumptionPeriod und smokingInterruptionPeriod), Einheit UCUM a. Definition vollständig fassen: Jahre vor einer Unterbrechung von 10 oder mehr Jahren entfallen, Unterbrechungsjahre unter 10 Jahren zählen mit, nur Zigaretten. Der Kriteriumsnachweis (ja/nein) gehört in eligibilityCheckResult bzw. eligibilityReport. Codes nur als Näherung mit Hinweis auf die Zählregel. |
| Status | **behalten** – abgeleitet (aus Konsumabschnitten und Unterbrechungen) |

##### 8. `packYearsCalculated` – Packungsjahre (jahrweise nach § 1 Abs. 2 LuKrFrühErkV)

| Feld | Inhalt |
|---|---|
| Definition | Summe je anrechenbares Jahr aus Zigaretten/Tag ÷ 20; ohne Konsum vor Unterbrechungen ≥ 10 Jahre; nur Zigaretten. Kriterium ≥ 15. |
| Datentyp · Kardinalität · Kategorie | Quantity · 1..1 · sozialanamnese (Vorschlag: 0..1 je Prüfung) |
| BPMN | Activity_0ya2ob0 „Zulässigkeitsvoraussetzungen prüfen (§2)“; Activity_1npn3bx „Bericht erstellen (§2 Abs.1 Nr.3)“ (process_step: G2 Raucheranamnese \| Praxis: Activity_0ya2ob0 → Bericht erstellen (Activity_1npn3bx)) |
| Rolle | berichterstellende Ärzt:in (berechnet); Selbstschätzung der Versicherten als Methode |
| Trigger | bei der Anspruchsprüfung; Inhalt des Berichts |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. Kriterium (mindestens 15 Packungsjahre) im Bericht: LuKrFrühErkV § 2 Abs. 1 S. 1 Nr. 3 Buchst. a Doppelbuchst. bb i. V. m. § 1 Abs. 2 S. 1–4; KFE-RL § 39 Nr. 1. Der Zahlenwert ist nicht zwingend. |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 1 Abs. 2; § 2 Abs. 1 Nr. 3 a bb: „Die nach Satz 2 errechneten Ergebnisse der einzelnen Jahre sind zu addieren.“ (Konsolidierung)<br>[Q01] LuKrFrühErkV, § 1 Abs. 2 S. 1: „Packungsjahr ist die Einheit, in der der Zigarettenkonsum angegeben wird.“<br>[Q05] KBV PraxisInfoSpezial (Oktober 2026), Anspruchsberechtigung: „(Packungsjahre: Zahl der pro Tag gerauchten Zigarettenpackungen multipliziert mit der Zahl der Raucherjahre)“ |
| Codes (Beleg, Bewertung) | SNOMED CT 401201003 *Cigarette pack-years (observable entity)* – Beleg: tx.fhir.org INT 20250201, Ontoserver INT 20260601: aktiv; Elternkonzept 230056004 – Bewertung: Primärcode (nur Zigaretten)<br>SNOMED CT 782516008 *Number of calculated pack years for cumulative lifetime tobacco exposure* – Beleg: tx.fhir.org, Ontoserver: aktiv – Bewertung: nur breiteres Mapping (Tabak gesamt, nicht die Zählregel der Verordnung)<br>LOINC 8664-5 *Cigarettes smoked total (pack per year) - Reported* – Beleg: tx.fhir.org, LOINC 2.82: ACTIVE, Property NRat – Bewertung: Mapping (Methode „Reported“) |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn cigaretteConsumptionPeriod (mihub.lung.screening.cigaretteConsumptionPeriod.v0.1); dependsOn cigarettesPerDayInPeriod (mihub.lung.screening.cigarettesPerDayInPeriod.v0.1); dependsOn smokingInterruptionPeriod (mihub.lung.screening.smokingInterruptionPeriod.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,80); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Einheit {pack-years}; KV-Vorlagen und ACR-Formel nicht jahrweise; eigenes Q3-Profil nötig. |
| Umsetzung (Synthese) | Als generisches Element „Packungsjahre“ (nur Zigaretten) führen; Rechenweg als Methode (jahrweise nach § 1 Abs. 2 \| vereinfachte Schätzung nach KBV/KV \| Selbstschätzung) und Urheber (Ärzt:in \| Versicherte) statt im Namen. Primärcode SNOMED 401201003; LOINC 8664-5 als Observation.code-Mapping (Methode „Reported“); 782516008 höchstens als breiteres Mapping (Tabak gesamt). Einheit an den gewählten Code anpassen. Kriterium ≥ 15 in eligibilityCheckResult. Eigenes Q3-Profil nötig, weil ISiK und IPS keine Packungsjahre kennen. |
| Status | **behalten** – eigenständig (generalisiert; nimmt packYearsSelfEstimate auf) |

#### G3 Zulässigkeit/Eignung

##### 9. `lastQualifyingChestCtDate` – Datum der letzten befundungsgeeigneten Thorax-CT

| Feld | Inhalt |
|---|---|
| Definition | Datum der letzten befundungsgeeigneten Lungen-CT (Screening oder anderer Anlass) mit Anlass; reguläre LDCT frühestens zwölf Monate danach. |
| Datentyp · Kardinalität · Kategorie | date · 0..1 · bildgebung (Vorschlag: Reference bzw. date mit Qualifiern) |
| BPMN | Activity_0ya2ob0 „Zulässigkeitsvoraussetzungen prüfen (§2)“; Activity_0l9ecr6 „Rechtfertigende Indikation stellen und Voruntersuchung prüfen (§3 und §4 Abs.2)“ (process_step: G3 Zulässigkeit \| Praxis: Activity_0ya2ob0; Radiologie: Activity_0l9ecr6) |
| Rolle | Praxis (Anamnese); Erstbefunder (Prüfung der Voraufnahme) |
| Trigger | jede Anspruchsprüfung und jede Indikationsstellung |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. Zulässig nur, wenn die letzte befundungsgeeignete Lungen-CT mindestens zwölf Monate zurückliegt: LuKrFrühErkV § 2 Abs. 1 Nr. 2; KFE-RL § 38 Abs. 2; Ausnahme nach kontrollbedürftigem Befund (§ 2 Abs. 2). Die Vorlagen führen das Kriterium nur als Ja/Nein. |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 2 Abs. 1 Nr. 2: „bei denen die letzte Untersuchung der Lunge mittels Computertomographie, die qualitativ zur Befundung im Hinblick …“ (Konsolidierung)<br>[Q02] KFE-RL, § 38 Abs. 2: „Erfolgte innerhalb der letzten 12 Monate … bereits aus anderen Gründen eine Untersuchung der Lunge mittels Computertomographie und ist diese Voraufnahme qualitativ zur Befundung im Hinblick auf ein Lungenkarzinom geeignet“<br>[Q03] G-BA Tragende Gründe 18.06.2025, zu § 38 Abs. 2, S. 16: „mindestens die gesamte Lunge in der erforderlichen Bildqualität“ |
| Codes (Beleg, Bewertung) | SNOMED CT 169069000 *CT of chest* – Beleg: tx.fhir.org INT 20250201, Ontoserver INT 20260601: aktiv – Bewertung: Näherung; Kindkonzept 713548006 (LDCT) wird subsumiert |
| Bezug zum Bestand | overlaps_existing: ctThoraxScan. Vorgeschlagene Relationen: specializes ctThoraxScan (mihub.lung.followup.ctThoraxScan.v0.1); dependsOn diagnosticReportDocument (mihub.lung.primarycare.diagnosticReportDocument.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,60); vollständige Urteile in candidates.json |
| Umsetzung (Synthese) | Als Erweiterung von ctThoraxScan modellieren (phasenübergreifende Thorax-CT-Vorgeschichte oder Screening-Spezialisierung mit specializes): Datum (Teilpräzision zulässig), Anlass/Herkunft (Screening \| andere Indikation \| extern/anamnestisch), Qualifier „befundungsgeeignet für Lungenkarzinom“ (boolean), Verweis auf diagnosticReportDocument bzw. ImagingStudy mit Befundkategorie (für § 2 Abs. 2). „Letzte“ als Abfrage, die 12-Monats-Regel als Constraint in eligibilityCheckResult. Label „befundungsgeeignete Lungen-CT“. KFE-RL § 38 Abs. 2 und TrG zu § 38 Abs. 2 ergänzen. |
| Status | **behalten** – Erweiterung von ctThoraxScan (Thorax-CT-Vorgeschichte) |

##### 10. `symptomAndLungCancerCareStatus` – Asymptomatik und kein laufender Lungenkrebs-Behandlungskontext

| Feld | Inhalt |
|---|---|
| Definition | Feststellung, ob die Person asymptomatisch ist und nicht wegen Lungenkrebs in (Nach-)Behandlung; sonst kurative Versorgung statt Früherkennung. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..1 · befund |
| BPMN | Activity_0ya2ob0 „Zulässigkeitsvoraussetzungen prüfen (§2)“; Gateway_1whuu15 „Voraussetzungen erfüllt?“ (process_step: G3 Zulässigkeit \| Praxis: Activity_0ya2ob0 → Voraussetzungen erfüllt? (Gateway_1whuu15)) |
| Rolle | berichterstellende Ärzt:in (Praxis) |
| Trigger | jede Anspruchsprüfung (erneut bei Indikationsstellung) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **mittelbar**. Früherkennung nur bei Personen ohne Krankheitssymptome und ohne konkreten Verdacht (StrlSchG § 5 Abs. 16); Behandlung, Nachbehandlung oder Verdacht führen in die kurative Versorgung (KFE-RL § 38 Abs. 3). |
| Quellen mit Zitat | [Q02] KFE-RL, § 38 Abs. 3: „Versicherte, die sich aufgrund einer Lungenkrebserkrankung in ärztlicher Behandlung oder Nachbehandlung befinden …“ (Konsolidierung)<br>[Q09] StrlSchG, § 5 Abs. 16: „Personen, die keine Krankheitssymptome und keinen konkreten Krankheitsverdacht aufweisen“<br>[Q02] KFE-RL, § 38 Abs. 3 (Fortsetzung): „oder bei denen aufgrund von Vorliegen typischer Symptome ein konkreter Verdacht auf eine Lungenkrebserkrankung besteht, haben Anspruch auf die notwendige ärztliche Betreuung und Behandlung innerhalb der kurativen Versorgung.“<br>[X05] KVBB-Musterbericht (PDF 12.05.2026), Feld: „Ist eine Lungenkrebserkrankung bekannt Ja ☐ Nein ☐“ |
| Codes (Beleg, Bewertung) | SNOMED CT 84387000 *Asymptomatic (finding)* – Beleg: tx.fhir.org INT 20250201, Ontoserver: aktiv – Bewertung: Wert<br>SNOMED CT 162573006 *Suspected lung cancer (situation)* – Beleg: tx.fhir.org INT 20250201: aktiv; Vorzugsbegriff in INT 20260601 „Malignant neoplasm of lung suspected“ – Bewertung: Wert; Display nachziehen<br>SNOMED CT 139841002 *Suspected lung cancer (inaktiv)* – Beleg: tx.fhir.org: inaktiv – Bewertung: nicht verwenden |
| Bezug zum Bestand | overlaps_existing: cancerDiagnosis; currentTumorStatus; screeningProgramEnrolment. Vorgeschlagene Relationen: dependsOn cancerDiagnosis (mihub.lung.primarycare.cancerDiagnosis.v0.1); dependsOn treatmentStatus (mihub.lung.primarycare.treatmentStatus.v0.1); dependsOn screeningProgramEnrolment (mihub.lung.followup.screeningProgramEnrolment.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,70); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | 139841002 inaktiv; Spannung zu S3 16.7 (Screening nach Nachsorge). |
| Umsetzung (Synthese) | Auf den Status zu Symptomen und Verdacht reduzieren (z. B. Name symptomStatusAtEligibilityCheck): asymptomatisch (84387000) \| typische Symptome mit konkretem Verdacht (162573006), optional mit Symptomliste (z. B. Onkopedia NSCLC 04/2025, Tab. 1). Den Behandlungskontext nicht erfassen, sondern als Constraint aus cancerDiagnosis, treatmentStatus und screeningProgramEnrolment ableiten. Zitat um den Symptomteil vervollständigen; StrlSchG § 5 Abs. 16 und TrG zu § 38 Abs. 3 ergänzen. Widerspruch KFE-RL § 38 Abs. 3 („Nachbehandlung“) zu S3 Empf. 16.7 klären (E7). |
| Status | **behalten** – eigenständig, reduziert auf Symptom- und Verdachtsstatus |

##### 11. `medicalSuitabilityProfile` – Medizinisches Eignungsprofil

| Feld | Inhalt |
|---|---|
| Definition | Ärztliche Beurteilung der Eignung für kurativ intendierte Behandlung und ausreichender Lebenserwartung, inkl. hoher Komorbiditätslast. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..1 · assessment |
| BPMN | Activity_0ya2ob0 „Zulässigkeitsvoraussetzungen prüfen (§2)“; Activity_1npn3bx „Bericht erstellen (§2 Abs.1 Nr.3)“ (process_step: G3 Eignung \| Praxis: Activity_0ya2ob0 → Bericht erstellen (Activity_1npn3bx)) |
| Rolle | berichterstellende Ärzt:in (Praxis) |
| Trigger | Erstprüfung; erneute Prüfung nach S3 Empf. 5.6 |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. LuKrFrühErkV § 2 Abs. 1 S. 1 Nr. 3 Buchst. b; KFE-RL § 39 Nr. 1 („das Vorliegen des medizinischen Eignungsprofils“). Der Inhalt ist nicht legaldefiniert (S3 Empf. 5.5, EK). |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 2 Abs. 1 Nr. 3 b: „ein medizinisches Eignungsprofil der zu untersuchenden Person und die hierfür relevanten anamnestischen Daten“ (Konsolidierung)<br>[Q12] S3-LL Lungenkarzinom 5.1, Empf. 5.5 (EK): „die für eine kurativ intendierte Lungenkrebs-Behandlung geeignet sind“<br>[Q12] S3-LL Lungenkarzinom 5.1, Empf. 5.5 (EK): „Während die aktuell noch unzureichende Evidenz keine Definition von eindeutigen Ausschlusskriterien in Bezug auf die medizinische Eignung erlaubt“<br>[Q15] Whitepaper Blum et al. 2026, Supplement, Abb. S 6 (Prüfbericht): „würde sich die Person für eine Therapie des Lungenkarzinoms grundsätzlich eignen („medizinisches Eignungsprofil“)“ |
| Codes (Beleg, Bewertung) | SNOMED CT 762713009 *Charlson Comorbidity Index (assessment scale)* – Beleg: tx.fhir.org INT 20250201, Ontoserver: aktiv – Bewertung: als Elementcode streichen (Instrument, keine Eignungsbeurteilung)<br>SNOMED CT 713671003 *Medically fit for surgery (finding)* – Beleg: tx.fhir.org, INT 20250201: aktiv (Gegenprüfung) – Bewertung: als Teilmapping prüfen |
| Bezug zum Bestand | overlaps_existing: comorbidity. Vorgeschlagene Relationen: dependsOn comorbidity (mihub.lung.primarycare.comorbidity.v0.1); dependsOn ecogPerformanceStatus (mihub.lung.followup.ecogPerformanceStatus.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,80) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,80); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Keine konsentierten Ausschlusskriterien (S3 5.5); Werteliste lokal. |
| Umsetzung (Synthese) | Lokale Werteliste: geeignet \| nicht geeignet \| geeignet mit Hinweis auf erhöhtes Risiko von Überdiagnose und Übertherapie (S3 Empf. 5.5/5.6); standard_binding_status no-standard-found. 762713009 als Elementcode streichen; einen CCI-Wert über standardizedAssessmentScore erfassen. Belege per Verweis anbinden (dependsOn comorbidity, ecogPerformanceStatus u. a.); inhaltlich verwandt mit curativeRecurrencePotential. Teilmapping SNOMED 713671003 prüfen. Die Fälligkeit der Wiederholung als Attribut führen (eligibilityProfileReviewDueDate). Hinweis: S3 zitiert „§ 2 Abs. 1 Satz 3“, richtig ist Satz 1 Nr. 3 Buchst. b. |
| Status | **behalten** – eigenständig |

##### 12. `eligibilityProfileReviewDueDate` – Fälligkeit der erneuten Prüfung des Eignungsprofils

| Feld | Inhalt |
|---|---|
| Definition | Fälligkeit der erneuten Eignungsprüfung nach erster LDCT: bis 70 J. alle 5 Jahre, 70–75 J. mind. alle 3 Jahre, vorgezogen bei neuer Komorbidität. |
| Datentyp · Kardinalität · Kategorie | date · 0..1 · versorgungsplanung |
| BPMN | Event_1d2c01e „Anfrage erhalten“ (process_step: G3 Eignung \| Praxis: Wiedereintritt Anfrage erhalten (Event_1d2c01e); im BPMN fehlend) |
| Rolle | Praxis (berechneter Wert) |
| Trigger | nach der ersten LDCT, bei jeder Eignungsprüfung neu berechnet; vorgezogen bei neuer hoher Komorbiditätslast |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. S3 Empf. 5.6 (EK, „sollten“); keine Rechtspflicht. Im BPMN fehlt ein Schritt für die erneute Prüfung. |
| Quellen mit Zitat | [Q12] S3-LL Lungenkarzinom, Empf. 5.6 (EK): „bis zu einem Alter von 70 Jahren alle 5 Jahre sowie im Alter von 70 bis 75 Jahren mindestens alle 3 Jahre eine …“ (Konsolidierung)<br>[Q12] S3-LL Lungenkarzinom 5.1, Empf. 5.6 (EK): „ggf. vorgezogen bei Bekanntwerden einer neuen hohen Komorbiditätslast“ |
| Codes (Beleg, Bewertung) | keine Codes beansprucht; lokale Werteliste bzw. no-standard-found |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn medicalSuitabilityProfile (mihub.lung.screening.medicalSuitabilityProfile.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,70); vollständige Urteile in candidates.json |
| Umsetzung (Synthese) | Nicht als eigenständig erhobenes Element führen, sondern als berechnetes Attribut „nächste Eignungsprüfung fällig“ von medicalSuitabilityProfile: Regel nach S3 Empf. 5.6 in constraints_de (unter 70 Jahren +5 Jahre, 70 bis 75 Jahre +3 Jahre, vorgezogen bei Bekanntwerden einer neuen hohen Komorbiditätslast; Eingänge Prüfdatum und Geburtsdatum). Zusätzlich Recall-Anlass „Neubewertung“ in screeningInvitation. Definition auf das medizinische Eignungsprofil beschränken. Die KBV-Information sieht ohnehin eine Kriterienprüfung je Runde vor. |
| Status | **behalten** – abgeleitetes Attribut (Zusammenlegung mit medicalSuitabilityProfile prüfen) |

##### 13. `eligibilityCheckResult` – Ergebnis der Zulässigkeitsprüfung in der Praxis

| Feld | Inhalt |
|---|---|
| Definition | Ergebnis der Prüfung nach § 2 je Kriterium und gesamt mit Datum; bei Nichterfüllung strukturierter Absagegrund. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..1 · assessment (Vorschlag: 1..* je Episode) |
| BPMN | Gateway_1whuu15 „Voraussetzungen erfüllt?“; Event_0rhy6wb „Teilnahme nicht möglich“; Gateway_0ofbhg1 „Anforderungen erfüllt?“ (process_step: G3 Zulässigkeit \| Praxis: Gateway_1whuu15; nein → Teilnahme nicht möglich (Event_0rhy6wb)) |
| Rolle | berichterstellende Ärzt:in; Prüfung durch den Erstbefunder (LuKrFrühErkV § 3 Nr. 1) |
| Trigger | Abschluss der Anspruchsprüfung je Runde |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. Pflicht ist nur die positive Bestätigung der erfüllten Kriterien im Bericht (LuKrFrühErkV § 2 Abs. 1 S. 1 Nr. 3 Buchst. a/b; KFE-RL § 38, § 39 Nr. 1, § 40 S. 3). Die Zulässigkeitsprüfung des Erstbefunders regeln LuKrFrühErkV § 3 Nr. 1 und KFE-RL § 41 Abs. 1. Negatives Ergebnis und Absagegrund haben keine Rechtsgrundlage. |
| Quellen mit Zitat | [Q05] KBV PraxisInfoSpezial, Bericht und Überweisung: „Sie dokumentieren nach dem Gespräch in einem Bericht, dass der beziehungsweise die Versicherte die …“ (Konsolidierung)<br>[Q01] LuKrFrühErkV, § 3 Nr. 1: „die Zulässigkeitsvoraussetzungen nach § 2 prüft“<br>[Q03] G-BA Tragende Gründe 18.06.2025, zu § 41: „Dabei sollte sich der Erstbefunder durch Rückfrage bei der versicherten Person versichern, dass die Angaben des Berichts zum Zeitpunkt der Indikationsstellung noch aktuell sind.“<br>[Q39] BPMN lung-cancer-screening-pathway, Event_0rhy6wb (documentation): „Die Person erfüllt nicht alle Zulässigkeitsvoraussetzungen gemäß §2 LuKrFrühErkV. Die Ablehnung wird der Person mitgeteilt.“ |
| Codes (Beleg, Bewertung) | keine Codes beansprucht; lokale Werteliste bzw. no-standard-found |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn creditableSmokingDurationYears (mihub.lung.screening.creditableSmokingDurationYears.v0.1); dependsOn packYearsCalculated (mihub.lung.screening.packYearsCalculated.v0.1); dependsOn lastQualifyingChestCtDate (mihub.lung.screening.lastQualifyingChestCtDate.v0.1); dependsOn symptomAndLungCancerCareStatus (mihub.lung.screening.symptomAndLungCancerCareStatus.v0.1); dependsOn medicalSuitabilityProfile (mihub.lung.screening.medicalSuitabilityProfile.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,70) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,70); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Kriterien und Absagegründe lokal codieren; Mindestmenge KVBW/DGP. |
| Umsetzung (Synthese) | Auf das Gesamtergebnis je Runde reduzieren (lokale Werteliste: erfüllt \| nicht erfüllt \| Nachweis unvollständig), dazu Absagegrund 0..* (lokal, optional) und Datum (Observation.effective). Einzelkriterien per dependsOn verknüpfen statt doppelt führen; Alter aus dem Geburtsdatum, Rauchstopp aus den Konsumabschnitten ableiten. Umbenennen in „Ergebnis der Prüfung der Anspruchsberechtigung“. Die Prüfung durch den Erstbefunder (Zulässigkeit, Aktualitätsrückfrage nach TrG) über care_process.data_flows abbilden (usage_type validate, system ris-pacs). KBV PraxisInfoSpezial nur als Sekundärbeleg. |
| Status | **behalten** – eigenständig (Gesamtergebnis; Rolle Erstbefunder über data_flows) |

#### G5 Information/Entscheidung/Entwöhnung

##### 14. `screeningInformationConsultation` – Informations- und Beratungsgespräch (Erstberatung)

| Feld | Inhalt |
|---|---|
| Definition | Mündliches Informationsgespräch der berichterstellenden Ärzt:in (gemeinsame Entscheidungsfindung) mit Datum, Dauer, Person und Kontaktform. |
| Datentyp · Kardinalität · Kategorie | dateTime · 1..1 · kontakt-visite (Vorschlag: Period bzw. Reference (Procedure/Encounter)) |
| BPMN | Activity_0e82ewp „Aufklärungsgespräch (§2 Abs.1 Nr.4)“ (process_step: G5 Information \| Praxis: Aufklärungsgespräch (§2 Abs.1 Nr.4) (Activity_0e82ewp)) |
| Rolle | berichterstellende Ärzt:in (Innere Medizin, Allgemeinmedizin, Arbeitsmedizin; ab 01.10.2026 laut BA 854 auch Praktische Ärzt:innen und Ärzt:innen ohne Gebietsbezeichnung) |
| Trigger | vor der Berichtserstellung; Erstberatung (EBM 01876 nur einmal je Versicherten) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. LuKrFrühErkV § 2 Abs. 1 S. 1 Nr. 4 (mündliches Gespräch und Textform); KFE-RL § 40 S. 1 i. V. m. § 43 Abs. 2. |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 2 Abs. 1 Nr. 4: „in einem mündlichen Gespräch und durch Aushändigung von Informationen in Textform über Folgendes informiert wurden“ (Konsolidierung)<br>[Q03] G-BA Tragende Gründe 18.06.2025, zu § 40: „darf erst durchgeführt werden, wenn ein Informationsgespräch durch einen an der vertragsärztlichen Versorgung teilnehmenden Internisten oder Allgemein- oder Arbeitsmediziner stattgefunden hat“<br>[Q06] EBA 87. Sitzung (11.03.2026), GOP 01876: „Einmalige Erstberatung des Versicherten zur Früherkennung von Lungenkrebs gemäß § 40 der Krebsfrüherkennungs-Richtlinie“ |
| Codes (Beleg, Bewertung) | EBM-GOP 01876 *Erstberatung zur Früherkennung von Lungenkrebs* – Beleg: EBA 87. Sitzung (11.03.2026, Wirkung 01.04.2026), Volltext gelesen – Bewertung: kein Konzeptcode; nur Abrechnungsbezug (keine belegte System-URI)<br>SNOMED CT 225328009 *Pre-screening counseling (procedure)* – Beleg: tx.fhir.org INT 20250201, Ontoserver 20260930: aktiv (Gegenprüfung) – Bewertung: vorgeschlagener Konzeptcode |
| Bezug zum Bestand | overlaps_existing: patientGoalsAndPreferences. Vorgeschlagene Relationen: hasPart patientInformationLeafletProvided (mihub.lung.screening.patientInformationLeafletProvided.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,85); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | BPMN 'Aufklärungsgespräch' = rechtlich Information; Aufklärung erst durch Erstbefunder. |
| Umsetzung (Synthese) | Als Anker behalten. Datentyp Period (Beginn/Ende) oder Reference(Procedure/Encounter) mit performer. Konzeptcode SNOMED 225328009 statt EBM 01876; die GOP nur als Abrechnungsbezug führen. Kontaktform mit der Werteliste von consultationModality, aber als lokale Angabe kennzeichnen (die KBV erlaubt Telefon und Video ausdrücklich nur für GOP 01880 und 01881). „Gemeinsame Entscheidungsfindung“ nur über S3 Kap. 5.1.4.5 (Hintergrund) stützen. patientInformationLeafletProvided als hasPart; die erfolgte Information wird im eligibilityReport bestätigt (KFE-RL § 40 S. 3). |
| Status | **behalten** – eigenständig (Anker des Informationsakts) |

##### 15. `patientInformationLeafletProvided` – Aushändigung der G-BA-Versicherteninformation (Fassung, Format)

| Feld | Inhalt |
|---|---|
| Definition | Aushändigung der Versicherteninformation nach Anlage I KFE-RL mit Datum, Fassung und Format (Druck, elektronisch, Leichte Sprache). |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..1 · dokument (Vorschlag: Reference (DocumentReference) oder Procedure · 1..1 je Erstberatung (0..* bei neuen Fassungen)) |
| BPMN | Activity_0e82ewp „Aufklärungsgespräch (§2 Abs.1 Nr.4)“ (process_step: G5 Information \| Praxis: Activity_0e82ewp) |
| Rolle | berichterstellende Ärzt:in; Bereitstellung auch über das Portal |
| Trigger | im Informationsgespräch (Erstberatung); erneut bei neuer Fassung |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. LuKrFrühErkV § 2 Abs. 1 S. 1 Nr. 4 und S. 2 (Strahlenrisiko in Textform); KFE-RL § 40 S. 1 mit Anlage I; obligater Leistungsinhalt von EBM 01876. |
| Quellen mit Zitat | [Q06] EBA-Beschluss 87. Sitzung, GOP 01876: „Ausgabe der Versicherteninformation gemäß § 40 der Krebsfrüherkennungs-Richtlinie“ (Konsolidierung)<br>[Q01] LuKrFrühErkV, § 2 Abs. 1 S. 2: „In den Informationen in Textform ist darüber hinaus auf das Strahlenrisiko hinzuweisen.“<br>[Q02] KFE-RL, § 40 S. 1: „in einem mündlichen Gespräch und durch Aushändigung von Informationen in Textform nach Anlage I zu informieren“ |
| Codes (Beleg, Bewertung) | SNOMED CT 699823003 *Provision of written information (procedure)* – Beleg: Ontoserver INT 20260601; tx.fhir.org INT 20250201: aktiv – Bewertung: Procedure.code |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: isPartOf screeningInformationConsultation (mihub.lung.screening.screeningInformationConsultation.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,90) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,60); vollständige Urteile in candidates.json |
| Umsetzung (Synthese) | Als hasPart von screeningInformationConsultation modellieren. Datentyp Reference(DocumentReference) mit G-BA-Dokument, Fassungsdatum und Format (Druck \| barrierefreies PDF \| Leichte Sprache) oder Procedure (code 699823003, usedReference). Quellen ergänzen: LuKrFrühErkV § 2 Abs. 1 S. 1 Nr. 4 und S. 2, KFE-RL § 40 S. 1 mit Anlage I; EBA 87 als Abrechnungsbeleg. Prüfpunkt: Die Fassung in Leichter Sprache (25.06.2026) ist nicht Anlage I; ob ihre alleinige Aushändigung § 40 erfüllt, ist offen. |
| Status | **behalten** – Teil von screeningInformationConsultation |

##### 16. `decisionAidResponse` – Entscheidungshilfe der Versicherteninformation (Antworten)

| Feld | Inhalt |
|---|---|
| Definition | Antworten in der Entscheidungshilfe: bevorzugte Option mit Gründen, Entscheidungsstand 0–10 und eigene Fragen für das Gespräch. |
| Datentyp · Kardinalität · Kategorie | Reference · 0..1 · prom (Vorschlag: 0..*) |
| BPMN | Activity_00yhsqy „Arztpraxis kontaktieren“ (process_step: G5 Entscheidung \| Versicherte: um Activity_00yhsqy; Portal) |
| Rolle | Versicherte (Selbsteingabe im Portal) |
| Trigger | optional vor oder nach dem Informationsgespräch; Wiederholung möglich |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **keine**. Freiwilliges Arbeitsblatt der Anlage I KFE-RL; keine Dokumentations- oder Übermittlungspflicht (§§ 39–44 KFE-RL). |
| Quellen mit Zitat | [Q02] KFE-RL Anlage I, Entscheidungshilfe: „Kreuzen Sie in der Tabelle an, welche Option Sie sich vorstellen können, und tragen Sie ein, was für Sie dafür und …“ (Konsolidierung)<br>[Q02] KFE-RL Anlage I, Unterstützung Ihrer Entscheidung: „Markieren Sie den Stand Ihrer Entscheidung auf der Skala von 0 bis 10.“<br>[Q20] ACR LCSR & IPN Data Dictionary (28.05.2026), Item 128: „Is there documentation of shared decision making?“ |
| Codes (Beleg, Bewertung) | keine Codes beansprucht; lokale Werteliste bzw. no-standard-found |
| Bezug zum Bestand | overlaps_existing: patientGoalsAndPreferences. Vorgeschlagene Relationen: dependsOn patientInformationLeafletProvided (mihub.lung.screening.patientInformationLeafletProvided.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,70) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,60); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | QuestionnaireResponse im Portal; kein Code für den Entscheidungsstand. |
| Umsetzung (Synthese) | Nur als optionales Portal-Element führen (QuestionnaireResponse; data_flows patientenportal/patient-entered; standardmäßig privat, Weitergabe nur mit Zustimmung; DPIA prüfen). Definition quellentreu: Option(en), die sich die Person vorstellen kann (keine Früherkennung / Früherkennung mit Niedrigdosis-CT), je mit Gründen dafür und dagegen; Entscheidungsstand 0–10 (lokales Item); eigene Fragen. Fundstelle: Anlage I, Abschnitt „Unterstützung Ihrer Entscheidung“ (PDF-S. 39–40; Broschüre S. 18–21); den Begriff „Entscheidungshilfe“ nur mit Verweis auf die TrG vom 18.12.2025. Kategorie eher versorgungsplanung statt prom. dependsOn patientInformationLeafletProvided; Vorstufe von participationDecision. |
| Status | **behalten** – eigenständig, optional (Portal) |

##### 17. `participationDecision` – Teilnahmeentscheidung der versicherten Person

| Feld | Inhalt |
|---|---|
| Definition | Entscheidung mit Datum nach Information, vor der LDCT (nach Aufklärung) und zur Fortsetzung nach dem Ergebnis; bei Ablehnung optional Grund. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..* · versorgungsplanung (Vorschlag: CodeableConcept (Observation mit effectiveDateTime) · 0..*) |
| BPMN | Activity_0e82ewp „Aufklärungsgespräch (§2 Abs.1 Nr.4)“ (process_step: G5 Entscheidung \| Radiologie: Gateway_0jgpvd3; Versicherte: Activity_0io1wvp → Gateway_1dj77wn) |
| Rolle | Versicherte (dokumentiert durch die Praxis oder im Portal) |
| Trigger | nach der Information (G5); bei Ablehnung optional mit Grund |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **keine**. Freiwilligkeit (Versicherteninformation S. 2; TrG zur Versicherteninformation). Dokumentationspflichtig ist nur die Einwilligung vor der LDCT (BGB § 630d Abs. 1, § 630f Abs. 2; KFE-RL § 41 Abs. 2); sie gehört zu ldctInformedConsent. |
| Quellen mit Zitat | [Q04] G-BA Versicherteninformation, S. 2: „Ob Sie das Angebot annehmen oder nicht, entscheiden Sie selbst.“ (Konsolidierung)<br>[Q04] G-BA Tragende Gründe zur Versicherteninformation (18.12.2025), Abschn. 2: „sollen die Anspruchsberechtigten dabei unterstützt werden, eine informierte Entscheidung für oder gegen die Teilnahme an der Früherkennungsuntersuchung treffen zu können“<br>[X05] KVBB-Musterbericht (PDF 12.05.2026), Feld: „eine Überweisung zum Lungenkrebsscreening gewünscht“ |
| Codes (Beleg, Bewertung) | SNOMED CT 13015001000119105 *Lung cancer screening declined (situation)* – Beleg: Ontoserver INT 20260601, tx.fhir.org INT 20250201: aktiv, Modul 900000000000207008; Elternkonzept 31021000119100 – Bewertung: nur für den Wert „abgelehnt“ |
| Bezug zum Bestand | overlaps_existing: patientGoalsAndPreferences. Vorgeschlagene Relationen: dependsOn screeningInformationConsultation (mihub.lung.screening.screeningInformationConsultation.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,60) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,65); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Qualifier Entscheidungspunkt nötig; Ablehnungsgründe lokal. |
| Umsetzung (Synthese) | Auf die Entscheidung nach der Information (G5) begrenzen; die Entscheidung vor der LDCT über ldctInformedConsent, Fortsetzung oder Abbruch über screeningEpisode abbilden. Als Observation: angenommen \| abgelehnt \| unentschieden (abgelehnt = SNOMED 13015001000119105, sonst lokal), effectiveDateTime, optionaler Ablehnungsgrund (lokal). Für „angenommen“ keinen Code setzen, solange keiner belegt ist. Die Entscheidungspunkte nach Information und nach Ergebnis als Modellierung aus dem BPMN kennzeichnen. |
| Status | **behalten** – eigenständig, auf die Entscheidung nach der Information begrenzt |

##### 18. `tobaccoCessationOfferScreening` – Information über und Angebot einer Tabakentwöhnung (Opt-out)

| Feld | Inhalt |
|---|---|
| Definition | Information über und Angebot einer Tabakentwöhnung (Kurzberatung, Kurs, Telefon/Digital, Medikation) mit Reaktion (angenommen, Opt-out, später). |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 0..* · prozedur |
| BPMN | Activity_0f2lkuk „Auf Rauchentwöhnungsprogramm hinweisen“ (process_step: G5 Entwöhnung \| Praxis: Auf Rauchentwöhnungsprogramm hinweisen (Activity_0f2lkuk)) |
| Rolle | berichterstellende Ärzt:in (Praxis) |
| Trigger | bei aktiv rauchenden Personen (smokingStatusScreening) im Informationsgespräch und bei Folgekontakten |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht (Information) / Leitlinie (Angebot)**. Information über die Möglichkeiten der Tabakentwöhnung ist Pflicht (KFE-RL § 40 S. 2; Bestätigung im Bericht nach S. 3). Angebot im Opt-out-Ansatz mit Reaktion: S3 Empf. 4.5 und 5.7 (Grad A), keine Rechtspflicht. |
| Quellen mit Zitat | [Q02] KFE-RL, § 40 S. 2: „Die Information umfasst auch die verschiedenen Möglichkeiten zur Tabakentwöhnung.“ (Konsolidierung)<br>[Q12] S3-LL Lungenkarzinom 5.1, Empf. 4.5 (A, LoE 1, neu 2026): „Rauchenden, die sich einem Lungenkarzinom-Screening unterziehen, soll eine Tabakentwöhnung mit Beratung (z.B. ABC-Ansatz) und pharmakologischer Unterstützung angeboten werden (opt out Ansatz).“<br>[Q20] ACR LCSR & IPN Data Dictionary (28.05.2026), Item 127: „Did physician provide smoking cessation guidance to patient?“ |
| Codes (Beleg, Bewertung) | SNOMED CT 771155005 *Brief intervention for smoking cessation (procedure)* – Beleg: Ontoserver INT 20260601, tx.fhir.org: aktiv; Elternkonzept 225323000 – Bewertung: Angebot (Kurzintervention)<br>SNOMED CT 225323000 *Smoking cessation education* – Beleg: Bestand (tobaccoCessationCounselling); Elternkonzept von 771155005 laut Gegenprüfung – Bewertung: Informationsteil |
| Bezug zum Bestand | overlaps_existing: tobaccoCessationCounselling (followup) – um Phase screening erweitern. Vorgeschlagene Relationen: specializes tobaccoCessationCounselling (mihub.lung.followup.tobaccoCessationCounselling.v0.1); dependsOn smokingStatusScreening (mihub.lung.screening.smokingStatusScreening.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,55); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Pflicht als Informationsinhalt (§ 40 KFE-RL); Angebot nach S3 4.5/5.7. |
| Umsetzung (Synthese) | specializes mihub.lung.followup.tobaccoCessationCounselling.v0.1 (Codes übernehmen, 771155005 ergänzen). Definition auf Angebot und Reaktion beschränken (angenommen \| abgelehnt/Opt-out \| später; lokales ValueSet); mandatory_by_law für das Angebot auf false. Den Pflichtteil (Information nach § 40 S. 2) über die Bestätigung der erfolgten Information im eligibilityReport (§ 40 S. 3) nachweisen, da informationTopicsCovered verworfen wurde; für den Informationsteil SNOMED 225323000. Trigger: aktiv rauchend laut smokingStatusScreening. S3-Empfehlungen mit Version 5.1 (Juli 2026) zitieren. |
| Status | **behalten** – Spezialisierung von tobaccoCessationCounselling (followup) |

#### G6 Bericht/Überweisung

##### 19. `eligibilityReport` – Bericht gemäß § 2 Abs. 1 Nr. 3 LuKrFrühErkV (Prüfbericht)

| Feld | Inhalt |
|---|---|
| Definition | Formfreier Bericht mit Zigarettenkonsum, Eignungsprofil, Anamnese und bestätigter Information; Aushändigung (auch ePA) und Vorlage beim Erstbefunder. |
| Datentyp · Kardinalität · Kategorie | Reference · 1..1 · dokument (Vorschlag: 1..* (je Runde)) |
| BPMN | Activity_1npn3bx „Bericht erstellen (§2 Abs.1 Nr.3)“; DataObjectReference_07wjx8v „Bericht gem. §2 Abs.1 Nr.3 PDF“; Activity_17m122u „Überweisung und Bericht übermitteln“; Event_1hwpffc „Überweisung und Bericht eingegangen“; Activity_1rd4qnc „Bericht lesen“ (process_step: G6 Bericht \| Praxis: Activity_1npn3bx → Activity_17m122u; Radiologie: Bericht lesen (Activity_1rd4qnc)) |
| Rolle | berichterstellende Ärzt:in; Aushändigung an die Versicherten; Vorlage beim Erstbefunder |
| Trigger | nach dem Gespräch je Runde, wenn die Voraussetzungen erfüllt sind |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. LuKrFrühErkV § 2 Abs. 1 S. 1 Nr. 3; KFE-RL § 39 Nr. 1 (S. 2: Bericht an die Person), § 40 S. 3 (Bestätigung der Information), § 41 Abs. 1 (Berücksichtigung durch den Erstbefunder); EBM 01875. Formfrei: Anlagen II und III der KFE-RL sind „[nicht belegt]“. |
| Quellen mit Zitat | [Q02] KFE-RL, § 39 Nr. 1: „Der Bericht wird der versicherten Person zur Verfügung gestellt.“ (Konsolidierung)<br>[Q02] KFE-RL, § 40 S. 3: „Die Ärztin oder der Arzt gemäß Satz 1 bestätigt im Bericht gemäß § 39 Nummer 1 die erfolgte Information zur Vorlage bei der ärztlichen Person gemäß § 41 Absatz 1.“<br>[Q03] G-BA Tragende Gründe 18.06.2025, zu § 39 Nr. 1 S. 2 (Aushändigung des Berichts): „Je nach Wunsch der Versicherten umfasst dies entweder eine Aushändigung in gedruckter Form oder, soweit rechtlich zulässig, in elektronischer Form über insbesondere die elektronische Patientenakte (vgl. § 341 Abs. 2 SGB V).“<br>[Q11] KVBB, Hinweise zum Musterbericht, Hinweis: „Nutzen Sie gern diesen Musterbericht oder erstellen Sie gemäß den Vorgaben einen eigenen Bericht“ |
| Codes (Beleg, Bewertung) | KDL AD020204 *Krebsfrüherkennung* – Beleg: Paket dvmd.kdl.r4 2026.0.0 (CodeSystem http://dvmd.de/fhir/CodeSystem/kdl), Elternkonzept AD0202 – Bewertung: nur breites Mapping („wider“) |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: hasPart packYearsCalculated (mihub.lung.screening.packYearsCalculated.v0.1); hasPart creditableSmokingDurationYears (mihub.lung.screening.creditableSmokingDurationYears.v0.1); hasPart medicalSuitabilityProfile (mihub.lung.screening.medicalSuitabilityProfile.v0.1); hasPart eligibilityCheckResult (mihub.lung.screening.eligibilityCheckResult.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,90) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,85); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Kein amtliches Formular; BÄK-Vorlage angekündigt; Composition. |
| Umsetzung (Synthese) | Kardinalität 1..* (je Runde). hasPart packYearsCalculated, creditableSmokingDurationYears, medicalSuitabilityProfile, eligibilityCheckResult und die Bestätigung der erfolgten Information (§ 40 S. 3); Abschnitt „Relevante Anamnese“ mit Verweisen auf comorbidity u. a. (statt des verworfenen relevantAnamnesticData); Selbsterklärung nach KFE-RL § 43 Abs. 2 S. 3 als Anlage (statt des verworfenen reportingPhysicianSelfDeclaration). KDL AD020204 nur als breites Mapping (binding example/extensible). Notes korrigieren: Die BÄK-Vorgaben (12.12.2025) verlangen nur, dass Fortbildungen eine Berichtsvorlage bereitstellen; eine konsentierte Vorlage kündigt das Whitepaper an, in S3 5.1 ist sie nicht enthalten. Elektronische Aushändigung über die ePA nennen die TrG (zu § 39 Nr. 1 S. 2) als Option „soweit rechtlich zulässig“, nicht der Normtext. |
| Status | **behalten** – eigenständig (Composition) |

##### 20. `ldctReferral` – Überweisung zur Niedrigdosis-CT an den Erstbefunder

| Feld | Inhalt |
|---|---|
| Definition | Überweisung an eine Radiologie mit Genehmigung als Erstbefunder zur Screening-LDCT, zusammen mit Bericht und Selbsterklärung. |
| Datentyp · Kardinalität · Kategorie | Reference · 1..1 · administrativ (Vorschlag: 1..* (je Runde)) |
| BPMN | Activity_1fi5rrl „Überweisung ausstellen“; Activity_17m122u „Überweisung und Bericht übermitteln“; Activity_16eirv7 „Überweisung der Radiologie vorlegen“; Event_11h9bwq „Überweisung erhalten“ (process_step: G6 Überweisung \| Praxis: Activity_1fi5rrl → Activity_17m122u; Radiologie: Event_11h9bwq) |
| Rolle | berichterstellende Ärzt:in (Praxis) an den Erstbefunder mit KV-Genehmigung |
| Trigger | je Runde, wenn die Voraussetzungen erfüllt sind |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Pflicht**. In der GKV verpflichtend über den Überweisungsvorbehalt der Radiologie (BMV-Ä § 13 Abs. 4 S. 1, Fassung 01.04.2026); EBM 01875 setzt die Überweisung zur Niedrigdosis-CT voraus. LuKrFrühErkV und KFE-RL verlangen nur den Bericht. |
| Quellen mit Zitat | [Q04] G-BA Versicherteninformation, S. 7: „Wenn Sie alle Voraussetzungen zur Teilnahme erfüllen, erhalten Sie eine Überweisung.“ (Konsolidierung)<br>[X01] BMV-Ä (Fassung 01.04.2026), § 13 Abs. 4 S. 1: „Ärzte für … Radiologische Diagnostik bzw. Radiologie … können nur auf Überweisung in Anspruch genommen werden.“<br>[Q05] KBV PraxisInfoSpezial (Oktober 2026), S. 4: „Sind alle Voraussetzungen erfüllt, überweisen sie den Versicherten“ |
| Codes (Beleg, Bewertung) | LOINC 79086-5 *CT Chest for screening WO contrast* – Beleg: tx.fhir.org $lookup, LOINC 2.82: aktiv, ORDER_OBS Both – Bewertung: ServiceRequest.code<br>KDL AU050102 *Überweisungsschein* – Beleg: KDL 2026.0.0 (wie referralOrder) – Bewertung: ergänzen (Dokumentklasse) |
| Bezug zum Bestand | overlaps_existing: referralOrder (Spezialisierung). Vorgeschlagene Relationen: specializes referralOrder (mihub.lung.primarycare.referralOrder.v0.1); dependsOn eligibilityReport (mihub.lung.screening.eligibilityReport.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,55); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Norm verlangt den Bericht, nicht die Überweisung → nicht Pflicht. |
| Umsetzung (Synthese) | specializes mihub.lung.primarycare.referralOrder.v0.1. ServiceRequest.code LOINC 79086-5, zusätzlich KDL AU050102. mandatory_by_law = true mit den Quellen BMV-Ä § 13 Abs. 4 S. 1–2 und EBM 01875; die Notiz der Konsolidierung („nicht Pflicht“) ersetzen durch „LuKrFrühErkV und KFE-RL verlangen den Bericht; die Überweisung folgt aus dem Überweisungsvorbehalt der Radiologie im BMV-Ä“. supportingInfo → eligibilityReport; performer = Erstbefunder mit KV-Genehmigung (KFE-RL § 43 Abs. 5). Versicherteninformation S. 7 als Ablaufbeleg behalten. |
| Status | **behalten** – Spezialisierung von referralOrder (primarycare) |

#### G7 Radiologie vor LDCT

##### 21. `justifyingIndication` – Rechtfertigende Indikation (§ 83 Abs. 3 StrlSchG) mit Zeitpunkt

| Feld | Inhalt |
|---|---|
| Definition | Rechtfertigende Indikation des Erstbefunders unter Berücksichtigung des Berichts, mit Zeitpunkt, Person und Befragung zu früheren Strahlenanwendungen. |
| Datentyp · Kardinalität · Kategorie | dateTime · 1..1 · prozedur (Vorschlag: Reference (Procedure) bzw. CodeableConcept + dateTime · 1..1 je LDCT-Runde) |
| BPMN | Activity_0l9ecr6 „Rechtfertigende Indikation stellen und Voruntersuchung prüfen (§3 und §4 Abs.2)“ (process_step: G7 Radiologie \| Erstbefunder: Rechtfertigende Indikation stellen (Activity_0l9ecr6)) |
| Rolle | Erstbefunder (Person nach LuKrFrühErkV § 6 Abs. 1) |
| Trigger | vor jeder LDCT (Regel- und Kontroll-LDCT) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. LuKrFrühErkV § 3 Nr. 2 (rechtfertigende Indikation nach StrlSchG § 83 Abs. 3 unter Berücksichtigung des Berichts); Aufzeichnung mit Zeitpunkt StrlSchG § 85 Abs. 1 S. 2 Nr. 1; Befragung zu früheren Strahlenanwendungen StrlSchV § 119 Abs. 3 S. 2; Rolle KFE-RL § 41 Abs. 1 S. 1, § 39 Nr. 3, § 43 Abs. 5. |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 3 Nr. 2: „die rechtfertigende Indikation nach § 83 Absatz 3 des Strahlenschutzgesetzes … unter Berücksichtigung des Berichts …“ (Konsolidierung)<br>[Q09] StrlSchG, § 85 Abs. 1 S. 2 Nr. 1: „Angaben zur rechtfertigenden Indikation und den Zeitpunkt der Indikationsstellung“<br>[Q09] StrlSchV, § 119 Abs. 3 S. 2: „Zu diesem Zweck ist die zu untersuchende oder zu behandelnde Person über frühere Anwendungen ionisierender Strahlung oder radioaktiver Stoffe, die für die vorgesehene Anwendung von Bedeutung sein können, zu befragen.“ |
| Codes (Beleg, Bewertung) | keine Codes beansprucht; lokale Werteliste bzw. no-standard-found |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn eligibilityReport (mihub.lung.screening.eligibilityReport.v0.1); dependsOn lastQualifyingChestCtDate (mihub.lung.screening.lastQualifyingChestCtDate.v0.1); dependsOn eligibilityCheckResult (mihub.lung.screening.eligibilityCheckResult.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,85); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Inkl. Befragung § 119 Abs. 3 StrlSchV; kein Standardcode. |
| Umsetzung (Synthese) | Strukturiert modellieren, z. B. Procedure: performed[x] = Zeitpunkt der Indikationsstellung, performer = Erstbefunder, outcome gestellt \| nicht gestellt (lokal, no-standard-found). Die Befragung zu früheren Strahlenanwendungen nicht doppelt führen, sondern über dependsOn auf lastQualifyingChestCtDate, eligibilityReport und eligibilityCheckResult verweisen (statt des verworfenen firstReaderEligibilityVerification). StrlSchG § 85 Abs. 1 S. 2 Nr. 1 als Quelle der Dokumentationspflicht und StrlSchV § 119 Abs. 3 S. 2 aus den notes in sources überführen. |
| Status | **behalten** – eigenständig |

##### 22. `priorScreeningImagesAvailability` – Vorliegen von Voraufnahmen und Vorbefunden (§ 4 Abs. 2)

| Feld | Inhalt |
|---|---|
| Definition | Status der Voraufnahmen und Vorbefunde der letzten (zwei) Früherkennungsuntersuchungen (vorliegend, keine, angefordert, Verzicht mit Grund) mit Verweis. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..1 · bildgebung (Vorschlag: 1..1 (Wert „nicht zutreffend“ bei Erstrunde)) |
| BPMN | Activity_0l9ecr6 „Rechtfertigende Indikation stellen und Voruntersuchung prüfen (§3 und §4 Abs.2)“; DataStoreReference_10mkbcy „PACS“ (process_step: G7 Radiologie \| Erstbefunder: Activity_0l9ecr6 (Annotation §4 Abs.2); PACS) |
| Rolle | Erstbefunder (Strahlenschutzverantwortliche:r sorgt für das Vorliegen) |
| Trigger | vor jeder Folge-LDCT (nach mindestens einer früheren Früherkennungsuntersuchung) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **bedingt**. Sicherstellung der Aufnahmen und Befunde der letzten beiden Untersuchungen bzw. der einen Voruntersuchung (LuKrFrühErkV § 4 Abs. 2 S. 1; KFE-RL § 41 Abs. 1 S. 2–3); Verzicht im Einzelfall (§ 4 Abs. 2 S. 2). Eine Dokumentation von Status oder Verzicht ist nicht ausdrücklich normiert. |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 4 Abs. 2 S. 2: „kann im Einzelfall auf das Vorliegen der Unterlagen verzichtet werden“ (Konsolidierung)<br>[Q20] ACR Lung-RADS v2022, Note 9: „If waiting on prior exams (either a prior screening or diagnostic CT), the Lung-RADS 0 category is temporary until the comparison study is available“<br>[Q03] G-BA Tragende Gründe 18.06.2025, zu § 41, S. 18 (Verzichtsgründe): „eine fehlende Schweigepflichtsentbindung“ |
| Codes (Beleg, Bewertung) | EBM-GOP 01871 *Niedrigdosis-CT zur Früherkennung von Lungenkrebs* – Beleg: EBA 87. Sitzung (11.03.2026), Teil A – Bewertung: entfernen (Abrechnungsziffer der gesamten LDCT, kein Statuskonzept) |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn lastQualifyingChestCtDate (mihub.lung.screening.lastQualifyingChestCtDate.v0.1); dependsOn resultTransmissionConsentReferrer (mihub.lung.screening.resultTransmissionConsentReferrer.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,80) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,75); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | befundung: keine Dokumentationspflicht → hier Pflicht (Voraussetzung, EBM). |
| Umsetzung (Synthese) | EBM 01871 entfernen (Leistung, kein Statuskonzept; gehört als Abrechnungsbezug zu ldctExamination). Lokales Value Set: vorliegend \| nicht zutreffend (Erstuntersuchung) \| angefordert \| Verzicht: nicht möglich \| Verzicht: unverhältnismäßiger Aufwand; standard_binding_status no-standard-found. Den Verweis auf die Vorstudie getrennt führen (Reference ImagingStudy/DiagnosticReport). Verzichtsgründe nach TrG S. 18 (u. a. fehlende Schweigepflichtsentbindung) als Werteliste. Quellen ergänzen: § 4 Abs. 2 S. 1 und 2, KFE-RL § 41 Abs. 1 S. 2–3, TrG S. 18, obligater Leistungsinhalt von EBM 01871/01872. Den Wert „angefordert“ als Prozesswert ohne Quellenbezug kennzeichnen. |
| Status | **behalten** – eigenständig (lokales ValueSet) |

##### 23. `ldctInformedConsent` – Aufklärung durch den Erstbefunder und Einwilligung in die LDCT

| Feld | Inhalt |
|---|---|
| Definition | Aufklärung vor der LDCT (§ 630e BGB, Strahlenrisiko, Beteiligte, Datenaustausch) mit Ergebnis, Datum, Person und Abschriften. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..1 · prozedur (Vorschlag: 1..1 je LDCT-Runde) |
| BPMN | Activity_1uptzny „Aufklärung Niedrigdosis-CT durchführen“; Gateway_0jgpvd3 „Teilnahme durch Versicherte bestätigt?“ (process_step: G7 Radiologie \| Erstbefunder: Aufklärung Niedrigdosis-CT (Activity_1uptzny) → Gateway_0jgpvd3) |
| Rolle | Erstbefunder (Aufklärung); Versicherte (Einwilligung) |
| Trigger | vor jeder LDCT (Regel- und Kontroll-LDCT) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. Aufklärung durch den Erstbefunder (KFE-RL § 41 Abs. 2); Einwilligung, Aufklärung und Dokumentation nach BGB § 630d Abs. 1, § 630e Abs. 1–2, § 630f Abs. 2; Strahlenrisiko StrlSchV § 124 Abs. 1. Das Ergebnis „erteilt/abgelehnt“ folgt aus dem BGB, nicht aus der KFE-RL. |
| Quellen mit Zitat | [Q02] KFE-RL, § 41 Abs. 2: „Ein Erstbefunder hat die versicherte Person vor Anwendung der Niedrigdosis-Computertomographie aufzuklären.“ (Konsolidierung)<br>[Q03] G-BA Tragende Gründe 18.06.2025, zu § 41, S. 18: „insbesondere nach § 630e BGB sowie nach § 124 Strahlenschutzverordnung aufzuklären“<br>[X02] BGB, § 630f Abs. 2 S. 1: „Einwilligungen und Aufklärungen“ |
| Codes (Beleg, Bewertung) | SNOMED CT 182771004 *Informed consent for procedure (procedure)* – Beleg: Ontoserver INT 20260601, tx.fhir.org INT 20250201: aktiv – Bewertung: Elementcode<br>KDL AM010302 *Diagnostischer Aufklärungsbogen* – Beleg: KDL 2026.0.0 (Gegenprüfung) – Bewertung: Dokumenttyp (vorgeschlagen)<br>LOINC 64293-4 *Procedure consent Document* – Beleg: LOINC 2.82: aktiv (Gegenprüfung) – Bewertung: Dokumenttyp (vorgeschlagen) |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn justifyingIndication (mihub.lung.screening.justifyingIndication.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,80); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Ablehnung als Abbruchpfad im BPMN ohne Endereignis. |
| Umsetzung (Synthese) | Das Einwilligungsergebnis (erteilt \| abgelehnt) nur hier führen; participationDecision auf die Entscheidung nach der Information begrenzen. Alternativ als Prozedur mit dateTime der Aufklärung, aufklärender Ärzt:in und Verweis auf den unterschriebenen Bogen (Dokumenttyp KDL AM010302 bzw. LOINC 64293-4). Quellen ergänzen: TrG zu § 41 (S. 18) und zu § 42 (S. 19), BGB §§ 630d, 630e, 630f, StrlSchV § 124 Abs. 1. Aufklärungsinhalt „Beteiligte/Datenaustausch“ mit resultTransmissionConsentReferrer verknüpfen. Im BPMN fehlt ein Endereignis für die Ablehnung nach der Aufklärung. |
| Status | **behalten** – eigenständig (Einwilligungsergebnis nur hier) |

##### 24. `resultTransmissionConsentReferrer` – Einwilligung in die Befundübermittlung an die berichterstellende Praxis

| Feld | Inhalt |
|---|---|
| Definition | Einwilligung, dass der Befundbericht auch an die berichterstellende Praxis geht; ohne Einwilligung erhält ihn nur die versicherte Person. |
| Datentyp · Kardinalität · Kategorie | boolean · 1..1 · administrativ (Vorschlag: CodeableConcept + Datum oder Reference (FHIR Consent)) |
| BPMN | Activity_1uptzny „Aufklärung Niedrigdosis-CT durchführen“; Event_13jgib0 „Rückmeldung der Radiologie eingegangen“ (process_step: G7 Radiologie \| Erstbefunder: Activity_1uptzny; Bedingung für Event_13jgib0) |
| Rolle | Versicherte (Einwilligung); Erstbefunder (Einholung) |
| Trigger | Aufklärung vor der LDCT; Widerruf jederzeit |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **bedingt**. Übermittlung des strukturierten Befundberichts an die berichterstellende Ärzt:in nur bei Einwilligung (KFE-RL § 42 Abs. 2 S. 2); ohne Einwilligung nur an die Person (S. 1). |
| Quellen mit Zitat | [Q02] KFE-RL, § 42 Abs. 2 S. 2: „Bei Einwilligung der versicherten Person übermittelt der Erstbefunder auch dem Arzt oder der Ärztin gemäß § 43 …“ (Konsolidierung)<br>[Q04] G-BA Versicherteninformation (Anlage I KFE-RL), Ablauf: „bei Vorliegen Ihrer Einwilligung – Ihrer behandelnden Ärztin“ |
| Codes (Beleg, Bewertung) | LOINC 64292-6 *Release of information consent Document* – Beleg: LOINC 2.83 über Ontoserver, 2.82 über tx.fhir.org: aktiv; im FHIR-R4-ValueSet consent-category enthalten – Bewertung: Consent.category<br>KDL AM050107 *Schweigepflichtentbindung* – Beleg: Paket dvmd.kdl.r4 2026.0.0 (Gegenprüfung) – Bewertung: Dokumenttyp (vorgeschlagen) |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: – |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,92) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,80); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Bedingte Pflicht; BPMN modelliert Rückmeldung an Praxis unbedingt. |
| Umsetzung (Synthese) | Zum gemeinsamen Einwilligungselement für Datenweitergaben ausbauen, mit Empfänger-Qualifier: berichterstellende Praxis \| Zweitbefunder \| Einrichtung mit Voraufnahmen. Werte erteilt \| verweigert \| widerrufen (lokal) plus Datum, oder Reference auf FHIR Consent (category LOINC 64292-6, provision.actor = Empfänger); Dokument KDL AM050107. Die Pflicht ist bedingt: An die Praxis wird nur bei „erteilt“ übermittelt. Im BPMN ist die Rückmeldung an die Praxis (Event_13jgib0) unbedingt modelliert. |
| Status | **behalten** – eigenständig; Ausbau zum gemeinsamen Einwilligungselement (nimmt providerDataExchangeConsent auf) |

##### 25. `screeningDataUseConsent` – Einwilligung in zentrale Speicherung, Registerabgleich und Forschung

| Feld | Inhalt |
|---|---|
| Definition | Zweckbezogene Einwilligungen: zentrale Speicherung, Melde-/Krebsregisterabgleich, Forschung und künftiges G-BA-Monitoring (erteilt, verweigert, widerrufen). |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 0..* · administrativ (Vorschlag: Reference (FHIR Consent je Zweck)) |
| BPMN | Activity_0e82ewp „Aufklärungsgespräch (§2 Abs.1 Nr.4)“; Activity_1uptzny „Aufklärung Niedrigdosis-CT durchführen“ (process_step: G7 Einwilligung \| Praxis: Activity_0e82ewp bzw. Erstbefunder: Activity_1uptzny) |
| Rolle | Versicherte; Einholung durch Praxis oder Erstbefunder |
| Trigger | optional bei Information oder Aufklärung; Widerruf jederzeit |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. S3 Empf. 5.13 (EK, „sollte“); derzeit ohne Empfänger: Das Monitoring nach KFE-RL § 46 Abs. 2 schafft der G-BA erst bis Ende 2028. |
| Quellen mit Zitat | [Q12] S3-LL Lungenkarzinom, Empf. 5.13 (EK): „Hierzu sollte eine Einwilligung der Teilnehmer für • eine zentrale Speicherung der im Rahmen des …“ (Konsolidierung)<br>[Q02] KFE-RL, § 46 Abs. 2: „Bis spätestens zum Ablauf des Jahres 2028 wird der G-BA die regulatorischen und strukturellen Voraussetzungen für ein Monitoring“ |
| Codes (Beleg, Bewertung) | SNOMED CT 736814000 *Consent given for observational study participation (finding)* – Beleg: tx.fhir.org INT 20250201, Ontoserver: aktiv, Core-Modul, effectiveTime 20180131 – Bewertung: nur Beispiel für den Forschungszweck |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: – |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,60); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Derzeit kein Empfänger; DPIA-Touchpoint. |
| Umsetzung (Synthese) | Als optionales, vorausschauendes Element ohne aktuellen Empfänger kennzeichnen. Zwecke auf S3 Empf. 5.13 beschränken (zentrale Speicherung; Abgleich mit Einwohnermeldeämtern und Krebsregistern; Forschung „zur Optimierung des Lungenkrebs-Screeningprogramms“); „künftiges G-BA-Monitoring“ erst nach einer G-BA-Regelung aufnehmen (ggf. als Widerspruch statt Einwilligung). FHIR Consent je Zweck (provision.purpose plus status). Forschungszweck am MII-Modul Consent (Broad Consent) ausrichten; 736814000 nur als Beispiel-Coding für den Forschungszweck. DPIA- und Justiziariats-Touchpoint. |
| Status | **behalten** – eigenständig, optional und vorausschauend |

#### G8 LDCT

##### 26. `ldctExamination` – Niedrigdosis-CT des Thorax zur Früherkennung (Durchführung)

| Feld | Inhalt |
|---|---|
| Definition | Durchgeführte LDCT nach § 4 und Anlage mit Zeitpunkt, Art, Einrichtung und Verweis auf die DICOM-Studie; Bezug für Fristen und Intervalle. |
| Datentyp · Kardinalität · Kategorie | dateTime · 1..1 · bildgebung (Vorschlag: Reference (Procedure/ImagingStudy) · 0..* (1 je Runde)) |
| BPMN | Activity_12qrin2 „Niedrigdosis-CT durchführen (§4, §5)“; DataStoreReference_10mkbcy „PACS“ (process_step: G8 LDCT \| Erstbefunder: Niedrigdosis-CT durchführen (Activity_12qrin2); PACS) |
| Rolle | Erstbefunder (Strahlenschutzverantwortliche:r; Durchführung durch MTR) |
| Trigger | je Runde (Regel-LDCT) bzw. Kontroll-LDCT |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. Dokumentation der Durchführung (KFE-RL § 44 S. 1); Aufzeichnung von Zeitpunkt und Art der Anwendung (StrlSchG § 85 Abs. 1 S. 2 Nr. 2); Anforderungen nach LuKrFrühErkV § 4 Abs. 1 mit Anlage. |
| Quellen mit Zitat | [Q09] StrlSchG, § 85 Abs. 1: „den Zeitpunkt und die Art der Anwendung“ (Konsolidierung)<br>[Q02] KFE-RL, § 44 S. 1: „Der Erstbefunder dokumentiert in der Patientenakte die Durchführung der Niedrigdosis-Computertomographie“ |
| Codes (Beleg, Bewertung) | SNOMED CT 713548006 *Low dose computed tomography of thorax (procedure)* – Beleg: tx.fhir.org INT 20250201, Ontoserver: aktiv; $subsumes unter 169069000 – Bewertung: Elementcode<br>LOINC 79086-5 *CT Chest for screening WO contrast* – Beleg: tx.fhir.org, LOINC 2.82: aktiv – Bewertung: Mapping (Auftrag/Studie)<br>EBM-GOP 01871 *Niedrigdosis-CT zur Früherkennung von Lungenkrebs* – Beleg: EBA 87. Sitzung (11.03.2026), Teil A – Bewertung: nur Abrechnungsbezug, ergänzt um 01872 (Kontroll-LDCT) |
| Bezug zum Bestand | overlaps_existing: ctThoraxScan (Spezialisierung). Vorgeschlagene Relationen: specializes ctThoraxScan (mihub.lung.followup.ctThoraxScan.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,85); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Nicht verwenden: SNOMED 724167008 (inaktiv), 171184001. |
| Umsetzung (Synthese) | specializes mihub.lung.followup.ctThoraxScan.v0.1. Datentyp Reference (Procedure/ImagingStudy) oder Definition auf den Durchführungszeitpunkt beschränken; Kardinalität 0..* (eine je Runde). EBM-GOP nicht als Konzeptcode (01871 Regel-LDCT, 01872 Kontroll-LDCT nur als Abrechnungsbezug). Mapping MII KDS Bildgebung 2026.0.0: …/fhir/ext/modul-bildgebung/StructureDefinition/mii-pr-bildgebung-bildgebungsprozedur bzw. -bildgebungsstudie (ImagingStudy.started). „Art“ als Anwendungsart nach § 85 StrlSchG präzisieren; die Untersuchungsart gehört zu screeningExaminationType. Einrichtung und DICOM-Studienverweis sind nicht gesetzlich gefordert. Für die 12-Monats-Prüfung zählt jede befundungsgeeignete Lungen-CT (lastQualifyingChestCtDate). |
| Status | **behalten** – Spezialisierung von ctThoraxScan (followup) |

##### 27. `screeningExaminationType` – Art der Früherkennungsuntersuchung und Runde

| Feld | Inhalt |
|---|---|
| Definition | Einordnung der LDCT: Erstuntersuchung, reguläre Folgeuntersuchung, vorgezogene Kontrolle oder Kurzintervall (Lung-RADS 0), mit Rundennummer. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..1 · versorgungskontext (Vorschlag: 1 je LDCT) |
| BPMN | Activity_0l9ecr6 „Rechtfertigende Indikation stellen und Voruntersuchung prüfen (§3 und §4 Abs.2)“; Activity_12qrin2 „Niedrigdosis-CT durchführen (§4, §5)“ (process_step: G8 LDCT \| Erstbefunder: Activity_0l9ecr6 / Activity_12qrin2) |
| Rolle | Erstbefunder |
| Trigger | je LDCT |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **keine**. Keine Dokumentationspflicht. Abrechnung: EBM 01872 setzt die Angabe des Kontrollintervalls in Monaten voraus; Rechtsgrundlage der Kontroll-LDCT ist LuKrFrühErkV § 2 Abs. 2, die Unterscheidung Erst-/Folgeuntersuchung stützt § 4 Abs. 2. |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 2 Abs. 2: „nach einem kontrollbedürftigen Befund eine Untersuchung zur Lungenkrebsfrüherkennung mittels …“ (Konsolidierung)<br>[Q06] EBA 87. Sitzung (11.03.2026), GOP 01872: „Die Berechnung der Gebührenordnungsposition 01872 setzt die Angabe dieses Kontrollintervalls in Monaten voraus.“<br>[Q26] NHS England QA standards v3 (03.02.2025), Annex 1: „Type of scan: Baseline/ 3 month/ 12 month/ 24 month“ |
| Codes (Beleg, Bewertung) | RadElement RDE1703 *Baseline study* – Beleg: RSNA RadElement-API: Set RDES267 „Lung-RADS categorization“, Published 2024-05-31; Werte yes/no/unknown – Bewertung: nur Mapping für das Baseline-Flag |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: isPartOf ldctExamination (mihub.lung.screening.ldctExamination.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,60) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,55); vollständige Urteile in candidates.json |
| Umsetzung (Synthese) | Als Attribut „Untersuchungsart“ von ldctExamination führen: Erst-LDCT (Baseline) \| Regel-LDCT (≥ 12 Monate) \| Kontroll-LDCT (§ 2 Abs. 2 LuKrFrühErkV). „Kurzintervall (Lung-RADS 0)“ streichen bzw. rechtlich klären (zulässig nur über § 2 Abs. 2 oder bei nicht befundungsgeeigneter Voraufnahme; E12). Rundennummer aus screeningEpisode ableiten statt erfassen. Mappings: RadElement RDE1703 (Baseline ja/nein) und EBM 01871/01872. Quellen ergänzen: LuKrFrühErkV § 4 Abs. 2, KFE-RL § 38 Abs. 1 S. 2, EBM 01871/01872, S3 Empf. 5.9 (Lung-RADS 0). |
| Status | **behalten** – Attribut von ldctExamination (Zusammenlegung prüfen) |

##### 28. `ctdiVol` – Volumen-CT-Dosisindex (CTDIvol) der Spiral-LDCT

| Feld | Inhalt |
|---|---|
| Definition | Mittlerer CTDIvol der Spiralaufnahme (mGy, ohne Übersicht) aus dem Dosisbericht; Definitionsmerkmal der LDCT (≤ 1,3 mGy). |
| Datentyp · Kardinalität · Kategorie | Quantity · 1..1 · messwert (Vorschlag: 0..* (1 je LDCT)) |
| BPMN | Activity_12qrin2 „Niedrigdosis-CT durchführen (§4, §5)“; Activity_14vmlwn „Qualitätsdaten erheben und dokumentieren (§7)“ (process_step: G8 LDCT \| Activity_12qrin2; Qualitätsdaten (§7) (Activity_14vmlwn)) |
| Rolle | Radiologie (Übernahme aus dem Dosisbericht/RDSR) |
| Trigger | je LDCT (Spiral-Bestrahlungsereignis) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **mittelbar**. Definitionsmerkmal der LDCT (LuKrFrühErkV § 1 Abs. 1 S. 1 Nr. 1 und S. 2) mit Einhaltungspflicht nach § 4 Abs. 1 S. 2 und Anlage; Aufzeichnung der Exposition nach StrlSchG § 85 Abs. 1 S. 2 Nr. 3 Buchst. a (ohne bestimmte Dosisgröße). |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 1 Abs. 1: „ein Volumen-Computertomographie-Dosisindex von 1,3 Milligray nicht überschritten wird oder“ (Konsolidierung)<br>[Q01] LuKrFrühErkV, § 4 Abs. 1 S. 2: „Der Strahlenschutzverantwortliche hat dafür zu sorgen, dass die Anforderungen eingehalten werden.“<br>[Q20] ACR LCSR & IPN Data Dictionary (28.05.2026), #143 CTDIvol (mGy): „Do not include the topogram.“ |
| Codes (Beleg, Bewertung) | DICOM DCM 113830 *Mean CTDIvol* – Beleg: DICOM PS3.16 2026d, Annex D; Teil von TID 10013 – Bewertung: Elementcode<br>NCIt C101138 *Computed Tomography Dose Index Volume* – Beleg: NCI EVS REST API, NCIt 26.09d: aktiv – Bewertung: Mapping |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: isPartOf ldctExamination (mihub.lung.screening.ldctExamination.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,75) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,80); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | MII-Extension modalitaetCT; § 85 StrlSchG ohne bestimmte Dosisgröße. |
| Umsetzung (Synthese) | Kardinalität 0..* (1 je LDCT bzw. Spiral-Bestrahlungsereignis), unit mGy; isPartOf ldctExamination. Mapping: …/fhir/ext/modul-bildgebung/StructureDefinition/mii-ex-bildgebung-modalitaet-ct (Slice CTDIvol) bzw. DICOM TID 10013. Konformität (≤ 1,3 mGy) und ggf. den Grund einer Überschreitung (Körperstatur) hier als Attribut führen (statt des verworfenen ctdiVolExceedanceJustification). Optional den CTDIvol der Übersichtsaufnahme als Komponente (Anlage: ≤ 0,2 × angestrebter Spiral-CTDIvol). Fundstelle präzisieren: § 1 Abs. 1 S. 1 Nr. 1 und S. 2. Codesysteme dicom-dcm und ncit im Repo ergänzen. |
| Status | **behalten** – eigenständig (isPartOf ldctExamination) |

##### 29. `ldctAcquisitionParameters` – Aufnahme- und Rekonstruktionsparameter nach Anlage zu § 4 (mit Konformität)

| Feld | Inhalt |
|---|---|
| Definition | Protokollparameter nach Anlage (Gerät, Scan-/Rotationszeit, Kollimation, Pitch, kV/mA, Schichtdicke, Kern, Rekonstruktion, kein Kontrastmittel) mit Konformität. |
| Datentyp · Kardinalität · Kategorie | Reference · 0..1 · bildgebung (Vorschlag: 0..*) |
| BPMN | Activity_12qrin2 „Niedrigdosis-CT durchführen (§4, §5)“; Activity_14vmlwn „Qualitätsdaten erheben und dokumentieren (§7)“ (process_step: G8 LDCT \| Activity_12qrin2; Activity_14vmlwn (Annotation Anlage zu §4)) |
| Rolle | Radiologie (MTR, Medizinphysik) |
| Trigger | je LDCT bzw. im Rahmen der Protokoll-QS |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **keine**. Die Einhaltung der Anlage ist Pflicht (LuKrFrühErkV § 4 Abs. 1 mit Anlage; QS-Vereinbarung § 11 Abs. 5); eine Einzeldokumentation je Untersuchung schreibt keine Norm vor (das QS-System „berücksichtigt“ die Parameter, § 7 Abs. 1 S. 2 Nr. 3). |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 7 Abs. 1 Nr. 3: „die physikalisch-technischen Parameter bei der Erstellung der Computertomographieaufnahme“ (Konsolidierung)<br>[Q07] Vereinbarung Strahlendiagnostik (ab 01.04.2026), § 11 Abs. 5: „Eine NDCT darf nur durchgeführt werden, wenn die Anforderungen … nach der Anlage zu § 4 Absatz 1 Satz 1 der LuKrFrühErkV erfüllt sind.“ |
| Codes (Beleg, Bewertung) | DICOM DCM 113828 *Pitch Factor* – Beleg: DICOM PS3.16 (Gegenprüfung) – Bewertung: nur Einzelparameter; als Elementcode ersetzen<br>DICOM DCM 113822 *CT Acquisition Parameters* – Beleg: DICOM PS3.16 2026d, in TID 10013 (Gegenprüfung) – Bewertung: vorgeschlagener Elementcode |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: isPartOf ldctExamination (mihub.lung.screening.ldctExamination.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,75) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,55); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Einhaltung Pflicht, Einzeldokumentation nicht; 11 Einzelparameter zusammengefasst. |
| Umsetzung (Synthese) | Auf die Konformität je LDCT reduzieren (Anlage zu § 4 eingehalten ja/nein plus Abweichungen) mit Reference auf den RDSR (DCM 113701) bzw. die DICOM-Studie; Kerncode DCM 113822 statt 113828. Parameterliste an die Anlage angleichen: Spannungs- und Dosisautomatik ja/nein statt kV/mA; „Schichtdicke“ stammt nicht aus der Anlage (Belege S3 Kap. 6.3, ACR #150). Geräte- und protokollbezogene Anforderungen (dynamische Kollimation, Rekonstruktionsverfahren, Befundarbeitsplatz) in Struktur- bzw. QS-Daten auslagern. Primärquelle auf § 4 Abs. 1 mit Anlage umstellen, § 7 Abs. 1 S. 2 Nr. 3 als QS-Bezug. |
| Status | **behalten** – eigenständig, reduziert auf Konformität und RDSR-Referenz |

#### G9 Befundung

##### 30. `screeningReadingEvent` – Befundungsvorgang (Rolle, ohne/mit CAD, Software, Person)

| Feld | Inhalt |
|---|---|
| Definition | Befundungsschritt mit Rolle (Erst-/Zweitbefunder), Modus (ohne, dann mit CAD), Zeitpunkt, Person und Software-Version; Zweitbefund unabhängig. |
| Datentyp · Kardinalität · Kategorie | Reference · 1..* · prozedur (Vorschlag: 0..* je Phase (≥ 1 je LDCT)) |
| BPMN | Activity_1tdikdp „Erstbefundung ohne CAD-Software (§5 Abs.1) durchführen“; Activity_1mvivag „Erstbefundung mit CAD-Software (§5 Abs.1) durchführen“; Activity_1ww2vbt „Zweitbefundung ohne CAD-Software (§5 Abs.2) durchführen“; Activity_0mx6d87 „Zweitbefundung mit CAD-Software (§5 Abs.2) durchführen“ (process_step: G9 Befundung \| Activity_1tdikdp → Activity_1mvivag; Zweitbefunder: Activity_1ww2vbt → Activity_0mx6d87) |
| Rolle | Erstbefunder; Zweitbefunder |
| Trigger | je Befundungsschritt (zuerst ohne, dann mit CAD) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. Verfahren LuKrFrühErkV § 5 Abs. 1–2; Dokumentation KFE-RL § 44 S. 1, QS-Vereinbarung § 13f, StrlSchG § 85 Abs. 1 S. 2 Nr. 4; Mindestzahlen „befunden und dokumentieren“ § 6 Abs. 1 S. 2 und Abs. 2 S. 2. Software-Version und Zeitpunkt sind nicht normiert (S3 Empf. 5.8). |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 5 Abs. 1: „die Computertomographieaufnahme zunächst ohne und anschließend unter Nutzung einer Software zur …“ (Konsolidierung)<br>[Q12] S3-LL Lungenkarzinom 5.1, Empf. 5.8 (EK): „Die Software zur computerassistierten Detektion, Volumetrie und Berechnung der Volumenverdopplungszeit sollte qualitätsgesichert und für den Erst- und Zweitbefunder identisch sein.“<br>[Q02] KFE-RL, § 44 S. 1: „seine Befundung und im Falle einer Zweitbefundung auch diesen Befund“ |
| Codes (Beleg, Bewertung) | SNOMED CT 28191001 *Consultation and report by radiologist (procedure)* – Beleg: tx.fhir.org INT 20250201, Ontoserver: aktiv; Pattern von Procedure.code im MII-Profil radiologische-befundungsprozedur (Bildgebung 2026.0.0) – Bewertung: behalten; Semantik prüfen |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn ldctExamination (mihub.lung.screening.ldctExamination.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,80) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,70); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Mind. 2 Instanzen (Schema erlaubt nur 1..*). |
| Umsetzung (Synthese) | Rolle, Zeitpunkt und Person nur hier führen; readerAssessmentCategory trägt nur die Kategorie (Verknüpfung über Procedure.report). „Erst ohne, dann mit CAD“ als Attribut (Flag oder zwei Zeitstempel) statt mindestens zwei Instanzen (das Schema erlaubt kein 2..*). CAD-Software als Device-Referenz, konsistent mit cadAnalysisReport. Mapping: …/fhir/ext/modul-bildgebung/StructureDefinition/mii-pr-bildgebung-radiologische-befundungsprozedur. Die gemeinsame Beurteilung (§ 5 Abs. 3) über screeningResultCategory abgrenzen. Code 28191001 semantisch prüfen (Elternkonzept „Consultation“). |
| Status | **behalten** – eigenständig (Procedure je Befundung) |

##### 31. `cadAnalysisReport` – CAD-Auswertung als erweiterte Bilddokumentation

| Feld | Inhalt |
|---|---|
| Definition | Gespeicherte CAD-Auswertung (Detektion, Volumetrie, VDT) als erweiterte Bilddokumentation, z. B. DICOM Chest CAD SR. |
| Datentyp · Kardinalität · Kategorie | Reference · 0..* · dokument (Vorschlag: 1..* je LDCT (bzw. Invariante je ldctExamination)) |
| BPMN | Activity_1mvivag „Erstbefundung mit CAD-Software (§5 Abs.1) durchführen“; Activity_0mx6d87 „Zweitbefundung mit CAD-Software (§5 Abs.2) durchführen“; DataStoreReference_0sls43b „PACS“ (process_step: G9 Befundung \| Befundung mit CAD (Activity_1mvivag, Activity_0mx6d87); PACS) |
| Rolle | Erstbefunder; Zweitbefunder (CAD-Software) |
| Trigger | je CAD-gestützter Befundung |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. Anlage zu § 4 Abs. 1 S. 1 (Zeile CAD-Software: „Speicherung der Auswertung als erweiterte Bilddokumentation“) i. V. m. § 4 Abs. 1 S. 2 und § 5 Abs. 1–2 LuKrFrühErkV; QS-Vereinbarung § 11 Abs. 5. Ein Speicherformat schreibt die Verordnung nicht vor. |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, Anlage zu § 4: „Detektion und Volumetrie von Lungenrundherden sowie Berechnung der Volumenverdopplungszeit und Speicherung der …“ (Konsolidierung)<br>[Q01] LuKrFrühErkV, § 5 Abs. 1: „zunächst ohne und anschließend unter Nutzung einer Software zur computerassistierten Detektion befundet (Erstbefunder)“ |
| Codes (Beleg, Bewertung) | DICOM DCM 112000 *Chest CAD Report* – Beleg: DICOM PS3.16 2026d, Annex D; tx.fhir.org $lookup mit System http://dicom.nema.org/resources/ontology/DCM – Bewertung: Elementcode, wenn ein Chest CAD SR erzeugt wird<br>DICOM DCM 126000 *Imaging Measurement Report* – Beleg: DICOM PS3.16 2026d (Gegenprüfung) – Bewertung: Alternative (TID 1500) |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn ldctExamination (mihub.lung.screening.ldctExamination.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,88) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,80); vollständige Urteile in candidates.json |
| Umsetzung (Synthese) | Kardinalität an die Rechtslage anpassen: je LDCT mindestens eine CAD-Auswertung des Erstbefunders, bei Zweitbefundung eine weitere (1..* oder Invariante je ldctExamination statt 0..*). Binding extensible/example: DCM 112000 nur, wenn ein Chest CAD SR erzeugt wird; DCM 126000 (TID 1500) als Alternative. „dicom-dcm“ in scripts/verify-terminology.py (SYSTEM_URL) ergänzen oder den Code unter standard_mappings (dicom-sr) führen. pulmonaryNoduleFinding, noduleSizeMeasurement und noduleVolumeDoublingTime hängen von cadAnalysisReport ab (dependsOn). Software und Lesemodus nicht doppelt zu screeningReadingEvent erfassen. |
| Status | **behalten** – eigenständig |

##### 32. `pulmonaryNoduleFinding` – Lungenrundherd (Einzelbefund je Rundherd)

| Feld | Inhalt |
|---|---|
| Definition | Befund je Rundherd: Kennung, Typ, Lage, Baseline/neu/vorbestehend, Verlauf, benigne bzw. suspekte Merkmale, Bildreferenz. |
| Datentyp · Kardinalität · Kategorie | Reference · 0..* · befund |
| BPMN | Activity_1tdikdp „Erstbefundung ohne CAD-Software (§5 Abs.1) durchführen“; Activity_1mvivag „Erstbefundung mit CAD-Software (§5 Abs.1) durchführen“; Activity_1ww2vbt „Zweitbefundung ohne CAD-Software (§5 Abs.2) durchführen“; Activity_0mx6d87 „Zweitbefundung mit CAD-Software (§5 Abs.2) durchführen“ (process_step: G9 Befundung \| Activity_1mvivag (und Zweitbefundung)) |
| Rolle | Erstbefunder; Zweitbefunder |
| Trigger | je detektiertem Rundherd (mindestens der führende Herd) |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. V-Lung-RADS (S3 Empf. 5.9, Tab. 17) und Lung-RADS Note 1 setzen eine Bewertung je Rundherd voraus; die Detektion ist CAD-Pflichtfunktion (Anlage). Eine Einzeldokumentation je Rundherd ist nicht normiert. |
| Quellen mit Zitat | [Q20] ACR Lung-RADS v2022, Note 1: „Each exam should be coded 0-4 based on the nodule with the highest degree of suspicion.“ (Konsolidierung)<br>[Q16] DRG/DGP/DGT-Positionspapier, Supplement, Tab. S1 Anm. 1: „Jede Untersuchung wird basierend auf dem Rundherd mit dem höchsten Verdachtsgrad mit 0-4 codiert.“ |
| Codes (Beleg, Bewertung) | SNOMED CT 786838002 *Nodule of lung (disorder)* – Beleg: Ontoserver INT 20260601, tx.fhir.org INT 20250201: aktiv – Bewertung: Condition.code bzw. Observation.value, nicht Observation.code<br>DICOM DCM 112013 *Location in Chest* – Beleg: DICOM PS3.16 2026d (Gegenprüfung) – Bewertung: Lageangabe (vorgeschlagen) |
| Bezug zum Bestand | overlaps_existing: ctThoraxFinding; tumorLocalisation. Vorgeschlagene Relationen: hasPart noduleSizeMeasurement (mihub.lung.screening.noduleSizeMeasurement.v0.1); hasPart noduleVolumeDoublingTime (mihub.lung.screening.noduleVolumeDoublingTime.v0.1); hasPart noduleMalignancyProbability (mihub.lung.screening.noduleMalignancyProbability.v0.1); dependsOn cadAnalysisReport (mihub.lung.screening.cadAnalysisReport.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,60) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,85); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Teilsolide ohne SNOMED-Konzept; Erfassungsumfang offen. |
| Umsetzung (Synthese) | Klammerbefund je Rundherd. 786838002 ist ein disorder-Konzept: als Condition.code oder Observation.valueCodeableConcept verwenden, nicht als Observation.code. Den Verlauf nicht als freies Attribut doppeln, sondern über noduleSizeMeasurement und noduleVolumeDoublingTime abbilden (hasPart, analog pulmonaryFunctionTest). Lage über SNOMED-Körperstrukturen oder DICOM 112013 statt der ICD-O-3-Codes aus tumorLocalisation. Stabile Rundherd-Kennung (Identifier) für den Vergleich über Runden (§ 4 Abs. 2). Erfassungsumfang (alle, nicht-benigne oder führender Herd) ist zu entscheiden (E13). Quellen ergänzen: Lung-RADS-Kategorientabelle mit Notes 4–8, V-Lung-RADS (S3 Tab. 17; Supplement Tab. S1 Anm. 1), LuKrFrühErkV-Anlage. |
| Status | **behalten** – eigenständig (Klammerbefund; hasPart Größe, VDT, Malignitätswahrscheinlichkeit) |

##### 33. `noduleSizeMeasurement` – Rundherdgröße (Volumen, mittlerer Durchmesser, solide Komponente)

| Feld | Inhalt |
|---|---|
| Definition | Rundherdvolumen (mm³, ganzzahlig) bzw. mittlerer Durchmesser (mm, eine Dezimale), bei teilsoliden Herden auch solide Komponente. |
| Datentyp · Kardinalität · Kategorie | Quantity · 0..* · messwert |
| BPMN | Activity_1tdikdp „Erstbefundung ohne CAD-Software (§5 Abs.1) durchführen“; Activity_1mvivag „Erstbefundung mit CAD-Software (§5 Abs.1) durchführen“ (process_step: G9 Befundung \| Activity_1tdikdp / Activity_1mvivag) |
| Rolle | Befunder (CAD-Volumetrie) |
| Trigger | je Rundherd und Untersuchung |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. Messregeln: DRG/DGP/DGT-Supplement Tab. S1 Anm. 4, Lung-RADS Note 4. Die Volumetrie ist als CAD-Funktion vorgeschrieben (Anlage), der einzelne Messwert als Befundfeld nicht. |
| Quellen mit Zitat | [Q16] DRG/DGP/DGT-Positionspapier, Supplement, Tab. S1 Anm. 4: „Lungenrundherdmessung: Volumina werden auf die nächste ganze Zahl in mm³ gerundet.“ (Konsolidierung)<br>[Q16] DRG/DGP/DGT-Positionspapier, Supplement, Tab. S1 Anm. 4: „Nur wenn eine Volumetrie technisch nicht möglich ist, messen Sie sowohl die lange als auch die kurze Achse auf eine Dezimalstelle in mm und geben Sie den mittleren Rundherddurchmesser auf eine Dezimalstelle an“<br>[Q20] ACR Lung-RADS v2022, Note 4: „Volumes, if obtained, should be reported to the nearest whole number in mm³.“ |
| Codes (Beleg, Bewertung) | SNOMED CT 118565006 *Volume (property) (qualifier value)* – Beleg: Ontoserver INT 20260601: aktiv – Bewertung: Volumen<br>SNOMED CT 81827009 *Diameter (qualifier value)* – Beleg: Ontoserver INT 20260601: aktiv (Gegenprüfung) – Bewertung: mittlerer Durchmesser (vorgeschlagen) |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: isPartOf pulmonaryNoduleFinding (mihub.lung.screening.pulmonaryNoduleFinding.v0.1); dependsOn cadAnalysisReport (mihub.lung.screening.cadAnalysisReport.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,70); vollständige Urteile in candidates.json |
| Umsetzung (Synthese) | Aufteilen: noduleVolume (mm3, SNOMED 118565006) und noduleMeanDiameter (mm, eine Dezimale; SNOMED 81827009; Methode Mittel aus Lang- und Kurzachse); die solide Komponente teilsolider Herde als Komponente mit Qualifier gesamt/solide. Rangfolge in der Definition festhalten: Volumen ist Primärmaß, Durchmesser nur, wenn Volumetrie technisch nicht möglich ist. isPartOf pulmonaryNoduleFinding; dependsOn cadAnalysisReport. |
| Status | **behalten** – Teil von pulmonaryNoduleFinding (Aufteilung empfohlen) |

##### 34. `noduleVolumeDoublingTime` – Volumenverdopplungszeit (VDT) des Rundherds

| Feld | Inhalt |
|---|---|
| Definition | Volumenverdopplungszeit in Tagen aus zwei oder mehr Volumina, mit Vergleichsuntersuchung, Software und Methode. |
| Datentyp · Kardinalität · Kategorie | Quantity · 0..* · messwert |
| BPMN | Activity_1mvivag „Erstbefundung mit CAD-Software (§5 Abs.1) durchführen“ (process_step: G9 Befundung \| Activity_1mvivag) |
| Rolle | Befunder (CAD-Berechnung) |
| Trigger | Rundherd mit mindestens zwei Volumenmessungen (Vergleichsuntersuchung) |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. S3 Empf. 5.8/5.9 mit Tab. 17 (V-Lung-RADS: VDT-Schwelle 600 Tage); die Berechnung ist als CAD-Funktion vorgeschrieben (Anlage), ein eigenes Befundfeld nicht. |
| Quellen mit Zitat | [Q18] ESTI (Prokop et al. 2026), Definition of growth: „If multiple time points are available, a logistic regression across all time points should be used to more …“ (Konsolidierung)<br>[Q18] ESTI (Prokop et al., Eur Radiol 2026;36:122–134), Definition of growth: „For follow-up, the same segmentation software should be used to improve the reproducibility of measurements.“<br>[Q12] S3-LL Lungenkarzinom 5.1, Tab. 17, Kategorie 4A: „mit <VDT 600 Tage“ |
| Codes (Beleg, Bewertung) | NCIt C113268 *Volume Doubling Time* – Beleg: NCI EVS REST API, NCIt 26.09d: aktiv; kein SNOMED-, LOINC- oder DCM-Konzept gefunden – Bewertung: einziges belegtes Konzept; pending-mapping |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: isPartOf pulmonaryNoduleFinding (mihub.lung.screening.pulmonaryNoduleFinding.v0.1); dependsOn noduleSizeMeasurement (mihub.lung.screening.noduleSizeMeasurement.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,80) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,85); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Kein SNOMED/LOINC/DCM-Code; Schwellen je Fassung verschieden → Rohdaten speichern. |
| Umsetzung (Synthese) | isPartOf pulmonaryNoduleFinding; abgeleitet aus mindestens zwei Volumina (noduleSizeMeasurement), der Vergleichsuntersuchung (ImagingStudy) und der CAD-Software (Device); Methode (Zwei-Punkt-Formel oder Regression) als Observation.method; Einheit UCUM d. Nur den Rohwert speichern, keine fassungsabhängigen Schwellen (V-Lung-RADS 600 Tage, ESTI 250/400/500 Tage, NELSON 400/600 Tage). „ncit“ fehlt in scripts/verify-terminology.py und tx.fhir.org kennt C113268 nicht: SYSTEM_URL ergänzen oder standard_binding_status pending-mapping. Deutsche Primärquellen ergänzen (Anlage zu § 4, S3 Empf. 5.8 und 5.9). |
| Status | **behalten** – Teil von pulmonaryNoduleFinding |

##### 35. `noduleMalignancyProbability` – Malignitätswahrscheinlichkeit des Rundherds

| Feld | Inhalt |
|---|---|
| Definition | Malignitätswahrscheinlichkeit in % mit Modell (Brock/PanCan, Herder); Entscheidungskriterium bei Lung-RADS 4A (> 10 %). |
| Datentyp · Kardinalität · Kategorie | Quantity · 0..* · assessment |
| BPMN | Activity_10riunt „Gemeinsame Beurteilung vornehmen (§5 Abs.3)“; Activity_0gyncma „Gemeinsame Beurteilung vornehmen (§5 Abs.3)“ (process_step: G9 Befundung \| Gemeinsame Beurteilung (Activity_10riunt/Activity_0gyncma)) |
| Rolle | Erst- und Zweitbefunder (gemeinsame Beurteilung) |
| Trigger | solider Rundherd der Kategorie 4A in der Baseline-LDCT; 4B-Management |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. S3 Tab. 17, Kategorie 4A (Kann-Option PET/CT nach Fallkonferenzbeschluss bei Malignitätswahrscheinlichkeit > 10 %); das Modell legt die S3 nicht fest. |
| Quellen mit Zitat | [Q12] S3-LL Lungenkarzinom, Tab. 17, 4A: „wenn die *Wahrscheinlichkeit von Malignität >10% beim Baseline LDCT ist“ (Konsolidierung)<br>[Q16] DRG/DGP/DGT-Positionspapier, Supplement, Tab. S1 Anm. 13: „Radiologen werden ermutigt, das Bewertungstool von McWilliams, et al. für CT Befunde zu verwenden“ |
| Codes (Beleg, Bewertung) | keine Codes beansprucht; lokale Werteliste bzw. no-standard-found |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: isPartOf pulmonaryNoduleFinding (mihub.lung.screening.pulmonaryNoduleFinding.v0.1); dependsOn noduleSizeMeasurement (mihub.lung.screening.noduleSizeMeasurement.v0.1); dependsOn emphysemaSeverity (mihub.lung.screening.emphysemaSeverity.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,75) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,70); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Verbindliches Modell offen. |
| Umsetzung (Synthese) | Im Screening auf den Baseline-Wert (Brock/PanCan) aus der gemeinsamen Beurteilung beschränken; den Herder-Wert nach PET/CT der Abklärung zuordnen. Modell verpflichtend als Observation.method, Einheit UCUM %, lokaler Code (no-standard-found). isPartOf pulmonaryNoduleFinding, dependsOn noduleSizeMeasurement; emphysemaSeverity (vorhanden/nicht vorhanden) ist Brock-Eingang. Abgrenzung zum verworfenen personenbezogenen Risikoscore (lungCancerRiskModelScore). S3 Empf. 6.29, 6.30 und 6.41 betreffen inzidentelle Rundherde außerhalb der Früherkennung und sind kein Screening-Beleg. |
| Status | **behalten** – Teil von pulmonaryNoduleFinding |

##### 36. `lungRadsCategory` – Lung-RADS-Kategorie (V-Lung-RADS 2022) mit Version und S-Modifikator

| Feld | Inhalt |
|---|---|
| Definition | V-Lung-RADS-2022-Kategorie 0–4X je Befundung und abschließend, mit Version, Grund bei Kategorie 0 und Modifikator S. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..* · assessment (Vorschlag: 0..* (1..* nur bei verbindlicher Vorgabe)) |
| BPMN | Activity_1mvivag „Erstbefundung mit CAD-Software (§5 Abs.1) durchführen“; Activity_0mx6d87 „Zweitbefundung mit CAD-Software (§5 Abs.2) durchführen“; Gateway_10udrva „Befund kategorie?“ (process_step: G9 Befundung \| Activity_1mvivag, Activity_0mx6d87 → Befund kategorie? (Gateway_10udrva)) |
| Rolle | Erstbefunder; Zweitbefunder |
| Trigger | je Befundung und abschließend |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. S3 Empf. 5.9 (EK, „soll“); TrG zu § 42 Abs. 2 und 3 („sollte“); die KFE-RL nennt Lung-RADS nur als Fortbildungsinhalt (§ 43 Abs. 2 Nr. 4) – keine Rechtspflicht. |
| Quellen mit Zitat | [Q12] S3-LL Lungenkarzinom, Empf. 5.9 (EK): „soll in Deutschland einheitlich die modifizierte Lung-RADS Klassifikation von 2022 mit integrierter …“ (Konsolidierung)<br>[Q03] G-BA Tragende Gründe 18.06.2025, zu § 42 Abs. 2 und 3: „Hierfür sollte die … modifizierte Lung-RADS-Klassifikation mit Einbezug der Volumenverdopplungszeit verwendet werden.“ |
| Codes (Beleg, Bewertung) | SNOMED CT 1362105002 *Lung Imaging Reporting and Data System category (observable entity)* – Beleg: Ontoserver INT 20260601: aktiv, Modul 900000000000207008, effectiveTime 20250301; tx.fhir.org (INT 20250201) kennt den Code nicht – Bewertung: Observation.code<br>NCIt C226306 *Lung Imaging Reporting and Data System* – Beleg: NCI EVS, NCIt 26.09d: aktiv – Bewertung: nur Systemangabe<br>NCIt C226307–C226313 *Lung-RADS-Kategorien 0–4X* – Beleg: NCI EVS, NCIt 26.09d (Gegenprüfung) – Bewertung: Mapping der Kategoriewerte (vorgeschlagen)<br>RadElement RDE1702 *Category of findings* – Beleg: RSNA RadElement-API, Set RDES267 (ACR, Published) – Bewertung: nur Mapping (ACR-v2022-Unterkategorien, nicht V-Lung-RADS)<br>SNOMED CT 1362106001 *Lung Imaging Reporting and Data System (assessment scale)* – Beleg: Gegenprüfung (Ontoserver) – Bewertung: nur Systemangabe (vorgeschlagen) |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn pulmonaryNoduleFinding (mihub.lung.screening.pulmonaryNoduleFinding.v0.1); dependsOn incidentalFinding (mihub.lung.screening.incidentalFinding.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,90) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,85); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Nur 'sollte' (TrG) → nicht Pflicht; Kategoriewerte lokal mit Mapping. |
| Umsetzung (Synthese) | SNOMED 1362105002 als Observation.code. Werte als lokales CodeSystem „V-Lung-RADS 2022“ (0, 1, 2, 3, 4A, 4B, 4X, Modifikator S, Grund bei Kategorie 0) mit Mapping auf NCIt C226307–C226313 und RadElement RDE1702; NCIt C226306 bzw. SNOMED 1362106001 nur als Systemangabe. Die Trennung je Befunder/abschließend mit readerAssessmentCategory und screeningResultCategory harmonisieren (Qualifier). S-Modifikator dependsOn incidentalFinding. Mindest-SNOMED-Edition (INT ab 2025-03-01) dokumentieren; die MII-Bildgebung bindet Observation.code an „< 404684003 Clinical finding“ – das Observable ist dort nicht konform (offene Frage). |
| Status | **behalten** – eigenständig |

##### 37. `readerAssessmentCategory` – Befundkategorie je Befunder (Erst-/Zweitbefund)

| Feld | Inhalt |
|---|---|
| Definition | Rechtliche Kategorie (unauffällig, kontroll-, abklärungsbedürftig) je Befunder mit Text, Datum und Rolle. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..* · befund |
| BPMN | Gateway_0mk0bmb „Kontroll- oder abklärungsbedürftiger Befund?“; Activity_1ww2vbt „Zweitbefundung ohne CAD-Software (§5 Abs.2) durchführen“; Activity_0mx6d87 „Zweitbefundung mit CAD-Software (§5 Abs.2) durchführen“ (process_step: G9 Befundung \| Erstbefunder: Gateway_0mk0bmb; Zweitbefunder: Activity_0mx6d87) |
| Rolle | Erstbefunder; Zweitbefunder |
| Trigger | nach jeder Befundung (je Befunder) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. Dokumentation von Erst- und Zweitbefund: QS-Vereinbarung § 13f, KFE-RL § 44 S. 1. Kategorien legaldefiniert in LuKrFrühErkV § 1 Abs. 4/5; der Erstbefund steuert die Zweitbefundung (§ 5 Abs. 2). |
| Quellen mit Zitat | [Q07] Vereinbarung Strahlendiagnostik, § 13f: „den Erst- und den Zweitbefund der NDCT und das Ergebnis der gemeinsamen Beurteilung sowie ggf. Empfehlungen für …“ (Konsolidierung)<br>[Q02] KFE-RL, § 44 S. 1: „Der Erstbefunder dokumentiert in der Patientenakte die Durchführung der Niedrigdosis-Computertomographie, seine Befundung und im Falle einer Zweitbefundung auch diesen Befund sowie das Ergebnis der gemeinsamen Beurteilung“ |
| Codes (Beleg, Bewertung) | keine Codes beansprucht; lokale Werteliste bzw. no-standard-found |
| Bezug zum Bestand | overlaps_existing: ctThoraxFinding. Vorgeschlagene Relationen: dependsOn screeningReadingEvent (mihub.lung.screening.screeningReadingEvent.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,75); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Kein Standardcode → lokales CodeSystem. |
| Umsetzung (Synthese) | Ein lokales CodeSystem gemeinsam mit screeningResultCategory nutzen; Begriffe an LuKrFrühErkV § 1 Abs. 4/5 binden; „unauffällig“ ist dort nicht definiert und als „weder kontroll- noch abklärungsbedürftig“ zu definieren; standard_binding_status no-standard-found. Rolle (Erst- oder Zweitbefunder) als performer bzw. Qualifier; dependsOn screeningReadingEvent. Die abschließende Kategorie nur in screeningResultCategory führen. Optional die Ableitungsregel aus lungRadsCategory nach S3 Empf. 5.9 dokumentieren. Quellen ergänzen: KFE-RL § 44 S. 1; LuKrFrühErkV § 1 Abs. 4/5 und § 5 Abs. 1–2. |
| Status | **behalten** – eigenständig (lokales CodeSystem gemeinsam mit screeningResultCategory) |

##### 38. `secondReadingRequest` – Veranlassung der Zweitbefundung (Konsiliarauftrag, Datenübermittlung)

| Feld | Inhalt |
|---|---|
| Definition | Konsiliarauftrag des Erstbefunders an eine:n Zweitbefunder:in mit Datum, Empfänger und sicherer Übermittlung der Bilder. |
| Datentyp · Kardinalität · Kategorie | Reference · 0..1 · mitbetreuung |
| BPMN | Activity_1rsqdi6 „Zweitbefundung anordnen (§5 Abs.2) und Überweisung ausstellen“ (process_step: G9 Befundung \| Erstbefunder: Zweitbefundung anordnen (Activity_1rsqdi6)) |
| Rolle | Erstbefunder (Auftrag) an Zweitbefunder |
| Trigger | kontroll- oder abklärungsbedürftiger Erstbefund (Pflichtfall); bei Bedarf auch sonst (S3 Empf. 5.8) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **bedingt**. Zweitbefundung Pflicht bei kontroll- oder abklärungsbedürftigem Erstbefund (LuKrFrühErkV § 5 Abs. 2; KFE-RL § 42 Abs. 1 S. 2); Datenübermittlung „soll“ elektronisch (S. 4–5); Überweisung nach BMV-Ä § 24 Abs. 4 Nr. 4. Den Auftrag selbst müssen weder KFE-RL § 44 noch QS-Vereinbarung § 13f dokumentiert sehen. |
| Quellen mit Zitat | [Q02] KFE-RL, § 42 Abs. 1: „sollen elektronische Kommunikations- und Informationstechnologien eingesetzt werden“ (Konsolidierung)<br>[Q12] S3-LL Lungenkarzinom 5.1, Empf. 5.8 (EK): „Darüber hinaus sollte bei Bedarf der Erstbefunder auch eine Zweitbefundung anfordern.“<br>[Q06] EBA 87. Sitzung (11.03.2026), GOP 01878 (obligater Leistungsinhalt): „Veranlassung der Zweitbefundung und abschließende gemeinsame Beurteilung nach § 42 Krebsfrüherkennungs-Richtlinie“ |
| Codes (Beleg, Bewertung) | EBM-GOP 01878 *Veranlassung der konsiliarischen Zweitbefundung* – Beleg: EBA 87. Sitzung (11.03.2026), Teil A; nur binnen 14 Tagen nach 01871/01872 – Bewertung: kein Kerncode; nur Abrechnungsbezug |
| Bezug zum Bestand | overlaps_existing: referralOrder. Vorgeschlagene Relationen: specializes referralOrder (mihub.lung.primarycare.referralOrder.v0.1); dependsOn readerAssessmentCategory (mihub.lung.screening.readerAssessmentCategory.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,65) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,65); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | 01878 nur binnen 14 Tagen; Zweitbefundung bei unauffälligem Erstbefund nicht gefordert. |
| Umsetzung (Synthese) | specializes mihub.lung.primarycare.referralOrder.v0.1; FHIR ServiceRequest mit requester = Erstbefunder, performer = Zweitbefunder, authoredOn, supportingInfo auf ImagingStudy bzw. cadAnalysisReport. EBM 01878 nicht als Kerncode (umfasst auch die gemeinsame Beurteilung), nur als Abrechnungsbezug; ServiceRequest.code lokal bzw. pending-mapping. mandatory_by_law als „bedingt“ kennzeichnen. Die Zweitbefundung (screeningReadingEvent) verweist per basedOn auf den Auftrag; die sichere Übermittlung (KFE-RL § 42 Abs. 1 S. 5) als Attribut. |
| Status | **behalten** – Spezialisierung von referralOrder (primarycare) |

##### 39. `incidentalFinding` – Klinisch relevanter Nebenbefund mit Empfehlung

| Feld | Inhalt |
|---|---|
| Definition | Relevanter Nebenbefund ohne Lungenkrebsbezug (z. B. ILA, Aortenaneurysma, Schilddrüse) mit Ausprägung, neu/vorbekannt und Empfehlung. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 0..* · befund |
| BPMN | Activity_1tdikdp „Erstbefundung ohne CAD-Software (§5 Abs.1) durchführen“; Activity_12ef5s1 „Rückmeldung übermitteln“ (process_step: G9 Befundung \| Activity_1tdikdp → Rückmeldung übermitteln (Activity_12ef5s1)) |
| Rolle | Erstbefunder; Zweitbefunder |
| Trigger | klinisch relevanter Nebenbefund ohne Lungenkrebsbezug |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. Lung-RADS v2022 Note 15 (S-Modifikator „may“); DRG/DGP/DGT-Supplement Tab. S1 Anm. 15 (klinisch relevant = abklärungsbedürftig) i. V. m. S3 Empf. 5.9. LuKrFrühErkV und KFE-RL regeln Nebenbefunde nicht. |
| Quellen mit Zitat | [Q20] ACR Lung-RADS v2022, Note 15b: „Findings that are already known, and have been or are in the process of clinical evaluation DO NOT require an …“ (Konsolidierung)<br>[Q20] ACR Lung-RADS v2022, Note 15: „An S modifier may be added to Lung-RADS categories 0-4 for clinically significant or potentially clinically significant findings unrelated to lung cancer.“<br>[Q16] DRG/DGP/DGT-Positionspapier, Supplement, Tab. S1 Anm. 15: „Als klinisch relevant werden solche Befunde definiert, die eine weitere Abklärung erfordern.“ |
| Codes (Beleg, Bewertung) | SNOMED CT 1381861002 *Interstitial lung abnormality (FSN: Abnormality of interstitial tissue of lung (finding))* – Beleg: Ontoserver: aktiv, Modul INT, effectiveTime 20251201; tx.fhir.org (INT 20250201) kennt den Code nicht – Bewertung: nur Beispielwert; setzt SNOMED CT INT ab 2025-12-01 voraus<br>SNOMED CT 261087003 *Incidental (qualifier value)* – Beleg: Ontoserver: aktiv (Gegenprüfung) – Bewertung: optionaler Qualifier (vorgeschlagen) |
| Bezug zum Bestand | overlaps_existing: comorbidity. Vorgeschlagene Relationen: – |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,75) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,70); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Mitteilung nur nach Einwilligung und Vereinbarung. |
| Umsetzung (Synthese) | Auf S-relevante Nebenbefunde begrenzen, die eine weitere Abklärung erfordern; Koronarkalk und Emphysem sind eigene Routinefelder (specializes incidentalFinding). Als Befundgruppe: Befundcode (Binding < 404684003 \|Clinical finding\|, extensible; ILA nur als Beispielwert), Ausprägung, Status neu/vorbekannt (Lung-RADS Note 15b; fehlt in der deutschen V-Lung-RADS-Fassung), Empfehlung; optional Qualifier 261087003 \|Incidental\|. Die Notiz „Mitteilung nur nach Einwilligung und Vereinbarung“ streichen oder belegen: einschlägig ist nur KFE-RL § 42 Abs. 2 S. 2 (Übermittlung des gesamten Befundberichts an die Praxis). Bestätigte Diagnosen bleiben in comorbidity. Bezug zu lungRadsCategory (S) und clarificationReferral. Beispielbefunde und Schwellen mit O’Dowd et al. 2023, Tab. 2 belegen. |
| Status | **behalten** – eigenständig (Befundgruppe) |

##### 40. `coronaryArteryCalcification` – Koronararterienverkalkung (visuell, optional Agatston)

| Feld | Inhalt |
|---|---|
| Definition | Koronarkalk visuell (keine, gering, mäßig, schwer), optional Agatston-Score, mit Empfehlung zur hausärztlichen Abklärung. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 0..1 · befund |
| BPMN | Activity_1tdikdp „Erstbefundung ohne CAD-Software (§5 Abs.1) durchführen“; Activity_12ef5s1 „Rückmeldung übermitteln“ (process_step: G9 Befundung \| Activity_1tdikdp → Activity_12ef5s1) |
| Rolle | Erstbefunder |
| Trigger | jede Befundung (routinemäßige Angabe) |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. DRG/DGP/DGT-Supplement Tab. S1 Anm. 15 („sollten routinemäßig … angegeben werden“); Skala und Empfehlung nach O’Dowd et al. 2023 (Tab. 2). |
| Quellen mit Zitat | [Q16] DRG/DGP/DGT-Positionspapier, Supplement, Tab. S1 Anm. 15: „Emphysem oder Koronarkalk sollten routinemäßig als häufige Komorbiditäten im Befund angegeben werden.“ (Konsolidierung)<br>[Q17] O’Dowd et al. 2023 (Eur J Cardiothorac Surg 2023;64:ezad302), Tab. 2: „Classify (using simple visual scoring) as: None, Mild, Moderate, Severe“<br>[Q17] O’Dowd et al. 2023, Coronary artery calcification: „The statements recommend primary care evaluation of cardiovascular risk factors in case of significant CAC.“<br>[Q16] DRG/DGP/DGT-Positionspapier, Supplement, Tab. S1 Anm. 15: „Emphysem oder Koronarkalk sollten routinemäßig als häufige Komorbiditäten im Befund angegeben werden.“ |
| Codes (Beleg, Bewertung) | SNOMED CT 445512009 *Calcification of coronary artery (disorder)* – Beleg: tx.fhir.org, Ontoserver: aktiv – Bewertung: nur Befundwert bei vorhandenem Kalk<br>SNOMED CT 450360000 *Coronary artery calcium score (observable entity)* – Beleg: Ontoserver: aktiv, effectiveTime 20120731 (Gegenprüfung) – Bewertung: vorgeschlagener Elementcode |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: specializes incidentalFinding (mihub.lung.screening.incidentalFinding.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,70); vollständige Urteile in candidates.json |
| Umsetzung (Synthese) | Element-Code als Observable SNOMED 450360000; Wert = visuelle Stufe keine \| gering \| mäßig \| schwer (lokales Ordinal-ValueSet, no-standard-found; Quelle O’Dowd 2023 Tab. 2); Agatston-Score als optionale, alternative Komponente (Quantity); 445512009 nur als Befundwert bei vorhandenem Kalk. Die Empfehlung (hausärztliche Abklärung des kardiovaskulären Risikos bei mäßigem oder schwerem Koronarkalk) gehört in die Empfehlungskomponente von incidentalFinding bzw. in die Überweisung, nicht ins Element. specializes incidentalFinding. |
| Status | **behalten** – Spezialisierung von incidentalFinding |

##### 41. `emphysemaSeverity` – Lungenemphysem – Ausprägung

| Feld | Inhalt |
|---|---|
| Definition | Emphysem-Ausprägung (kein, leicht < 25 %, mittel 25–50 %, schwer > 50 %); Nebenbefund und Brock-Eingang. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 0..1 · befund |
| BPMN | Activity_1tdikdp „Erstbefundung ohne CAD-Software (§5 Abs.1) durchführen“; Activity_12ef5s1 „Rückmeldung übermitteln“ (process_step: G9 Befundung \| Activity_1tdikdp → Activity_12ef5s1) |
| Rolle | Erstbefunder |
| Trigger | jede Befundung (routinemäßige Angabe) |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. DRG/DGP/DGT-Supplement Tab. S1 Anm. 15; Graduierung nach O’Dowd et al. 2023 („Emphysema“, Tab. 2). |
| Quellen mit Zitat | [Q17] O'Dowd et al. 2023, Emphysema: „A suitable qualitative classification is mild (<25%) moderate (25–50%) and severe (>50%).“ (Konsolidierung)<br>[Q17] O’Dowd et al. 2023, Emphysema: „Emphysema on CT cannot be used to diagnose COPD“<br>[Q17] O’Dowd et al. 2023, Tab. 2: „Refer those with moderate to severe radiological emphysema for clinical assessment“ |
| Codes (Beleg, Bewertung) | SNOMED CT 87433001 *Pulmonary emphysema (disorder)* – Beleg: Ontoserver: aktiv, INT-Kernmodul; Elternkonzept 13645005 (COPD) – Bewertung: nur Befundfokus mit Hinweis „keine COPD-Diagnose“ |
| Bezug zum Bestand | overlaps_existing: comorbidity. Vorgeschlagene Relationen: specializes incidentalFinding (mihub.lung.screening.incidentalFinding.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,70); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | CT-Emphysem ist keine COPD-Diagnose. |
| Umsetzung (Synthese) | Strikt als Bildbefund-Beobachtung modellieren, nicht als Condition. 87433001 nur als Befundfokus bzw. Observation.code mit Hinweis „keine COPD-Diagnose“. Wert = lokales Ordinal-ValueSet kein \| leicht < 25 % \| mittel 25–50 % \| schwer > 50 % (no-standard-found; Quelle O’Dowd 2023). specializes incidentalFinding; Eingang für noduleMalignancyProbability (Brock nutzt nur vorhanden/nicht vorhanden). Optional Attribut „Überweisung zur klinischen Abklärung bei mittel/schwer“. COPD- und Emphysem-Diagnosen bleiben in comorbidity. |
| Status | **behalten** – Spezialisierung von incidentalFinding |

#### G10 Ergebnis/Mitteilung

##### 42. `screeningResultCategory` – Abschließendes Ergebnis der Früherkennungsuntersuchung

| Feld | Inhalt |
|---|---|
| Definition | Abschließende Rechtskategorie (unauffällig, kontroll-, abklärungsbedürftig) mit Datum: Erstbefund oder Ergebnis der gemeinsamen Beurteilung. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..1 · befund (Vorschlag: 1..1 je Runde (vorher Status „ausstehend“)) |
| BPMN | Gateway_10udrva „Befund kategorie?“; Gateway_0mk0bmb „Kontroll- oder abklärungsbedürftiger Befund?“ (process_step: G10 Ergebnis \| Befund kategorie? (Gateway_10udrva) bzw. Gateway_0mk0bmb) |
| Rolle | Erstbefunder (bei gemeinsamer Beurteilung zusammen mit dem Zweitbefunder) |
| Trigger | Abschluss der Befundung je Runde |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Pflicht**. Kategorien legaldefiniert (LuKrFrühErkV § 1 Abs. 4/5); gemeinsame Beurteilung § 5 Abs. 3; Dokumentation KFE-RL § 44; Zählung für die QS (§ 7 Abs. 2 Nr. 2) und den Quartalsbericht an die KV (KFE-RL § 44). |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 1 Abs. 5: „Ein abklärungsbedürftiger Befund ist ein Befund, der mit so hoher Wahrscheinlichkeit auf ein Lungenkarzinom …“ (Konsolidierung)<br>[Q03] G-BA Tragende Gründe 18.06.2025, zu § 42 Abs. 2 und 3, S. 20: „Das Ergebnis der Lungenkrebsfrüherkennungsuntersuchung ist der abschließende Befund: bei unauffälligem Befund des Erstbefunders dieser Befund und bei einem abklärungsbedürftigen oder kontrollbedürftigen Befund des Erstbefunders das Ergebnis der gemeinsamen Beurteilung von Erst- und Zweitbefunder.“<br>[Q20] ACR Lung-RADS v2022, Note 9: „the Lung-RADS 0 category is temporary until the comparison study is available“ |
| Codes (Beleg, Bewertung) | keine Codes beansprucht; lokale Werteliste bzw. no-standard-found |
| Bezug zum Bestand | overlaps_existing: ctThoraxFinding. Vorgeschlagene Relationen: dependsOn readerAssessmentCategory (mihub.lung.screening.readerAssessmentCategory.v0.1); dependsOn lungRadsCategory (mihub.lung.screening.lungRadsCategory.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,85) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,85); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Lung-RADS 0 ohne Rechtskategorie; 4A je nach Pfad. |
| Umsetzung (Synthese) | jointAssessment hier aufgehen lassen, als Qualifier: Grundlage (Erstbefund allein \| gemeinsame Beurteilung), Zeitpunkt der abschließenden Beurteilung (effective), optional Konsensuskonferenz bei Dissens. Lokales CodeSystem: unauffällig \| kontrollbedürftig (§ 1 Abs. 4) \| abklärungsbedürftig (§ 1 Abs. 5); standard_binding_status no-standard-found; „unauffällig“ als nicht legaldefiniert kennzeichnen (TrG und KBV: „unauffällig“, S3: „negativ“). Mapping-Tabelle zu lungRadsCategory mit Regeln für Kategorie 0 und 4A. dependsOn readerAssessmentCategory; steuert recommendedManagement, recommendedControlInterval und abnormalResultDiscussion. Quellen ergänzen: § 1 Abs. 4 und 5, § 5 Abs. 2 und 3, § 7 Abs. 2 Nr. 2; KFE-RL § 42 Abs. 3 und § 44; TrG S. 20; S3 Empf. 5.9. |
| Status | **behalten** – eigenständig (nimmt jointAssessment auf) |

##### 43. `recommendedManagement` – Empfehlung für das weitere Vorgehen

| Feld | Inhalt |
|---|---|
| Definition | Empfohlenes weiteres Vorgehen: reguläre LDCT nach ≥ 12 Monaten, vorgezogene LDCT, Kurzintervall, bei 4A Kontrolle oder PET/CT, Abklärung. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 1..1 · versorgungsplanung |
| BPMN | Activity_07i9gmj „Empfehlung für (Zeitpunkt der) nächsten Untersuchung abgeben (§5 Abs.3)“; Activity_0es6xoa „Klinische Abklärung anzeigen und Überweisung ausstellen“ (process_step: G10 Ergebnis \| Empfehlung abgeben (Activity_07i9gmj) bzw. Abklärung (Activity_0es6xoa)) |
| Rolle | Erst- und Zweitbefunder (gemeinsam); bei unauffälligem Erstbefund der Erstbefunder |
| Trigger | mit dem abschließenden Ergebnis |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **bedingt**. KFE-RL § 44 („mit der Empfehlung für das weitere Vorgehen“) und LuKrFrühErkV § 5 Abs. 3 bei gemeinsamer Beurteilung, also bei kontroll- oder abklärungsbedürftigem Erstbefund; sonst S3 Empf. 5.9 (Leitlinie). |
| Quellen mit Zitat | [Q02] KFE-RL, § 44: „sowie das Ergebnis der gemeinsamen Beurteilung der Lungenkrebsfrüherkennungsuntersuchung mit der Empfehlung für …“ (Konsolidierung)<br>[Q05] KBV PraxisInfoSpezial (Oktober 2026), Befundung: „Beide Befunder müssen dann in einer gemeinsamen Beurteilung zu einem einheitlichen Ergebnis kommen und eine Empfehlung über weiterführende Maßnahmen zur Kontrolle oder Abklärung abgeben.“<br>[Q12] S3-LL Lungenkarzinom 5.1, Empf. 5.9 (EK): „reguläre Niedrigdosis-CT-Verlaufskontrolle nach mindestens 12 Monaten“ |
| Codes (Beleg, Bewertung) | SNOMED CT 424900004 *Recommendation - action (qualifier value)* – Beleg: Ontoserver, tx.fhir.org: aktiv – Bewertung: nur generisches Tag bzw. Mapping |
| Bezug zum Bestand | overlaps_existing: recommendationsForPrimaryCare. Vorgeschlagene Relationen: specializes recommendationsForPrimaryCare (mihub.lung.primarycare.recommendationsForPrimaryCare.v0.1); dependsOn screeningResultCategory (mihub.lung.screening.screeningResultCategory.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,80) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,65); vollständige Urteile in candidates.json |
| Umsetzung (Synthese) | Werteliste nur für die Art des nächsten Schritts: reguläre Screening-LDCT nach 12 Monaten \| Kontroll-LDCT \| ergänzende Bildgebung/Vergleich bei Lung-RADS 0 \| PET/CT \| Abklärung in spezialisierter Einrichtung (lokal, mit Mapping auf das Lung-RADS-Management; Belege S3 Empf. 5.9 und Supplement Tab. S1 Anm. 3). Den Zeitpunkt nur in recommendedControlInterval führen. Konsistenzregeln: unauffällig → regulär; kontrollbedürftig → Kontroll-LDCT plus Intervall; abklärungsbedürftig → Abklärung plus abnormalResultDiscussion und clarificationReferral. specializes recommendationsForPrimaryCare (Abgrenzung in definition_de); 424900004 nur als generisches Tag bzw. Mapping, nicht als Observation-Code. |
| Status | **behalten** – eigenständig (Spezialisierung von recommendationsForPrimaryCare) |

##### 44. `recommendedControlInterval` – Empfohlenes Kontrollintervall bis zur nächsten Untersuchung (Monate)

| Feld | Inhalt |
|---|---|
| Definition | Empfohlenes Kontrollintervall in Monaten ab LDCT bei kontrollbedürftigem Befund (< 12, z. B. 3 oder 6); daraus Fälligkeitsdatum. |
| Datentyp · Kardinalität · Kategorie | Quantity · 0..1 · versorgungsplanung (Vorschlag: 0..1 (Pflicht genau bei „kontrollbedürftig“)) |
| BPMN | Activity_07i9gmj „Empfehlung für (Zeitpunkt der) nächsten Untersuchung abgeben (§5 Abs.3)“ (process_step: G10 Ergebnis \| Empfehlung für nächste Untersuchung (§5 Abs.3) (Activity_07i9gmj)) |
| Rolle | Erst- und Zweitbefunder (gemeinsam) |
| Trigger | kontrollbedürftiges Ergebnis |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **bedingt**. LuKrFrühErkV § 5 Abs. 3 S. 2 (gemeinsame Empfehlung für den Zeitpunkt der nächsten Untersuchung); KFE-RL § 42 Abs. 3 Nr. 1 (Übermittlung an die Person); EBM 01872 verlangt die Angabe in Monaten. |
| Quellen mit Zitat | [Q01] LuKrFrühErkV, § 5 Abs. 3 S. 2: „ist eine gemeinsame Empfehlung für den Zeitpunkt der nächsten Untersuchung zur Lungenkrebsfrüherkennung abzugeben“ (Konsolidierung)<br>[Q20] ACR Lung-RADS v2022, Note 2: „The timing of follow-up imaging is from the date of the exam being interpreted.“<br>[Q06] EBA 87. Sitzung (11.03.2026), GOP 01872: „nur berechnungsfähig, wenn in der vorausgegangenen Untersuchung gemäß der Gebührenordnungsposition 01871 ein Kontrollintervall von weniger als 12 Monaten festgelegt wurde“ |
| Codes (Beleg, Bewertung) | EBM-GOP 01872 *Niedrigdosis-CT zur Befundkontrolle* – Beleg: EBA 87. Sitzung (11.03.2026); durch BA 854 (Wirkung 01.10.2026) unverändert – Bewertung: aus value_set entfernen (nur Abrechnungsbezug) |
| Bezug zum Bestand | overlaps_existing: followUpInterval; plannedFollowUpAppointment. Vorgeschlagene Relationen: dependsOn screeningResultCategory (mihub.lung.screening.screeningResultCategory.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,90) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,75); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Pflicht bei kontrollbedürftigem Befund; EBM 01872 verlangt Monatsangabe; Einheit mo. |
| Umsetzung (Synthese) | EBM 01872 aus value_set entfernen (Abrechnungsbezug, kein Konzept „empfohlenes Intervall“); value_set n/a, unit mo (UCUM). Invariante: Pflicht genau dann, wenn screeningResultCategory = kontrollbedürftig; Wert < 12. Fälligkeitsdatum = Datum der ausgewerteten LDCT + Intervall (Lung-RADS Note 2) ableiten; es speist screeningInvitation und plannedFollowUpAppointment. recommendedManagement ohne eigene Zeitwerte. dependsOn screeningResultCategory. Quellen ergänzen: KFE-RL § 42 Abs. 3 Nr. 1 und S3 Empf. 5.9 (3 bzw. 6 Monate). |
| Status | **behalten** – eigenständig |

##### 45. `abnormalResultDiscussion` – Besprechung eines abklärungsbedürftigen Befunds

| Feld | Inhalt |
|---|---|
| Definition | Besprechung des abklärungsbedürftigen Befunds und der Abklärung mit der Person (persönlich, Telefon, Video), möglichst vor dem schriftlichen Bericht. |
| Datentyp · Kardinalität · Kategorie | dateTime · 0..1 · kontakt-visite |
| BPMN | Activity_0es6xoa „Klinische Abklärung anzeigen und Überweisung ausstellen“ (process_step: G10 Ergebnis \| Klinische Abklärung anzeigen (Activity_0es6xoa, Zweitbefunder-Lane)) |
| Rolle | Erstbefunder (laut den Entscheidungserheblichen Gründen zum EBA-Beschluss und der KBV); im BPMN in der Lane Zweitbefunder |
| Trigger | abklärungsbedürftiges Ergebnis; zeitnah (EBM 01880 nur binnen 14 Tagen nach 01871/01872) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **bedingt**. KFE-RL § 42 Abs. 3 Nr. 2: Befund und weitere Maßnahmen sind mit der Person zu besprechen und die notwendigen Maßnahmen unverzüglich einzuleiten. Die 14 Tage sind nur die Abrechnungsfrist der GOP 01880. |
| Quellen mit Zitat | [Q02] KFE-RL, § 42 Abs. 3 Nr. 2: „sind dieser und die weiteren notwendigen Maßnahmen zur Abklärung mit der versicherten Person zu besprechen“ (Konsolidierung)<br>[Q03] G-BA Tragende Gründe 18.06.2025, S. 21: „sollte das Gespräch … möglichst vor der Übermittlung des schriftlichen Befundberichts stattfinden“<br>[Q05] KBV PraxisInfoSpezial (Oktober 2026), Befundmitteilung: „Der Erstbefunder bespricht zeitnah die weiteren Schritte mit der oder dem Versicherten.“ |
| Codes (Beleg, Bewertung) | EBM-GOP 01880 *Beratung bei abklärungsbedürftigem Befund* – Beleg: EBA 87. Sitzung (11.03.2026): auch telefonisch und per Videosprechstunde berechnungsfähig – Bewertung: nur Abrechnungsbezug |
| Bezug zum Bestand | overlaps_existing: consultationModality. Vorgeschlagene Relationen: dependsOn screeningResultCategory (mihub.lung.screening.screeningResultCategory.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,90) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,75); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | 01880 binnen 14 Tagen; BPMN-Lane klären. |
| Umsetzung (Synthese) | responsible_role = Erstbefunder; die BPMN-Lane (Zweitbefunder) korrigieren lassen. Kontaktform als Attribut mit der Werteliste von consultationModality (persönlich \| Telefon \| Video), keine neuen Codes. Bedingung: screeningResultCategory = abklärungsbedürftig. EBM 01880 als Abrechnungsbezug. Den Zusatz „möglichst vor dem schriftlichen Bericht“ mit den TrG (S. 21) belegen; KFE-RL, EBA und KBV sagen nur „unverzüglich“ bzw. „zeitnah“. |
| Status | **behalten** – eigenständig |

##### 46. `clarificationReferral` – Einleitung der Abklärung: Überweisung an spezialisierte Einrichtung

| Feld | Inhalt |
|---|---|
| Definition | Unverzüglich eingeleitete Abklärung: Überweisung zur spezialisierten Einrichtung (Sprechstunde, Fallkonferenz), auch wegen Nebenbefunden. |
| Datentyp · Kardinalität · Kategorie | Reference · 0..* · mitbetreuung |
| BPMN | Activity_0es6xoa „Klinische Abklärung anzeigen und Überweisung ausstellen“; DataObjectReference_0nkkzl8 „Überweisung“; Event_0nesy5q „Überweisung zur weiteren Behandlung wird nachgegangen“ (process_step: G10 Ergebnis \| Activity_0es6xoa → Versicherte: Event_0nesy5q) |
| Rolle | Erstbefunder (im BPMN Lane Zweitbefunder) an die spezialisierte Einrichtung |
| Trigger | abklärungsbedürftiges Ergebnis (§ 1 Abs. 5 LuKrFrühErkV) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **bedingt**. KFE-RL § 42 Abs. 3 Nr. 2 („die notwendigen Maßnahmen unverzüglich einzuleiten“). Das Ziel „spezialisierte Einrichtung“ ist Empfehlung (TrG S. 21; S3 Empf. 5.9 und 5.11); die Wahl der Einrichtung ist frei. |
| Quellen mit Zitat | [Q02] KFE-RL, § 42 Abs. 3 Nr. 2: „die notwendigen Maßnahmen unverzüglich einzuleiten“ (Konsolidierung)<br>[Q03] G-BA Tragende Gründe 18.06.2025, S. 21: „Als eine der notwendigen Maßnahmen zur Abklärung soll der versicherten Person eine Vorstellung in einer interdisziplinären Sprechstunde in einer spezialisierten Einrichtung gemäß § 43 Absatz 4 empfohlen werden.“<br>[Q12] S3-LL Lungenkarzinom 5.1, Empf. 5.11 (EK): „soll zeitnah in einer auf die Untersuchung und Behandlung von Lungenkrebs spezialisierten Einrichtung (gemäß der Anforderungskriterien in (Tabelle 15) erfolgen“ |
| Codes (Beleg, Bewertung) | SNOMED CT 3457005 *Patient referral (procedure)* – Beleg: Ontoserver INT 20260601, tx.fhir.org INT 20250201: aktiv – Bewertung: wie referralOrder<br>LOINC 57133-1 *Referral note* – Beleg: tx.fhir.org, LOINC 2.82: aktiv (Gegenprüfung) – Bewertung: optional (vorgeschlagen) |
| Bezug zum Bestand | overlaps_existing: referralOrder; tumorBoardDecision. Vorgeschlagene Relationen: specializes referralOrder (mihub.lung.primarycare.referralOrder.v0.1); dependsOn screeningResultCategory (mihub.lung.screening.screeningResultCategory.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,70) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,60); vollständige Urteile in candidates.json |
| Umsetzung (Synthese) | specializes mihub.lung.primarycare.referralOrder.v0.1. Auf abklärungsbedürftige Befunde nach § 1 Abs. 5 beschränken; „auch wegen Nebenbefunden“ streichen (dafür normale referralOrder mit reasonReference → incidentalFinding). „Fallkonferenz“ aus der Definition streichen (gehört zu screeningCaseConference). ServiceRequest: reasonReference → screeningResultCategory, performer = spezialisierte Einrichtung (KFE-RL § 43 Abs. 4), authoredOn als Nachweis für „unverzüglich“. Die TrG verlangen, verschiedene Einrichtungen vorzuschlagen. Optional LOINC 57133-1 wie in referralOrder. |
| Status | **behalten** – Spezialisierung von referralOrder (primarycare) |

##### 47. `structuredScreeningReport` – Strukturierter Befundbericht der Lungenkrebsfrüherkennung

| Feld | Inhalt |
|---|---|
| Definition | Strukturierter Befundbericht mit Befunden, V-Lung-RADS, Rechtskategorie, Empfehlung und verständlicher Erläuterung; an die Person, mit Einwilligung an die Praxis. |
| Datentyp · Kardinalität · Kategorie | Reference · 1..1 · dokument (Vorschlag: 1..1 je Runde (1..* je Episode)) |
| BPMN | Activity_12ef5s1 „Rückmeldung übermitteln“; DataObjectReference_0l2c9b0 „Rückmeldung Radiologie“; Event_1w13vdp „Rückmeldung der Radiologie eingegangen“; Event_13jgib0 „Rückmeldung der Radiologie eingegangen“ (process_step: G10 Mitteilung \| Rückmeldung übermitteln (Activity_12ef5s1) → Event_1w13vdp, Event_13jgib0) |
| Rolle | Erstbefunder |
| Trigger | Abschluss jeder Runde (Soll: binnen 14 Tagen nach Erstellung der Aufnahme) |
| Pflicht nach Norm | Konsolidierung: ja → nach Gegenprüfung: **Soll-Vorschrift**. KFE-RL § 42 Abs. 2 S. 1 („soll … innerhalb von 14 Tagen … als strukturierter Befundbericht übermittelt werden“), S. 2 (an die Praxis nur bei Einwilligung); Inhalte: TrG S. 21 („sollte“ V-Lung-RADS), S3 Empf. 5.9. |
| Quellen mit Zitat | [Q02] KFE-RL, § 42 Abs. 2: „soll durch den Erstbefunder innerhalb von 14 Tagen nach Erstellung der Niedrigdosis-Computertomographieaufnahme …“ (Konsolidierung)<br>[Q02] KFE-RL, § 42 Abs. 2 S. 1: „Das Ergebnis der Lungenkrebsfrüherkennungsuntersuchung soll durch den Erstbefunder innerhalb von 14 Tagen nach Erstellung der Niedrigdosis-Computertomographieaufnahme der versicherten Person als strukturierter Befundbericht übermittelt werden.“<br>[Q03] G-BA Tragende Gründe 18.06.2025, S. 21: „Der strukturierte Befundbericht beschreibt die relevanten Befunde und gibt Empfehlungen für das weitere Vorgehen.“ |
| Codes (Beleg, Bewertung) | LOINC 18748-4 *Diagnostic imaging study* – Beleg: tx.fhir.org, LOINC 2.82: aktiv; Klasse DOC.MISC – Bewertung: ersetzen (passt nicht zum MII-Required-Binding)<br>LOINC 79086-5 *CT Chest for screening WO contrast* – Beleg: tx.fhir.org: aktiv, CLASS RAD, SCALE Doc (Gegenprüfung); Zugehörigkeit zum MII-ValueSet per Terminologieserver prüfen – Bewertung: vorgeschlagener DiagnosticReport.code<br>SNOMED CT 4261000179100 *Computed tomography imaging report (record artifact)* – Beleg: Ontoserver INT 20260601, tx.fhir.org: aktiv, INT-Modul; $subsumes unter 371525003 – Bewertung: behalten<br>KDL DG020103 *CT-Befund* – Beleg: KDL 2026.0.0 (Bestand) – Bewertung: Dokumentklasse |
| Bezug zum Bestand | overlaps_existing: diagnosticReportDocument. Vorgeschlagene Relationen: specializes diagnosticReportDocument (mihub.lung.primarycare.diagnosticReportDocument.v0.1); hasPart lungRadsCategory (mihub.lung.screening.lungRadsCategory.v0.1); hasPart screeningResultCategory (mihub.lung.screening.screeningResultCategory.v0.1); hasPart recommendedManagement (mihub.lung.screening.recommendedManagement.v0.1); hasPart recommendedControlInterval (mihub.lung.screening.recommendedControlInterval.v0.1); hasPart incidentalFinding (mihub.lung.screening.incidentalFinding.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,80) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,65); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Kein normiertes Format; ESTI-Vorlage als Basis. |
| Umsetzung (Synthese) | specializes diagnosticReportDocument; hasPart lungRadsCategory, screeningResultCategory, recommendedManagement, recommendedControlInterval, incidentalFinding. Empfänger und Übermittlung aus der Definition nehmen (gehören zu resultCommunicationToPatient und resultTransmissionConsentReferrer). Für das MII-Mapping LOINC 79086-5 statt 18748-4 als DiagnosticReport.code (Required-Binding des MII-Profils radiologischer-befund verlangt CLASS RAD und SCALE Doc). mandatory_by_law aufteilen: Übermittlung als strukturierter Befundbericht = Soll-Vorschrift; Inhaltsbestandteile = Empfehlungen. Die „verständliche Erläuterung“ auf die Bedeutung von „kontrollbedürftig“ (TrG) eingrenzen oder als lokal kennzeichnen. Zitat bis „… als strukturierter Befundbericht übermittelt werden“ vervollständigen. |
| Status | **behalten** – Spezialisierung von diagnosticReportDocument (primarycare) |

##### 48. `resultCommunicationToPatient` – Übermittlung des Befundberichts (Zeitpunkt, Weg, Empfänger)

| Feld | Inhalt |
|---|---|
| Definition | Zeitpunkt, Weg und Empfänger der Übermittlung des Befundberichts; Nachweis der Soll-Frist von 14 Tagen. |
| Datentyp · Kardinalität · Kategorie | dateTime · 1..* · kontakt-visite (Vorschlag: Reference (FHIR Communication) oder dateTime je Empfänger) |
| BPMN | Activity_12ef5s1 „Rückmeldung übermitteln“; Event_1w13vdp „Rückmeldung der Radiologie eingegangen“; Event_13jgib0 „Rückmeldung der Radiologie eingegangen“ (process_step: G10 Mitteilung \| Activity_12ef5s1 → Event_1w13vdp / Event_13jgib0) |
| Rolle | Erstbefunder |
| Trigger | je Übermittlung des Befundberichts (an die Person; an die Praxis nur mit Einwilligung) |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **keine**. Keine eigene Dokumentationspflicht; Nachweis der Soll-Frist nach KFE-RL § 42 Abs. 2 (14 Tage nach Erstellung der Aufnahme). Die BPMN-Annotation „Ergebnis-mitteilung nach 4-5 Tagen“ ist ein Erwartungswert aus Sicht der Versicherten. |
| Quellen mit Zitat | [Q39] BPMN lung-cancer-screening-pathway, Annotation Lane Radiologie: „Ergebnis-mitteilung nach 4-5 Tagen“ (Konsolidierung)<br>[Q04] G-BA Versicherteninformation, S. 8: „in der Regel innerhalb von 14 Tagen nach der Untersuchung das Ergebnis übermitteln“<br>[Q05] KBV PraxisInfoSpezial (Oktober 2026), Befundmitteilung: „Dies soll innerhalb von 14 Tagen nach Durchführung der Untersuchung erfolgen.“ |
| Codes (Beleg, Bewertung) | SNOMED CT 165355002 *Patient informed - test result* – Beleg: tx.fhir.org INT 20250201, Ontoserver INT 20260601: aktiv – Bewertung: nur Information der Person; Display korrigieren |
| Bezug zum Bestand | overlaps_existing: –. Vorgeschlagene Relationen: dependsOn structuredScreeningReport (mihub.lung.screening.structuredScreeningReport.v0.1); dependsOn resultTransmissionConsentReferrer (mihub.lung.screening.resultTransmissionConsentReferrer.v0.1); dependsOn ldctExamination (mihub.lung.screening.ldctExamination.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,55) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,55); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Nicht Pflicht (prozess: Pflicht); BPMN 4–5 Tage vs. Soll 14 Tage (KFE-RL § 42 Abs. 2). |
| Umsetzung (Synthese) | Fundstelle korrigieren: Die Annotation (TextAnnotation_045vu1u) liegt im Pool der Versicherten am Sequenzfluss Flow_1996xd4 (Überweisung vorlegen → Rückmeldung eingegangen), nicht in einer Lane Radiologie; Bezugsgröße ist die Vorlage der Überweisung, nicht die LDCT. KFE-RL § 42 Abs. 2 als Primärquelle. Datentyp Reference (Communication: sent, recipient, medium, payload → structuredScreeningReport) oder „Zeitpunkt der Übermittlung je Empfänger“ (dateTime 1..*). Display von 165355002 auf „Patient informed - test result“ korrigieren; für die Übermittlung an die Praxis keinen Patienten-Code verwenden. Vom Freigabedatum des Berichts abgrenzen (DiagnosticReport.issued; S3-QI in Empf. 5.13). „Weg“ nur als lokale Angabe. |
| Status | **behalten** – eigenständig (Übermittlungsereignis) |

#### G11 Teilnahmeverlauf

##### 49. `screeningEpisode` – Teilnahme-Episode und Status in der Früherkennung

| Feld | Inhalt |
|---|---|
| Definition | Klammer über alle Runden mit Status (aktiv, Kontrolle, ausgesetzt, beendet, Wiedereintritt) und bei Ende Datum und Grund. |
| Datentyp · Kardinalität · Kategorie | Period · 1..1 · versorgungskontext (Vorschlag: Reference (FHIR EpisodeOfCare) oder Period + Austrittsgrund · 1..* je Person (Wiedereintritt = neue Episode)) |
| BPMN | Gateway_1dj77wn „Behandlung fortsetzen“; Event_1fjvvjs „Screening beendet“; Event_10ae0lt „Untersuchung abgeschlossen“ (process_step: G11 Verlauf \| pfadübergreifend bis Gateway_1dj77wn → Screening beendet (Event_1fjvvjs)) |
| Rolle | Praxis bzw. Programm (systemseitig geführt) |
| Trigger | Beginn mit der ersten Anspruchsprüfung; Statuswechsel je Runde; Ende beim Austritt |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **keine**. S3 Tab. 16 Schritte 6 und 8 (Hintergrund ohne Empfehlungsgrad). Austrittsgründe sind normativ ableitbar: KFE-RL § 38 Abs. 1 (Altersgrenze) und Abs. 3 (Behandlung, Verdacht); LuKrFrühErkV § 2 Abs. 1 Nr. 3; S3 Empf. 5.5/5.6. |
| Quellen mit Zitat | [Q12] S3-LL Lungenkarzinom, Tab. 16 Schritt 6: „Strukturierte Fortführung, Verlassen bzw. Beendigung des Früherkennungsprozesses“ (Konsolidierung)<br>[Q12] S3-LL Lungenkarzinom 5.1, Tab. 16, Schritt 8: „Wiedereintritt in den Früherkennungsprozess“ |
| Codes (Beleg, Bewertung) | SNOMED CT 275981009 *Lung neoplasm screening (procedure); Synonym „Lung cancer screening“* – Beleg: tx.fhir.org INT 20250201, Ontoserver INT 20260601: aktiv – Bewertung: EpisodeOfCare.type |
| Bezug zum Bestand | overlaps_existing: screeningProgramEnrolment. Vorgeschlagene Relationen: – |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,60) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,60); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | FHIR EpisodeOfCare; Austrittsgründe lokal. |
| Umsetzung (Synthese) | Reference auf FHIR EpisodeOfCare (type 275981009, status, statusHistory, period) oder Period plus CodeableConcept für den Austrittsgrund. Status auf aktiv \| ausgesetzt \| beendet begrenzen (lokal); „Kontrolle“ streichen (ableitbar aus screeningResultCategory und recommendedControlInterval). Austrittsgründe lokal: Altersgrenze (Vollendung des 76. Lebensjahres), Lungenkrebsdiagnose, Symptome bzw. kurative Versorgung (§ 38 Abs. 3 KFE-RL), Ablehnung, Eignungsprofil, Rauchstopp vor 10 oder mehr Jahren. Wiedereintritt als neue Episode (statt des verworfenen screeningEntryRoute). Bezug zu screeningProgramEnrolment (Beginn beim Übergang aus der Nachsorge; Spannung zu § 38 Abs. 3). „ausgesetzt“ sowie Enddatum und Grund als lokale MiHUB-Festlegung kennzeichnen. |
| Status | **behalten** – eigenständig (EpisodeOfCare) |

##### 50. `participantExperienceFeedback` – Rückmeldung der Teilnehmenden (PREM, Belastung)

| Feld | Inhalt |
|---|---|
| Definition | Optionale Rückmeldung nach der Mitteilung zu Information, Termin, Untersuchung, Wartezeit, Angst und Verständnis; ggf. EQ-5D-5L. |
| Datentyp · Kardinalität · Kategorie | Reference · 0..* · prom (Vorschlag: Reference (QuestionnaireResponse) · 0..*) |
| BPMN | Activity_0io1wvp „Rückmeldung besprechen und Entscheidung treffen“ (process_step: G11 Verlauf \| Versicherte: nach Activity_0io1wvp; Portal) |
| Rolle | Versicherte (Portal) |
| Trigger | optional nach der Mitteilung des Ergebnisses |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **keine**. Internationale Empfehlung (NHS England Standard protocol v3, 8.7.1); kein deutscher Normbezug, allenfalls mittelbar KFE-RL § 37 Abs. 1 (Minimierung der Belastungen). |
| Quellen mit Zitat | [Q26] NHS England Standard protocol, 8.7.1: „consideration should be given to offering participants a basic questionnaire about their experience including:“ (Konsolidierung)<br>[Q02] KFE-RL, § 37 Abs. 1: „Dabei ist eine Minimierung der Belastungen, die mit einer Früherkennungsuntersuchung auf Lungenkrebs verbunden sein können, zu gewährleisten.“ |
| Codes (Beleg, Bewertung) | keine Codes beansprucht; lokale Werteliste bzw. no-standard-found |
| Bezug zum Bestand | overlaps_existing: qualityOfLifeScore; distressThermometerScore. Vorgeschlagene Relationen: – |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,65) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,50); vollständige Urteile in candidates.json |
| Umsetzung (Synthese) | Auf eine reine PREM mit der Itemliste aus NHS 8.7.1 begrenzen (lung health check, booking, consent process, scanning, information, understanding, willingness to continue, smoking cessation advice). Angst/Belastung und EQ-5D-5L herausnehmen und bei Bedarf über bestehende Instrumente abbilden (distressThermometerScore bzw. ein HRQoL-Element); „Belastung“ aus dem Label nehmen. Lokaler Fragebogen (no-standard-found bzw. pending-mapping). Fassung (v3 vom 03.02.2025, PR1646) und URL angeben; als UK-Vorbild kennzeichnen. |
| Status | **behalten** – eigenständig, optional (projektspezifisch) |

#### G12 Abklärung

##### 51. `screeningCaseConference` – Interdisziplinäre Fallkonferenz zum abklärungsbedürftigen Befund

| Feld | Inhalt |
|---|---|
| Definition | Datum und Ergebnis der thorax-onkologischen Fallkonferenz zum abklärungsbedürftigen Befund (Bildgebung, Diagnosesicherung, Kontrolle). |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 0..1 · versorgungsplanung (Vorschlag: dateTime (Konferenzdatum) + Ergebnis · 0..*) |
| BPMN | Activity_0es6xoa „Klinische Abklärung anzeigen und Überweisung ausstellen“; Event_0nesy5q „Überweisung zur weiteren Behandlung wird nachgegangen“ (process_step: G12 Abklärung \| nach Activity_0es6xoa, spezialisierte Einrichtung (nicht modelliert)) |
| Rolle | spezialisierte Einrichtung (thorax-onkologisches Tumorboard) |
| Trigger | abklärungsbedürftiger Befund |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. S3 Empf. 5.9 (soll: initiale Fallvorstellung), 5.12 (sollte: Entscheidung über Diagnostik), 5.13 (QI „wünschenswert“); Tab. 15 (mindestens wöchentliche Fallkonferenz). |
| Quellen mit Zitat | [Q12] S3-LL Lungenkarzinom, Empf. 5.13 (EK): „Zeitintervall von Datum der Niedrigdosis-CT bis Datum der interdisziplinären Fallkonferenz aller Teilnehmer mit …“ (Konsolidierung)<br>[Q12] S3-LL Lungenkarzinom 5.1, Empf. 5.12 (EK): „in einem Thorax-Onkologischen Tumorboard einer auf die Untersuchung und Behandlung von Lungenkrebs spezialisierten Einrichtung entschieden werden“<br>[Q12] S3-LL Lungenkarzinom 5.1, Empf. 5.9 (EK): „mit initialer Fallvorstellung in einer interdisziplinären Fallkonferenz“ |
| Codes (Beleg, Bewertung) | SNOMED CT 1268903003 *Consultation by multidisciplinary team* – Beleg: tx.fhir.org: aktiv (Gegenprüfung) – Bewertung: vorgeschlagen (wie Bestand)<br>LOINC 85231-9 *Tumor board Note* – Beleg: tx.fhir.org, LOINC 2.82: aktiv (Gegenprüfung) – Bewertung: vorgeschlagen<br>KDL SD150103 *Tumorboard (Bestand tumorBoardDecision)* – Beleg: Bestand (Gegenprüfung) – Bewertung: vorgeschlagen |
| Bezug zum Bestand | overlaps_existing: tumorBoardDecision. Vorgeschlagene Relationen: specializes tumorBoardDecision (mihub.lung.primarycare.tumorBoardDecision.v0.1); dependsOn clarificationReferral (mihub.lung.screening.clarificationReferral.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,75) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,55); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | Rückkanal an Screening-Einheit fehlt im BPMN. |
| Umsetzung (Synthese) | specializes tumorBoardDecision; dependsOn clarificationReferral. Konferenzdatum als QI-Rückmeldung (S3 Empf. 5.13) und Ergebnis getrennt modellieren; Ergebnis per Verweis auf tumorBoardDecision oder als Werteliste nach Empf. 5.12: weitere Bildgebung (z. B. FDG-PET/CT) \| Diagnosesicherung (Bronchoskopie mit transbronchialer Biopsie, CT-gesteuerte Biopsie, minimal-invasive Resektion) \| Kontrolle. Codes aus dem Bestand übernehmen (SNOMED 1268903003, LOINC 85231-9, KDL SD150103). Verbindlichkeit angeben (5.13 „wünschenswert“, 5.12 „sollte“, 5.9 „soll“). Der Rückkanal an die Screening-Einheit fehlt im BPMN. |
| Status | **behalten** – Spezialisierung von tumorBoardDecision (primarycare); Grenzfall des Scopes |

##### 52. `invasiveWorkupProcedure` – Folge- und Abklärungsmaßnahme nach Screeningbefund (inkl. Komplikation)

| Feld | Inhalt |
|---|---|
| Definition | Maßnahme nach Screeningbefund (CT, PET/CT, Bronchoskopie, Biopsie, Resektion) mit Datum, Dignität und Komplikationen. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 0..* · prozedur (Vorschlag: Reference (FHIR Procedure) oder CodeableConcept nur für die Art · 0..*) |
| BPMN | Event_0nesy5q „Überweisung zur weiteren Behandlung wird nachgegangen“ (process_step: G12 Abklärung \| spezialisierte Einrichtung nach Event_0nesy5q) |
| Rolle | spezialisierte Einrichtung |
| Trigger | je invasiver Abklärungsmaßnahme nach abklärungsbedürftigem Befund |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **Leitlinie**. S3 Empf. 5.13 („wünschenswert“: Anteil maligner Befunde an bioptierten bzw. resezierten Patienten); Verfahren nach Empf. 5.12 und TrG S. 21. Keine Quelle verlangt die Erfassung von Komplikationen. |
| Quellen mit Zitat | [Q12] S3-LL Lungenkarzinom, Empf. 5.13 (EK): „Anteil der Patienten mit einem malignen Befund an allen endoskopisch oder CT-gesteuert bioptierten Patienten“ (Konsolidierung)<br>[Q12] S3-LL Lungenkarzinom 5.1, Empf. 5.12 (EK): „Bronchoskopie mit transbronchialer Biopsie, CT-gesteuerte transthorakale Biopsie oder minimal-invasive chirurgische Resektion“<br>[Q04] G-BA Versicherteninformation, S. 9: „Bei einer Biopsie sind verschiedene Komplikationen wie Nachblutungen oder Fieber möglich.“ |
| Codes (Beleg, Bewertung) | SNOMED CT 78603008 *Biopsy of lung (procedure)* – Beleg: tx.fhir.org INT 20250201, Ontoserver INT 20260601: aktiv – Bewertung: Oberbegriff<br>SNOMED CT 243685008 *Bronchoscopy with transbronchial lung biopsy* – Beleg: tx.fhir.org: aktiv (Gegenprüfung) – Bewertung: vorgeschlagen<br>SNOMED CT 429932001 *CT guided biopsy of lung* – Beleg: Ontoserver INT 20260601, tx.fhir.org: aktiv (Gegenprüfung) – Bewertung: vorgeschlagen<br>SNOMED CT 444188003 *Thoracoscopic wedge resection of lung* – Beleg: tx.fhir.org: aktiv (Gegenprüfung) – Bewertung: vorgeschlagen |
| Bezug zum Bestand | overlaps_existing: postTherapyComplication; treatmentSideEffectOrComplication. Vorgeschlagene Relationen: dependsOn screeningCaseConference (mihub.lung.screening.screeningCaseConference.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,70) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,55); vollständige Urteile in candidates.json |
| Umsetzung (Synthese) | Dignität entfernen (gehört zu workupOutcome). Werteliste auf die invasiven Verfahren nach S3 Empf. 5.12/5.13 begrenzen (243685008, 429932001, 444188003; Oberbegriff 78603008); nicht-invasive Bildgebung (CT, PET/CT) hier nicht aufnehmen. Datentyp Reference (Procedure: code, performedDateTime, complication) oder CodeableConcept nur für die Eingriffsart. Komplikationen als Procedure.complication (Schadensindikator des Screenings), nicht über postTherapyComplication; als lokal und optional kennzeichnen (die Versicherteninformation S. 9 informiert nur). dependsOn screeningCaseConference. |
| Status | **behalten** – eigenständig; Grenzfall des Scopes |

##### 53. `workupOutcome` – Ergebnis der Abklärung eines abklärungsbedürftigen Befunds

| Feld | Inhalt |
|---|---|
| Definition | Endgültiges Abklärungsergebnis mit Datum: Karzinom gesichert, benigne (mit/ohne invasive Abklärung), anderes Malignom, unklar, nicht erfolgt. |
| Datentyp · Kardinalität · Kategorie | CodeableConcept · 0..1 · diagnose (Vorschlag: 0..1 je abklärungsbedürftigem Befund) |
| BPMN | Activity_14vmlwn „Qualitätsdaten erheben und dokumentieren (§7)“ (process_step: G12 Abklärung \| Rückmeldung an Qualitätsdaten (§7) (Activity_14vmlwn)) |
| Rolle | spezialisierte Einrichtung (Rückmeldung an die Screening-Einheit) |
| Trigger | Abschluss der Abklärung eines abklärungsbedürftigen Befunds |
| Pflicht nach Norm | Konsolidierung: nein → nach Gegenprüfung: **keine**. Ratsempfehlung 2022/C 473/01 Nr. 12 (unverbindlich); S3 Empf. 5.13 („wünschenswert“) und Kap. 5.1.5.3. § 7 Abs. 2 LuKrFrühErkV und § 44 KFE-RL verlangen nur Zählungen, kein Abklärungsergebnis; das Monitoring nach § 46 Abs. 2 KFE-RL folgt erst bis Ende 2028. |
| Quellen mit Zitat | [Q27] Council Recommendation 2022/C 473/01, Empfehlung 12: „to aim to collect, manage and evaluate data on all screening tests, assessments and final diagnoses“ (Konsolidierung)<br>[Q12] S3-LL Lungenkarzinom 5.1, Kap. 5.1.5.3: „Zeit bis zur abschließenden Beurteilung/Operation“ |
| Codes (Beleg, Bewertung) | SNOMED CT 363358000 *Malignant neoplasm of lung* – Beleg: tx.fhir.org INT 20250201, Ontoserver INT 20260601, MII TermServ SNOMED CT INT 20260701: aktiv – Bewertung: Wert „Lungenkarzinom gesichert“ (umfasst auch Lungenmetastasen 94391008)<br>SNOMED CT 448993007 *Carcinoma of lung* – Beleg: tx.fhir.org: aktiv, Kind von 363358000 (Gegenprüfung) – Bewertung: präzisere Alternative (vorgeschlagen)<br>SNOMED CT 363346000 *Malignant neoplastic disease* – Beleg: MII TermServ SNOMED CT INT 20260701: aktiv (Gegenprüfung) – Bewertung: Wert „anderes Malignom“ (vorgeschlagen)<br>SNOMED CT 442754001 *Inconclusive evaluation finding* – Beleg: MII TermServ SNOMED CT INT 20260701: aktiv (Gegenprüfung) – Bewertung: Wert „unklar“ (vorgeschlagen) |
| Bezug zum Bestand | overlaps_existing: cancerDiagnosis; tnmStage; tumorHistology. Vorgeschlagene Relationen: dependsOn cancerDiagnosis (mihub.lung.primarycare.cancerDiagnosis.v0.1); dependsOn tumorHistology (mihub.lung.primarycare.tumorHistology.v0.1); dependsOn tnmStage (mihub.lung.primarycare.tnmStage.v0.1); dependsOn invasiveWorkupProcedure (mihub.lung.screening.invasiveWorkupProcedure.v0.1) |
| Gegenprüfung | Quelle: nicht widerlegt (Konfidenz 0,75) · Dublette/Scope/Modell: nicht widerlegt (Konfidenz 0,70); vollständige Urteile in candidates.json |
| Hinweis der Konsolidierung | PPV-Definition festlegen. |
| Umsetzung (Synthese) | Prozessanker ändern in „G12 Abklärung – Rückmeldung der spezialisierten Einrichtung (BPMN-Lücke)“ und den Bezug auf § 7 entfernen; Datenfluss, Rechtsgrundlage bzw. Einwilligung als Issue (DPIA). Werte: Lungenkarzinom gesichert (363358000 oder präziser 448993007) \| anderes Malignom (363346000) \| benigne (lokal) \| unklar (442754001) \| nicht erfolgt (lokal); „mit/ohne invasive Abklärung“ über invasiveWorkupProcedure. Auslöser screeningResultCategory = abklärungsbedürftig; Datum über effective[x]. dependsOn cancerDiagnosis, tumorHistology und tnmStage statt Stadium und Histologie zu wiederholen. PPV1/PPV2 nach S3 Kap. 5.1.5.3 in instruction_de definieren. Deutsche Quelle ergänzen (S3 Empf. 5.13, Kap. 5.1.5.3); „unklar“ und „nicht erfolgt“ als Modellierungsentscheidung kennzeichnen. |
| Status | **behalten** – eigenständig; Grenzfall des Scopes (Rückkanal) |

## 5 Verworfene und zusammengeführte Kandidaten

### 5.1 Verworfen in der Gegenprüfung

Verworfen wurde ein Kandidat, sobald mindestens einer der beiden Skeptiker ihn widerlegt hat. Das traf 24 von 77 Kandidaten: 21 widerlegte nur der Dubletten-/Scope-Skeptiker, 1 nur der Quellen-Skeptiker, 2 beide. Je Gruppe: G1 1 von 2, G2 2 von 9, G3 2 von 7, G4 3 von 3, G5 2 von 7, G6 1 von 3, G7 4 von 9, G8 3 von 7, G9 1 von 13, G11 1 von 3, G12 1 von 4, G13 3 von 3. Die Gruppen G4 (optionale Risikoabschätzung) und G13 (QS, Struktur, Abrechnung) entfallen damit vollständig.

| Nr. (Konsol.) | name | label_de | Gruppe | Urteil Quelle | Urteil Dublette/Scope | Grund (verdichtet) | Verbleib |
|---|---|---|---|---|---|---|---|
| 0 | `screeningEntryRoute` | Zugangsweg zur Lungenkrebs-Früherkennung | G1 | **widerlegt** (0,60) | nicht widerlegt (0,75) | Die zitierte Versicherteninformation (S. 6) beschreibt nur einen Zugangsweg (Eigeninitiative, dann Praxis) und fordert keine Dokumentation. „Übergang aus Nachsorge“ stammt aus S3 Empf. 16.7 und kollidiert mit KFE-RL § 38 Abs. 3; die Werteliste mischt Auslöser und Rundentyp, das Datum passt nicht in ein CodeableConcept 1..1. | Start-Ereignisse des BPMN; Anlass über screeningInvitation, Beginn und Wiedereintritt über screeningEpisode; Übergang aus der Nachsorge über screeningProgramEnrolment (Bestand). |
| 6 | `smokingCessationDate` | Datum des Rauchstopps (Jahre seit Rauchstopp) | G2 | nicht widerlegt (0,70) | **widerlegt** (0,60) | Ableitbar: Ende des jüngsten Konsumabschnitts bzw. Beginn der laufenden Unterbrechung (openEHR at0014: „identical to the 'Episode end date'“). Rechtlich kein eigenes Kriterium, sondern Anwendung der Unterbrechungsregel (TrG Abschn. 2.1, Fn. 7). Die KBV-Quelle ist Sekundärquelle; die Arbeitsnotiz (Abschn. 7.1) irrt, die TrG nennen das Kriterium. | Abgeleiteter Wert aus cigaretteConsumptionPeriod und smokingInterruptionPeriod; LOINC 74010-0 als Mapping. |
| 10 | `packYearsSelfEstimate` | Packungsjahre – Selbstschätzung der versicherten Person | G2 | nicht widerlegt (0,60) | **widerlegt** (0,75) | Gleiches Konzept wie packYearsCalculated (gemeinsamer LOINC 8664-5); verschieden sind nur Urheber und Rechenweg, also Metadaten einer Instanz. Die zitierte Whitepaper-Quelle (Kap. 10) ist ein ärztlicher Rechner; die Selbstschätzung belegt KFE-RL Anlage I („Das folgende kleine Formular hilft Ihnen, Ihre Packungsjahre abzuschätzen:“). | packYearsCalculated als generisches Element „Packungsjahre“ mit Methode (jahrweise \| vereinfacht \| Selbstschätzung) und Urheber; Portal-Eingabe über data_flows patient-entered. |
| 11 | `ageAtEligibilityCheck` | Alter bei der Anspruchsprüfung (vollendete Lebensjahre) | G3 | nicht widerlegt (0,85) | **widerlegt** (0,70) | Aus Geburtsdatum (Bestand birthYear, Patient.birthDate; im Screening volles Datum erforderlich) und Bezugsdatum ableitbar; keine Pflicht, den Alterswert zu dokumentieren; KV-Vorlagen führen Geburtsdatum und Ja/Nein. Stichtag laut Quellen-Skeptiker: Indikationsstellung bzw. LDCT-Tag (TrG S. 17), nicht die Prüfung in der Praxis. | birthYear (primarycare) mit vollständigem Datum für die Screening-Phase; Alterskriterium als Constraint in eligibilityCheckResult. |
| 15 | `relevantAnamnesticData` | Relevante anamnestische Daten zum Eignungsprofil | G3 | nicht widerlegt (0,75) | **widerlegt** (0,70) | Inhaltliche Dublette von comorbidity, historyTakingPrimaryCare, ecogPerformanceStatus/functionalStatus und cancerTreatmentHistory; das Freitextfeld „Relevante Anamnese“ ist ein Abschnitt des Berichts. Die zitierte S3 Empf. 5.4 ist Leitlinie; die Rechtspflicht steht in LuKrFrühErkV § 2 Abs. 1 Nr. 3 b und KFE-RL § 39 Nr. 1. | Abschnitt „Relevante Anamnese“ in eligibilityReport mit Verweisen auf die Bestandselemente. |
| 18 | `familyHistoryLungCancer` | Lungenkrebs bei Verwandten ersten Grades | G4 | nicht widerlegt (0,65) | **widerlegt** (0,75) | Scope: weder Zulässigkeitskriterium noch Berichtsinhalt, keine BPMN-Entscheidung; S3 Empf. 3.1 gilt für Erkrankte, Kap. 3.7.17 ist Hintergrund. Einziger Zweck wäre der PLCOm2012-Eingang. Codes sind belegt (SNOMED 429011007, ICD-10-GM 2026 Z80.1). | Anamnese der Diagnostikphase; optionales Risikomodell-Set nur nach Entscheidung E4. |
| 19 | `occupationalCarcinogenExposure` | Berufliche Exposition gegenüber Lungenkarzinogenen | G4 | nicht widerlegt (0,60) | **widerlegt** (0,80) | Scope: kein Kriterium nach LuKrFrühErkV § 2 bzw. KFE-RL § 38; EVA-Lunge ist ein DGUV-Angebot außerhalb der GKV-Episode; die Arbeitsanamnese (S3 Empf. 3.1) gilt für Erkrankte. Ein CodeableConcept trägt Tätigkeit, Beginn und Dauer nicht. | Diagnostikphase; EVA-Lunge als offene Scope-Frage (E11). |
| 20 | `lungCancerRiskModelScore` | Lungenkrebsrisiko nach Risikomodell (z. B. PLCOm2012) | G4 | **widerlegt** (0,80) | **widerlegt** (0,70) | Von beiden Skeptikern widerlegt: S3 Empf. 5.3 richtet sich an Normgeber (Prüfung der Einschlusskriterien), nicht an Einzelpersonen; der Anspruch hängt nur an festen Kriterien; kein BPMN-Schritt; Ethnie ist besondere Datenkategorie (Art. 9 DSGVO). NCIt C178262 bezeichnet das Modell, nicht den Wert (dafür C178263). | Nicht in Inkrement 1; Entscheidung E4 (PLCOm2012 optional). |
| 22 | `informationTopicsCovered` | Vermittelte Pflichtinhalte und Bestätigung im Bericht | G5 | nicht widerlegt (0,80) | **widerlegt** (0,75) | Pflichtinhalte sind gesetzlich festgelegt (LuKrFrühErkV § 2 Abs. 1 Nr. 4 a–d, S. 2) und vollständig in Anlage I enthalten; die Bestätigung der Information ist Berichtsinhalt (KFE-RL § 40 S. 3); das Thema Tabakentwöhnung trägt tobaccoCessationOfferScreening, das Gespräch screeningInformationConsultation. Keine Norm verlangt eine Dokumentation nach Themen. | eligibilityReport (Bestätigung der erfolgten Information), patientInformationLeafletProvided (Textform inkl. Strahlenrisiko). |
| 27 | `nicotineDependenceScore` | Schweregrad der Tabakabhängigkeit (FTND oder HSI) | G5 | nicht widerlegt (0,80) | **widerlegt** (0,60) | Scope: Keine Screening-Norm verlangt einen Abhängigkeitsscore; der FTND ist Erstattungsvoraussetzung der Pharmakotherapie (AM-RL § 14a: Punktwert mindestens 6) und gehört zur Entwöhnungsbehandlung. Funktional eine Instanz von standardizedAssessmentScore; HSI ohne Code; die S3-LL Rauchen und Tabakabhängigkeit ist laut Deckblatt nur bis 31.12.2025 gültig. | standardizedAssessmentScore (Instrument FTND) bzw. Hinweis in tobaccoCessationCounselling. |
| 29 | `reportingPhysicianSelfDeclaration` | Selbsterklärung und Qualifikation der berichterstellenden Ärzt:in | G6 | nicht widerlegt (0,90) | **widerlegt** (0,60) | Bestandteil bzw. Anlage des Berichts (KFE-RL § 43 Abs. 2 S. 3; EBM 01875 bündelt Bericht und Selbsterklärung; KV-Vorlagen als Ankreuzfeld). Approbation, Fachgebiet und Fortbildung sind Strukturdaten der Ärzt:in. Der Normkonflikt § 6 Abs. 3 LuKrFrühErkV vs. BA 854 ist bestätigt. | Anlage bzw. hasPart von eligibilityReport; Qualifikation im Practitioner-Modul. |
| 31 | `firstReaderEligibilityVerification` | Zulässigkeitsprüfung durch den Erstbefunder | G7 | nicht widerlegt (0,90) | **widerlegt** (0,65) | Gleicher Gegenstand und Wertebereich wie eligibilityCheckResult, nur andere Rolle; Rollen werden im Repo über care_process.data_flows abgebildet (usage_type validate). Teilprüfungen liegen in lastQualifyingChestCtDate und priorScreeningImagesAvailability; das BPMN bündelt die Prüfung in Activity_0l9ecr6. EBM 01871 ist kein Konzeptcode. | eligibilityCheckResult (data_flow Erstbefunder, Aktualitätsrückfrage nach TrG) und justifyingIndication. |
| 34 | `ldctAppointment` | Termin für die Niedrigdosis-CT und Terminwahrnehmung | G7 | nicht widerlegt (0,70) | **widerlegt** (0,65) | Spezialisierung des Bestandselements plannedFollowUpAppointment (gleicher Datentyp, gleiche Kardinalität, Appointment.start); der Wahrnehmungsstatus ist ein Attribut (FHIR AppointmentStatus noshow, cancelled, fulfilled). Den Termin vereinbart die Person selbst (Versicherteninformation); die NHS-Quelle betrifft ein organisiertes Einladungsprogramm. | plannedFollowUpAppointment (Bestand) mit Status; Erinnerung über screeningInvitation. |
| 36 | `providerDataExchangeConsent` | Einwilligung/Schweigepflichtentbindung für Datenaustausch zwischen Leistungserbringern | G7 | nicht widerlegt (0,85) | **widerlegt** (0,60) | Nah-Dublette zu resultTransmissionConsentReferrer: gleiche Consent-Kategorie (LOINC 64292-6), gleiche Dokumentklasse (KDL AM050107), gleicher Zeitpunkt und Akteur; nur der Empfänger unterscheidet sich, und Empfänger sind im Bestand Qualifier. Ob für die Zweitbefundung überhaupt eine Einwilligung nötig ist, bleibt offen (§ 5 Abs. 2 LuKrFrühErkV; StrlSchG § 85 Abs. 3 Nr. 3). | resultTransmissionConsentReferrer als gemeinsames Einwilligungselement mit Empfänger-Qualifier. |
| 39 | `incidentalFindingsDisclosurePreference` | Vereinbarung zum Umgang mit Zufallsbefunden | G7 | nicht widerlegt (0,80) | **widerlegt** (0,55) | Keine Norm (LuKrFrühErkV, KFE-RL, Versicherteninformation) und kein BPMN-Schritt; einzige Quelle ist das BfS-Beratungsmodell (BfS-35/21), das die Verordnung nicht übernommen hat. Eine individuelle Präferenz ist als Freitext in patientGoalsAndPreferences abbildbar; ein „informierter Verzicht“ steht im Spannungsfeld zur Befundaufzeichnung (StrlSchG § 85 Abs. 1 S. 2 Nr. 4). | Entscheidungsfrage Zufallsbefunde (E14); ggf. Teil der Aufklärung in ldctInformedConsent. |
| 43 | `ctdiVolExceedanceJustification` | Begründung einer CTDIvol-Überschreitung wegen Körperstatur | G8 | nicht widerlegt (0,75) | **widerlegt** (0,70) | Die Überschreitung ist aus ctdiVol ableitbar; die einzig zulässige Begründung ist gesetzlich festgelegt (Körperstatur, § 1 Abs. 1 Nr. 2); Größe, Gewicht und BMI doppeln bodyMassIndex; LOINC 29463-7 ist „Body weight“, kein Begründungscode; StrlSchG § 85 Abs. 1a gilt nur für diagnostische Referenzwerte. | Attribut „Konformität/Grund“ an ctdiVol. |
| 44 | `doseLengthProduct` | Dosislängenprodukt (DLP) der LDCT | G8 | **widerlegt** (0,70) | **widerlegt** (0,60) | Von beiden Skeptikern widerlegt: Die NHS-Quelle (QA standards v3, 14d) meint die effektive Dosis in mSv, nicht das DLP; keine deutsche Screening-Norm fordert das DLP; die MII-CT-Extension hat keinen DLP-Slice; das DLP ist ableitbar (CTDIvol × Scanlänge). | Im RDSR (DCM 113701) über ldctAcquisitionParameters referenzierbar. |
| 46 | `ldctImageQuality` | Diagnostische Bildqualität und Beurteilbarkeit | G8 | nicht widerlegt (0,70) | **widerlegt** (0,60) | „Nicht beurteilbar“ entspricht Lung-RADS 0 mit Grund (in lungRadsCategory), die Folge steht in recommendedManagement bzw. recommendedControlInterval. LuKrFrühErkV § 7 Abs. 1 Nr. 2 ist eine Anforderung an das QS-System, keine Dokumentationspflicht je Untersuchung (anders als bei der CCTA in der QS-Vereinbarung). DCM 111210 ist ein Ablehnungsgrund der Projektionsradiographie. | lungRadsCategory (Kategorie 0 mit Grund) und recommendedManagement. |
| 56 | `jointAssessment` | Gemeinsame Beurteilung von Erst- und Zweitbefunder | G9 | nicht widerlegt (0,85) | **widerlegt** (0,80) | Echte Dublette von screeningResultCategory: Dokumentationspflichtig ist das Ergebnis der gemeinsamen Beurteilung (KFE-RL § 44), und dieses Ergebnis ist der abschließende Befund (TrG S. 20). Die Form ist frei, das Ergebnis immer übereinstimmend (TrG S. 19); EBM 01881 deckt nur den Dissensfall ab. Ein dateTime 0..1 kann Form und Konsensuskonferenz nicht tragen. | screeningResultCategory (Qualifier Grundlage, Zeitpunkt, Konsensuskonferenz); Akteure in screeningReadingEvent. |
| 68 | `intervalSymptomReport` | Beschwerden zwischen den Untersuchungen (Selbstmeldung) | G11 | nicht widerlegt (0,60) | **widerlegt** (0,70) | Wer Symptome hat, verlässt die Früherkennung (KFE-RL § 38 Abs. 3); die Versicherteninformation verweist nur auf den Arztbesuch. Die vier Warnsymptome sind mit identischen SNOMED-Codes bereits in followUpHistoryFinding modelliert, die Selbstmeldung im Portal in patientReportedSymptomWeb, der Arztkontakt in reasonForEncounter. | Bestandselemente; Folgen über symptomAndLungCancerCareStatus und screeningEpisode (Austrittsgrund). |
| 73 | `lungCancerDetectionMode` | Entdeckungsweg eines Lungenkarzinoms bei (ehemals) Teilnehmenden | G12 | nicht widerlegt (0,70) | **widerlegt** (0,65) | „Im Screening entdeckt“ ist aus workupOutcome und der Runde ableitbar, Intervallkarzinome aus screeningEpisode und cancerDiagnosis; „nach Ausscheiden“ und „außerhalb“ liegen außerhalb der Episode. Ein Registerabgleich ist für die LDCT nicht geregelt (nur Mammographie-Screening; Monitoring nach § 46 Abs. 2 KFE-RL bis Ende 2028). Die Kategorien sind nicht disjunkt. | Auswertung über Register bzw. künftiges Monitoring, nicht Erfassung; SNOMED 444589003 (Intervallkarzinom) für spätere Auswertungen belegt. |
| 74 | `quarterlyQualityReport` | Quartalsbericht und QS-Aufzeichnung der Screening-Einheit | G13 | nicht widerlegt (0,85) | **widerlegt** (0,85) | Aggregat (MeasureReport), kein patientenbezogenes Datenelement: zählt ldctExamination und screeningResultCategory je Erstbefunder und Quartal; integer 1..* ohne Dimension, Zeitraum und Berichtseinheit. Der Normbezug ist korrekt (LuKrFrühErkV § 7 Abs. 2; KFE-RL § 44: Quartalsbericht an die KV als Abrechnungsvoraussetzung). | Kennzahlenkatalog bzw. abgeleitete Auswertung (Entscheidung E18). |
| 75 | `readerQualificationAndApproval` | KV-Genehmigung, Qualifikation und Jahresbefundzahlen der Befunder | G13 | nicht widerlegt (0,85) | **widerlegt** (0,85) | Struktur- und Organisationsdaten (KV-Genehmigung nach KFE-RL § 43 Abs. 3/5, Fallzahlen nach LuKrFrühErkV § 6), die nicht je versicherter Person entstehen; der patientenbezogene Anteil (wer in welcher Rolle befundet) liegt in screeningReadingEvent. | Practitioner- bzw. Organization-Modul außerhalb des Katalogs. |
| 76 | `ebmServiceCode` | Abgerechnete EBM-Gebührenordnungsposition | G13 | nicht widerlegt (0,70) | **widerlegt** (0,80) | Abrechnungssicht auf bereits modellierte Ereignisse (sechs der acht GOPs hängen an Prozess-Kandidaten); keine Dokumentationspflicht (der EBA regelt die Berechnungsfähigkeit); keine belegte FHIR-System-URI für EBM-GOP. Die zitierte Bestimmung 7 belegt den Quartalsbericht, nicht die GOP. | GOP als Abrechnungsbezug in notes bzw. instruction_de der Prozess-Elemente (01871/01872 ldctExamination, 01875 eligibilityReport, 01876 screeningInformationConsultation, 01878 secondReadingRequest, 01879 Zweitbefundung, 01880 abnormalResultDiscussion, 01881 Konsensuskonferenz). |

### 5.2 Zusammenführungen in der Konsolidierung

Die Konsolidierung hat 309 Linsen-Kandidaten auf 77 zusammengeführt (vollständige Zuordnung in den Arbeitsdaten der Recherche). Wesentliche Bündelungen laut Konsolidierungsnotiz: 11 Technikparameter zu `ldctAcquisitionParameters`; 17 Rundherd-Elemente zu 5; Zufallsbefunde zu 3; Einwilligungen nach Zweck getrennt; Struktur- und Organisationsdaten reduziert; PLCOm2012-Eingaben (Bildung, Ethnie, COPD, eigene Krebsanamnese) nur im Risikomodell vermerkt; Stammdaten nur per Verweis. Entfernt wurden unbelegte oder ungültige Codes: RadLex RID50134, LOINC 18783-1, NCIt C671504 (Druckfehler im ACR-Dictionary, richtig C67150), SNOMED 724167008 (inaktiv), 171184001, 89362005 und 139841002 (inaktiv).

### 5.3 Weitere Zusammenführungen, die die Gegenprüfung für behaltene Kandidaten vorschlägt

| Kandidat | Vorschlag | Folge |
|---|---|---|
| eligibilityProfileReviewDueDate | berechnetes Attribut von medicalSuitabilityProfile; Recall-Anlass „Neubewertung“ in screeningInvitation | kein eigenständig erhobenes Element |
| screeningExaminationType | Attribut „Untersuchungsart“ von ldctExamination; Rundennummer aus screeningEpisode | kein eigenständiges Element |
| cigarettesPerDayInPeriod | isPartOf cigaretteConsumptionPeriod (eine Observation je Abschnitt) | Kopf-/Teilelement |
| patientInformationLeafletProvided | hasPart von screeningInformationConsultation | Teilakt des Informationsgesprächs |
| noduleSizeMeasurement, noduleVolumeDoublingTime, noduleMalignancyProbability | isPartOf pulmonaryNoduleFinding; Größe in Volumen und Durchmesser aufteilen | Rundherd als Klammerbefund |
| coronaryArteryCalcification, emphysemaSeverity | specializes incidentalFinding | Routinefelder der Nebenbefunde |
| resultTransmissionConsentReferrer | gemeinsames Einwilligungselement mit Empfänger-Qualifier (nimmt providerDataExchangeConsent auf) | ein Element für Datenweitergaben |
| screeningResultCategory | nimmt jointAssessment auf (Qualifier Grundlage, Zeitpunkt, Konsensuskonferenz) | ein Element für das abschließende Ergebnis |
| packYearsCalculated | nimmt packYearsSelfEstimate auf (Methode, Urheber) | ein Element „Packungsjahre“ |
| eligibilityCheckResult | nimmt firstReaderEligibilityVerification als Datenfluss des Erstbefunders auf | ein Element für die Anspruchsprüfung |
| participationDecision, ldctInformedConsent | Entscheidung vor der LDCT nur in ldctInformedConsent; participationDecision auf die Entscheidung nach der Information begrenzen | keine Doppelerfassung desselben Gateways |
| lastQualifyingChestCtDate | Erweiterung von ctThoraxScan (Thorax-CT-Vorgeschichte mit Anlass und Befundungseignung) statt eigenes Datumselement | phasenübergreifend nutzbar |

Fix-Hinweise, die auf inzwischen verworfene Kandidaten verweisen (etwa EBM-GOP in ebmServiceCode, informationTopicsCovered als hasPart oder dependsOn firstReaderEligibilityVerification), sind in den Umsetzungsempfehlungen von Abschnitt 4 bereits auf die Verbleib-Elemente umgestellt.

## 6 Vorschlag für die Repo-Umsetzung

### 6.1 Ausgangslage im Repository

Das Schema (`schemas/data-element.schema.json`, Commit c4fb886) kennt die Phase `screening` noch nicht: Sie fehlt im Enum `phase` und im ID-Pattern (`mihub.lung.(followup|surveillance|palliative|primarycare)…`). Weitere Lücken für die Screening-Elemente:

- `evidence.guideline_references[].source` ist ein Enum mit elf Werten; Rechtsquellen (LuKrFrühErkV, KFE-RL) gibt es nur als „andere“.
- Ein Feld für die rechtliche Verbindlichkeit fehlt. `mandatory_by_law` der Kandidaten hat keine Entsprechung; nur `care_process.data_flows[].mandatory` existiert je Datenfluss.
- `category` hat 17 Werte, keinen für Einwilligungen.
- `related_elements[].relation` kennt isPartOf, hasPart, specializes, generalizes, dependsOn, supersedes, supersededBy – kein `derivedFrom`, das mehrere Fix-Hinweise verwenden.
- `cardinality` erlaubt nur `^[01*]..[1*]$`; eine Mindestzahl von zwei Befundungsschritten (2..*) ist nicht ausdrückbar.
- `value_set.codings[].system` ist Freitext. `scripts/verify-terminology.py` (SYSTEM_URL) kennt elf Systeme (snomed-ct, loinc, icd-10-gm, ops, atc, kdl, ucum, icd-o-3, icf, meddra, hl7-v3), nicht aber dicom-dcm, ncit, radelement, ebm und openehr-archetype. Die behaltenen Kandidaten tragen 61 Codes; davon stammen 15 aus Systemen, die das Prüfskript nicht kennt.

**Vorarbeit (umgesetzt mit dem PR, der dieses Dossier einführt):** Der Branch `feat/screening-episode-preparation` setzt die Schritte 1 bis 8 aus `docs/howto-add-element.md` § D um: Enum und ID-Pattern im Schema (Minor-Version), Ordner `elements/screening/` mit README, `build-catalog.py`, `_elicitation.py`, Issue-Template, `build-fhir-logical-models.py` (PhasesCS) und CODEOWNERS (`@mihub-ap8/lead-screening`). Ebenfalls umgesetzt: Phasenlisten in README.md, AGENTS.md und docs/methodology.md, die neu erzeugte Excel-Vorlage sowie `docs/screening/` mit diesem Dossier, der vorbefüllten Erhebungsmappe und `quellen.json`.

### 6.2 Vorschläge

**U1 – Phase `screening` aufnehmen.** *(Umgesetzt.)* Schema-Änderungen, Schritt 8, neu erzeugte Excel-Vorlage. Ordner `elements/screening/` (Enum-Wert und Ordnername sind gleich). Dossier (mit Matrix in Abschnitt 3) und vorbefüllte Mappe liegen unter `docs/screening/`. `tumor_entity` ist für asymptomatische Personen nicht sinnvoll; da das Feld optional ist, im Screening weglassen (oder `lung_cancer_any` mit Hinweis).

**U2 – Pflicht-Quelle in die Quellen-Enum.** *(Minimalvariante umgesetzt: `LuKrFrühErkV` und `G-BA KFE-RL`; die erweiterte Variante bleibt Entscheidung E23.)* `evidence.guideline_references[].source` mindestens um `LuKrFrühErkV` und `KFE-RL` erweitern. Als Option zusätzlich: `G-BA (Tragende Gründe, Versicherteninformation)`, `EBM/BMV-Ä`, `StrlSchG/StrlSchV`, `BGB`, `ACR Lung-RADS`, `DRG/DGP/DGT`, `NHS England LCSP`, `BfS`. Für Normen `recommendation_grade: n/a`; `section` in der Zitierweise „§ 2 Abs. 1 Satz 1 Nr. 3 Buchst. a Doppelbuchst. aa“. Variante B (Entscheidung E23): ein eigenes Feld `evidence.legal_references[]` mit Norm, Fassung, Fundstelle und Verbindlichkeit (pflicht | bedingt | mittelbar | soll | keine), damit die Einstufung aus Abschnitt 4 maschinenlesbar wird.

**U3 – Verbindlichkeit abbilden.** Solange es kein Feld gibt: `care_process.data_flows[].mandatory = true` für die verpflichtete Rolle und das System, Normzitat in `evidence`, bedingte und mittelbare Pflichten in `constraints_de`. Die Einstufung *Pflicht nach Norm* (nach Gegenprüfung) aus Abschnitt 4 ist die Vorlage dafür.

**U4 – smokingStatus zu Raucheranamnese-Bausteinen (Q3) erweitern.**

- `smokingStatusScreening` als Phasen-Pendant mit `specializes mihub.lung.followup.smokingStatus.v0.2` anlegen (Präzedenz `ecogPerformanceStatusSurveillance → ecogPerformanceStatus`). Eine Phasenliste statt des Einzelwerts wäre eine Major-Änderung des Schemas (Entscheidung E21) und wird nicht empfohlen.
- Bausteine: `cigaretteConsumptionPeriod` (Kopf, hasPart `cigarettesPerDayInPeriod`), `smokingInterruptionPeriod`, `otherTobaccoNicotineProductUse`; abgeleitet `creditableSmokingDurationYears` und `packYearsCalculated` (mit Methode und Urheber; nimmt die Selbstschätzung auf). Alle mit Schlüsselwort „Q3 Raucheranamnese“ in `iso13972_metadata.keywords`, damit Behandlung und Nachsorge sie später referenzieren können.
- Korrekturen an `smokingStatus` (Bestand): Mapping-Ziel `…/modul-person/StructureDefinition/Raucher` existiert im Paket MII Person 2025.0.1 nicht → auf das Q3-Profil mit Basis ISiKRaucherStatus umstellen; Wertebindung auf LL2201-3 harmonisieren (SNOMED CT als Mapping); E-Zigarette (722499006) und Passivrauch (43381005) aus dem Status in `otherTobaccoNicotineProductUse` bzw. ein Expositionselement verlagern; den Issue „verwandte Produkte“ dort auflösen. Die S3-Referenz steht seit c4fb886 bereits auf 5.1 (die Arbeitsnotiz bezog sich auf Commit 8acb4f6). Mit der Zweitprüfung der Nachsorge-Elemente (PR #15) sind die Version der S3-LL Rauchen und Tabakabhängigkeit (3.1) korrigiert, das Mapping auf ISiKRaucherStatus (`fhir-isik`) sowie das MII-Kardio-Profil `mii-pr-kardio-observation-rauchen` (nur Ballot) umgestellt und Issues zur Achsenmischung (Status, E-Zigarette, Passivrauch) und zur Wertebindung an LL2201-3 ergänzt; offen bleiben die Umstellung der Wertecodes und die Verlagerung der Expositionen.
- Profil: Packungsjahre kennen weder ISiK noch IPS; ein eigenes Q3-Profil (Muster US Core Smoking Status) ist nötig.

**U5 – Spezialisierungen statt Dubletten.** 10 behaltene Kandidaten spezialisieren ein Bestandselement, 2 weitere den neuen Kandidaten `incidentalFinding`:

| Kandidat | specializes | Ziel-ID |
|---|---|---|
| `smokingStatusScreening` | smokingStatus | mihub.lung.followup.smokingStatus.v0.2 |
| `lastQualifyingChestCtDate` | ctThoraxScan | mihub.lung.followup.ctThoraxScan.v0.1 |
| `tobaccoCessationOfferScreening` | tobaccoCessationCounselling | mihub.lung.followup.tobaccoCessationCounselling.v0.1 |
| `ldctReferral` | referralOrder | mihub.lung.primarycare.referralOrder.v0.1 |
| `ldctExamination` | ctThoraxScan | mihub.lung.followup.ctThoraxScan.v0.1 |
| `secondReadingRequest` | referralOrder | mihub.lung.primarycare.referralOrder.v0.1 |
| `recommendedManagement` | recommendationsForPrimaryCare | mihub.lung.primarycare.recommendationsForPrimaryCare.v0.1 |
| `clarificationReferral` | referralOrder | mihub.lung.primarycare.referralOrder.v0.1 |
| `structuredScreeningReport` | diagnosticReportDocument | mihub.lung.primarycare.diagnosticReportDocument.v0.1 |
| `screeningCaseConference` | tumorBoardDecision | mihub.lung.primarycare.tumorBoardDecision.v0.1 |
| `coronaryArteryCalcification` | incidentalFinding | mihub.lung.screening.incidentalFinding.v0.1 |
| `emphysemaSeverity` | incidentalFinding | mihub.lung.screening.incidentalFinding.v0.1 |

**U6 – Kategorien.** Die vorhandene Taxonomie trägt die Kandidaten weitgehend. Vorschlag: neue Kategorie `einwilligung` (Einwilligung, Entscheidung, Widerspruch) für `ldctInformedConsent`, `resultTransmissionConsentReferrer`, `screeningDataUseConsent` und `participationDecision` (bisher prozedur, administrativ bzw. versorgungsplanung). `decisionAidResponse` von prom nach versorgungsplanung umstellen (Gegenprüfung). Eine eigene Kategorie für Qualitätskennzahlen ist nicht nötig, weil `quarterlyQualityReport` verworfen wurde (Entscheidung E22).

**U7 – Codesysteme und Terminologieprüfung.**

- `SYSTEM_URL` in `scripts/verify-terminology.py` um `dicom-dcm` → `http://dicom.nema.org/resources/ontology/DCM` ergänzen (in der Gegenprüfung per tx.fhir.org-Lookup bestätigt).
- `ncit`: kanonische System-URI festlegen und prüfen; tx.fhir.org kennt NCIt C113268 nicht.
- `radelement`: nur als `standard_mappings` bzw. in notes.
- `ebm`: keine belegte FHIR-System-URI für EBM-GOP → keine Codings, nur Abrechnungsbezug in notes bzw. instruction_de.
- `openehr-archetype`: als `standard_mappings` (Wert im Enum vorhanden), nicht als Coding.
- Mindest-Edition dokumentieren: SNOMED 1362105002 (effectiveTime 20250301), 1381861002 (20251201) und 1388653002 (20260301) fehlen in der Edition auf tx.fhir.org (INT 20250201).
- Vor der Aufnahme alle Codes mit `scripts/verify-terminology.py` gegen den MII-TermServ (SNOMED CT 20260701, LOINC 2.83) prüfen; bisher hat dort nur der Dubletten-Skeptiker der Gruppe 10 Codes geprüft.

**U8 – Schemaregeln einhalten.** `derivedFrom` aus den Fix-Hinweisen als `dependsOn` umsetzen oder das Relations-Enum erweitern. „Mindestens zwei Instanzen“ als Constraint statt als Kardinalität. Ereignisse mit Attributen (Kanal, Empfänger, Person) als `Reference` statt `dateTime` modellieren (screeningInvitation, resultCommunicationToPatient, justifyingIndication, screeningInformationConsultation).

**U9 – Bestandskorrekturen (außerhalb Screening; mit PR #15 erledigt).** smokingStatus (U4). In c4fb886 zitierten `smokingStatus` und `tobaccoCessationCounselling` die S3-LL Rauchen und Tabakabhängigkeit als Version „1.0 (03/2021)“; das Dokument nennt Versions-Nr. 3.1 (mit PR #15 korrigiert). Acht Elemente verweisen auf MII-Bildgebung-URLs unter `…/fhir/core/modul-bildgebung/…` (`ctThoraxScan`, `ctThoraxFinding`, `ctAbdomenFollowUp`, `chestXRayFollowUp`, `petCtFollowUp`, `abdominalUltrasoundFollowUp`, `brainMriFinding`, `diagnosticReportDocument`); das Paket 2026.0.0 nutzt `…/fhir/ext/modul-bildgebung/…` (z. B. `mii-pr-bildgebung-bildgebungsstudie` statt `mii-pr-bildgebung-imagingstudy`) — mit PR #15 korrigiert.

**U10 – Reihenfolge.**

1. Entscheidungen aus Abschnitt 7 einholen, mindestens E1–E3, E12, E21–E23.
2. Schema-PR: Phase `screening`, Quellen-Enum, ggf. Kategorie `einwilligung` und Relation.
3. Q3-Bausteine und Korrektur von smokingStatus.
4. M1-Inkrement 1 in Wellen: zuerst die 16 Kandidaten mit Pflicht nach Norm, dann die bedingten und mittelbaren, zuletzt Leitlinien- und optionale Elemente (Befundung, Zufallsbefunde, Portal) nach den Entscheidungen der Radiologie bzw. des Datenschutzes; G12 erst nach der DPIA.
5. Je Welle: `check-duplicates.py`, `validate.py`, `verify-terminology.py`, Katalog neu erzeugen, audit-log.

Aus den Kandidatendaten (Felder der Konsolidierung, Urteile beider Skeptiker, Synthese) wurde die vorbefüllte Erhebungsmappe erzeugt; ausgefüllte Mappen lassen sich mit `scripts/import-elicitation-workbook.py` in YAML-Entwürfe überführen (Round-trip mit allen 53 Zeilen geprüft).

## 7 Entscheidungsbedarf für die Erhebung

Die Fragen sind nach Adressat geordnet. „Fakten“ fasst die Quellenlage zusammen, „Vorschlag“ ist die Empfehlung dieses Dossiers und keine Entscheidung.

### 7.1 Allgemeinmedizin, Innere Medizin, Arbeitsmedizin (berichterstellende Praxis)

**E1 – Konsumabschnitte oder Jahresdurchschnitt?** Erfasst die Praxis den Zigarettenkonsum in Abschnitten (Beginn, Ende, Zigaretten pro Tag) oder genügt ein über die Rauchjahre gemittelter Tageskonsum wie in den KV-Vorlagen?

- Fakten: § 1 Abs. 2 LuKrFrühErkV rechnet jahrweise. Ohne vollständige Unterbrechung von zehn oder mehr Jahren ergibt ein korrekt gemittelter Wert dieselbe Summe. Abschnitte braucht man für Unterbrechungen, für die NELSON-Kriterien (S3 Statement 5.2: ≥ 15 Zigaretten/Tag über ≥ 25 Jahre oder ≥ 10 über ≥ 30 Jahre) und für die Selbstauskunft im Portal.
- Vorschlag: ein Abschnitt als Standard, weitere nur bei vollständiger Unterbrechung oder deutlichem Intensitätswechsel. Zu klären sind außerdem die Präzision (Jahr oder Monat), der Umgang mit Teiljahren und die Regel, nach der NELSON-Kriterien aus wechselnder Intensität abgeleitet werden.

**E2 – Unterbrechung und Rauchstopp.** (a) Gilt laufende Abstinenz als Unterbrechung im Sinne von § 1 Abs. 2 S. 4 (so die Auslegung der TrG, Abschn. 2.1, Fn. 7)? (b) Unterbricht das Rauchen anderer Produkte (Pfeife, Zigarre, E-Zigarette) eine Zigarettenpause oder nicht? (c) Welcher Stichtag gilt für „weniger als zehn Jahre“ – Anspruchsprüfung, Indikationsstellung oder LDCT-Tag? Beteiligt: Klinik, Justiziariat, ggf. KBV.

**E3 – Packungsjahre: Rechenweg und Urheber.** Jahrweise Rechnung nach der Verordnung oder die vereinfachte Formel der KBV, der KV-Vorlagen und des Formulars in Anlage I (Packungen pro Tag × Raucherjahre)? Vorschlag: ein Element „Packungsjahre“ mit Methode und Urheber; die Selbstschätzung im Portal dient der Vorbefüllung, maßgeblich ist die ärztliche Berechnung. Wie wird eine Abweichung den Versicherten erklärt?

**E4 – PLCOm2012 und Risikomodelle optional?** Verworfen wurden lungCancerRiskModelScore, familyHistoryLungCancer und occupationalCarcinogenExposure: Der Anspruch hängt nur an festen Kriterien, und S3 Empf. 5.3 richtet sich an den Normgeber. Optionen: (a) gar nicht; (b) optionales Variablen-Set für die Forschung (HANSE-Schwelle 1,58 %). Datenschutz: Die Ethnie ist eine besondere Kategorie nach Art. 9 DSGVO; für die Bildung fehlt eine validierte Zuordnung deutscher Abschlüsse. Vorschlag: (a) für Inkrement 1; erneut prüfen im S3-Prüfzyklus (mindestens alle drei Jahre).

**E5 – Medizinisches Eignungsprofil.** Reicht die Werteliste geeignet | nicht geeignet | geeignet mit Hinweis auf Überdiagnose? Welche Belege werden referenziert (Komorbiditäten, ECOG, Lebenserwartung)? Wird ein Instrument wie der Charlson-Index genutzt? Wie oft wird geprüft: nach S3 Empf. 5.6 alle fünf bzw. drei Jahre oder nach KBV in jeder Runde? Muss der Bericht je Runde neu erstellt werden (EBM 01875 „einmal im Krankheitsfall“)?

**E6 – Absage dokumentieren?** Ein negatives Prüfergebnis und Absagegründe haben keine Rechtsgrundlage. Sollen sie trotzdem erfasst werden (Teilnahme- und Absagequote, Rückfragen)? Wenn ja: welche Gründe?

**E7 – Symptome und Übergang aus der Nachsorge.** Genügt die Angabe asymptomatisch ja/nein, oder wird eine Symptomliste geführt (z. B. Onkopedia NSCLC Tab. 1)? Ab wann dürfen Personen nach der Lungenkrebs-Nachsorge in die Früherkennung (S3 Empf. 16.7: nach fünf Jahren) angesichts von KFE-RL § 38 Abs. 3 („Nachbehandlung“ → kurative Versorgung)?

**E8 – Information und Entscheidung.** Wird die Teilnahmeentscheidung nach der Information mit Ablehnungsgrund erfasst? Bleibt die Entscheidungshilfe im Portal privat oder darf sie geteilt werden? Erfüllt die Aushändigung der Fassung in Leichter Sprache die Pflicht nach § 40 KFE-RL?

**E9 – Tabakentwöhnung.** Wird das Opt-out-Angebot mit Reaktion (angenommen, abgelehnt, später) erfasst? Werden Fagerström-Test und HSI nur in der Entwöhnungsbehandlung geführt (verworfen: nicotineDependenceScore)?

**E10 – Aufforderung und Recall.** Wer fordert auf bzw. erinnert (Praxis, Radiologie, Portal), über welchen Kanal? Auf welcher Rechtsgrundlage dürfen Praxen Risikopersonen aus dem PVS selektieren und das Portal erinnern? Werden Termin und Nichterscheinen über plannedFollowUpAppointment erfasst?

**E11 – Rollen.** Wie wird die Arbeitsmedizin im GKV-Pfad abgebildet, wenn EBM 01875/01876 nur bestimmte Arztgruppen zulassen? Wie geht die Rollen-Werteliste mit dem Normkonflikt um (§ 6 Abs. 3 LuKrFrühErkV: Innere Medizin, Allgemeinmedizin, Arbeitsmedizin; BA 854 ab 01.10.2026 zusätzlich Praktische Ärzt:innen und Ärzt:innen ohne Gebietsbezeichnung)? Wird EVA-Lunge (DGUV) als paralleler Zugangsweg modelliert?

### 7.2 Radiologie (Erst- und Zweitbefunder)

**E12 – Lung-RADS und §-Kategorien.** Werden beide geführt (V-Lung-RADS je Befundung, Rechtskategorie abschließend)? Wie werden Lung-RADS 0 (keine Rechtskategorie) und 4A (kontroll- oder abklärungsbedürftig je nach PET-Pfad) zugeordnet? Ist eine LDCT nach 1–3 Monaten bei Kategorie 0 eine Kontroll-LDCT nach § 2 Abs. 2 (GOP 01872)? Klärung mit G-BA, KBV oder DRG nötig. Vorschlag: beide führen, Mapping-Tabelle mit expliziten Regeln für 0 und 4A.

**E13 – Rundherde.** Welche Rundherde werden einzeln strukturiert erfasst (alle, alle nicht-benignen oder nur der führende Herd)? Volumen oder Durchmesser als Pflichtwert? Werden die Rohdaten für die VDT (Volumina, Untersuchungsdaten, Software und Version, Methode) gespeichert? Wie bleibt die Rundherd-Kennung über Software- und Einrichtungswechsel stabil? Welches Malignitätsmodell gilt (Brock/PanCan in der Baseline)?

**E14 – Zufallsbefunde.** Welche Nebenbefunde werden strukturiert erfasst (S-Modifikator; Koronarkalk und Emphysem routinemäßig nach DRG/DGP/DGT-Supplement Anm. 15)? Visuelle Graduierung oder Agatston-Score auf der nicht getriggerten LDCT? Mitteilung an die Praxis nur im Rahmen der Einwilligung nach § 42 Abs. 2 S. 2? Wie wird mit dem Recht auf Nichtwissen umgegangen (das BfS-Modell einer Vereinbarung wurde nicht übernommen; verworfen: incidentalFindingsDisclosurePreference)?

**E15 – Dosis und Technik.** CTDIvol je LDCT aus dem RDSR übernehmen? Konformität mit der Anlage zu § 4 als ja/nein mit Abweichungen statt Einzelparametern? DLP und Bildqualität nicht gesondert erfassen (beide verworfen)?

**E16 – Befundungsprozess.** Werden Zeitstempel und CAD-Software-Version je Befundung erfasst (S3 Empf. 5.8: identische Software für Erst- und Zweitbefunder)? Wie wird eine Zweitbefundung bei Bedarf (S3 Empf. 5.8) vom Pflichtfall unterschieden und abgerechnet? Konsensuskonferenz (EBM 01881) als Qualifier am Ergebnis?

**E17 – Ergebnismitteilung.** Ist die BPMN-Annotation „nach 4-5 Tagen“ ein lokaler Erwartungswert oder ein Fehler (Soll: 14 Tage nach Erstellung der Aufnahme)? Wer bespricht abklärungsbedürftige Befunde (Erstbefunder laut EBA-Gründen und KBV, im BPMN die Lane Zweitbefunder)? Rückmeldung an die Praxis nur mit Einwilligung – im BPMN ist sie unbedingt.

### 7.3 Datenschutz, Justiziariat und Qualitätssicherung

**E18 – Registerdaten und § 7.** Werden die Zählungen nach § 7 Abs. 2 LuKrFrühErkV und der Quartalsbericht nach § 44 KFE-RL als abgeleitete Kennzahlen (z. B. FHIR MeasureReport) außerhalb des Katalogs geführt? Zählen Personen oder Untersuchungen (inklusive Kontroll-LDCT)? Ein amtliches Berichtsformular wurde nicht gefunden. Für Intervallkarzinome ist ein Registerabgleich bei der LDCT nicht geregelt (nur beim Mammographie-Screening); das Monitoring nach § 46 Abs. 2 KFE-RL kommt bis Ende 2028. Abwarten oder vorbereiten?

**E19 – Einwilligungen.** Welche Struktur: je Zweck und Empfänger (Praxis, Zweitbefunder, Einrichtungen mit Voraufnahmen; zentrale Speicherung, Registerabgleich, Forschung nach S3 Empf. 5.13), als FHIR Consent, angelehnt an den MII Broad Consent? DPIA-Touchpoints: Entscheidungshilfe im Portal, PREM, Rückkanal aus der Abklärung, Einwilligung in Datennutzung.

**E20 – Rückkanal aus der Abklärung (G12).** Bleiben screeningCaseConference, invasiveWorkupProcedure und workupOutcome im Screening-Katalog oder werden sie aus Diagnostik-Elementen referenziert? Soll das BPMN um einen Rückmeldeschritt der spezialisierten Einrichtung erweitert werden? Rechtsgrundlage bzw. Einwilligung klären.

### 7.4 Modellierung (Maintainer, MI-Team)

**E21 – Phase als Einzelwert.** Spezialisierungen je Phase (Vorschlag, Minor-Änderung) oder Phasenliste (Major-Änderung des Schemas)?

**E22 – Kategorien.** Neue Kategorie `einwilligung`, oder Einwilligungen weiter unter administrativ und prozedur führen?

**E23 – Quellen-Enum.** Minimal (LuKrFrühErkV, KFE-RL) oder erweitert, mit oder ohne eigenes Feld für Rechtsquellen und Verbindlichkeit?

**E24 – Codesysteme.** dicom-dcm und ncit in das Prüfskript aufnehmen; EBM nur als Abrechnungsbezug ohne Codings; V-Lung-RADS, Rechtskategorien und Absagegründe als lokale CodeSystems (oder Konzeptanträge an SNOMED International bzw. RadElement)?

## 8 Offene Punkte und UNSICHER

### 8.1 Quellen mit eingeschränkter Prüfung (UNSICHER oder Teile nicht gelesen)

- [Q13] S3-Leitlinie Rauchen und Tabakabhängigkeit: Screening, Diagnostik und Behandlung: Kap. 3.2, 3.3, 4.1 gelesen (prozess); Überarbeitungsstand nicht verifiziert
- [Q16] DRG/DGP/DGT-Positionspapier nationales LDCT-Programm mit Supplement; DGP-Positionspapier Tabakentwöhnung (Rupp et al.): Supplement im Volltext (befundung); Hauptartikel und Rupp nur Abstract = UNSICHER (leitlinien)
- [Q19] Europäische Statements: ESR/ERS White Paper 2015, ESR/ERS Statement 2020, European position statement 2017, ERS Technical Standard 2023: 2015 Volltext (befundung); 2017, 2020, 2023 nur Abstract = UNSICHER (evidenz, befundung)
- [Q23] Randomisierte Studien: NLST (2011), NELSON (de Koning 2020; Zhao 2011; van Iersel 2007), LUSI (2020): NLST und Zhao Volltext (evidenz, befundung); de Koning, van Iersel, LUSI nur Abstract = UNSICHER
- [Q24] HANSE: Studiendesign (RöFo 2022), Ergebnisse (Lancet Oncol 2025), Registereintrag NCT04913155: Design Volltext (befundung, evidenz); Lancet nur Abstract = UNSICHER; Register-JSON gelesen
- [Q26] NHS England Lung Cancer Screening Programme: Standard protocol v3, QA standards v3, LCSDS user guidance, NHS Data Dictionary: Protokoll/QA Volltext, per Prüfsumme bestätigt (evidenz, prozess); LCSDS nur via Spiegel = Stand UNSICHER
- [Q27] EU-Ebene: Council Recommendation 2022/C 473/01; EC-LuC; EUCanScreen; SOLACE: Council Rec. Volltext (evidenz); EC-LuC/EUCanScreen Seiten gelesen; SOLACE-Leitlinie nur Sekundärquelle = UNSICHER
- [Q28] IARC Handbooks Vol. 21, Press Release Nr. 385: Pressemitteilung gelesen (evidenz); Handbook/NEJM-Report nicht gelesen
- [Q29] Weitere Programme: Litauen-Pilot (Danila 2025), 4-IN-THE-LUNG-RUN (Hubert 2026; Walstra 2026), Cabrera 2026, Positionspapier Österreich (Wass 2026): Litauen, Hubert, Wass Volltext (evidenz); Walstra, Cabrera nur Abstract = UNSICHER
- [Q36] oBDS 3.0.4_RKI und KBV-MIO-Katalog: Schema bzw. Katalog durchsucht (standards); vollständiges oBDS-XSD nicht geprüft = UNSICHER
- [X06] G-BA-Beschluss Mammographie-Screening (Widerspruchsrecht): nur in einer Gegenprüfung erwähnt, URL und Wortlaut nicht dokumentiert = UNSICHER
- [X07] ESMO-Leitlinien zum NSCLC (Zer A et al., Ann Oncol 2025;36(11):1245–1262; Postmus et al. 2017): nicht geprüft: 2025 nur im Abonnement, 2017 nur über Sekundärquellen = UNSICHER; nicht als Kandidatenquelle genutzt
- [X08] Probability of cancer in pulmonary nodules detected on first screening CT (Brock/PanCan; McWilliams A et al.): nur Abstract (Europe PMC) = UNSICHER

Weitere nicht geprüfte Stellen aus den Linsen: der Hauptartikel des DRG/DGP/DGT-Positionspapiers (Vorgaben zu Befundbericht und Mindestdatensatz), der ACR LCS Incidental Findings Quick Reference Guide, das NELSON-Protokoll (Xu et al. 2006), die RadLex-IDs aus dem IHE-AIR-Beispiel, eine RSNA-RadReport-Vorlage „Lung Cancer Screening“ (im API-Listing mit 434 Vorlagen nicht gefunden) und das Muster-Einladungsschreiben der KFE-RL (Anlage IV a; nur das Inhaltsverzeichnis gesehen). Die Zahl von etwa 5,5 Millionen Anspruchsberechtigten stammt aus Sekundärquellen.

### 8.2 Terminologie

- Geprüft wurde über tx.fhir.org (SNOMED CT INT 20250201, LOINC 2.82), CSIRO Ontoserver (INT-Modul in den Editionen 20260601/20260930), die NCI-EVS-API (NCIt 26.09d), DICOM PS3.16 2026d, die RadElement-API und das KDL-Paket 2026.0.0. Gegen den MII-TermServ (SNOMED CT 20260701, LOINC 2.83) hat nur der Dubletten-Skeptiker der Gruppe 10 Codes geprüft (workupOutcome, lungCancerDetectionMode, ebmServiceCode). Vor der Aufnahme: `scripts/verify-terminology.py` für alle Codes.
- Drei SNOMED-Konzepte setzen neuere Editionen voraus: 1362105002 (20250301), 1381861002 (20251201), 1388653002 (20260301). Ob sie in der vom BfArM lizenzierten deutschen Edition verfügbar sind, ist offen.
- Ohne Standardcode: Rechtskategorien (unauffällig, kontrollbedürftig, abklärungsbedürftig), V-Lung-RADS-Werte, VDT (nur NCIt), teilsolide Rundherde, Entscheidungsstand 0–10, Absage- und Austrittsgründe, Rundentyp, Nikotinbeutel, HSI. Lokale CodeSystems oder Konzeptanträge (E24).
- Ob LOINC 79086-5 im ValueSet des MII-Profils „radiologischer Befund“ liegt, ist nur abgeleitet und per Terminologieserver zu prüfen.
- Die MII-Bildgebung bindet Observation.code an „< 404684003 Clinical finding“; das Lung-RADS-Observable 1362105002 ist damit nicht konform. Rückmeldung an die MII-AG Bildgebung oder eigenes Profil?
- Die kanonische System-URI für EBM-GOP ist nicht belegt; die NCIt-URI ist im Prüfskript festzulegen.

### 8.3 Rechtliche Unklarheiten

- Normkonflikt zum Zuweiserkreis: § 6 Abs. 3 LuKrFrühErkV gegen die EBM-Öffnung durch BA 854 (ab 01.10.2026).
- Lung-RADS 0 und 4A ohne eindeutige Rechtskategorie; Abrechenbarkeit einer Kurzintervall-LDCT als 01872.
- Laufende Abstinenz als Unterbrechung (nur G-BA-Auslegung) und Stichtag der Zehn-Jahres-Regel.
- Gültigkeit des Berichts: neuer Bericht je Runde (KBV: Prüfung vor jeder Runde; EBM 01875 „einmal im Krankheitsfall“) oder älterer Bericht mit Aktualitätsrückfrage durch den Erstbefunder (TrG)?
- Fassung in Leichter Sprache und Anlage I KFE-RL.
- Übergang aus der Nachsorge (S3 Empf. 16.7) gegen KFE-RL § 38 Abs. 3.
- Zufallsbefunde, Einwilligungen für Datenweitergaben und Sekundärnutzung, Registerabgleich und Monitoring (bis Ende 2028) sind normativ ungeregelt oder noch nicht geregelt.

### 8.4 Befunde am BPMN-Modell (für die Modellierer:innen)

- Kein Schritt für die Terminvereinbarung in der Radiologie und kein Nichterscheinen-/Absagepfad (ldctAppointment verworfen; plannedFollowUpAppointment nutzen).
- Keine Schritte für Einwilligungen (Übermittlung an die Praxis, Datenaustausch mit Zweitbefunder und Voreinrichtungen, Datennutzung nach S3 Empf. 5.13).
- Gateway_0jgpvd3 „Teilnahme durch Versicherte bestätigt?“: nein-Pfad ohne benanntes Abbruch-Endereignis.
- Rückmeldung an die Praxis (Event_13jgib0) unbedingt modelliert, rechtlich nur bei Einwilligung (KFE-RL § 42 Abs. 2 S. 2).
- Activity_0es6xoa (Besprechung und Überweisung bei abklärungsbedürftigem Befund) liegt in der Lane Zweitbefunder; EBA-Gründe und KBV sehen den Erstbefunder vor.
- Annotation „Ergebnis-mitteilung nach 4-5 Tagen“ (TextAnnotation_045vu1u, Pool Versicherte) weicht von der Soll-Frist ab (14 Tage nach Erstellung der Aufnahme, KFE-RL § 42 Abs. 2); Bezugsgröße unklar.
- Keine erneute Prüfung des Eignungsprofils (S3 Empf. 5.6), kein Opt-out-Ergebnis der Tabakentwöhnung (S3 Empf. 4.5), keine Konsensuskonferenz (EBM 01881), kein Rückkanal aus der Abklärung (G12).
- Die Dokumentation von Activity_0l9ecr6 („Rechtfertigende Indikation stellen …“) ist eine Kopie der Dokumentation von Activity_1fi5rrl („Die Praxis stellt eine Überweisung …“) – eigene Prüfung im Synthese-Schritt.
- S3-Bezug (Kap. 5) im Modell nicht referenziert (Quellenliste des Pfad-Repos, Kriterium SEM-2).

Kleinere Auffälligkeiten: Tippfehler „Versichterte“ im Namen von Activity_0o694d5 und „Eignungsprofi“ in der Annotation zu § 2.

### 8.5 Hinweise zum Workflow und zur Datenlage

- Die Recherche wurde wegen eines Nutzungslimits einmal unterbrochen und fortgesetzt; bereits abgeschlossene Schritte wurden unverändert übernommen.
- Die Konsolidierung hat Zitate gekürzt („…“) und je Kandidat nur die maßgebliche Quelle übernommen. Vollständige Zitate stehen in den Urteilen der Gegenprüfung (Arbeitsdaten der Recherche; auf Anfrage bei der Maintainer:in).
- Mehrere Fix-Hinweise verweisen auf Kandidaten, die verworfen wurden (u. a. ebmServiceCode, jointAssessment, informationTopicsCovered, firstReaderEligibilityVerification, screeningEntryRoute, ldctAppointment, incidentalFindingsDisclosurePreference, relevantAnamnesticData, ageAtEligibilityCheck, smokingCessationDate). Die Umsetzungsempfehlungen in Abschnitt 4 sind darauf abgestimmt; Abschnitt 5 nennt den Verbleib.
- Widersprüche zwischen den Skeptikern wurden im Synthese-Schritt aufgelöst: Die ePA-Aushändigung des Berichts nennen die TrG (zu § 39 Nr. 1 S. 2), nicht der Normtext – eigene Prüfung der lokalen Kopie. Den Zusatz „möglichst vor dem schriftlichen Bericht“ (abnormalResultDiscussion) belegen die TrG (S. 21), nicht KFE-RL, EBA oder KBV.
- Der Bestandskatalog wurde mit dem Stand der Zweitprüfung der Nachsorge-Elemente abgeglichen (Branch feat/guideline-resync-terminology-primarycare, Basis c4fb886, PR #15). Vor der Umsetzung die Dublettenprüfung gegen den dann aktuellen Stand wiederholen.

## Anhang: Methode und Kennzahlen

| Schritt | Ergebnis |
|---|---|
| Recherche (6 Perspektiven) | Recht 45 Kandidaten/15 Quellen · Leitlinien 30 Kandidaten/12 Quellen · Befundung 70 Kandidaten/28 Quellen · Standards 45 Kandidaten/31 Quellen · Evidenz 45 Kandidaten/33 Quellen · Prozess 74 Kandidaten/26 Quellen |
| Konsolidierung | 309 → 77 Kandidaten; 40 Quellen; 38 als Pflicht markiert |
| Gruppen (behalten/gesamt) | G1 Zugang 1/2 · G2 Raucheranamnese 7/9 · G3 Zulässigkeit/Eignung 5/7 · G4 optionale Risikoabschätzung 0/3 · G5 Information/Entscheidung/Entwöhnung 5/7 · G6 Bericht/Überweisung 2/3 · G7 Radiologie vor LDCT 5/9 · G8 LDCT 4/7 · G9 Befundung 12/13 · G10 Ergebnis/Mitteilung 7/7 · G11 Teilnahmeverlauf 2/3 · G12 Abklärung 3/4 · G13 QS/Struktur/Abrechnung 0/3 |
| Gegenprüfung | 10 Gruppen à höchstens 8 Kandidaten, je ein Quellen-Skeptiker (im Zweifel „widerlegt“) und ein Dubletten-/Scope-Skeptiker; behalten nur bei zwei Urteilen „nicht widerlegt“ |
| Ergebnis | 53 behalten, 24 verworfen (21 Dublette/Scope, 1 Quelle, 2 beide) |
| Synthese | Rolle, Trigger, Verbindlichkeit, Umsetzungsform, Code-Bewertung und Relationen je Kandidat; Zitate maschinell gegen die Urteilstexte der Gegenprüfung und die lokale Kopie der Tragenden Gründe geprüft; BPMN-IDs gegen das Modell geprüft |

