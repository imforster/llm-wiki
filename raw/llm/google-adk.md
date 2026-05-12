# Google Agent Development Kit (ADK)

Source: https://google.github.io/adk-docs/get-started/about/ + https://google.github.io/adk-docs/agents/multi-agents/
Retrieved: 2026-05-11

## Overview

ADK is an open-source, model-agnostic framework for building, managing, evaluating, and deploying AI agents. While optimized for Google's Gemini models, it supports multiple LLMs through its BaseLlm interface. Available in Python, TypeScript, Go, and Java.

- **GitHub**: github.com/google/adk-python, adk-js, adk-go, adk-java
- **License**: Apache 2.0
- **Languages**: Python, TypeScript, Go, Java (all four are first-class)
- **Status**: ADK Python 2.0 Beta (with workflows and agent teams), ADK TypeScript 1.0, ADK Go 1.0
- **Interop**: Native MCP support for tools, native A2A (Agent-to-Agent) protocol for cross-framework agent communication

## Core Concepts

1. **Agent (BaseAgent)**: The fundamental worker unit. Can be LLM-powered (LlmAgent) or deterministic workflow controllers.
2. **LlmAgent**: Agent powered by a large language model for complex reasoning.
3. **Workflow Agents**: Specialized deterministic agents for orchestration:
   - **SequentialAgent**: Executes sub-agents one after another in order
   - **ParallelAgent**: Executes sub-agents concurrently (fan-out)
   - **LoopAgent**: Executes sub-agents in a loop until max_iterations or escalate=True
4. **Tool**: Gives agents abilities beyond conversation (FunctionTool, AgentTool, MCP tools, OpenAPI tools)
5. **Session & State**: Handles conversation context and working memory
6. **Memory**: Long-term recall across multiple sessions
7. **Artifact**: File/binary data management (images, PDFs, reports)
8. **Event**: Unit of communication forming conversation history
9. **Runner**: Engine managing execution flow and orchestration
10. **Callbacks**: Custom code at specific execution points

## Multi-Agent System Architecture

### Agent Hierarchy
- Parent-child relationships via sub_agents parameter
- Single parent rule (agent can only have one parent)
- Navigate with agent.parent_agent or agent.find_agent(name)

### Interaction Mechanisms

a) **Shared Session State (session.state)**: Passive communication via shared state. One agent writes, another reads. output_key auto-saves agent response to state.

b) **LLM-Driven Delegation (Agent Transfer)**: Dynamic routing via transfer_to_agent() function call. LLM decides which sub-agent to route to based on descriptions. Configurable transfer scope (parent, sub-agent, siblings).

c) **Explicit Invocation (AgentTool)**: Wrap any agent as a callable tool. Parent LLM calls it like a function, gets result back. Synchronous within parent's flow.

## Multi-Agent Patterns

1. **Coordinator/Dispatcher**: Central LlmAgent routes to specialists via transfer or AgentTool
2. **Sequential Pipeline**: SequentialAgent chains steps, passing data via state
3. **Parallel Fan-Out/Gather**: ParallelAgent for concurrent execution, then aggregation
4. **Hierarchical Task Decomposition**: Multi-level tree, recursive delegation
5. **Review/Critique (Generator-Critic)**: Sequential generate-then-review
6. **Iterative Refinement**: LoopAgent with quality checking and escalation
7. **Human-in-the-Loop**: Custom tools for approval gates, or PolicyEngine with SecurityPlugin (TypeScript recommended pattern)

## Key Capabilities

1. **Multi-Agent System Design**: Hierarchical composition, LLM-driven transfer, AgentTool invocation
2. **Rich Tool Ecosystem**: FunctionTool, AgentTool, MCP tools, OpenAPI tools, code execution
3. **Flexible Orchestration**: Workflow agents + LLM-driven dynamic routing
4. **Integrated Developer Tooling**: CLI, Developer UI for inspection and debugging
5. **Native Streaming**: Bidirectional audio/video via Gemini Live API Toolkit
6. **Built-in Evaluation**: Multi-turn eval datasets, local evaluation via CLI/UI
7. **Broad LLM Support**: Gemini, Gemma, Claude, Ollama, vLLM, LiteLLM, LiteRT-LM
8. **Artifact Management**: Versioned file/binary handling
9. **A2A Protocol**: Native cross-framework agent communication
10. **State and Memory**: Short-term (session state) + long-term (memory service)

## ADK 2.0 (Beta)

- **Graph-based workflows**: Graph routes, data handling, human input
- **Collaborative agents**: Team-based coordination
- **Dynamic workflows**: Runtime-adaptive orchestration

## Model Support

- Google Gemini (optimized)
- Google Gemma
- Anthropic Claude
- Agent Platform hosted
- Apigee AI Gateway
- Model routing
- Ollama
- vLLM
- LiteLLM
- LiteRT-LM

## Deployment Options

- Agent Runtime (standard deployment, agents-cli)
- Google Cloud Run
- Google Kubernetes Engine (GKE)
- Ambient Agents (background execution)

## Observability

- Logging
- Metrics
- Traces (OpenTelemetry-compatible)

## A2A Protocol Integration

ADK has native A2A (Agent-to-Agent) protocol support:
- Expose ADK agents as A2A services (Python, Go, Java quickstarts)
- Consume external A2A agents from within ADK
- A2A Extension for seamless integration

The A2A protocol is Google's open standard for cross-framework agent interoperability, allowing agents built with different frameworks to communicate.

## Key Signals

- Four-language support (Python, TS, Go, Java) is unique among agent frameworks
- Model-agnostic despite Google origin — supports Claude, Ollama, etc.
- Native A2A + MCP makes it the most interoperable framework
- ADK 2.0 adding graph-based workflows validates the graph convergence thesis
- Workflow agents (Sequential/Parallel/Loop) provide deterministic control without LLM overhead
- Google Cloud integration (Cloud Run, GKE, Agent Platform) for deployment
- Built-in evaluation distinguishes it from most competitors
