---
title: Agent Execution Rules
type: process
created: 2026-06-21
updated: 2026-06-21
status: control
confidence: high
sources:
  - raw/context/full-conversation-ledger.md
  - raw/package/physics-walk-checklist.md
  - raw/package/cover-letter.md
---

# Agent Execution Rules

These rules govern future agents using this wiki for execution.

## Start here every time

1. Read `SCHEMA.md`.
2. Read [[corpus-lineage]].
3. Read [[supersession-map]].
4. Read [[locked-actual-decrement-map]].
5. If doing physics-domain work, read [[physics-domain-mature-status]] and [[physics-domain-work-plan]].
6. Read [[dimension-and-spacetime-status]].
7. Read this page.
8. If doing theorem/proof/status work, read [[known-failure-modes]].

## Do not average the corpus

The raw package contains historical and superseded files. A claim appearing in a file is not enough. Determine its standing:

- current;
- historical;
- superseded;
- Open;
- Conjectured;
- Registered;
- Registered and Sealed;
- contested;
- computed/check only;
- deprecated/raw-package `locked actual` requiring translation through [[locked-actual-decrement-map]].

## No tool theater

A computation must be a real computation whose result could have come back against the thesis.

Forbidden:

- writing a formula by hand and printing it as "confirmed";
- hard-coding the desired result;
- using Python/Bash merely to display prose as if it were evidence;
- calling an assertion a simulation.

Allowed:

- deterministic checks like `verify.py` where actual conditions are evaluated;
- mechanical link/lint checks;
- calculations whose input is not the desired conclusion;
- scripts that surface failures and can return nonzero.

If there is no derivation, say: **the framework does not currently derive this**.

## Do not upgrade modal status

If a source says "argued," do not report "proved." If it says "selection," do not report "forced." If raw package text says `locked actual`, do not use that status directly; translate it through [[locked-actual-decrement-map]] into Open, Conjectured, Registered, or Registered and Sealed.

Spacetime-dimensionality special case: exact `3+1` is Registered and Sealed at the same strength as triadic exactly-three plus horizontal flattening: three With-flattened spatial degrees plus one From-succession direction. Do not present this as a completed formal theorem, and do not justify it by arity-to-dimension or D6 stability alone.

## Canonical vocabulary

Use the current vocabulary from [[vertical-and-horizontal]]:

- vertical = synchronic office-composition / admissibility / J;
- horizontal = diachronic accumulation / realizability / ρ;
- layers/nesting = horizontal-standing-face, not canonical vertical;
- color = This-flattening / interior triadic distinction, not mediation carrier.

## Execution outputs

When producing new work from this wiki, include:

- source pages read;
- status of each claim used;
- whether any superseded material was consulted;
- open joints touched;
- verification performed;
- exact files changed or created.

See also: [[known-failure-modes]], [[supersession-map]], [[vertical-and-horizontal]].
