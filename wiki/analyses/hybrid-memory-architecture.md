---
type: analysis
created: 2026-04-15
updated: 2026-04-15
sources: ["[[memory-architecture-comparison]]", "[[mem0-memory-management]]", "[[continuum-memory-architectures]]", "[[langgraph-mem0-integration]]", "[[memory-lifecycle-drift]]", "[[llm-wiki-karpathy]]", "[[agent-memory-systems-2026]]"]
tags: [analysis, memory, hybrid, wiki, mem0, architecture]
---

# Hybrid Memory Architecture: Combining Wiki + Mem0

A novel architecture combining the File+Database pattern (this wiki) with Graph+Vector retrieval ([[mem0]]). Neither pattern alone achieves full CMA compliance — together they reach 5/6, matching [[pai]]'s hierarchical approach but with full transparency.

---

## Why Neither Pattern Is Enough Alone

| Capability | Wiki (File+DB) | Mem0 (Graph+Vector) |
|-----------|---------------|-------------------|
| Fast retrieval (<100ms) | ❌ | ✅ |
| Deep synthesis | ✅ | ❌ |
| Human-readable | ✅ | ❌ |
| Automatic forgetting | ❌ | ✅ |
| Contradiction detection | Manual (lint) | Automatic (write-time) |
| Relationship queries | Via wikilinks (manual) | Graph traversal (automatic) |
| Git version history | ✅ | ❌ |
| CMA compliance | 2/6 | 4/6 |

The wiki excels at depth, transparency, and synthesis. Mem0 excels at speed, automation, and relationships. They're complementary.

---

## The Three-Layer Hybrid

### Layer 1: Mem0 as Fast Memory (Working + Session + User)

Handles what needs to be fast and automatic:
- Session context (current task)
- User preferences ("prefers Python," "uses LangGraph")
- Entity relationships ("Mem0 is a tool," "CMA is from Logan's paper")
- Contradiction resolution (ADD/UPDATE/DELETE/NOOP at write time)
- Forgetting (automatic decay, confidence scoring per [[memory-lifecycle-drift]])

Sub-second retrieval. 1,800 tokens instead of 26,000. Queried on every agent interaction.

### Layer 2: Wiki as Deep Memory (Semantic + Organizational)

Handles what needs depth and transparency:
- Synthesized analyses (11 analyses connecting patterns across 39 sources)
- Cross-references (wikilinks surfacing non-obvious connections)
- Provenance (every claim traces to a source page)
- Human curation (user decides what matters, LLM files it)
- Version history (git tracks every change)

Consulted for deep questions requiring multi-page synthesis.

### Layer 3: The Bridge (Bidirectional Sync)

**Wiki → Mem0 (index extraction)**:
- Extract discrete facts from wiki pages into Mem0
- Entity pages → Mem0 entity nodes with relationships
- Concept summaries → high-confidence semantic memories
- Wiki cross-references → graph edges in Mem0g
- Result: wiki knowledge available for fast retrieval

**Mem0 → Wiki (consolidation)**:
- Periodically promote important Mem0 memories into wiki pages
- Review high-importance, high-confidence memories weekly
- Patterns and insights become wiki concept pages or analyses
- Wiki grows from daily interactions, not just source ingestion
- This is the [[memory-lifecycle-drift]] compression pattern applied across systems

---

## The Flow

```
Daily agent interactions
    ↓
Mem0 (fast: extract facts, resolve contradictions, decay old)
    ↓ weekly consolidation
Wiki (deep: synthesize, cross-reference, analyze, version)
    ↓ index extraction
Mem0 (wiki knowledge available for fast retrieval)
```

---

## CMA Compliance: Hybrid vs Individual

