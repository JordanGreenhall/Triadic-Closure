---
title: Agent Execution Rules
type: process
updated: 2026-07-13
status: control
confidence: high
sources:
  - repository-inventory.md
  - physics-walk-checklist.md
---

# Agent Execution Rules

## Start here

1. Read [README.md](README.md).
2. Read [index.md](index.md).
3. Read [repository-inventory.md](repository-inventory.md).
4. Read [SCHEMA.md](SCHEMA.md).
5. Read [corpus-lineage.md](corpus-lineage.md).
6. Read [supersession-map.md](supersession-map.md).
7. Read [locked-actual-decrement-map.md](locked-actual-decrement-map.md).
8. For physics work, read [physics-domain-mature-status.md](physics-domain-mature-status.md), [physics-domain-work-plan.md](physics-domain-work-plan.md), and [dimension-and-spacetime-status.md](dimension-and-spacetime-status.md).
9. For proof or status work, read [known-failure-modes.md](known-failure-modes.md).

## Source-location rule

GitHub is the primary execution corpus for every migrated file. Google Drive is used only for missing-source recovery, migration comparison, or provenance.

Most migrated sources are at repository root. Former Drive folder paths are historical unless the directory visibly exists. `_compiler/`, `overview/`, `tools/`, and `.github/` are actual directories.

Do not cite a source as locally available until its repository path resolves. Do not infer authority from location.

## Do not average the corpus

A statement appearing in a file is evidence, not automatic authority. Apply the claim-specific priority order and evidence rules in [Corpus Authority and Supersession](corpus-lineage.md). In particular, direct current rulings and surviving explicit repairs govern their exact claims until absorbed; status ledgers may govern standing without replacing detailed derivations; summaries, metadata, file order, and partial compiler coverage never settle authority by themselves.

Classify apparent disagreement before resolving it: contradiction, supersession, refinement, conditional scope, different reading, grade difference, shorthand, compression, or notation change.

## Standing discipline

Keep claim standing separate from warrant route, conditions, confidence, workflow state, and disposition. Apply [Claim Standing and Warrant](claim-status-vocabulary.md); never upgrade either axis. `Locked actual` is deprecated. Exact `3+1` is governed by [dimension-and-spacetime-status.md](dimension-and-spacetime-status.md), not by package-era cautions, arity-to-dimension shortcuts, or D6 stability alone.

## No tool theater

A computation must be capable of returning against the thesis. Hard-coded outputs, print-only confirmation, and prose masquerading as simulation are prohibited. Historical verifier output is provenance unless the exact verifier is rerun against the exact current artifacts.

## Historical and shadow files

Package-era and superseded files must be treated as provenance unless later work explicitly preserves the claim. Files under `overview/` are migration shadows unless expressly classified otherwise. Never let a shadow duplicate override its root-level governing counterpart.

## Canonical vocabulary

Use [vertical-and-horizontal.md](vertical-and-horizontal.md):

- vertical = synchronic office-composition / admissibility / `J`;
- horizontal = diachronic accumulation / realizability / `rho`;
- layers and nesting = horizontal;
- color = This-flattening / interior triadic distinction.

## Required execution record

For new substantive work, state:

- repository files read;
- any Drive sources used because the GitHub source was absent;
- claim standing and warrant route for each load-bearing claim;
- historical or superseded sources consulted;
- open joints touched;
- verification performed;
- files changed or created.
