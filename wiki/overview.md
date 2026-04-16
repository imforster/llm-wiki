---
type: overview
created: 2026-04-07
updated: 2026-04-15
tags: [meta, overview]
---

# LLM Wiki — Agentic AI Landscape

A persistent, compounding knowledge base about the agentic AI ecosystem, built and maintained by an LLM following the [[llm-wiki-pattern]] proposed by [[andrej-karpathy]].

## What This Wiki Is

Instead of re-deriving knowledge from scratch on every question (like RAG), this wiki **incrementally compiles and maintains** a structured, interlinked collection of markdown files. Every source ingested updates entity pages, concept pages, cross-references, and synthesis — so the knowledge compounds over time.

The human curates sources, directs analysis, and asks questions. The LLM does everything else — summarizing, cross-referencing, filing, and bookkeeping.

## What's Inside

39 sources across tools, standards, methodologies, evaluation, memory, multi-agent frameworks, economics, governance, industry analysis, and production guides:

**Tools**: [[scion]] (GCP), [[kiro]] (AWS), [[claude-code]] (Anthropic), [[fabric]] (Miessler), [[pai]] (Miessler), [[paperclip]] (company-level orchestration), [[promptfoo]] (eval tooling), [[notebooklm]] (Google Labs), [[mem0]] (memory management)

**Methodologies**: [[spec-kit]] (GitHub), [[bmad-method]] (agile AI-driven), [[ten-pillars-agentic-skill-design]] (Forster)

**Standards**: [[agent-skills-standard]] (agentskills.io), [[mcp-protocol]] (Model Context Protocol)

**Evaluation & Benchmarks**: [[anthropic-eval-guide]], [[evaluating-agent-skills-caparas]], [[promptfoo]], [[humaneval-benchmark]] (code gen, 96.3%), [[swe-bench]] (real-world SE, 74.4%), [[gaia-benchmark]] (general AI, humans 92% vs AI <50%), [[agentbench]] (8 interactive environments)

**Memory & Persistence**: [[mem0-memory-management]] (LOCOMO benchmarks), [[continuum-memory-architectures]] (CMA formal requirements), [[agent-memory-systems-2026]] (four patterns), [[efficient-memory-architectures]] (H-MEM, MemGPT, GraphRAG), [[memory-lifecycle-drift]] (decay, contradiction, confidence, compression, expiry), [[langgraph-mem0-integration]] (LangGraph + Mem0 tutorial), [[shared-agent-memory]] (multi-agent shared memory patterns)

