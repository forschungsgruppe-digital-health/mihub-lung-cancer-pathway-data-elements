# Screening-Episode — Vorbereitung der Datenelement-Erhebung

Lungenkrebs-Früherkennung mit Niedrigdosis-CT (LuKrFrühErkV, G-BA KFE-RL Abschnitt D.III) als Phase `screening`
des Katalogs. Dieser Ordner enthält die Arbeitsgrundlage für die Erhebung 2026-10/11; im Katalog
(`elements/screening/`) stehen noch keine Elemente.

| Datei | Inhalt | Für wen |
| --- | --- | --- |
| [`dossier.md`](dossier.md) | Quellenverzeichnis (54 Quellen), Prozessschritt → Datenelement-Matrix entlang des BPMN-Modells, 53 geprüfte Kandidaten mit Einzelblättern (Definition, Fundstellen mit Zitat, Verbindlichkeit, Codes, Bezug zum Bestand), verworfene Kandidaten mit Begründung, Umsetzungsvorschlag (U1–U10), Entscheidungsfragen (E1–E24), offene Punkte | alle |
| [`datenelement-erhebung-screening.xlsx`](datenelement-erhebung-screening.xlsx) | Vorbefüllte Erhebungsmappe (Vorlage des Repos): Zeilen DE-S01 … DE-S53 entsprechen den Einzelblättern Nr. 1–53 des Dossiers | klinische Expert:innen |
| [`quellen.json`](quellen.json) | Maschinenlesbares Quellenverzeichnis mit Prüfvermerk und zitierenden Kandidaten | MI-Team |

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

## Stand und Grenzen

- Rechtsgrundlagen: LuKrFrühErkV vom 15.05.2024 (in Kraft 01.07.2024); KFE-RL Abschnitt D.III (§§ 37–46, Fassung
  18.12.2025, in Kraft 12.03.2026); Abrechnung nach EBM seit 01.04.2026. Leitlinie: S3-LL Lungenkarzinom 5.1, Kap. 5.
- Recherche und Gegenprüfung sind KI-gestützt (sechs Recherche-Perspektiven, je Kandidat zwei unabhängige Skeptiker;
  Methode im Anhang des Dossiers, Offenlegung in [`AI_USAGE.md`](../../AI_USAGE.md)). Das klinische Review steht aus.
- Codes wurden in der Recherche überwiegend über tx.fhir.org geprüft (SNOMED CT INT 20250201, LOINC 2.82). Vor der
  Aufnahme in den Katalog sind alle Codes gegen den MII TermServ zu prüfen (Dossier, Abschnitt 8.2).
- Raucheranamnese ist ein Querschnittsthema: Die sieben Bausteine der Gruppe G2 sollen später auch Behandlung und
  Nachsorge dienen (`smokingStatus` im Bestand wird spezialisiert, nicht dupliziert).
