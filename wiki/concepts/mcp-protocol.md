---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[claude-code-docs]]", "[[kiro-autonomous-agent]]"]
tags: [protocol, tools, integration, open-standard]
---

# MCP (Model Context Protocol)

An open protocol that standardizes how applications provide context and tools to LLMs. Enables communication between AI agents and external services.

## How Claude Code Uses MCP

[[claude-code]] uses MCP as its primary tool integration mechanism:
- Connect to external data sources (Google Drive, Jira, Slack, custom tooling)
- Discover and install prebuilt plugins
- Create custom plugins
- Tool definitions deferred by default — only tool names consume context until Claude uses a specific tool (tool search)

## Usage Across the Ecosystem

- **[[claude-code]]**: Primary tool integration. Supports prebuilt and custom plugins.
- **[[kiro]]**: [[kiro-powers]] contain curated MCP servers as part of expertise packages.
- **[[scion]]**: Not directly mentioned, but the [[plugin-system]] (hashicorp/go-plugin over gRPC) serves a similar role.

## Significance

MCP is emerging as a shared standard across the coding agent ecosystem. Both Anthropic (Claude Code) and AWS (Kiro) use it, making it a potential interoperability layer between different agent tools. The [[agent-skills-standard]] (agentskills.io) is a complementary open standard: skills teach agents *how* to do things; MCP connects agents to external *tools and data*.

## See Also
- [[claude-code]]
- [[kiro-powers]]
- [[kiro]]
- [[plugin-system]]
