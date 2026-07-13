---
title: Verification Companion
type: result
created: 2026-06-21
updated: 2026-06-21
status: current
confidence: high
sources:
  - raw/package/verification-companion.md
  - raw/package/verify.py
  - _meta/verify-output.txt
---

# Verification Companion

The verification companion gives findings, grades, dependencies, falsifiers, and a replication protocol for the mathematical-domain walk.

## Mature status

Status: **current verification support**, finite-range / lemma-grade where tagged.

The checks support the mathematical-domain walk. They do not automatically seal physics-domain claims.

## Local verification

`raw/package/verify.py` was run locally during wiki creation.

Result: **9/9 checks passed**.

Output stored at `_meta/verify-output.txt`.

## Scope caution

Machine checks are finite-range and lemma-grade where tagged as such. They are not automatically formal proofs.

See also: [[claim-status-vocabulary]], [[known-failure-modes]], [[corpus-lineage]].