| CMA Requirement | Wiki | Mem0 | Hybrid |
|----------------|------|------|--------|
| 1. Persistence | ✅ | ✅ | ✅ |
| 2. Selective Retention | ❌ (manual lint) | ✅ (decay + RIF) | ✅ |
| 3. Retrieval-Driven Mutation | ❌ | ❌ (partial) | ❌ |
| 4. Associative Routing | ❌ (wikilinks are manual) | ✅ (graph traversal) | ✅ |
| 5. Temporal Continuity | ❌ | ✅ (partial) | ✅ |
| 6. Consolidation & Abstraction | ✅ (analyses) | ❌ | ✅ |
| **Score** | **2/6** | **4/6** | **5/6** |

The only missing CMA property is full retrieval-driven mutation (lookups altering future accessibility). This could be added by tracking which Mem0 memories are retrieved and boosting their reinforcement scores — the [[memory-lifecycle-drift]] access_count pattern.

---

## When to Use Which Layer

```
Quick factual question?              → Mem0 (fast retrieval)
  "What memory pattern does Scion use?"

Deep synthesis question?             → Wiki (read pages, synthesize)
  "How do memory architectures compare?"

New information from interaction?    → Mem0 (automatic extraction)
  User mentions a new tool preference

Pattern emerging across interactions? → Wiki (consolidate from Mem0)
  Multiple Mem0 memories about the same theme

Need to audit/debug?                 → Wiki (human-readable, git history)
  "Why does the agent think I use PostgreSQL?"
```

---

## Implementation Steps

### Phase 1: Set Up Mem0 Alongside Wiki
- Install Mem0 per [[langgraph-mem0-integration]]
- Configure for your user_id
- Don't change wiki workflow — Mem0 is additive

### Phase 2: Extract Wiki Index into Mem0
- Script reads `wiki/index.md`
- Creates Mem0 memories from entity summaries, concept summaries
- Tags with source provenance (wiki page slug)
- High confidence (0.9) since wiki content is curated

### Phase 3: Build Daily Interaction Memory
- Agent interactions store facts in Mem0 automatically
- Contradiction detection catches preference changes
- Decay handles staleness
- This runs independently of wiki

### Phase 4: Build the Consolidation Loop
- Weekly: query Mem0 for high-importance, high-confidence, high-access memories
- Review for patterns that deserve wiki pages
- Promote to wiki concept pages or analyses
- Mark promoted Mem0 memories as "consolidated"

### Phase 5: Close the Loop
- New wiki pages get extracted back into Mem0 (Phase 2 runs on new content)
- The system becomes self-reinforcing: interactions → Mem0 → wiki → Mem0

---

## Cost Estimate

| Component | Monthly Cost |
|-----------|-------------|
| Mem0 (self-hosted, free tier) | $0 |
| Mem0 (cloud, moderate usage) | $20-50 |
| Wiki (filesystem + git) | $0 |
| Extraction script (weekly, gpt-4o-mini) | $1-5 |
| Consolidation review (weekly, human time) | 30 min/week |

Total: $1-55/month depending on Mem0 hosting choice. The wiki itself remains free.

---

## What This Architecture Enables

1. **Fast answers from deep knowledge** — Mem0 retrieves wiki-sourced facts in <100ms
2. **Knowledge that grows from daily work** — interactions consolidate into wiki analyses
3. **Transparent and auditable** — wiki layer is human-readable, git-versioned
4. **Self-maintaining** — Mem0 handles forgetting and contradictions automatically
5. **Blog content pipeline** — wiki analyses (fed by Mem0 consolidation) become blog post drafts

This directly supports the Six Thinking Hats goal: wiki as content engine for writing and teaching, powered by daily interaction memory.

---

*Novel architecture synthesized from 7 wiki sources. Not documented in any single source — emerges from combining the wiki's File+DB pattern with Mem0's Graph+Vector pattern.*

## See Also
- [[memory-architecture-comparison]]
- [[agent-memory-persistence]]
- [[langgraph-mem0-integration]]
- [[memory-lifecycle-drift]]
- [[llm-wiki-pattern]]
- [[getting-started-guide]]
