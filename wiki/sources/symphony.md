---
type: source
created: 2026-05-09
updated: 2026-05-09
origin: human
sources: []
tags: [multi-agent, orchestration, openai, codex, spec-driven]
---

# Symphony

[Original](https://github.com/openai/symphony) | [Raw](symphony-readme.md)

## Summary

Symphony is OpenAI's open-source orchestration service that turns issue tracker work (Linear) into isolated, autonomous coding agent runs. Rather than providing a framework or SDK, Symphony publishes a language-agnostic **specification** (SPEC.md, 78KB) that any team can implement in their language of choice. The reference implementation is in Elixir. 23K stars, Apache 2.0.

## Key Takeaways

1. **Spec-first, not framework-first** — Symphony is a 2,169-line specification document, not a library. Teams are expected to implement it in their own language. This is a radically different approach from every other tool in the wiki — it's a protocol, not a product.

2. **WORKFLOW.md as the single source of truth** — All agent behavior (prompt template, runtime config, hooks, tracker settings) lives in one version-controlled file with YAML front matter. Dynamic reload without restart. This is the strongest "policy-as-code" implementation in the wiki.

3. **Scheduler/runner, not an agent** — Symphony explicitly does NOT write to the issue tracker. It reads issues, dispatches agents, and tracks state. The coding agent (Codex) handles all mutations. Clear separation of concerns.

4. **Per-issue workspace isolation** — Each issue gets its own filesystem workspace (sanitized path, contained under root). Workspaces persist across runs. Lifecycle hooks (after_create, before_run, after_run, before_remove) provide extension points.

5. **In-memory state, tracker-driven recovery** — No persistent database. On restart, Symphony recovers by polling the tracker and reusing preserved workspaces. Intentionally simple.

6. **Multi-turn continuation within a session** — A single worker can run up to max_turns (default 20) on the same thread, re-checking issue state between turns. Continuation turns don't resend the original prompt.

7. **Harness engineering prerequisite** — Symphony assumes the codebase is already prepared for coding agents. It's "the next step" after harness engineering — managing work, not managing agents.

## Architecture

Six-layer abstraction:
1. Policy (WORKFLOW.md)
2. Configuration (typed getters)
3. Coordination (orchestrator)
4. Execution (workspace + agent)
5. Integration (Linear adapter)
6. Observability (logs + status)

## Comparison to Wiki Tools

| Dimension | Symphony | [[gastown]] | [[multica]] | [[paperclip]] |
|-----------|----------|-------------|-------------|---------------|
| Approach | Spec/protocol | CLI workspace manager | Platform/SaaS | Org-level |
| Implementation | Elixir (reference) | Go | Go + TypeScript | Agent-agnostic |
| Agent runtime | Codex app-server only | Any CLI agent | Any CLI agent | Any |
| Persistence | Filesystem + tracker | Git worktrees | PostgreSQL | Agent-agnostic |
| Issue tracker | Linear (only) | Beads (built-in) | Built-in board | Built-in board |
| Concurrency | Configurable (default 10) | 20-30 agents | Unlimited (runtime-bound) | Company-level |
| Merge strategy | None (agent handles) | Bors-style queue | None | Goal-based |

## Notable Design Decisions

- **No database** — Recovery is tracker + filesystem driven
- **No UI required** — Optional HTTP extension, but not needed for conformance
- **Exponential backoff** — min(10s × 2^(attempt-1), 5min cap)
- **Stall detection** — Kills sessions with no activity beyond 5min
- **Blocker-aware dispatch** — Todo issues with non-terminal blockers are skipped
- **Trust boundary is implementation-defined** — Spec doesn't prescribe sandbox policy

## See Also
- [[symphony]]
- [[multi-agent-orchestration]]
- [[openai-swarm]]
- [[gastown]]
