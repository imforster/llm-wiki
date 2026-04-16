---
type: analysis
created: 2026-04-15
updated: 2026-04-15
sources: ["[[mem0-memory-management]]", "[[continuum-memory-architectures]]", "[[agent-memory-systems-2026]]", "[[efficient-memory-architectures]]", "[[cross-source-themes]]", "[[personal-ai-infrastructure]]", "[[claude-code-docs]]", "[[llm-wiki-karpathy]]"]
tags: [analysis, memory, architecture, persistence, forgetting, benchmarks]
---

# How AI Agents Remember: A Comparison of Memory Architectures

Synthesized from 8 sources across this wiki. This analysis compares the four dominant memory architecture patterns, maps them against formal requirements from cognitive science, and provides a practical decision framework for choosing the right approach.

---

## The Core Problem

LLMs are stateless. Every session starts blank. Without persistent memory, agents re-discover known information, repeat mistakes, and can't build on prior work. But persistent memory introduces its own risks: stale facts, compounding errors, and growing retrieval noise. This is the fundamental tension the [[cross-source-themes]] identified as "the unsolved frontier."

Four sources ingested in April 2026 have moved this from "unsolved" to "understood with clear tradeoffs."

---

## Why RAG Is Not Enough

Standard RAG treats memory as a stateless lookup table ([[continuum-memory-architectures]]). It fails on six dimensions:

| Requirement | What It Means | RAG Support |
|-------------|--------------|-------------|
| Persistence | State survives across sessions | ✅ Partial (stores persist, but no identity continuity) |
| Selective Retention | Old/irrelevant memories fade | ❌ Everything persists equally |
| Retrieval-Driven Mutation | Lookups change future accessibility | ❌ Read-only retrieval |
| Associative Routing | Multi-hop traversal across entities | ❌ Embedding distance only |
| Temporal Continuity | "What happened around X?" | ❌ Time is metadata, not structure |
| Consolidation | Episodes compress into knowledge | ❌ No abstraction mechanism |

CMA won 82 of 92 decisive trials against a RAG baseline. The evidence is clear: RAG is a starting point, not a destination.

---

## Four Failure Modes of Flat Vector Storage

Before choosing an architecture, understand what goes wrong with the simplest approach ([[efficient-memory-architectures]]):

1. **Context Poisoning** — Agent stores its own hallucinations, retrieves them later, compounds errors in a feedback loop. The most dangerous failure mode for autonomous agents.

2. **Context Distraction** — Vector DB returns top-10 semantically similar entries, but semantic similarity ≠ relevance. Critical information buried under noise. LLM attention diluted.

3. **Context Clash** — Contradictory facts loaded simultaneously (old address + new address). Agent guesses which is current. Often guesses wrong.

4. **Work Duplication** — In multi-agent systems without shared memory, agents duplicate each other's work. Computational waste multiplies, state diverges.

---

## The Four Architecture Patterns

### Pattern 1: Vector-Only

Store text embeddings in a vector database. Search by cosine similarity.

- **Tools**: Pinecone, Chroma, Weaviate, Qdrant
- **Strengths**: Fast (p95 < 50ms), mature tooling, easy to start
- **Weaknesses**: No relationships, no time awareness, no contradiction detection
- **Cost**: ~$0.10-0.50/GB/month. Free tiers available.
- **Best for**: RAG apps, document Q&A, prototyping, tight budgets
- **CMA compliance**: 1/6 (persistence only)

### Pattern 2: Graph + Vector (Mem0 Style)

Combine graph databases with vector embeddings. Entities as nodes, relationships as edges. Semantic search + graph traversal.

- **Tools**: [[mem0]], Neo4j + embeddings
- **Strengths**: Understands relationships, multi-hop reasoning, temporal awareness, contextual retrieval
- **Weaknesses**: More complex setup, higher learning curve, graph ETL maintenance (budget 20-30% engineering time)
- **Cost**: Similar to vector-only for storage. [[mem0]] abstracts infrastructure.
- **Best for**: Autonomous agents, customer service, research assistants, long-term autonomy
- **CMA compliance**: 4/6 (persistence, selective retention, associative routing, partial temporal)

**Benchmark** (LOCOMO): Mem0g achieves 68.4% accuracy at 1,800 tokens vs full-context 72.9% at 26,000 tokens. That's 93% fewer tokens for a 4.5-point accuracy tradeoff.

### Pattern 3: File + Database Hybrid

Markdown files in directories with a lightweight index (SQLite, frontmatter). Human-readable, git-compatible.

