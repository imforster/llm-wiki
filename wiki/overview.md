---
type: overview
created: 2026-04-07
updated: 2026-04-14
tags: [meta, overview]
---

# LLM Wiki — Agentic AI Landscape

A persistent, compounding knowledge base about the agentic AI ecosystem, built and maintained by an LLM following the [[llm-wiki-pattern]] proposed by [[andrej-karpathy]].

## What This Wiki Is

Instead of re-deriving knowledge from scratch on every question (like RAG), this wiki **incrementally compiles and maintains** a structured, interlinked collection of markdown files. Every source ingested updates entity pages, concept pages, cross-references, and synthesis — so the knowledge compounds over time.

The human curates sources, directs analysis, and asks questions. The LLM does everything else — summarizing, cross-referencing, filing, and bookkeeping.

## What's Inside

33 sources across tools, standards, methodologies, evaluation, memory, multi-agent frameworks, economics, governance, and industry analysis:

**Tools**: [[scion]] (GCP), [[kiro]] (AWS), [[claude-code]] (Anthropic), [[fabric]] (Miessler), [[pai]] (Miessler), [[paperclip]] (company-level orchestration), [[promptfoo]] (eval tooling), [[notebooklm]] (Google Labs), [[mem0]] (memory management)

**Methodologies**: [[spec-kit]] (GitHub), [[bmad-method]] (agile AI-driven), [[ten-pillars-agentic-skill-design]] (Forster)

**Standards**: [[agent-skills-standard]] (agentskills.io), [[mcp-protocol]] (Model Context Protocol)

**Evaluation & Benchmarks**: [[anthropic-eval-guide]], [[evaluating-agent-skills-caparas]], [[promptfoo]], [[humaneval-benchmark]] (code gen, 96.3%), [[swe-bench]] (real-world SE, 74.4%), [[gaia-benchmark]] (general AI, humans 92% vs AI <50%), [[agentbench]] (8 interactive environments)

**Memory & Persistence**: [[mem0-memory-management]] (LOCOMO benchmarks), [[continuum-memory-architectures]] (CMA formal requirements), [[agent-memory-systems-2026]] (four patterns), [[efficient-memory-architectures]] (H-MEM, MemGPT, GraphRAG)

**Multi-Agent Frameworks**: [[autogen-multi-agent]] (Microsoft, 56.8K stars), [[crewai-multi-agent]] (role-based teams), [[langgraph-agent-orchestration]] (stateful graphs), [[openai-swarm]] (minimal handoffs)

**Economics, Governance & Industry**: [[agent-cost-economics]] ($5T bet, token optimization), [[agentic-ai-governance]] (five pillars, NIST/EU AI Act), [[agentic-ai-non-code-domains]] (6 industries), [[agentic-ux-patterns]] (6 UX patterns for trust)

**Practitioner Insights**: [[ai-technique-podcast]], [[skills-pipeline-sleestk]]

## The Emerging Stack

Six distinct layers have emerged across 33 sources:

| Layer | Representatives | Focus |
|-------|----------------|-------|
| **Company** | [[paperclip]] | Org charts, budgets, governance, goal alignment |
| **Methodology** | [[spec-kit]], [[bmad-method]] | Specs, plans, tasks, quality gates, agile workflows |
| **Infrastructure** | [[scion]], [[langgraph-agent-orchestration]], [[autogen-multi-agent]] | Containers, runtimes, graph orchestration, state machines |
| **Tool** | [[claude-code]], [[kiro]], [[crewai-multi-agent]] | Agentic loop, skills, hooks, MCP, permissions |
| **Pattern** | [[fabric]], [[agent-skills-standard]], [[openai-swarm]] | Curated prompts, composable strategies, handoff patterns |
| **Memory** | [[mem0]], [[agent-memory-persistence]] | Persistence, retrieval, forgetting, knowledge graphs |

## Key Themes

Across 33 sources, the original eight themes have deepened and four new ones have emerged:

**Original themes (strengthened):**
- **Context beats clever prompting** — now backed by memory architecture research showing 93% token reduction with selective retrieval ([[mem0-memory-management]])
- **Composition over monoliths** — validated across all four open-source frameworks (AutoGen, CrewAI, LangGraph, Swarm)
- **The human stays in the loop — but how much?** — now formalized as six UX patterns with measurable metrics ([[agentic-ux-patterns]])
- **Memory is the unsolved frontier** — no longer unsolved: CMA defines six formal requirements, Mem0 provides benchmarks, four architecture patterns documented ([[agent-memory-persistence]])
- **Evaluation is the weakest link** — now covered from code generation (96.3%) through real-world SE (74.4%) to general reasoning (humans 92% vs AI <50%) ([[agent-benchmarks]])

**New themes from expanded coverage:**
- **Graphs are becoming the consensus orchestration architecture** — both AutoGen (MAF) and LangGraph converging on graph-based workflows
- **Token economics drive architecture decisions** — 60-80% of agent tokens are waste; optimization is an architectural concern, not just a billing one ([[agent-cost-economics]])
- **Governance is the next frontier** — 68% of employees use AI without IT approval; five-pillar governance framework emerging alongside NIST/EU AI Act ([[agentic-ai-governance]])
- **Agentic AI is expanding beyond code** — finance (40-60% compliance reduction), legal (existential SaaS disruption), healthcare, manufacturing ([[agentic-ai-non-code-domains]])

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

- **Sources** — 33 raw sources that feed this wiki
- **Concepts** — 22 concept pages covering patterns, standards, and architectural ideas
- **Entities** — 17 pages for tools, people, and organizations
- **Analyses** — 4 synthesized analyses filed back into the wiki
