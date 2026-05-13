---
type: entity
created: 2026-04-07
updated: 2026-05-12
sources: ["[[kiro-autonomous-agent]]", "[[kiro-cli-2.0]]"]
tags: [tool, ide, agent, aws, devtools]
---

# Kiro

Kiro is an agentic IDE by [[aws]] for software development. It has three main surfaces:

## Kiro IDE

Interactive, synchronous collaboration on your local machine. Pair programming, suggestions, real-time code iteration. Spec-driven development.

## Kiro CLI

Custom agents as configuration files that customize Kiro's behavior for specific workflows. Define tool access, permissions, and context. Pre-approve tools, reduce interruptions, optimize for specific tasks.

### CLI 2.0 (April 2026)

- **Headless mode**: API key + environment variable → programmatic access for CI/CD pipelines, build scripts, deployment automation. Full tool/agent/capability access without human presence.
- **Windows support**: Native install, no WSL required.
- **Subagent monitoring**: `ctrl+g` shows per-agent traces and status. Permission approvals visible in both agent monitor and main screen.
- **Task lists**: Real-time progress tracking as agent works through steps. Auto-used on larger tasks.

Headless mode moves Kiro from interactive tool to infrastructure component — the first wiki source showing a concrete "developer tool → CI/CD automation" path for an agentic coding tool.

## Kiro Autonomous Agent

A [[frontier-agent]] that works asynchronously in the background on complex, multi-step development tasks. Key capabilities:
- Takes high-level task descriptions and plans implementation autonomously
- Writes code across multiple repositories
- Runs tests and creates pull requests (never auto-merges)
- Runs in isolated sandbox environments
- Maintains persistent context across tasks, repos, and sessions
- Learns from code review feedback
- Coordinates specialized sub-agents

Tasks assigned from kiro.dev or GitHub, not from within the IDE.

Status: Preview — rolling out to Pro, Pro+, and Power users.

## Kiro Powers

[[kiro-powers]] — specialized packages that enhance agents with prebuilt expertise. Contain curated MCP servers, steering files, and hooks.

## Team Integrations

Jira, Confluence, GitLab, GitHub, Teams, Slack (during preview).

## See Also
- [[frontier-agent]]
- [[kiro-powers]]
- [[aws]]
- [[multi-agent-orchestration]]