- **Tools**: Markdown + SQLite, Obsidian, this wiki ([[llm-wiki-pattern]])
- **Strengths**: Human-readable, git version control, easy to debug, portable, transparent
- **Weaknesses**: Manual schema management, no built-in semantic search, harder to scale past ~200 files
- **Cost**: Essentially free (filesystem + optional SQLite)
- **Best for**: Solo developers, small teams, personal knowledge management, situations where debuggability matters more than speed
- **CMA compliance**: 2/6 (persistence, partial consolidation via manual curation)

**Key insight**: This wiki itself is a File + Database Hybrid memory system. The [[llm-wiki-pattern]] is a legitimate memory architecture — not just a note-taking approach.

### Pattern 4: Hierarchical Memory

Multi-tier memory inspired by cognitive science. Information flows between layers based on importance and access patterns.

- **Implementations**:
  - **H-MEM**: Domain → Category → Memory Trace → Episode. Index-based routing eliminates irrelevant branches early.
  - **MemGPT**: OS-inspired paging. Small Core Memory (always in context) + massive External Context (archival). Token savings exceeding 90%.
  - **[[pai]]**: Three-tier hot/warm/cold with continuous signal capture and self-modification.
- **Strengths**: Mimics human cognition, efficient resource use, good for long-lived agents
- **Weaknesses**: Complex to implement, needs tuning for promotion/demotion rules, overkill for simple agents
- **Cost**: Infrastructure varies. MemGPT reduces token costs 90% (10,000 → 1,000 tokens).
- **Best for**: Enterprise agents, agents running days/weeks, multi-tenant SaaS
- **CMA compliance**: 5/6 (all except full retrieval-driven mutation in most implementations)

---

## Decision Matrix

| Factor | Vector-Only | Graph+Vector | File+DB | Hierarchical |
|--------|-------------|-------------|---------|-------------|
| Semantic Search | ★★★ | ★★★ | ★★ | ★★ |
| Relationship Queries | ★ | ★★★ | ★★ | ★★ |
| Debuggability | ★★ | ★★ | ★★★ | ★★ |
| Setup Complexity | Low | Medium | Low | High |
| Scalability | ★★★ | ★★ | ★★ | ★★ |
| Token Efficiency | ★★ | ★★★ | ★★★ | ★★★ |
| CMA Compliance | 1/6 | 4/6 | 2/6 | 5/6 |
| Monthly Cost | $0.10-0.50/GB | Similar | ~Free | Variable |

### When to Use What

```
Simple Q&A / RAG app?           → Vector-Only
Autonomous agent, long-running? → Graph + Vector (Mem0)
Solo dev, want transparency?    → File + Database (wiki pattern)
Enterprise, multi-tenant?       → Hierarchical (MemGPT / H-MEM)
```

### Progression Path

Start simple, add complexity when you hit real problems:

1. **Start**: Vector-Only (prototype, validate the use case)
2. **Scale**: Add Graph when you need relationships ("who worked with whom on project X?")
3. **Optimize**: Add Hierarchical layers when token costs or retrieval noise become problems
4. **Maintain**: Add Forgetting when the store grows past useful size

---

## The Memory Types That Matter

All four sources converge on the same cognitive science mapping:

| Memory Type | What It Stores | Persistence | Implementation |
|-------------|---------------|-------------|----------------|
| **Working** | Current context window | Session only | LLM context window |
| **Episodic** | Specific past events | Medium-term, decays | Vector DB with timestamps |
| **Semantic** | Persistent facts | Long-term | Knowledge graph or vector DB |
| **Procedural** | Learned skills/workflows | Long-term | Code, PDDL, Pydantic schemas |

**Critical insight from [[mem0-memory-management]]**: Treating all memory identically is the root cause of most production failures. Episodic memories decay faster than semantic ones. Procedural memory is underused but disproportionately valuable.

---

## Forgetting: The Counterintuitive Requirement

Every source agrees: a memory system that never forgets eventually fails.

- **Bjork's Theory of Disuse**: Forgetting is active and adaptive — it protects retrieval quality ([[mem0-memory-management]])
- **Ebbinghaus Curves**: Steep initial decay, reduced rate for reinforced memories ([[efficient-memory-architectures]])
- **RIF Scoring**: RIF = α×Recency + β×Relevance + γ×Utility — tunable per domain ([[efficient-memory-architectures]])
- **CMA Selective Retention**: Memories compete for accessibility based on recency, usage, salience ([[continuum-memory-architectures]])
- **Production results**: Aggressive forgetting reduces vector DB size 40-60% after 30 days

