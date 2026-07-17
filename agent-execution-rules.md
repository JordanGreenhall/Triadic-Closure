---
title: Agent Execution Rules
type: process
updated: 2026-07-17
status: control
confidence: high
sources:
  - repository-inventory.md
  - corpus-lineage.md
  - claim-status-vocabulary.md
  - known-failure-modes.md
  - physics-walk-checklist.md
  - jordan-decisions.md
---

# Agent Execution Rules

This is the canonical execution discipline for semantic normalization of the Triadic Closure corpus. It governs how an agent works; it does not decide theory content, authority, or claim warrant.

## 1. Start here

Before substantive work, read:

1. [README.md](README.md)
2. [index.md](index.md)
3. [repository-inventory.md](repository-inventory.md)
4. [SCHEMA.md](SCHEMA.md)
5. [corpus-lineage.md](corpus-lineage.md)
6. [supersession-map.md](supersession-map.md)
7. [claim-status-vocabulary.md](claim-status-vocabulary.md)
8. [known-failure-modes.md](known-failure-modes.md)
9. Any domain controls named by the active unit

GitHub is the primary execution corpus for migrated material. Use an external source only for missing-source recovery, migration comparison, or provenance, and record that use. A search failure is not evidence that a claim or source does not exist.

## 2. Three independent control questions

Do not conflate:

- **C1 — Authority:** which formulation governs the exact disputed claim?
- **C2 — Warrant and registration:** what has the framework secured, by what route and reach, and what inherited name is licensed?
- **C3 — Execution:** how must normalization be performed?

C3 may apply C1 and C2 results. It may not silently redo them.

## 3. Active semantic-unit discipline

Work on semantic units, not arbitrary files and not the corpus as a whole.

A semantic unit is the smallest coherent region with its own authority lineage, dependency structure, natural canonical home, and local frontier. It must be large enough that its contents mutually define one another and small enough to reach a fixed point without normalizing the whole domain.

Rules:

1. Exactly one semantic unit is active.
2. All other units are read-only except for propagation strictly required by the active unit.
3. Do not solve an interesting neighboring issue merely because it appears during review.
4. Record a non-blocking out-of-unit defect as a queued dependency or frontier, then continue.
5. If an upstream defect blocks the active unit, suspend it, normalize the upstream unit separately, merge that work, and then resume. Do not combine two semantic units in one opaque change set.
6. A downstream propagation edit may change only the use of the active result; it may not improve unrelated content in the target file.

### Required opening note

Write this before editing:

```text
Unit: [ID and name]
Boundary: [included questions]
Excluded neighbors: [questions not being solved]
Primary dependencies: [units]
Expected downstream propagation: [files or units]
Applicable passes: [numbers]
```

## 4. Source-set and authority discipline

For the active unit, collect every accessible:

- current canonical or detailed source;
- explicit repair, supersession, and adjudication;
- frontier, quarantine, or implementation boundary;
- adversarial or failed route with unique evidentiary value;
- summary or status page;
- downstream source that spends the result;
- historical source needed to understand a surviving ambiguity.

Record repository paths and any external provenance. Do not infer authority from location, genre, date, upload time, filename, or self-declared status.

Apply the claim-specific authority order in [corpus-lineage.md](corpus-lineage.md). Classify disagreement before resolving it: contradiction, supersession, refinement, conditional scope, different reading, grade difference, shorthand, compression, or notation change.

## 5. Non-invention and research boundary

Normalization reduces semantic entropy; it does not create new theory.

The agent may adjudicate existing formulations, clarify, rewrite, merge, split, reorder, relocate, archive, delete, propagate, and expose genuine gaps. The agent may not:

- invent a missing premise, derivation, value, or bridge;
- invent a proof obligation by positing a failure mode for which no framework operation has been identified;
- upgrade framework warrant or semantic registration without existing authority;
- import mature domain content as framework content;
- preserve a living contradiction merely for historical completeness;
- treat a temporary ruling or compiler artifact as permanent substitute theory;
- manufacture a computation, citation, or tool result to simulate support.

When the corpus cannot resolve a question:

1. state the exact missing premise, countermodel, calculation, or empirical input;
2. preserve the strongest warranted formulation;
3. record the gap locally and in the global frontier;
4. continue the active unit if the gap is non-blocking.

