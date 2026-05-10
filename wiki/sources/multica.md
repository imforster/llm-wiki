---
type: source
created: 2026-05-09
updated: 2026-05-09
origin: human
sources: []
tags: [multi-agent, orchestration, platform, saas, open-source]
---

# Multica

[Original](https://github.com/multica-ai/multica) | [Raw](../../raw/human/multica-readme.md)

## Summary

Multica is an open-source managed agents platform that treats coding agents as first-class teammates. Agents get assigned issues, show up on the board, post comments, report blockers, and compound reusable skills over time. Cloud-first with self-hosting option. 26.6K stars, Go + TypeScript, 65 releases.

## Key Takeaways

1. **Agents as teammates, not tools** — The core metaphor is "your next 10 hires won't be human." Agents have profiles, appear on boards, participate in conversations, and report blockers proactively. This is the most human-like agent UX in the wiki.

2. **Multiplexing thesis** — Named after Multics (time-sharing OS). The bet: two engineers + a fleet of agents can move like twenty. Time-sharing for an era where "users" are both humans and autonomous agents.

3. **Reusable skills that compound** — Every solution becomes a reusable skill for the whole team. Deployments, migrations, code reviews — skills compound capabilities over time. This is the [[agent-skills-standard]] applied at the team level.

4. **Vendor-neutral runtime** — Supports 11 agent CLIs: Claude Code, Codex, GitHub Copilot CLI, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI. Most runtime-agnostic tool in the wiki.

5. **Cloud-first architecture** — Next.js frontend + Go backend + PostgreSQL (pgvector) + local daemon. WebSocket for real-time progress streaming. This is a full SaaS platform, not a CLI tool.

6. **Lightweight management** — Explicitly positions against [[paperclip]]'s heavy governance (org charts, budgets, approvals). Multica uses Issues/Projects/Labels — closer to Linear than to a company simulator.

## Architecture

```
Frontend (Next.js 16) → Backend (Go/Chi/WebSocket) → PostgreSQL 17 (pgvector)
                                    ↕
                            Agent Daemon (local)
```

Key components:
- **Runtime** — Compute environment (local daemon or cloud). Auto-detects available agent CLIs.
- **Agent** — Has profile, assigned issues, posts comments, reports blockers
- **Skills** — Reusable solutions that compound over time
- **Workspace** — Team-level isolation

## Comparison to Wiki Tools

| Dimension | Multica | [[gastown]] | [[paperclip]] | [[symphony]] |
|-----------|---------|-------------|---------------|--------------|
| Metaphor | Teammates | Town/Rigs | Company | Scheduler |
| User model | Multi-user teams | Single operator | Single operator | Single operator |
| Deployment | Cloud-first | Local CLI | Local-first | Local daemon |
| Agent interaction | Issues + Chat | Mail + Convoys | Issues + Heartbeat | Issue tracker |
| Management | Lightweight | Medium (convoys) | Heavy (governance) | Minimal (spec) |
| Skills | Built-in, compounding | N/A | Skills + Plugins | WORKFLOW.md |
| Scale model | Team collaboration | 20-30 agents | Company-level | Bounded concurrency |

## See Also
- [[multica]]
- [[multi-agent-orchestration]]
- [[paperclip]]
- [[gastown]]
- [[agent-skills-standard]]
