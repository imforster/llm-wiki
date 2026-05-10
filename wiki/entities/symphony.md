---
type: entity
created: 2026-05-09
updated: 2026-05-09
sources: ["[[symphony]]"]
tags: [tool, multi-agent, orchestration, openai, spec-driven]
---

# Symphony

Open-source orchestration service by OpenAI that turns issue tracker work into isolated, autonomous coding agent runs. Published as a language-agnostic specification (SPEC.md) with an Elixir reference implementation.

## Key Facts

- **Repository**: https://github.com/openai/symphony
- **Organization**: [[openai-org]]
- **License**: Apache 2.0
- **Stars**: 23K
- **Language**: Elixir (reference), spec is language-agnostic
- **Agent runtime**: Codex app-server
- **Issue tracker**: Linear (only, currently)
- **Approach**: Spec-first — teams implement the protocol in their own language

## Core Design

- **WORKFLOW.md** — Single file containing prompt template (Markdown body) + runtime config (YAML front matter). Version-controlled with the codebase. Dynamic reload without restart.
- **Scheduler/runner only** — Reads issues, dispatches agents, tracks state. Does NOT write to the tracker. Clear separation of concerns.
- **Per-issue workspace isolation** — Sanitized paths, contained under root, lifecycle hooks
- **In-memory state** — No database. Recovery via tracker polling + preserved workspaces.
- **Multi-turn sessions** — Up to 20 turns per worker, continuation without re-sending prompt

## Differentiators

- Only spec/protocol in the wiki (not a framework, library, or product)
- Strongest "policy-as-code" implementation (everything in WORKFLOW.md)
- Assumes "harness engineering" as prerequisite
- Intentionally minimal — no UI, no database, no multi-tenant

## See Also
- [[multi-agent-orchestration]]
- [[openai-swarm]]
- [[gastown]]
- [[multica]]
