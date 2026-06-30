#!/usr/bin/env python3
"""Validate this repo's Agent Skills + Claude subagents against the Agent Skills
standard (https://agentskills.io/specification) and the repo's own conventions.

Self-contained (stdlib only) so CI never depends on an external linter being
installable. Run locally: `python3 .github/scripts/validate-agent-skills.py`.

Checks (ERROR = fail; WARN = report only):
  Skills (skills/*/SKILL.md), per agentskills.io:
    - frontmatter present (YAML between leading `---` fences)
    - name: 1-64 chars, ^[a-z0-9]+(-[a-z0-9]+)*$ (lowercase/digits/hyphens, no
      leading/trailing/consecutive hyphen), and MUST equal the parent dir name
    - description: present, 1-1024 chars
    - compatibility (optional): <= 500 chars
    - metadata (optional): a map of string -> string
    - WARN if SKILL.md body exceeds 500 lines (spec recommendation)
  Repo convention (single source of truth in skills/, symlinked per SKILLS_SETUP.md):
    - .claude/skills/<name> and .codex/skills/<name> exist and resolve to the skill dir
  Claude subagents (.claude/agents/*.md):
    - frontmatter present; name present and == filename stem; description present
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")  # also forbids leading/trailing/double hyphen
errors: list[str] = []
warnings: list[str] = []


def err(p, m):
    errors.append(f"{p}: {m}")


def warn(p, m):
    warnings.append(f"{p}: {m}")


def split_frontmatter(text):
    """Return (frontmatter_str, body_str) or (None, text) if no leading --- fence."""
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    return parts[1], parts[2]


def parse_frontmatter(fm):
    """Minimal YAML for these files: single-line `key: value` scalars plus one
    nested `metadata:` map of indented `key: value`. Sufficient for the SKILL.md /
    agent frontmatter shapes used here; not a general YAML parser."""
    data, in_metadata = {}, False
    for raw in fm.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[0] in " \t":  # indented -> belongs to the current nested map
            if in_metadata:
                m = re.match(r"\s+([^:]+):\s*(.*)$", raw)
                if m:
                    data.setdefault("metadata", {})[m.group(1).strip()] = m.group(2).strip().strip('"')
            continue
        m = re.match(r"([A-Za-z0-9_-]+):\s*(.*)$", raw)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        in_metadata = key == "metadata"
        if in_metadata and val == "":
            data["metadata"] = {}
        else:
            data[key] = val.strip('"')
    return data


def validate_skill(skill_dir):
    name_dir = os.path.basename(skill_dir)
    md = os.path.join(skill_dir, "SKILL.md")
    rel = os.path.relpath(md, ROOT)
    if not os.path.isfile(md):
        err(rel, "missing SKILL.md")
        return
    fm_str, body = split_frontmatter(open(md, encoding="utf-8").read())
    if fm_str is None:
        err(rel, "missing/invalid YAML frontmatter (must start with a --- fence)")
        return
    fm = parse_frontmatter(fm_str)

    name = fm.get("name", "")
    if not name:
        err(rel, "missing required field: name")
    else:
        if len(name) > 64:
            err(rel, f"name exceeds 64 chars ({len(name)})")
        if not NAME_RE.match(name):
            err(rel, f"name '{name}' must be lowercase a-z/0-9/hyphens, no leading/trailing/consecutive hyphen")
        if name != name_dir:
            err(rel, f"name '{name}' must match parent directory '{name_dir}'")

    desc = fm.get("description", "")
    if not desc:
        err(rel, "missing required field: description (non-empty)")
    elif len(desc) > 1024:
        err(rel, f"description exceeds 1024 chars ({len(desc)})")

    comp = fm.get("compatibility")
    if comp is not None and len(comp) > 500:
        err(rel, f"compatibility exceeds 500 chars ({len(comp)})")

    meta = fm.get("metadata")
    if meta is not None and not isinstance(meta, dict):
        err(rel, "metadata must be a key->value map")

    body_lines = body.strip("\n").count("\n") + 1 if body.strip() else 0
    if body_lines > 500:
        warn(rel, f"SKILL.md body is {body_lines} lines (spec recommends < 500; move detail to references/)")

    # repo convention: symlinked into both tool paths
    if name and name == name_dir:
        for tool_dir in (".claude/skills", ".codex/skills"):
            link = os.path.join(ROOT, tool_dir, name)
            if not os.path.exists(link):
                err(os.path.join(tool_dir, name), f"missing symlink for skill '{name}' (see skills/SKILLS_SETUP.md)")
            elif os.path.realpath(link) != os.path.realpath(skill_dir):
                err(os.path.join(tool_dir, name), f"symlink does not resolve to skills/{name}")


def validate_agent(md):
    rel = os.path.relpath(md, ROOT)
    stem = os.path.basename(md)[:-3]
    fm_str, _ = split_frontmatter(open(md, encoding="utf-8").read())
    if fm_str is None:
        err(rel, "missing/invalid YAML frontmatter")
        return
    fm = parse_frontmatter(fm_str)
    if not fm.get("name"):
        err(rel, "missing required field: name")
    elif fm["name"] != stem:
        err(rel, f"name '{fm['name']}' must match filename '{stem}'")
    if not fm.get("description"):
        err(rel, "missing required field: description")


def main():
    skills_root = os.path.join(ROOT, "skills")
    skill_dirs = sorted(
        d for d in (os.path.join(skills_root, n) for n in os.listdir(skills_root))
        if os.path.isdir(d) and os.path.isfile(os.path.join(d, "SKILL.md"))
    ) if os.path.isdir(skills_root) else []
    for d in skill_dirs:
        validate_skill(d)

    agents_root = os.path.join(ROOT, ".claude", "agents")
    agent_files = sorted(
        os.path.join(agents_root, f) for f in os.listdir(agents_root) if f.endswith(".md")
    ) if os.path.isdir(agents_root) else []
    for f in agent_files:
        validate_agent(f)

    # Cross-vendor portability: GitHub Copilot does not read skills/ or AGENTS.md
    # directly, so it must be bridged via .github/copilot-instructions.md (see
    # skills/SKILLS_SETUP.md); AGENTS.md carries the vendor-neutral capability catalog.
    copilot = os.path.join(ROOT, ".github", "copilot-instructions.md")
    if not os.path.isfile(copilot):
        err(".github/copilot-instructions.md", "missing Copilot bridge (cross-vendor portability; see skills/SKILLS_SETUP.md)")
    elif "AGENTS.md" not in open(copilot, encoding="utf-8").read():
        warn(".github/copilot-instructions.md", "should reference AGENTS.md as the canonical source")
    agents_md = os.path.join(ROOT, "AGENTS.md")
    if os.path.isfile(agents_md) and "Agent capabilities" not in open(agents_md, encoding="utf-8").read():
        warn("AGENTS.md", "missing the vendor-neutral 'Agent capabilities' catalog (cross-vendor discovery)")

    print(f"validated {len(skill_dirs)} skills + {len(agent_files)} agents")
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    if errors:
        print(f"\nFAILED: {len(errors)} error(s).")
        sys.exit(1)
    print("OK" + (f" ({len(warnings)} warning(s))" if warnings else ""))


if __name__ == "__main__":
    main()
