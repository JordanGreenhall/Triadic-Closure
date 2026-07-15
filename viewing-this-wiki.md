---
title: Viewing This Repository
type: overview
created: 2026-06-21
updated: 2026-07-13
status: control
confidence: high
---

# Viewing This Repository

This is a Markdown corpus stored primarily in a flattened repository-root layout.

## GitHub

Begin with [README.md](README.md), then [index.md](index.md). The index uses ordinary repository-relative Markdown links and is the governing navigation surface.

Do not follow former folder-qualified paths such as `overview/...`, `results/...`, `process/...`, or `raw/package/...` unless that directory is visibly present in GitHub. Resolve uploaded corpus documents by root-level filename.

## Local clone

After cloning the repository, open the repository root in any Markdown editor or IDE. The current repository path depends on where the user cloned it; no machine-specific absolute path is canonical.

Recommended entry sequence:

1. `README.md`
2. `index.md`
3. `SCHEMA.md`
4. `corpus-lineage.md`
5. `supersession-map.md`
6. `locked-actual-decrement-map.md`
7. `physics-domain-mature-status.md`
8. `physics-domain-work-plan.md`
9. `agent-execution-rules.md` — corpus normalization execution contract

## Obsidian

The repository root may be opened as an Obsidian vault. Obsidian-style wikilinks inside corpus documents may then resolve by basename, but repository governance should still use the explicit links in `index.md`.

## VS Code or another editor

Open the repository root. Useful capabilities include:

- Markdown preview;
- repository-wide filename search;
- broken-link checking;
- exact-text search for stale prefixes such as `results/`, `overview/`, `process/`, `raw/package/`, and `raw/context/`.

## Static generation

Do not assume a historical `_meta/build_html_wiki.py` or `_site/` path exists merely because an older document mentions it. Run a static builder only after verifying that the script exists in the current repository.

## Manual use

Start at [index.md](index.md). For control and status work, read:

- [Corpus Lineage](corpus-lineage.md)
- [Supersession Map](supersession-map.md)
- [Locked Actual Decrement Map](locked-actual-decrement-map.md)
- [Physics Domain Mature Status](physics-domain-mature-status.md)
- [Physics Domain Work Plan](physics-domain-work-plan.md)
- [Corpus Normalization Execution Rules](agent-execution-rules.md)

## Rule

Never treat a document as current merely because it is polished or because it formerly lived in a folder called `results`. Route through the current index, lineage, supersession, and status controls first.
