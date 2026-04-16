---
type: analysis
created: 2026-04-15
updated: 2026-04-15
sources: ["[[memory-architecture-comparison]]", "[[multi-agent-framework-guide]]", "[[cost-optimization-guide]]", "[[governance-safety-overview]]", "[[langgraph-mem0-integration]]", "[[memory-lifecycle-drift]]", "[[multi-agent-observability]]", "[[agentic-ux-patterns]]"]
tags: [analysis, tutorial, getting-started, practical, architecture]
---

# Building Your First Long-Running Agent: A Getting Started Guide

Synthesized from 8 wiki analyses and sources. This guide bridges the gap between the wiki's architectural recommendations and hands-on implementation. It answers: "I've read the comparisons — now what do I actually build?"

---

## The Architecture the Wiki Recommends

Based on all 37 sources, the wiki converges on this stack for a long-running agent:

| Layer | Choice | Why |
|-------|--------|-----|
| **Orchestration** | [[langgraph-agent-orchestration]] | Checkpointing, human-in-the-loop, most production-ready OSS |
| **Memory** | [[mem0]] (Graph + Vector) | Benchmarked (93% token reduction), handles relationships and forgetting |
| **Memory Lifecycle** | Decay + contradiction + confidence | Prevents drift, keeps store coherent ([[memory-lifecycle-drift]]) |
| **Cost Control** | Prompt caching + model routing + session discipline | 60-80% savings ([[cost-optimization-guide]]) |
| **Trust** | Autonomy Dial + Action Audit | Start at "Plan & Propose," graduate to autonomous ([[agentic-ux-patterns]]) |
| **Observability** | OpenTelemetry spans | Trace every agent action, debug failures ([[multi-agent-observability]]) |

---

## Phase 1: Single Agent with Memory (Week 1)

Start with one agent, not a multi-agent system. Get memory working first.

### Step 1: Set Up LangGraph + Mem0

From [[langgraph-mem0-integration]]:

```
pip install langgraph langchain-openai mem0ai
```

Define State with `messages` and `mem0_user_id`. Create a chatbot node that:
1. Searches Mem0 for relevant memories
2. Builds context string from results
3. Invokes LLM with system message + memories + conversation
4. Stores interaction via `mem0.add()`

Compile graph with chatbot node looping back to itself.

### Step 2: Configure Memory Extraction

Don't store everything. Define custom extraction prompts ([[langgraph-mem0-integration]]):
- **Store**: user preferences, project decisions, bugs found, explicit instructions
- **Skip**: greetings, one-off lookups, generic back-and-forth

Use Mem0's ADD/UPDATE/DELETE/NOOP pipeline to resolve contradictions at write time ([[mem0-memory-management]]).

### Step 3: Implement Cost Controls from Day 1

From [[cost-optimization-guide]] Tier 1 (do this week):
- **Prompt caching**: 90% discount on cached tokens. Structure system prompt as static (cacheable) + dynamic (per-request).
- **CLAUDE.md / system prompt under 200 lines**: every token resent on every request
- **Track costs**: use `/cost` or log tokens per API call

### What You Should Have

A single agent that remembers user preferences across sessions, resolves contradictions when facts change, and costs $80-150/month for daily use.

---

## Phase 2: Add Memory Lifecycle (Week 2)

Your memory store will degrade without maintenance. Add the five lifecycle components from [[memory-lifecycle-drift]]:

### Decay (Run Daily)
- Each memory gets `decay_score` (0-1), starts at 1.0
- Exponential decay based on idle time: `score = e^(-0.693 × days / half_life)`
- Half-life: 30 days for conversational, 90+ for long-running projects
- Below 0.1 → archived (not deleted)
- Frequently accessed memories get freshness bonus

### Contradiction Detection (Run on Every Write)
- When new memory stored, LLM checks against existing store
- Superseded memories marked with `contradicted_by` reference
- One gpt-4o-mini call per write (~200ms overhead)
- This is what prevents the "PostgreSQL vs MySQL" problem

### Confidence Scoring (Run on Every Write)
- LLM rates confidence 0.0-1.0 at write time
- Explicit statement = 1.0, inference = 0.5, speculation = 0.1
- Retrieval sorts by: importance × confidence × decay_score

### Compression (Run Weekly)
- Find clusters of memories repeating across conversations
- Merge N memories → 1 better entry via LLM synthesis
- gpt-4o-mini for clustering, gpt-4o for synthesis
- Merged memory gets confidence = 0.85

### Expiry (Run Daily)
- LLM detects natural end dates (deadlines, temporary states)
- Daily purge archives expired memories

### What You Should Have

