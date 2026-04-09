---
type: source
created: 2026-04-07
updated: 2026-04-07
sources: []
origin: llm
tags: [skills, agent-skills, anthropic, open-standard, specification]
---

# Anthropic Skills Repository & Agent Skills Spec

[Original](https://github.com/anthropics/skills) | [Spec](https://agentskills.io/specification) | [Raw](../../raw/llm/anthropic-skills-repo.md)

## Summary

[[anthropic]]'s official skills repository for Claude, plus the [[agent-skills-standard]] specification. Skills are folders of instructions, scripts, and resources that Claude loads dynamically. The repo contains 17 skills across creative, technical, enterprise, and document categories — including the production document skills that power Claude.ai's file capabilities.

## Key Takeaways

- **Agent Skills is an open standard**: Defined at agentskills.io, not Anthropic-proprietary. Designed for cross-tool compatibility. [[claude-code]] extends it with invocation control, subagent execution, and dynamic context injection.
- **Progressive disclosure is the core design principle**: Metadata (~100 tokens) loaded at startup for all skills. Full instructions (<5000 tokens recommended) loaded only when activated. Resources loaded only when needed. This is how skills scale without blowing up context.
- **SKILL.md is the only required file**: YAML frontmatter (name + description) + markdown instructions. Optional: scripts/, references/, assets/ directories. Keep under 500 lines.
- **Document skills are production code**: The docx, pdf, pptx, xlsx skills power Claude.ai's document capabilities. Source-available (not open source) — shared as reference for complex skill patterns.
- **Plugin marketplace for Claude Code**: `/plugin marketplace add anthropics/skills` registers the repo. Skills installable individually.
- **Partner ecosystem emerging**: Notion has published skills for Claude. The `allowed-tools` field (experimental) hints at future tool-level permission control per skill.

## See Also
- [[agent-skills-standard]]
- [[claude-code]]
- [[anthropic]]
- [[mcp-protocol]]
