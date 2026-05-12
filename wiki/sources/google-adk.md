---
type: source
created: 2026-05-11
updated: 2026-05-11
origin: llm
tags: [multi-agent, framework, google, model-agnostic, a2a]
---

# Google Agent Development Kit (ADK)

[Original](https://google.github.io/adk-docs/) | [Raw](../../raw/llm/google-adk.md)

## Summary

ADK is Google's open-source, model-agnostic framework for building AI agents. Available in Python, TypeScript, Go, and Java — the broadest language support of any agent framework. Features deterministic workflow agents (Sequential/Parallel/Loop), native A2A protocol for cross-framework interop, and native MCP for tools.

## Key Takeaways

- **Four languages**: Python, TypeScript, Go, Java — all first-class. Unique in the space.
- **Model-agnostic**: Supports Gemini, Claude, Ollama, vLLM, LiteLLM despite Google origin.
- **Workflow agents**: SequentialAgent, ParallelAgent, LoopAgent provide deterministic orchestration without LLM overhead. These are the ADK equivalent of [[langgraph-agent-orchestration]]'s graph nodes.
- **Three interaction mechanisms**: Shared session state, LLM-driven delegation (transfer_to_agent), and explicit invocation (AgentTool wrapping).
- **Native A2A**: First-class Agent-to-Agent protocol support — expose ADK agents as A2A services or consume external A2A agents.
- **Native MCP**: Full Model Context Protocol support for tool integration.
- **ADK 2.0 Beta**: Adding graph-based workflows, collaborative agents, and dynamic workflows — validating the [[multi-agent-orchestration]] graph convergence thesis.
- **Built-in evaluation**: Multi-turn eval datasets, local evaluation via CLI/UI. Most frameworks lack this.
- **Deployment**: Cloud Run, GKE, Agent Runtime, Ambient Agents.

## Architecture

Hierarchical agent composition:
- Parent-child via sub_agents (single parent rule)
- Workflow agents as deterministic orchestrators
- LlmAgent for reasoning tasks
- Custom agents (BaseAgent) for specialized logic

## Multi-Agent Patterns

1. Coordinator/Dispatcher — central router
2. Sequential Pipeline — ordered steps via state
3. Parallel Fan-Out/Gather — concurrent execution
4. Hierarchical Task Decomposition — recursive delegation
5. Review/Critique (Generator-Critic) — quality loops
6. Iterative Refinement — LoopAgent with escalation
7. Human-in-the-Loop — PolicyEngine + SecurityPlugin

## Positioning

| Dimension | Google ADK |
|-----------|-----------|
| Model support | 10+ (Gemini, Claude, Ollama, vLLM, LiteLLM, etc.) |
| Languages | Python, TypeScript, Go, Java |
| Orchestration | Workflow agents + LLM transfer + AgentTool |
| State | Session state + long-term memory service |
| Interop | MCP (tools) + A2A (agents) |
| Production features | Eval, observability, deployment, streaming |
| Graph workflows | ADK 2.0 beta |

## See Also
- [[multi-agent-orchestration]]
- [[microsoft-agent-framework]] — similar scope, different ecosystem
- [[langgraph-agent-orchestration]] — graph-first alternative
- [[openai-agents-sdk]] — simpler but model-locked
- [[mcp-protocol]]
