---
type: overview
created: 2026-04-07
updated: 2026-04-08
tags: [meta, overview]
---

# LLM Wiki — Agentic AI Landscape

A persistent, compounding knowledge base about the agentic AI ecosystem, built and maintained by an LLM following the [[llm-wiki-pattern]] proposed by [[andrej-karpathy]].

## What This Wiki Is

Instead of re-deriving knowledge from scratch on every question (like RAG), this wiki **incrementally compiles and maintains** a structured, interlinked collection of markdown files. Every source ingested updates entity pages, concept pages, cross-references, and synthesis — so the knowledge compounds over time.

The human curates sources, directs analysis, and asks questions. The LLM does everything else — summarizing, cross-referencing, filing, and bookkeeping.

## What's Inside

This wiki tracks the emerging agentic AI landscape across tools, standards, and methodologies:

**Tools**: [[scion]] (GCP), [[kiro]] (AWS), [[claude-code]] (Anthropic), [[fabric]] (Miessler), [[pai]] (Miessler)

**Standards**: [[agent-skills-standard]] (agentskills.io), [[mcp-protocol]] (Model Context Protocol)

**Methodologies**: [[ten-pillars-agentic-skill-design]] (Forster), [[skill-evaluation]] (Caparas), [[prompt-engineering-patterns]], [[context-management]]

**Synthesis**: [[key-insights-agentic-landscape]] — 10 key insights across all sources

## How It Works

Three operations:
- **Ingest**: Drop a source → LLM processes it → creates/updates 10-15 wiki pages → updates index and log
- **Query**: Ask a question → LLM reads index, finds relevant pages, synthesizes answer → optionally files back as analysis
- **Lint**: Health-check for contradictions, orphan pages, stale claims, missing cross-references

## Browse

- **[[key-insights-agentic-landscape]]** — Start here for the big picture
- **Sources** — The 9 raw sources that feed this wiki
- **Concepts** — 18 concept pages covering patterns, standards, and architectural ideas
- **Entities** — 10 pages for tools, people, and organizations
- **Analyses** — Synthesized insights filed back into the wiki