Under-proof and over-proof are symmetric distortions. Before recording a missing proof, identify the exact operation that could exclude, alter, or defeat the inherited result at the location in question. If no such operation exists, the proposed burden is a manufactured demand and must be removed rather than promoted to the frontier. Whole-ground inheritance does not require constitutive structure to be re-admitted or re-populated in a successor domain.

## 6. One-unit execution loop

1. **Define** the boundary, dependencies, downstream uses, and excluded neighbors.
2. **Collect** the complete source set.
3. **Establish authority** claim by claim.
4. **Build current understanding** with scope and the C2 record.
5. **Run applicable passes** one optimization target at a time.
6. **Propagate** the normalized understanding to every consumer.
7. **Dispose** of residual documents by unique value.
8. **Verify** semantics, links, terminology, frontiers, and fresh-AI comprehension.
9. **Commit** one intelligible pass or unit of work.
10. **Repeat** from the earliest affected pass until a second full cycle produces no change.

A pass that exposes an earlier-pass defect stops. Return explicitly to the earliest affected pass; do not patch around it.

## 7. Compiler passes

| Pass | Target | Constraint |
|---|---|---|
| 0 — Authority | Classify primary, subsidiary, historical, archive, and delete sources. | No prose editing or movement. |
| 1 — Semantic normalization | Resolve contradiction, ambiguity, obsolete wording, duplicated doctrine, and AI hazards. | No directory restructuring. |
| 2 — Propagation | Update every consumer of the corrected understanding. | No unrelated improvement. |
| 3 — Structural normalization | Move, split, merge, or reorder into natural semantic homes. | No theory change. |
| 4 — Information architecture | Repair purpose, abstraction level, hierarchy, reading order, and navigation. | Dependency order, not historical order. |
| 5 — Frontier audit | Synchronize every live gap locally and globally; remove stale duplicates. | Do not perform the missing research. |
| 6 — Claim-record normalization | Apply C2 state, warrant, registration, scope, and debt fields. | No unsupported upgrade. |
| 7 — Vocabulary normalization | Give technical terms one stable meaning and preferred use. | Preserve distinct concepts. |
| 8 — Notation normalization | Normalize symbols, variables, equations, and deprecated forms. | Do not hide semantic change as notation. |
| 9 — Compression and disposition | Merge, archive, or delete material that fails the existence test. | Lose no unique understanding or evidence. |
| 10 — Readability | Improve prose, titles, transitions, examples, and section order. | Only after semantics stabilize. |
| 11 — Verification | Test contradiction, duplication, frontier, link, terminology, propagation, and AI comprehension. | Verification must be capable of failure. |

### Typical pass selection

| Region | Passes |
|---|---|
| Control: authority | 0, 1, 2, 3, 4, 7, 9, 10, 11 |
| Control: warrant and registration | 0, 1, 2, 6, 7, 8, 9, 10, 11 |
| Control: execution discipline | 0, 1, 3, 4, 7, 9, 10, 11 |
| Foundation or physics derivation | 0–11 |
| Generic method / D-series | 0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11 |
| Mathematics | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 |
| Physics quarantine / boundary | 0, 1, 2, 4, 5, 6, 7, 9, 10, 11 |
| Interface or chemistry | 0–11 |

Required propagation remains part of every unit even when Pass 2 is not a separately emphasized pass.

## 8. Propagation discipline

Propagation is complete only when every living consumer either:

- states the normalized result accurately;
- links to the canonical home without restating unstable doctrine;
- is marked historical or superseded; or
- is removed because it has no unique value.

Search for concepts and paraphrases, not only exact phrases. Check summaries, status matrices, execution controls, frontiers, compiler inventories, indexes, and downstream derivations. A correction is not complete while a competent reader or AI can still recover the obsolete answer from living content.

## 9. Framework warrant and semantic registration

Keep C2’s axes independent.

- Framework epistemic state for claims offered for warrant: Open / Conjectured / Secured.
- Foundational premise category: Pure posit, with no warrant claimed and downstream dependence explicit.
- Semantic registration: Native / Unregistered / Registered / Registered–Sealed.

A pure posit is neither Conjectured nor Secured and is not an incomplete defended posit. Every Secured claim names warrant route, reach, scope, conditions, and debts. Every Registered use states the licensed core and quarantined surplus. Registered–Sealed requires scoped bidirectional content identity. Registration contributes no warrant. Apply [claim-status-vocabulary.md](claim-status-vocabulary.md); `locked actual` is deprecated.

