---
type: source
created: 2026-04-14
updated: 2026-04-14
origin: llm
tags: [memory, persistence, retrieval, benchmarks, production]
---

# Mem0: AI Memory Management for LLMs and Agents

[Original](https://mem0.ai/blog/ai-memory-management-for-llms-and-agents) | [Raw](../../raw/llm/mem0-ai-memory-management.md)

Technical deep-dive from the [[mem0]] engineering team on production memory management for LLM agents. Provides the most concrete benchmark data in the wiki for memory system tradeoffs.

## Four Memory Layers

1. **Conversation memory** — active context window. Resets at session end.
2. **Session memory** — spans a single task/goal sequence. Survives across turns.
3. **User memory** — long-term: preferences, tools, projects, communication style. Most valuable, most expensive.
4. **Organizational memory** — team/company level. Shared policies, consistent across all agents.

Each answers a different question: "what's happening now?" / "what's this task's context?" / "what do I know about this person?" / "what's universally true?"

## Two-Phase Extraction Pipeline

**Phase 1 — Extraction**: LLM pass identifies discrete, durable facts (not summaries). "User prefers Python," "user's timezone is CET." Mirrors Craik & Lockhart's levels-of-processing theory.

**Phase 2 — Update**: Four operations before any write:
- **ADD** — new fact
- **UPDATE** — supersedes existing (user changed jobs)
- **DELETE** — existing fact no longer true
- **NOOP** — duplicate, skip

Resolves contradictions at write time, not query time. Store stays coherent as it grows. Directly addresses the wiki's identified tension that "persistent context compounds value AND errors."

## Memory Types (Cognitive Science Mapping)

- **Semantic** — factual knowledge (what user does, tools, domain)
- **Episodic** — event-specific (what happened in a conversation). Decays faster.
- **Procedural** — how things are done (workflows, patterns). Underused, disproportionately valuable.
- **Working** — active context window contents

## Graph-Enhanced Retrieval (Mem0g)

Vector similarity weaknesses: phrasing-sensitive, no time concept, no contradiction detection. Mem0g stores memories as directed labeled graph — entities as nodes, relationships as edges. Enables graph traversal for relational queries.

## Forgetting as Design Requirement

Based on Bjork's "New Theory of Disuse": forgetting is active and adaptive, protects retrieval quality. Memories decay without reinforcement. Entries below threshold are pruned.

## Benchmark Results (LOCOMO)

| Approach | Accuracy | Median Latency | Tokens |
|----------|----------|----------------|--------|
| Full-context | 72.9% | 9.87s | ~26,000 |
| Mem0 (vector) | 66.9% | 0.71s | ~1,800 |
| Mem0g (graph) | 68.4% | 1.18s | ~1,800 |
| OpenAI Memory | 52.9% | — | — |
| A-Mem | 68.6% | — | — |
| LangMem | 50.9% | — | — |

93% token reduction with selective retrieval. The 4.5-point accuracy gap vs full-context is the core tradeoff.

## Memory Scoping

Five dimensions: user_id, session_id, agent_id, run_id, org_id. Over-broad scoping bleeds memory between users. Under-broad means agent can't access what it should.

## See Also
- [[context-management]]
- [[agent-memory-persistence]]
- [[continuum-memory-architectures]]
- [[agent-memory-systems-2026]]
