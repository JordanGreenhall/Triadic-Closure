# Physics Execution Wiki Schema

## Domain
This wiki compiles Jordan Hall's physics-stratum package and its contextual conversation ledger into an execution-oriented knowledge base for future agents.

The wiki is not a publication draft. It is an agent navigation layer: what is current, what is superseded, where claims stand, and what work is safe to perform next.

## Source Layers
- `raw/package/` — immutable package files from `Physics Large MD Package.zip`.
- `raw/context/full-conversation-ledger.md` — full conversation ledger contextualizing revisions, supersessions, decisions, and failures.
- `_meta/source-inventory.json` — hashes and line counts for all raw sources.
- `_meta/verify-output.txt` — output of the included `verify.py`; last verified: 2026-06-21, result: 9/9 PASS.

## Page Types
- `overview` — orientation maps, lineage, current package shape.
- `concept` — core framework concepts and canonical vocabulary.
- `result` — current result modules or stabilized derivations.
- `claim` — important claims with standing/status.
- `process` — agent execution rules, QA rules, build policy.

## Frontmatter
Every curated page should begin with:

```yaml
---
title: Page Title
type: overview | concept | result | claim | process
created: YYYY-MM-DD
updated: YYYY-MM-DD
status: current | historical | superseded | contested | open | control
confidence: high | medium | low
sources:
  - raw/package/example.md
  - raw/context/full-conversation-ledger.md
---
```

## Status Meanings
- `current` — safe for agents to treat as live unless contradicted by a more recent control page.
- `historical` — useful for provenance, not current authority.
- `superseded` — preserved in raw sources but should not be used as doctrine.
- `contested` — active disagreement or unresolved proof-status issue.
- `open` — explicitly not closed; safe only as work frontier.
- `control` — governs wiki/agent behavior.

## Agent Rules
1. Always read `index.md`, `overview/corpus-lineage.md`, `overview/supersession-map.md`, and `process/agent-execution-rules.md` before acting.
2. Do not revive claims from superseded files unless a current file explicitly reinstates them.
3. Treat the full conversation ledger as lineage/adjudication authority, not polished doctrine.
4. Any claim labeled computed must cite a real computation that could have failed. Print-statement theater is forbidden.
5. Preserve the distinction between:
   - vertical: synchronic office-composition / admissibility / J;
   - horizontal: diachronic accumulation of actuals / realizability / ρ;
   - layers/nesting: horizontal-standing-face, not canonical vertical.
6. Use live claim statuses for physics claims: Open, Conjectured, Registered, Registered and Sealed. `Locked actual` is deprecated/disfavored; translate it through [[locked-actual-decrement-map]].
7. When uncertain, downgrade status rather than upgrade it.

## Linking Rules
- Every curated page should include at least two wikilinks.
- Every live result should link to its source files and its relevant status/supersession page.
- Superseded pages must link to the current replacement.

## Quality Gate
Before handing wiki context to an execution agent:
- broken wikilinks: 0 preferred;
- raw source inventory exists;
- `verify.py` output checked;
- supersession map read;
- agent rules read;
- no obsolete claim promoted to current.
