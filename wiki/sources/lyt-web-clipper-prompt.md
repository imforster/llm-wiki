---
type: source
created: 2026-05-12
updated: 2026-05-12
origin: llm
sources: []
tags: [obsidian, web-clipper, knowledge-management, prompt]
---

# My Web Clipper Prompt (LYT)

[Original](https://www.linkingyourthinking.com/thank-you/my-web-clipper-prompt) | [Raw](../../raw/llm/lyt-web-clipper-prompt.md)

**Author:** Nick Milo (Linking Your Thinking)

## Summary

Setup guide for the Obsidian Web Clipper's Interpreter feature. Uses three AI-powered prompts (via `{{" "}}` syntax) to generate structured layers above any clipped article:

1. **Summary** — most interesting aspect as a single declarative statement
2. **Headlines** — bold one-line insights with 1-2 supporting sentences
3. **Things** — bulleted list of people, places, numbers, things, and concepts

Model-agnostic — works with Claude, GPT, Gemini, DeepSeek, or local models via Ollama.

## Significance

A lightweight, zero-code approach to knowledge capture that complements the [[llm-wiki-pattern]]:
- **Web Clipper**: capture-time processing, single-article scope, browser-native
- **LLM Wiki**: ingest-time processing, cross-source synthesis, vault-native

Both share the principle: AI processes, human curates. The three-layer template (summary → headlines → entities) mirrors this wiki's own source page structure.

## Connections

- Complements [[notebooklm-notes-guide]] — both are "AI-enhanced capture" tools with different scopes
- Validates [[llm-wiki-pattern]] — same capture→process→organize flow, lighter weight
- Connects to [[context-management]] — the interpreter prompt is a micro-context-engineering exercise

## See Also
- [[llm-wiki-pattern]]
- [[notebooklm]]
