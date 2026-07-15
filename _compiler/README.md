# Compiler Workspace

The `_compiler` directory is the semantic-adjudication workspace for the Triadic Closure corpus. Its compilation unit is a semantic object, not a document. [Agent Execution Rules](../agent-execution-rules.md) is the canonical normalization discipline; this page states only workspace-specific requirements.

## Execution discipline

- Activate exactly one semantic unit and write its opening note before editing.
- Treat every other unit as read-only except for propagation required by the active result.
- Collect current, superseded, adversarial, summary, frontier, and downstream sources before adjudication.
- Run applicable compiler passes one objective at a time. If a pass exposes an earlier-pass defect, return to the earliest affected pass.
- Do not perform new research to close a corpus debt. Preserve the strongest warranted result and synchronize the local and global frontier.
- Do not retain compiler inventories, adjudication packets, or reports after their unique work is absorbed.
- Complete propagation, Pass 11 verification, the fresh-AI test, and a second no-change compiler cycle before claiming fixed point.
- Record actual commit SHAs and tool scope; intentions and historical verifier output are not completion evidence.

## Source authority after migration

GitHub is the primary execution source for every migrated file listed in [../repository-inventory.md](../repository-inventory.md). Google Drive is secondary and may be used only for:

- recovering a source not yet migrated;
- checking migration completeness;
- comparing provenance or prior versions;
- resolving a citation whose GitHub target is absent.

Every evidence ledger should record whether support came from GitHub, Drive, or both. A Drive copy does not override a migrated GitHub source merely by location; authority remains claim-specific.

The supplemental foundation audit and chemistry deposit retain only their stated grades. The nine-document reconstruction has no authority and must not be consulted.

## Governing compilation rule

Encountering a claim begins the work. Before retention, revision, or removal, search the accessible corpus for earlier and later formulations, detailed derivations, repairs, objections, status changes, downstream expenditures, conflicting summaries, notation changes, dependencies, and propagation targets.

Normal claim-specific authority order:

1. a current direct Jordan ruling, for the exact claim ruled on, until propagated;
2. the latest surviving explicit repair, supersession, or adjudication, for the exact claim it resolves;
3. the latest integrated frontier ledger or concept-load ledger, for the exact claim it grades or closes;
4. the latest complete detailed derivation that incorporates the relevant repair;
5. portions of an earlier detailed derivation that have not been superseded;
6. a current frontier, quarantine, or implementation document, only for the boundary it defines;
7. downstream work that necessarily spends the corrected result;
8. summaries, status pages, and reading guides;
9. compiler inventories;
10. historical failed routes, development ledgers, migration reports, memorials, and reverted commits.

Chronology alone does not settle authority. A direct ruling governs only its exact claim until propagated; after full absorption, the standalone ruling record is provenance.

## Required adjudication record

A completed semantic unit should state:

- canonical formulation;
- epistemic state: Open, Conjectured, or Secured;
- warrant route and reach;
- scope, conditions, and debts;
- registration state for every inherited name;
- licensed legacy core and quarantined surplus for Registered use;
- bidirectional content-identity and scope for Registered–Sealed use;
- dependencies;
- downstream expenditures;
- adjudication among competing formulations;
- excluded obsolete revivals;
- open joints;
- propagation targets;
- evidence ledger with repository paths and source location.

## Contradiction and living-content discipline

Classify disagreement before resolving it: contradiction, supersession, refinement, conditional scope, different reading, grade difference, shorthand, compression, or notation change. Do not silently harmonize genuine contradictions or preserve retired formulations as living identities.

Deleting an obsolete formulation requires identifying its replacement unless the underlying claim was explicitly abandoned. Absence from `_compiler` never implies absence from the framework.

## Standing discipline

Framework warrant and semantic registration are independent. Epistemic state is Open, Conjectured, or Secured; registration is Native, Unregistered, Registered, or Registered–Sealed. Registration contributes no warrant. Every Registered use carries a licensed-core and quarantined-surplus ledger; Registered–Sealed requires scoped bidirectional content-identity. Normalize legacy compounds through [../claim-status-vocabulary.md](../claim-status-vocabulary.md). Historical verifier output is provenance unless the exact verifier is rerun against the exact current artifact. `Locked actual` is deprecated.

## Semantic identity

Until a global symbol table exists, semantic identity is `<inventory path> + <semantic heading>`. Bare legacy labels are local and non-unique.

## Adjudication state

Every claim currently present in `_compiler` has undergone a corpus-wide adjudication pass. This does not mean every living claim in the migrated GitHub corpus has been ingested. The newly reconciled repository inventory contains many detailed physics sources still absent from the compiler graph.

## Current compiler files

See this directory directly for the governing inventories, the ten-part Triadic Structure inventory, and the chemistry supplement inventory. [source-manifest.md](source-manifest.md) identifies the two supplemental deposits.

## Source-coverage boundary

The substantive chemistry D1–D4 deposit remains absent from the migrated GitHub corpus. Treat its manifest entry as supplemental evidence until the source is recovered and its owning chemistry unit is active. Do not let that absence redirect an unrelated active unit.