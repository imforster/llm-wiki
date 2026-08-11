---
type: entity
created: 2026-08-11
updated: 2026-08-11
tags: [semantic-web, knowledge-representation, data-structure]
---

# Knowledge Graphs

**Definition:** Structured knowledge models representing domain concepts (entities) and relationships between them. Stored in machine-readable formats, serve as backing store for intelligent applications.

Knowledge graphs (KGs) are used across multiple domains:
- **Scientific KGs**: Computer Science Knowledge Graph (CS-KG, 10M entities from 6.7M publications)
- **Web search**: Google Knowledge Graph, DBpedia
- **Domain-specific**: Medical KGs, product recommendation graphs, research metadata graphs

## Quality Challenge

Automated KG generation enables scale but introduces quality issues: erroneous, inconsistent, or misleading facts. The [[knowledge-graph-validation]] problem addresses this tension.

## Validation Quality Dimensions

From [[kg-validation-hybrid-workflows]]:
- **Precision**: Reducing false positives (incorrect triples in the KG)
- **Recall**: Avoiding over-aggressive filtering (missing valid triples)
- **Scalability**: Validating millions of triples without proportional manual effort

## See Also

- [[knowledge-graph-validation]]
- [[kg-validation-hybrid-workflows]]
- [[agent-memory-persistence]] (KGs as agent memory structure)
