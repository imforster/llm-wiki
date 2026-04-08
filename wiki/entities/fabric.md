---
type: entity
created: 2026-04-08
updated: 2026-04-08
sources: ["[[fabric-github]]"]
tags: [tool, open-source, cli, prompts, patterns]
---

# Fabric

An open-source framework (Go, MIT) for augmenting humans using AI. Created by [[daniel-miessler]].

Mission: "human flourishing via AI augmentation"

## Core Concept: Patterns

Patterns are curated, well-structured prompts organized by real-world task. 251+ patterns covering:
- Content extraction (YouTube, podcasts, articles)
- Writing (essays, social media, documentation)
- Analysis (code, claims, debates, incidents, logs)
- Creation (art prompts, concept maps, changelogs)
- And many more

Each pattern is a directory with a `system.md` file. Markdown-based, clear instructions, System section focused.

## Prompt Strategies

Nine composable strategies applied as modifiers on top of any pattern:

| Strategy | Approach |
|----------|----------|
| `cot` | Chain-of-Thought: step-by-step reasoning |
| `cod` | Chain-of-Draft: minimal notes per step |
| `tot` | Tree-of-Thought: multiple paths, select best |
| `aot` | Atom-of-Thought: smallest independent sub-problems |
| `ltm` | Least-to-Most: easiest to hardest |
| `self-consistent` | Multiple paths with consensus |
| `self-refine` | Answer → critique → refine |
| `reflexion` | Answer → brief critique → refined answer |
| `standard` | Direct answer |

This separates *what* to do (pattern) from *how* to reason (strategy).

## Architecture

- CLI-first, Unix philosophy: `echo "input" | fabric -p pattern_name`
- REST API server with Swagger docs
- 30+ AI providers (OpenAI, Anthropic, Gemini, Ollama, Bedrock, etc.)
- Per-pattern model mapping
- Shell aliases: each pattern becomes a command
- Obsidian integration for saving output as markdown
- Docker support, i18n (10 languages)

## In the Ecosystem

- Patterns are simpler predecessors to [[agent-skills-standard]] skills — same concept (curated prompt packages by task) but without scripts, progressive disclosure, or tool integration
- Strategies implement the [[prompt-engineering-patterns]] from academic literature
- Model-agnostic like [[scion]] is harness-agnostic
- Obsidian integration connects to the [[llm-wiki-pattern]]

## See Also
- [[daniel-miessler]]
- [[agent-skills-standard]]
- [[prompt-engineering-patterns]]
- [[llm-wiki-pattern]]
