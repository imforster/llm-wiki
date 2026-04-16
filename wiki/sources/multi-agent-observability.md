---
type: source
created: 2026-04-15
updated: 2026-04-15
origin: llm
tags: [observability, debugging, tracing, multi-agent, production, OpenTelemetry]
---

# How to Trace and Debug Multi-Agent Systems

[Original](https://futureagi.substack.com/p/how-to-trace-and-debug-multi-agent) | [Raw](../../raw/llm/multi-agent-observability.md)

Production guide (Future AGI, March 2026) for multi-agent observability using OpenTelemetry. Fills the wiki's observability tooling gap.

## Why Multi-Agent Fails Differently

Tool calling errors (malformed params), silent failures (incomplete context handoff, no error thrown), hallucination cascading (fabrication in step 2 corrupts all subsequent steps), latency compounding.

## Trace Hierarchy

Root Span → Agent Span → LLM Span → Tool Span → Retriever Span → Embedding Span. Each carries tokens, latency, model, status, errors. Parent-child links = full execution tree.

## Debugging Patterns

- **Tool errors**: inspect tool span input → check output → look at next LLM span reaction
- **Hallucination**: compare retriever span docs against LLM span output. Automated via faithfulness scoring.
- **Latency**: sort spans by duration, identify bottleneck (e.g., unindexed vector store query)

## Key Metrics

Task completion rate, tool accuracy, faithfulness score, end-to-end latency, cost per query, agent handoff success rate.

## See Also
- [[multi-agent-framework-guide]]
- [[agentic-ai-governance]]
- [[skill-evaluation]]
- [[agent-benchmarks]]
