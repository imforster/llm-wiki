# Symphony

**Turns project work into isolated, autonomous implementation runs, allowing teams to manage work instead of supervising coding agents.**

Source: https://github.com/openai/symphony
Blog post: https://openai.com/index/open-source-codex-orchestration-symphony/

- 23K stars, Apache 2.0 license
- Reference implementation in Elixir
- Language-agnostic spec (SPEC.md) — designed to be reimplemented in any language

## Overview

Symphony is a long-running automation service that continuously reads work from an issue tracker (Linear), creates an isolated workspace for each issue, and runs a coding agent session (Codex app-server) for that issue inside the workspace.

The service solves four operational problems:
- Turns issue execution into a repeatable daemon workflow instead of manual scripts
- Isolates agent execution in per-issue workspaces so agent commands run only inside per-issue workspace directories
- Keeps the workflow policy in-repo (WORKFLOW.md) so teams version the agent prompt and runtime settings with their code
- Provides enough observability to operate and debug multiple concurrent agent runs

## Key Design Principle: Harness Engineering

Symphony works best in codebases that have adopted "harness engineering" — the practice of preparing a codebase so coding agents can work effectively. Symphony is the next step: moving from managing coding agents to managing work that needs to get done.

## Architecture (from SPEC.md)

### Main Components

1. **Workflow Loader** — Reads WORKFLOW.md, parses YAML front matter and prompt body
2. **Config Layer** — Typed getters for workflow config values with defaults and env var indirection
3. **Issue Tracker Client** — Fetches candidate issues, normalizes tracker payloads
4. **Orchestrator** — Owns the poll tick, in-memory runtime state, dispatch/retry/stop decisions
5. **Workspace Manager** — Maps issue identifiers to workspace paths, runs lifecycle hooks
6. **Agent Runner** — Creates workspace, builds prompt, launches Codex app-server client
7. **Status Surface** (optional) — Human-readable runtime status
8. **Logging** — Structured runtime logs

### Abstraction Layers

1. **Policy Layer** (repo-defined) — WORKFLOW.md prompt body, team-specific rules
2. **Configuration Layer** — Typed getters, defaults, environment tokens
3. **Coordination Layer** — Polling loop, eligibility, concurrency, retries, reconciliation
4. **Execution Layer** — Workspace + agent subprocess
5. **Integration Layer** — Linear adapter
6. **Observability Layer** — Logs + optional status surface

## Orchestration State Machine

Internal issue states (not tracker states):
1. **Unclaimed** — Not running, no retry scheduled
2. **Claimed** — Reserved to prevent duplicate dispatch
3. **Running** — Worker task exists
4. **RetryQueued** — Worker not running, retry timer exists
5. **Released** — Claim removed (terminal, non-active, or retry exhausted)

Run attempt lifecycle phases:
PreparingWorkspace → BuildingPrompt → LaunchingAgentProcess → InitializingSession → StreamingTurn → Finishing → Succeeded/Failed/TimedOut/Stalled/CanceledByReconciliation

## Key Spec Details

### Polling & Scheduling
- Fixed cadence polling (default 30s)
- Bounded concurrency (default 10 agents, configurable per-state)
- Priority-based dispatch (priority ascending, oldest first, identifier tiebreaker)
- Blocker-aware: Todo issues with non-terminal blockers are not dispatched

### Retry & Recovery
- Normal completion → short continuation retry (1s) to re-check if issue still active
- Failure → exponential backoff: min(10000 * 2^(attempt-1), max_retry_backoff_ms)
- Default max backoff: 5 minutes
- Stall detection: kills sessions with no activity beyond stall_timeout_ms (default 5min)

### Workspace Safety
- Per-issue isolated workspace directories
- Sanitized identifiers (only [A-Za-z0-9._-])
- Path containment: workspace MUST stay under workspace root
- Agent cwd MUST be the per-issue workspace path
- Lifecycle hooks: after_create, before_run, after_run, before_remove

### WORKFLOW.md Contract
- YAML front matter for config + Markdown body for prompt template
- Strict template rendering (unknown variables/filters fail)
- Template variables: issue object + attempt number
- Dynamic reload without restart
- Versioned with the codebase

### Agent Integration
- Launches Codex app-server via bash -lc
- Multi-turn within a single worker session (up to max_turns, default 20)
- Continuation turns reuse the same thread (don't resend original prompt)
- Token accounting and rate-limit tracking
- Optional client-side tools (e.g., linear_graphql)

### Observability
- Structured logs with issue_id, issue_identifier, session_id
- Optional HTTP server extension with JSON API (/api/v1/state, /api/v1/<issue>, POST /api/v1/refresh)
- Token/runtime aggregation
- Rate-limit tracking

## Implementation Options

1. **Build your own** — Tell any coding agent to implement Symphony from the spec
2. **Use the Elixir reference implementation** — elixir/README.md

## Important Boundaries

- Symphony is a scheduler/runner and tracker reader
- Ticket writes (state transitions, comments, PR links) are performed by the coding agent
- A successful run can end at a workflow-defined handoff state (e.g., "Human Review"), not necessarily "Done"
- No rich web UI or multi-tenant control plane (by design)
- No persistent database — recovery is tracker-driven and filesystem-driven
- Trust and safety posture is implementation-defined (not prescribed by spec)

## Optional Extensions

- HTTP server for dashboard/API
- linear_graphql client-side tool
- SSH worker extension for remote execution
- Pluggable tracker adapters (future)
