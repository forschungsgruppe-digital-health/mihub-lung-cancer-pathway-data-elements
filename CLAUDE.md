# CLAUDE.md

@AGENTS.md

> All project context, repository conventions, the quality gate, branching and the binding
> rules live in the `AGENTS.md` imported above (tool-agnostic, canonical — also read by Codex,
> Cursor, Gemini and other agents). This file exists only so Claude Code picks up the same single
> source. Add Claude-Code-specific notes below if ever needed.
>
> Skills live in `skills/` and are exposed to Claude Code via the `.claude/skills` symlinks
> (→ `../../skills/<name>`) and as subagents via `.claude/agents/<name>.md` (symlinks to the same
> `SKILL.md`): `data-element-analyzer`, `data-element-validator`, `check-duplicate-data-element`,
> `ai-usage-curator`. See [`skills/SKILLS_SETUP.md`](skills/SKILLS_SETUP.md).
