---
type: analysis
created: 2026-04-09
updated: 2026-04-09
sources: ["[[ten-pillars-agentic-skill-design]]", "[[agent-skills-standard]]", "[[claude-code-docs]]", "[[fabric-github]]", "[[personal-ai-infrastructure]]", "[[skills-pipeline-sleestk]]", "[[evaluating-agent-skills-caparas]]", "[[ai-technique-podcast]]", "[[scion-docs]]", "[[kiro-autonomous-agent]]", "[[llm-wiki-karpathy]]"]
tags: [analysis, ten-pillars, evidence, validation]
---

# Evidence Map: Supporting the Ten Pillars Framework

This analysis maps each pillar from [[ten-pillars-agentic-skill-design]] against real-world evidence collected across 11 sources in this wiki. Your paper acknowledged "no original controlled study" as a limitation — the wiki now provides post-hoc validation from production implementations.

---

## Pillar 1: Architecture and Structure

**Your claim**: Organize content into clearly defined sections — metadata, interfaces, core logic, workflows, configuration.

**Supporting evidence**:

- **[[agent-skills-standard]]** codified this into a formal spec: SKILL.md with YAML frontmatter (name, description, license, compatibility, metadata, allowed-tools) + markdown body + optional scripts/references/assets directories. This is now an open standard at agentskills.io.
- **[[claude-code]]** implements it: `.claude` directory with CLAUDE.md, `.claude/rules/`, `.claude/skills/`, `.claude/agents/`. Hierarchical, scoped (org → project → user → local).
- **[[pai]]** takes it further: USER/ vs SYSTEM/ separation. Six layers of customization (identity, preferences, workflows, skills, hooks, memory). Upgrade-safe architecture.
- **[[skills-pipeline-sleestk]]** follows the spec exactly: each skill is a directory with SKILL.md + references/ subdirectory.

**Strength**: Strong. Multiple independent implementations converged on the same structure. The Agent Skills spec formalizes what your paper recommended.

---

## Pillar 2: Documentation Clarity

**Your claim**: Skills should be self-documenting with descriptions, usage triggers, examples, limitations, dependencies.

**Supporting evidence**:

- **[[agent-skills-standard]]**: `description` field is required (max 1024 chars). Must describe both what the skill does AND when to use it. "Should include specific keywords that help agents identify relevant tasks."
- **[[skills-pipeline-sleestk]]**: The Obsidian skill has an exhaustive trigger list — 30+ keywords and phrases that should activate it. "When in doubt — trigger this skill."
- **[[claude-code]]**: Skills support `description` in frontmatter that Claude uses to decide when to load them automatically.
- **[[ai-technique-podcast]]**: "Context beats clever prompting" — the description IS the context that determines whether the skill gets activated.

**Strength**: Strong. The ecosystem has converged on description-as-routing — the skill's documentation is what makes it discoverable.

---

## Pillar 3: Scope Definition (Single Responsibility)

**Your claim**: Each skill addresses one domain. Avoid monolithic skills. Composition over inheritance.

**Supporting evidence**:

- **[[skills-pipeline-sleestk]]**: YouTube pipeline decomposes video production into 6 focused skills (research, script, SEO, visual, editor, thumbnail) rather than one monolithic "make a video" skill. SaaS stack splits into 4 domain-specific skills (Next.js, Supabase, Stripe, Vercel).
- **[[claude-code]]**: Built-in subagents follow SRP — Explore (read-only search), Plan (research), General-purpose (all tools). Custom subagents are explicitly scoped.
- **[[scion]]**: Harness-per-tool architecture. Each harness (Gemini, Claude, OpenCode, Codex) handles one LLM tool. Templates define one agent blueprint.
- **[[fabric]]**: 251+ patterns, each doing one thing. `summarize`, `extract_wisdom`, `analyze_claims` — not `do_everything`.
- **Anti-example**: Your paper's anti-pattern of a monolithic "business-operations" skill is validated by the ecosystem's universal preference for focused, composable units.

**Strength**: Very strong. Every tool in the wiki independently chose composition over monoliths.

---

## Pillar 4: Modularity and Reusability

**Your claim**: Design skills as composable units. Leverage include directives, skill libraries, dependency injection.

**Supporting evidence**:

- **[[claude-code]]**: CLAUDE.md supports `@path/to/import` syntax for including other files. `.claude/rules/` for path-specific rules. Skills at personal, project, enterprise, and plugin levels.
- **[[agent-skills-standard]]**: Plugin marketplace for distribution (`/plugin marketplace add anthropics/skills`). Skills installable individually.
- **[[skills-pipeline-sleestk]]**: The YouTube pipeline IS composition — 6 independent skills chained together. Each works standalone but integrates seamlessly.
- **[[pai]]**: Packs are standalone, AI-installable capability modules (Research, Security, Thinking, etc.) that work without full PAI installation. Modular by design.
- **[[fabric]]**: Shell aliases turn each pattern into a composable Unix command. `echo "input" | fabric -p summarize | fabric -p extract_wisdom`.

