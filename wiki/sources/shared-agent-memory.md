---
type: source
created: 2026-04-15
updated: 2026-04-15
origin: llm
tags: [multi-agent, shared-memory, conflict, deduplication, vector-store]
---

# Shared Agent Memory: Stopping Agents from Repeating Work

[Original](https://www.roborhythms.com/how-to-stop-ai-agents-repeating-work-2026/) | [Raw](../../raw/llm/shared-agent-memory.md)

Tutorial (Cole, RoboRhythms, April 2026) on shared memory layers for multi-agent systems. Fills gaps #14 (conflict resolution), #15 (shared state patterns), #16 (consensus).

## The Pattern

Solution store + write hook (after task) + retrieval step (BEFORE task) + similarity threshold (~0.85). The retrieval step must be unconditional — if agents don't check before starting, the store is decoration.

## Memory Pattern Options

Key-value (exact match, Redis) → Vector similarity (similar tasks, Chroma/Pinecone) → Graph store (relationships, Neo4j) → Shared scratchpad (single session, in-memory).

## Conflict Resolution Status

Implicit: retrieval returns highest-similarity match, newer solutions naturally supersede. Explicit conflicts (Agent A says X, Agent B says Y): **no standard mechanism exists** — remains an open problem. Partial solution: store with timestamps, use recency as tiebreaker.

## Key Insight

Store partial completions (agents pick up mid-pipeline) and failed attempts (agents skip known dead ends).

## See Also
- [[agent-memory-persistence]]
- [[multi-agent-framework-guide]]
- [[memory-architecture-comparison]]
