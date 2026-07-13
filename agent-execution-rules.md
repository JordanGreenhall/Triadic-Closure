---
title: Agent Execution Rules
type: process
created: 2026-06-21
updated: 2026-07-13
status: control
confidence: high
sources:
  - cover-letter.md
  - physics-walk-checklist.md
---

# Agent Execution Rules

These rules govern future agents using this repository for execution.

## Start here every time

1. Read [README.md](README.md).
2. Read [index.md](index.md).
3. Read [SCHEMA.md](SCHEMA.md).
4. Read [Corpus Lineage](corpus-lineage.md).
5. Read [Supersession Map](supersession-map.md).
6. Read [Locked Actual Decrement Map](locked-actual-decrement-map.md).
7. For physics-domain work, read [Physics Domain Mature Status](physics-domain-mature-status.md) and [Physics Domain Work Plan](physics-domain-work-plan.md).
8. Read [Dimension and Spacetime Status](dimension-and-spacetime-status.md).
9. For theorem, proof, or status work, read [Known Failure Modes](known-failure-modes.md).

## Repository path discipline

The corpus is stored primarily at repository root. Former Google Drive paths such as `results/`, `overview/`, `process/`, `concepts/`, `raw/package/`, and `raw/context/` are not current repository topology unless the directory is visibly present.

- Resolve ordinary corpus files by root-level basename.
- Use GitHub-resolvable Markdown links in governing documents.
- Preserve obsolete folder-qualified paths only when explicitly labeled as historical provenance.
- Do not infer semantic authority from a former folder name.
- `_compiler/` remains a real directory and must retain its path prefix.
- Do not cite a source or conversation ledger as present unless its repository path resolves.

## Do not average the corpus

A claim appearing in a file is not enough. Determine its standing and its claim-specific lineage:

- current;
- historical;
- superseded;
- Open;
- Conjectured;
- Conjectured-strong;
- Registered-candidate;
- Registered;
- Registered and Sealed;
- Defended posit;
- Dissolved;
- computed or check-only.

Deprecated `locked actual` language must be translated through [Locked Actual Decrement Map](locked-actual-decrement-map.md).

## Claim-specific authority

For a disputed or multiply stated claim, inspect the whole relevant lineage. Prefer:

1. the most advanced complete detailed derivation available in the repository;
2. later detailed repairs or extensions;
3. explicit adjudications and current rulings;
4. downstream work that necessarily spends and sharpens the claim;
5. current control pages;
6. summaries and orientation prose.

A summary may route the reader but may not erase a stronger detailed result.

## No tool theater

A computation must be a real computation whose result could have come back against the thesis.

Forbidden:

- writing a formula by hand and printing it as confirmed;
- hard-coding the desired result;
- using Python or shell merely to display prose as evidence;
- calling an assertion a simulation.

Allowed:

- deterministic checks where actual conditions are evaluated;
- mechanical link and lint checks;
- calculations whose input is not the desired conclusion;
- scripts that surface failures and can return nonzero.

Where no derivation exists, state that the framework does not currently derive the claim.

## Do not upgrade modal status

If a source says argued, do not report proved. If it says selection, do not report forced. Keep warrant route and claim standing distinct.

Spacetime-dimensionality special case: exact `3+1` is Registered and Sealed at the same strength as triadic exactly-three plus horizontal flattening—three With-flattened spatial degrees plus one From-succession direction. Do not present this as a completed formal theorem, and do not justify it by arity-to-dimension or D6 stability alone.

## Canonical vocabulary

Use [Vertical and Horizontal](vertical-and-horizontal.md):

- vertical = synchronic office-composition / admissibility / J;
- horizontal = diachronic accumulation / realizability / ρ;
- layers or nesting = horizontal-standing-face, not canonical vertical;
- color = This-flattening / interior triadic distinction, not mediation carrier.

## Execution outputs

When producing new work from this repository, include:

- source pages read;
- current repository paths used;
- status of each claim used;
- whether historical or superseded material was consulted;
- open joints touched;
- verification performed;
- exact files changed or created.

See also: [Known Failure Modes](known-failure-modes.md), [Supersession Map](supersession-map.md), and [Vertical and Horizontal](vertical-and-horizontal.md).
