---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[scion-docs]]"]
tags: [blueprint, configuration, agent]
---

# Template

In [[scion]], a Template is a versioned blueprint for creating an [[agent]]. It defines the base configuration, system prompt, tools, and initial state.

## Contents

- `home/` directory tree — copied into the agent's home
- `scion-agent.json` (or `.yaml`) — specifies [[harness]] type, env vars, volumes, command args, model overrides, container image, resource requirements

## Inheritance

Templates support inheritance via a `base` field. Scion walks the chain and merges configurations bottom-up (base first, then overrides).

## Scopes

- **Project-level**: `.scion/templates/`
- **Global**: `~/.scion/templates/`
- **Hosted**: Can be scoped as global, grove, or user, with visibility controls (private, grove, public)

## Management

```
scion templates create
scion templates clone
scion templates list
scion templates show
scion templates update-default
```

## Defaults

Scion ships default templates for each supported [[harness]]: `gemini`, `claude`, `opencode`, `codex`. Users can create custom templates for specialized roles (e.g., "Security Auditor", "React Specialist").

## See Also
- [[scion]]
- [[agent]]
- [[harness]]
- [[grove]]
