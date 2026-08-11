---
type: concept
created: 2026-08-11
updated: 2026-08-11
tags: [governance, automation, quality-assurance, workflow-design]
---

# Human-in-the-Loop

**Definition:** Workflow patterns where humans remain in decision-making authority over automated processes, applied selectively to improve quality without sacrificing scalability.

The tension human-in-the-loop resolves: pure automation ignores edge cases and novel failures; pure manual labor doesn't scale. Selective human involvement captures the best of both.

## Automation Spectrum (from [[kg-validation-hybrid-workflows]])

Four collaboration levels formalized through KG validation workflows:

1. **Human Judgment** (workflows 1-3)
   - Humans decide every case (possibly supported by automated filters)
   - Precision: +8-18% over baseline
   - Scalability: ~1,800 triples max
   - Use case: Small, high-stakes KGs (medical, legal)

2. **AI Assistance** (workflow 4)
   - Task partitioning: AI handles high-confidence cases, humans handle uncertain ones
   - Precision: +15% (but recall -13%)
   - Use case: Precision-critical systems where coverage is secondary

3. **Human Verification** (workflows 5-6) ← **OPTIMAL PATTERN**
   - Humans validate only when automated validators disagree
   - F1 score: 82% (+5% vs baseline)
   - Human effort: <13% of total volume
   - Balanced precision/recall improvements
   - Use case: Large-scale systems needing quality without proportional labor

4. **Fully Automated**
   - No human involvement
   - Precision: +3-12% (with integration), -5% (standalone LLM)
   - Use case: Sampling-based quality checks, post-hoc audits

## The Disagreement Strategy

**Core insight from wiki**: Human effort is most valuable when automated methods conflict.

When two independent validators produce different results:
- **High confidence scenario**: Both agree → trust the consensus, no review needed
- **Uncertainty scenario**: They disagree → escalate to human for authoritative decision

Applied across domains:
- [[kg-validation-hybrid-workflows]]: Knowledge graph fact-checking
- [[agentic-ux-patterns]]: User approval gates (Autonomy Dial)
- [[langgraph-agent-orchestration]]: Checkpointing with human-in-loop at uncertain nodes
- [[multi-agent-observability]]: Escalation patterns when agent confidence is low

## Cross-Domain Pattern

The disagreement strategy appears across multiple domains in the wiki:

| Domain | System | Disagreement Trigger | Source |
|--------|--------|---------------------|--------|
| Knowledge graphs | Fact validation | Two validators disagree on triple truth | [[kg-validation-hybrid-workflows]] (Workflows 5/6: F1 +5%) |
| Code systems | Impact analysis | Static & AI analysis disagree on breaking change | [[ai-dependency-graph-analysis]] (40% outage reduction) |
| Agent orchestration | Task execution | Multiple validators disagree on plan safety | [[langgraph-agent-orchestration]] (human-in-loop at uncertain nodes) |

**Pattern**: Whenever automated methods conflict, escalate to human for authoritative decision. Achieves superior F1/quality with minimal human effort compared to pure automation or pure manual approaches.

## Governance Layer

From [[agentic-ai-governance]], human-in-the-loop is one of five governance pillars:
- **Intent Preview**: Humans see what the agent plans before execution
- **Autonomy Dial**: Humans control automation level per task
- **Confidence Signal**: System flags low-confidence decisions for review
- **Audit & Undo**: Humans can inspect and reverse decisions
- **Escalation Paths**: Unclear cases surface to appropriate authority level

## Implementation Considerations

**Costs:**
- Annotation time per case: varies (minutes for KG validation, seconds for approval gates)
- Bottleneck risk: if escalation rate is too high, becomes pure manual again
- Expertise requirement: humans must understand domain well enough to judge

**Best practices (from [[kg-validation-hybrid-workflows]]):**
- Pre-filter to reduce human review volume (only send cases with disagreement)
- Provide context: show why automated methods disagreed, what evidence exists
- Batch processing: efficient UI for reviewing many cases at once
- Feedback loop: human decisions train next-generation validators

## See Also

- [[kg-validation-hybrid-workflows]] (empirical validation of this pattern)
- [[agentic-ux-patterns]] (UX design for human-in-loop)
- [[skill-evaluation]] (three-tier evaluation includes human tier)
- [[langgraph-agent-orchestration]] (human-in-loop at any workflow node)
- [[agentic-ai-governance]] (governance pillar overview)
