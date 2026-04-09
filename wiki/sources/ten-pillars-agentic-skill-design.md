---
type: source
created: 2026-04-08
updated: 2026-04-08
sources: []
origin: llm
tags: [skills, framework, best-practices, research, paper]
---

# The Ten Pillars of Agentic Skill Design

[Original](../../raw/llm/ten-pillars-agentic-skill-design.md)

Author: Ian Forster (with support of Kiro)
Version: 2.0 | November 2024

## Summary

A research paper proposing a comprehensive ten-pillar framework for designing agentic skills files — the modular extensions that encapsulate domain knowledge, workflows, and tool integrations for AI agents. Synthesizes software engineering principles, prompt engineering best practices, and analysis of 4,476+ GitHub repositories to address the lack of standardized design methodologies.

## The Ten Pillars

1. **Architecture and Structure** — Metadata, interfaces, core logic, workflows, configuration. Hierarchical separation of concerns following [[mcp-protocol]] server architecture.
2. **Documentation Clarity** — Self-documenting skills: purpose, usage triggers, examples, limitations, dependencies.
3. **Scope Definition** — Single Responsibility Principle. One domain per skill. Composition over inheritance.
4. **Modularity and Reusability** — Composable units. Include directives, skill libraries, dependency injection.
5. **Prompt Engineering** — Chain of Thought, ReAct pattern, self-reflection (Reflexion). System messages, stepwise instructions, few-shot examples.
6. **Tool Integration and Security** — [[mcp-protocol]] patterns. Defense-in-depth: credential management, input validation, sandboxing, human-in-the-loop, prompt injection defenses.
7. **Testing, Validation, and Observability** — Unit/integration tests. AgentOps observability: execution traces, model interactions, performance metrics, anomaly detection, quality monitoring.
8. **Version Control and Maintenance** — Semantic versioning. Changelogs. Dependency management. Compatibility matrices.
9. **Performance Optimization** — Token optimization. Context management recipes: chunking, progressive summarization, selective context loading, agent persona context templates. Caching patterns.
10. **Anti-Patterns** — Monolithic skills, hard-coded config, overly generic prompts, missing error handling, ignoring token limits, poor tool integration, lack of testing.

## Key Findings

- **Standardization matters**: MCP as universal protocol demonstrates need for standards. Skills on standard protocols show better interoperability.
- **Modular > monolithic**: MASAI achieved 28.33% on SWE-bench Lite by decomposing into specialized sub-agents. Validates pillars 3-4.
- **Sometimes agents aren't needed**: AGENTLESS achieved 27% on SWE-bench with a simple three-phase pipeline. Skills should match complexity to task requirements.
- **Trajectory efficiency**: LLMs often generate unnecessary reasoning steps. Skills should implement early stopping.
- **Self-reflection improves performance**: Reflexion and ReAct frameworks show feedback loops and self-correction significantly help.
- **Context management is critical**: Concrete recipes for multi-skill pipelines where different agent personas collaborate.

## Context Management Recipes

Four concrete patterns for multi-skill pipelines:
1. **Chunking** — Split large documents into semantic chunks with overlap for context continuity
2. **Progressive Summarization** — Two-pass compression preserving key facts at target ratio
3. **Selective Context Loading** — ContextManager class that loads only relevant context per skill, with priority-based budget allocation
4. **Agent Persona Context Templates** — Minimal context handoff between agent personas (analyst→engineer→reviewer)

## Empirical Evidence Cited

- Anthropic Productivity Study (2025): 80% task time reduction across 100K conversations
- SWE-bench: 1.96% success rate reveals gaps in structured problem-solving
- CodeAct: 20% higher success rate with structured executable code actions
- AutoGen: 4x coding effort reduction, 3-10x manual interaction reduction
- MASAI: 28.33% on SWE-bench Lite via modular sub-agents
- AGENTLESS: 27% on SWE-bench without agentic workflows

## Honest Limitations

The paper explicitly acknowledges: no original controlled study, no before/after case studies, no ablation studies, repository survey lacks formal methodology. Benefits are "anticipated" not "proven." Recommends practitioners measure their own results.

## See Also
- [[agent-skills-standard]]
- [[mcp-protocol]]
- [[claude-code]]
- [[multi-agent-orchestration]]
- [[context-management]]
- [[prompt-engineering-patterns]]