**Domain caveat**: Healthcare, financial, and legal domains may legally require perfect recall. Use tiered archival storage instead of deletion.

---

## How Existing Wiki Tools Handle Memory

The wiki's original sources already documented different memory approaches. The new sources provide the theoretical framework to evaluate them:

| Tool | Pattern | CMA Score | Strength | Weakness |
|------|---------|-----------|----------|----------|
| [[scion]] | None (fresh per agent) | 0/6 | Clean, no stale data | Re-discovers everything |
| [[claude-code]] | File (CLAUDE.md) + auto | 2/6 | Simple, human-editable | No relationships, no forgetting |
| [[kiro]] | Persistent + learning | 3/6 | Compounds across sessions | Risk of stale memories |
| [[pai]] | Hierarchical (hot/warm/cold) | 5/6 | Most sophisticated | High setup cost |
| [[mem0]] | Graph + Vector | 4/6 | Best benchmarked | Graph maintenance overhead |
| [[llm-wiki-pattern]] | File + Database | 2/6 | Transparent, git-friendly | Manual curation required |

---

## The Extraction Problem: What to Remember

[[mem0-memory-management]] provides the clearest answer with its two-phase pipeline:

**Phase 1 — Extract**: Not every message is memory-worthy. Run an LLM pass to identify discrete, durable facts. Not summaries. Not compressed conversation. Specific facts: "user prefers Python," "project uses PostgreSQL."

**Phase 2 — Update**: Before writing, check against existing store:
- **ADD** — new fact
- **UPDATE** — supersedes existing (user changed jobs)
- **DELETE** — existing fact no longer true
- **NOOP** — duplicate, skip

This resolves contradictions at write time, not query time. The store stays coherent as it grows. This directly addresses the wiki's core tension: "persistent context compounds value AND errors."

---

## Benchmark Summary

| System | Accuracy | Latency (median) | Tokens | Approach |
|--------|----------|-------------------|--------|----------|
| Full-context | 72.9% | 9.87s | ~26,000 | Send everything |
| CMA | 89% win rate | 1.48s | — | Graph + temporal + mutation |
| Mem0g | 68.4% | 1.18s | ~1,800 | Graph + vector |
| A-Mem | 68.6% | — | — | Zettelkasten-inspired |
| Mem0 | 66.9% | 0.71s | ~1,800 | Vector-only selective |
| OpenAI Memory | 52.9% | — | — | Built-in |
| LangMem | 50.9% | — | — | — |
| MemoryBank | 31.3% | — | — | — |

**The core tradeoff**: Full-context is most accurate but 14× more tokens and 7× slower. Selective retrieval (Mem0/CMA) trades ~5% accuracy for 93% token reduction and 7× speed improvement. For any interactive, real-time agent, selective retrieval is the production-viable path.

---

## Recommendations

1. **For most developers starting out**: Use Vector-Only (Pinecone/Chroma). It's the fastest path to working memory. Switch to Graph+Vector when you hit relationship queries or contradiction problems.

2. **For production autonomous agents**: Graph + Vector ([[mem0]]) is the current best balance. Benchmarked, production-tested, handles relationships and forgetting.

3. **For personal knowledge management**: File + Database (the [[llm-wiki-pattern]]). Human-readable, git-friendly, transparent. This wiki proves the pattern works at 33+ sources.

4. **For enterprise/long-running agents**: Hierarchical (MemGPT or [[pai]]-style). The setup cost is high but the token savings and cognitive fidelity pay back at scale.

5. **For everyone**: Implement forgetting. A memory system that never prunes will eventually drown in noise. Start with conservative decay rates and tune based on retrieval quality metrics.

---

## Open Questions

- Can CMA's retrieval-driven mutation be implemented without unacceptable latency at scale?
- How should multi-agent systems share memory without cascading errors? (CRDTs? Event sourcing?)
- What's the right forgetting rate for different domains?
- Can the File + Database pattern (this wiki) be enhanced with semantic search while keeping its transparency?
- How do you audit an evolving memory graph for compliance?

---

*Analysis based on 8 sources ingested into this wiki between 2026-04-07 and 2026-04-14. Represents the state of agent memory architectures as of April 2026.*

## See Also
- [[agent-memory-persistence]]
- [[context-management]]
- [[cross-source-themes]]
- [[agent-cost-economics]]
- [[mem0]]
