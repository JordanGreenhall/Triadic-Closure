# Triadic Closure Repository Schema

## Domain

This repository is the primary execution corpus for Jordan Hall's Triadic Closure project. It contains foundational architectonics, mathematical work, physics and physics-to-chemistry work, controls, historical sources, maintenance scripts, and compiler artifacts.

## Repository topology

Most substantive Markdown files live at repository root. The complete current inventory is [repository-inventory.md](repository-inventory.md).

Actual directories with distinct roles:

- `_compiler/` — semantic adjudication artifacts;
- `overview/` — residual migration-shadow pages pending consolidation;
- `tools/` — import, normalization, and audit utilities;
- `.github/workflows/` — repository automation.

Former Drive paths such as `results/`, `concepts/`, `process/`, `raw/package/`, and `raw/context/` are historical provenance unless visibly present.

## Source-location rule

For a migrated root document, use:

```text
filename.md
```

Do not infer standing or authority from a former folder name. Historical source paths may remain in frontmatter only when clearly labeled as provenance.

## Document roles

- `overview` or `control` — orientation and durable execution controls;
- `adjudicative` — temporary repair, supersession, ruling, status, load, or boundary packet awaiting absorption;
- `concept` — framework vocabulary and structural concepts;
- `result` — current result modules and derivations;
- `claim` — focused claims with explicit standing;
- `process` — execution and QA rules;
- `historical` or `superseded` — provenance and displaced formulations;
- compiler artifact — semantic inventories under `_compiler/`.

## Frontmatter

For new or repaired documents:

```yaml
---
title: Page Title
type: overview | concept | result | claim | process | control | adjudicative | frontier | historical | memorial
status: current | historical | superseded | contested | open | control | adjudicative
confidence: high | medium | low
sources:
  - source-file.md
historical_sources:
  - former/path/source-file.md
---
```

## Linking rules

1. Governing navigation uses repository-resolvable Markdown links.
2. Root-level migrated files are linked by basename.
3. `_compiler/` paths retain their prefix.
4. `overview/` paths are migration shadows unless expressly retained.
5. Verify a target before changing a link; do not invent basenames.
6. Obsidian wikilinks may remain in historical prose but do not constitute repository navigation.

## Authority and migration

GitHub is primary for every migrated file. Google Drive is fallback provenance and source recovery for files not yet migrated.

Claim authority is semantic and claim-specific. [Corpus Authority and Supersession](corpus-lineage.md) governs the exact priority order. Frontmatter, document role, recency, reading order, and migration location are evidence about a source, never substitutes for claim-level lineage adjudication.

## Claim standing

Standing and warrant route are separate. The five live corpus standings are:

- Open;
- Conjectured;
- Registered;
- Registered and Sealed;
- Defended posit.

Route, premises, conditions, empirical inputs, confidence, review state, sealing debt, and disposition must be recorded separately. `Lead`, `Conjectured-strong`, `Registered-candidate`, `Registered-not-Sealed`, and similar compounds are normalized under [Claim Standing and Warrant](claim-status-vocabulary.md). `Dissolved` is a disposition. `Locked actual` is deprecated and must be translated claim by claim through [locked-actual-decrement-map.md](locked-actual-decrement-map.md).

## Agent rules

Before substantive work, read [README.md](README.md), [index.md](index.md), [repository-inventory.md](repository-inventory.md), [corpus-lineage.md](corpus-lineage.md), [supersession-map.md](supersession-map.md), and [agent-execution-rules.md](agent-execution-rules.md).

Do not average conflicting formulations. Do not let a summary override stronger detailed work. When uncertainty survives adjudication, expose the open joint and avoid status inflation.

## Repository quality gate

A migration or refactor pass is complete only when:

- the repository inventory matches the actual tree;
- governing links resolve;
- shadow duplicates are classified or removed;
- historical and superseded pages are visibly marked;
- absent Drive sources are distinguished from migrated files;
- compiler source records identify whether evidence came from GitHub, Drive, or both;
- semantic content is not altered merely to repair topology.
