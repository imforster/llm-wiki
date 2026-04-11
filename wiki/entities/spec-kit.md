---
type: entity
created: 2026-04-10
updated: 2026-04-10
sources: ["[[spec-kit]]"]
tags: [tool, methodology, spec-driven, github, open-source]
---

# Spec Kit

Open-source toolkit by GitHub for Spec-Driven Development. CLI (`specify`) + slash commands across 30+ AI agents. MIT licensed.

"Build high-quality software faster. Focus on product scenarios and predictable outcomes instead of vibe coding."

## Core Workflow

```
/speckit.constitution  →  Establish project principles
/speckit.specify       →  Define requirements (the "what" and "why")
/speckit.clarify       →  Structured questioning to reduce rework
/speckit.plan          →  Technical implementation plan (the "how")
/speckit.tasks         →  Actionable task breakdown with dependencies
/speckit.implement     →  Execute all tasks
```

Optional: `/speckit.analyze` (consistency check), `/speckit.checklist` (quality validation)

## Key Features

- **30+ supported agents**: Claude Code, Codex, Gemini CLI, Cursor, Kiro CLI, Copilot, and many more
- **50+ community extensions**: Jira, Azure DevOps, Confluence, security review, code review, V-Model testing
- **Presets**: Customize templates and commands without changing tooling
- **Constitution**: Project governance principles that guide all development
- **Feature branching**: Each feature gets its own branch, spec directory, and artifacts

## In the Ecosystem

Spec Kit operates at the **methodology layer** — above individual agents but orthogonal to organizational orchestration:

| Layer | Tool | Focus |
|-------|------|-------|
| Company | [[paperclip]] | Org charts, budgets, governance |
| Methodology | Spec Kit | Specs, plans, tasks, quality gates |
| Infrastructure | [[scion]] | Containers, runtimes, harnesses |
| Tool | [[claude-code]] | Agentic loop, skills, hooks |

## See Also
- [[agent-skills-standard]]
- [[claude-code]]
- [[multi-agent-orchestration]]
- [[paperclip]]
