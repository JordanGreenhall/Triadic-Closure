# Triadic Closure Repository Schema

## Domain

This repository is the primary execution corpus for Jordan Hall's Triadic Closure project. It contains the living foundational, mathematical, physical, physics-to-chemistry, and chemical corpus together with current controls and subordinate compiler artifacts.

## Repository topology

Most substantive Markdown files live at repository root. The complete current inventory is [repository-inventory.md](repository-inventory.md).

Directories with distinct live roles:

- `_compiler/` — semantic adjudication and verification artifacts subordinate to the substantive corpus;
- `13-higgs-yukawa-electroweak-generations-spectrum-quarantine/` — retained boundary packet.

Former Drive paths and deleted repository paths are not live navigation.

## Source-location rule

For a migrated root document, use its root basename. Do not infer standing or authority from a former folder name. Historical source paths may appear only when required to identify an unmigrated source.

## Document roles

- `overview` or `control` — current orientation, lineage, supersession, status, and execution controls;
- `concept` — framework vocabulary and structural concepts;
- `result` — current result modules and derivations;
- `claim` — focused claims with explicit standing;
- `process` — current execution and QA rules;
- compiler artifact — semantic inventories and verification records under `_compiler/`.

`historical` and `superseded` are transitional lifecycle labels, not permanent retention categories. A document whose only remaining function is historical record should be deleted after useful content is absorbed.

## Frontmatter

For new or repaired documents:

```yaml
---
title: Page Title
type: overview | concept | result | claim | process | control
status: current | contested | open | control
confidence: high | medium | low
sources:
  - source-file.md
---
```

The frontmatter `status` field records document lifecycle or control role only. It never assigns claim standing to the document or every sentence within it.

## Linking rules

1. Governing navigation uses repository-resolvable Markdown links.
2. Root-level migrated files are linked by basename.
3. `_compiler/` paths retain their prefix.
4. Verify a target before changing a link; do not invent basenames.
5. Obsidian wikilinks do not constitute repository navigation.
6. Deleted historical paths must not remain in governing navigation.

## Authority and migration

GitHub is primary for every migrated file. Google Drive is fallback source recovery for files not yet migrated.

Claim authority is semantic and claim-specific. Apply the exact order in [corpus-lineage.md](corpus-lineage.md): current direct ruling for the exact ruled claim until propagation; latest surviving repair or adjudication; integrated ledger; repaired complete derivation; unsuperseded earlier derivation; scoped frontier; necessary downstream expenditure; summaries; compiler inventories. Chronology and metadata alone never settle authority.

## Epistemic warrant and semantic registration

Framework epistemic states are Open, Conjectured, and Secured. A Pure posit is a foundational premise with no warrant claimed. Semantic registration for inherited names is Native, Unregistered, Registered, or Registered–Sealed. Registration contributes no warrant. See [claim-status-vocabulary.md](claim-status-vocabulary.md).

## Agent rules

Before substantive work, read [README.md](README.md), [index.md](index.md), [repository-inventory.md](repository-inventory.md), [corpus-lineage.md](corpus-lineage.md), [supersession-map.md](supersession-map.md), and [agent-execution-rules.md](agent-execution-rules.md).

Normalization activates exactly one semantic unit or one expressly global pass. Other theory remains read-only except for required propagation. Do not average conflicting formulations or let a summary override stronger detailed work.

## Semantic compression rule

The live corpus preserves current semantic capability, not document history.

- If a document is fully superseded, delete it.
- If only part remains useful, extract and compress that material into the proper living owner, verify preservation, and delete the obsolete container.
- Historical record, development sequence, migration provenance, and isolated useful fragments are not sufficient reasons for retention.
- Git history is the archive.
- Retention requires a substantial current semantic, proof, frontier, control, or navigation function that cannot be provided more simply elsewhere.

The preferred operation is `extract -> compress -> integrate -> verify -> delete`, not `retain -> label obsolete`.

## Semantic-unit quality gate

A normalization unit is complete only when authority and canonical formulation are stable; propagation is complete; no living contradiction or obsolete answer remains recoverable; local and global frontiers agree; retained files have unique current value; links and navigation resolve; verification was capable of failure; a fresh reader selects the right source; and a second full cycle produces no further change.

## Repository quality gate

A global architecture or compression pass is complete only when:

- the inventory matches the actual tree;
- governing links resolve;
- one canonical reader path exists;
- duplicate navigation is removed;
- every retained document performs a substantial current function;
- useful fragments have been absorbed before obsolete containers are deleted;
- no document remains solely for historical record;
- semantic content and claim standing are unchanged except where an explicitly activated semantic unit authorizes change.
