# Agent Compatibility

This project is host-neutral. The core distribution format is `skills/<skill-name>/SKILL.md`.

## Supported Shape

Any agent host that can read Agent Skills-style folders can use the suite:

```text
skills/
  brand-icon-system/SKILL.md
  brand-logo-brief/SKILL.md
  brand-logo-explore/SKILL.md
  brand-logo-refine/SKILL.md
  brand-logo-produce/SKILL.md
  brand-logo-audit/SKILL.md
```

The `agents/openai.yaml` files are optional UI metadata for OpenAI/Codex-style hosts. Other hosts can ignore them.

## Manual Install

Copy all skills into the directory your host reads:

```bash
cp -R skills/* /path/to/your/agent/skills/
```

Examples of common skill roots include `.agents/skills`, `.claude/skills`, and `~/.codex/skills`.

## Shared Scripts

Stage skills call shared scripts in `brand-icon-system/scripts`. If your host does not provide an automatic path to sibling skills, set:

```bash
BRAND_ICON_SYSTEM_HOME="/absolute/path/to/skills/brand-icon-system"
```

Then run scripts from that directory.

## Host-Specific Metadata

Add platform-specific package metadata only when needed. Keep the canonical skills in `skills/` so the repository remains portable.
