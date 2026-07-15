---
title: Corpus Normalization Execution Rules
type: process
updated: 2026-07-15
status: control
confidence: high
sources:
  - corpus-lineage.md
  - claim-status-vocabulary.md
  - known-failure-modes.md
  - physics-walk-checklist.md
  - sm-frontier-closed-loop-execution-structure.md
---

# Corpus Normalization Execution Rules

This is the durable execution contract for compiling the Triadic Closure corpus into a smaller, clearer, internally coherent living system. The compiler preserves warranted understanding. It does not invent theory, raise standing, or manufacture closure.

## 1. Governing constraints

1. Work on **semantic units**, not whole files and not the whole corpus at once.
2. Keep exactly one semantic unit active. Other units are read-only except for required propagation from the active unit.
3. Apply [Corpus Authority and Supersession](corpus-lineage.md) claim by claim. Do not average sources or infer authority from polish, date, location, or compiler coverage.
4. Keep standing, warrant, premises, conditions, confidence, workflow state, and disposition separate under [Claim Standing and Warrant](claim-status-vocabulary.md). Never upgrade standing or warrant.
5. Preserve every live dependency, derivation, counterargument, empirical input, scope restriction, and frontier. Compression is permitted only after meaning and load are accounted for.
6. Stop at the research boundary. When support is insufficient, state the strongest warranted formulation and the exact missing premise, countermodel test, calculation, or empirical input. Do not solve the research problem unless separately authorized.
7. A normalization is complete only at a verified fixed point, not when the prose sounds finished.

## 2. Required start sequence

Before substantive work, read:

1. [README.md](README.md)
2. [index.md](index.md)
3. [repository-inventory.md](repository-inventory.md)
4. [SCHEMA.md](SCHEMA.md)
5. [Corpus Authority and Supersession](corpus-lineage.md)
6. [Claim Standing and Warrant](claim-status-vocabulary.md)
7. [Known Failure Modes](known-failure-modes.md)

Then read every source, status ledger, repair, objection, historical formulation, downstream expenditure, and frontier document relevant to the active unit. GitHub is the primary execution corpus for migrated files. Use an external source only for missing-source recovery, migration comparison, or provenance, and record that use.

## 3. Unit opening record

Open every unit with this record before changing the corpus:

| Field | Required content |
|---|---|
| Unit | Stable unit identifier and name |
| Boundary | Exact claims and relations owned by the unit |
| Excluded neighbors | Adjacent questions that remain read-only |
| Dependencies | Upstream claims and controls the unit spends |
| Expected propagation | Downstream pages or controls likely to require synchronized change |
| Applicable passes | Pass numbers expected to bite; all passes must still be checked |

An issue found outside the boundary goes to the appropriate later unit or global ledger unless it is a necessary propagation consequence. If it changes the active unit's authority or premises, return to the earliest affected pass.

## 4. Execution cycle

For one unit:

1. **Define.** Write the opening record and identify exclusions.
2. **Collect.** Search the accessible corpus and history for all relevant formulations, repairs, objections, statuses, uses, notation, and frontier statements. An index is a lead, never proof of completeness.
3. **Adjudicate authority.** Establish the governing formulation for each claim before rewriting it.
4. **Reconstruct current understanding.** State the strongest warranted formulation, its standing and warrant, scope, dependencies, exclusions, and downstream load.
5. **Run passes 0–11 in order.** Each pass has one target. Do not conceal an earlier defect by fixing it in a later pass.
6. **Propagate.** Update every necessary downstream expenditure, control, link, name, status, and frontier consequence.
7. **Dispose.** Assign every touched document a disposition and apply it only after unique content and links are accounted for.
8. **Verify.** Run semantic, structural, frontier, link, status, terminology, tool-integrity, and fresh-reader checks.
9. **Commit.** Commit small semantic/pass-scoped changes; do not mix authority, theory, structure, and prose into an opaque commit.
10. **Reread.** Repeat the compiler cycle. Completion requires a second cycle that produces no warranted change.

## 5. Ordered normalization passes

If a later pass reveals a defect owned by an earlier pass, stop and return to the earliest affected pass. Rerun all following passes after the repair.

| Pass | Target | Required result |
|---:|---|---|
| 0 | Authority | Claim-specific governing source, surviving repairs, conflicts, and supersessions settled |
| 1 | Semantic normalization | One coherent formulation preserving all warranted content and distinctions |
| 2 | Propagation | Every necessary downstream use synchronized; no correction remains local by accident |
| 3 | Structural | Unit boundaries, dependencies, sequence, and document roles made explicit |
| 4 | Information architecture | Canonical homes and navigation expose the current understanding without competing controls |
| 5 | Frontier | Exact local and global frontier entries created, updated, or removed |
| 6 | Claim status | Standing and warrant normalized without inflation; conditions and workflow metadata separated |
| 7 | Vocabulary | Terms made stable, explicit, and non-duplicative without erasing meaningful distinctions |
| 8 | Notation | Symbols and formulas made consistent; local conventions and changes identified |
| 9 | Compression and disposition | Redundancy removed; each document classified and existence-tested |
| 10 | Readability | A careful new reader can recover the argument, scope, and open joints without hidden context |
| 11 | Verification | Semantic, structural, frontier, link, status, vocabulary, notation, AI, and tool checks pass |

## 6. Monotonicity and return rule

A pass may not spend a result that a prior pass has not established. A later edit that changes authority, meaning, dependency, standing, or scope invalidates every downstream pass that relied on it. Return immediately to the earliest affected pass, record the reason, and rerun forward. Repeated cosmetic passes do not substitute for this return.

## 7. Propagation rule

