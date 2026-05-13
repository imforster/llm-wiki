---
type: entity
created: 2026-04-07
updated: 2026-05-12
sources: ["[[claude-code-docs]]", "[[scion-docs]]", "[[claude-code-token-optimization]]"]
tags: [tool, coding-agent, cli, anthropic, devtools]
---

# Claude Code

An agentic coding tool by [[anthropic]] that lives in your terminal, understands your codebase, and helps you code faster through natural language commands.

## Architecture

Claude Code is the "agentic harness" around Claude models. It provides tools, context management, and execution environment that turn a language model into a coding agent.

### The Agentic Loop
Three phases: **gather context → take action → verify results**, chained together with course-correction. Claude decides what each step requires based on what it learned from the previous step.

### Five Tool Categories
1. **File operations** — read, edit, create, rename
2. **Search** — find files by pattern, regex content search
3. **Execution** — shell commands, servers, tests, git
4. **Web** — search, fetch docs, look up errors
5. **Code intelligence** — type errors, definitions, references (via plugins)

### Three Execution Environments
- **Local**: Your machine (default)
- **Cloud**: Anthropic-managed VMs
- **Remote Control**: Your machine, controlled from browser

## Memory

Dual system for cross-session knowledge:

- **CLAUDE.md**: Human-written instructions. Scoped to org/project/user/local. Loaded at session start. Target under 200 lines. Supports `@imports` and `.claude/rules/` for path-specific rules.
- **Auto memory**: Claude-written learnings (build commands, debugging insights, preferences). Per working tree. First 200 lines or 25KB loaded at session start.

Reads CLAUDE.md, not AGENTS.md — but can import AGENTS.md for cross-tool compatibility.

## Permission Modes

| Mode | Auto-approved | Best for |
|------|---------------|----------|
| `default` | Reads only | Sensitive work |
| `acceptEdits` | Reads + file edits | Iterating on code |
| `plan` | Reads only (research mode) | Exploring before changing |
| `auto` | Everything (classifier-reviewed) | Long tasks |
| `dontAsk` | Pre-approved tools only | CI/CD |
| `bypassPermissions` | Everything | Containers/VMs only |

## Extensibility

Five extension mechanisms:
1. **[[mcp-protocol]]** — Open standard for external tool integration
2. **Plugins** — Custom commands and functionality
3. **Skills** — SKILL.md files following [[agent-skills-standard]]. Bundled: `/batch` (parallel changes in git worktrees), `/simplify`, `/loop`, `/debug`. Plugin marketplace for distribution.
4. **Hooks** — 25+ lifecycle events. Shell commands, HTTP endpoints, or LLM prompts. Can block actions, inject context, automate workflows.
5. **Subagents** — Own context window, system prompt, tool access. Built-in: Explore (Haiku), Plan, General-purpose. Custom via markdown files. Cannot spawn sub-subagents.

## Platforms

Terminal (CLI), VS Code, JetBrains, Desktop, Web, Chrome extension, Slack, GitHub (@claude on PRs), GitHub Actions, GitLab CI/CD, Remote Control, iOS app.

Sessions portable across all surfaces. Same CLAUDE.md and MCP servers everywhere.

## In the Ecosystem

- Built by [[anthropic]], powered by Claude models
- One of the [[harness]]es supported by [[scion]] (as `claude` harness)
- Competes with / complements [[kiro]] (AWS), Gemini CLI (Google), Codex (OpenAI)
- AGENTS.md import enables cross-tool instruction sharing

## Token Optimization (from [[claude-code-token-optimization]])

Key insight: **context architecture > prompt engineering**. You pay for the entire context window, not just the prompt.

- Switch models by task (Haiku → Sonnet → Opus) and use `/effort` for thinking budget
- CLAUDE.md costs tokens on every turn — keep under 200 lines, use as lookup table
- Subagents isolate verbose work but have startup overhead — use for large tasks only
- `/compact` proactively (before overload, not after)
- `/context` to diagnose what's consuming the window
- Point to exact files/lines to avoid expensive exploration
- Plan mode (`Shift+Tab`) before expensive operations

## See Also
- [[anthropic]]
- [[mcp-protocol]]
- [[scion]]
- [[harness]]
- [[kiro]]
- [[multi-agent-orchestration]]
