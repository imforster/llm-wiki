---
type: source
created: 2026-05-12
updated: 2026-05-12
origin: llm
sources: []
tags: [kiro, cli, ci-cd, subagents, headless]
---

# Kiro CLI 2.0: Headless Pipelines, Windows, and UX Refresh

[Original](https://kiro.dev/blog/cli-2-0/) | [Raw](../../raw/llm/kiro-cli-2.0.md)

**Published:** 2026-04-13 (Kiro blog)

## Summary

[[kiro]] CLI 2.0 release announcement. Three major additions: headless mode for CI/CD automation, native Windows support, and a refreshed TUI with subagent monitoring and task lists. Moves Kiro CLI from interactive-only to programmatic access — enabling true automation without human presence.

## Key Features

### Headless Mode
- Generate an API key, set as environment variable → Kiro CLI runs programmatically
- Pipe inputs, script outputs, integrate into CI/CD pipelines and build scripts
- Full access to every tool, agent, and capability from interactive sessions
- Use case: generating PRs, running troubleshooting workflows, deployment automation

### Windows Support
- Native Windows install (no more WSL workaround)
- Works in Windows Terminal with PowerShell

### UX Refresh (GA)
- **Subagent experience**: `ctrl+g` to monitor subagent activity, see traces per agent, status of all subagents
- **Task lists**: real-time progress tracking as agent works through steps — automatically used on larger tasks
- **Permission approval**: visible in both agent monitor (yellow highlight) and main orchestrator screen
- Subagents used to parallelize work while protecting parent agent's context

## Significance

This release represents Kiro's evolution from "agentic IDE" to "agentic platform":
- **Interactive** → terminal sessions (existing)
- **Programmatic** → headless CI/CD (new)
- **Observable** → subagent monitoring (new)

The headless mode is particularly significant — it's the first wiki source showing a concrete path from "developer tool" to "infrastructure component" for an agentic coding tool.

## Connections

- Updates [[kiro]] entity with CLI 2.0 capabilities
- Connects to [[multi-agent-orchestration]] — subagent pattern with monitoring is a lightweight orchestration approach
- Connects to [[claude-code-token-optimization]] — subagent isolation protects parent context (same pattern, different framing)
- Connects to [[agentic-ux-patterns]] — task lists and permission approval implement "Confidence Signal" and "Escalation" patterns
- Headless mode connects to [[frontier-agent]] concept — programmatic access enables autonomous operation

## See Also
- [[kiro]]
- [[claude-code]]
- [[multi-agent-orchestration]]
- [[frontier-agent]]
