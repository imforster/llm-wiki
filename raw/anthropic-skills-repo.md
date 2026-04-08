# Anthropic Skills Repository & Agent Skills Specification

Source: https://github.com/anthropics/skills
Spec: https://agentskills.io/specification
Retrieved: 2026-04-07

## Overview

This repository contains Anthropic's implementation of skills for Claude. Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. They teach Claude how to complete specific tasks in a repeatable way.

The repository also references the Agent Skills open standard at agentskills.io.

## Agent Skills Specification

### Directory Structure

A skill is a directory containing, at minimum, a SKILL.md file:

```
skill-name/
├── SKILL.md          # Required: metadata + instructions
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
├── assets/           # Optional: templates, resources
└── ...               # Any additional files or directories
```

### SKILL.md Format

YAML frontmatter followed by Markdown content.

Required fields:
- name: Max 64 chars. Lowercase letters, numbers, hyphens only. Must match parent directory name.
- description: Max 1024 chars. What the skill does and when to use it.

Optional fields:
- license: License name or reference to bundled license file
- compatibility: Max 500 chars. Environment requirements (product, system packages, network)
- metadata: Arbitrary key-value mapping
- allowed-tools: Space-delimited list of pre-approved tools (experimental)

### Progressive Disclosure

Skills structured for efficient context use:
- Metadata (~100 tokens): name and description loaded at startup for all skills
- Instructions (< 5000 tokens recommended): Full SKILL.md body loaded when skill activated
- Resources (as needed): Files in scripts/, references/, assets/ loaded only when required

Keep main SKILL.md under 500 lines. Move detailed reference to separate files.

### Validation

Use skills-ref reference library: `skills-ref validate ./my-skill`

## Skills in This Repository

### Creative & Design
- algorithmic-art
- brand-guidelines
- canvas-design
- frontend-design
- slack-gif-creator
- theme-factory
- web-artifacts-builder

### Development & Technical
- claude-api
- mcp-builder
- skill-creator
- webapp-testing

### Enterprise & Communication
- doc-coauthoring
- internal-comms

### Document Skills (Source-Available, not Open Source)
Powers Claude's document capabilities in production:
- docx (Word documents)
- pdf (PDF processing)
- pptx (PowerPoint presentations)
- xlsx (Spreadsheets)

## Usage

### Claude Code
Register as plugin marketplace:
```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

### Claude.ai
All example skills available to paid plans.

### Claude API
Skills available via the Skills API.

## Partner Skills
- Notion: Notion Skills for Claude

## Key Design Principles

- Skills are self-contained in their own folder
- SKILL.md is the entrypoint
- Progressive disclosure minimizes context usage
- Open standard (agentskills.io) for cross-tool compatibility
- Claude Code extends the standard with invocation control, subagent execution, and dynamic context injection
