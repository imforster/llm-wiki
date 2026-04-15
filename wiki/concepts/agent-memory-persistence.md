---
type: concept
created: 2026-04-14
updated: 2026-04-14
sources: ["[[mem0-memory-management]]", "[[continuum-memory-architectures]]", "[[agent-memory-systems-2026]]", "[[efficient-memory-architectures]]"]
tags: [memory, persistence, architecture, forgetting, knowledge-graph]
---

# Agent Memory & Persistence

How LLM agents retain, retrieve, and manage knowledge across sessions. Identified as "the unsolved frontier" in [[cross-source-themes]] — the biggest divergence across tools in the wiki.

## The Core Problem

LLMs are stateless by design. Context windows reset at session end. Without persistent memory, agents start fresh every time, making the same mistakes and asking the same questions. But persistent context compounds value AND errors — the fundamental tension.

## Memory Architecture Patterns

Four patterns have emerged (per [[agent-memory-systems-2026]]):

| Pattern | Best For | Key Tradeoff |
|---------|----------|-------------|
| **Vector-Only** | RAG apps, prototyping | Fast but no relationships |
| **Graph + Vector** ([[mem0]]) | Autonomous agents | Relationships + semantic search, more complex |
| **File + Database** ([[llm-wiki-pattern]]) | Solo devs, small teams | Human-readable, git-friendly, no semantic search |
| **Hierarchical** | Enterprise agents | Mimics human cognition, complex to tune |

## Memory Types (Cognitive Science)

From [[mem0-memory-management]] and [[efficient-memory-architectures]], mapped from psychology:

- **Working memory** — active context window. Fast, limited, temporary.
- **Episodic memory** — specific past experiences. Decays in relevance.
- **Semantic memory** — persistent facts. Knowledge graphs or vector DBs.
- **Procedural memory** — learned skills and workflows. Underused, high-value.

Critical insight: treating all memory identically is the root cause of most production failures.

## Four Memory Layers ([[mem0]])

1. Conversation → "what's happening now?"
2. Session → "what's this task's context?"
3. User → "what do I know about this person?"
4. Organizational → "what's universally true?"

## CMA: Formal Requirements ([[continuum-memory-architectures]])

Six necessary conditions for real agent memory (standard RAG meets none):
1. Persistence across sessions
2. Selective retention (forgetting curves)
3. Retrieval-driven mutation (lookups alter future accessibility)
4. Associative routing (graph traversal, multi-hop)
5. Temporal continuity (episode ordering)
6. Consolidation and abstraction (gist extraction)

CMA won 82/92 decisive trials vs RAG baseline.

## Failure Modes of Flat Vector Storage

From [[efficient-memory-architectures]]:
1. **Context Poisoning** — agent retrieves own hallucinations, compounds errors
2. **Context Distraction** — semantic similarity ≠ relevance
3. **Context Clash** — contradictory info loaded simultaneously
4. **Work Duplication** — multi-agent systems without shared memory

## Forgetting as Design Requirement

Both [[mem0-memory-management]] and [[continuum-memory-architectures]] emphasize active forgetting:
- Bjork's "New Theory of Disuse": forgetting protects retrieval quality
- RIF scoring: Recency × Relevance × Frequency
- Ebbinghaus curves: steep initial decay, reinforced memories persist
- Production: 40-60% DB size reduction after 30 days of pruning

## How Wiki Tools Handle Memory

| Tool | Approach | From |
|------|----------|------|
| [[scion]] | No memory (each agent starts fresh) | [[cross-source-themes]] |
| [[claude-code]] | CLAUDE.md + auto memory | [[claude-code-docs]] |
| [[kiro]] | Learns from reviews, persistent | [[kiro-autonomous-agent]] |
| [[pai]] | TELOS (10 files), three-tier hot/warm/cold | [[personal-ai-infrastructure]] |
| [[mem0]] | Graph+vector, four layers, five scopes | [[mem0-memory-management]] |
| [[llm-wiki-pattern]] | Compiled markdown knowledge base | [[llm-wiki-karpathy]] |

## Benchmark Landscape

| System | Accuracy (LOCOMO) | Tokens |
|--------|-------------------|--------|
| Full-context | 72.9% | ~26,000 |
| Mem0g (graph) | 68.4% | ~1,800 |
| A-Mem | 68.6% | — |
| Mem0 (vector) | 66.9% | ~1,800 |
| OpenAI Memory | 52.9% | — |
| LangMem | 50.9% | — |

The 4.5-point accuracy gap between full-context and selective retrieval is the core tradeoff: 93% fewer tokens for ~5% less accuracy.

## See Also
- [[context-management]]
- [[cross-source-themes]]
- [[multi-agent-orchestration]]
- [[mem0]]
- [[llm-wiki-pattern]]
