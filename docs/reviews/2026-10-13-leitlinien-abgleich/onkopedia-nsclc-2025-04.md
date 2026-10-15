# Onkopedia-Leitlinie „Lungenkarzinom, nicht-kleinzellig (NSCLC)" — Nachsorge-Auswertung gegen den MiHUB-Datenelement-Katalog

> **Momentaufnahme vor der Umsetzung (2026-10-13).** Read-only-Abgleich des Katalogstands `0.1.0-rc.2` (51 Elemente) gegen die Leitlinie; die daraus abgeleiteten Änderungen sind in `docs/audit-log.md` §13 dokumentiert und im zugehörigen Pull Request umgesetzt. Zeilen- und Elementangaben beziehen sich auf den Stand **vor** dem Update. Erstellt KI-gestützt (Claude Code, Fable 5.1) mit Live-Abruf der Quellen; mit **UNSICHER** markierte Punkte sind nicht verifiziert.

Erstellt: 2026-10-13 (read-only Recherche; Quelle live abgerufen und als Rohtext gesichert). Alle Zitate sind wörtlich aus dem Online-Volltext; nicht verifizierbare Punkte sind mit **UNSICHER** markiert.

---

## 1 Quelle + Version/Stand

| Feld | Befund |
| --- | --- |
| Titel / ICD-10 | „Lungenkarzinom, nicht-kleinzellig (NSCLC)" — ICD-10 C34.- |
| URL (Volltext) | https://www.onkopedia.com/de/onkopedia/guidelines/lungenkarzinom-nicht-kleinzellig-nsclc/@@guideline/html/index.html |
| **Stand (online, 2026-10-13)** | **„Stand April 2025"** — „Dies ist die aktuell gültige Version des Dokuments" |
| Vorversion / Archiv | Archivierte Versionen: Januar 2025, November 2022, Juli 2021, Oktober 2019, November 2018, April 2017, März 2017, November 2016, Februar 2016, April 2015, Oktober 2012. „Änderungen gegenüber Vorversion: Überarbeitung der Version von 1/2025 mit diesen inhaltlichen Schwerpunkten: Aktualisierung der Empfehlungen für die kombinierte Immunchemotherapie … / für die gezielte Therapie auf der Basis neuer Zulassungen" — **keine Änderung an Kap. 7/8 (Nachsorge) ausgewiesen.** Leserkommentare vom Juli 2025 und Januar 2026 beziehen sich auf diese Version (Abb. 7 / Tab. 7 Staging) — bestätigt, dass April 2025 weiterhin die gültige Fassung ist. |
| Autorenzeile | „Autoren: Frank Griesinger, Gudrun Absenger, Annalen Bleckmann, Wilfried Eberhardt, Martin Eichhorn, Nikolaj Frost, Martin Früh, Oliver Gautschi, Sylvia Gütz, Wolfgang Hilbe, Hans Hoffmann, Rudolf Maria Huber, Klaus Kraywinkel, Sonja Loges, Christoph Pöttgen, Martin Reck, Niels Reinmuth, Martin Sebastian, Jan Michael Siehl, Cornelius Waller, Jürgen Wolf, Bernhard Wörmann — In Kooperation mit der AIO". Vorherige Autoren: Robert Pirker, Ron Pritzkuleit, Jan Stöhlmacher, Michael Thomas, Dieter Ukena, Martin Wolf. Beteiligte Fachgesellschaften (Kürzel wie auf der Seite): dgho · oegho · sghssh · sgmo · aio · dkr. |
| Relevante Kapitel | **7 Rehabilitation** · **8 Nachsorge und Kontrolluntersuchungen** (8.1 Kurative Therapie · 8.2 Nicht-kurativ intendierte Therapie) · **Tabelle 12 „Strukturierte Nachsorge nach kurativer Therapie"** (Monatsspalten 3 / 6 / 12 / 18 / 24 / 36 / 48 / 60 — **kein Monat 9**). Ergänzend: 6.1.6.2.1.1 (ALK, ZNS-Bildgebung), 6.1.6.2.2.1.2.1 (Erhaltungstherapie-Alternative, 6–8-wöchige Kontrolle), 6.2.2.1 (Strahlenpneumonitis), 6.1.6.2 (Stadium IVB: symptom-/therapieorientierte Diagnostik), 3.1/3.2 (Rauchen, Früherkennung). Es gibt **kein** eigenes Kapitel „Verlaufskontrolle", „Survivorship" oder „Supportive Therapie"; „Psychoonkologie", „Spätfolgen", „Raucherentwöhnung" kommen im Nachsorgekapitel **nicht** vor. |
| In Kap. 8 zitierte Literatur (Zuordnung über die alphabetische Referenzliste) | [28] Denis P et al., JNCI 109:djx029, 2017 (web-mediated follow-up) · [46] Greer JA et al., JAMA 332:1153, 2024 (Telehealth vs. In-Person Early Palliative Care) · [117] S3-Leitlinie Lungenkarzinom 020-007OL, **November 2022** · [121] Schneider BJ et al., ASCO Guideline Summary „Lung Cancer Surveillance After Definitive Curative-Intent Therapy", JCO OP 16:83, 2020 |

**Diskrepanz zum Repository (Handlungsbedarf):** 7 YAMLs (`followUpInterval`, `ctThoraxScan`, `pulmonaryFunctionTest`, `brainMriHighRisk`, `ecogPerformanceStatus`, `patientReportedSymptomWeb`, `systemicTherapyRegimen`) sowie `README.md:236`, `docs/methodology.md:236` und `docs/audit-log.md:398` pinnen „Onkopedia NSCLC, **Stand 03/2026**". Online existiert keine Fassung 03/2026 — weder als gültige noch als archivierte Version. **UNSICHER**, ob je eine Fassung 03/2026 publiziert wurde (keine Spur auf onkopedia.com); korrekt ist nach heutigem Stand **„Stand April 2025"**. Zusätzlich: `docs/audit-log.md:399` behauptet für Tab. 12 NSCLC Monatsspalten „3/6/9/12/18/24/36/48/60" — die Spalte 9 gibt es nur in Onkopedia-SCLC Tab. 9, nicht in NSCLC Tab. 12.

