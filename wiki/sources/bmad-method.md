---
type: source
created: 2026-04-10
updated: 2026-04-10
sources: []
tags: [agile, methodology, agents, multi-agent, open-source]
---

# BMad Method: AI-Driven Agile Development

[Original](https://github.com/bmad-code-org/BMAD-METHOD) | [Docs](https://docs.bmad-method.org) | [Raw](../../raw/llm/bmad-method-readme.md)

## Summary

[[bmad-method]] is an AI-driven agile development framework with scale-adaptive intelligence — it adjusts planning depth from bug fixes to enterprise systems. Uses 12+ specialized agent personas (PM, Architect, Developer, UX, etc.) with structured workflows grounded in agile best practices. Modular ecosystem with official modules for testing, game dev, creative intelligence, and custom agent building. MIT licensed.

## Key Takeaways

- **Agents as expert collaborators, not autopilots**: "Traditional AI tools do the thinking for you, producing average results. BMad agents act as expert collaborators who guide you through a structured process to bring out your best thinking." This is a fundamentally different philosophy from [[kiro]]'s autonomous frontier agents.
- **Scale-Domain-Adaptive**: Automatically adjusts planning depth based on project complexity. A bug fix doesn't need the same ceremony as an enterprise system. This addresses the "sometimes agents aren't needed" finding from [[ten-pillars-agentic-skill-design]].
- **12+ specialized agent personas**: PM, Architect, Developer, UX, and more. Each is a domain expert with a specific role. Related to [[skills-pipeline-sleestk]]'s persona-driven skills and [[pai]]'s agent personalities.
- **Party Mode**: Bring multiple agent personas into one session to collaborate and discuss. A novel approach to multi-agent interaction — not parallel execution (like [[scion]]) but collaborative dialogue within a single session.
- **Modular ecosystem**: Core framework (BMM, 34+ workflows) + official modules: BMad Builder (create custom agents), Test Architect (risk-based testing), Game Dev Studio, Creative Intelligence Suite. Extensible like [[agent-skills-standard]] but at the methodology level.
- **bmad-help skill**: Invoke anytime for guidance on what's next. Context-aware — knows your project state and installed modules. This is the "AI as thinking partner" pattern from [[ai-technique-podcast]].
- **Complete lifecycle**: Brainstorming → analysis → architecture → implementation → deployment. Broader than [[spec-kit]]'s spec-focused workflow.
- **Structured workflows over prompts**: 34+ workflows grounded in agile best practices. Not just prompt templates — structured processes with phases, checkpoints, and handoffs.

## Comparison with Spec Kit

| | [[spec-kit]] | BMad Method |
|---|---|---|
| **Focus** | Spec-driven (specs as primary artifact) | Agile-driven (structured workflows as primary process) |
| **Agents** | Agent-agnostic (30+ supported) | 12+ specialized personas built in |
| **Scaling** | Same workflow for all projects | Scale-adaptive (adjusts depth to complexity) |
| **Collaboration** | Single agent executes steps | Party Mode (multi-persona dialogue) |
| **Extensions** | 50+ community extensions | Official modules (testing, game dev, creative) |
| **Philosophy** | "Specs before code" | "Expert collaboration over autopilot" |

Both operate at the methodology layer. Spec Kit is more prescriptive (seven fixed steps). BMad is more adaptive (adjusts to project scale).

## Connections

- **[[multi-agent-orchestration]]**: Party Mode is a unique approach — multi-agent collaboration within a single session rather than across containers (Scion) or org charts (Paperclip).
- **[[ten-pillars-agentic-skill-design]]**: Scale-adaptive intelligence addresses the "sometimes agents aren't needed" finding. BMad's structured workflows implement multiple pillars (architecture, scope, modularity, testing).
- **[[agent-skills-standard]]**: BMad's skills architecture and the `bmad-help` skill follow similar patterns. The modular ecosystem (BMM + TEA + BMGD + CIS) is like a curated skill marketplace.
- **[[context-management]]**: Scale-adaptive planning is a form of context management — don't load enterprise-level ceremony for a bug fix.
- **[[ai-technique-podcast]]**: "AI as thinking partner, not executor" — BMad's core philosophy matches this practitioner insight exactly.

## See Also
- [[bmad-method]]
- [[spec-kit]]
- [[multi-agent-orchestration]]
- [[agent-skills-standard]]
- [[ten-pillars-agentic-skill-design]]
