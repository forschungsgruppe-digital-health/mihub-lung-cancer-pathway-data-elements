# Glossar

Strukturierte Auflistung der medizinischen Terminologie, Akronyme, Klassifikations-Codes und projekt-spezifischen Bezeichner, die in den Datenelementen verwendet werden.

**Einheitliches 4-Spalten-Schema:**

- **Akronym** — Kurzform / projekt-internes Code-Token (`—` falls keines)
- **Bedeutung** — Vollform / Auflösung des Akronyms
- **Beschreibung** — Kontext, Wertebereich, ggf. Cut-off, klinische Relevanz
- **Quelle** — Verlinkung zur Primärquelle bzw. Standard

**Verifikations-Hinweis (siehe §18):** Alphanumerische Codes (SNOMED-IDs, LOINC-Nummern, ICD-O-3-Codes) sollten gegen Terminologie-Server validiert werden — die hier angegebenen Codes sind plausibel, aber nicht durchgehend Server-verifiziert.

> **Pflege-Verantwortung:** Der `data-element-analyzer`-Sub-Agent (siehe `AGENTS.md`) prüft bei jedem Lauf, ob neue Begriffe in den YAMLs auftauchen, und schlägt Erweiterungen vor.

---

## 1 Tumor-Entitäten und Stadien

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **NSCLC** | Non-Small Cell Lung Cancer | Nicht-kleinzelliges Lungenkarzinom; ca. 85 % aller Lungenkarzinome; Histologie u. a. Adeno-, Plattenepithel-, großzelliges Karzinom | S3-LL Lungenkarzinom v5.01 Kap. 6.6, Onkopedia NSCLC |
| **SCLC** | Small Cell Lung Cancer | Kleinzelliges Lungenkarzinom; ca. 12–15 % aller Lungenkarzinome; hochproliferativ, hohe initiale Chemo-/Radiosensitivität | S3-LL Lungenkarzinom v5.01 Kap. 9, Onkopedia SCLC |
| **LD-SCLC** | Limited Disease SCLC | SCLC-Stadium auf Hemithorax begrenzt (T1–4 N0–3 M0) | S3-LL Lungenkarzinom v5.01 Kap. 9.5 |
| **ED-SCLC** | Extensive Disease SCLC | SCLC-Stadium mit Fernmetastasen (M1) | S3-LL Lungenkarzinom v5.01 Kap. 9.6 |
| **VLD** | Very Limited Disease | SCLC T1–2 N0–1 M0 (kuratives Setup, ggf. inkl. Operation) | S3-LL Lungenkarzinom v5.01 Kap. 9.4 |
| **OMD** | Oligometastatic Disease | Begrenzte Anzahl Fernmetastasen, oft lokal-ablativ behandelbar | ESMO/ESTRO/EORTC Konsens 2020 (Lancet Oncol 21:e18–e28) |
| **TNM** | Tumor – Node – Metastasis | UICC-Klassifikation des Tumorstadiums; aktuell 9. Auflage 2024 | IASLC Staging Project; UICC TNM 9th ed. (2024) |
| **R0/R1/R2** | Residualtumor-Klassifikation | R0 = mikroskopisch tumorfrei; R1 = mikroskopisch positiv; R2 = makroskopisch positiv | UICC TNM Supplement |
| **C34.x** | ICD-10-GM Topographie Lungentumor | C34.0 Hauptbronchus, C34.1 Oberlappen, C34.2 Mittellappen, C34.3 Unterlappen, C34.8 Übergreifend, C34.9 n.n.b. | BfArM ICD-10-GM 2026 |

## 2 Performance Status & Funktion

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **ECOG** | Eastern Cooperative Oncology Group Performance Status | 0 = asymptomatisch · 1 = symptomatisch, ambulant · 2 = bettlägerig <50 % · 3 = bettlägerig >50 % · 4 = bettlägerig 100 % · 5 = Tod | Oken MM et al. Am J Clin Oncol 5:649–655 (1982); LOINC 89262-0 |
| **KPS** | Karnofsky Performance Status | 0–100 in 10er-Schritten; höher = besser; 100 = normal, 50 = Hilfe nötig, 10 = moribund | Karnofsky DA, Burchenal JH (1949); SNOMED 373802001 |
| **AKPS** | Australian-modified Karnofsky Performance Status | Adaption an Palliativkontext (insb. häuslich); 0–100 | Abernethy AP et al. BMC Palliat Care (2005); LOINC 70924-1 |
| **ADL** | Activities of Daily Living | Aktivitäten des täglichen Lebens (i. d. R. Barthel, ADL-Index) | Katz S et al. JAMA 185:914 (1963) |
| **Barthel-Index** | — | Selbstversorgungs-Skala 0–100 (10er-Schritte); höher = mehr Selbstständigkeit | Mahoney FI, Barthel DW. Md State Med J 14:61 (1965); LOINC 65488-5 |

