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

- `overview` or `control` — orientation, lineage, supersession, status, and execution controls;
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
type: overview | concept | result | claim | process | control | historical
status: current | historical | superseded | contested | open | control
confidence: high | medium | low
sources:
  - source-file.md
historical_sources:
  - former/path/source-file.md
---
```

The frontmatter `status` field records document lifecycle or control role only. It never assigns claim standing to the document or to every sentence within it. Frontmatter `confidence` is likewise document-level metadata unless a claim-level confidence statement is explicitly scoped.

## Linking rules

1. Governing navigation uses repository-resolvable Markdown links.
2. Root-level migrated files are linked by basename.
3. `_compiler/` paths retain their prefix.
4. `overview/` paths are migration shadows unless expressly retained.
5. Verify a target before changing a link; do not invent basenames.
6. Obsidian wikilinks may remain in historical prose but do not constitute repository navigation.

## Authority and migration

GitHub is primary for every migrated file. Google Drive is fallback provenance and source recovery for files not yet migrated.

Claim authority is semantic and claim-specific. Apply the exact order in [corpus-lineage.md](corpus-lineage.md): current direct ruling for the exact ruled claim until propagation; latest surviving repair/supersession/adjudication; integrated ledger; repaired complete derivation; unsuperseded earlier derivation; scoped frontier; necessary downstream expenditure; summaries; compiler inventories; then historical evidence. Chronology and metadata alone never settle authority.

## Claim standing

Standing and warrant route are separate. The four live claim standings are:

- Open;
- Conjectured;
- Registered;
- Registered and Sealed.

Record warrant route/profile/strength, conditions and inheritance, evidence/test state, confidence, workflow state, and disposition in separate fields. In particular, `Conjectured-strong`, `Registered-candidate`, `Defended posit`, and `Dissolved` are not additional standings. See [claim-status-vocabulary.md](claim-status-vocabulary.md).

`Locked actual` is deprecated and must be translated through [locked-actual-decrement-map.md](locked-actual-decrement-map.md).

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