Propagation is semantic, not a search-and-replace exercise. For each changed claim, inspect:

- definitions and concise summaries;
- detailed derivations and proof dependencies;
- downstream applications and quantitative expenditures;
- status, supersession, load, boundary, and frontier ledgers;
- indexes, reading orders, schema, compiler inventories, and automation;
- historical pages whose current/historical boundary would otherwise become misleading.

Change only what the active unit requires. If a downstream page contains a separate defect, queue it. If the page cannot remain correct without resolving that defect, expose the blocker rather than silently broadening scope.

## 8. Document disposition

Every document touched in a unit receives one disposition:

- **Canonical** — natural home of the living formulation.
- **Supporting** — unique derivation, example, implementation, or explanation that supports a canonical home.
- **Adjudicative** — temporary repair, ruling, status, load, or boundary packet awaiting absorption.
- **Frontier** — exact open-work record that is not duplicated elsewhere.
- **Historical** — provenance that is useful but not living authority.
- **Memorial** — intentionally preserved record with contextual rather than doctrinal value.
- **Delete** — no unique semantic, evidentiary, frontier, or memorial value remains.

Before retaining a file, ask whether the corpus would lose unique warranted understanding, necessary evidence, an exact frontier, or intentional memory if it vanished. Before deletion, identify the replacement or the explicit abandonment, inspect history, verify inbound links, propagate necessary content, and repair navigation. File count is not a success metric.

## 9. Frontier discipline

An unresolved issue appears in exactly two places:

1. locally, at the claim or derivation it limits; and
2. globally, in the active frontier ledger for cross-corpus planning.

Each frontier entry must state:

- the exact unresolved claim and current standing;
- what is established;
- the missing premise, countermodel test, calculation, or empirical input;
- dependencies and downstream consequences;
- the false-completion risk;
- the next legitimate research action.

Do not scatter duplicate open-work prose across summaries and process files. When research support is insufficient, write the exact boundary and continue normalization; the compiler must not fill the gap with conjecture, mature-domain import, or smoother prose.

## 10. Domain-specific closed loops

Some research programs use additional pass states such as `PASS`, `CONDITIONAL`, `QUARANTINED`, `OPEN / MISSING PREMISE`, and `COUNTERMODEL`. These are workflow or integration verdicts, not replacements for corpus standing. The [SM Frontier Closed-Loop Execution Structure](sm-frontier-closed-loop-execution-structure.md) is one such supporting protocol.

A frontier item is not a loop. A loop is the repeated attempt on one item until a valid pass verdict, countermodel, exact missing-premise boundary requiring controller judgment, or explicit human stop. Integration occurs only to the extent licensed by both the verdict and the claim standing.

## 11. Verification gates

### Semantic

- The governing formulation matches the adjudicated lineage.
- No contradiction is silently harmonized.
- No derivation, dependency, objection, qualification, or downstream load has been lost.
- No claim is strengthened by condensation, terminology, or status translation.

### Structural

- Canonical homes and supporting roles are unambiguous.
- Governing links resolve and the repository inventory matches the tree.
- No shadow, compiler artifact, status page, or historical file presents a competing current formulation.
- Moves and deletions have repaired inbound references.

### Frontier

- Every unresolved load-bearing issue is stated locally and globally, exactly once in each role.
- Closed work is removed from the frontier; open work is not narrated as complete.
- Dependencies, false-completion risk, and next action are explicit.

### Fresh-agent / AI

A fresh reader given only governing navigation must be able to recover the same authority, standing, scope, dependency graph, and frontier without relying on chat context. Check specifically for partial-corpus inference, invented paths, stale summaries, completion theater, and unreported partial work.

### Tool integrity

A computation must be capable of returning against the thesis. Hard-coded outputs, print-only confirmation, prose presented as simulation, unverifiable tool claims, and stale verifier output are not evidence. Historical output is provenance unless the exact verifier is rerun against the exact current artifacts.

## 12. Fixed-point criterion

A unit is complete only when:

1. passes 0–11 have run in order with all returns resolved;
2. propagation and dispositions are committed;
3. verification gates pass against the committed tree; and
4. a second full compiler cycle finds no further authority, semantic, propagation, structural, frontier, standing, vocabulary, notation, compression, or readability change.

“No change” means no warranted change, not that a deadline was reached. If the second cycle changes anything, recommence at the earliest affected pass.

## 13. GitHub and reporting discipline

GitHub is the execution record. Verify the branch and committed contents after every write. Keep commits small and labeled by semantic unit and pass; verify a target before deletion or link repair; use repository history when current files do not settle lineage.

Report each committed unit with:

- semantic unit;
- pass or pass range;
- sources actually read;
- changes actually committed;
- contradictions and their classifications;
- propagation performed;
- document dispositions;
- local and global frontier effects;
- blockers or deliberately queued issues;
- commit SHA;
- fixed-point result.

Do not report intentions as accomplishments. Do not say a unit or corpus is complete without the relevant commit and fixed-point verification. When work is partial, state the exact last completed unit and the first unfinished pass.

## 14. Corpus order

Run units in this order unless a return to an earlier unit is required:

1. Control: `C1` authority and supersession; `C2` standing and warrant; `C3` execution discipline.
2. Foundation: `F1`–`F5`.
3. Mathematics: `M1`–`M4`.
4. Physics: `P1`–`P29`.
5. Cross-domain gate: `X1`.
6. Chemistry: `CH1`–`CH10`.
7. Global architecture, archive/delete, verification, and release passes.

Only one unit is active. A required correction to an earlier completed unit triggers the return rule; otherwise out-of-order findings are queued.
