# AGENTS.md

Dieses Repository stellt drei spezialisierte Sub-Agenten bereit, die in **Anthropic Claude Code**, **OpenAI Codex CLI** und vergleichbaren agentischen Tools auto-erkannt werden können.

> Format-Hinweis: Die hier dokumentierten Agenten sind in `.claude/agents/<name>.md` (Anthropic-Format mit YAML-Frontmatter) hinterlegt und werden zusätzlich in dieser AGENTS.md (OpenAI-/Codex-CLI-Konvention) beschrieben. Beide Konventionen verweisen auf dieselben System-Prompts.

## Verbindliche Regeln für alle Agenten

1. **Keine eigenständigen Änderungen am Datenbestand.** Vor jeder Änderung an Schema, YAML-Datenelementen, CodeSystems/ValueSets oder Doku ist die explizite Zustimmung der Nutzer:in einzuholen — **datenelementweise** bei inhaltlichen Änderungen.
2. **Web-Recherche-Pflicht.** Bei jeder Aufgabe prüfen, ob für die referenzierten Standards / Leitlinien / Codes neuere Versionen verfügbar sind. Neue Standards werden nur nach Zustimmung der Nutzer:in in `MiHUBStandardsCS` aufgenommen; bestehende Datenelemente werden anschließend systematisch auf Anwendbarkeit geprüft.
3. **Audit-Pflicht.** Jede ausgeführte Aktion ist im `docs/audit-log.md` als neuer Eintrag zu dokumentieren (Element-ID, Änderungstyp, Quelle, Begründung, Datum).
4. **Doku-Konsistenz-Pflicht.** Vor Beendigung jeder Aufgabe prüfen, ob `README.md`, `docs/methodology.md`, `docs/phases-overview.md` und `docs/audit-log.md` mit dem Ergebnis konsistent sind (Element-Zähler, Versionen, Standards-Listen, Cross-References). Bei Inkonsistenz: korrigieren.
5. **Glossar-Pflicht.** Vor Beendigung jeder Analyzer-/Validator-Aufgabe prüfen, ob alle in den geänderten Datenelementen vorkommenden Akronyme, Skalen, Frequenz-Codes, Standard-Identifier oder klinischen Konzepte in `GLOSSARY.md` enthalten sind. Fehlende Begriffe pro Eintrag mit `AskUserQuestion` zur Aufnahme vorlegen.
5. **Read-only-Default.** Die Standardrechte sind Lesen + Web-Recherche. Schreibrechte (Edit/Write/Bash) erst nach explizitem User-Approval pro Operation.

## Agenten-Übersicht

| Name | Datei | Zweck |
| --- | --- | --- |
| [`data-element-analyzer`](.claude/agents/data-element-analyzer.md) | `.claude/agents/data-element-analyzer.md` | Analysiert bereitgestellte Dokumente (Leitlinien, Onkopedia-Updates, Standard-Spezifikationen, Veröffentlichungen) auf neue, zu ergänzende oder veraltete Datenelemente. Konsultiert die Nutzer:in **datenelementweise** vor jeder Änderung. |
| [`data-element-validator`](.claude/agents/data-element-validator.md) | `.claude/agents/data-element-validator.md` | Verifiziert neue oder geänderte YAML-Datenelemente, prüft Codings (Schema-Konformität, plausible Coding-Systeme, Web-Lookup bei Unsicherheit), erzeugt anschließend `catalog/data-dictionary.csv` und optional die FHIR-Logical-Model-Artefakte neu. |
| [`ai-usage-curator`](.claude/agents/ai-usage-curator.md) | `.claude/agents/ai-usage-curator.md` | Pflegt die KI-Nutzungs-Disklosure (`AI_USAGE.md`) gemäß EU AI Act Art. 50, COPE und einschlägigen Community-Standards. Erkennt werkzeug-/governance-bezogene Trigger-Ereignisse (neue Modell-Releases, Maintainer-Wechsel, neue Sub-Agenten, geschlossene Backlog-Items, EU-Guidance-Aktualisierungen) und konsultiert die Nutzer:in vor jeder Änderung. Kümmert sich auch um Cross-Konsistenz mit README-Badge, `CONTRIBUTING.md`, PR-Template. |

### Trennung der Konzerne (Separation of Concerns)

