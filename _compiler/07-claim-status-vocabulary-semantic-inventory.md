# Claim-Status Vocabulary — Adjudicated Semantic Inventory

Status: corpus-wide adjudicated compiler artifact. The original claim-status control was checked against later physics status matrices, work plans, GR/QM ledgers, result pages, audit repairs, and current detailed derivations.

## Corpus-wide finding

The four live claim standings remain:

1. **Open**
2. **Conjectured**
3. **Registered**
4. **Registered and Sealed**

Later documents sometimes use expressions such as `Conjectured-strong`, `derived-with-empirical-state-input`, `defended posit`, `forced`, `checked`, or `argued`. Corpus-wide adjudication shows that these expressions do not establish additional claim-status grades. They describe warrant strength, dependency conditions, empirical inputs, or route. They must be represented in separate metadata rather than silently expanding the standing vocabulary.

---

## CSV-001 — Modal standing must be preserved exactly

A compiler, summary, or later document must preserve the live standing of each claim and may not promote it by compression, terminology, or rhetorical confidence.

**Disposition:** retained.

## CSV-002 — The live standing vocabulary has four members

The authoritative standings are Open, Conjectured, Registered, and Registered and Sealed.

**Disposition:** retained. Later compound expressions are normalized into one of these four standings plus separate warrant, condition, confidence, or input metadata.

## CSV-003 — Open

Open marks an explicitly unclosed claim, dependency, or joint that remains on the work frontier. It may be discussed or used as a named dependency, but it may not be spent downstream as though closed.

**Disposition:** retained and clarified.

## CSV-004 — Conjectured

Conjectured marks a live proposal not yet registered by the framework. Qualifiers such as “strong” may describe evidential or argumentative strength but do not create a fifth standing.

**Disposition:** retained and clarified.

## CSV-005 — Registered

Registered means that the framework reaches the claim in essence or under explicitly stated conditions, while full closure, uniqueness, bidirectional identity, or sealing remains incomplete. Conditions and unresolved debts must travel with the claim.

**Disposition:** retained and strengthened against condition loss.

## CSV-006 — Registered and Sealed

Registered and Sealed means that the framework has closed the relevant content identity or equivalent relation sufficiently that the recognized name carries no unearned surplus within the stated scope. Sealing is scope-sensitive; it does not automatically seal every theorem, extension, numerical value, or conventional association attached to the name elsewhere.

**Disposition:** retained with scope clarification.

## CSV-007 — Standing and warrant route are distinct axes

Retorsion-secured, forced, defended posit, selection, recognition, construction, checked, argued, and derived-with-input describe how or under what conditions a claim is supported. They do not replace its standing.

**Disposition:** retained. This distinction is required to normalize later corpus usage.

## CSV-008 — Translation and summary may not upgrade standing

A summary may clarify or, where evidence requires, downgrade a claim. It may never strengthen the standing merely because it omits conditions, open joints, or route limitations.

**Disposition:** retained.

---

## Normalization rules forced by later corpus usage

- `Conjectured-strong` → **Conjectured**, with `warrant-strength: strong`.
- `derived-with-empirical-state-input` → assign the standing justified by the derivation, while recording the empirical input and conditionality separately; the phrase itself is not a standing.
- `defended posit` → warrant profile, not standing.
- `forced` → warrant route, not standing.
- `current`, `control`, `mature`, and `confidence: high/medium` → document or confidence metadata, not claim standing.
- A page-level status never determines the standing of every sentence in the page.
- A sealed recognition is sealed only over the content actually identified; surplus associations remain excluded.

## Completed adjudication ledger

- CSV-001 through CSV-008: checked against the current status matrix, work plan, GR/QM ledgers, Lambda, dimensionality, gauge, probability, mass, and audit usage.
- Substantive contradiction found: later documents sometimes present compound route/confidence phrases in the syntactic position of statuses.
- Repair: preserve the four-standing vocabulary and split compound phrases into standing plus separate metadata.
- Deprecated status identities retained: none.