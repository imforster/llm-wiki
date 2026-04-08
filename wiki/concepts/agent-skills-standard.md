---
type: concept
created: 2026-04-07
updated: 2026-04-07
sources: ["[[anthropic-skills-repo]]", "[[claude-code-docs]]"]
tags: [open-standard, skills, extensibility, specification]
---

# Agent Skills Standard

An open standard (agentskills.io) for packaging reusable capabilities that AI agents can load dynamically. Initiated by [[anthropic]], designed for cross-tool compatibility.

## Specification

A skill is a directory with a `SKILL.md` file:

```
skill-name/
├── SKILL.md          # Required: YAML frontmatter + markdown instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
```

### Required Frontmatter
- `name`: Max 64 chars, lowercase + hyphens, must match directory name
- `description`: Max 1024 chars, what it does and when to use it

### Optional Frontmatter
- `license`, `compatibility`, `metadata`, `allowed-tools` (experimental)

## Progressive Disclosure

The key design principle — skills scale without blowing up context:

| Layer | When loaded | Budget |
|-------|-------------|--------|
| Metadata (name + description) | Session startup, all skills | ~100 tokens |
| Instructions (SKILL.md body) | When skill activated | <5000 tokens recommended |
| Resources (scripts, references, assets) | When specifically needed | As needed |

Keep SKILL.md under 500 lines. Move detailed reference to separate files.

## Implementations

- **[[claude-code]]**: Primary implementation. Extends the standard with invocation control, subagent execution, and dynamic context injection. Plugin marketplace for distribution.
- **[[kiro]]**: [[kiro-powers]] contain skills-like packages (MCP servers + steering files + hooks). Not explicitly Agent Skills standard, but similar pattern.

## Comparison with Other Extension Mechanisms

| Mechanism | Standard | Scope | Loading |
|-----------|----------|-------|---------|
| Agent Skills | Open (agentskills.io) | Instructions + scripts + resources | Progressive disclosure |
| [[mcp-protocol]] | Open | Tool integration with external services | Tool definitions deferred |
| [[fabric]] Patterns | Open (MIT) | Curated prompts by task (system.md) | Full pattern per invocation |
| [[kiro-powers]] | Proprietary | MCP servers + steering + hooks | On demand |
| Scion [[plugin-system]] | Proprietary | Harness + message broker plugins | gRPC |

Agent Skills and MCP are complementary: skills teach the agent *how* to do things; MCP connects the agent to external *tools and data*. Fabric Patterns are a simpler predecessor — same concept (curated prompts by task) but without scripts, progressive disclosure, or tool integration. The [[ten-pillars-agentic-skill-design]] framework provides comprehensive design methodology for building effective skills.

## See Also
- [[claude-code]]
- [[anthropic]]
- [[mcp-protocol]]
- [[kiro-powers]]
