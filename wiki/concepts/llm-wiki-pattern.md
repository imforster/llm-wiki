---
type: concept
created: 2026-04-08
updated: 2026-04-08
sources: ["[[llm-wiki-karpathy]]"]
tags: [knowledge-management, pattern, methodology, wiki, meta]
---

# LLM Wiki Pattern

A pattern for building personal knowledge bases where the LLM incrementally builds and maintains a persistent, interlinked wiki from raw sources. Proposed by [[andrej-karpathy]]. This wiki is a running instance of this pattern.

## Core Insight

**Wiki > RAG.** RAG rediscovers knowledge from scratch on every query — no accumulation. An LLM-maintained wiki compiles knowledge once and keeps it current. Cross-references, contradictions, and synthesis compound with every source added.

## Three-Layer Architecture

```
Raw Sources (immutable)  →  Wiki (LLM-maintained)  →  Schema (CLAUDE.md)
   you add these              LLM writes these         you + LLM co-evolve
```

1. **Raw sources**: Immutable documents. LLM reads, never modifies.
2. **The wiki**: LLM-generated markdown. Summaries, entities, concepts, comparisons, synthesis. LLM owns entirely.
3. **The schema**: Instructions telling the LLM how the wiki works — structure, conventions, workflows. The key configuration file.

## Three Operations

1. **Ingest**: Process a source → create/update 10-15 wiki pages → update index → append to log
2. **Query**: Read index → find relevant pages → synthesize answer → optionally file back as new page
3. **Lint**: Health-check for contradictions, stale claims, orphan pages, missing cross-references, data gaps

## Navigation

- **index.md**: Content-oriented catalog. LLM reads first on every query. Works at moderate scale (~100 sources, ~hundreds of pages) without embedding infrastructure.
- **log.md**: Chronological append-only record. Parseable with `grep "^## \[" log.md`.

## Why It Works

Humans abandon wikis because maintenance burden grows faster than value. LLMs don't get bored, don't forget cross-references, can touch 15 files in one pass. The maintenance cost is near zero.

The human's job: curate sources, direct analysis, ask good questions, think about meaning.
The LLM's job: everything else.

## Intellectual Lineage

Related to Vannevar Bush's **Memex** (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, connections as valuable as documents. The part he couldn't solve was who does the maintenance.

## Connections to the Ecosystem

- The schema (CLAUDE.md) is effectively a **skill** in the [[agent-skills-standard]] sense — instructions that shape agent behavior for a domain
- Index-first navigation is a form of **[[context-management]]** — selective loading, same principle as progressive disclosure
- Could scale to **[[multi-agent-orchestration]]**: separate agents for ingest, query, lint, with the wiki as shared state
- **[[claude-code]]**'s CLAUDE.md and auto memory are the native implementation substrate

## See Also
- [[andrej-karpathy]]
- [[context-management]]
- [[agent-skills-standard]]
- [[claude-code]]
- [[multi-agent-orchestration]]