**Strength**: Very strong. Composability is a first-class concern across the ecosystem.

---

## Pillar 5: Prompt Engineering Within Skills

**Your claim**: Use CoT, ReAct, self-reflection. System messages, stepwise instructions, few-shot examples.

**Supporting evidence**:

- **[[fabric]]**: Implements 9 composable strategies (CoT, ToT, Reflexion, self-refine, etc.) as JSON modifiers applied on top of any pattern. Cleanly separates *what* to do (pattern) from *how* to reason (strategy). This is the most elegant implementation of your pillar.
- **[[skills-pipeline-sleestk]]**: Persona-driven skills with explicit decision logic: "Before responding: 1. Identify output type, 2. Load reference files, 3. Produce complete output." This is a lightweight agentic loop.
- **[[claude-code]]**: The agentic loop is explicitly three phases — gather context → take action → verify results — with course-correction. Multiple models available (Sonnet for most tasks, Opus for complex reasoning).
- **[[ai-technique-podcast]]**: "Treat prompts like code — version them, refine them, reuse them." One guest needed ~20 iterations to get a reliable framework.
- **[[pai]]**: "The Foundational Algorithm" — observe → think → plan → build → execute → verify → learn. This is ReAct + self-reflection as a system-level loop.

**Strength**: Strong. Fabric's composable strategies are the standout validation — they prove the pattern/strategy separation your paper implies.

---

## Pillar 6: Tool Integration and Security

**Your claim**: Standardize API hooks via MCP. Defense-in-depth: credentials, validation, sandboxing, human-in-the-loop, prompt injection defenses.

**Supporting evidence**:

- **[[mcp-protocol]]**: Now an open standard used by both Claude Code and Kiro. Tool definitions deferred by default (progressive disclosure for tools).
- **[[claude-code]]**: Six permission modes from `default` (reads only) to `bypassPermissions`. `auto` mode uses a separate classifier model to review actions — a novel safety layer. 25+ hook events for lifecycle control. PreToolUse can deny actions.
- **[[scion]]**: Favors isolation over constraints — `--yolo` mode + container isolation + shadow mounts (tmpfs). Security at the infrastructure layer.
- **[[pai]]**: Policy-based security hooks + allowlists. No `--dangerously-skip-permissions` needed. Security as deterministic rules.
- **[[kiro]]**: Sandbox environments + PR-only output. Never auto-merges.

**Strength**: Strong. Your paper's defense-in-depth recommendation is validated, but no single tool implements all five layers. The ecosystem has split into different security philosophies (inside vs. outside the agent).

---

## Pillar 7: Testing, Validation, and Observability

**Your claim**: Unit/integration tests, AgentOps observability, execution traces, anomaly detection.

**Supporting evidence**:

- **[[evaluating-agent-skills-caparas]]**: Provides the concrete methodology your paper lacked — three-tier evaluation (deterministic → LLM-as-judge → human review) with economics ($0/commit vs. $0.10/eval vs. $2/eval). Directly operationalizes this pillar.
- **[[skills-pipeline-sleestk]]**: Ships 10 test prompts inline with the Obsidian skill. The skill IS its own eval suite. This is "start small with a targeted prompt set" in practice.
- **[[claude-code]]**: 25+ hook events provide observability infrastructure. PostToolUse, SubagentStart/Stop, PreCompact/PostCompact — granular lifecycle tracing.
- **[[scion]]**: Agent state model with three dimensions (Phase, Activity, Detail) provides structured observability. OpenTelemetry support in Gemini and Claude harnesses.

**Strength**: Moderate → Strong. Your paper identified the gap; the Caparas article fills it with methodology; the Skills Pipeline shows inline testing in practice. But no tool has a complete, integrated eval pipeline yet.

---

## Pillar 8: Version Control and Maintenance

**Your claim**: Semantic versioning, changelogs, dependency management, compatibility matrices.

**Supporting evidence**:

- **[[pai]]**: Full semantic versioning (v4.0.3). Detailed changelogs per release. Upgrade migration guides. USER/SYSTEM separation ensures upgrades don't break customizations.
- **[[agent-skills-standard]]**: `license` and `compatibility` fields in frontmatter. `metadata` for version tracking.
- **[[fabric]]**: Active release cycle (v1.4.437+). Migration guide from Python to Go version. Per-pattern model mapping.
- **[[claude-code]]**: Checkpointing — save and restore state. Session history as plaintext JSONL. Git-backed by nature.

**Strength**: Moderate. Tools version themselves well, but skill-level versioning (individual skills with semver) is still informal in most implementations.

---

## Pillar 9: Performance Optimization / Context Management

**Your claim**: Token optimization, chunking, progressive summarization, selective context loading, agent persona context templates.

