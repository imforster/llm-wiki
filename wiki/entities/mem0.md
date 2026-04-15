---
type: entity
created: 2026-04-14
updated: 2026-04-14
sources: ["[[mem0-memory-management]]", "[[agent-memory-systems-2026]]", "[[efficient-memory-architectures]]"]
tags: [tool, memory, persistence, graph, production]
---

# Mem0

Open-source memory management platform for LLM agents. Provides selective memory extraction, graph-enhanced retrieval (Mem0g), and multi-scope memory (user, session, agent, run, org). The most benchmarked memory system in the wiki.

## Key Features

- **Two-phase pipeline**: extraction (discrete facts, not summaries) → update (ADD/UPDATE/DELETE/NOOP)
- **Graph-enhanced retrieval** (Mem0g): entities as nodes, relationships as edges. 68.4% accuracy vs 66.9% vector-only.
- **Five scoping dimensions**: user_id, session_id, agent_id, run_id, org_id
- **Forgetting**: active decay based on Bjork's Theory of Disuse
- **93% token reduction** vs full-context approach (1,800 vs 26,000 tokens)

## Benchmark (LOCOMO)

Best-in-class among memory systems: Mem0g 68.4%, A-Mem 68.6%, full-context 72.9% (but at 14× token cost and 7× latency).

## Integration

LangChain/LangGraph (retriever + storage backend), Mastra (remember + memorize tools), MCP-compatible clients.

## Position in Landscape

Mem0 represents the **Graph + Vector** pattern — the recommended approach for most autonomous agents per [[agent-memory-systems-2026]]. Contrasts with [[pai]]'s three-tier memory (hot/warm/cold) and the [[llm-wiki-pattern]]'s file-based approach.

## See Also
- [[agent-memory-persistence]]
- [[context-management]]
- [[pai]]
