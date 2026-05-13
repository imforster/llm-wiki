---
type: entity
created: 2026-05-12
updated: 2026-05-12
sources: ["[[trusted-remote-execution-rex]]"]
tags: [tool, runtime, sandbox, policy, aws, open-source]
---

# Rex (Trusted Remote Execution)

Open-source policy-enforced scripting runtime by [[aws]]. Scripts written in Rhai (no built-in system access) can only reach the host through operations authorized by a [[cedar]] policy at invocation time.

## Architecture

- **Rhai engine**: sandboxed — zero direct host access
- **Rex SDK**: purpose-built operations (`read`, `write`, `open`, etc.)
- **Cedar policy**: evaluated before every operation executes
- **Separation**: script defines behavior, policy defines boundaries

## Key Properties

- Host owner controls permissions, not the script author or agent
- Policy violations return clear `ACCESS_DENIED_EXCEPTION` — agents can observe and adapt
- Same script + different policy = different permissions
- Composable with AWS IAM and SSM for production use

## Significance

First concrete open-source implementation of **policy-enforced agent execution** — makes governance concepts tangible. Operates at the system-call layer, below [[claude-code]]'s permission modes and [[kiro]]'s tool approval.

## See Also
- [[cedar]]
- [[aws]]
- [[agentic-ai-governance]]
- [[claude-code]]
