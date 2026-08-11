---
type: concept
created: 2026-08-11
updated: 2026-08-11
tags: [quality-assurance, semantic-web, hybrid-workflows, automation]
---

# Knowledge Graph Validation

**Definition:** The process of ensuring quality in knowledge graphs by identifying and filtering erroneous, inconsistent, or misleading facts before they reach downstream applications.

Validation sits at a critical intersection: automated KG generation enables scale but introduces errors. Manual validation doesn't scale. [[human-in-the-loop]] validation bridges this gap.

## Three Validation Approaches

1. **Automated** (statistics/rules)
   - Transformer-based classifiers trained on reliable subset
   - Ontology-based schema validation
   - Embedding-based consistency checks
   - Pros: Scales to millions of triples
   - Cons: ~30% recall errors (34% false removals, 35% false additions)

2. **Human validation** (crowdsourcing)
   - Domain experts manually judge triple correctness
   - Scales only to ~1,800 triples
   - High precision but labor-intensive

3. **Hybrid** (LLM + human-in-the-loop)
   - Best performers: workflows 5 & 6 from [[kg-validation-hybrid-workflows]]
   - Strategy: validate disagreements only
   - F1 score: 82% (+5% vs baseline) with <13% human effort

## The Disagreement Strategy (Optimal Pattern)

When two automated validators disagree:
- **Workflow 5**: Human decides on both adds and removals → +5% precision, F1 +2-3%
- **Workflow 6**: Human decides on removals only → +8% recall, same effort

This pattern appears repeatedly across the wiki as [[agentic-ux-patterns]] governance layer: delegate to automation when confident, escalate to human on uncertainty.

## LLM Role in Validation

Empirical data from [[kg-validation-hybrid-workflows]]:
- **Standalone LLMs**: 70% precision (weakest approach)
- **LLMs + automated validators**: 87% precision (strongest)
- **Integration point**: LLM as second validator, triggers human escalation on disagreement

LLMs excel at reasoning about semantic correctness. Integration with rule-based validators catches schema violations that LLMs might miss.

## Open Challenges

- **Scalability for millions**: Current methods handle thousands. Millions-of-triple KGs need dynamic workflow selection.
- **Domain transfer**: Workflows tested on CS-KG (computer science). Generalization to medical, legal, e-commerce KGs unstudied.
- **Ground truth definition**: LLMs sometimes outperform junior human experts, raising question: what defines correctness?

## See Also

- [[kg-validation-hybrid-workflows]] (primary empirical source)
- [[human-in-the-loop]] (validation methodology)
- [[skill-evaluation]] (KG validation as instance of three-tier eval)
- [[knowledge-graphs]]
- [[agentic-ux-patterns]] (disagreement as governance pattern)
