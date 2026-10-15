# Screening-Episode — Vorbereitung der Datenelement-Erhebung

Lungenkrebs-Früherkennung mit Niedrigdosis-CT (LuKrFrühErkV, G-BA KFE-RL Abschnitt D.III) als Phase `screening`
des Katalogs. Dieser Ordner enthält die Arbeitsgrundlage für die Erhebung 2026-10/11; im Katalog
(`elements/screening/`) stehen noch keine Elemente.

| Datei | Inhalt | Für wen |
| --- | --- | --- |
| [`dossier.md`](dossier.md) | Quellenverzeichnis (54 Quellen), Prozessschritt → Datenelement-Matrix entlang des BPMN-Modells, 53 geprüfte Kandidaten mit Einzelblättern (Definition, Fundstellen mit Zitat, Verbindlichkeit, Codes, Bezug zum Bestand), verworfene Kandidaten mit Begründung, Umsetzungsvorschlag (U1–U10), Entscheidungsfragen (E1–E24), offene Punkte | alle |
| [`datenelement-erhebung-screening.xlsx`](datenelement-erhebung-screening.xlsx) | Vorbefüllte Erhebungsmappe (Vorlage des Repos): Zeilen DE-S01 … DE-S53 entsprechen den Einzelblättern Nr. 1–53 des Dossiers | klinische Expert:innen |
| [`entwuerfe/`](entwuerfe/) | **53 schema-valide YAML-Entwürfe** (je Kandidat ein Datenelement): Definition, Datentyp, MII-TermServ-geprüfte Codes, Profilziele über alle Standards, Quellenangaben mit wörtlichem Zitat und URL, Herkunft (`provenance.origin`), Prüfvermerke (`provenance.verification`) und offene Punkte | MI-Team, Review |
| [`quellen.json`](quellen.json) | Maschinenlesbares Quellenverzeichnis mit Prüfvermerk und zitierenden Kandidaten (`locator` der Entwürfe verweist auf die Q-ID) | MI-Team |
| [`pruefprotokoll.json`](pruefprotokoll.json) | Prüfprotokoll je Kandidat: Urteile der Gegenprüfung (Quelle, Dublette/Scope) mit Begründung, alle Code- und Profilvorschläge mit Skeptiker-Urteil, Änderungen bei der Zusammenführung | Review, Audit |

## Ablauf der Erhebung

1. Mappe öffnen, Blatt »Anleitung« lesen.
2. Je gelb hinterlegter Zeile: bestätigen, korrigieren oder streichen (in »Anmerkungen« `STREICHEN` eintragen). Fehlende Elemente in den freien Zeilen ergänzen.
3. Die Entscheidungsfragen des eigenen Fachgebiets beantworten (Dossier, Abschnitt 7):
   E1–E11 berichterstellende Praxis (Allgemein-, Innere, Arbeitsmedizin) · E12–E17 Radiologie (Erst- und Zweitbefunder) ·
   E18–E20 Datenschutz, Justiziariat, Qualitätssicherung · E21–E24 Modellierung (MI-Team).
4. Rückgabe an das MI-Team. Import und Prüfung wie bei jeder Erhebung:
   `scripts/import-elicitation-workbook.py <mappe> --out <ordner> --validate`, danach `scripts/check-duplicates.py --candidates <ordner>`
   und `scripts/verify-terminology.py` gegen den MII TermServ; Aufnahme nach `elements/screening/` per Pull Request (siehe
   [`docs/howto-add-element.md`](../howto-add-element.md)).

## Codes, Profile und Herkunft (Stand 2026-10-15)

- **Codes:** am MII TermServ ermittelt (Lookup/Expand), von einer Skeptiker:in gegengeprüft, Teilkorrekturen zusammengeführt und abschließend per `scripts/verify-terminology.py` geprüft: **355 Codings, davon 294 aus Standardterminologien — alle gefunden und aktiv** (SNOMED CT 20260701, LOINC 2.83, DICOM DCM, RadLex 4.2, KDL, OPS, NCIt, HL7) und 61 lokale Platzhalter dort, wo es keinen Standardcode gibt (Konzeptbedarf in `issues`). Die Rolle jedes Codes (Element-Code, Antwortwert, Methode, Dokumentklasse) steht in `value_set.notes`.
- **Profile:** über alle Standards zugeordnet, nicht nur MII KDS: 301 Ziele (MII KDS 85, ISiK 28 — u. a. `ISiKRaucherStatus`, `ISiKLebensZustand`, `ISiKProzedur`, `ISiKBerichtSubSysteme` —, FHIR-Basis 32, IPS/Basisprofil DE und weitere unter `other`, DICOM SR 14, openEHR 33, KBV MIO 5, gematik ePA 5, IHE 5, mCODE 5). Alle **214 FHIR-Canonicals existieren** als StructureDefinition in den publizierten Paketen (maschinell geprüft); Nur-Ballot-Profile sind in `notes` gekennzeichnet.
- **Herkunft:** jede Quellenangabe trägt ein wörtliches Zitat — **151/151** maschinell gegen die beschafften Quelltexte geprüft —, die URL und die Q-ID aus `quellen.json`; `provenance.origin` nennt Dossier-Nummer, Prozessgruppe, BPMN-Schritt und die zusammengeführten Rohkandidaten; `provenance.verification` die Prüfläufe mit Ergebnis.

## Stand und Grenzen

- Rechtsgrundlagen: LuKrFrühErkV vom 15.05.2024 (in Kraft 01.07.2024); KFE-RL Abschnitt D.III (§§ 37–46, Fassung
  18.12.2025, in Kraft 12.03.2026); Abrechnung nach EBM seit 01.04.2026. Leitlinie: S3-LL Lungenkarzinom 5.1, Kap. 5.
- Recherche und Gegenprüfung sind KI-gestützt (sechs Recherche-Perspektiven, je Kandidat zwei unabhängige Skeptiker;
  Methode im Anhang des Dossiers, Offenlegung in [`AI_USAGE.md`](../../AI_USAGE.md)). Das klinische Review steht aus.
- Die Code-Angaben im Dossier stammen aus der Recherche (tx.fhir.org); maßgeblich sind die am MII TermServ geprüften Codes der Entwürfe.
- Raucheranamnese ist ein Querschnittsthema: Die sieben Bausteine der Gruppe G2 sollen später auch Behandlung und
  Nachsorge dienen (`smokingStatus` im Bestand wird spezialisiert, nicht dupliziert).
