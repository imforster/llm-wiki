---
type: overview
created: 2026-04-07
updated: 2026-04-09
tags: [meta, overview]
---

# LLM Wiki — Agentic AI Landscape

A persistent, compounding knowledge base[[wiki/concepts/llm-wiki-pattern]] about the agentic AI ecosystem, built and maintained by an LLM following the [[llm-wiki-pattern]] proposed by [[andrej-karpathy]].

## What This Wiki Is

Instead of re-deriving knowledge from scratch on every question (like RAG), this wiki **incrementally compiles and maintains** a structured, interlinked collection of markdown files. Every source ingested updates entity pages, concept pages, cross-references, and synthesis — so the knowledge compounds over time.

The human curates sources, directs analysis, and asks questions. The LLM does everything else — summarizing, cross-referencing, filing, and bookkeeping.

## What's Inside

14 sources across tools, standards, methodologies, evaluation, and practitioner insights:

**Tools**: [[scion]] (GCP), [[kiro]] (AWS), [[claude-code]] (Anthropic), [[fabric]] (Miessler), [[pai]] (Miessler), [[paperclip]] (company-level orchestration), [[promptfoo]] (eval tooling)

**Standards**: [[agent-skills-standard]] (agentskills.io), [[mcp-protocol]] (Model Context Protocol)

**Methodologies**: [[ten-pillars-agentic-skill-design]] (Forster), [[skill-evaluation]] (Caparas), [[prompt-engineering-patterns]], [[context-management]]

**Evaluation**: [[anthropic-eval-guide]], [[evaluating-agent-skills-caparas]], [[promptfoo]] — from methodology to tooling

**Practitioner Insights**: [[ai-technique-podcast]], [[skills-pipeline-sleestk]] — real-world patterns and skill pipelines

## Key Themes

Across 14 sources, eight themes keep surfacing (see [[cross-source-themes]] for the full analysis):

- **Context beats clever prompting** (9/14 sources) — Progressive disclosure, context documents, selective loading. The strongest consensus in the wiki.
- **Composition over monoliths** (8/14) — Every tool chose small, focused, composable units. No one builds monolithic agents or skills.
- **The human stays in the loop — but how much?** (7/14) — A spectrum from "always interactive" ([[scion]]) to "days of autonomy" ([[kiro]]) to "self-modifying" ([[pai]]). No consensus.
- **Four orchestration layers emerging** — Company ([[paperclip]]), Infrastructure ([[scion]]), Product ([[kiro]]), Tool ([[claude-code]]). See [[multi-agent-orchestration]].
- **Skills evolving into a standard** — Fabric Patterns → Agent Skills Spec → Claude Code Skills → Pipelines + Evaluation. Clear trajectory.
- **Memory is the unsolved frontier** — Persistent context compounds value *and* errors. No one has solved memory hygiene.
- **Open standards winning** — [[mcp-protocol]] + [[agent-skills-standard]] as two-layer open substrate.
- **Evaluation is the weakest link** — Everyone knows it matters. Almost no one does it rigorously. See [[how-to-eval-a-skill]] for a practical framework.

## Analyses

- **[[key-insights-agentic-landscape]]** — 10 key insights across the landscape
- **[[cross-source-themes]]** — 8 common themes with evidence tables from all sources
- **[[ten-pillars-evidence-map]]** — How the wiki validates (and challenges) the Ten Pillars framework
- **[[how-to-eval-a-skill]]** — Practical guide: 5 surfaces, 3 tiers, pass@k, CI/CD integration

## How It Works

Three operations:
- **Ingest**: Drop a source → LLM processes it → creates/updates wiki pages → updates index and log
- **Query**: Ask a question → LLM reads index, synthesizes answer → optionally files back as analysis
- **Lint**: Health-check for contradictions, orphan pages, stale claims, missing cross-references

## Browse

- **Sources** — 14 raw sources that feed this wiki
- **Concepts** — 18 concept pages covering patterns, standards, and architectural ideas
- **Entities** — 12 pages for tools, people, and organizations
- **Analyses** — 4 synthesized analyses filed back into the wiki
