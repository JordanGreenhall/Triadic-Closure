---
title: Known Failure Modes
type: overview
created: 2026-06-21
updated: 2026-06-21
status: control
confidence: high
sources:
  - physics-walk-checklist.md
historical_sources:
  - raw/context/full-conversation-ledger.md
---

# Known Failure Modes

This page records failure modes that future agents must avoid.

## 1. Tool-theater / fake computation

The conversation ledger contains a major failure involving a script that printed assumed formulas and narrated them as confirmed. This is forbidden.

Rule: if a tool cannot actually test the claim, do not use it to create the appearance of testing.

## 2. Reviving superseded claims

Examples:

- treating F10 as simply "not done" despite `mathematization-F10-resolved.md`;
- treating SU(3) as conditional on (A) despite `gauge-structure-result.md`;
- treating color as a mediation carrier rather than This-flattening.

Always consult [supersession-map](supersession-map.md).

## 3. Vertical/horizontal collapse

Do not confuse:

- vertical office-composition;
- horizontal accumulated layers/nesting;
- standing-face readout of horizontal history.

This collapse causes downstream confusion around J, ρ, composition, and emergence.

## 4. Deprecated `locked actual` status

Do not use `locked actual` as a live status. It is deprecated/disfavored because it hides the proper standing. Translate raw-package `locked actual` language through [locked-actual-decrement-map](locked-actual-decrement-map.md) into Open, Conjectured, Registered, or Registered and Sealed.

Dimensionality special case: exact `3+1` is Registered and Sealed at the same level as triadic exactly-three plus horizontal flattening. Do not downgrade it to a merely empirical trajectory lock, and do not overclaim it as a completed formal theorem.

## 5. Premature physical naming

Do not import mature physics names before the framework earns them. Use recognition language where appropriate.

## 6. Claim-status inflation

Do not convert:

- argued → proved;
- checked → theorem;
- finite-range verification → proof;
- selection → forced;
- raw-package `locked actual` → live status without decrementing through [locked-actual-decrement-map](locked-actual-decrement-map.md).

## 7. Regression to earlier lineage

The conversation shows that earlier docs often contain good work in obsolete frames. Extract provenance carefully; do not restore the old frame.

## 8. Treating the ledger as polished doctrine

The full conversation is a lineage source, not a final document. Use it to understand decisions, not to quote every provisional statement as doctrine.

See also: [agent-execution-rules](agent-execution-rules.md), [supersession-map](supersession-map.md), [corpus-lineage](corpus-lineage.md).
