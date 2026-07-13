# Triadic Closure Physics Corpus

This repository currently contains the uploaded **physics execution corpus** for Jordan Hall's Triadic Closure project. The upload was flattened: files formerly distributed across Google Drive folders now generally live directly at repository root.

The repository does not presently mirror the full Google Drive hierarchy, and its navigation must not assume that it does.

## Current layout

At repository root:

- `README.md` — repository orientation;
- `index.md` — verified navigational index;
- `SCHEMA.md` — repository conventions;
- physics result, control, concept, process, historical, and provenance Markdown files;
- package sources such as `cover-letter.md` and `physics-walk-checklist.md` where uploaded.

Actual subdirectory:

- `_compiler/` — semantic inventories and adjudication controls. These are working control artifacts, not substitutes for the substantive corpus.

## Path rule

The current path for an uploaded root document is simply:

```text
filename.md
```

Former Google Drive paths such as these are stale as repository paths:

```text
results/filename.md
overview/filename.md
concepts/filename.md
process/filename.md
raw/package/filename.md
raw/context/filename.md
```

A former path may be retained as provenance only when explicitly labeled historical. It must not be presented as a live GitHub link.

## Navigation

Use ordinary repository-relative Markdown links:

```markdown
[Mass as Self-Closure](mass-as-self-closure.md)
```

Governing navigation begins with [index.md](index.md). Do not add an index entry until the target filename has been verified in the current repository tree.

Obsidian-style wikilinks may remain inside historical corpus text, but they are not sufficient for GitHub navigation.

## Current verified corpus scope

The verified index currently covers:

- foundational and methodological pages;
- physics control and status pages;
- physics result modules for propagation, Lorentz structure, gauge structure, chiral structure, mass, gravity, Lambda, and related topics;
- claim-status and vertical/horizontal concept controls;
- execution rules and provenance material.

Files known from later Google Drive work must not be assumed present merely because another corpus version contains them.

## Corpus authority

Authority is claim-specific rather than folder-specific or document-wide. For any claim, prefer:

1. the most advanced complete detailed derivation available in this repository;
2. later detailed repairs or extensions;
3. explicit adjudications and current rulings;
4. downstream work that necessarily spends and sharpens the claim;
5. current control pages;
6. summaries and orientation prose.

A newer or shorter summary may not override a stronger detailed derivation.

## Claim standing

The live claim standings are:

- **Open**;
- **Conjectured**;
- **Conjectured-strong**;
- **Registered-candidate**;
- **Registered**;
- **Registered and Sealed**;
- **Defended posit**;
- **Dissolved**.

`Locked actual` is deprecated and must be translated through the current status discipline.

## Editorial rules

- Never upgrade a claim beyond its dependency route.
- Distinguish structural derivation from empirical fit, imported identification, and recognition after the fact.
- Preserve the distinction between vertical office-composition and horizontal accumulation.
- Treat historical source-location metadata as provenance, not current topology.
- Do not infer authority from a former folder name.
- Repair paths without silently changing semantic content.
- Do not cite a conversation ledger or source file as present unless it can be resolved in the repository.

## Maintenance state

The repository is undergoing path normalization after the flattened upload. The current priority is:

1. keep `README.md`, `index.md`, `SCHEMA.md`, `agent-execution-rules.md`, and `corpus-lineage.md` aligned with the actual tree;
2. replace stale folder-qualified navigation with verified root-relative links;
3. distinguish absent Drive sources from uploaded repository files;
4. keep `_compiler/` controls synchronized with, but subordinate to, the substantive corpus.
