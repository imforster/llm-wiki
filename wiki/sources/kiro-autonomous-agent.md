---
type: source
created: 2026-04-07
updated: 2026-04-07
sources: []
origin: llm
tags: [kiro, autonomous-agent, frontier-agent, aws, devtools]
---

# Kiro Autonomous Agent Page

[Original](https://kiro.dev/autonomous-agent/) | [Raw](../../raw/llm/kiro-autonomous-agent.md)

## Summary

Product page and FAQ for [[kiro]]'s autonomous agent feature — a [[frontier-agent]] that works independently on development tasks in the background. It takes high-level task descriptions, plans implementation, writes code across multiple repositories, runs tests, and creates pull requests, all asynchronously without requiring an active session.

## Key Takeaways

- **Asynchronous by design**: Unlike the Kiro IDE (interactive pair programming) and Kiro CLI (local custom agents), the autonomous agent runs in isolated sandbox environments in the background. You assign tasks from kiro.dev or GitHub.
- **Multi-repo coordination**: Can plan a change once and create coordinated edits and PRs across multiple repositories — not just one repo at a time.
- **Learns from feedback**: Maintains persistent context across tasks, repos, and PRs. Uses code review feedback to shape future changes. This is a key differentiator from stateless agent approaches.
- **Never auto-merges**: Always creates PRs for human review. Safety-first approach.
- **Sub-agent coordination**: Coordinates specialized sub-agents to complete complex development work.
- **Team features**: Integrates with Jira, Confluence, GitLab, GitHub, Teams, Slack. Handles routine fixes and follow-ups to protect engineer focus time.
- **"Frontier agent" branding**: [[aws]] positions this as a new class of agent — autonomous, massively scalable, works independently for hours or days.
- **Preview status**: Rolling out to Pro/Pro+/Power users. Free during preview with weekly limits.

## Scope

Product marketing page with FAQ. No deep technical architecture details — this is the public-facing description of capabilities and positioning.

## See Also
- [[kiro]]
- [[frontier-agent]]
- [[kiro-powers]]
- [[multi-agent-orchestration]]
