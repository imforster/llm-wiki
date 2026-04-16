# CrewAI in Production — Building Multi-Agent Teams That Actually Deliver

- **Author**: Sanjeev Sharma (webcoderspeed)
- **Source**: https://webcoderspeed.com/blog/scaling/crewai-production-guide
- **Date**: March 15, 2026
- **Type**: Production guide with code examples

## Practical Crew Patterns

### Content Pipeline (Sequential)
Researcher → Writer → Reviewer. Each task receives output of previous via context. Most common and predictable pattern.

### Customer Support (Hierarchical)
Manager agent orchestrates: Analyzer classifies ticket → routes to urgent or standard handling → generates response. Manager can reassign if quality insufficient.

### Event-Driven (Flows)
CrewAI Flows for complex workflows: states + transitions + event listeners. Example: ticket.created event → analyze → route by priority → handle → complete.

## Memory Configuration

Three types with practical setup:
- **Short-term**: contextWindow (last N messages), enabled per agent
- **Long-term**: vector DB backend (Chroma for dev, Pinecone for production)
- **Entity**: Redis for entity-specific knowledge, with update-on-new-info pattern

## Cost Optimization

Use cheap models (gpt-3.5-turbo) for simple tasks like summarization. Reserve expensive models for complex reasoning. Per-agent model selection.

## Production Patterns

- Async execution with job queue for scalability
- Retry with exponential backoff (maxRetries, timeoutMs)
- REST API integration (Express/FastAPI) for crew-as-a-service
- Cost tracking per crew run (tokens per agent, cost estimate)
- Error handling: timeout protection, graceful degradation

## Checklist

Design crew composition → implement custom tools → configure memory → integrate LLMs → build async execution → add retry logic → deploy as API → implement cost tracking.
