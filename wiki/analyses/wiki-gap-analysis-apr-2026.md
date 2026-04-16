---
type: analysis
created: 2026-04-15
updated: 2026-04-15
sources: ["[[memory-architecture-comparison]]", "[[multi-agent-framework-guide]]", "[[cost-optimization-guide]]", "[[governance-safety-overview]]", "[[beyond-code-industry-impact]]"]
tags: [analysis, gaps, query, roadmap]
---

# Wiki Gap Analysis: What's Still Missing (April 2026)

Generated from a conversational query test: "If I wanted to build a long-running autonomous agent that manages a small team's knowledge base, what does the wiki recommend?" The wiki provided strong architectural guidance but exposed five gaps where sources are needed.

---

## Gap 1: No "Getting Started" Guide

The wiki has architecture comparisons and decision matrices, but no step-by-step guide for building a first long-running agent. The analyses tell you *what* to choose but not *how* to wire it together.

**What's needed**: A practical tutorial covering: project setup → memory configuration → agent definition → workflow graph → human-in-the-loop gates → deployment → monitoring. Ideally using LangGraph + Mem0 since the wiki recommends both.

**Priority**: High — this is the bridge between the wiki's knowledge and hands-on application.

## Gap 2: LangGraph + Mem0 Integration

The wiki recommends LangGraph for orchestration and Mem0 for memory, but no source covers how they work together. Memory operations as graph nodes in a LangGraph workflow is the obvious architecture, but it's undocumented in the wiki.

**What's needed**: Source or tutorial on integrating memory retrieval/storage as LangGraph nodes. How checkpointed state interacts with persistent memory. How to scope memory per agent in a multi-agent graph.

**Priority**: High — these are the wiki's top two recommendations and they need to connect.

## Gap 3: Non-Code Knowledge Management Agents

The wiki has the [[llm-wiki-pattern]] (this wiki) and [[pai]] (personal AI), but nothing on team-level knowledge management agents. The [[beyond-code-industry-impact]] analysis covers industries but not this specific use case.

**What's needed**: Sources on AI agents for team wikis, shared knowledge bases, research synthesis, document management. How do the patterns differ from solo knowledge management?

**Priority**: Medium — directly relevant to the user's stated goals but less foundational than gaps 1-2.

## Gap 4: Knowledge Quality Evaluation

The [[agent-benchmarks]] cover code generation (HumanEval), software engineering (SWE-bench), general reasoning (GAIA), and interactive agents (AgentBench). But how do you measure whether a knowledge management agent is doing a good job?

**What's needed**: Metrics and evaluation approaches for: accuracy of cross-references, completeness of entity extraction, freshness of information, quality of synthesis, detection of contradictions. The wiki's own lint operation is a primitive version of this.

**Priority**: Medium — connects to the user's concern about trusting agent output.

## Gap 5: Agent Observability Tooling

The [[governance-safety-overview]] says "log reasoning chains" and "behavioral baselines," but no source covers the actual tools for monitoring long-running agents in practice.

**What's needed**: Sources on LangSmith, Weights & Biases, Helicone, custom logging approaches. How to set up dashboards for agent health. What metrics to track for long-running agents (token consumption trends, error rates, memory growth, retrieval quality degradation).

**Priority**: Medium — operational concern that becomes critical at production scale.

---

## Mapping Gaps to Next Actions

| Gap | Action | Type |
|-----|--------|------|
| 1. Getting started guide | Write as analysis (hands-on project from Six Thinking Hats) | Create |
| 2. LangGraph + Mem0 | Search for integration sources | Research |
| 3. Team knowledge agents | Search for sources | Research |
| 4. Knowledge quality eval | Search for sources or derive from existing eval framework | Research/Create |
| 5. Observability tooling | Search for sources | Research |

## See Also
- [[memory-architecture-comparison]]
- [[multi-agent-framework-guide]]
- [[cost-optimization-guide]]
- [[agent-benchmarks]]
- [[skill-evaluation]]