**Supporting evidence — this is your strongest pillar**:

- **[[agent-skills-standard]]**: Progressive disclosure is the core spec design — ~100 tokens at startup, <5000 when activated, resources on demand. "Keep SKILL.md under 500 lines."
- **[[claude-code]]**: MCP tool definitions deferred (names only until used). Skills load on demand. Subagents get isolated context windows. Auto-compaction when context fills. CLAUDE.md target under 200 lines.
- **[[skills-pipeline-sleestk]]**: The YouTube pipeline IS your "Agent Persona Context Templates" recipe — each stage produces structured output that becomes the next stage's minimal input. The Obsidian skill loads 8 reference files on demand.
- **[[scion]]**: Each agent gets its own container with its own context. No shared context pollution. The ultimate isolation.
- **[[kiro]]**: Persistent context across tasks/repos/sessions — the opposite approach, betting on accumulation over isolation.
- **[[llm-wiki-pattern]]**: Index-first navigation is selective context loading — read the catalog, drill into only relevant pages.
- **[[ai-technique-podcast]]**: "Context beats clever prompting" — practitioner validation from Amazon employees.

**Strength**: Very strong. Every tool independently converged on progressive disclosure. Your four recipes map directly to production implementations.

---

## Pillar 10: Anti-Patterns

**Your claim**: Avoid monolithic skills, hard-coded config, overly generic prompts, missing error handling, ignoring token limits, poor tool integration, lack of testing.

**Supporting evidence**:

- **Monolithic skills**: Every tool chose decomposition (see Pillar 3). The YouTube pipeline's 6-stage approach vs. a single "make video" skill is the clearest anti-example.
- **Hard-coded config**: Claude Code uses environment variables and `.claude` directory. PAI uses USER/SYSTEM separation. Scion uses settings.yaml with profile overrides.
- **Overly generic prompts**: The Agent Skills spec requires descriptions that include "specific keywords that help agents identify relevant tasks." Fabric's 251 focused patterns vs. one generic "help me" prompt.
- **Ignoring token limits**: Progressive disclosure is the universal answer (see Pillar 9).
- **Lack of testing**: The Caparas article and Skills Pipeline's inline test prompts show the ecosystem is starting to address this, but it remains the weakest area.

**Strength**: Strong. The anti-patterns you identified are real — the ecosystem's design choices consistently avoid them.

---

## Summary: Pillar Strength Rankings

| Pillar | Evidence Strength | Best Supporting Source |
|--------|------------------|----------------------|
| 3. Scope (SRP) | ⭐⭐⭐⭐⭐ | Skills Pipeline (6-stage YouTube pipeline) |
| 4. Modularity | ⭐⭐⭐⭐⭐ | Claude Code (imports, rules, plugins, marketplace) |
| 9. Context Management | ⭐⭐⭐⭐⭐ | Agent Skills Standard (progressive disclosure spec) |
| 1. Architecture | ⭐⭐⭐⭐ | Agent Skills Standard (formal spec) |
| 5. Prompt Engineering | ⭐⭐⭐⭐ | Fabric (composable strategies) |
| 6. Tool Integration | ⭐⭐⭐⭐ | Claude Code (6 permission modes, MCP, 25+ hooks) |
| 10. Anti-Patterns | ⭐⭐⭐⭐ | Ecosystem-wide avoidance |
| 2. Documentation | ⭐⭐⭐ | Agent Skills Standard (description-as-routing) |
| 7. Testing | ⭐⭐⭐ | Caparas (methodology) + Skills Pipeline (inline tests) |
| 8. Versioning | ⭐⭐ | PAI (full semver + migration guides) |

## What This Means for Your Paper

**Your framework is validated by the ecosystem.** The 10 sources ingested after your paper was written independently implement the patterns you recommended. The strongest validation:

1. **Progressive disclosure** (Pillar 9) is now a formal open standard (Agent Skills spec)
2. **Composition over monoliths** (Pillars 3-4) is universal — no tool chose the monolithic approach
3. **Context beats clever prompting** (Pillar 9) is validated by both technical implementations and practitioner experience

**Gaps your paper could address in v3**:

1. **Composable strategies**: Fabric's separation of pattern (what) from strategy (how to reason) is an elegant extension of Pillar 5 that your paper doesn't cover
2. **Inline evaluation**: Skills shipping with their own test prompts (Skills Pipeline) is a practical pattern for Pillar 7
3. **The autonomy spectrum**: Claude Code's 6 permission modes show that security (Pillar 6) isn't binary — it's a configurable dial
4. **Skills as pipelines**: The YouTube pipeline pattern (each stage's output → next stage's input) deserves its own recipe in Pillar 9

## See Also
- [[ten-pillars-agentic-skill-design]]
- [[key-insights-agentic-landscape]]
- [[agent-skills-standard]]
- [[skill-evaluation]]
