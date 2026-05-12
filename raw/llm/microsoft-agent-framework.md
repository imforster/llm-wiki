# Microsoft Agent Framework 1.0

Source: https://techcommunity.microsoft.com/blog/azuredevcommunityblog/the-future-of-agentic-ai-inside-microsoft-agent-framework-1-0/4510698 + https://www.digitalapplied.com/blog/microsoft-agent-framework-1-0-dotnet-python-guide
Retrieved: 2026-05-11

## Overview

Microsoft Agent Framework 1.0 GA shipped April 3, 2026 — the production-ready convergence of Semantic Kernel and AutoGen into a single unified SDK. Between them the two predecessor projects accumulated more than 75,000 GitHub stars and three years of enterprise field experience.

- **GitHub**: github.com/microsoft/agent-framework
- **Package**: Microsoft.Agents.AI (.NET) / microsoft-agents-ai (Python)
- **Languages**: .NET 9+ (C# 13), Python 3.10+
- **License**: MIT
- **Interop**: MCP (full), A2A 1.0 (native)
- **Support**: Long-term support commitment for 1.0 APIs

## The Merger: Semantic Kernel + AutoGen

### What Semantic Kernel Contributes (Foundation Layer)
- Kernel abstraction and DI integration
- Plugin model (functions, filters, planners)
- Connector system (chat, embeddings, memory)
- Prompt template language

### What AutoGen Contributes (Graph Workflow Layer)
- Multi-agent conversation patterns
- Group chat / round-robin / hierarchical roles
- Task hand-off and state reconciliation
- Graph-typed workflows with typed edges

**Key insight**: Semantic Kernel doesn't go away — it becomes the foundation layer. AutoGen's orchestration concepts get re-implemented as a graph workflow engine on top.

## Architecture (Five Layers)

1. **Connectors**: Provider-specific adapters. Swappable with a single registration line.
2. **Kernel**: DI container and configuration surface (from Semantic Kernel).
3. **Agents**: First-class agent primitive — instructions, tools, memory, state.
4. **Orchestration**: Graph workflow engine. Multi-agent patterns live here.
5. **Interop Layer**: MCP and A2A protocol adapters.

## Provider Matrix (Six Providers, One-Line Swap)

| Provider | Package | Auth | Streaming |
|----------|---------|------|-----------|
| Azure OpenAI | Microsoft.Agents.AI.AzureOpenAI | Managed Identity, API key | Yes |
| OpenAI | Microsoft.Agents.AI.OpenAI | API key | Yes |
| Anthropic Claude | Microsoft.Agents.AI.Anthropic | API key | Yes |
| Amazon Bedrock | Microsoft.Agents.AI.Bedrock | IAM | Yes |
| Google Gemini | Microsoft.Agents.AI.Google | API key / OAuth | Yes |
| Ollama (local) | Microsoft.Agents.AI.Ollama | localhost | Yes |

## Multi-Agent Orchestration Patterns

Four canonical patterns out of the box:

1. **Round-robin**: Each agent has a clear turn in a deterministic pipeline.
2. **Supervisor**: One coordinator routes messages to specialist agents and aggregates outputs.
3. **Hierarchical**: Tree topology — managers own sub-teams.
4. **Dynamic hand-off**: Agents decide at runtime which peer to transfer to.

## MCP + A2A Interoperability

### MCP: Dynamic Tool Discovery
```csharp
var agent = new ChatAgent("TradingAgent", instructions: "...")
    .WithMcpServer("https://mcp.example.com/trading")
    .WithMcpServer(new StdioMcpServer("pipx", "run", "--spec", "...", "google-ads-mcp"));
// Tools appear automatically; no code changes as the server catalog evolves.
```

### A2A: Cross-Framework Coordination
A2A 1.0 lets an Agent Framework agent coordinate with agents running in other frameworks (LangChain, ADK, custom implementations) via structured, protocol-driven messaging.

## DevUI: Local Debugger

Browser-based local debugger launched with `agent-framework devui`. Shows:
- Full message graph per workflow run
- Tool invocations and parameter bindings
- Token stream latency per node
- Orchestration decisions with rationale traces

For production: OpenTelemetry natively emitted — pipe into App Insights, Datadog, Honeycomb.

## Hello World (.NET)

```csharp
var agent = new ChatAgent(
    name: "Concierge",
    instructions: "You are a concise agency concierge. Answer in one paragraph.",
    model: new OpenAIChatClient("gpt-4.1", Environment.GetEnvironmentVariable("OPENAI_API_KEY")!)
);

await foreach (var token in agent.RunStreamingAsync("Explain MCP in 3 sentences."))
{
    Console.Write(token.Text);
}
```

## Hello World (Python)

```python
import os, asyncio
from microsoft.agents.ai import ChatAgent
from microsoft.agents.ai.openai import OpenAIChatClient

async def main():
    agent = ChatAgent(
        name="Concierge",
        instructions="You are a concise agency concierge. Answer in one paragraph.",
        model=OpenAIChatClient("gpt-4.1", api_key=os.environ["OPENAI_API_KEY"]),
    )
    async for token in agent.run_streaming("Explain MCP in 3 sentences."):
        print(token.text, end="", flush=True)

asyncio.run(main())
```

## Legacy Migration

- **Semantic Kernel**: Continues to receive maintenance. Migrations can be lazy — migrate as features require.
- **AutoGen**: Also receives maintenance but investment flows into Agent Framework. Plan migrations during 2026.
- **Migration guides**: Published for both SK and AutoGen at learn.microsoft.com/agent-framework/migration-guide/

## Azure Deployment

Reference architecture with Azure App Service:
1. Provision App Service, Azure OpenAI, managed identity
2. Grant managed identity access (no API keys in config)
3. Publish via CI/CD with slot-based blue/green deployments
4. Monitor with Application Insights (OpenTelemetry auto-flows)
5. Scale via autoscale rules

## Key Signals

- First enterprise agent SDK shipping as 1.0 with LTS commitment
- 75K+ GitHub stars of prior work (SK + AutoGen) unified
- Graph-based workflows validate the convergence thesis
- Six-provider support makes it truly model-agnostic
- Native MCP + A2A = full interoperability story
- .NET + Python first-class = enterprise-friendly
- DevUI for local debugging is a differentiator
- AutoGen is now officially legacy (maintenance mode)
- Canonical choice for Microsoft/Azure-centric stacks through 2027
