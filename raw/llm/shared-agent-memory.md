# AI Agents Repeating Work? Add a Shared Memory Layer

- **Author**: Nathan Cole (RoboRhythms)
- **Source**: https://www.roborhythms.com/how-to-stop-ai-agents-repeating-work-2026/
- **Date**: April 7, 2026
- **Type**: Tutorial with code examples

## The Problem

Each agent starts fresh with no knowledge of what sibling agents have solved. Agent A solves problem at step 3, Agent B hits same problem at step 7, solves from scratch. Multiply across 10 agents = burning compute on duplicate work.

## Shared Memory Pattern (4 Components)

1. **Solution store** — persists results across agent runs
2. **Write hook** — fires after agent completes a sub-problem
3. **Retrieval step** — fires BEFORE agent begins new sub-problem (this is where most fail)
4. **Similarity threshold** — determines if cached result is close enough to reuse (~0.85)

Key: retrieval step must be unconditional. If agents don't check the store before starting work, the store is just an archive.

## Memory Pattern Comparison

| Pattern | When to Use | Complexity | Best Tool |
|---------|------------|-----------|-----------|
| Key-value cache | Exact same task repeats | Low | Redis |
| Vector similarity | Similar but not identical tasks | Medium | Chroma, Pinecone, Qdrant |
| Graph store | Tasks with relationships/dependencies | High | Neo4j, LanceDB |
| Shared scratchpad | Single-session coordination only | Low | In-memory dict, SQLite |

Vector similarity best for most multi-agent use cases.

## Implementation

Before: `result = llm.complete(task)` (starts from scratch every time)
After: query shared store → if similarity > 0.85, return cached → else run fresh and store result

## Partial and Failed Solutions

Store partial completions with "status: partial" metadata — agents pick up mid-pipeline. Store failed attempts with failure reason — future agents skip known dead ends.

## Conflict Resolution (Implicit)

When multiple agents store solutions for similar tasks, the retrieval step returns the highest-similarity match. Newer solutions naturally supersede older ones if stored with timestamps. For explicit conflicts (Agent A says X, Agent B says Y), no standard mechanism exists — this remains an open problem.

## Performance

ChromaDB local: <20ms query on <100K entries. Pinecone hosted: 50-150ms. Negligible vs LLM call (500ms-3s).
