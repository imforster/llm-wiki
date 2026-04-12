---
type: entity
created: 2026-04-11
updated: 2026-04-11
sources: ["[[notebooklm-notes-guide]]"]
tags: [tool, google, knowledge-management, ai, gemini]
---

# NotebookLM

A Gemini-powered writing and research tool from Google Labs. Co-founded by [[steven-johnson]]. Designed for AI-assisted knowledge work grounded in user-curated sources.

## Core Design

- Users upload sources (documents, articles, notes) — the AI only reasons over those sources, not the open web
- Two note types: Written Notes (user-authored, editable) and Saved Responses (AI-generated, immutable)
- Provenance tracking built in: clear separation between human-written and AI-generated content
- Source-integrated reading with AI actions (summarize, explain, find related ideas)

## Relationship to the Wiki Landscape

NotebookLM occupies a different point in the AI knowledge management space than the tools tracked elsewhere in this wiki:

| Dimension | NotebookLM | [[llm-wiki-pattern]] | [[claude-code]] |
|-----------|------------|---------------------|-----------------|
| Source grounding | User-uploaded docs | User-curated raw files | Codebase + CLAUDE.md |
| Knowledge persistence | Notes (session-scoped) | Wiki pages (permanent, interlinked) | Auto memory + CLAUDE.md |
| AI role | Conversational assistant | Wiki maintainer | Coding agent |
| Cross-reference | Manual / AI-suggested | Automatic wikilinks | File references |
| Provenance | Written vs. Saved notes | Source frontmatter | Git history |

NotebookLM is interactive and session-oriented; the [[llm-wiki-pattern]] is cumulative and persistent. Both share the principle that the human curates sources and the AI processes them.

## Limitations (as of March 2024)

- 5,000-word ceiling on note queries
- No native cross-notebook note sharing
- Saved Responses not editable

## See Also
- [[steven-johnson]]
- [[notebooklm-notes-guide]]
- [[llm-wiki-pattern]]
- [[context-management]]
