---
type: overview
created: 2026-04-07
updated: 2026-04-09
tags: [meta, overview]
---

# LLM Wiki — Agentic AI Landscape

A persistent, compounding knowledge base about the agentic AI ecosystem, built and maintained by an LLM following the [[llm-wiki-pattern]] proposed by [[andrej-karpathy]].

## What This Wiki Is

Instead of re-deriving knowledge from scratch on every question (like RAG), this wiki **incrementally compiles and maintains** a structured, interlinked collection of markdown files. Every source ingested updates entity pages, concept pages, cross-references, and synthesis — so the knowledge compounds over time.

The human curates sources, directs analysis, and asks questions. The LLM does everything else — summarizing, cross-referencing, filing, and bookkeeping.

## What's Inside

This wiki tracks the emerging agentic AI landscape across tools, standards, methodologies, and practitioner insights:

**Tools**: [[scion]] (GCP), [[kiro]] (AWS), [[claude-code]] (Anthropic), [[fabric]] (Miessler), [[pai]] (Miessler)

**Standards**: [[agent-skills-standard]] (agentskills.io), [[mcp-protocol]] (Model Context Protocol)

**Methodologies**: [[ten-pillars-agentic-skill-design]] (Forster), [[skill-evaluation]] (Caparas), [[prompt-engineering-patterns]], [[context-management]]

**Practitioner Insights**: [[ai-technique-podcast]] — AI as workflow replacement layer, context documents, daily prompts

**Synthesis**: [[key-insights-agentic-landscape]] — 10 key insights across all sources

## Key Themes

Across 10 sources, several themes keep surfacing:

- **Context beats clever prompting** — From the [[agent-skills-standard]]'s progressive disclosure to [[pai]]'s TELOS to the [[ai-technique-podcast]]'s "context document technique," the consensus is clear: loading the right context matters more than crafting the perfect prompt.
- **Three architectural philosophies competing** — Infrastructure ([[scion]]), Product ([[kiro]]), Tool ([[claude-code]]). No winner yet. See [[multi-agent-orchestration]].
- **Two open standards emerging** — [[mcp-protocol]] (tools/data) and [[agent-skills-standard]] (capabilities). Complementary, not competing.
- **Memory is the unsolved frontier** — From no memory (Scion) to structured self-knowledge (PAI's TELOS). Persistent context compounds value *and* errors.
- **The personal AI vision is bigger than coding** — [[llm-wiki-pattern]], [[pai]], and the [[ai-technique-podcast]] all point to persistent, personalized AI infrastructure that compounds across all domains.

## How It Works

Three operations:
- **Ingest**: Drop a source → LLM processes it → creates/updates 10-15 wiki pages → updates index and log
- **Query**: Ask a question → LLM reads index, finds relevant pages, synthesizes answer → optionally files back as analysis
- **Lint**: Health-check for contradictions, orphan pages, stale claims, missing cross-references

## Browse

- **[[key-insights-agentic-landscape]]** — Start here for the big picture
- **Sources** — 10 raw sources that feed this wiki
- **Concepts** — 18 concept pages covering patterns, standards, and architectural ideas
- **Entities** — 10 pages for tools, people, and organizations
- **Analyses** — Synthesized insights filed back into the wiki
