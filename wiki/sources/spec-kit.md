---
type: source
created: 2026-04-10
updated: 2026-04-10
sources: []
tags: [spec-driven, development, methodology, github, open-source, skills]
---

# Spec Kit: Spec-Driven Development Toolkit

[Original](https://github.com/github/spec-kit) | [Raw](../../raw/llm/spec-kit-readme.md)

## Summary

[[spec-kit]] is an open-source toolkit by GitHub for Spec-Driven Development (SDD) — a methodology where specifications become executable, directly generating working implementations rather than just guiding them. Provides a CLI (`specify`) and a set of slash commands that work across 30+ AI agents. MIT licensed.

## Key Takeaways

- **Specifications as the primary artifact**: SDD flips the script — specs define the "what" before the "how." Code is generated from specs, not the other way around. This is the opposite of "vibe coding."
- **Seven-step workflow**: Constitution (principles) → Specify (requirements) → Clarify → Plan (tech stack) → Tasks (breakdown) → Implement → Verify. Each step produces a persistent artifact.
- **Agent-agnostic**: Supports 30+ AI agents including [[claude-code]], Codex, Gemini CLI, Cursor, Kiro CLI, Copilot, and many more. Uses slash commands (`/speckit.specify`) or agent skills (`$speckit-specify`).
- **Extension ecosystem**: 50+ community extensions covering docs, code review, process orchestration, integrations (Jira, Azure DevOps, Confluence, GitHub Projects), visibility, and security. Categories: docs, code, process, integration, visibility.
- **Presets for customization**: Override templates and commands without changing tooling. Stack multiple presets with priority ordering. Examples: pirate speak, compliance-oriented formats, domain-specific terminology.
- **Constitution as governance**: A `constitution.md` file establishes project principles that guide all subsequent development — similar to [[claude-code]]'s CLAUDE.md but focused on project governance rather than agent behavior.
- **Feature branching built in**: Each feature gets its own branch (`001-create-taskify`), spec directory, plan, and task breakdown. Git-native workflow.
- **Clarification before planning**: `/speckit.clarify` runs structured questioning to reduce rework downstream. "Do not treat the first attempt as final."
- **Task breakdown with dependency management**: Tasks ordered by dependency, parallel execution markers (`[P]`), file path specifications, TDD structure, checkpoint validation.
- **Skills integration**: Installs as Claude Code skills (`.claude/skills/`) or Codex skills (`.agents/skills/`). Follows the [[agent-skills-standard]] pattern.

## Connections

- **[[agent-skills-standard]]**: Spec Kit installs its commands as skills following the standard. Each `/speckit.*` command is effectively a skill with a specific workflow.
- **[[ten-pillars-agentic-skill-design]]**: SDD operationalizes several pillars — Architecture (Pillar 1: structured artifacts), Documentation (Pillar 2: specs as documentation), Scope (Pillar 3: one feature per branch), Testing (Pillar 7: verify step), Version Control (Pillar 8: feature branching).
- **[[claude-code]]**: First-class integration. Skills installed in `.claude/skills/`. Constitution parallels CLAUDE.md.
- **[[multi-agent-orchestration]]**: Agent-agnostic like [[scion]], but at the methodology layer. The workflow is the same regardless of which agent executes it.
- **[[context-management]]**: The seven-step workflow is progressive disclosure applied to development — each step produces a focused artifact that feeds the next, rather than dumping everything into one prompt.
- **[[skill-evaluation]]**: The `/speckit.analyze` command (cross-artifact consistency check) and `/speckit.checklist` (quality validation) are built-in evaluation mechanisms — "unit tests for English."
- **[[paperclip]]**: Both address the "above the agent" layer, but differently. Paperclip = organizational orchestration (org charts, budgets). Spec Kit = methodological orchestration (specs, plans, tasks).
- **[[fabric]]**: Spec Kit's slash commands are like Fabric's patterns — reusable, named workflows. But Spec Kit's are sequential (a pipeline) while Fabric's are independent.

## See Also
- [[spec-kit]]
- [[agent-skills-standard]]
- [[claude-code]]
- [[multi-agent-orchestration]]
- [[context-management]]
