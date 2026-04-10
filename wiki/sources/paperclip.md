---
type: source
created: 2026-04-09
updated: 2026-04-09
sources: []
tags: [orchestration, multi-agent, company, open-source, governance]
---

# Paperclip: Open-Source Orchestration for Zero-Human Companies

[Original](https://github.com/paperclipai/paperclip) | [Raw](../../raw/llm/paperclip-readme.md)

## Summary

[[paperclip]] is an open-source Node.js server + React UI that orchestrates a team of AI agents to run a business. Not an agent framework — it's the company layer above agents. Org charts, budgets, governance, goal alignment, and agent coordination. "If OpenClaw is an employee, Paperclip is the company." MIT licensed.

## Key Takeaways

- **Company-level orchestration, not agent-level**: Paperclip doesn't build agents — it organizes them into companies with org charts, roles, reporting lines, budgets, and governance. This is a layer above [[scion]] (infrastructure), [[claude-code]] (tool), and [[kiro]] (product).
- **Bring your own agent**: Works with Claude Code, Codex, Cursor, OpenClaw, Bash, HTTP. "If it can receive a heartbeat, it's hired." Agent-agnostic like [[scion]], but at the business layer instead of the infrastructure layer.
- **Goal-aware execution**: Every task traces back to the company mission. Tasks carry full goal ancestry so agents see the "why," not just a title. This is [[pai]]'s TELOS concept (goal orientation) applied to multi-agent companies.
- **Heartbeat-based scheduling**: Agents wake on a schedule, check work, and act. Delegation flows up and down the org chart. Similar to [[claude-code]]'s scheduled tasks but with organizational hierarchy.
- **Cost control as first-class**: Monthly budgets per agent. Atomic budget enforcement — when they hit the limit, they stop. No runaway costs. Addresses the evaluation economics gap from [[evaluating-agent-skills-caparas]].
- **Governance with rollback**: Approval gates enforced, config changes revisioned, bad changes rolled back. "You're the board." This is the human-in-the-loop pattern from [[ten-pillars-agentic-skill-design]] (Pillar 6) at the organizational level.
- **Persistent agent state**: Agents resume the same task context across heartbeats instead of restarting from scratch. Addresses the memory/context persistence challenge from [[context-management]].
- **Runtime skill injection**: Agents learn Paperclip workflows and project context at runtime. Related to [[agent-skills-standard]]'s progressive disclosure.
- **Clipmart (coming soon)**: Download and run entire companies with one click. Pre-built company templates — full org structures, agent configs, and skills. This is the marketplace concept from [[agent-skills-standard]] applied to entire organizations.
- **Multi-company isolation**: One deployment, many companies. Complete data isolation. One control plane for a portfolio.

## What Paperclip Is NOT

- Not a chatbot (agents have jobs, not chat windows)
- Not an agent framework (doesn't tell you how to build agents)
- Not a workflow builder (no drag-and-drop pipelines)
- Not a prompt manager (agents bring their own prompts)
- Not a single-agent tool (this is for teams of 20+ agents)
- Not a code review tool (orchestrates work, not PRs)

## Connections

- **[[scion]]**: Both are multi-agent orchestration, but at different layers. Scion = infrastructure (containers, runtimes, harnesses). Paperclip = business (org charts, budgets, goals, governance). Paperclip could theoretically use Scion as its runtime layer.
- **[[multi-agent-orchestration]]**: Paperclip introduces a fourth approach — **company-level orchestration** — beyond the infrastructure (Scion), product (Kiro), and tool (Claude Code) approaches already in the wiki.
- **[[pai]]**: Both are goal-oriented. PAI's TELOS (mission, goals, projects) maps to Paperclip's company mission → project goals → task hierarchy. But PAI is personal; Paperclip is organizational.
- **[[context-management]]**: Persistent agent state across heartbeats + goal ancestry flowing down = a form of hierarchical context management.
- **[[agent-skills-standard]]**: Runtime skill injection + Clipmart (company templates) extends the skill concept to organizational blueprints.

## See Also
- [[paperclip]]
- [[multi-agent-orchestration]]
- [[scion]]
- [[pai]]
- [[context-management]]
