---
type: source
created: 2026-04-08
updated: 2026-04-08
sources: []
tags: [fabric, patterns, prompts, open-source, cli]
---

# Fabric GitHub Repository

[Original](https://github.com/danielmiessler/fabric) | [Raw](../../raw/fabric-github.md)

Author: [[daniel-miessler]]

## Summary

[[fabric]] is an open-source framework (Go, MIT) for augmenting humans using AI. Its core contribution is **Patterns** — 251+ curated, well-structured prompts organized by real-world task. Also implements composable **prompt strategies** (CoT, ToT, Reflexion, etc.) as modifiers on top of patterns. Model-agnostic with 30+ provider integrations.

## Key Takeaways

- **Patterns as the fundamental unit**: Fabric's insight is that AI has a capabilities problem but an *integration* problem. Patterns solve this by packaging prompts as reusable, discoverable, shareable units organized by task. 251+ patterns covering everything from YouTube extraction to academic paper summarization.
- **Pattern design principles**: Markdown for readability, extremely clear instructions, System section almost exclusively. Each pattern is a directory with a `system.md` file.
- **Composable strategies**: Nine prompt strategies (CoT, CoD, ToT, AoT, LtM, self-consistent, self-refine, reflexion, standard) applied as modifiers on top of any pattern. Stored as JSON. This separates *what* to do (pattern) from *how* to reason (strategy).
- **CLI-first, Unix philosophy**: Pipe input, compose with other tools. `echo "input" | fabric --strategy cot -p analyze_code`. Shell aliases turn each pattern into a command.
- **Model-agnostic**: 30+ providers. Per-pattern model mapping via environment variables.
- **Obsidian integration**: Save output as dated markdown files — directly relevant to the [[llm-wiki-pattern]].
- **Community-driven**: Open source pattern library. The "wisdom of crowds" approach to prompt curation.

## Connections

- Patterns are conceptually similar to skills in the [[agent-skills-standard]] — both are curated prompt packages organized by task. But patterns are simpler (just a system.md) while skills support scripts, references, assets, and progressive disclosure.
- Fabric's strategies map directly to the [[prompt-engineering-patterns]] described in academic literature and the [[ten-pillars-agentic-skill-design]] framework (Pillar 5).
- Fabric is model-agnostic like [[scion]] is harness-agnostic — both abstract over the underlying AI provider.

## See Also
- [[fabric]]
- [[daniel-miessler]]
- [[agent-skills-standard]]
- [[prompt-engineering-patterns]]
- [[llm-wiki-pattern]]
