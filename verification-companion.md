---
title: Verification Companion
type: result
created: 2026-06-21
updated: 2026-06-21
status: current
confidence: high
sources:
  - verify.py
historical_sources:
  - verification-companion.md
  - _meta/verify-output.txt
---

# Verification Companion

The verification companion gives findings, grades, dependencies, falsifiers, and a replication protocol for the mathematical-domain walk.

## Mature status

Status: **current verification support**, finite-range / lemma-grade where tagged.

The checks support the mathematical-domain walk. They do not automatically seal physics-domain claims.

## Local verification

`verify.py` was run locally during wiki creation.

Result: **9/9 checks passed**.

Output stored at `_meta/verify-output.txt`.

## Scope caution

Machine checks are finite-range and lemma-grade where tagged as such. They are not automatically formal proofs.

See also: [claim-status-vocabulary](claim-status-vocabulary.md), [known-failure-modes](known-failure-modes.md), [corpus-lineage](corpus-lineage.md).
