# Building Long-Term Memory in AI Agents with LangGraph and Mem0

- **Authors**: Adrien Payong, Shaoni Mukherjee
- **Source**: https://www.digitalocean.com/community/tutorials/langgraph-mem0-integration-long-term-ai-memory
- **Date**: March 13, 2026
- **Type**: Tutorial (DigitalOcean)

## Integration Architecture

1. Message reception — agent gets user message through LangGraph node
2. Memory search — node calls mem0.search() with user message + userId
3. Context construction — memory list formatted into system prompt
4. LLM invocation — system message + conversation history + memories
5. Memory update — mem0.add() stores interaction asynchronously

LangGraph maintains state across iterations. Mem0 persists long-term storage.

## Key Code Pattern

State includes `messages` and `mem0_user_id`. Chatbot node: search memories → build context → invoke LLM → store interaction. Graph: chatbot node loops back to itself for each turn.

## Memory Extraction Strategies

- Define what counts as memory (custom fact extraction prompts)
- Define how memory changes (ADD/UPDATE/DELETE/NONE actions)
- Control ingestion quality — store only verified facts in real-time, process less critical data async

## Production Considerations

- Vector DB: SQLite for testing, pgvector/Pinecone/Weaviate for production
- Privacy: encrypt sensitive fields, retention policies, user consent, deletion APIs
- Cost: semantic search is fast and batchable. ~90% token savings and 91% lower p95 latency vs full-context
- Reliability: LangGraph checkpoints for crash recovery, memory storage backups
- Security: restrict write access to agent only, isolate namespaces in multi-tenant

## Tradeoffs

- Storage vs latency: full conversations = perfect recall but high cost. Summarization reduces storage at expense of precision.
- Privacy vs personalization: memory enables personalization but stores user data
- Accuracy vs cost: too many memories confuse LLM, too few miss critical info. Tune max_memories and relevance threshold.
