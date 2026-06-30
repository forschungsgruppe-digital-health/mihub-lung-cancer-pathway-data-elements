# AGENTS.md — MiHUB Lungenkrebs-Datenelemente

Operativer Kontext für KI-Coding-Agenten (Anthropic Claude Code, OpenAI Codex CLI, Cursor,
Gemini CLI, GitHub Copilot u. a.). **Diese Datei ist die kanonische, vendor-neutrale Quelle.**
Claude Code liest sie zusätzlich über `CLAUDE.md`; GitHub Copilot über
[`.github/copilot-instructions.md`](.github/copilot-instructions.md) (dünne Brücke hierher).
Bei Widerspruch gewinnt diese Datei.

## Projekt

Versionierbares Repository der klinischen **Datenelemente** entlang des Lungenkrebs-Patienten-
pfads (NSCLC/SCLC) im Projekt **MiHUB** (TU Dresden / Forschungsgruppe Digital Health), erhoben
in den Use-Case-Arbeitspaketen AP6/AP7/AP8 mit Bezug zum BPMN-Pfad aus AP3
([`mihub-lung-cancer-pathway`](https://github.com/forschungsgruppe-digital-health/mihub-lung-cancer-pathway)).
Initial befüllt: Nachsorge (`followup`), Surveillance, Palliativ — **51 Datenelemente**.

## Repository-Konventionen

- **Einzige Quelle (SSoT):** ein YAML je Datenelement unter `elements/<phase>/*.yaml`.
- **Auto-generiert (nicht von Hand editieren):** `catalog/data-dictionary.csv` + `.md`,
  `docs/phases-overview.md`, alles unter `derived/`.
- **Schema:** `schemas/data-element.schema.json` (ISO 13972:2022 / ISO 13606-2 / HL7 HSRA).
- **Validierung:** `python scripts/validate.py` · **Aggregation:** `python scripts/build-catalog.py`
  · **FHIR (optional):** `python scripts/build-fhir-logical-models.py`.
- **Branching:** Beiträge per Pull Request gegen **`dev`** (Integrations-/Review-Branch);
  **`main`** ist die Release-Branch. Nicht direkt auf `main` pushen, nicht selbst mergen.
- **Drei Beitrags-Spuren** (siehe [`CONTRIBUTING.md`](CONTRIBUTING.md)): GitHub-Issue-Formular ·
  Excel-Vorlage (`templates/`) · YAML+PR. Neue Kandidaten **vor Aufnahme** auf Dubletten prüfen
  (`scripts/check-duplicates.py` bzw. Skill `check-duplicate-data-element`).

## Verbindliche Regeln für alle Agenten

1. **Keine eigenständigen Änderungen am Datenbestand.** Vor jeder Änderung an Schema, YAML,
   CodeSystems/ValueSets oder Doku die explizite Zustimmung der Nutzer:in einholen —
   **datenelementweise** bei inhaltlichen Änderungen.
2. **Web-Recherche-Pflicht.** Bei jeder Aufgabe prüfen, ob referenzierte Standards/Leitlinien/
   Codes neuere Versionen haben. Neue Standards nur nach Zustimmung aufnehmen, dann den Bestand
   systematisch auf Anwendbarkeit prüfen.
3. **Audit-Pflicht.** Jede ausgeführte Aktion in `docs/audit-log.md` dokumentieren (Element-ID,
   Änderungstyp, Quelle, Begründung, Datum).
4. **Doku-Konsistenz-Pflicht.** Vor Abschluss prüfen, ob `README.md`, `docs/methodology.md`,
   `docs/phases-overview.md`, `docs/audit-log.md` konsistent sind (Zähler, Versionen, Standards,
   Cross-References) — sonst korrigieren.
5. **Glossar-Pflicht.** Neue Akronyme/Skalen/Frequenz-Codes/Standard-Identifier/klinische
   Konzepte der geänderten Elemente in `GLOSSARY.md` ergänzen (per `AskUserQuestion`).
6. **Read-only-Default.** Standardrechte sind Lesen + Web-Recherche; Schreibrechte erst nach
   explizitem Approval pro Operation. **Keine `git`-Operationen** durch Agenten.

## Agent capabilities (vendor-neutral catalog)

Die spezialisierten Fähigkeiten dieses Repos liegen als **portable Agent Skills** in
[`skills/`](skills) (offener agentskills.io-Standard) — das ist die **einzige Quelle**. Jedes
Werkzeug entdeckt sie an seinem eigenen Pfad; alle werkzeugspezifischen Dateien verweisen nur
hierher (Details: [`skills/SKILLS_SETUP.md`](skills/SKILLS_SETUP.md)). Wo ein Werkzeug die native
Primitive nicht hat (z. B. Copilot kann keinen Sub-Agenten aufrufen), die **Rolle inline ausführen**.

| Skill | Zweck | Trigger | Modus |
| --- | --- | --- | --- |
| [`data-element-analyzer`](skills/data-element-analyzer/SKILL.md) | Dokumente (Leitlinien, Onkopedia, Publikationen) → neue/aktualisierte/veraltete Datenelemente vorschlagen | neue LL-/Onkopedia-Version, Stakeholder-Workshop, Publikation | read-only, datenelementweise Konsultation |
| [`data-element-validator`](skills/data-element-validator/SKILL.md) | YAML verifizieren (Schema, Codings, Konsistenz), Catalog + FHIR-Modell regenerieren | nach Analyzer-Lauf oder manueller Element-Änderung | schreibt nach Zustimmung |
| [`check-duplicate-data-element`](skills/check-duplicate-data-element/SKILL.md) | neue Kandidaten (Issue / Excel / YAML) auf Dubletten/Ähnlichkeit prüfen — vor Aufnahme | neues Issue, ausgefüllte Excel-Mappe, neue YAMLs | read-only, Konsultation vor Merge |
| [`ai-usage-curator`](skills/ai-usage-curator/SKILL.md) | KI-Nutzungs-Disklosure `AI_USAGE.md` pflegen (EU AI Act Art. 50, COPE) | neues Modell/Werkzeug/Sub-Agent, Governance-Trigger | read-only-Default, Konsultation |

### Wie jedes Werkzeug die Capabilities konsumiert

- **Claude Code** — Skills via `.claude/skills/<name>` (Symlinks → `../../skills/<name>`);
  zusätzlich als Sub-Agenten via `.claude/agents/<name>.md` (Symlinks → `../../skills/<name>/SKILL.md`,
  **dieselbe** Quelle). Aufruf: `Agent`-Tool mit `subagent_type: "<name>"` oder Skill-Trigger.
- **OpenAI Codex / Cursor / Gemini CLI** — Skills via `.codex/skills/<name>` (Symlinks) bzw. den
  werkzeugeigenen Skills-Pfad; alternativ diese `AGENTS.md` lesen und die Rolle inline ausführen.
- **GitHub Copilot** — liest das `SKILL.md`-Format nicht; gebrückt über
  [`.github/copilot-instructions.md`](.github/copilot-instructions.md) → diese `AGENTS.md`.
  Workflow inline ausführen.

Validierung der Konsistenz (Frontmatter, `name`==Verzeichnis, Symlinks, Sub-Agenten, Copilot-
Brücke): `python3 .github/scripts/validate-agent-skills.py` (CI: `.github/workflows/skill-lint.yml`).

### Trennung der Zuständigkeiten (Separation of Concerns)

| Skill | Konzern | Hauptdatei(en) |
| --- | --- | --- |
| `data-element-analyzer` | klinisch-inhaltlich (Quellen → Elemente) | `elements/`, `audit-log.md` |
| `data-element-validator` | technische Konsistenz (valide, Codings, Sichten) | `elements/`, `catalog/`, `derived/`, `audit-log.md` |
| `check-duplicate-data-element` | Eingangskontrolle (Dubletten vor Aufnahme) | `elements/_incoming/`, `audit-log.md` (read-only) |
| `ai-usage-curator` | Werkzeug/Governance (KI-Disклosure) | `AI_USAGE.md`, `audit-log.md`, README-Badge |

Die Skills rufen sich **nicht** gegenseitig auf; sie geben am Ende höchstens einen Hinweis aus
(z. B. „Curator-Lauf empfehlenswert"). Die Entscheidung über Folgeläufe bleibt bei der Nutzer:in.

## KI-Nutzungs-Disklosure

Dieses Repository wird KI-unterstützt gepflegt — vollständige, EU-AI-Act-/COPE-konforme
Disclosure in [`AI_USAGE.md`](AI_USAGE.md). Inhalte sind **Author Draft** und vor produktivem
Einsatz klinisch zu reviewen. Zweckbestimmung/Haftung: [`DISCLAIMER.md`](DISCLAIMER.md).
