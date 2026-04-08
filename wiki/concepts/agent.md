---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[scion-docs]]"]
tags: [agent, llm, isolation, container]
---

# Agent

In [[scion]], an Agent is an isolated process running an LLM + [[harness]] loop against a task. It is the fundamental unit of execution.

## Properties

Each agent has:
- **Identity**: Unique name, container ID, and (in hosted mode) a UUID and URL-safe slug
- **Home directory**: Mounted at `/home/<user>` — contains harness config, credentials, `agent-info.json`
- **Workspace**: Mounted at `/workspace` — a dedicated git worktree or cloned repo
- **Template**: The [[template]] blueprint that seeded its configuration
- **Harness**: The LLM-specific adapter (Claude, Gemini, OpenCode, Codex)

## State Model

See [[agent-state-model]] for the full three-dimensional state tracking system.

## Isolation

Agents are strictly isolated from each other:
- Dedicated filesystem and home directory
- Shadow mounts (tmpfs) prevent access to `.scion` data or other agents
- Environment variables explicitly projected
- Credentials mounted read-only or injected per-agent

## Sub-agents

Scion agents are not limited by a harness's built-in sub-agent feature. Through templates (home folder content, env vars, custom mounts), they have full agent capabilities even when acting as sub-agents from the orchestrator's perspective.

## See Also
- [[scion]]
- [[agent-state-model]]
- [[harness]]
- [[template]]
- [[grove]]
