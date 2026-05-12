# AI Architecture: Building Your Second Brain with Claude and Obsidian

## Overview

This notebook outlines a paradigm shift from manually learning Obsidian's features to becoming an **architect** who uses Claude AI as a builder to automate vault construction. The core idea is **context engineering** — teaching Claude the rules of Obsidian through specialized "skills" so it can read, write, and organize notes natively.

---

## 1. The Paradigm Shift: From Learner to Architect

- Stop trying to "learn" Obsidian's complex plugins, syntax, and shortcuts — focus on **context engineering** instead.
- In the AI era, understanding a tool's **framework** matters more than memorizing its features.
- The roles:
  - **You** = the Architect (provide intent and context)
  - **Claude** = the Builder (executes the work)
  - **Obsidian** = the Material (local markdown files)

## 2. Obsidian as AI-Native Material

Obsidian is uniquely suited for AI integration because:

- Every note is a **plain Markdown (.md) file** stored locally — no proprietary database or cloud lock-in.
- Markdown is "Claude's first language" — the AI can read, write, and edit these files natively without complex API hacks.
- No SaaS dependency: everything lives on your local filesystem.

## 3. Context Engineering via "Skills"

Specialized **skills** are structured instructions that teach Claude the specific rules of the Obsidian environment.

- **Obsidian CEO's contribution**: Stefan (Kapano), CEO of Obsidian, released an open-source GitHub repo containing agent skills that teach Claude exact file grammars.
- Without these skills, Claude often generates broken syntax (invalid WikiLinks, malformed Canvas JSON, etc.).
- The repo contains **five skills**:
  1. **Markdown** — standard note creation
  2. **Bases** — Obsidian's Bases feature
  3. **Canvas** — correct JSON schema for Canvas files
  4. **CLI** — command-line operations
  5. **Defutle** — web clipping capabilities
- An **Obsidian Power User Prompt** compresses Obsidian's documentation into a reusable format Claude can use instantly.

## 4. Automated Vault Construction

With skills loaded, Claude can automate research and organization:

- **One-sentence execution**: A single plain-English instruction (e.g., "Research topic X and create a folder") triggers Claude to perform research, create directories, and write notes directly into the vault.
- Claude automatically handles:
  - **Frontmatter** — metadata blocks (title, date, tags, status) for searching and filtering
  - **WikiLinks** — `[[double bracket]]` connections that turn a vault into a web of ideas
  - **Callouts and DataView** — Obsidian-specific syntax handled correctly

## 5. Remote Access via Claude Code CLI

Advanced setup for managing a vault through the command line:

- **Claude Code** — a CLI tool giving Claude direct access to local folders.
- **Setup**: `cd` into the vault directory, then run Claude Code.
- **Remote control**: Using SSH, you can manage your vault from a phone by connecting to your desktop terminal.
- **Command**: `claude --dangerously-skip-permissions` allows Claude Code to operate without frequent permission interrupts, enabling remote automation.
- This preserves the **local-first** philosophy while enabling anywhere access.

---

## Key Technical Concepts

| Concept | Description |
|---------|-------------|
| Markdown (.md) | Native file format for both Obsidian and Claude |
| WikiLinks | `[[double brackets]]` connecting notes into a knowledge graph |
| Frontmatter | YAML metadata block at top of notes (tags, dates, status) |
| Canvas JSON | Schema for Obsidian's visual canvas files |
| Context Engineering | Teaching AI the rules/grammar of a tool via structured prompts |
| Skills | Reusable instruction sets that make Claude "production-ready" for Obsidian |

## Tools & Resources

- **Obsidian** — [obsidian.md](https://obsidian.md) (free for personal use)
- **Claude Code** — CLI for direct local folder access
- **Obsidian Skills repo** — Open-source GitHub repo by Obsidian CEO (Kapano/Stefan)
- **Defutle** — Web clipper integrated into the agent skills
- **SSH** — For remote vault management from mobile

---

*Summary generated from NotebookLM notebook on 2026-04-12.*
