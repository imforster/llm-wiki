# How to Trace and Debug Multi-Agent Systems: A Production Guide

- **Author**: Future AGI
- **Source**: https://futureagi.substack.com/p/how-to-trace-and-debug-multi-agent
- **Date**: March 23, 2026
- **Type**: Production guide (Substack)

## Why Multi-Agent Systems Fail Differently

- Tool calling errors: malformed parameters, agent retries incorrectly or hallucinates answer
- Silent failures: Agent A passes incomplete context to Agent B, confident but wrong response, no error thrown
- Hallucination in multi-step: fabrication in step 2 corrupts every subsequent step
- Latency compounding: each agent adds latency, 2s delay in one pushes total past tolerance

## Trace and Span Hierarchy

Trace = one complete execution. Spans nested within:
- Root Span: full workflow (invoke_agent triage_agent)
- Agent Span: individual agent processing
- LLM Span: single model call
- Tool Span: external tool/API invocation
- Retriever Span: vector DB query
- Embedding Span: embedding generation

Each span carries: input/output tokens, latency, model name, status code, error type. Parent-child links preserve full execution tree.

## Debugging Patterns

### Tool Call Errors
Inspect tool span input attributes → check output for error → look at next LLM span for agent reaction. Example: empty destination field because model couldn't resolve "somewhere warm."

### Hallucination Detection
Compare retriever span documents against LLM span output. If output contains details not in retrieved docs = hallucination. Automated: LLM-as-judge compares each span's output against retriever docs, assigns faithfulness score. Below threshold → flagged.

### Latency Diagnosis
Sort spans by duration in waterfall view. Example: retriever agent's vector store query taking 5.9s on unindexed 2M+ doc collection.

## Key Metrics

- Task Completion Rate: % queries with correct final output
- Tool Accuracy: % tool calls with correct parameters and valid responses
- Faithfulness Score: output matches retrieved context
- End-to-End Latency: root span duration
- Cost per Query: total tokens across all agents
- Agent Handoff Success Rate: % handoffs preserving required context

## Implementation

OpenTelemetry (OTel) as standard. GenAI SIG defines span operations (invoke_agent, execute_tool) and attributes (gen_ai.agent.name, gen_ai.request.model, gen_ai.usage.input_tokens). Three instrumentation paths: manual OTel, framework-native (LangSmith, CrewAI events), auto-instrumentation libraries.

## Best Practices

- Instrument from day one (not after incident)
- Name spans descriptively (research_agent:web_search not tool_call)
- Trace agent state, not just inputs/outputs
- Combine tracing with automated evaluation
- Use consistent span attributes across frameworks
