# Claude Code Documentation (Detailed)

Source: https://code.claude.com/docs/en (raw .md endpoints)
GitHub: https://github.com/anthropics/claude-code
Retrieved: 2026-04-07

## Overview

Claude Code is an agentic coding tool by Anthropic that lives in your terminal, understands your codebase, and helps you code faster. Available in terminal, IDE, desktop app, and browser.

## The Agentic Loop

When you give Claude a task, it works through three phases: gather context, take action, and verify results. These phases blend together. Claude uses tools throughout.

The loop adapts to what you ask. Claude decides what each step requires based on what it learned from the previous step, chaining dozens of actions together and course-correcting along the way.

Claude Code serves as the "agentic harness" around Claude: it provides the tools, context management, and execution environment that turn a language model into a capable coding agent.

### Models
Multiple models available: Sonnet for most tasks, Opus for complex architectural decisions. Switch with `/model` during a session.

### Tools (Five Categories)
1. File operations: Read, edit, create, rename files
2. Search: Find files by pattern, search content with regex
3. Execution: Run shell commands, start servers, run tests, use git
4. Web: Search the web, fetch documentation, look up error messages
5. Code intelligence: Type errors, jump to definitions, find references (via plugins)

## What Claude Can Access
- Your project files
- Your terminal (any command you could run)
- Your git state
- CLAUDE.md (project instructions)
- Auto memory (learnings saved automatically)
- Extensions: MCP servers, skills, subagents, Chrome

## Execution Environments
- Local: Your machine (default)
- Cloud: Anthropic-managed VMs
- Remote Control: Your machine, controlled from browser

## Memory System

Two mechanisms carry knowledge across sessions:

### CLAUDE.md Files
Instructions you write. Loaded at start of every session. Scopes:
- Managed policy: Organization-wide (/Library/Application Support/ClaudeCode/CLAUDE.md)
- Project: ./CLAUDE.md or ./.claude/CLAUDE.md (shared via source control)
- User: ~/.claude/CLAUDE.md (personal, all projects)
- Local: ./CLAUDE.local.md (personal, current project, gitignored)

Can import other files with @path/to/import syntax. Supports .claude/rules/ for path-specific rules.

Best practices: target under 200 lines per file. Use markdown headers and bullets. Be specific and concrete.

### Auto Memory
Notes Claude writes itself based on corrections and preferences. Per working tree. First 200 lines or 25KB loaded at session start. Subagents can maintain their own auto memory.

### AGENTS.md Compatibility
Claude Code reads CLAUDE.md, not AGENTS.md. Can import AGENTS.md from CLAUDE.md for cross-tool compatibility.

## Permission Modes

| Mode | What runs without asking | Best for |
|------|--------------------------|----------|
| default | Reads only | Getting started, sensitive work |
| acceptEdits | Reads and file edits | Iterating on code you're reviewing |
| plan | Reads only | Exploring before changing |
| auto | Everything, with background safety checks | Long tasks, reducing prompt fatigue |
| dontAsk | Only pre-approved tools | Locked-down CI and scripts |
| bypassPermissions | Everything except protected paths | Isolated containers and VMs only |

Switch with Shift+Tab in CLI. Auto mode uses a separate classifier model to review actions before they run.

## Subagents

Specialized AI assistants that handle specific types of tasks. Each runs in its own context window with custom system prompt, specific tool access, and independent permissions.

### Built-in Subagents
- Explore: Fast, read-only (Haiku model). File discovery, code search.
- Plan: Research agent for plan mode. Read-only.
- General-purpose: Complex multi-step tasks. All tools.

### Custom Subagents
Defined in Markdown files with YAML frontmatter. Can be user-level (~/.claude/agents/) or project-level (.claude/agents/). Managed via /agents command.

Features: custom system prompts, tool restrictions, permission modes, hooks, skills, persistent memory, model selection, color coding.

Subagents cannot spawn other subagents (prevents infinite nesting).

## Skills

Skills extend what Claude can do. Create a SKILL.md file with instructions. Claude uses skills when relevant, or invoke directly with /skill-name.

Follows the Agent Skills open standard (agentskills.io).

### Bundled Skills
- /batch: Orchestrate large-scale changes in parallel. Spawns one agent per unit in isolated git worktrees.
- /claude-api: Load Claude API reference material.
- /debug: Enable debug logging and troubleshoot.
- /loop: Run a prompt repeatedly on an interval.
- /simplify: Review changed files for quality issues.

### Skill Locations
- Enterprise: Managed settings
- Personal: ~/.claude/skills/
- Project: .claude/skills/
- Plugin: <plugin>/skills/

## Hooks

User-defined shell commands, HTTP endpoints, or LLM prompts that execute automatically at specific points in Claude Code's lifecycle.

### Hook Events (25+)
SessionStart, UserPromptSubmit, PreToolUse, PermissionRequest, PermissionDenied, PostToolUse, PostToolUseFailure, Notification, SubagentStart, SubagentStop, TaskCreated, TaskCompleted, Stop, StopFailure, TeammateIdle, InstructionsLoaded, ConfigChange, CwdChanged, FileChanged, WorktreeCreate, WorktreeRemove, PreCompact, PostCompact, Elicitation, ElicitationResult, SessionEnd.

Hooks can block actions (PreToolUse deny), inject context, automate workflows.

## MCP (Model Context Protocol)

Open standard for connecting AI tools to external data sources. Claude Code can read design docs in Google Drive, update tickets in Jira, pull data from Slack, or use custom tooling.

## Platforms

Terminal (CLI), VS Code, JetBrains, Desktop app, Web (claude.ai/code), Chrome extension, Slack, GitHub (@claude on PRs), GitHub Actions, GitLab CI/CD, Remote Control, iOS app.

Sessions aren't tied to a single surface. Move work between environments. CLAUDE.md files, settings, and MCP servers work across all of them.

## Context Window Management

Claude compacts automatically when context fills up. Clears older tool outputs first, then summarizes. Put persistent rules in CLAUDE.md. Run /context to see usage. MCP tool definitions deferred by default (loaded on demand).

Skills load on demand. Subagents get their own fresh context (isolation helps with long sessions).

## Sessions

Saved locally as plaintext JSONL under ~/.claude/projects/. Independent — each new session starts fresh. Can resume (--continue), fork (--fork-session). Git worktrees for parallel sessions.

## Key Capabilities Summary
- Automate tedious tasks (tests, lint, merge conflicts, dependency updates)
- Build features and fix bugs across multiple files
- Create commits and pull requests
- Connect tools via MCP
- Customize with CLAUDE.md, skills, hooks
- Run agent teams and custom subagents
- Pipe, script, automate (Unix philosophy)
- Schedule recurring tasks (cloud or desktop)
- Work from anywhere (Remote Control, web, mobile, Slack)