Hinweis: Onkopedia vergibt keine Empfehlungsgrade/Evidenzlevel; Verbindlichkeit ergibt sich nur aus dem Wortlaut (soll / sollte / kann / „sollte man durchaus erwägen"). In Tab. 12 ist „(X)" nicht legendiert — hier als „fakultativ/individuell" interpretiert (**UNSICHER**).

---

## 2 Nachsorgeprogramm (Onkopedia NSCLC, Stand April 2025)

### 2.1 Nach kurativ intendierter Therapie (Kap. 8.1, Tab. 12)

Wortlaut der Ziele: „Ziele der Nachsorge sind die frühzeitige Diagnose eines Rezidivs mit dem Ziel der Verlängerung der Überlebenszeit / Erhöhung der Heilungschance, die Erkennung von Nebenwirkungen der Therapie und Vorsorge. Bei Pat. mit Lungenkarzinom ist der Wert einer intensiven, strukturierten Nachsorge in Bezug auf eine Verlängerung der Überlebenszeit nicht gesichert. Nach kurativer Therapie ist Ziel der Nachsorge auch die frühzeitige Diagnostik eines Zweittumors."

**Tabelle 12 (wörtlich rekonstruiert):**

| Untersuchung | 3 Mo | 6 Mo | 12 Mo | 18 Mo | 24 Mo | 36 Mo | 48 Mo | 60 Mo |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Anamnese, körperliche Untersuchung | X | X | X | X | X | X | X | X |
| CT Thorax | X* | X* | X | X* | X | X | X | X |
| Lungenfunktion | X | X | (X) | (X) | (X) | — | — | — |

„* nach Strahlentherapie"

| Nr. | Untersuchung / Maßnahme | Intervall / Zeitpunkte | Zielpopulation / Setting | Empfehlungswortlaut (Kurzzitat) | Fundstelle |
| --- | --- | --- | --- | --- | --- |
| L-01 | Anamnese | Monate 3, 6, 12, 18, 24, 36, 48, 60 | alle Pat. nach Therapie in kurativer Intention (OP, RT, RCT, multimodal) | „Empfehlungen für eine konventionelle, strukturierte Nachsorge nach Therapie in kurativer Intention sind in Tabelle 12 zusammengefasst." | Kap. 8.1, Tab. 12 |
| L-02 | Körperliche Untersuchung | Monate 3, 6, 12, 18, 24, 36, 48, 60 | wie L-01 | Tab. 12 („X" an allen 8 Zeitpunkten) | Kap. 8.1, Tab. 12 |
| L-03 | CT Thorax — Basisraster | Monate 12, 24, 36, 48, 60 (jährlich) | alle kurativ behandelten Pat. | Tab. 12 („X") | Kap. 8.1, Tab. 12 |
| L-04 | CT Thorax — zusätzliche Zeitpunkte | Monate 3, 6, 18 | **nur nach Strahlentherapie** (Fußnote „* nach Strahlentherapie") | Tab. 12 („X*") | Kap. 8.1, Tab. 12 Fußnote |
| L-05 | Lungenfunktion | Monate 3, 6 (X); Monate 12, 18, 24 „(X)" = fakultativ (**UNSICHER**, nicht legendiert); nach Monat 24 nicht mehr | alle kurativ behandelten Pat. (Zeile ohne Fußnote) | Tab. 12 | Kap. 8.1, Tab. 12 |
| L-06 | Lungenfunktion — Fortführung nach RT/RCT | bis Ende des Pneumonitis-Risikos; Risikofenster lt. Kap. 6.2.2.1 „innerhalb von 6-24 Monaten nach Ende der Bestrahlung" | Pat. nach alleiniger Strahlentherapie oder Radiochemotherapie | „… **soll** die Überprüfung der Lungenfunktion bis zum Ende des Pneumonitis-Risikos fortgeführt werden [121]." / „Zur Diagnostik der Strahlenpneumonitis ist das Thorax CT geeignet, siehe Kapitel 8. Nachsorge. Die funktionelle Einschränkung wird mittels Lungenfunktionstestung einschließlich der Diffusionskapazität erfasst und quantifiziert." | Kap. 8.1 (Text nach Tab. 12); Kap. 6.2.2.1 |
| L-07 | MRT-Schädel | alle 6–9 Monate, **nur in den ersten 3 Jahren nach Lokaltherapie** | Pat. mit „individuell hohem Risiko der Entwicklung einer cerebralen Metastasierung (z. B. großzellige Karzinome, undifferenzierte Adenokarzinome, kleinzellige Karzinome oder Mischtumoren, seltene Lungentumorhistologien)" | „… **sollte man durchaus erwägen**, in realistischen Abständen (6-9 Monaten), allerdings nur in den ersten drei Jahren nach Lokaltherapie, MRT-Schädel Untersuchungen mit in das Nachsorgekonzept einzuplanen." (= Kann-Empfehlung) | Kap. 8.1 (Text nach Tab. 12) |
| L-08 | Verkürztes Nachsorgeintervall | 6–8 Wochen | Pat. mit Rezidiv oder Zweitkarzinom **mit kurativem Potenzial** | „Bei einigen Pat. mit Rezidiv oder einem Zweitkarzinom besteht ein kuratives Potenzial. Bei diesen Pat. **kann** das Nachsorgeintervall auf 6-8 Wochen verkürzt werden [117]." | Kap. 8.1 |
| L-09 | Nachsorgeziele: Rezidiv-Früherkennung, Zweittumor-Diagnostik, Erkennung von Therapie-Nebenwirkungen, Vorsorge | implizit an jedem Nachsorgetermin | alle kurativ behandelten Pat. | s. Zitat oben | Kap. 8.1 |
| L-10 | Rehabilitation — Information/Beratung; Reha-Maßnahme | „frühzeitig" (kein fester Zeitpunkt) | alle Pat. mit Therapiefolgestörungen (nach OP, RT, medikamentöser Therapie, Komorbidität) | „Die Pat. **sollen** über die Möglichkeiten ambulanter und stationärer Rehabilitationsmaßnahmen sowie weiterer Ansprüche, die sich aus dem Sozialrecht ergeben, frühzeitig informiert werden. Hinsichtlich der Rehabilitationsklinik sollen die Wünsche der Pat. berücksichtigt werden (§9 SGB IX). Dennoch **sollte** eine Empfehlung für eine Klinik mit onkologischem Schwerpunkt abgegeben werden …" | Kap. 7 |
| L-11 | Psychosoziale Rehabilitation / psychische Beschwerden | — (unspezifisch) | alle (Kap. 7); Stadium IVB (Kap. 6.1.6.2) | „… gezielte rehabilitative Maßnahmen im somatischen und **psychosozialen** Bereich" (Kap. 7); „Die Therapie beinhaltet die Behandlung körperlicher und **psychischer** Beschwerden. Sie erfolgt interdisziplinär." (6.1.6.2). **Keine** eigene Psychoonkologie-/Distress-Screening-Empfehlung in Kap. 8. | Kap. 7; Kap. 6.1.6.2 |
| L-12 | Therapiefolgestörungen / Spätfolgen | Pneumonitis → Fibrose 6–24 Mo nach RT; sonst kein Zeitfenster | nach OP/RT/Systemtherapie; nach Ganzhirnbestrahlung | „… Therapiefolgestörungen unterschiedlichen Schwergrades" (Kap. 7); „Der akuten Pneumonitis folgt oft der Übergang in eine pulmonale Fibrose mit Sekundärkomplikationen." (6.2.2.1); Ganzhirnbestrahlung „wegen der kognitiven und neurologischen Langzeitnebenwirkungen nicht empfohlen" (6.1.6.1). **Kein** strukturiertes Spätfolgen-/Survivorship-Programm. | Kap. 7; 8.1; 6.2.2.1; 6.1.6.1 |
| L-13 | Raucherentwöhnung | — | **nicht als Nachsorge-Item** | Nur in Kap. 3: „Das Vermeiden von Rauchen ist die entscheidende Präventionsmaßnahme" (3.1); zum LDCT-Screening: „Geplant ist die Kombination mit einem Angebot zur Raucherentwöhnung." (3.2). In Kap. 7/8 **nicht erwähnt**. | Kap. 3.1 / 3.2 (nicht Kap. 8) |

### 2.2 Nicht-kurativ intendierte Therapie / Verlaufskontrolle unter Systemtherapie (Kap. 8.2 + Kap. 6)

| Nr. | Untersuchung / Maßnahme | Intervall | Zielpopulation / Setting | Empfehlungswortlaut (Kurzzitat) | Fundstelle |
| --- | --- | --- | --- | --- | --- |
| L-14 | Kontrollintervall in der palliativen Situation (Modalität nicht spezifiziert) | **6–8 Wochen** statt 3 Monate | nach medikamentöser Erstlinientherapie (Option der frühen Zweitlinie bei Progress); ebenso als Alternative zur Erhaltungstherapie | „Die S3 Leitlinie empfiehlt im Expertenkonsens die Verkürzung der dreimonatigen auf kürzere, 6-8wöchige Intervalle [117]. Daten prospektiver Studien zum optimalen Nachsorge-Intervall bei Einsatz der aktuellen Therapieoptionen liegen bisher nicht vor." (8.2) / „Notwendig ist eine engmaschige Kontrolle, z. B. in Abständen von 6-8 Wochen, um frühzeitig einen Progress zu diagnostizieren." (6.1.6.2.2.1.2.1) | Kap. 8.2; Kap. 6.1.6.2.2.1.2.1 |
| L-15 | Web-basierte wöchentliche Symptom-Selbsteinschätzung (PRO) | wöchentlich | Pat. in fortgeschrittenen Stadien ohne Krankheitsprogress (palliative Situation) | „Vielversprechende, neue Optionen … sind die personalisierte Überwachung der Pat. und des Krankheitsverlaufs mittels Web-basierter Instrumente. … zwischen einer wöchentlichen, Web-basierten Selbsteinschätzung und einer standardisierten 3-bzw. 6-monatlichen CT Kontrolle randomisiert. Pat. im experimentellen Arm hatten ein signifikant längeres, medianes Überleben (HR 0,32; Median 7 Monate) [28]. Aktuelle Daten aus den USA unterstützen diese Ergebnisse." (US-Daten ohne Referenz — **UNSICHER**, welche Studie gemeint ist) | Kap. 8.2 [28] |
| L-16 | Video-Sprechstunde | — | Pat. mit fortgeschrittenem NSCLC | „Die Patientenzufriedenheit von Video-Sprechstunden bei Pat. mit fortgeschrittenem NSCLC war der persönlichen Sprechstunde nicht unterlegen [46]." | Kap. 8.2 [46] |
| L-17 | ZNS-Bildgebung (MRT) bei ALK+ | bei Diagnosestellung; dann „z. B. alle 3-6 Monate"; zusätzlich bei Symptomen | ALK-positive Pat., auch asymptomatisch | „Unabhängig von klinischen Symptomen sollte bei Diagnosestellung eine Bildgebung mittels MRT erfolgen. Eine strukturierte bildgebende Untersuchung, z. B. alle 3-6 Monate, **sollte** auch asymptomatischen Pat. angeboten werden, darüber hinaus bei Auftreten klinischer Symptome." | Kap. 6.1.6.2.1.1 |
| L-18 | Symptom-/therapieorientierte Diagnostik im Stadium IV (Tab. 2: Labor = Blutbild, Elektrolyte, Nieren-/Leberparameter, LDH, Gerinnung; CT Thorax/Oberbauch mit KM oder FDG-PET-CT; MRT als Alternative; Bronchoskopie/Biopsie bei Verdacht) | ad hoc | Stadium IVB | „Die Diagnostik erfolgt symptom- und therapieorientiert, siehe Tabelle 2." | Kap. 6.1.6.2 (→ Tab. 2, Kap. 5.2.1) |
| L-19 | Therapie-spezifische Toxizitätsüberwachung (konditional) | therapiebezogen | Durvalumab-Konsolidierung („ohne Zeichen einer Pneumonitis", 6.1.4.3/6.1.4.4); T-DXd („interstitielle Lungenerkrankung/Pneumonitis und linksventrikuläre Dysfunktion", 6.1.6.2.1.4 / 6.2.3.3.22); Amivantamab (Infusionsreaktionen, Hautreaktionen, venöse Thromboembolien, 6.2.3.3.4); HIV-assoziiert („in regelmäßigen Abständen die Zahl der CD4 positiven Helferzellen sowie der HIV-Viruslast", 6.3.7) | s. Spalte Population | Kap. 6 (siehe Nummern) |

**Nicht in Onkopedia NSCLC enthalten (Nachsorge/Surveillance):** Röntgen-Thorax, Sonografie Abdomen, Bronchoskopie, PET-CT, CT Abdomen/Becken, Laborparameter/Tumormarker als Nachsorge-Untersuchungen; Distress-Screening; strukturiertes Survivorship-/Spätfolgenprogramm; ECOG als Nachsorge-Item (ECOG nur Kap. 5.6 als Allgemeinzustand).

---

## 3 Abdeckungs-Matrix (Repo-Phasen `followup` / `surveillance`)

Legende: COVERED = Element vorhanden und inhaltlich deckungsgleich · PARTIAL = Element vorhanden, aber Intervall/Population/Trigger/Quelle weichen ab · MISSING = kein Element.

| Leitlinien-Item | Status | Repo-Element(e) | Lücke |
| --- | --- | --- | --- |
| L-01 Anamnese (8 Zeitpunkte) | **PARTIAL** | indirekt: `postTherapyComplication`, `ecogPerformanceStatus`, `smokingStatus`, `distressThermometerScore` (alle per-encounter) | Kein Element „Nachsorgevisite" (nur `firstFollowUpVisitDate`, once) und keine strukturierte Nachsorge-Anamnese (Symptome: Husten, Dyspnoe, Hämoptysen, Schmerz, Gewicht, Neurologie). Zeitraster 3/6/12/18/24/36/48/60 nirgends als Ereignis abgebildet. |
| L-02 Körperliche Untersuchung | **MISSING** | — | Kein Element; weder Durchführung noch Befund. |
| L-03 CT Thorax Basisraster (jährlich M12–M60) | **PARTIAL** | `ctThoraxScan` (Q3M-Y1-Y2;Q6M-Y3-Y5), `ctThoraxFinding` | Frequenz ist S3-abgeleitet; Onkopedia-Raster (nur M12/24/36/48/60 für alle) nicht darstellbar; Onkopedia-Zitat „Tab. 12" ohne Hinweis auf die Abweichung; Versionspin falsch (03/2026). |
| L-04 CT Thorax M3/M6/M18 nach RT | **PARTIAL** | `ctThoraxScan` (Trigger-Text „zusätzlich nach Strahlentherapie") | Bedingung nur als Freitext; kein Element für die kurative Therapiemodalität (OP/RT/RCT), von der die Zeitpunkte abhängen. |
| L-05 Lungenfunktion M3/M6 (alle), (X) M12–M24 | **PARTIAL** | `pulmonaryFunctionTest` (Trigger „Nach Strahlentherapie/Radiochemotherapie"; Q3M-Y1), `fev1PercentPredicted`, `dlcoPercentPredicted` | Repo beschränkt auf RT/RCT — Tab. 12 setzt „X" bei Monat 3 und 6 für **alle** kurativ Behandelten (auch nach OP); fakultative Zeitpunkte 12/18/24 fehlen; Versionspin falsch. |
| L-06 Lungenfunktion bis Ende Pneumonitis-Risiko (soll) | **PARTIAL** | `pulmonaryFunctionTest` (Trigger „bis Ende Pneumonitis-Risiko fortführen"), `dlcoPercentPredicted` | Risikofenster „6–24 Monate nach RT-Ende" (6.2.2.1) nicht operationalisiert; Quelle Kap. 6.2.2.1 fehlt. |
| L-07 MRT-Schädel Hochrisiko 6–9 Mo, nur Y1–Y3 | **PARTIAL** | `brainMriHighRisk` (Q6-9M-Y1-Y3 ✓), `brainMriFinding` (COVERED) | Populationsdefinition im Repo molekular (EGFR/ALK/ROS1, Adeno St. III — S3); Onkopedia definiert **histologisch** (großzellig, undifferenziertes Adeno, kleinzellige Anteile/Mischtumor, seltene Histologien). Empfehlungsstärke „sollte man durchaus erwägen" nicht vermerkt; Versionspin falsch. |
| L-08 Intervall 6–8 Wo bei kurativem Rezidiv-/Zweittumorpotenzial | **PARTIAL** | `followUpInterval` (Code `Q6-9M`, Display „alle 6–9 Wochen (palliativ unter Systemtherapie)") | Kein Code für diesen Fall; vorhandener Code inkonsistent (Code sagt Monate, Display Wochen); Wert 6–8 (Onkopedia) vs. 6–9; kein Trigger-Element „kuratives Potenzial" (Tumorboard-Entscheid). |
| L-09 Nachsorgeziele (Rezidiv, Zweittumor, Nebenwirkungen, Vorsorge) | **COVERED** | `recurrenceOrSecondPrimary`, `postTherapyComplication`, `structuredFollowUpPlan` | — (Onkopedia-Referenz Kap. 8.1 könnte ergänzt werden) |
| L-10 Rehabilitation (Information, Sozialrecht, Reha-Maßnahme, onkologischer Schwerpunkt) | **MISSING** | — | Keinerlei Reha-Element in `followup`; Schema nennt „rehabilitation" nur als mögliche künftige Phase. |
| L-11 Psychosoziale Rehabilitation / psychische Beschwerden | **COVERED** | `distressThermometerScore`, `psychoOncologyReferral` (Quellen S3/OCP) | Repo geht über Onkopedia hinaus (Onkopedia unspezifisch); Onkopedia Kap. 7 als Zusatzreferenz möglich. |
| L-12 Therapiefolgestörungen / Spätfolgen | **PARTIAL** | `postTherapyComplication`, `survivorshipCarePlan`, `ctThoraxFinding`, `dlcoPercentPredicted` | Keine spätfolgenspezifischen Codings (Strahlenpneumonitis, Lungenfibrose, neurokognitive Störung nach WBRT); kein Zeitfenster 6–24 Mo; Onkopedia Kap. 7/6.2.2.1 nicht referenziert. |
| L-13 Raucherentwöhnung (bei Onkopedia kein Nachsorge-Item) | **COVERED** | `smokingStatus`, `tobaccoCessationCounselling` (Quelle S3 Empf. 16.3 / S3 Tabakentwöhnung) | Keine Onkopedia-NSCLC-Referenz möglich (dort nur Prävention/Screening) — Quellenlage im Repo korrekt. |
| L-14 Kontrollintervall 6–8 Wo nach Erstlinie / statt Erhaltung | **PARTIAL** | `restagingImagingDate`, `recistResponse` (Q6-9W, „unter Systemtherapie", S3 Empf. 16.9) | Intervall 6–8 (Onkopedia) vs. 6–9 Wo; Trigger deckt die **therapiefreie Beobachtung nach Erstlinientherapie** (Alternative zur Erhaltung) nicht ab; Onkopedia-Referenzen Kap. 8.2 / 6.1.6.2.2.1.2.1 fehlen; Modalität von Onkopedia offen gelassen. |
| L-15 Web-basierte wöchentliche PRO-Selbsteinschätzung | **COVERED** | `patientReportedSymptomWeb` (weekly, Kap. 8.2, Denis 2017) | Nur Versionspin (03/2026 → April 2025) und Population („fortgeschrittene Stadien ohne Krankheitsprogress") ergänzen. |
| L-16 Video-Sprechstunde | **MISSING** | — | Keine Abbildung der Kontaktform (Präsenz/Video/Telefon) einer Verlaufskontrolle. |
| L-17 ALK+: MRT bei Diagnose + alle 3–6 Mo auch asymptomatisch | **PARTIAL** | `brainMriUnderTherapy` (Trigger „Hochrisiko-Genotyp"; Frequenz nur „Q3M (SCLC ED W&W); ad-hoc") | Strukturiertes 3–6-Monats-Raster für ALK+ fehlt; Onkopedia Kap. 6.1.6.2.1.1 nicht referenziert. |
| L-18 Symptom-/therapieorientierte Diagnostik Stadium IV (Tab. 2) | **PARTIAL** | `restagingImagingDate` (CT), `brainMriUnderTherapy`, `molecularRetestingCtdna` | Kein Labor-Element (Blutbild, Elektrolyte, Nieren-/Leberwerte, LDH, Gerinnung) in `surveillance`; symptomgetriggerte Diagnostik nicht als Trigger modelliert. |
| L-19 Therapie-spezifische Toxizitätsüberwachung | **PARTIAL** | `adverseEventCtcae`, `adverseEventCtcaeGrade`, `immuneRelatedAdverseEvent` (generisch) | Kein Pneumonitis-Ausschluss vor Durvalumab-Konsolidierung, kein ILD-Monitoring T-DXd, kein VTE-Item Amivantamab, kein HIV-Monitoring (CD4/Viruslast) — alles Nische/konditional. |

**Bilanz (19 Leitlinien-Items):** COVERED 4 (L-09, L-11, L-13, L-15) · PARTIAL 12 (L-01, L-03–L-08, L-12, L-14, L-17–L-19) · MISSING 3 (L-02, L-10, L-16).

Querschnittslücke: In **allen** Onkopedia-Referenzen des Repos ist die Version falsch gepinnt (03/2026 statt April 2025) — betrifft 7 YAMLs + 3 Doku-Stellen (siehe Abschnitt 1).

---

## 4 Vorgeschlagene neue oder zu ändernde Datenelemente

Formate folgen `schemas/data-element.schema.json` (datatype-Enum, `care_process`, `evidence.guideline_references`). Alle Vorschläge sind Entwürfe zur klinischen Review; keine Repo-Änderung vorgenommen.

### 4.1 Neue Elemente — Phase `followup`

```yaml
# N-1
name: followUpVisit
label_de: Nachsorgevisite (Anamnese und körperliche Untersuchung)
definition_de: Durchgeführter Nachsorgetermin nach kurativ intendierter Therapie, bei dem Anamnese und körperliche Untersuchung erfolgen. Bildet das Zeitraster der strukturierten Nachsorge als Ereignis ab.
datatype: dateTime
cardinality: 0..*
care_process:
  trigger: Routinekontrolle Monat 3/6/12/18/24/36/48/60 nach Abschluss der kurativ intendierten Therapie
  frequency_pattern: M3;M6;M12;M18;M24;M36;M48;M60   # Onkopedia-Raster; alternativ Q3M-Y1-Y2;Q6M-Y3-Y5 (S3)
  responsible_role: Nachsorge-führende Ärzt:in (Onkologe / Pneumologe / Thoraxchirurg)
evidence: {source: "Onkopedia NSCLC", version: "Stand April 2025", section: "Kap. 8.1, Tab. 12 (Zeile 'Anamnese, körperliche Untersuchung')"}
# Mapping-Hinweis: fhir-r4-base Encounter.period.start
```

```yaml
# N-2
name: followUpHistoryFinding
label_de: Nachsorge-Anamnese — Befund
definition_de: Strukturiert erfasste anamnestische Angaben der Nachsorgevisite (z. B. Husten, Dyspnoe, Hämoptysen, Thoraxschmerz, Gewichtsverlust, neurologische Symptome, neue Beschwerden). Dient der Rezidiv-, Zweittumor- und Nebenwirkungserkennung.
datatype: CodeableConcept
cardinality: 0..*
care_process:
  trigger: bei jeder Nachsorgevisite (followUpVisit)
  frequency_pattern: per-encounter
  responsible_role: Onkologe / Pneumologe
evidence: {source: "Onkopedia NSCLC", version: "Stand April 2025", section: "Kap. 8.1, Tab. 12 (Anamnese); Kap. 8.1 Nachsorgeziele"}
```

```yaml
# N-3
name: physicalExaminationFinding
label_de: Körperliche Untersuchung — Befund
definition_de: Befund der körperlichen Untersuchung in der Nachsorgevisite (z. B. Auskultation, Lymphknotenstatus, Narbenverhältnisse, Ödeme, neurologischer Status). Pathologische Befunde triggern weiterführende Diagnostik.
datatype: CodeableConcept
cardinality: 0..*
care_process:
  trigger: bei jeder Nachsorgevisite (followUpVisit)
  frequency_pattern: per-encounter
  responsible_role: Onkologe / Pneumologe
evidence: {source: "Onkopedia NSCLC", version: "Stand April 2025", section: "Kap. 8.1, Tab. 12 (körperliche Untersuchung)"}
```

```yaml
# N-4
name: curativeTreatmentModality
label_de: Kurative Therapiemodalität (Eingangsgröße Nachsorgeplan)
definition_de: Modalität der abgeschlossenen kurativ intendierten Therapie (Operation, alleinige Strahlentherapie, Radiochemotherapie, multimodal inkl. systemischer Therapie). Steuert die modalitätsabhängigen Zeitpunkte von CT Thorax (M3/M6/M18 nur nach Strahlentherapie) und Lungenfunktion.
datatype: CodeableConcept
cardinality: 1..1
care_process:
  trigger: Therapieabschluss / Erstellung des Nachsorgeplans
  frequency_pattern: once-per-treatment-completion
  responsible_role: Lead-Clinician (Onkologe / Pneumologe / Thoraxchirurg / Strahlentherapeut)
evidence: {source: "Onkopedia NSCLC", version: "Stand April 2025", section: "Kap. 8.1, Tab. 12 Fußnote '* nach Strahlentherapie'; Kap. 8.1 (Lungenfunktion nach RT/RCT)"}
```

```yaml
# N-5
name: pneumonitisRiskPeriod
label_de: Pneumonitis-Risikofenster nach Strahlentherapie
definition_de: Zeitraum, in dem nach alleiniger Strahlentherapie oder Radiochemotherapie das Risiko einer Strahlenpneumonitis besteht (Onkopedia: 6–24 Monate nach Ende der Bestrahlung); bis zu dessen Ende soll die Lungenfunktionsprüfung fortgeführt werden.
datatype: Period
cardinality: 0..1
care_process:
  trigger: Ende der Strahlentherapie / Radiochemotherapie
  frequency_pattern: once
  responsible_role: Strahlentherapie / Pneumologie
evidence: {source: "Onkopedia NSCLC", version: "Stand April 2025", section: "Kap. 8.1 (Lungenfunktion bis Ende Pneumonitis-Risiko, soll); Kap. 6.2.2.1 (6-24 Monate nach Ende der Bestrahlung)"}
# Alternative: als constraints_de in pulmonaryFunctionTest statt eigenes Element
```

```yaml
# N-6
name: brainMetastasisRiskProfile
label_de: Individuelles Risiko für zerebrale Metastasierung
definition_de: Einstufung des individuellen Risikos einer ZNS-Metastasierung zur Steuerung der Schädel-MRT in der Nachsorge; Onkopedia-Kriterien histologisch (großzellige Karzinome, undifferenzierte Adenokarzinome, kleinzellige Anteile/Mischtumoren, seltene Lungentumorhistologien), S3-Kriterien molekular (EGFR+, ALK+, ROS1+, Adenokarzinom Stadium III).
datatype: CodeableConcept
cardinality: 0..1
care_process:
  trigger: Erstellung des Nachsorgeplans (nach Lokaltherapie)
  frequency_pattern: once-per-treatment-completion
  responsible_role: Onkologe / MDT (Tumorboard)
evidence: {source: "Onkopedia NSCLC", version: "Stand April 2025", section: "Kap. 8.1 (MRT-Schädel 6-9 Monate, erste drei Jahre nach Lokaltherapie); Kap. 6.1.6.2.1.1 (ALK)"}
```

```yaml
# N-7
name: curativeRecurrencePotential
label_de: Kuratives Potenzial bei Rezidiv / Zweitkarzinom
definition_de: Tumorboard-Einschätzung, ob bei einem in der Nachsorge detektierten Rezidiv oder Zweitkarzinom ein kurativer Therapieanspruch besteht. Bei „ja" kann das Nachsorgeintervall auf 6–8 Wochen verkürzt werden.
datatype: boolean
cardinality: 0..1
care_process:
  trigger: Detektion Rezidiv/Zweittumor (recurrenceOrSecondPrimary) → Tumorboard-Entscheid
  frequency_pattern: ad-hoc
  responsible_role: MDT (Tumorboard)
evidence: {source: "Onkopedia NSCLC", version: "Stand April 2025", section: "Kap. 8.1 ('kann das Nachsorgeintervall auf 6-8 Wochen verkürzt werden')"}
```

```yaml
# N-8
name: rehabilitationCounselling
label_de: Information/Beratung zu Rehabilitation und sozialrechtlichen Ansprüchen erfolgt
definition_de: Dokumentation, dass die Patient:in frühzeitig über ambulante und stationäre Rehabilitationsmaßnahmen sowie weitere sozialrechtliche Ansprüche informiert wurde (Onkopedia: „sollen … frühzeitig informiert werden").
datatype: boolean
cardinality: 1..1
care_process:
  trigger: Therapieabschluss; spätestens bei der Erstvorstellung in der Nachsorge (firstFollowUpVisitDate)
  frequency_pattern: once-per-treatment-completion
  responsible_role: Onkologe / Sozialdienst
evidence: {source: "Onkopedia NSCLC", version: "Stand April 2025", section: "Kap. 7 Rehabilitation"}
```

```yaml
# N-9
name: rehabilitationMeasure
label_de: Rehabilitationsmaßnahme (Setting, onkologischer Schwerpunkt)
definition_de: Beantragte/durchgeführte Rehabilitationsmaßnahme nach Therapie mit Setting (ambulant/stationär/AHB), Berücksichtigung des Patientenwunsches (§9 SGB IX) und Angabe, ob eine Klinik mit onkologischem Schwerpunkt empfohlen bzw. gewählt wurde.
datatype: CodeableConcept
cardinality: 0..*
care_process:
  trigger: Antrag / Antritt einer Rehabilitationsmaßnahme
  frequency_pattern: ad-hoc
  responsible_role: Sozialdienst / Onkologe / Reha-Einrichtung
evidence: {source: "Onkopedia NSCLC", version: "Stand April 2025", section: "Kap. 7 Rehabilitation (Klinik mit onkologischem Schwerpunkt, §9 SGB IX)"}
# Mapping-Hinweis: fhir-r4-base ServiceRequest / Procedure; Setting als Coding
```

### 4.2 Neue Elemente — Phase `surveillance`

```yaml
# N-10
name: consultationModality
label_de: Kontaktform der Verlaufskontrolle (Präsenz / Video / Telefon)
definition_de: Form des Patientenkontakts einer Verlaufskontrolle unter bzw. nach Systemtherapie. Onkopedia: Patientenzufriedenheit von Video-Sprechstunden bei fortgeschrittenem NSCLC der persönlichen Sprechstunde nicht unterlegen.
datatype: code
cardinality: 0..1
care_process:
  trigger: bei jedem Kontakt der Verlaufskontrolle
  frequency_pattern: per-encounter
  responsible_role: Onkologe
evidence: {source: "Onkopedia NSCLC", version: "Stand April 2025", section: "Kap. 8.2 (Video-Sprechstunden, Ref. Greer 2024)"}
# Priorität niedrig; Mapping fhir-r4-base Encounter.class / virtual
```

```yaml
# N-11
name: laboratoryPanelSurveillance
label_de: Laborkontrolle unter Systemtherapie (Basislabor)
definition_de: Symptom- und therapieorientiertes Basislabor im Stadium IV gemäß Onkopedia Tab. 2 (Blutbild, Elektrolyte, Nierenparameter, Leberparameter, LDH, Gerinnung); kein Nachsorge-Standard nach kurativer Therapie.
datatype: dateTime
cardinality: 0..*
care_process:
  trigger: symptom-/therapieorientiert, vor jedem Therapiezyklus bzw. bei jeder Verlaufskontrolle
  frequency_pattern: per-cycle
  responsible_role: Onkologe
evidence: {source: "Onkopedia NSCLC", version: "Stand April 2025", section: "Kap. 6.1.6.2 ('Diagnostik erfolgt symptom- und therapieorientiert, siehe Tabelle 2'); Tab. 2 (Kap. 5.2.1)"}
# UNSICHER: Onkopedia nennt keine Frequenz unter Therapie; per-cycle ist Praxisableitung
```

### 4.3 Zu ändernde Elemente

| Nr. | Element | Änderung | Begründung / Fundstelle |
| --- | --- | --- | --- |
| Ä-1 | `followUpInterval`, `ctThoraxScan`, `pulmonaryFunctionTest`, `brainMriHighRisk`, `ecogPerformanceStatus`, `patientReportedSymptomWeb`, `systemicTherapyRegimen` + `README.md:236`, `docs/methodology.md:236`, `docs/audit-log.md:398-399` | `version: "Stand 03/2026"` → **`"Stand April 2025"`**; audit-log: Monatsspalten für NSCLC Tab. 12 ohne „9" korrigieren | Abschnitt 1; keine Fassung 03/2026 auffindbar (UNSICHER, ob je existent) |
| Ä-2 | `followUpInterval` | (a) Code `Q6-9M` → `Q6-9W` (Display sagt Wochen); (b) neue Codes `Q6-8W-post-first-line` (Kap. 8.2) und `Q6-8W-curative-recurrence` (Kap. 8.1); (c) Code für Onkopedia-Raster `M3;M6;M12;M18;M24;M36;M48;M60` ergänzen (oder FHIR `Timing`); (d) `section` → „Kap. 8.1, Tab. 12" | L-03, L-08, L-14 |
| Ä-3 | `ctThoraxScan` | `frequency_pattern` quellenspezifisch: Onkopedia `M12;M24;M36;M48;M60 (alle) + M3;M6;M18 (nach RT/RCT)`; S3 `Q3M-Y1-Y2;Q6M-Y3-Y5`; Trigger an `curativeTreatmentModality` (N-4) koppeln; `constraints_de`: Onkopedia nennt nur „CT Thorax" (Oberbauch nicht erwähnt — UNSICHER) | L-03, L-04 |
| Ä-4 | `pulmonaryFunctionTest` | Trigger: „alle kurativ Behandelten Monat 3 und 6 (Tab. 12); fakultativ Monat 12/18/24; nach alleiniger RT/RCT bis Ende Pneumonitis-Risiko (6–24 Monate nach RT-Ende, soll)"; `frequency_pattern: M3;M6;(M12;M18;M24)`; Zusatzreferenz Kap. 6.2.2.1 | L-05, L-06 |
| Ä-5 | `brainMriHighRisk` | Trigger um Onkopedia-Histologiekriterien und „nur in den ersten drei Jahren nach Lokaltherapie" ergänzen; `section: "Kap. 8.1 (Text nach Tab. 12)"`; Empfehlungsstärke „sollte man durchaus erwägen" als `recommendation_grade: n/a` + Zitat in `notes`; optional Referenz auf N-6 | L-07 |
| Ä-6 | `brainMriUnderTherapy` | Trigger: „ALK+: MRT bei Diagnosestellung unabhängig von Symptomen; strukturierte Bildgebung z. B. alle 3–6 Monate auch asymptomatisch; zusätzlich bei Symptomen"; `frequency_pattern` um `Q3-6M (ALK+)` ergänzen; Onkopedia-Referenz Kap. 6.1.6.2.1.1 | L-17 |
| Ä-7 | `restagingImagingDate`, `recistResponse` | Onkopedia-Referenzen Kap. 8.2 (6–8 Wochen, S3-Expertenkonsens) und Kap. 6.1.6.2.2.1.2.1 (Erhaltungstherapie-Alternative) ergänzen; Trigger auf „unter Systemtherapie **und** in der therapiefreien Beobachtung nach Erstlinientherapie" erweitern; `frequency_pattern: Q6-8W (Onkopedia) / Q6-9W (S3)`; `constraints_de`: Modalität von Onkopedia nicht spezifiziert (Kontrollarm Denis 2017: CT alle 3–6 Monate) | L-14 |
| Ä-8 | `patientReportedSymptomWeb` | Population „Pat. in fortgeschrittenen Stadien ohne Krankheitsprogress" in `constraints_de`; Referenz [28] Denis 2017 JNCI 109:djx029 explizit; `evidence_level: 1b` beibehalten | L-15 |
| Ä-9 | `postTherapyComplication`, `survivorshipCarePlan` | Onkopedia Kap. 7 („Therapiefolgestörungen"), Kap. 8.1 („Erkennung von Nebenwirkungen der Therapie"), Kap. 6.2.2.1 (Pneumonitis → Fibrose), Kap. 6.1.6.1 (neurokognitive Langzeitfolgen nach Ganzhirnbestrahlung) als Referenzen; Value-Set um Strahlenpneumonitis / Lungenfibrose / neurokognitive Störung erweitern | L-12 |
| Ä-10 | `recurrenceOrSecondPrimary`, `structuredFollowUpPlan` | Onkopedia Kap. 8.1 (Nachsorgeziele; „Wert einer intensiven, strukturierten Nachsorge … nicht gesichert") als Zusatzreferenz; Verknüpfung zu N-7 | L-09 |

---

## 5 Bewertung der Kliniker-Kandidaten

| Kandidat | Phase | Onkopedia NSCLC empfiehlt in Nachsorge/Surveillance? | Fundstelle / Begründung | Hinweis für Repo |
| --- | --- | --- | --- | --- |
| Anamnese | followup | **ja** | Tab. 12, „X" an allen 8 Zeitpunkten (3/6/12/18/24/36/48/60 Mo) | fehlt als Element → N-1/N-2 |
| Körperliche Untersuchung | followup | **ja** | Tab. 12, „X" an allen 8 Zeitpunkten | fehlt als Element → N-1/N-3 |
| Röntgen Thorax | followup | **nein** | Nicht in Tab. 12/Kap. 8. Einzige Erwähnung Kap. 3.2: „Frühere Ansätze zum Einsatz von Röntgenaufnahmen des Thorax oder der Sputumzytologie hatten keinen signifikanten Einfluss auf die Senkung der Mortalität." (Screening-Kontext). Nachsorge-Bildgebung = CT Thorax. | nicht aufnehmen (allenfalls als `ad-hoc` Symptomdiagnostik) |
| Sonografie Abdomen | followup | **nein** | Nur Tab. 3 (Staging, Kap. 5.2.1): „Sonographie Oberbauch". Keine Nachsorge-Empfehlung. | nicht aufnehmen |
| Bronchoskopie | followup | **nein** (nur konditional bei Verdacht) | Nur Tab. 2 (Erstdiagnose): „Bronchoskopie mit Biopsie — bei bildgebendem Verdacht und zugänglicher Raumforderung". In Kap. 8 nicht erwähnt. Bei Rezidivverdacht gilt die Erstdiagnostik-Logik (Rückschluss, nicht Wortlaut — UNSICHER). | nicht als Routine; ggf. `ad-hoc` bei Rezidivverdacht |
| PET-CT | followup | **nein** | Nur Staging: Tab. 2 „CT Thorax / Oberbauch mit Kontrastmittel, oder FDG-PET-CT — Methode der ersten Wahl"; Tab. 3 „FDG-PET-CT — bei kurativem Therapiekonzept"; Kap. 6.1.6.1 (Oligometastasierung: „komplettes Staging einschl. FDG-PET und Schädel MRT"). In Kap. 8 nicht erwähnt. (Die von Onkopedia zitierte ASCO-Surveillance-Leitlinie [121] rät nach Erinnerung von PET-CT-Surveillance ab — **UNSICHER**, nicht aus dem Onkopedia-Text.) | nicht aufnehmen; Restaging bei Rezidiv/kurativem Potenzial = Treatment-/Diagnostik-Phase |
| Abdomen-CT | followup | **nein** | Tab. 12 nennt ausschließlich „CT Thorax". Abdomen nur Staging: Tab. 2 „CT Thorax / Oberbauch"; Tab. 3 „CT Abdomen (einschl. Nebennieren, unterer Leberrand und Becken) — falls FDG-PET-CT nicht durchführbar". Ob das Nachsorge-CT den Oberbauch einschließt, sagt Onkopedia nicht (UNSICHER). | nicht als eigenes Routine-Element |
| Laborparameter | followup | **nein** | In Kap. 8/Tab. 12 nicht enthalten. Labor nur Tab. 2 (Erstdiagnose): „Blutbild, Elektrolyte, Nierenparameter, Leberparameter, LDH, Gerinnung". Tumormarker kommen in der gesamten Leitlinie nicht vor. | nicht aufnehmen (followup) |
| Anamnese | surveillance | **konditional / implizit** | Kap. 8.2 benennt keine Einzeluntersuchungen; Kontrolle alle 6–8 Wochen (S3-EK) und „personalisierte Überwachung … mittels Web-basierter Instrumente" (wöchentliche Symptom-Selbsteinschätzung) sind die genannten Instrumente; Kap. 6.1.6.2: „Diagnostik erfolgt symptom- und therapieorientiert". | abgedeckt über `patientReportedSymptomWeb`; klinische Anamnese per Kontakt ergänzbar (per-encounter) |
| Körperliche Untersuchung | surveillance | **konditional / implizit** | Nicht explizit genannt; Teil der 6–8-wöchigen Kontrolle (Modalität offen) — UNSICHER | optional, per-encounter |
| CT-Thorax | surveillance | **konditional (ja)** | Kap. 8.2: Kontrollarm Denis 2017 = „standardisierte 3- bzw. 6-monatliche CT Kontrolle"; S3-EK 6–8-wöchige Intervalle; Kap. 6.1.6.2.2.1.2.1: „engmaschige Kontrolle, z. B. in Abständen von 6-8 Wochen"; Modalität über Tab. 2 (CT Thorax/Oberbauch mit KM oder FDG-PET-CT). Onkopedia legt das CT-Intervall unter Therapie **nicht** explizit fest. | `restagingImagingDate` (Ä-7) |
| CT-Abdomen | surveillance | **konditional** | Nur über Tab. 2 („CT Thorax / **Oberbauch**", nicht ganzes Abdomen) bzw. Tab. 3 (CT Abdomen falls PET-CT nicht durchführbar) als symptom-/therapieorientierte Diagnostik (Kap. 6.1.6.2). Keine eigene Surveillance-Aussage. | in `restagingImagingDate` bereits als „CT Thorax/Abdomen/Becken" definiert — Definition geht über Onkopedia hinaus (S3-basiert) |
| CT Becken | surveillance | **nein** | „Becken" nur in Tab. 3 als Teil des CT Abdomen im Staging „falls FDG-PET-CT nicht durchführbar". Keine Surveillance-Empfehlung. | nicht als eigenes Element |

---

### Anhang: Verifizierungsnotizen
- Abruf: 2026-10-13, `curl` auf den Volltext (633 KB HTML → 2.726 Textzeilen) und die Übersichtsseite; Kapitel 7/8 und Tab. 12 wörtlich aus dem Rohtext übernommen (nicht aus einer Zusammenfassung).
- Referenznummern [28]/[46]/[117]/[121] wurden über die alphabetische Referenzliste zugeordnet (Denis 2017 / Greer 2024 / S3-LL 2022 / Schneider 2020) — die HTML-Liste trägt keine sichtbaren Nummern; Zuordnung durch Kontext (z. B. [117] auch bei „Standard ist die Lobektomie [82, 117]") plausibilisiert.
- Onkopedia Kap. 8.2 bezieht sich auf die S3-Leitlinie **November 2022** [117]; das Repo zitiert S3 v5.01 (Konsultationsfassung 04/2026) — abweichende S3-Version, hier nicht geprüft.
- Nicht geprüft (außerhalb des Auftrags): Onkopedia SCLC (Repo-Pin „Stand 09/2025"), S3-LL Lungenkarzinom.
