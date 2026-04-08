---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[kiro-autonomous-agent]]"]
tags: [agent, autonomous, aws, frontier]
---

# Frontier Agent

A term coined by [[aws]] for a new class of AI agents with three defining characteristics:

1. **Autonomous**: Direct them towards a goal, and they figure out how to achieve it
2. **Massively scalable**: Able to perform multiple concurrent tasks and distribute work across agents
3. **Work independently**: Operating for hours or days without intervention

## Distinction from Regular Agents

Regular AI agents can plan and execute multi-step tasks with some autonomy. Frontier agents go further — they're designed for long-running, independent operation at scale, not just responding to individual prompts or short interactive sessions.

## Examples

- [[kiro]] Autonomous Agent — works independently on development tasks, maintains context across sessions, learns from code reviews, coordinates sub-agents

## Comparison with Scion's Approach

[[scion]] takes a different architectural approach to the same problem space. Where frontier agents (as defined by AWS) emphasize autonomy and independence, Scion emphasizes that "interaction is imperative" — expecting agents to proceed to completion without interaction is unreasonable. Scion positions itself as infrastructure (a "hypervisor") rather than the agent itself, and is harness-agnostic. Kiro's autonomous agent is a specific, opinionated agent product.

Both share:
- Multi-agent coordination (sub-agents)
- Isolated execution environments (sandboxes / containers)
- Git-based workspace management

## See Also
- [[kiro]]
- [[aws]]
- [[multi-agent-orchestration]]
- [[scion]]