## 3 PROM / Symptomerfassungs-Instrumente

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **PROM** | Patient-Reported Outcome Measurement | Übergreifender Begriff für Selbsteinschätzungs-Instrumente | ISO 9001 / FDA Guidance (2009) |
| **NRS** | Numerische Rating-Skala | 0–10; verwendet für Schmerz, Atemnot, Distress u. a. | S3-LL Palliativ v3.01 Kap. 9.2 + 10.2 |
| **VAS** | Visuelle Analogskala | i. d. R. 0–100 mm | Wewers ME, Lowe NK. Res Nurs Health 13:227 (1990) |
| **EORTC QLQ-C30** | European Org. for Research and Treatment of Cancer · Quality of Life Questionnaire — Core 30 | 30 Items in 5 Funktions-Skalen + 9 Symptom-Skalen + globale QoL; 0–100 (höher = besser bei QoL/Funktion) | Aaronson NK et al. JNCI 85:365 (1993); LOINC 73831-0 |
| **EORTC QLQ-LC13** | EORTC Lung Cancer Module | 13 Items, ergänzt QLQ-C30 für Lungenkarzinom | Bergman B et al. Eur J Cancer 30A:635 (1994) |
| **EORTC QLQ-C15-Pal** | Palliativ-Modul (15 Items) | Verkürzte palliative Version von QLQ-C30 | Groenvold M et al. Eur J Cancer 42:55 (2006); S3-LL Palliativ Tab. 9 |
| **MIDOS2** | Minimales Dokumentationssystem 2 | Symptomerfassung in der dt. Palliativversorgung; 7+ Items | Stiel S et al. Schmerz 24:596 (2010); S3-LL Palliativ Tab. 6 |
| **ESAS-r** | Edmonton Symptom Assessment System — Revised | 0–10 für 9 Kernsymptome (Schmerz, Müdigkeit, Atemnot, …) | Watanabe SM et al. J Pain Symptom Manage 41:456 (2011); S3-LL Palliativ Tab. 6 |
| **IPOS** | Integrated Palliative care Outcome Scale | 17 Items (Patient + Personal); mehrdimensional | Murtagh FE et al. Palliat Med 33:1045 (2019); LOINC 89200-0 |
| **POS** | Palliative care Outcome Scale | Vorgänger von IPOS; 12 Items | Hearn J, Higginson IJ. Qual Health Care 8:219 (1999) |
| **Distress-Thermometer** | NCCN Distress Thermometer + Problemliste | 0–10; Cut-off ≥ 5 = Indikation für Psychoonkologie/Sozialberatung | NCCN Guidelines for Distress Management; Mehnert A et al. (deutsche Validierung); LOINC 63994-4 |
| **PHQ-9** | Patient Health Questionnaire (9 Items) — Depression | 0–27; Cut-off ≥ 5 mild · ≥ 10 mittelschwer · ≥ 15 schwer · ≥ 20 sehr schwer | Kroenke K et al. JGIM 16:606 (2001); LOINC 44261-6 |
| **HADS** | Hospital Anxiety and Depression Scale | 14 Items, Subskalen Angst (HADS-A) und Depression (HADS-D), je 0–21; Cut-off ≥ 8 auffällig · ≥ 11 wahrscheinlich klinisch | Zigmond AS, Snaith RP. Acta Psychiatr Scand 67:361 (1983); LOINC 62106-6 |
| **Zarit ZBI** | Zarit Burden Interview | 22 Items × 0–4 → 0–88; Cut-offs 0–21 (gering) / 21–40 (mild-moderat) / 41–60 (moderat-schwer) / 61–88 (schwer) | Zarit SH et al. Gerontologist 20:649 (1980); LOINC 62133-0 |
| **CAREPAL** | Multidimensionaler CAREPAL-Fragebogen | Belastung Angehöriger pflegebedürftiger Krebspatient:innen, mehrdimensional | S3-LL Palliativ v3.01 Tab. 6 |
| **HPS-DEGAM** | Häusliche Pflegeskala der DEGAM | Hausärztliches Belastungs-Assessment, mehrdimensional | DEGAM Praxisempfehlung Pflege |
| **MRC-Skala** | Medical Research Council Dyspnoea Scale | 0–4 Belastungsdyspnoe (0 = Atemnot nur bei starker Belastung; 4 = Atemnot bei An- und Auskleiden) | Fletcher CM, MRC. BMJ 2:1665 (1959) |
| **RDOS** | Respiratory Distress Observation Scale | 8 Items zur Fremdeinschätzung Atemnot bei kognitiver Einschränkung; 0–16 | Campbell ML. J Palliat Med 11:44 (2008); S3-LL Palliativ v3.01 Kap. 9.2 |

