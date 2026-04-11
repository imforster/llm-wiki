---
type: overview
created: 2026-04-07
updated: 2026-04-10
tags: [meta, overview]
---

# LLM Wiki — Agentic AI Landscape

A persistent, compounding knowledge base about the agentic AI ecosystem, built and maintained by an LLM following the [[llm-wiki-pattern]] proposed by [[andrej-karpathy]].

## What This Wiki Is

Instead of re-deriving knowledge from scratch on every question (like RAG), this wiki **incrementally compiles and maintains** a structured, interlinked collection of markdown files. Every source ingested updates entity pages, concept pages, cross-references, and synthesis — so the knowledge compounds over time.

The human curates sources, directs analysis, and asks questions. The LLM does everything else — summarizing, cross-referencing, filing, and bookkeeping.

## What's Inside

16 sources across tools, standards, methodologies, evaluation, and practitioner insights:

**Tools**: [[scion]] (GCP), [[kiro]] (AWS), [[claude-code]] (Anthropic), [[fabric]] (Miessler), [[pai]] (Miessler), [[paperclip]] (company-level orchestration), [[promptfoo]] (eval tooling)

**Methodologies**: [[spec-kit]] (GitHub, spec-driven development), [[bmad-method]] (agile AI-driven development), [[ten-pillars-agentic-skill-design]] (Forster)

**Standards**: [[agent-skills-standard]] (agentskills.io), [[mcp-protocol]] (Model Context Protocol)

**Evaluation**: [[anthropic-eval-guide]], [[evaluating-agent-skills-caparas]], [[promptfoo]] — from methodology to tooling

**Practitioner Insights**: [[ai-technique-podcast]], [[skills-pipeline-sleestk]] — real-world patterns and skill pipelines

## The Emerging Stack

Five distinct layers have emerged across the 16 sources:

| Layer | Tools | Focus |
|-------|-------|-------|
| **Company** | [[paperclip]] | Org charts, budgets, governance, goal alignment |
| **Methodology** | [[spec-kit]], [[bmad-method]] | Specs, plans, tasks, quality gates, agile workflows |
| **Infrastructure** | [[scion]] | Containers, runtimes, harnesses, isolation |
| **Tool** | [[claude-code]], [[kiro]] | Agentic loop, skills, hooks, MCP, permissions |
| **Pattern** | [[fabric]], [[agent-skills-standard]] | Curated prompts, composable strategies, reusable skills |

## Key Themes

Across 16 sources, eight themes keep surfacing (see [[cross-source-themes]] for the full analysis):

- **Context beats clever prompting** (strongest consensus) — Progressive disclosure, context documents, selective loading.
- **Composition over monoliths** — Every tool chose small, focused, composable units.
- **The human stays in the loop — but how much?** — A spectrum from "always interactive" ([[scion]]) to "expert collaborator" ([[bmad-method]]) to "days of autonomy" ([[kiro]]) to "self-modifying" ([[pai]]).
- **Five orchestration layers emerging** — Company, Methodology, Infrastructure, Tool, Pattern.
- **Two methodology philosophies** — "Specs before code" ([[spec-kit]]) vs. "Expert collaboration over autopilot" ([[bmad-method]]). Prescriptive vs. scale-adaptive.
- **Memory is the unsolved frontier** — Persistent context compounds value *and* errors.
- **Open standards winning** — [[mcp-protocol]] + [[agent-skills-standard]] as two-layer open substrate.
- **Evaluation is the weakest link** — See [[how-to-eval-a-skill]] for a practical framework.

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

- **Sources** — 16 raw sources that feed this wiki
- **Concepts** — 18 concept pages covering patterns, standards, and architectural ideas
- **Entities** — 14 pages for tools, people, and organizations
- **Analyses** — 4 synthesized analyses filed back into the wiki