## 10. Frontier discipline

Every live gap appears in exactly two places:

1. locally at the actual live edge;
2. in the single corpus-wide frontier summary.

A frontier entry states:

- exact open claim or derivation;
- current strongest result and C2 record;
- what is already established;
- precise missing premise, countermodel, calculation, or empirical input;
- dependencies and downstream claims affected;
- false-completion risk;
- next legitimate research action, without performing it in compiler mode.

Do not create independent third frontier lists.

## 11. File disposition and creation restraint

Allowed dispositions are Canonical, Supporting, Adjudicative, Frontier, Historical, Memorial, and Delete.

Before retaining a file, ask:

1. What unique understanding disappears if it vanishes?
2. Is that value current theory, necessary evidence, a live frontier, or only history?
3. Can its unique content move to a more natural home without loss?
4. Would retention create duplicate doctrine or AI ambiguity?

If deletion loses nothing, delete. If only developmental history remains, archive or mark historical. If current understanding or necessary evidence would be lost, keep. Create a permanent file only when a genuine semantic region has no natural current home.

Before moving, archiving, or deleting, verify unique value and repair every link, index, inventory, and source reference affected.

## 12. Tool integrity

A tool call used as epistemic support must do real work and be capable of returning against the thesis.

- No hard-coded outputs, print-only confirmation, prose masquerading as simulation, or fabricated citations.
- State what the tool actually tests, its inputs, and its limits.
- Historical verifier output is provenance unless the exact verifier is rerun against the exact current artifacts.
- A successful command does not verify claims outside its tested scope.
- A failed or partial search does not prove absence.
- Do not claim a file mutation, external action, commit, or PR exists until the returned state confirms it.
- Preserve current user changes and unrelated work.
- Use the least destructive operation that satisfies the active unit.

See [known-failure-modes.md](known-failure-modes.md).

## 13. Verification and fixed point

### Semantic checks

- Every in-unit claim agrees with the adjudicated current formulation.
- No obsolete formulation remains in living content.
- Summaries preserve scope and qualifications.
- C2 epistemic state, pure-posit category, warrant, and registration are separate and accurate.
- Conditional and idealized results are scoped.

### Structural checks

- Each idea is at its natural abstraction level.
- No file performs incompatible semantic jobs without necessity.
- Canonical doctrine is not duplicated.
- Reading order follows dependency.

### Frontier checks

- Every live gap is local and global.
- Resolved frontiers are removed.
- No summary silently reports a frontier as complete.

### Repository checks

- Links and renamed paths resolve.
- Navigation and inventory match the actual tree.
- Propagation searches return no living obsolete use.
- Verification tools run against current artifacts and report their real scope.

### Fresh-AI comprehension test

Read the unit as a competent model with no conversational memory. It fails if that reader could reasonably select the wrong authority, recover an obsolete answer, confuse scope, infer invented content, or mistake a tool demonstration for proof.

### Fixed-point criterion

A unit is complete only when authority is stable, contradictions are absent, propagation is complete, structure is coherent, frontiers are exact, every file passes the existence test, and a second full compiler cycle produces no further change.

## 14. GitHub discipline

- Begin from current merged `main`.
- Use a branch dedicated to one semantic unit.
- Keep commits small, intelligible, and organized by pass.
- Do not mix authority adjudication, semantic repair, structural movement, and prose polishing in one opaque commit.
- Repair links after moves or renames.
- Use surviving GitHub state, not memory of a reverted or closed branch.
- Do not report completion before the commit exists and Pass 11 plus the second-cycle check have run.
- Open the unit PR only after the branch diff is coherent; keep later units out.

## 15. Required records

### Unit completion record

```text
Semantic unit:
Passes completed:
Sources examined:
Changes made:
Contradictions resolved:
Propagation targets updated:
Files kept / merged / archived / deleted:
Frontiers added / removed:
Remaining blockers or queued dependencies:
Verification performed:
Commit SHA(s):
```

### Per-pass record

For each completed pass, record the pass, sources examined, changes made, contradictions resolved, propagation targets, file dispositions, frontier changes, blockers, and commit SHA.

Do not report intentions as accomplishments. Do not claim completion until the commit exists and the fixed-point checks have run. State partial progress exactly.
