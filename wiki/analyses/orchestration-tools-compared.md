---
type: analysis
created: 2026-05-09
updated: 2026-05-09
sources: ["[[gastown]]", "[[symphony]]", "[[multica]]", "[[paperclip]]", "[[langgraph-agent-orchestration]]", "[[autogen-multi-agent]]", "[[crewai-multi-agent]]", "[[openai-swarm]]"]
tags: [multi-agent, orchestration, comparison, analysis]
---

# Agent Orchestration Tools Compared: The 2026 Landscape

A comparative analysis of the emerging agent orchestration space, synthesizing wiki sources with three external comparison articles that directly evaluate [[gastown]], [[symphony]], and [[multica]] against each other and the broader field.

## The Fundamental Architectural Split

The most important finding from cross-source analysis is a **fundamental architectural split** in how multi-agent systems coordinate work:

| Architecture | Control Plane | Tools | Scale |
|---|---|---|---|
| **Conversation-as-control** | LLM routes via messages | AutoGen, CrewAI, LangGraph, OpenAI Agents SDK | 3-5 agents (token cost multiplies) |
| **Process-model** | Deterministic routing via external state | Gas Town | 20-30 agents (independent processes) |
| **Issue-tracker-driven** | Tracker polls + workspace isolation | Symphony | Bounded concurrency (default 10) |
| **Platform/board** | Web UI + daemon dispatch | Multica | Runtime-bound (unlimited agents) |

Gas Town is the only tool that uses a **process model** — agents coordinate via external state (Dolt/Git), not via LLM conversation. This is why it scales to 20-30 parallel agents while conversation-based frameworks struggle beyond 3-5. Every additional agent in a conversation multiplies token cost; every additional polecat in Gas Town is just another independent process with its own worktree.

## Seven Approaches to Orchestration

The wiki now documents seven distinct philosophies, from minimal to maximal:

| # | Approach | Tool | Complexity | Key Primitive |
|---|---|---|---|---|
| 1 | Simple loop | Ralph | Minimal | `while :; do cat PROMPT.md \| agent ; done` |
| 2 | Spec/protocol | [[symphony]] | Low | WORKFLOW.md + per-issue workspace |
| 3 | Handoff-based | [[openai-swarm]] | Low | Routines + handoffs |
| 4 | Workspace CLI | [[gastown]] | High | Git worktrees + hooks + GUPP |
| 5 | Platform/SaaS | [[multica]] | Medium | Agents as teammates + skills |
| 6 | Graph-based | [[langgraph-agent-orchestration]] | Medium | State machine + checkpoints |
| 7 | Company sim | [[paperclip]] | High | Org charts + budgets + governance |

## Head-to-Head: Gas Town vs Symphony vs Multica

| Dimension | Gas Town | Symphony | Multica |
|---|---|---|---|
| **Philosophy** | "Steam engine with Mayor as drive shaft" | "Manage work, not agents" | "Your next 10 hires won't be human" |
| **Stars** | 9.9K → 23K+ | 23K (3 weeks!) | 26.6K |
| **Language** | Go | Elixir (ref), any (spec) | Go + TypeScript |
| **Persistence** | Git worktrees + Dolt (cell-level merge) | Filesystem + tracker (no DB) | PostgreSQL + pgvector |
| **Agent runtime** | Claude, Codex, Copilot, Gemini, Cursor, + more | Codex app-server only | 11 CLIs (most vendor-neutral) |
| **Issue tracking** | Beads (built-in, git-backed) | Linear (external, read-only) | Built-in board |
| **Concurrency** | 20-30 parallel polecats | Default 10, configurable | Runtime-bound |
| **Merge strategy** | Bors-style bisecting queue (Refinery) | None (agent handles PRs) | None |
| **Monitoring** | 3-tier watchdog (Daemon→Deacon→Witness) | Structured logs + optional HTTP | Web dashboard |
| **Quality gates** | Refinery verification | None (trusted environments) | None |
| **Federation** | Wasteland (DoltHub) | N/A | N/A |
| **User model** | Single operator (tmux) | Single operator (daemon) | Multi-user teams |
| **Deployment** | Local CLI | Local daemon | Cloud-first + self-host |
| **Maturity** | Early (Jan 2026), experimental | Engineering preview | 65 releases, production |

## Key Differentiators

### Gas Town: Process-Model Pioneer

- **GUPP** (Gas Town Universal Propulsion Principle): "If there is work on your hook, YOU MUST RUN IT." Pull-based, crash-surviving execution. No other framework has this.
- **Separation of identity from session**: Agent Beads survive crashes. Every completion becomes part of a permanent capability ledger.
- **Dolt cell-level merge**: 20-30 agents writing to the same database without conflicts.
- **Git-worktree isolation**: Each polecat in its own worktree — most frameworks share state.
- **Escalation tiers**: Deacon (T1) → Mayor (T2) → Human (T3). More nuanced than binary human-in-loop.

