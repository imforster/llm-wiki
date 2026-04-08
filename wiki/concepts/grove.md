---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[scion-docs]]"]
tags: [workspace, project, git]
---

# Grove

In [[scion]], a Grove is a project workspace where [[agent]]s live. It corresponds to a `.scion` directory on the filesystem.

## Scope

- **Project-level**: Located at the root of a git repository
- **Global**: In the user's home folder (`~/.scion`)

## Identification

Every grove has a unique Grove ID:
- **Git-backed groves**: Deterministic UUID v5 derived from namespace + normalized git URL — same repo always maps to same ID regardless of protocol
- **Hub-native groves**: Random UUID v4

## Contents

A grove contains:
- `agents/` — Per-agent state (gitignored)
- `templates/` — Grove-scoped [[template]] definitions
- `settings.yaml` — Project-level configuration overrides

## Resolution Order (Solo Mode)

1. Explicit `--grove` flag
2. Project-level `.scion` directory (walking up from cwd)
3. Global `~/.scion` directory

## See Also
- [[scion]]
- [[agent]]
- [[template]]
- [[hub]]
