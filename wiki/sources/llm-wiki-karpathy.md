---
type: source
created: 2026-04-08
updated: 2026-04-08
sources: []
origin: llm
tags: [llm-wiki, knowledge-management, pattern, methodology, meta]
---

# LLM Wiki (Karpathy)

[Original](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) | [Raw](../../raw/llm/llm-wiki-karpathy.md)

Author: [[andrej-karpathy]]

## Summary

The foundational idea file for the LLM Wiki pattern — the methodology this entire wiki is built on. Proposes that instead of RAG (re-deriving knowledge on every query), LLMs should incrementally build and maintain a persistent, interlinked wiki from raw sources. The wiki is a compounding artifact: cross-references already exist, contradictions are flagged, synthesis reflects everything ingested.

## Key Ideas

- **Wiki > RAG**: RAG rediscovers knowledge from scratch every query. A wiki compiles knowledge once and keeps it current. The synthesis compounds.
- **Three-layer architecture**: Raw sources (immutable) → Wiki (LLM-maintained markdown) → Schema (CLAUDE.md/AGENTS.md defining conventions and workflows).
- **Three operations**: Ingest (process source → update 10-15 pages), Query (search index → synthesize answer → optionally file back), Lint (health-check for contradictions, orphans, gaps).
- **Index + Log**: index.md is content-oriented (catalog for navigation), log.md is chronological (append-only timeline). Index-first navigation works at moderate scale without embedding infrastructure.
- **Human role vs. LLM role**: Human curates sources, directs analysis, asks questions, thinks about meaning. LLM does everything else — summarizing, cross-referencing, filing, bookkeeping.
- **Why wikis fail and this doesn't**: Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored, don't forget cross-references, can touch 15 files in one pass. Maintenance cost ≈ zero.
- **Memex lineage**: Related to Vannevar Bush's Memex (1945) — personal knowledge store with associative trails. Bush couldn't solve who does the maintenance. The LLM handles that.

## Meta: This Wiki's Relationship to This Source

This wiki is a direct instantiation of Karpathy's LLM Wiki pattern. Our CLAUDE.md schema implements the three-layer architecture. Our ingest/query/lint workflows follow the operations described. Our index.md and log.md serve exactly the roles specified. The pattern is the blueprint; this wiki is a running instance.

## Connections to Other Sources

- **[[agent-skills-standard]]** and **[[ten-pillars-agentic-skill-design]]**: The wiki schema (CLAUDE.md) functions like a skill — it's instructions that shape agent behavior for a specific domain. Progressive disclosure applies: the schema loads at session start, raw sources load on ingest.
- **[[claude-code]]**: The wiki runs on Claude Code (or similar). CLAUDE.md is the native instruction format. Auto memory complements the wiki's explicit knowledge with implicit learnings.
- **[[context-management]]**: The index-first navigation pattern is a form of selective context loading — read the index (~catalog), then drill into only relevant pages. Same principle as the [[agent-skills-standard]]'s progressive disclosure.
- **[[multi-agent-orchestration]]**: The wiki pattern could scale to multi-agent: one agent ingests, another answers queries, another lints. The wiki itself is the shared state.

## See Also
- [[andrej-karpathy]]
- [[llm-wiki-pattern]]
- [[context-management]]
- [[agent-skills-standard]]