### Symphony: Spec-First Minimalism

- **Language-agnostic specification**: 78KB SPEC.md that teams implement themselves. Unique in the space.
- **WORKFLOW.md as policy-as-code**: Strongest version-controlled agent behavior definition.
- **Harness engineering prerequisite**: Assumes the codebase is already prepared for agents.
- **No database, no UI**: Intentionally minimal. Recovery via tracker + filesystem.
- **Blocker-aware dispatch**: Todo issues with non-terminal blockers are automatically skipped.

### Multica: Team Collaboration Platform

- **Agents as first-class teammates**: Profiles, board presence, comments, blocker reporting.
- **Compounding skills**: Every solution becomes reusable for the whole team.
- **Most vendor-neutral**: 11 agent CLIs supported (more than any other tool).
- **Cloud-first architecture**: Full SaaS with WebSocket streaming, pgvector for skills.
- **Multi-user teams**: Roles, permissions, workspace isolation. Only tool designed for team collaboration.

## Emerging Patterns Across the Field

### 1. Cross-Model Adversarial Review
Metaswarm (not yet in wiki) implements writer ≠ reviewer (Claude writes, Codex/Gemini reviews). No instruction path from FAIL to COMMIT. Fresh reviewer spawned on retry to prevent anchoring bias. This is the strongest trust pattern emerging.

### 2. Harness Engineering as Prerequisite
Both Symphony and Gas Town assume the codebase is prepared for agents (CI, docs, AGENTS.md). This is becoming a recognized discipline — invest in repo structure so agents can operate autonomously.

### 3. Git as Universal Coordination
Gas Town (worktrees + Dolt), Symphony (per-issue workspaces), and AgentHub (branchless DAG) all use git as the coordination primitive. This validates the wiki's long-standing "git as universal coordination" theme.

### 4. The Autonomy Spectrum Crystallizes

```
Manual ←──────────────────────────────────────────────→ Autonomous
Ralph    Symphony    Multica    Gas Town    Paperclip
(loop)   (daemon)   (assign)   (GUPP)      (company)
```

### 5. Convergence Signal: Orchestrators Will Absorb Platforms
The rywalker.com analysis predicts: by 2027, enterprise adoption shifts to orchestration platforms. By 2028, "autonomous agent" and "orchestrator" categories merge. The distinction between "tool" and "teammate" will blur.

## Decision Framework

### Choose Symphony when:
- You use Linear for issue tracking
- You want minimal infrastructure (no DB, no UI)
- Your codebase already has strong CI/docs ("harness engineering")
- You want to implement the protocol in your own language
- Single agent per issue is sufficient

### Choose Gas Town when:
- You need 20-30+ parallel agents
- You want crash-surviving state (GUPP + git worktrees)
- You need a merge queue with quality gates
- You're comfortable with tmux and CLI-first workflows
- You want federation across workspaces (Wasteland)

### Choose Multica when:
- You have a team (not solo developer)
- You want agents visible on a board alongside humans
- You need cloud-first with self-hosting option
- You want compounding reusable skills
- You need the most vendor-neutral runtime support

### Choose Paperclip when:
- You want company-level governance (org charts, budgets)
- You need approval workflows and accountability
- You're simulating an entire AI-driven organization

## Open Questions

1. **Will Symphony expand beyond Linear?** The spec mentions pluggable tracker adapters as future work.
2. **Will Gas Town's process model be adopted by others?** The tmchow survey argues it shouldn't converge — the process model IS the differentiator.
3. **Will Multica's "skills" become a standard?** Compounding team skills is unique but unproven at scale.
4. **Cross-model review**: Will adversarial review (Metaswarm pattern) become standard? It's the strongest trust mechanism but doubles token cost.
5. **Federation**: Gas Town's Wasteland is the only cross-workspace coordination. Will others follow?

## Sources (External)

- [Autonomous Agentic Engineering Tools Compared](https://rywalker.com/research/autonomous-agentic-engineering-tools) — Ry Walker, March 2026. Compares 10 tools including Gas Town and Symphony.
- [Survey: Agent Orchestration Frameworks vs Gas City](https://gist.github.com/tmchow/f539adef1d11974eb51478a32a72ff68) — tmchow, March 2026. Deep comparison of Gas Town against 7 frameworks.
- [How Personal AI Agents and Agent Orchestrators are Made](https://gist.github.com/championswimmer/bd0a45f0b1482cb7181d922fd94ab978) — championswimmer, Feb 2026. Explains the agent stack from LLM call to orchestrator.

## See Also
- [[multi-agent-orchestration]]
- [[gastown]]
- [[symphony]]
- [[multica]]
- [[paperclip]]
- [[multi-agent-framework-guide]]
