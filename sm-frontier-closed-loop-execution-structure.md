---
title: SM Frontier Closed-Loop Execution Structure
type: process
status: current
updated: 2026-07-15
---

# SM Frontier Closed-Loop Execution Structure

## Purpose

This folder exists to remove mature-physics smuggling from the framework by deriving clean framework-native equivalents for the physics concepts that are actually load-bearing.

The loop works backwards from established physics: first identify what the physics concept actually does in physics, then identify what the wiki is asking it to do, then derive the framework-native equivalent of that capacity. Do not ask a physics concept to do more than it does in physics. Do not pass a framework result by merely renaming a physics concept.

## Loop

For one frontier item at a time:

1. **Measure load.** Read the actual downstream text. No “if”; identify what the concept is actually required to do.
2. **Name the physics capacity.** State what the established physics/math concept actually does.
3. **Translate the capacity.** State the exact framework-native object/function that must perform the same work.
4. **Attempt derivation.** Prove it, weaken it, quarantine it, or identify the exact missing premise/countermodel.
5. **Verify adversarially.** A verifier checks against actual downstream use and against over-asking the physics concept.
6. **Integrate only on PASS.** Patch dependent pages only after the upstream item genuinely carries the measured load.

## Pass states

- **PASS** — framework-native derivation carries every measured downstream load for the item.
- **CONDITIONAL** — the concept works only under explicit premises; downstream pages must carry those premises.
- **QUARANTINED** — the concept may be used only as empirical observation, mathematics-as-mathematics, or mature-physics comparison.
- **OPEN / MISSING PREMISE** — exact missing premise named; do not hide it under better prose.
- **COUNTERMODEL** — current derivation route fails.

## Agent rule

Every loop output must contain:

1. Concept.
2. Physics capacity.
3. Framework use with file/line evidence.
4. Native derivation target.
5. Derivation attempt or exact blocker.
6. Pass/fail verdict.
7. Integration rule.

## Current concept-load ledger

For Items 3-10, use:

- [[03-10-physics-concept-load-pass-ledger]]

For Item 2 load-audit correction, use:

- [[02-amplitude-readout]]
- [[02-with-to-this-item2-load-audit]]


## Completed 2026-07-15 execution

The ordered full-load packets and verdicts are indexed at [lineage-execution/README.md](lineage-execution/README.md). Component grades and quarantines remain controlling; a lineage PASS does not promote them.