A memory system that maintains itself. Old memories fade, contradictions resolve at write time, confidence guides retrieval, duplicates compress, and temporary facts expire. If you're manually cleaning the database, something is wrong.

---

## Phase 3: Add Human-in-the-Loop (Week 3)

From [[agentic-ux-patterns]], implement the phased trust model:

### Start at "Plan & Propose"
Agent creates plans, human reviews every one before execution. Use LangGraph's human-in-the-loop at the approval node:
- Agent proposes action → graph pauses at approval node → human reviews → approves/edits/rejects → graph resumes

### Add Action Audit & Undo
- Log every agent action with timestamp and reasoning chain
- Provide undo capability for reversible actions
- Target: <5% reversion rate. If higher, the agent is making too many mistakes.

### Add Explainable Rationale
- Agent proactively explains "why" grounded in user preferences
- "I suggested X because you previously said Y" — traces back to specific memories

### Graduate to "Act with Confirmation"
Once acceptance rate >85% and reversion rate <5%, move to Act with Confirmation:
- Agent prepares actions, human gives final go/no-go
- Faster than Plan & Propose, still has safety gate

---

## Phase 4: Add Observability (Week 4)

From [[multi-agent-observability]], instrument before you need to debug:

### Set Up OpenTelemetry Tracing
- Root span per workflow execution
- Agent span per agent processing step
- LLM span per model call (capture tokens, latency, model name)
- Tool span per external tool/API invocation

### Track Key Metrics
- **Task completion rate**: % queries with correct output
- **Faithfulness score**: output matches retrieved context (catches hallucination)
- **Cost per query**: total tokens across all spans
- **Memory health**: decay distribution, contradiction rate, compression ratio

### Set Up Alerts
- Latency spike beyond SLA
- Error rate increase in tool spans
- Faithfulness score drops
- Token cost anomalies (often signals agent loops)

---

## Phase 5: Scale to Multi-Agent (Month 2+)

Only after single-agent is solid. From [[multi-agent-framework-guide]]:

### When to Add Agents
- When a single agent's system prompt exceeds 500 lines
- When tasks require genuinely different expertise (research vs writing vs review)
- When you need parallel execution

### How to Add Agents
- Each agent becomes a subgraph in LangGraph
- Define explicit handoff edges between agents
- Share memory via Mem0 scoping (agent_id dimension)
- Monitor per-agent token consumption

### Watch For
- **Cost multiplication**: N agents ≠ N× cost if memory is shared, but budget 2-3× single agent
- **Context loss at handoffs**: each handoff risks losing context. Log handoff spans.
- **Conflicting memories**: when agents learn contradictory facts, no standard resolution yet. Use Mem0's write-time contradiction detection per agent, and flag cross-agent conflicts for human review.

---

## Cost Budget by Phase

| Phase | Monthly Cost | What You're Paying For |
|-------|-------------|----------------------|
| 1. Single agent + memory | $80-150 | LLM API + Mem0 (free tier or self-hosted) |
| 2. + Memory lifecycle | $100-180 | + weekly compression calls (gpt-4o) |
| 3. + Human-in-the-loop | Same | No additional cost (LangGraph feature) |
| 4. + Observability | $100-200 | + tracing backend (Jaeger free, or managed) |
| 5. Multi-agent | $200-500 | 2-3× single agent with optimization |

With optimization (prompt caching, model routing, session discipline): these costs. Without: 2-3× higher.

---

## Common Mistakes

1. **Starting with multi-agent** — get single-agent + memory working first. Multi-agent adds complexity that masks memory and cost problems.
2. **Skipping memory lifecycle** — your agent will seem smart for a month, then degrade as stale memories accumulate.
3. **No cost tracking** — you'll be surprised by your first bill. Track from day 1.
4. **Full autonomy too early** — start at Plan & Propose. Trust is earned, not granted.
5. **No observability** — when something breaks (it will), you need traces, not guesses.
6. **Long sessions** — short focused sessions with fresh context are cheaper AND produce better output.

---

## What This Guide Doesn't Cover (Yet)

- Specific code examples (see [[langgraph-mem0-integration]] for the closest)
- Deployment and hosting (serverless vs containers)
- Team-level knowledge management (gap #3 in wiki)
- Non-code domain adaptation (see [[beyond-code-industry-impact]] for industry patterns)

---

*Guide synthesized from 37 wiki sources, April 2026. Represents the wiki's consensus recommendations for building a first long-running agent.*

## See Also
- [[langgraph-mem0-integration]]
- [[memory-architecture-comparison]]
- [[multi-agent-framework-guide]]
- [[cost-optimization-guide]]
- [[governance-safety-overview]]
- [[memory-lifecycle-drift]]
- [[multi-agent-observability]]
- [[agentic-ux-patterns]]
