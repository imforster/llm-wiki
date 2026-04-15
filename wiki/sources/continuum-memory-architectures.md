---
type: source
created: 2026-04-14
updated: 2026-04-14
origin: llm
tags: [memory, architecture, academic, RAG, cognitive-science]
---

# Continuum Memory Architectures for Long-Horizon LLM Agents

[Original](https://arxiv.org/html/2601.09913v1) | [Raw](../../raw/llm/continuum-memory-architectures.md)

Academic paper by Joe Logan (Mode7 GK, Tokyo) defining CMA as a formal architectural class for agent memory. Provides the theoretical foundation for why RAG is insufficient and what properties a real memory system must have.

## The Problem with RAG

RAG treats memory as a stateless lookup table: information persists indefinitely, retrieval is read-only, temporal continuity is absent. Agents reconstruct context afresh each time rather than maintaining it — no continuity of identity or purpose.

## Six CMA Requirements (Necessary Conditions)

1. **Persistence** — state preserved across sessions. Agent accumulates identity.
2. **Selective Retention** — memories compete for accessibility (recency, usage, salience). Ebbinghaus forgetting curves.
3. **Retrieval-Driven Mutation** — every lookup alters future accessibility. Consulted fragments stabilize, contradictory ones recede.
4. **Associative Routing** — structure connecting entities. Activation spreads along links for multi-hop answers.
5. **Temporal Continuity** — episodic traces defined by order. Explicit temporal edges enable "what was happening around X?" queries.
6. **Consolidation and Abstraction** — sleep-inspired replay and gist extraction. Episodes fade once schemas emerge.

Standard RAG meets none of these. These are necessary and collectively sufficient.

## Reference Lifecycle

Ingest → Retrieval → Mutation → Consolidation. Memory substrate is a structured store with semantic, temporal, and structural edges. Each node retains reinforcement history, salience, timestamps, provenance.

## Evaluation Results (vs RAG Baseline)

CMA won 82 of 92 decisive trials across four behavioral probes. Latency increased ~2.4× (1.48s vs 0.65s).

| Study | RAG Wins | CMA Wins | Effect Size |
|-------|----------|----------|-------------|
| Knowledge Updates | 1 | 38 | d=1.84 |
| Temporal Association | 1 | 13 | h=2.06 |
| Associative Recall | 5 | 14 | h=0.99 |
| Disambiguation | 3 | 17 | h=1.55 |

## Failure Modes

- Latency scaling with graph edges
- Memory drift from reinforcement feedback loops
- Temporal sensitivity (half of temporal queries stumped both systems)
- Interpretability of evolving graphs
- Data governance for persistent memories

## Key Insight

Future agent architectures differentiated less by model size, more by how they instantiate memory. Memory is an inevitable architectural primitive.

## Related Work

[[mem0]] (Mem0g), MemGPT, A-MEM (Zettelkasten, NeurIPS 2025), Hindsight (four-network architecture), SimpleMem, MemoRAG.

## See Also
- [[agent-memory-persistence]]
- [[context-management]]
- [[mem0-memory-management]]
