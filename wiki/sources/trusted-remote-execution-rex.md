---
type: source
created: 2026-05-12
updated: 2026-05-12
origin: llm
sources: []
tags: [agent-safety, policy, cedar, sandbox, aws, open-source]
---

# Introducing Trusted Remote Execution (Rex)

[Original](https://aws.amazon.com/blogs/opensource/introducing-trusted-remote-execution-policy-enforced-scripts-for-ai-agents-and-humans/) | [Raw](../../raw/llm/trusted-remote-execution-rex.md)

**Authors:** Nick MacDonald, Joshua Brindle (AWS)
**Published:** 2026-05-04

## Summary

[[aws]] open-source announcement of **Rex** (Trusted Remote Execution) — a scripting runtime where every system operation is authorized by policy. Scripts are written in Rhai (a lightweight language with no built-in system access). The only way to reach the host is through operations Rex explicitly provides, each authorized against a [[cedar]] policy at invocation time.

Designed specifically for the AI agent use case: when an agent generates and executes scripts autonomously, there's no human reviewing each system call. Rex gives the **host owner** full control over what's permitted, regardless of what the agent requests.

## How It Works

1. **Rhai engine** has zero direct host access — sandboxed by design
2. **Rex SDK operations** (`read`, `write`, `open`, etc.) are the only system interface
3. **Cedar policy** is evaluated before every operation executes
4. **Policy violation** → clear `ACCESS_DENIED_EXCEPTION` (agent can observe, reason, adjust)
5. **Script and policy are separate** — same script, different policies = different permissions

```
Script says WHAT to do → Policy says WHAT'S ALLOWED → Rex enforces at runtime
```

## Key Design Decisions

- **Constrains what the agent can do to the host** (not the agent itself) — host owner retains control
- **Policy is separate from code** — service owner defines boundaries, agent/script author defines behavior
- **Graceful denial** — agents receive clear errors and can adapt (not crash or hang)
- **Composable with IAM/SSM** — can pair with AWS identity and session management for production use

## Significance for Agentic AI

This is the first concrete open-source implementation of **policy-enforced agent execution** in the wiki. It makes the governance concepts from [[agentic-ai-governance]] tangible:

- The "kill switch" pillar → Cedar policy can deny any operation
- The "least privilege" principle → policy explicitly enumerates allowed actions
- The "prompt injection" risk → even if an agent is manipulated, the policy boundary holds
- [[claude-code]]'s permission modes (ask/auto-accept) operate at a different layer — Rex operates at the **system call** layer

## Connections

- Implements [[agentic-ai-governance]] pillar 2 (least privilege) and pillar 5 (kill switches) concretely
- Extends [[claude-code]] trust model — Claude Code has permission modes for tool use; Rex adds a host-side enforcement layer below that
- Connects to [[agentic-ux-patterns]] — the "Autonomy Dial" pattern, but enforced by policy rather than UI
- Validates [[vibe-coding-lessons-k10s]] Tenet 5 — AI shouldn't own state transitions; Rex ensures it can't bypass policy
- New entity: [[rex]] (Trusted Remote Execution)
- New entity: [[cedar]] (Cedar policy language)

## See Also
- [[agentic-ai-governance]]
- [[claude-code]]
- [[kiro]]
- [[agentic-ux-patterns]]
