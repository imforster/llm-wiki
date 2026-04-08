---
type: source
created: 2026-04-07
updated: 2026-04-07
sources: []
tags: [multi-agent, orchestration, llm, google, containers, devtools]
---

# Scion Documentation

[Original](https://googlecloudplatform.github.io/scion) | [Raw](../../raw/scion-docs.md)

## Summary

Scion is an experimental multi-agent orchestration testbed by [[google-cloud-platform]], designed to manage concurrent LLM-based [[agent]]s running in [[container]]s across local machines and remote [[kubernetes]] clusters. It acts as a "hypervisor for agents" — not a full multi-agent framework, but an infrastructure layer for running, isolating, and managing agent processes.

## Key Takeaways

- **Manager-Worker architecture**: A host-side CLI (`scion`) orchestrates agent containers. Each agent runs an LLM + [[harness]] loop in isolation.
- **Harness-agnostic**: Supports [[gemini-cli]], [[claude-code]], [[opencode]], and [[codex]] through a common adapter interface. New harnesses can be added via a [[plugin-system]].
- **Two operating modes**: Solo mode (local Docker/Podman, zero-config) and Hosted mode (centralized [[hub]] dispatching to [[runtime-broker]]s).
- **Strict isolation**: Each agent gets its own filesystem, credentials, environment variables, and git workspace. Shadow mounts (tmpfs) prevent cross-agent access.
- **Git-native workspaces**: Local mode uses git worktrees; hosted mode uses git init + fetch. Each agent works on its own branch.
- **[[template]]s as blueprints**: Agents are created from templates that define system prompts, tools, images, and configuration. Templates support inheritance.
- **[[agent-state-model]]**: Three-dimensional state tracking — Phase (lifecycle), Activity (cognitive state), Detail (freeform context).
- **Philosophy**: Favors isolation over constraints, interaction over autonomy, diversity of models/harnesses, and action over planning. Runs agents in `--yolo` mode with infrastructure-level guardrails.

## Scope

The documentation covers: architecture, core concepts, all four supported harnesses, configuration system, Hub/Broker distributed architecture, workspace strategies, security model, plugin system, and the Go package structure.

## See Also
- [[agent]]
- [[grove]]
- [[hub]]
- [[harness]]
- [[template]]
- [[agent-state-model]]
- [[multi-agent-orchestration]]