Die drei Agenten haben **disjunkte Zuständigkeiten** und beeinflussen sich nur über einen leichten Hinweis-Mechanismus (kein automatischer gegenseitiger Aufruf):

| Agent | Konzern | Trigger | Hauptdatei(en) |
|---|---|---|---|
| `data-element-analyzer` | klinisch-inhaltlich (neue Quellen → neue/aktualisierte Datenelemente) | neue LL-/Onkopedia-Version, Stakeholder-Workshop-Ergebnisse, neue Publikation | `elements/`, `audit-log.md` (inhaltliche Belege) |
| `data-element-validator` | technisch-konsistenz (YAMLs valide, Codings plausibel, Sichten regeneriert) | nach jedem Analyzer-Lauf oder bei manueller Element-Änderung | `elements/`, `catalog/`, `derived/`, `audit-log.md` (Validator-Lauf) |
| `ai-usage-curator` | werkzeug-/governance-bezogen (KI-Nutzungs-Disklosure aktuell halten) | neuer Modell-Release, Maintainer-Wechsel, neuer Sub-Agent, EU-Guidance-Update, Backlog-Erledigung | `AI_USAGE.md`, `audit-log.md` (Curator-Lauf), ggf. README-Badge / CONTRIBUTING / PR-Template |

Analyzer und Validator dürfen am Ende ihres Laufs einen **Hinweis** ausgeben, wenn sie ein Curator-Trigger-Ereignis bemerken (z. B. ein neues Modell wurde verwendet) — sie starten den Curator aber nicht selbst. Die Entscheidung über den Curator-Lauf bleibt bei der Nutzer:in.

## Aufruf

### Anthropic Claude Code

```bash
# Im Projekt-Root (data-elements/) ausführen
claude
> /agents data-element-analyzer "Analysiere LL-Lungenkarzinom v4.1 (Konsultationsfassung 2026)"
```

oder durch direkten `Agent`-Tool-Aufruf mit `subagent_type: "data-element-analyzer"`.

### OpenAI Codex CLI / Vergleichbare Tools

Tools, die die `AGENTS.md`-Konvention unterstützen, lesen diese Datei beim Start und stellen die hier gelisteten Agenten als auswählbare Workflows bereit. Die System-Prompts liegen unter `.claude/agents/*.md` (YAML-Frontmatter + Markdown-Body) und sind direkt einlesbar.

### Manuelles Ausführen ohne Agenten-Framework

Die Agent-Definitionen sind als **System-Prompts** formuliert. In Tools ohne native Sub-Agent-Unterstützung kann der Inhalt der jeweiligen `.claude/agents/<name>.md` (alles unterhalb des YAML-Frontmatters) als System-Prompt geladen werden; das gewünschte Eingabedokument bzw. die Element-Liste folgt im User-Turn.

## Repository-Konventionen

- **Single Source of Truth:** YAML pro Datenelement unter `elements/<phase>/*.yaml`
- **Auto-generiert** (nicht manuell editieren): `catalog/data-dictionary.csv`, `docs/phases-overview.md`, alles unter `derived/`
- **Schema:** `schemas/data-element.schema.json`
- **Validierung:** `python scripts/validate.py`
- **Aggregation:** `python scripts/build-catalog.py`
- **FHIR-Generation (optional):** `python scripts/build-fhir-logical-models.py`

Allgemeine Beitrags-Regeln: siehe [`CONTRIBUTING.md`](CONTRIBUTING.md). Zwei Beitrags-Spuren (Klinik / MI): [`docs/howto-add-element.md`](docs/howto-add-element.md).

## KI-Nutzungs-Disklosure

Dieses Repository wird KI-unterstützt gepflegt — die vollständige, EU-AI-Act-/COPE-konforme Disclosure liegt in [`AI_USAGE.md`](AI_USAGE.md) (Werkzeuge, Modellversionen, Verantwortliche, Prüfprozess, Maschinenlesbare Kennzeichnung, Nicht-Nutzung, Rechtsgrundlagen). Inhalte sind als Author Draft zu betrachten und vor produktivem Einsatz klinisch zu reviewen.

Die Pflege der Disclosure erfolgt über den [`ai-usage-curator`](.claude/agents/ai-usage-curator.md)-Sub-Agenten.
