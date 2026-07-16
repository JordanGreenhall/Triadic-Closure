---
title: Verification Companion
type: result
created: 2026-06-21
updated: 2026-07-16
status: current
confidence: high
sources:
  - verify.py
  - triadic-structure-of-relating-rev-canonical.md
historical_sources:
  - _meta/verify-output.txt
---

# Verification Companion

This companion separates executable evidence from framework warrant for the mathematical-domain walk.

## Current executable result

The current `verify.py` on the M1 branch was executed with Python 3 on 2026-07-16.

Result: **9/9 checks passed**.

The script is deterministic and uses only the Python standard library. Its checks are finite-range or lemma-grade evidence at the scopes named by V1–V9; a passing run is not by itself a framework derivation or a registration seal. The historical output at `_meta/verify-output.txt` remains provenance rather than current evidence.

## M1 evidence boundary

M1 concerns the gate and boundary of mathematics, boundary-registration at D1, the unmarked dyad, non-collapse, and exchange-equivariance.

The current verifier does **not** independently establish that gate, boundary selection, D1 dyad, or non-collapse argument. Those claims receive their framework standing from the dependency, construction, and retorsion traces in Part 9.2 of the canonical foundation.

V4 tests a later orientation-role consequence, and V5–V9 test later mathematical constructions. They must not be cited backward as the warrant for M1. No machine check licenses the inherited name `mathematics`; registration is the separate semantic mapping recorded in the canonical foundation and gateway.

## Replication

Run:

```sh
python3 verify.py
```

A conforming run prints PASS for V1 through V9 and terminates with `9/9 checks passed`. Any failed check is evidence against the exact tested construction at its stated finite scope and requires adjudication; it does not automatically refute or downgrade unrelated framework claims.

See also: [The Triadic Structure of Relating — Canonical Foundation](triadic-structure-of-relating-rev-canonical.md), [Epistemic Warrant and Semantic Registration](claim-status-vocabulary.md), [Known Failure Modes](known-failure-modes.md), and [Corpus Lineage](corpus-lineage.md).
