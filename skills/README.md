# Agent Skills — eine Quelle, von jedem Werkzeug konsumiert

Dieses Verzeichnis ist die **einzige Quelle** (single source of truth) für die
werkzeug-unabhängigen [Agent Skills](https://agentskills.io/specification) dieses
Repositorys. Jede `skills/<name>/SKILL.md` trägt YAML-Frontmatter (`name`, `description`
+ die Claude-Erweiterungsfelder `tools`/`model`, die andere Werkzeuge ignorieren) und
Markdown-Anweisungen. Werkzeuge entscheiden anhand der `description`, wann ein Skill greift.
**Alle werkzeugspezifischen Dateien verweisen nur hierher — niemals den Skill-Body kopieren.**

| Skill | Wann es greift | Wesen |
| --- | --- | --- |
| [`data-element-analyzer`](data-element-analyzer/SKILL.md) | neue Leitlinie/Onkopedia/Publikation → neue/aktualisierte/veraltete Datenelemente | read-only Analyse, datenelementweise Konsultation |
| [`data-element-validator`](data-element-validator/SKILL.md) | nach Analyzer-Lauf oder manueller Element-Änderung | Schema-/Codings-/Konsistenz-Prüfung, regeneriert Catalog |
| [`check-duplicate-data-element`](check-duplicate-data-element/SKILL.md) | neues Issue / ausgefüllte Excel-Mappe / neue YAMLs | Dubletten-/Ähnlichkeits-Prüfung vor Aufnahme (read-only) |
| [`ai-usage-curator`](ai-usage-curator/SKILL.md) | neues Modell/Werkzeug/Sub-Agent, Governance-Trigger | pflegt `AI_USAGE.md` (EU AI Act Art. 50) |

## Wie jedes Werkzeug diese Skills konsumiert

- **Anthropic Claude Code** — Skills via `.claude/skills/<name>` (Symlinks → `../../skills/<name>`);
  zusätzlich als Sub-Agenten via `.claude/agents/<name>.md` (Symlinks → `../../skills/<name>/SKILL.md`,
  dieselbe Quelle). Kein Kopieren, keine Duplikate.
- **OpenAI Codex / Cursor / Gemini CLI** — Skills via `.codex/skills/<name>` (Symlinks → `../../skills/<name>`)
  bzw. der werkzeugeigene Skills-Pfad; alternativ lesen sie die [`AGENTS.md`](../AGENTS.md).
- **GitHub Copilot** — liest das `SKILL.md`-Format NICHT; gebrückt über
  [`.github/copilot-instructions.md`](../.github/copilot-instructions.md), das auf den
  vendor-neutralen Katalog in [`AGENTS.md`](../AGENTS.md) verweist (Workflow inline ausführen).

Vollständige Mechanik + Anlege-Anleitung: [`SKILLS_SETUP.md`](SKILLS_SETUP.md).

## Validierung

`.github/scripts/validate-agent-skills.py` (stdlib-only) prüft Frontmatter, `name`==Verzeichnis,
die `.claude`/`.codex`-Symlinks, die Sub-Agenten und die Copilot-Brücke — lokal und in CI
(`.github/workflows/skill-lint.yml`):

```bash
python3 .github/scripts/validate-agent-skills.py
```
