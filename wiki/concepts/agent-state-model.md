---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[scion-docs]]"]
tags: [agent, state, lifecycle]
---

# Agent State Model

[[scion]] tracks agent state across three dimensions:

## Phase (Lifecycle)

The infrastructure lifecycle of the agent container:

`created → provisioning → cloning → starting → running → stopping → stopped (or error)`

## Activity (Cognitive State)

What the agent is doing within the `running` phase:

`idle | thinking | executing | waiting_for_input | blocked | completed | limits_exceeded | offline`

- **Sticky activities**: `completed`, `blocked`, and `limits_exceeded` persist until explicit restart or stop
- **blocked**: Set by agents themselves when waiting for an expected event (e.g., child agent completing) — prevents false stall detection
- **offline**: Occurs when heartbeat is lost, often due to auth token refresh failure. Fix: stop and restart the agent.

## Detail (Freeform Context)

Freeform text about the current activity — tool name, message, task summary.

## Design Rationale

The separation allows UI and API consumers to distinguish between infrastructure lifecycle events (provisioning, stopping) and the agent's cognitive state (thinking, waiting for input).

## See Also
- [[agent]]
- [[scion]]
