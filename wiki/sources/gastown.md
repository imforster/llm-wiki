---
type: source
created: 2026-05-08
updated: 2026-05-08
origin: human
sources: []
tags: [multi-agent, orchestration, go, cli, git-persistence]
---

# Gas Town

[Original](https://github.com/gastownhall/gastown) | [Raw](gastown-readme.md)

## Summary

Gas Town is an open-source multi-agent orchestration system written in Go that coordinates AI coding agents (Claude Code, GitHub Copilot, Codex, Gemini, Cursor, and others) with persistent work tracking. It solves the problem of agents losing context on restart by persisting work state in git-backed worktrees ("hooks"), enabling reliable coordination of 20-30+ concurrent agents.

## Key Takeaways

1. **Git worktrees as persistence primitive** — All agent state lives in git worktrees called "hooks." Work survives crashes, restarts, and session loss. This is the same "git as universal coordination" pattern seen across the wiki, but taken further than any other tool.

2. **Hierarchical agent roles** — A clear role hierarchy: Mayor (coordinator) → Polecats (workers) → Witness/Deacon/Dogs (monitors). Each role has persistent identity but ephemeral sessions.

3. **Bors-style merge queue** — The "Refinery" batches completed work, runs verification gates, and bisects failures. Polecats never push directly to main.

4. **Federated work coordination** — The "Wasteland" network links multiple Gas Town instances via DoltHub for cross-workspace work claiming and reputation tracking.

5. **Capacity scheduling** — Built-in scheduler prevents API rate limit exhaustion by governing concurrent polecat dispatch.

6. **Session continuity via Seance** — Agents can query predecessor sessions for context and decisions, solving the "lost context" problem without requiring persistent memory stores.

## Architecture

The system uses a town/rig/crew metaphor:

- **Town** — Workspace root (`~/gt/`), contains all projects and config
- **Rig** — Project container wrapping a git repo + its agents
- **Crew** — Human workspace within a rig
- **Polecat** — Worker agent (persistent identity, ephemeral sessions)
- **Hook** — Git worktree for persistent agent state
- **Convoy** — Work tracking unit bundling multiple beads (issues)
- **Bead** — Git-backed issue (prefix + 5-char ID, e.g. `gt-abc12`)
- **Molecule** — Workflow template (TOML formula → tracked steps)

## Monitoring Stack

Three-tier watchdog chain:

```
Daemon (Go process) ← heartbeat every 3 min
    └── Boot (AI agent) ← intelligent triage
        └── Deacon (AI agent) ← continuous patrol
            └── Witnesses & Refineries ← per-rig agents
```

Agent health states: Working → Stalled → GUPP Violation → Zombie → Idle.

## Supported Runtimes

Built-in presets: `claude`, `gemini`, `codex`, `cursor`, `auggie`, `amp`, `opencode`, `copilot`, `pi`, `omp`. Custom runtimes configurable via `gt config agent set`.

## Comparison to Wiki Tools

| Dimension | Gas Town | [[scion]] | [[kiro]] | [[claude-code]] | [[paperclip]] |
|-----------|----------|-----------|----------|-----------------|---------------|
| Layer | Workspace orchestration | Infrastructure | Product agent | Tool/IDE | Org-level |
| Persistence | Git worktrees (hooks) | Containers | Sandboxes | CLAUDE.md + memory | Agent-agnostic |
| Scale target | 20-30 agents | Unbounded (infra) | Single agent | Sub-agents | Company-level |
| Merge strategy | Bors-style queue | N/A | PR-based | PR-based | Goal-based |
| Monitoring | 3-tier watchdog | Plugin-based | Built-in | Hooks | Governance |
| Federation | Wasteland (DoltHub) | Hub | N/A | N/A | N/A |

## Notable Design Decisions

- **Go CLI** — Single binary (`gt`), shell completions, tmux integration
- **Dolt as database** — Git-for-data backing the beads ledger
- **Agent-agnostic** — Any AI coding tool can be a polecat runtime
- **MEOW pattern** — Mayor-Enhanced Orchestration Workflow as recommended usage
- **OpenTelemetry** — Full observability via OTLP (VictoriaMetrics/VictoriaLogs)
- **Docker Compose** — First-class containerized deployment option

## See Also
- [[gastown]]
- [[multi-agent-orchestration]]
- [[agent-memory-persistence]]
- [[multi-agent-observability]]
