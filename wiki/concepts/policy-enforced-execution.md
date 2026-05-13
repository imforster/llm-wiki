---
type: concept
created: 2026-05-12
updated: 2026-05-12
sources: ["[[trusted-remote-execution-rex]]", "[[agentic-ai-governance]]"]
tags: [governance, safety, sandbox, authorization]
---

# Policy-Enforced Execution

A runtime model where every system operation an agent performs is authorized against an explicit policy before execution. The policy is defined by the host/service owner, separate from the script or agent that requests the operation.

## Key Properties

- **Separation of concerns**: script says *what* to do, policy says *what's allowed*
- **Host-owner control**: the system owner defines boundaries, not the agent author
- **Graceful denial**: policy violations return clear errors — agents can observe, reason, and adapt
- **Defense in depth**: even if an agent is compromised (prompt injection, hallucination), the policy boundary holds

## Implementations

| Tool | Layer | Mechanism |
|------|-------|-----------|
| [[rex]] | System call | Cedar policy evaluated per operation (read/write/open) |
| [[claude-code]] | Tool use | Permission modes (ask/auto-accept/plan) per tool category |
| [[kiro]] | Tool approval | Per-tool permission prompts, pre-approval in agent config |

Rex operates at the lowest layer — individual system calls. Claude Code and Kiro operate at the tool-invocation layer. These are complementary, not competing.

## Relationship to Governance

This concept makes [[agentic-ai-governance]] pillar 2 (least privilege) and pillar 5 (kill switches) concrete and enforceable at runtime. It's the technical implementation of what governance frameworks describe in policy terms.

## See Also
- [[rex]]
- [[cedar]]
- [[agentic-ai-governance]]
- [[claude-code]]
- [[kiro]]
- [[agentic-ux-patterns]]
