---
type: source
created: 2026-04-07
updated: 2026-04-07
sources: []
tags: [claude-code, anthropic, coding-agent, cli, devtools]
---

# Claude Code Documentation

[Original](https://code.claude.com/docs/en) | [GitHub](https://github.com/anthropics/claude-code) | [Raw](../../raw/claude-code-docs.md)

## Summary

Comprehensive documentation for [[claude-code]], [[anthropic]]'s agentic coding tool. Terminal-native CLI that understands your codebase, edits files, runs commands, and handles git workflows through natural language. Deeply extensible via [[mcp-protocol]], plugins, skills, hooks, and custom subagents.

## Key Takeaways

- **Agentic loop architecture**: Three phases — gather context, take action, verify results — chained together with course-correction. Claude Code is the "agentic harness" that provides tools, context management, and execution environment around the Claude model.
- **Five tool categories**: File operations, search, execution (shell), web, and code intelligence. This is the foundation; everything else extends it.
- **Dual memory system**: CLAUDE.md (human-written instructions, scoped to org/project/user/local) + auto memory (Claude-written learnings, per working tree). Both loaded at session start. Target under 200 lines per CLAUDE.md.
- **Six permission modes**: From `default` (reads only) to `bypassPermissions` (everything). `auto` mode uses a separate classifier model to review actions — a research preview. This is the trust/autonomy dial.
- **Subagents with isolation**: Each subagent gets its own context window, system prompt, tool access, and permissions. Built-in: Explore (Haiku, read-only), Plan (research), General-purpose (all tools). Custom subagents via markdown files. Cannot spawn sub-subagents.
- **Skills as open standard**: Follows Agent Skills (agentskills.io). SKILL.md files with YAML frontmatter. Bundled skills include `/batch` (parallel changes across codebase in git worktrees), `/simplify`, `/loop`, `/debug`.
- **25+ hook events**: Shell commands, HTTP endpoints, or LLM prompts at lifecycle points. Can block actions (PreToolUse deny), inject context, automate workflows. Extremely granular.
- **Three execution environments**: Local (your machine), Cloud (Anthropic VMs), Remote Control (local machine, browser UI).
- **Session portability**: Move between terminal, desktop, web, mobile, Slack. Same CLAUDE.md and MCP servers everywhere. Resume, fork, parallel sessions via git worktrees.
- **AGENTS.md compatibility**: Claude Code reads CLAUDE.md, not AGENTS.md, but can import AGENTS.md for cross-tool compatibility.

## See Also
- [[claude-code]]
- [[anthropic]]
- [[mcp-protocol]]
- [[multi-agent-orchestration]]
