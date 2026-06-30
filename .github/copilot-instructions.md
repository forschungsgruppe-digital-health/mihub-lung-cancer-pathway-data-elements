# GitHub Copilot — Repository-Instruktionen (MiHUB Lungenkrebs-Datenelemente)

> **Kanonische Quelle: [`AGENTS.md`](../AGENTS.md).** Diese Datei ist nur die GitHub-Copilot-
> Brücke dorthin (Copilot liest `AGENTS.md` nicht automatisch). Inhalte nicht duplizieren;
> bei Widerspruch gewinnt `AGENTS.md` — dann diese Datei korrigieren.

## Worum es geht
Versionierbares Repository der klinischen **Datenelemente** entlang des Lungenkrebs-Patienten-
pfads (MiHUB, AP6/7/8). **YAML pro Element** unter `elements/<phase>/*.yaml` ist die *einzige
Quelle*; CSV/Markdown/FHIR-Sichten werden daraus generiert. Schema:
[`schemas/data-element.schema.json`](../schemas/data-element.schema.json) (ISO 13972/13606).

## Harte Grenzen — NIE tun
- **Keine personenbezogenen / realen Patientendaten** ins Repo oder in Prompts — nur abstrakte
  Datenelement-Definitionen.
- **Auto-generierte Dateien nicht von Hand editieren:** `catalog/data-dictionary.csv` + `.md`,
  `docs/phases-overview.md`, alles unter `derived/`. Stattdessen `python scripts/build-catalog.py`.
- **Klinische Freigabe (`publication_status`) nicht autonom heben** (AuthorDraft → … →
  ApprovedForProductionUse ist menschliche/klinische Entscheidung).
- **Schema-Enums (Phase, Standards, Datentypen …) nicht stillschweigend ändern** — additiv +
  begründet; bestehende 51 YAMLs müssen gültig bleiben.

## Qualitäts-Gate (eine Änderung ist erst fertig, wenn das grün ist)
- `python scripts/validate.py` — alle YAMLs gegen das JSON-Schema (CI-erzwungen).
- `python scripts/build-catalog.py` — Catalog regenerieren + committen (CI prüft Drift).
- Conventional Commits. Pro PR möglichst **ein** Datenelement (atomare Reviews).
- **Branching:** PR gegen `dev`; `main` ist die Release-Branch — nie direkt pushen / selbst mergen.

## Drei Beitrags-Spuren (siehe [`CONTRIBUTING.md`](../CONTRIBUTING.md))
1. **GitHub-Issue-Formular** (Klinik, niederschwellig, online).
2. **Excel-Vorlage** (`templates/datenelement-erhebung.xlsx`; ohne Git/YAML) →
   `scripts/import-elicitation-workbook.py` erzeugt YAML-Entwürfe.
3. **YAML + Pull Request** (technisch).
Neue Kandidaten **vor Aufnahme** auf Dubletten prüfen: `python scripts/check-duplicates.py`.

## Wiederverwendbare Agenten-Fähigkeiten (hier entdecken, inline ausführen)
Die Capabilities liegen als portable **Agent Skills** in [`skills/`](../skills) (agentskills.io).
Copilot kann sie nicht *aufrufen*, soll aber den Workflow **inline** ausführen, wenn eine Aufgabe
passt. Vollständiger vendor-neutraler Katalog: **`AGENTS.md` → „Agent capabilities"**. Kurz:
- **`data-element-analyzer`** — neue Leitlinien/Publikationen → Vorschläge (read-only, Konsultation).
- **`data-element-validator`** — YAML-/Codings-/Konsistenz-Prüfung, Catalog-Regeneration.
- **`check-duplicate-data-element`** — Dubletten-/Ähnlichkeitsprüfung neuer Kandidaten (read-only).
- **`ai-usage-curator`** — pflegt `AI_USAGE.md` (EU AI Act Art. 50).

## Zuerst nachschlagen
[`README.md`](../README.md) · [`docs/howto-add-element.md`](../docs/howto-add-element.md) ·
[`docs/methodology.md`](../docs/methodology.md) · [`AGENTS.md`](../AGENTS.md) · Zweckbestimmung/
Haftung: [`DISCLAIMER.md`](../DISCLAIMER.md).
