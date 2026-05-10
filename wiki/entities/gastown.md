---
type: entity
created: 2026-05-08
updated: 2026-05-08
sources: ["[[gastown]]"]
tags: [tool, multi-agent, orchestration, go, open-source]
---

# Gas Town

Open-source multi-agent orchestration system for AI coding agents. Written in Go, distributed as a single CLI binary (`gt`). Coordinates 20-30+ concurrent agents with persistent work tracking via git worktrees.

## Key Facts

- **Repository**: https://github.com/gastownhall/gastown
- **Language**: Go 1.25+
- **License**: MIT
- **Install**: `brew install gastown` / `npm install -g @gastown/gt` / `go install`
- **Dependencies**: Git 2.25+, Dolt 1.82.4+, beads (bd) 0.55.4+, tmux 3.0+ (recommended)
- **Supported runtimes**: Claude Code, Codex, GitHub Copilot, Gemini, Cursor, Auggie, Amp, OpenCode, Pi, OMP

## Architecture

Hierarchical workspace model:

- **Town** → workspace root
- **Rig** → project container (git repo + agents)
- **Polecat** → worker agent (persistent identity, ephemeral sessions)
- **Hook** → git worktree for agent state persistence
- **Convoy** → work tracking unit (bundles beads/issues)
- **Refinery** → Bors-style merge queue per rig
- **Wasteland** → federated work network via DoltHub

## Monitoring

Three-tier watchdog: Daemon → Boot → Deacon → Witnesses/Refineries. Detects stuck agents (GUPP violations), zombies, and stalls. Escalation routing: Deacon → Mayor → Overseer.

## Differentiators

- Git worktrees as the persistence primitive (not databases, not memory stores)
- Agent-agnostic — any CLI-based AI tool can be a runtime
- Built-in merge queue with bisecting failure isolation
- Federated cross-workspace coordination (Wasteland)
- Session discovery (Seance) for context continuity across agent restarts
- OpenTelemetry observability built-in

## See Also
- [[multi-agent-orchestration]]
- [[scion]]
- [[paperclip]]
- [[claude-code]]
- [[multi-agent-observability]]
