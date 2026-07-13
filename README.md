# Triadic Closure

This repository contains the working Triadic Closure corpus in a **flattened root-level layout**. The Markdown files were uploaded from the prior Google Drive wiki without preserving its folder hierarchy. Paths inherited from the Drive layout—such as `results/`, `overview/`, `process/`, `concepts/`, `raw/package/`, and `raw/context/`—must therefore not be treated as current repository paths.

## Repository layout

The repository root contains:

- `index.md` — the primary navigational index;
- `SCHEMA.md` — repository conventions and agent rules;
- `README.md` — this repository-level orientation;
- current result, control, concept, process, frontier, historical, and provenance Markdown files, all at root unless an actual subdirectory is visible in GitHub;
- `_compiler/` — compiler and semantic-adjudication working files. These are control artifacts, not substitutes for the underlying corpus.

The authoritative path for a root document is therefore simply:

```text
filename.md
```

not:

```text
results/filename.md
overview/filename.md
process/filename.md
raw/package/filename.md
```

## Navigation and linking

Use ordinary repository-relative Markdown links:

```markdown
[Mass as Self-Closure](mass-as-self-closure.md)
```

Obsidian-style wikilinks such as `[[mass-as-self-closure]]` may remain inside historical corpus text, but governing navigation files should also provide explicit GitHub-resolvable links.

When a document cites another corpus file by an obsolete Drive path, resolve it by basename against the repository root. A stale path does not establish that the target is absent; it records the file's former location.

## Corpus authority

Authority is claim-specific rather than folder-specific or document-wide. For any claim, prefer:

1. the most advanced complete detailed derivation;
2. later detailed repairs or extensions;
3. explicit adjudications and current rulings;
4. downstream work that necessarily spends and sharpens the claim;
5. current control pages;
6. summaries and orientation prose.

A newer summary may not override a stronger detailed derivation merely by being newer or shorter.

## Claim standing

The live claim standings are:

- **Open** — an explicit work frontier;
- **Conjectured** — a serious proposal not yet registered;
- **Conjectured-strong** — substantial structural support, still short of registration;
- **Registered-candidate** — derived on registered parents but awaiting promotion after review;
- **Registered** — secured by the stated dependency route;
- **Registered and Sealed** — registered with the identity closed in both directions;
- **Defended posit** — maximally warranted beneath the totalization ceiling, while open to a genuine irreducible counterexample;
- **Dissolved** — removed because the question or gate arose from an imported ontology or category error.

`Locked actual` is deprecated and must be translated through the current status discipline.

## Governing editorial rules

- Never upgrade a claim beyond its dependency route.
- Distinguish structural derivation from empirical fit, imported identification, and recognition after the fact.
- Preserve the distinction between vertical office-composition and horizontal accumulation.
- Treat historical source-location metadata as provenance, not as current repository topology.
- Do not infer authority from a former folder name.
- When a path is stale, repair the path without silently changing the semantic claim.

## Current maintenance priority

The immediate repository-maintenance task is path normalization after the flattened upload:

1. keep `README.md`, `index.md`, and `SCHEMA.md` aligned with the actual tree;
2. replace stale folder-qualified navigation links with root-relative links;
3. preserve historical source paths only when explicitly labeled as historical provenance;
4. verify every referenced basename exists in the repository before treating a link repair as complete;
5. keep `_compiler/` controls synchronized with the substantive corpus rather than allowing them to replace it.
