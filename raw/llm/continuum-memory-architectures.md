# Continuum Memory Architectures for Long-Horizon LLM Agents

- **Author**: Joe Logan (Mode7 GK, Tokyo)
- **Source**: https://arxiv.org/html/2601.09913v1
- **Date**: January 2026
- **Type**: Academic paper (arXiv)

## Abstract

RAG treats memory as a stateless lookup table: information persists indefinitely, retrieval is read-only, temporal continuity is absent. CMA (Continuum Memory Architecture) defines a class of systems that maintain and update internal state across interactions through persistent storage, selective retention, associative routing, temporal chaining, and consolidation into higher-order abstractions.

## The Problem with RAG

RAG assumes memory is static storage: items never decay, retrieval never modifies state, temporal order doesn't matter. Systems reconstruct context afresh each time rather than maintaining it, leaving agents without continuity of identity or purpose.

## Six CMA Requirements (Necessary Conditions)

1. **Persistence** — state preserved across sessions. Agent accumulates identity rather than reconstructing from scratch. Fragments ingested days/weeks apart remain addressable without replaying prior transcripts.

2. **Selective Retention** — memories compete for accessibility based on recency, usage, salience, and integration. Inspired by Ebbinghaus forgetting curves and interference studies. Allows privileging updated info while suppressing superseded instructions.

3. **Retrieval-Driven Mutation** — every lookup alters future accessibility. Repeatedly consulted fragments stabilize while contradictory fragments naturally recede. Mirrors retrieval-induced forgetting in biological memory.

4. **Associative Routing** — stores structure connecting people to projects and events to consequences. Activation spreads along links. Enables multi-hop answers even when terms are absent from query.

5. **Temporal Continuity** — episodic traces defined by order as much as content. Explicit temporal edges and episode boundaries. Enables "what was happening around X?" queries.

6. **Consolidation and Abstraction** — sleep-inspired replay and gist extraction. Transforms streams of experience into reusable knowledge. Detailed episodes fade once higher-level schemas emerge.

Standard RAG meets none of these. These are necessary and collectively sufficient conditions for CMA compliance.

## Reference Lifecycle

Memory substrate: structured store where fragments become nodes connected by semantic, temporal, and structural edges. Each node retains reinforcement history, salience, timestamps, provenance.

Activation field: queries inject activation that propagates along edges with decay (spreading-activation theory). Converts intent into graded availability.

Lifecycle engine: ingest → retrieval → mutation → consolidation.
- Ingest: metadata (timestamps, session IDs, salience), edge creation/update, novelty detection, capacity management
- Retrieval: vector/lexical seeds + activation + recency + structural strength (multi-factor ranking)
- Mutation: accessed fragments gain reinforcement, near-misses suppressed, co-retrieved items linked
- Consolidation: background process — replay strengthens temporal chains, abstraction synthesizes themes, gist extraction converts episodes to semantic knowledge

## Behavioral Evaluation Results

Evaluated against Supabase pgvector RAG baseline. Both share identical embeddings (text-embedding-3-small).

| Study | RAG Wins | CMA Wins | Ties | Effect Size |
|-------|----------|----------|------|-------------|
| Knowledge Updates (40 queries) | 1 | 38 | 1 | d=1.84 |
| Temporal Association (30 queries) | 1 | 13 | 2 | h=2.06 |
| Associative Recall (30 queries) | 5 | 14 | 10 | h=0.99 |
| Disambiguation (48 queries) | 3 | 17 | 26 | h=1.55 |
| **Total** | **10** | **82** | **39** | — |

CMA won 82 of 92 decisive trials. Latency increased ~2.4× (mean 1.48s vs 0.65s).

## Failure Modes and Limitations

- **Latency and Scaling** — activation propagation grows with edges. Needs hierarchical storage or cached activation maps.
- **Memory Drift** — retrieval-induced updates can distort facts if feedback loops reinforce incorrect memories.
- **Temporal Sensitivity** — nearly half of temporal queries stumped both systems. Episode-boundary heuristics need work.
- **Interpretability** — evolving graph hard to audit. Needs provenance, reinforcement history, consolidation decision logs.
- **Data Governance** — persistent memories raise privacy/compliance concerns. Needs retention policies, deletion workflows.

## Key Insight

Future agent architectures will be differentiated less by model size and more by how they instantiate memory along CMA dimensions. Memory is an inevitable architectural primitive for reliable agentic systems.

## Related Work Referenced

- MemGPT (Packer et al., 2023) — structured stores alongside conversation
- A-MEM (Xu et al., 2025) — Zettelkasten principles, interconnected knowledge networks (NeurIPS 2025)
- Hindsight (Latimer et al., 2025) — four-network architecture: world facts, agent experiences, entity summaries, evolving beliefs
- SimpleMem (Liu et al., 2026) — highly compressed lifelong stores
- MemoRAG (Qian et al., 2025) — dual-system with global memory formation
