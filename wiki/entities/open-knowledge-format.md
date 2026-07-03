---
type: entity
created: 2026-07-02
updated: 2026-07-02
sources: ["[[open-knowledge-format]]"]
tags: [open-standard, specification, knowledge-format, google-cloud]
---

# Open Knowledge Format (OKF)

An open specification by [[google-cloud-platform]] that formalizes the [[llm-wiki-pattern]] into a portable, vendor-neutral standard for representing metadata, context, and curated knowledge consumed by AI agents.

## Key Facts

- **Version**: v0.1 (June 2026)
- **Authors**: Sam McVeety, Amir Hormati (Google Cloud Data Analytics)
- **License**: Open standard, no proprietary SDK required
- **Repo**: https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf
- **Spec size**: Fits on a single page

## What It Is

A **bundle** of markdown files with YAML frontmatter representing concepts (tables, metrics, playbooks, APIs). File path = identity. Concepts cross-link via standard markdown links, forming a knowledge graph.

### Required Fields

Only `type` is mandatory. Optional standardized fields: `title`, `description`, `resource`, `tags`, `timestamp`.

### Reserved Filenames

- `index.md` — progressive disclosure entry point
- `log.md` — chronological change history

## Design Principles

1. **Minimally opinionated** — spec defines interoperability surface, not content model
2. **Producer/consumer independence** — who writes and who reads are decoupled
3. **Format, not platform** — no cloud, SDK, or vendor lock-in

## Reference Implementations

- Enrichment agent (BigQuery → OKF)
- Static HTML graph visualizer (single file, no backend)
- Three sample bundles (GA4, Stack Overflow, Bitcoin)
- Google Cloud Knowledge Catalog integration

## Relationship to This Wiki

This wiki predates OKF but follows the same shape: markdown + YAML frontmatter + cross-links + index.md + log.md. Our `type` field (source/entity/concept/analysis) is an OKF-compatible type system. The wiki could be served as a conformant OKF bundle with minimal changes (wikilinks → markdown links being the main delta).

## See Also
- [[llm-wiki-pattern]]
- [[google-cloud-platform]]
- [[andrej-karpathy]]
- [[context-management]]
- [[icm-folder-structure]]
