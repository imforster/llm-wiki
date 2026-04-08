---
type: entity
created: 2026-04-07
updated: 2026-04-07
sources: ["[[scion-docs]]"]
tags: [tool, multi-agent, orchestration, google]
---

# Scion

Scion is an experimental multi-agent orchestration testbed by [[google-cloud-platform]]. It manages concurrent LLM-based [[agent]]s running in [[container]]s across local machines and remote clusters.

## What It Is

A "hypervisor for agents" — infrastructure for running, isolating, and managing LLM agent processes. It is explicitly *not* a full multi-agent framework. Components like agent memory, chatrooms, and task management are treated as orthogonal concerns.

## Architecture

Scion follows a Manager-Worker pattern:
- **CLI** (`scion`): Host-side orchestrator managing agent lifecycle and [[grove]]s
- **Agents**: Isolated containers running LLM software via [[harness]] adapters

Two operating modes:
- **Solo Mode**: Local-only, zero-config. CLI manages agents directly via Docker/Podman/Apple Container.
- **Hosted Mode**: Distributed. A centralized [[hub]] coordinates state and dispatches to [[runtime-broker]]s.

## Key Commands

```
scion init                          # Initialize project
scion start <name> "<task>"         # Launch an agent
scion attach <name>                 # Interactive session
scion logs <name>                   # View output
scion resume <name>                 # Restart preserving state
scion list                          # Show all agents
scion delete <name>                 # Clean up
scion templates [create|list|show]  # Manage templates
```

## Supported Harnesses

| Harness | Target Tool | Auth Methods |
|---------|-------------|--------------|
| gemini | [[gemini-cli]] | API Key, OAuth, Vertex AI |
| claude | [[claude-code]] | API Key, Vertex AI |
| opencode | [[opencode]] | API Key, Auth File |
| codex | [[codex]] | API Key, Auth File |

## Configuration

- Global: `~/.scion/settings.yaml`
- Project: `.scion/settings.yaml`
- Templates: `.scion/templates/` or `~/.scion/templates/`

## Written In

Go. Key packages: `pkg/agent/`, `pkg/harness/`, `pkg/runtime/`, `pkg/hub/`, `pkg/runtimebroker/`.

## Philosophy

- Less is more — hypervisor, not full stack
- Isolation over constraints — `--yolo` mode + container isolation
- Interaction is imperative — humans and agents collaborate
- Diversity yields quality — mix models, harnesses, configurations
- Action over pondering — testbed for experimentation

## See Also
- [[agent]]
- [[grove]]
- [[hub]]
- [[harness]]
- [[template]]
- [[runtime]]
- [[agent-state-model]]
- [[multi-agent-orchestration]]
