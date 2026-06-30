# Portable Agent Skills — Setup

Dieses `skills/`-Verzeichnis ist die **einzige Quelle** für die werkzeug-unabhängigen
Agent Skills dieses Repositorys (offener **Agent-Skills-Standard**, agentskills.io). Jedes
Skill ist ein Ordner mit einer `SKILL.md` (portabler `name` + `description`-Kern plus
Claude-spezifische Erweiterungsfelder, die andere Agenten gefahrlos ignorieren).

Drei Skills sind aus den ursprünglichen Claude-Code-Sub-Agenten dieses Repos hervorgegangen:
`data-element-analyzer`, `data-element-validator`, `ai-usage-curator`. Ein viertes,
`check-duplicate-data-element`, ist neu hinzugekommen (Dubletten-/Ähnlichkeitsprüfung
neuer Kandidaten vor Aufnahme).

## Kompatibilität

Der portable Kern (`name`, `description`, Markdown-Body) funktioniert über alle Werkzeuge, die
den Agent-Skills-Standard adoptieren — **Claude Code, OpenAI Codex CLI, Cursor, Gemini CLI** u. a.
Die Claude-spezifischen Felder (`tools`, `model`) sind Erweiterungen: Claude Code nutzt sie,
andere Werkzeuge ignorieren sie fehlerfrei. Read-only-Skills nennen ihre Read-only-Regel
zusätzlich als Prosa im Body, damit sie auch auf Werkzeugen sicher sind, die `tools` ignorieren.

**GitHub Copilot konsumiert das `SKILL.md`-Format NICHT** (keine `SKILL.md`-Erkennung). Es wird
separat über [`.github/copilot-instructions.md`](../.github/copilot-instructions.md) gebrückt —
diese Datei verweist auf den vendor-neutralen Katalog in [`AGENTS.md`](../AGENTS.md), damit
Copilot die Skills entdecken und den Workflow **inline** ausführen kann. Brücke und `AGENTS.md`
synchron halten (`AGENTS.md` ist kanonisch).

## Entdeckungs-Pfade unterscheiden sich je Werkzeug

Die Skills liegen neutral unter `skills/`. Jedes Werkzeug entdeckt sie an seinem eigenen Pfad —
empfohlen über **Symlinks**, damit die einzige Quelle in `skills/` bleibt.

### Claude Code

```bash
mkdir -p .claude/skills
for s in skills/*/; do n=$(basename "$s"); ln -s "../../skills/$n" ".claude/skills/$n"; done
# zusätzlich als Sub-Agenten (gleiche Quelle, kein Duplikat):
mkdir -p .claude/agents
for s in skills/*/; do n=$(basename "$s"); ln -s "../../skills/$n/SKILL.md" ".claude/agents/$n.md"; done
```

> Hinweis: `.claude/agents/<name>.md` zeigt per Symlink auf dieselbe `SKILL.md`. Deren
> Frontmatter (`name`, `description`, `tools`, `model`) ist zugleich gültiges Sub-Agenten-
> Frontmatter — so ist der Skill in Claude Code **sowohl** als Skill (`.claude/skills`) **als
> auch** als Sub-Agent (`.claude/agents`) verfügbar, ohne den Body zu duplizieren.

### OpenAI Codex

```bash
mkdir -p .codex/skills            # projektweit; oder ~/.codex/skills global
for s in skills/*/; do n=$(basename "$s"); ln -s "../../skills/$n" ".codex/skills/$n"; done
```

### Andere Werkzeuge

- **Cursor / VS Code:** konfigurierbare Skill-Orte — auf `skills/` zeigen oder analog symlinken.
- **Gemini CLI:** in den erwarteten Pfad symlinken (analog zu Codex).
- **GitHub Copilot:** NICHT per Symlink — Copilot liest `SKILL.md` nicht. Entdeckung + Projekt-
  regeln laufen über [`.github/copilot-instructions.md`](../.github/copilot-instructions.md).

## Symlinks und git

`git` speichert Symlinks standardmäßig als Symlinks. Auf Windows (unzuverlässige Symlinks)
entweder `core.symlinks=true` setzen oder den Symlink-Schritt durch Kopieren ersetzen (verliert
die einzige Quelle — bei Änderung neu kopieren).

## Verhältnis zu den Claude-Code-Sub-Agenten

Früher lagen die Capabilities als reine Sub-Agenten unter `.claude/agents/*.md`. Sie sind jetzt
nach `skills/` migriert (einzige Quelle) und werden von dort aus für Claude Code **als Skill und
als Sub-Agent** (Symlinks) sowie für Codex/Cursor/Gemini (Symlinks) und Copilot (Brücke)
bereitgestellt. Inhalt nur in `skills/<name>/SKILL.md` pflegen.

## Validierung

`.github/scripts/validate-agent-skills.py` (stdlib-only) erzwingt den Standard (`name`/
`description`-Grenzen, `name` == Verzeichnis, die `.claude`+`.codex`-Symlinks, das Sub-Agenten-
Frontmatter, die Copilot-Brücke) bei jedem PR, der `skills/`, `.claude/`, `.codex/` oder
`.github/` berührt — via **`skill-lint`** (`.github/workflows/skill-lint.yml`). Lokal:

```bash
python3 .github/scripts/validate-agent-skills.py
```

## Spezifikation

Format: https://agentskills.io/specification — Pflicht-Frontmatter: `name` (max. 64 Zeichen,
Kleinbuchstaben/Ziffern/Bindestriche, == Verzeichnisname) und `description` (max. 1024 Zeichen).
`SKILL.md`-Body möglichst < 500 Zeilen; Details nach `references/` auslagern.