## 4 Therapieansprechen & Onkologische Endpunkte

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **RECIST 1.1** | Response Evaluation Criteria In Solid Tumors | Standardisierte Kriterien zur radiologischen Beurteilung des Therapieansprechens; bewertet Größenänderung von Zielläsionen | Eisenhauer EA et al. Eur J Cancer 45:228 (2009) |
| **CR** | Complete Response | Verschwinden aller Zielläsionen | RECIST 1.1; SNOMED 182840001 |
| **PR** | Partial Response | ≥ 30 % Abnahme der Summe der längsten Durchmesser der Zielläsionen | RECIST 1.1; SNOMED 268910001 |
| **SD** | Stable Disease | Weder PR noch PD | RECIST 1.1; SNOMED 359746009 |
| **PD** | Progressive Disease | ≥ 20 % Zunahme der Summe der längsten Durchmesser ODER neue Läsion | RECIST 1.1; SNOMED 271879005 |
| **NE** | Not Evaluable | Bewertung nicht möglich (z. B. Bildgebung inadäquat) | RECIST 1.1 |
| **OS** | Overall Survival | Gesamtüberleben ab definiertem Zeitpunkt (z. B. Diagnose, Therapiebeginn) | klinischer Studienstandard |
| **PFS** | Progression-Free Survival | Zeit ab Therapiebeginn bis Progression oder Tod | klinischer Studienstandard |
| **DFS** | Disease-Free Survival | Zeit ab kurativer Behandlung bis Rezidiv oder Tod | klinischer Studienstandard |
| **QoL** | Quality of Life | Lebensqualität; meist über validierte PROMs erhoben | WHO QoL definition |

