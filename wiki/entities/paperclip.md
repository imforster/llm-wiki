---
type: entity
created: 2026-04-09
updated: 2026-04-09
sources: ["[[paperclip]]"]
tags: [tool, orchestration, multi-agent, open-source, company]
---

# Paperclip

Open-source orchestration for zero-human companies. Node.js server + React UI. MIT licensed.

"If OpenClaw is an employee, Paperclip is the company."

## What It Does

Orchestrates teams of AI agents into companies with:
- **Org charts**: Hierarchies, roles, reporting lines
- **Goal alignment**: Every task traces to company mission
- **Budgets**: Monthly per-agent, atomic enforcement
- **Governance**: Approval gates, rollback, audit logs
- **Heartbeats**: Scheduled agent wake cycles
- **Ticket system**: Every conversation traced, every decision explained
- **Multi-company**: One deployment, many isolated companies

## Agent Support

Agent-agnostic: Claude Code, Codex, Cursor, OpenClaw, Bash, HTTP. "If it can receive a heartbeat, it's hired."

## In the Ecosystem

Paperclip operates at a layer above the other tools in this wiki:

```
Paperclip    — Company layer (org charts, budgets, goals, governance)
  ↓
Scion        — Infrastructure layer (containers, runtimes, harnesses)
  ↓
Claude Code  — Tool layer (agentic loop, skills, hooks, MCP)
```

Introduces a fourth approach to [[multi-agent-orchestration]]: company-level orchestration, beyond infrastructure (Scion), product (Kiro), and tool (Claude Code).

## See Also
- [[multi-agent-orchestration]]
- [[scion]]
- [[pai]]
- [[context-management]]