**Multi-Agent Frameworks**: [[autogen-multi-agent]] ([Microsoft](https://github.com/microsoft/autogen), 56.8K stars), [[crewai-multi-agent]] ([CrewAI](https://github.com/crewAIInc/crewAI), role-based teams), [[langgraph-agent-orchestration]] ([LangGraph](https://github.com/langchain-ai/langgraph), stateful graphs), [[openai-swarm]] ([Swarm](https://github.com/openai/swarm), minimal handoffs), [[crewai-production-guide]] (production patterns and deployment)

**Observability**: [[multi-agent-observability]] (OpenTelemetry tracing, debugging patterns)

**Economics, Governance & Industry**: [[agent-cost-economics]] ($5T bet, token optimization), [[agentic-ai-governance]] (five pillars, NIST/EU AI Act), [[agentic-ai-non-code-domains]] (6 industries), [[agentic-ux-patterns]] (6 UX patterns for trust), [[ai-environmental-impact]] (energy/carbon/water benchmarks, Jevons Paradox)

**Practitioner Insights**: [[ai-technique-podcast]], [[skills-pipeline-sleestk]]

## The Emerging Stack

Six distinct layers have emerged across 39 sources:

| Layer | Representatives | Focus |
|-------|----------------|-------|
| **Company** | [[paperclip]] | Org charts, budgets, governance, goal alignment |
| **Methodology** | [[spec-kit]], [[bmad-method]] | Specs, plans, tasks, quality gates, agile workflows |
| **Infrastructure** | [[scion]], [[langgraph-agent-orchestration]], [[autogen-multi-agent]] | Containers, runtimes, graph orchestration, state machines |
| **Tool** | [[claude-code]], [[kiro]], [[crewai-multi-agent]] | Agentic loop, skills, hooks, MCP, permissions |
| **Pattern** | [[fabric]], [[agent-skills-standard]], [[openai-swarm]] | Curated prompts, composable strategies, handoff patterns |
| **Memory** | [[mem0]], [[agent-memory-persistence]] | Persistence, retrieval, forgetting, knowledge graphs |

## Key Themes

Across 39 sources, twelve themes have been identified (see [[cross-source-themes]] for full evidence tables):

**Strongest themes (10+ sources):**
- **Context beats clever prompting** (15/33) — 93% token reduction with selective retrieval ([[mem0-memory-management]])
- **Composition over monoliths** (14/33) — validated across all OSS frameworks and product tools
- **The human stays in the loop — but how much?** (13/33) — formalized as six UX patterns with metrics ([[agentic-ux-patterns]])
- **Memory architectures are understood** (10/33) — CMA defines six formal requirements, four patterns documented, forgetting is a design requirement ([[agent-memory-persistence]])

**Established themes (5-9 sources):**
- **Evaluation has a framework** (8/33) — from code gen (96.3%) to general reasoning (humans 92% vs AI <50%) ([[agent-benchmarks]])
- **Skills evolving into a standard** (6/33) — Fabric Patterns → Agent Skills Standard → Claude Code Skills
- **Git as universal substrate** (6/33) — every tool uses git for coordination
- **Open standards winning** (5/33) — MCP + Agent Skills as two-layer open substrate
- **Token economics drive architecture** (5/33) — 60-80% of tokens are waste ([[agent-cost-economics]])

**Emerging themes (3-4 sources):**
- **Graphs are the consensus orchestration architecture** (4/33) — AutoGen and LangGraph converging
- **Governance is the next frontier** (4/33) — 68% use AI without IT approval ([[agentic-ai-governance]])
- **Agentic AI expanding beyond code** (3/33) — six industries, SaaS disruption ([[agentic-ai-non-code-domains]])

## Analysis

11 synthesized analyses filed back into the wiki:

| Analysis | Focus |
|----------|-------|
| [[key-insights-agentic-landscape]] | 14 key insights across the landscape (refreshed for 33 sources) |
| [[cross-source-themes]] | 12 themes with evidence tables (refreshed for 33 sources) |
| [[ten-pillars-evidence-map]] | How the wiki validates the Ten Pillars framework |
| [[how-to-eval-a-skill]] | Practical eval guide: 5 surfaces, 3 tiers, pass@k |
| [[memory-architecture-comparison]] | Four memory patterns compared, CMA requirements, benchmarks, decision framework |
| [[multi-agent-framework-guide]] | Eight approaches compared (4 OSS + 4 product), graph convergence thesis |
| [[cost-optimization-guide]] | Five waste vectors, optimization playbook, architecture-cost connections |
| [[governance-safety-overview]] | Five governance pillars, regulatory landscape, UX as governance layer |
| [[beyond-code-industry-impact]] | Six industries, wiki themes generalization test, SaaS disruption |
| [[wiki-gap-analysis-apr-2026]] | 20 gaps identified via conversational query testing, 15 addressed |
| [[getting-started-guide]] | Five-phase guide from single agent to multi-agent, cost budgets |

## How It Works

Three operations:
- **Ingest**: Drop a source → LLM processes it → creates/updates wiki pages → updates index and log
- **Query**: Ask a question → LLM reads index, synthesizes answer → optionally files back as analysis
- **Lint**: Health-check for contradictions, orphan pages, stale claims, missing cross-references

## Browse

- **Sources** — 39 raw sources that feed this wiki
- **Concepts** — 20 concept pages covering patterns, standards, and architectural ideas
- **Entities** — 17 pages for tools, people, and organizations
- **Analysis** — 12 synthesized analyses filed back into the wiki