## 5 Toxizität & unerwünschte Ereignisse

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **AE** | Adverse Event | Unerwünschtes Ereignis, übergreifender Begriff in klinischen Studien | ICH-E2A Guidelines |
| **CTCAE** | Common Terminology Criteria for Adverse Events | Standardisierte Klassifikation und Graduierung; aktuell v5.0 (2017) und v6.0 (geplant); Grade 1 (mild) bis 5 (Tod) | NCI-CTCAE [ctep.cancer.gov](https://ctep.cancer.gov/protocoldevelopment/electronic_applications/ctc.htm) |
| **irAE** | immune-related Adverse Event | Spezifische Toxizitäten unter Checkpoint-Inhibitoren (Pneumonitis, Kolitis, Hepatitis, Endokrinopathien, Hautreaktionen) | Brahmer JR et al. JCO 36:1714 (2018); SNOMED 1217138004 |
| **MedDRA** | Medical Dictionary for Regulatory Activities | Hierarchische AE-Terminologie (SOC → HLGT → HLT → PT → LLT) | ICH-MedDRA, OID `urn:oid:2.16.840.1.113883.6.163` |
| **NCI** | National Cancer Institute (USA) | Herausgeber CTCAE | nih.gov/cancer.gov |

## 6 Versorgungsstrukturen & Versorgungsstufen (Palliativ)

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **PBP** | Palliativmedizinische Basisversorgung durch Primärbehandelnde | Niedrige Komplexität (Symptome wenig ausgeprägt, stabile Situation) | S3-LL Palliativ v3.01 Kap. 5.4 |
| **APV** | Allgemeine Palliativversorgung | Mittlere Komplexität (Symptome, Plan-Anpassungen, kurzfristige Interventionen) | S3-LL Palliativ v3.01 Kap. 5.4 |
| **SPV** | Spezialisierte Palliativversorgung | Hohe Komplexität (Schwer behandelbare Symptome, dauerhaft spezialisierte Expertise) | S3-LL Palliativ v3.01 Kap. 5.4 |
| **SAPV** | Spezialisierte Ambulante Palliativversorgung | Gesetzlicher Anspruch; SAPV-Teams (Mediziner + Pflegende + ggf. Sozial-/Seelsorge) | §37b SGB V; SAPV-Richtlinie G-BA |
| **AAPV** | Allgemeine Ambulante Palliativversorgung | Hausärztliche Palliativbetreuung außerhalb SAPV | KBV-Vereinbarung BAnz 2010 |
| **ACP** | Advance Care Planning | Vorausschauende Versorgungsplanung mit Patient:in (+ ggf. Angehörigen): Therapieziele, Patientenverfügung, Vorsorgevollmacht | S3-LL Palliativ v3.01 Kap. 6.5; SNOMED 713600000 |
| **OL** | Leitlinienprogramm Onkologie | DKG / DKH / AWMF gemeinsam | leitlinienprogramm-onkologie.de |

## 7 Therapie-Modalitäten

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **OP** | Operation (Resektion) | Kurative oder palliative chirurgische Entfernung | S3-LL Lungenkarzinom v5.01 Kap. 8 |
| **VATS** | Video-Assisted Thoracic Surgery | Videoassistierte Thorakoskopie; minimal-invasiv | S3-LL Lungenkarzinom v5.01 Empf. 8.15 |
| **RATS** | Robotic-Assisted Thoracic Surgery | Roboter-assistierte minimal-invasive Thoraxchirurgie | S3-LL Lungenkarzinom v5.01 Empf. 8.15 |
| **RTx / RT** | Radiotherapie / Strahlentherapie | Externe oder interne Strahlentherapie | S3-LL Lungenkarzinom v5.01 Kap. 8.5 |
| **CTx** | Chemotherapie | Systemische Zytostatika-Therapie | S3-LL Lungenkarzinom v5.01 Kap. 8.6 |
| **CRT** | Chemoradiotherapie | Kombinierte Chemo- und Strahlentherapie (sequenziell oder konkurrent) | Aupérin A et al. JCO 28:2181 (2010) |
| **SBRT / SABR** | Stereotactic Body Radiation Therapy / Ablative Radiotherapy | Hochpräzise hypofraktionierte Strahlentherapie | Chang JY et al. Lancet Oncol 16:630 (2015) |
| **PCI** | Prophylactic Cranial Irradiation | Prophylaktische Schädelbestrahlung (insb. SCLC) | S3-LL Lungenkarzinom v5.01 Kap. 9 |
| **TKI** | Tyrosine Kinase Inhibitor | Zielgerichtete orale Therapie (z. B. Osimertinib, Alectinib) | Onkopedia NSCLC Kap. 6 |
| **ICI** | Immune Checkpoint Inhibitor | Anti-PD-1, anti-PD-L1, anti-CTLA-4 (z. B. Pembrolizumab, Atezolizumab, Durvalumab) | Onkopedia NSCLC Kap. 6 |
| **NRT** | Nikotinersatztherapie | Pflaster, Kaugummi, Lutschtablette, Spray, Inhaler | S3-LL Tabakentwöhnung 076-006l (03/2021); ATC N07BA01 |
| **DiGA** | Digitale Gesundheitsanwendung | BfArM-zugelassene Software-Medizinprodukte; verordnungsfähig nach §33a SGB V | BfArM DiGA-Verzeichnis [diga.bfarm.de](https://diga.bfarm.de/) |
| **ABC-Schema** | — | Tabakentwöhnungs-Algorithmus: **A**sk – **B**rief advice – **C**essation support | S3-LL Lungenkarzinom v5.01 Empf. 4.3 |

## 8 Genetische Marker & Molekularpathologie

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **EGFR** | Epidermal Growth Factor Receptor | Aktivierende Mutationen v. a. Exon 19-Deletion (Del19) und Exon 21 L858R; Therapie: Osimertinib (1.-Linie), Afatinib | Onkopedia NSCLC Kap. 6.2; LOINC 21678-9 |
| **ALK** | Anaplastic Lymphoma Kinase | EML4-ALK-Translokation; Therapie: Alectinib (1.-Linie), Brigatinib, Lorlatinib | Hendriks LE et al. Ann Oncol 34:339 (2023) |
| **ROS1** | ROS Proto-Oncogene 1 | Translokation; Therapie: Crizotinib, Entrectinib, Repotrectinib | Drilon A et al. Lancet Oncol 21:261 (2020) |
| **KRAS** | Kirsten Rat Sarcoma viral oncogene | Häufigste Mutation in Adeno-NSCLC; G12C-Mutation: Sotorasib, Adagrasib | Hong DS et al. NEJM 383:1207 (2020); LOINC 81238-6 |
| **BRAF** | B-Raf Proto-Oncogene | V600E-Mutation; Therapie: Dabrafenib + Trametinib | Planchard D et al. Lancet Oncol 17:984 (2016) |
| **RET** | RET Proto-Oncogene | Fusion (KIF5B-RET u. a.); Therapie: Selpercatinib, Pralsetinib | Drilon A et al. JCO 41:385 (2022) |
| **NTRK** | Neurotrophic Tyrosine Receptor Kinase | Fusion (NTRK1/2/3); Therapie: Larotrectinib, Entrectinib | Doebele RC et al. Lancet Oncol 21:271 (2020) |
| **MET** | MET Proto-Oncogene | Exon-14-Skipping-Mutation oder Amplifikation; Therapie: Capmatinib, Tepotinib | Wolf J et al. NEJM 383:944 (2020) |
| **HER2** | Human Epidermal growth factor Receptor 2 | Mutation oder Überexpression; Therapie: Trastuzumab-Deruxtecan | Li BT et al. NEJM 386:241 (2022) |
| **PD-L1** | Programmed Death-Ligand 1 | Tumor Proportion Score (TPS): % der Tumorzellen mit Membranfärbung; Eligibility für ICI | Reck M et al. NEJM 375:1823 (2016) |
| **T790M** | EGFR-Resistenzmutation Exon 20 | Häufigste Resistenz gegen 1./2.-Generations-EGFR-TKI; Indikation für Osimertinib | Mok TS et al. NEJM 376:629 (2017) |
| **C797S** | EGFR-Resistenzmutation Exon 20 | Resistenz gegen Osimertinib (3. Generation) | Thress KS et al. Nat Med 21:560 (2015) |
| **G12C** | KRAS-Mutation Codon 12 (Glycin → Cystein) | Therapie: Sotorasib (AMG 510), Adagrasib | Hong DS et al. NEJM 383:1207 (2020) |
| **ctDNA** | circulating tumor DNA | Liquid Biopsy aus Plasma; Resistenz-Monitoring, Mutations-Tracking | Onkopedia NSCLC Kap. 8.2; LOINC 84141-0 |
| **HGVS** | Human Genome Variation Society Nomenclature | Standardisierte Variant-Notation (z. B. `c.2369C>T (p.Thr790Met)`) | varnomen.hgvs.org |
| **ICD-O-3** | International Classification of Diseases for Oncology, 3rd Edition | M-Codes (Histologie, 8000–9999) und T-Codes (Topographie); BfArM publiziert deutsche Edition | WHO/IARC ICD-O-3.2 (2019); BfArM; OID `urn:oid:2.16.840.1.113883.6.43.1` |

## 9 Bildgebung & Funktionsdiagnostik

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **CT** | Computertomographie | Schnittbildverfahren mit ionisierender Strahlung | LOINC 30688-4; OPS 3-202 |
| **MRT / MRI** | Magnetresonanztomographie | Schnittbildverfahren ohne ionisierende Strahlung | LOINC 24590-2 (MR Brain); OPS 3-820 |
| **PET-CT** | Positronen-Emissions-Tomographie + CT | Hybrid-Bildgebung mit ¹⁸F-FDG; Stoffwechselaktivität + Anatomie | Onkopedia NSCLC Kap. 5 |
| **LDCT** | Low-Dose-CT | Strahlenarmes CT; Lungenkarzinom-Screening (NLST, NELSON) | de Koning HJ et al. NEJM 382:503 (2020) |
| **DICOM** | Digital Imaging and Communications in Medicine | Standard für Bilddaten und Bildbefunde | dicomstandard.org |
| **DICOM SR** | DICOM Structured Report | Strukturierter Bildbefund-Container | DICOM PS3.3 Annex A.35 |
| **FEV1** | Forciertes exspiratorisches Volumen in 1 Sekunde | Spirometrie-Hauptparameter; relevant für Operabilität, COPD-Diagnose, Pneumonitis-Verlauf | LOINC 20150-9; SNOMED 59328004 |
| **FVC** | Forced Vital Capacity | Forcierte Vitalkapazität (Maximalvolumen forcierte Ausatmung); SNOMED 50834005 | ATS/ERS Standardisierung 2019 |
| **DLCO / TLCO** | Diffusing Capacity for Carbon Monoxide / Transfer Factor | Lungengasaustausch; relevant bei Strahlentherapie-Folgen, Pneumonitis | LOINC 17129-7; SNOMED 252464004 |

## 10 Klinische Dokumente, Pläne & Survivorship

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **SCP** | Survivorship Care Plan | Strukturierter Onkologischer Abschlussbericht: Diagnose, Therapie, Spätfolgen, Kontrollintervalle, Kontaktdaten | Klein A-A et al. Die Onkologie 32:91 (2026); AG LONKO Empfehlungen |
| **MDT** | Multidisciplinary Team | Tumorboard; interdisziplinäre Therapieentscheidung | OCP Lung 2nd ed. Principle 3 |
| **OCP** | Optimal Care Pathway | Strukturierter Versorgungspfad (AU); Cancer Council Victoria | cancer.org.au/OCP |
| **AG LONKO** | Arbeitsgemeinschaft Langzeitüberleben nach Krebs | Im Nationalen Krebsplan; Empfehlungen Survivorship | bundesgesundheitsministerium.de Nationaler Krebsplan |
| **SaxoForN** | Sächsisch-Hessisches Forschungspraxennetz Allgemeinmedizin | Hausarzt-Forschungs-Konsortium; BMBF-gefördert | Mergenthal K et al. Bundesgesundheitsbl 66:1042 (2023) |

## 11 Frequenz- und Zeitmuster (projekt-eigenes Vokabular)

Diese Codes sind als `local-no-standard-binding` markiert (kein etabliertes ValueSet); siehe `docs/design-faq.md` Sektion „Standardlücken".

> **Lese-Hilfe `Q…`:** Das vorangestellte `Q` ist die medizinisch-lateinische Abkürzung **`q` / *quaque* = „alle" / „jede(r/s)"** (analog zur Verordnungs-Notation `q4h` = alle 4 Stunden). Es bedeutet **nicht** „Quartal". Die nachfolgende Einheit ergibt sich aus dem Suffix: `W` = Wochen, `M` = Monate. `Q3M` ist somit nur dann „quartalsweise", wenn `n=3` zufällig genau einem Quartal entspricht — die Notation selbst ist einheiten-neutral.

**Pattern:**

- `Q<n>W` = alle `n` Wochen
- `Q<a>-<b>W` = alle `a` bis `b` Wochen
- `Q<n>M` = alle `n` Monate
- `Q<a>-<b>M` = alle `a` bis `b` Monate
- `Y<n>` = Jahr `n` nach Therapieabschluss
- `PostY<n>` = ab Jahr `n`

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| `Q3M-Y1-Y2` | alle 3 Monate, Jahr 1–2 | dreimonatlich (≈ quartalsweise) in den ersten beiden Jahren nach Therapieabschluss | S3-LL Lungenkarzinom v5.01 Empf. 16.7 (B) |
| `Q6M-Y3-Y5` | halbjährlich, Jahr 3–5 | alle 6 Monate, in Jahr 3 bis 5 | S3-LL Lungenkarzinom v5.01 Empf. 16.7 |
| `Q12M-PostY5` | jährlich ab Jahr 6 | jährliches Screening (LDCT-Anschluss) | S3-LL Lungenkarzinom v5.01 Empf. 16.7 |
| `Q6-9W` | alle 6–9 Wochen | unter palliativer Systemtherapie | S3-LL Lungenkarzinom v5.01 Empf. 16.9 (B) |
| `per-encounter` | bei jedem Patientenkontakt | übergreifend | projekt-spezifisch |
| `per-imaging-event` | nach jeder Bildgebung | Bildbefund-Erfassung | projekt-spezifisch |
| `per-procedure` | nach jeder Prozedur | Funktionsdiagnostik, Lungenfunktion | projekt-spezifisch |
| `per-cycle` | pro Therapiezyklus | Systemtherapie | projekt-spezifisch |
| `per-event` | pro Ereignis | Toxizität (AE/CTCAE) | projekt-spezifisch |
| `once` / `once-per-treatment-completion` / `once-per-transition` | einmalig | Pläne, Übergaben | projekt-spezifisch |
| `weekly` | wöchentlich | Web-PROM (Denis 2017) | Onkopedia NSCLC Kap. 8.2 |
| `Q1M in SPV` | monatlich in spezialisierter Palliativversorgung | Caregiver-Burden-Verlauf | S3-LL Palliativ v3.01 Kap. 7.4 |
| `ad-hoc` | bei Bedarf | situativ | projekt-spezifisch |
| `tägliche Re-Evaluation` | täglich | Sterbephase | S3-LL Palliativ v3.01 Kap. 21 |
| `ongoing` | fortlaufend | ACP über Erkrankungsverlauf | S3-LL Palliativ v3.01 Kap. 6.5 |

## 12 Krankheitsphasen (Palliativ)

Australian Palliative Care Phases — übernommen in S3-LL Palliativmedizin Kap. 5.3 / Tab. 6.

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| `stable` | stabil | Symptome durch Versorgungsplan kontrolliert; keine neuen Probleme | S3-LL Palliativ v3.01 Tab. 6 |
| `unstable` | instabil | Akute Verschlechterung; Plan-Anpassung erforderlich | S3-LL Palliativ v3.01 Tab. 6 |
| `deteriorating` | verschlechternd | Erwartbare graduelle Verschlechterung | S3-LL Palliativ v3.01 Tab. 6 |
| `dying` | sterbend (terminal) | Tod innerhalb der nächsten Tage wahrscheinlich | S3-LL Palliativ v3.01 Tab. 6 |

## 13 Standards & Implementation Guides

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **oBDS** | Onkologischer Basisdatensatz | DE Krebsregister-Pflichtmeldung; aktuelle Version 3.0 (03/2022); Plattform §65c SGB V | basisdatensatz.de; §65c SGB V |
| **GEKID / ADT** | GEKID = Gesellschaft der epidemiologischen Krebsregister; ADT = Arbeitsgemeinschaft Deutscher Tumorzentren | Vorgänger und Träger des oBDS | gekid.de |
| **MII** | Medizininformatik-Initiative | BMBF-gefördertes Konsortium der Universitätskliniken | medizininformatik-initiative.de |
| **MII KDS** | MII Kerndatensatz | Module Person, Diagnose, Prozedur, Labor, Medikation, Bildgebung, Onkologie u. a. | medizininformatik-initiative.de |
| **FDPG** | Forschungsdatenportal Gesundheit | Antrags-Plattform für MII-Daten | forschen-fuer-gesundheit.de |
| **DSF** | Dezentrale Systemföderation | MII Datenintegrations-Pattern (HiGHmed/MIRACUM/SMITH/DIFUTURE) | dsf.dev |
| **gematik ePA** | gematik elektronische Patientenakte (für alle) | DE gesetzliche ePA-Plattform; verpflichtend seit 01/2025 | fachportal.gematik.de |
| **eRezept** | gematik elektronisches Rezept | DE gesetzliche elektronische Verordnung | gematik.de |
| **ISiK** | Informationstechnische Systeme im Krankenhaus | gematik FHIR-IGs für KIS/AIS-Primärsysteme; Stufen 1–4 | gematik.de/isik |
| **KBV MIO** | KBV Medizinisches Informationsobjekt | DE ePA-Module (Patientenkurzakte, Impfpass, Mutterpass, ZahnBonusheft u. a.) | mio.kbv.de |
| **KDL** | Klinische Dokumentenklassen-Liste (DVMD) | DE-Standard-Klassifikation für klinische Dokumente; verbindlich seit 01.01.2024; OID `urn:oid:1.2.276.0.76.5.451` | DVMD; gemspec.gematik.de/ig/fhir/terminology |
| **mCODE** | minimal Common Oncology Data Elements | HL7 FHIR Onkologie IG; aktuell STU4 (~40 Profile in 6 Bereichen) | hl7.org/fhir/us/mcode/ |
| **OMOP CDM** | Observational Medical Outcomes Partnership Common Data Model | OHDSI; international Versorgungsforschung; mit Onkologie-Extension | ohdsi.github.io/CommonDataModel/ |
| **CDISC SDTM** | Clinical Data Interchange Standards Consortium · Study Data Tabulation Model | Klinische Studien; Regulatorik (FDA, EMA) | cdisc.org/standards/foundational/sdtm |
| **HL7 V2** | HL7 Messaging V2 | Legacy ADT, Labor, DALE-UV | hl7.org/v2 |
| **HL7 CDA** | HL7 Clinical Document Architecture | Strukturierte Dokumente (z. B. eArztbrief) | hl7.org/cda |
| **IHE XDS** | IHE · Cross-Enterprise Document Sharing | Dokumenten-Affinity-Domains | ihe.net/uploadedFiles/Documents/ITI/IHE_ITI_TF_Vol1.pdf |
| **openEHR** | openEHR | EHR-Architektur-Framework, Archetypen-basiert | openehr.org |
| **DiGA** | Digitale Gesundheitsanwendung (BfArM) | DE-Verzeichnis seit 2020 | diga.bfarm.de |

## 14 ISO / HL7 / FHIR-Begriffe

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **ISO 13606** | EHR Communication | Reference Model + Archetype Model + Archetype Interchange + Security + Interface Specification | ISO/IEC 13606-1…5 (2019) |
| **ISO 13940** | ContSys (Continuity of Care) | System of Concepts for Continuity of Care | ISO 13940:2015 |
| **ISO 13972** | Clinical Information Models | Characteristics, Structures and Requirements (CIM) | ISO 13972:2022 |
| **ISO 21090** | Healthcare Datatypes | Basis für FHIR-Datentypen | ISO 21090:2011 |
| **ISO 23903** | Interoperability and Integration Reference Architecture | Plattformneutralität; Generic Component Model | ISO 23903:2021 |
| **CIM** | Clinical Information Model | ISO-13972-Begriff (löste DCM ab) | ISO 13972 |
| **DCM** | Detailed Clinical Model | Vorgänger-Begriff zu CIM | ISO/TS 13972 (2010, abgelöst) |
| **RIM** | Reference Information Model | HL7 V3 / CDA Basis-Modell | hl7.org/implement/standards |
| **HSRA** | Health Services Reference Architecture | HL7 Cross Paradigm Specification, Edition 1 | hl7.org HSRA STU 09/2023 |
| **FHIR** | Fast Healthcare Interoperability Resources | HL7-Standard für moderne Interoperabilität | hl7.org/fhir |
| **FSH** | FHIR Shorthand | Authoring-Sprache für FHIR-Profile / -Logical-Models | hl7.org/fhir/uv/shorthand/ |
| **Logical Model** | — | FHIR `StructureDefinition.kind = logical`: Strukturdefinition jenseits konkreter Resources | hl7.org/fhir/logical.html |
| **EHDS-Pattern** | European Health Data Space — Modellierungs-Konvention | Logical Model mit `Parent: Base`, alle Felder als reguläre Sub-Elemente, ohne Extensions | xt-ehr.eu/fhir/models/; EU 2025/327 |
| **BackboneElement** | — | FHIR-Datentyp für nested Container ohne eigene Resource-Identität | hl7.org/fhir/backboneelement.html |
| **Profile** | — | FHIR-Constraint auf einer existierenden Resource | hl7.org/fhir/profiling.html |
| **Extension** | — | FHIR-Erweiterungs-Mechanismus über `extension[].valueX` | hl7.org/fhir/extensibility.html |
| **ValueSet / CodeSystem** | — | FHIR-Terminologie-Bindings | hl7.org/fhir/valueset.html |

## 15 Empfehlungsgrade (Leitlinien)

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **A** | Soll-Empfehlung | Starke Empfehlung (positive/negative Handlungsanweisung) | AWMF-Regelwerk Leitlinien |
| **B** | Sollte-Empfehlung | Empfehlung | AWMF-Regelwerk |
| **0** | Kann-Empfehlung | Offene Empfehlung | AWMF-Regelwerk |
| **EK** | Konsensbasierte Expertenempfehlung | Kein Evidenzlevel zugeordnet | AWMF-Regelwerk |
| **Statement** | — | Feststellung ohne Handlungs-Empfehlung | AWMF-Regelwerk |

## 16 Evidenzlevel (S3-LL-Konvention nach Oxford CEBM)

| Level | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **1a** | Systematic Review of RCTs | Systematische Übersichtsarbeit randomisierter Studien | Oxford CEBM Levels of Evidence |
| **1b** | Individual RCT | Einzelne randomisierte Studie | Oxford CEBM |
| **2a** | Systematic Review of Cohort Studies | Systematische Übersicht von Kohortenstudien | Oxford CEBM |
| **2b** | Individual Cohort / Low-quality RCT | Einzelne Kohortenstudie / RCT geringer Qualität | Oxford CEBM |
| **3** | Case-Control Studies | Fall-Kontroll-Studien | Oxford CEBM |
| **4** | Case Series / poor cohort / case-control | Fallserien / qualitativ schwache Studien | Oxford CEBM |
| **5** | Expert Opinion | Expertenmeinung | Oxford CEBM |

## 17 ePA / DSF / DiGA / Versorgungs-Akronyme (DE)

| Akronym | Bedeutung | Beschreibung | Quelle |
| --- | --- | --- | --- |
| **GKV / PKV** | Gesetzliche / Private Krankenversicherung | Zwei Säulen des deutschen Krankenversicherungs-Systems | SGB V / VVG |
| **DRG** | Diagnosis Related Groups | Pauschalierungs-System der Krankenhausvergütung; G-DRG = Deutsche Variante | InEK; KHEntgG |
| **OPS** | Operationen- und Prozedurenschlüssel | DE-Pendant zu CPT/HCPCS; jährliche BfArM-Update | BfArM OPS 2026 |
| **EBM** | Einheitlicher Bewertungsmaßstab | Vertragsärztliche Abrechnung GKV | KBV.de/EBM |
| **DIZ** | Datenintegrationszentrum | MII-Standortinfrastruktur an Universitätskliniken | medizininformatik-initiative.de |
| **BMG** | Bundesministerium für Gesundheit | Oberste Bundesbehörde | bundesgesundheitsministerium.de |
| **BfArM** | Bundesinstitut für Arzneimittel und Medizinprodukte | Zulassung Arzneimittel/Medizinprodukte; Klassifikations-Herausgeber (ICD, OPS, DiGA) | bfarm.de |
| **GKV-SV** | GKV-Spitzenverband | Spitzenorganisation der gesetzlichen Krankenkassen | gkv-spitzenverband.de |
| **DKG** | Deutsche Krebsgesellschaft | Wissenschaftliche Fachgesellschaft Onkologie | krebsgesellschaft.de |
| **DKH** | Deutsche Krebshilfe (Stiftung) | Förderorganisation; Co-Träger Leitlinienprogramm | krebshilfe.de |
| **AWMF** | Arbeitsgemeinschaft der Wissenschaftlichen Medizinischen Fachgesellschaften | Dachverband; Leitlinien-Register | awmf.org |
| **DGHO** | Deutsche Gesellschaft für Hämatologie und Medizinische Onkologie | Wiss. Fachgesellschaft; Träger Onkopedia | dgho.de; onkopedia.com |

## 18 Verifikations-Status

| Kategorie | Verifikation | Anmerkung |
| --- | --- | --- |
| ISO-Normen-Nummern (13606/13940/13972/21090/23903) | ✓ verifiziert | Stand: aktuelle Editions im DIN-/ISO-Katalog |
| OIDs (KDL `1.2.276.0.76.5.451`; ICD-O-3 `2.16.840.1.113883.6.43.1`; MedDRA `2.16.840.1.113883.6.163`) | ✓ verifiziert | offizielle DVMD-/HL7-Registry |
| Score-Bereiche (PHQ-9, HADS, Zarit, NRS, EORTC, ECOG, Karnofsky) | ✓ stichprobenartig verifiziert | Zarit per Web-Lookup bestätigt; übrige aus Primärpublikation |
| RECIST 1.1 (CR/PR/SD/PD/NE) | ✓ verifiziert | Eisenhauer 2009 |
| CTCAE-Grade 1–5 | ✓ verifiziert | NCI-Standard |
| LL-Empfehlungs-Verweise (S3-LL Lung v5.01, S3-LL Palliativ v3.01) | ✓ verifiziert | direkter Bezug zu im Audit-Log dokumentierten Quellen |
| SNOMED-CT-IDs (in Codings-Tabellen ggf. erwähnt) | ⚠ teilweise verifiziert | vollständige Terminologie-Server-Validierung steht aus (siehe `verification-log.md` §5) |
| LOINC-Codes (Score-Instrumente) | ⚠ teilweise verifiziert | Stichprobenverifikation; finale Liste über LOINC-Browser empfohlen |
| Genetische Marker / Drug-Indications | ✓ aus Onkopedia/NEJM-Primärquellen | Stand der aktuellen Onkologie-Leitfäden |
| Frequenz-Code-Pattern | ✓ projekt-eigene Konvention | dokumentiert in §11 + `docs/design-faq.md` |

**Bei Aktualisierungen:** Der `data-element-validator`-Sub-Agent prüft pro Lauf, ob die hier aufgeführten LL-/Standard-Versionen noch aktuell sind, und schlägt Updates vor.

## Pflege

Dieses Glossar wird durch den `data-element-analyzer`-Sub-Agenten gepflegt: Bei jedem Lauf werden neue Begriffe in YAML-Inhalten / Codings / Kommentaren auf Aufnahme geprüft. Manuelle Ergänzungen jederzeit möglich; Änderungen sollten im `docs/verification-log.md` als Audit-Eintrag dokumentiert werden.
