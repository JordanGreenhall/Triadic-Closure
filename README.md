# Triadic Closure Corpus

This repository is the primary execution corpus for Jordan Hall's Triadic Closure project. Most files formerly distributed across Google Drive folders have been migrated into a flattened root-level layout. The `_compiler/` directory remains the principal subdirectory.

## Start here

1. [Corpus Index](index.md)
2. [Repository Inventory](repository-inventory.md)
3. [Repository Schema](SCHEMA.md)
4. [Corpus Lineage](corpus-lineage.md)
5. [Supersession Map](supersession-map.md)
6. [Agent Execution Rules](agent-execution-rules.md)

## Current topology

Most substantive Markdown files live at repository root. Former paths such as `results/`, `overview/`, `concepts/`, `process/`, `raw/package/`, and `raw/context/` are historical provenance unless the directory visibly exists in GitHub.

The live path for a migrated root document is:

```text
filename.md
```

The following directories currently have distinct roles:

- `_compiler/` — semantic inventories and adjudication controls;
- `overview/` — residual migration-shadow pages requiring consolidation;
- `tools/` — import, reference-normalization, and audit scripts;
- `.github/workflows/` — repository automation.

## Corpus scope

The repository now contains:

- foundational architectonics and domain-entry method;
- mathematical and mathematization work;
- physics walks, spacetime, gauge, mass, gravity, and cosmology modules;
- the physics-to-chemistry gate;
- control, audit, historical, and provenance documents;
- compiler artifacts.

The substantive chemistry D1–D4 source deposit named in `_compiler/source-manifest.md` has not yet been migrated as a root source file. Its compiler inventory is present, but the source remains external.

## Authority

GitHub is the primary working source for every migrated file. Google Drive is fallback provenance and a source-recovery location for material not yet migrated.

Authority is claim-specific, not file-wide or folder-wide. Follow [Corpus Authority and Supersession](corpus-lineage.md) for the governing priority order, evidence rules, and absorption discipline. A newer or shorter summary, a `current` label, or a position in the reading order may not override the exact surviving repair and detailed living lineage.

## Standing and warrant

Claim standing and warrant route are separate. The live standings are Open, Conjectured, Registered, Registered and Sealed, and Defended posit. Compound expressions such as `Lead`, `Conjectured-strong`, `Registered-candidate`, and `Registered-not-Sealed` must be decomposed into a live standing plus separate route, condition, review, or frontier metadata. `Dissolved` is a disposition; `Locked actual` is deprecated. See [Claim Standing and Warrant](claim-status-vocabulary.md).

## Historical material

Package-era and superseded files remain for provenance, but may not be treated as current doctrine without adjudication. In particular, `cover-letter.md` and `phi-forward-reconstruction.md` are historical package materials whose broad status claims have been superseded in multiple places.

## Maintenance priorities

- keep [repository-inventory.md](repository-inventory.md) synchronized with the actual tree;
- consolidate or remove shadow duplicates under `overview/`;
- mark superseded files conspicuously in-file;
- ensure all governing links resolve;
- migrate the remaining substantive chemistry source;
- keep `_compiler/` synchronized with, but subordinate to, the substantive corpus.
