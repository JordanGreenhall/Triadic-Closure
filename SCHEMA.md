# Triadic Closure Repository Schema

## Domain

This repository contains Jordan Hall's Triadic Closure corpus, including foundational architectonics, domain-entry method, physics and chemistry work, current controls, historical sources, execution ledgers, and compiler artifacts.

The repository is an execution-oriented knowledge base rather than a publication draft.

## Current repository topology

The corpus was uploaded in a **flattened root-level layout**. Most Markdown documents therefore live directly at repository root, regardless of their former Google Drive folder.

Current path rule:

```text
filename.md
```

Former paths such as the following are historical provenance unless the directory is visibly present in GitHub:

```text
results/filename.md
overview/filename.md
concepts/filename.md
process/filename.md
raw/package/filename.md
raw/context/filename.md
```

The `_compiler/` directory is an actual repository directory and contains compiler/adjudication work products.

## Document roles

Role is carried by content and frontmatter, not by folder location:

- `overview` or `control` — orientation, lineage, supersession, status, and execution controls;
- `concept` — framework vocabulary and structural concepts;
- `result` — current result modules and derivations;
- `claim` — focused claims with explicit standing;
- `process` — execution and QA rules;
- `historical` or `superseded` — provenance and displaced formulations;
- compiler artifact — semantic inventories and adjudication controls under `_compiler/`.

## Frontmatter

Existing frontmatter may contain historical `sources:` paths inherited from Google Drive. Those paths are provenance metadata, not necessarily live GitHub paths.

For new or repaired documents, use repository-relative root paths:

```yaml
---
title: Page Title
type: overview | concept | result | claim | process | control
status: current | historical | superseded | contested | open | control
confidence: high | medium | low
sources:
  - source-file.md
  - another-source-file.md
---
```

When retaining an obsolete source path for provenance, label it explicitly as historical rather than presenting it as a navigable repository path.

## Linking rules

1. Governing navigation files must use GitHub-resolvable Markdown links, for example:

   ```markdown
   [Mass as Self-Closure](mass-as-self-closure.md)
   ```

2. Obsidian-style wikilinks may remain in corpus prose, but they are not sufficient for repository navigation.
3. Resolve a stale folder-qualified reference by basename against repository root.
4. Do not invent a replacement filename. Verify the target exists before changing a link.
5. Generated or historical references may remain only when clearly identified as provenance.
6. `_compiler/` paths must retain their directory prefix because that directory actually exists.

## Claim-standing vocabulary

Use the current claim standings and keep them separate from warrant route:

- Open;
- Conjectured;
- Conjectured-strong;
- Registered-candidate;
- Registered;
- Registered and Sealed;
- Defended posit;
- Dissolved.

`Locked actual` is deprecated and must be translated through the current status discipline.

## Agent rules

1. Read [README.md](README.md), [index.md](index.md), this schema, [corpus-lineage.md](corpus-lineage.md), [supersession-map.md](supersession-map.md), and [agent-execution-rules.md](agent-execution-rules.md) before substantive work.
2. Do not average conflicting corpus formulations.
3. Detailed successful derivations govern compressed summaries unless later detailed work explicitly supersedes them.
4. Treat source authority as claim-specific, not document-wide or folder-based.
5. Do not upgrade a claim beyond its dependency route.
6. Distinguish vertical office-composition from horizontal accumulation.
7. Treat the full conversation ledger and historical location metadata as adjudication/provenance sources, not automatically polished doctrine.
8. When uncertain, downgrade standing and expose the open joint.

## Repository quality gate

Before a navigation or refactor pass is complete:

- every explicit Markdown link in `README.md`, `index.md`, and governing control files resolves to a current repository path;
- stale folder-qualified paths are removed from live navigation;
- historical paths are labeled as historical;
- no basename is silently mapped to the wrong document;
- compiler artifacts remain distinguished from substantive corpus files;
- no obsolete claim is promoted merely because its link was repaired.
