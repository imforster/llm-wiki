---
type: source
created: 2026-08-11
updated: 2026-08-11
origin: human
tags: [knowledge-graphs, LLM-validation, human-in-the-loop, hybrid-workflows, quality-assurance, semantic-web]
---

# Knowledge Graph Validation by Integrating LLMs and Human-in-the-Loop

[Original](../../raw/human/Knowledge%20graph%20validation%20by%20integrating%20LLMs%20and%20human-in-the-loop.md)

**Authors:** [[stefani-tsaneva]], [[danilo-dessi]], [[francesco-osborne]], [[marta-sabou]]  
**Published:** Information Processing & Management (2025)  
**DOI:** 10.1016/j.ipm.2025.104145

Empirical investigation of nine [[knowledge-graph-validation]] workflows combining LLMs and [[human-in-the-loop]] methods, tested on the Computer Science Knowledge Graph (CS-KG, 3.6K triples from 6.7M publications). The paper directly addresses which automation levels balance validation precision/recall while minimizing human effort.

## Core Finding: The Disagreement Strategy

**Workflow 5 & 6 (Human Verification)**: When two automated validators disagree, a human decides. Achieves:
- F1 score: 82% (+5% vs baseline SCICERO)
- Precision: 80%+
- Human annotations: <13% of total triples
- No precision/recall tradeoff

This pattern resolves the classic tension: pure automation leaves orphaned triples unchecked, pure manual doesn't scale, but "validate only on disagreement" captures the best of both.

## Nine Workflows Across Four Automation Levels

### 1. Human Judgment (Workflows 1-3)

- **Workflow 1**: Pure manual (no automated support). High precision (+18%), poor scalability (all triples reviewed).
- **Workflow 2**: Human validation after SCICERO automated filters. Precision +8-18%, F1 +4% (1,800+ triples to review).
- **Workflow 3**: Partial human for low-support triples only. Precision +8%, F1 +3% (fewer manual annotations).

**Tradeoff**: Precision gains come with recall losses (-8%), labor-intensive.

### 2. AI Assistance (Workflow 4)

Balanced task partitioning: LLMs validate high-support triples, humans validate low-support triples.
- Precision: +15% (up to 90% with GPT-4o)
- Recall: -13% (significant loss)
- **Verdict**: Good for precision-critical KGs (medical), poor for coverage-critical KGs.

### 3. Human Verification (Workflows 5-6)

**Workflow 5**: Human validation upon disagreement (both add/remove decisions).
- Precision +5%, F1 +2-3%
- <13% human effort, balanced improvements

**Workflow 6**: Human validation only on removal disagreement (coverage prioritized).
- Recall +6-8%
- Same low human effort
- **Use case**: When KG coverage is priority (research, exploration).

### 4. Fully Automated (Workflows 7-9)

- **Workflow 7**: LLM validator as final stage (Precision +12%, F1 +5-7% with GPT-4o)
- **Workflow 8**: LLM for uncertain triples only (Precision +3-8%, no human effort)
- **Workflow 9**: LLM replaces SCICERO entirely (Precision -5%, F1 -3%) — **weakest approach alone**

**Key insight**: LLMs integrated with other methods (7/8) outperform LLMs standalone (9). Consensus validation > single validator.

## Two Experiments

### Experiment A: Large-Scale Simulation (CS-KG-3600)

3,600 triples across six categories (high support, low support, transformer-rejected, ontology-rejected, random corruptions). Human validation simulated using expert annotations from original CS-KG evaluation.

**Findings:**
- LLM-based validation increases precision 3-12% without manual effort (workflows 7/8)
- Human judgment improves precision 8-18% but requires 1,800+ reviews (workflows 1/2)
- Hybrid approaches (workflows 4-6) balance performance and effort

### Experiment B: Real-Life Validation (CS-KG-600)

Subset of 600 triples validated by four PhD researchers in Computer Science (not original evaluators). Only 333 triples sent to human validators (workflows 2-9, skipping pure manual).

**Findings:**
- Fully automated workflows show +5-12% precision improvement (GPT-4o)
- Human judgment workflows show smaller improvements (+4-8%) than Experiment A (junior vs. senior experts)
- Workflow 8 with Claude Sonnet achieves balanced improvements across all metrics
- **Key difference**: Real humans underperform simulated ground truth, but LLMs remain consistent

## Technical Implementation Details

**LLM validators tested:**
- GPT-4o (gpt-4o-2024-05-13)
- Claude Sonnet (claude-3-5-sonnet-20241022)
- Llama 3.3 70B (open-source alternative)

**Prompting strategy:**
- Binary task: classify triple as true/false
- Batch size: 100 triples per request
- Aggregation: majority vote across 3 runs per batch
- Context: No external sources, pure LLM reasoning

**KG generation pipeline (SCICERO):**
1. Extraction: CSO classifier + NLP modules → candidate triples
2. Entity/relationship handling: merge, filter generic terms
3. Validation: transformer validator (support-level based) + ontology validator (schema-based)

## Metrics & Trade-offs

| Workflow | Type | Precision | Recall | F1 | Human Effort | LLM Calls |
|----------|------|-----------|--------|----|----|---|
| SCICERO baseline | — | 75% | 79% | 77% | 0 | 0 |
| Workflow 5 | Hybrid | 80% | 77% | 78% | 13% of triples | 100% |
| Workflow 6 | Hybrid | 78% | 83% | 80% | <13% | 100% |
| Workflow 7 | Auto | 87% | 74% | 80% | 0 | 100% |
| Workflow 9 | Auto | 70% | 75% | 72% | 0 | 100% |

**Strongest paper claim**: "Both fully manual and fully automated validation approaches present trade-offs between precision and recall; a hybrid approach, leveraging human-in-the-loop only upon disagreement among automated methods, leads to highest F1 score (+5%) with minimal manual efforts."

## Connections to Wiki

This paper validates three wiki themes empirically:

1. **[[human-in-the-loop]]**: Formalized as spectrum from pure manual → hybrid → pure auto. Disagreement strategy is concrete UX pattern matching [[agentic-ux-patterns]].

2. **[[skill-evaluation]]**: KG validation is a concrete instance of three-tier skill evaluation (transformer baseline → LLM validator → human verification). Workflows 5/6 map to "human spot-checks disagreement" tier.

3. **[[agent-memory-persistence]]**: KGs are structured memory. Validation quality directly impacts downstream agent reliability — connects to [[memory-lifecycle-drift]] (confidence scoring).

## Limitations & Open Questions

- **Single KG domain**: CS-KG designed for Computer Science. Adaptability to medical, legal, e-commerce domains unclear (but workflows domain-independent by design).
- **LLM variability**: Different prompts, model versions, temperature settings not explored. RAG-enhanced validation not tested.
- **Scalability remaining challenge**: Hybrid workflows reduce manual effort but don't fully solve millions-of-triples KGs. Future work: dynamic workflow selection based on real-time resource availability.
- **Ground truth validity**: LLMs sometimes outperform junior human experts — raises question: which defines truth?

## See Also

- [[knowledge-graphs]]
- [[human-in-the-loop]]
- [[skill-evaluation]]
- [[agent-memory-persistence]]
- [[agentic-ux-patterns]] (disagreement strategy as governance pattern)
- [[langgraph-mem0-integration]] (KG as memory layer)
