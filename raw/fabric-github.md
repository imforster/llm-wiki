# Fabric

Source: https://github.com/danielmiessler/fabric
Author: Daniel Miessler
Retrieved: 2026-04-08

## Overview

Fabric is an open-source framework for augmenting humans using AI. It organizes prompts (called "Patterns") by real-world task, allowing people to create, collect, and organize their most important AI solutions in a single place. Written in Go. MIT licensed.

Mission: "human flourishing via AI augmentation"

Philosophy: "AI isn't a thing; it's a magnifier of a thing. And that thing is human creativity."

## Core Concept: Patterns

Patterns are Fabric's fundamental unit — curated, well-structured prompts organized by task. 251+ patterns covering life and work activities:
- Extracting interesting parts of YouTube videos and podcasts
- Writing essays in your own voice
- Summarizing academic papers
- Creating AI art prompts
- Rating content quality
- Explaining code
- Turning bad documentation into usable documentation
- Creating social media posts
- And many more

### Pattern Design Principles
- Use Markdown for maximum readability and editability
- Extremely clear instructions with Markdown structure for emphasis
- Use the System section of the prompt almost exclusively
- Each pattern is a directory with a system.md file

### Custom Patterns
Users can create custom patterns in ~/.config/fabric/patterns/

## Prompt Strategies

Fabric implements prompt strategies as composable modifiers applied on top of patterns:
- cot — Chain-of-Thought: Step-by-step reasoning
- cod — Chain-of-Draft: Iterative drafting with minimal notes (5 words max per step)
- tot — Tree-of-Thought: Multiple reasoning paths, select best
- aot — Atom-of-Thought: Break into smallest independent atomic sub-problems
- ltm — Least-to-Most: Solve from easiest to hardest sub-problems
- self-consistent — Multiple reasoning paths with consensus
- self-refine — Answer, critique, and refine
- reflexion — Answer, critique briefly, provide refined answer
- standard — Direct answer without explanation

Usage: `echo "input" | fabric --strategy cot -p analyze_code`

Strategies stored as JSON files in ~/.config/fabric/strategies/

## Architecture

- Written in Go (migrated from Python)
- CLI-first: `fabric --pattern <name>` or pipe input
- REST API server mode with Swagger/OpenAPI docs
- Ollama compatibility mode
- Shell aliases: each pattern becomes a command
- Obsidian integration: save output as dated markdown files

## Supported AI Providers (30+)

Native: OpenAI, OpenAI Codex, Anthropic (Claude), Google Gemini, Ollama, Azure OpenAI, Amazon Bedrock, Vertex AI, LM Studio, Perplexity, Microsoft 365 Copilot

OpenAI-Compatible: Abacus, AIML, Cerebras, DeepSeek, DigitalOcean, GitHub Models, GrokAI, Groq, Langdock, LiteLLM, MiniMax, Mistral, Novita AI, OpenRouter, SiliconCloud, Together, Venice AI, Z AI

## Key Features
- Per-pattern model mapping via environment variables
- Speech-to-text support
- Docker support
- i18n (10 languages)
- Shell completions (Zsh, Bash, Fish)
- Helper apps: to_pdf, code2context, generate_changelog
- Web interface (Fabric Web App)

## Relationship to Other Tools
- Fabric patterns are similar to skills in the Agent Skills standard — both are curated prompt packages organized by task
- Fabric's strategies (CoT, ReAct, Reflexion) map directly to the prompt engineering patterns described in academic literature
- Fabric is model-agnostic (30+ providers) like Scion is harness-agnostic
- The pattern library is community-driven, similar to the Agent Skills marketplace concept
