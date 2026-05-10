---
type: entity
created: 2026-05-09
updated: 2026-05-09
sources: ["[[multica]]"]
tags: [tool, multi-agent, platform, saas, open-source]
---

# Multica

Open-source managed agents platform that treats coding agents as first-class teammates. Cloud-first with self-hosting option. Agents get assigned issues, show up on boards, post comments, report blockers, and compound reusable skills.

## Key Facts

- **Repository**: https://github.com/multica-ai/multica
- **Website**: https://multica.ai
- **License**: Open source (see repo)
- **Stars**: 26.6K
- **Forks**: 3.2K
- **Releases**: 65 (v0.2.29 as of May 2026)
- **Languages**: TypeScript 47.4%, Go 45.4%
- **Stack**: Next.js 16 + Go (Chi/WebSocket) + PostgreSQL 17 (pgvector)
- **Supported runtimes**: Claude Code, Codex, GitHub Copilot CLI, OpenClaw, OpenCode, Hermes, Gemini, Pi, Cursor Agent, Kimi, Kiro CLI

## Core Design

- **Agents as teammates** — Profiles, board presence, comments, blocker reporting
- **Reusable skills** — Solutions compound over time for the whole team
- **Unified runtimes** — Local daemons + cloud, auto-detection of CLIs
- **Multi-workspace** — Team-level isolation
- **Cloud-first** — Full SaaS architecture with self-hosting option

## Positioning

Named after Multics (time-sharing OS). Thesis: two engineers + agent fleet = twenty engineers. Explicitly lighter than [[paperclip]] (Issues/Projects/Labels vs org charts/budgets/approvals). Most vendor-neutral runtime support in the wiki (11 agent CLIs).

## See Also
- [[multi-agent-orchestration]]
- [[paperclip]]
- [[gastown]]
- [[symphony]]
- [[agent-skills-standard]]
