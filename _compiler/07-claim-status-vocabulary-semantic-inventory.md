# Claim Status Vocabulary Semantic Inventory

Status: compiler working artifact. Source authority: original wiki only.

## Source

- `concepts/claim-status-vocabulary.md`
- Drive file ID: `1ly4Tkcer4TyBQDQk6nefnqvQueDjScsB`

## Preservation rule

This source is a control document. Only living semantic units are compiled. Deprecated or eliminated terminology is not assigned a semantic identity.

---

## CSV-001 — Modal status must be preserved exactly

**Kind:** control invariant

**Content:** Future agents must preserve the modal status assigned to a claim exactly.

**Source:** opening directive.

**Parents:** none internal to this source.

**Spent by:** every later compiler pass, migration decision, canonical rendering, and status summary.

**Standing:** current control rule.

---

## CSV-002 — The live physics-claim status vocabulary has four members

**Kind:** controlled vocabulary

**Content:** Live physics claims use exactly four statuses: Open, Conjectured, Registered, and Registered and Sealed.

**Source:** `Live claim statuses`.

**Parents:** CSV-001.

**Spent by:** physics ledgers, result-page summaries, and canonical status assignments.

**Standing:** current control rule.

---

## CSV-003 — Open marks an explicitly unclosed work frontier

**Kind:** status definition

**Content:** Open means the claim or joint is explicitly not closed and remains part of the work frontier.

**Parents:** CSV-002.

**Spent by:** frontier ledgers and prohibition on downstream expenditure as closed structure.

**Standing:** definition.

---

## CSV-004 — Conjectured marks a live proposal not registered by the framework

**Kind:** status definition

**Content:** Conjectured means plausible and live, but not yet registered by the framework.

**Parents:** CSV-002.

**Spent by:** candidate hypotheses, provisional routes, and downgrade decisions.

**Standing:** definition.

---

## CSV-005 — Registered marks essential or conditional framework reach without full sealing

**Kind:** status definition

**Content:** Registered means the framework reaches the item in essence or under stated conditions, while sealing or full closure remains incomplete.

**Parents:** CSV-002.

**Spent by:** conditional results and essential-form claims.

**Standing:** definition.

---

## CSV-006 — Registered and Sealed marks bidirectional content identity or equivalent closure

**Kind:** status definition

**Content:** Registered and Sealed means bidirectional content identity, or equivalent framework closure, such that the named item carries no surplus load beyond the registered structure.

**Parents:** CSV-002, sealed-recognition discipline from Architectonic Rigor.

**Spent by:** mature equivalence claims and terminology allowed to carry its full registered content.

**Standing:** definition.

---

## CSV-007 — Instrument vocabulary and live claim status are distinct axes

**Kind:** categorical distinction

**Content:** Retorsion-secured, forced, defended posit, selection, recognition, checked, and argued describe the instrument or evidence behind a claim. They do not replace the live claim status, which for the physics wiki must be one of the four statuses in CSV-002.

**Parents:** CSV-002; Architectonic Rigor.

**Spent by:** prevention of status inflation and the later crosswalk between warrant-route and claim-standing.

**Standing:** current control rule.

---

## CSV-008 — Status may never be upgraded in translation or summary

**Kind:** execution rule

**Content:** Never upgrade status. `Argued` may not be reported as `proved`; summaries and canonical rewrites must preserve or weaken the source standing, never strengthen it.

**Parents:** CSV-001, CSV-007.

**Spent by:** every compiler summary and canonical rewrite.

**Standing:** current control rule.

---

## Dependency and preservation effects

1. Live status and warrant-route must remain separate metadata fields in the compiler graph.
2. No deprecated or eliminated status receives a semantic unit in the living compiler graph.
3. No later document may use `forced`, `recognition`, `selection`, or similar route language as a substitute for one of the four live physics statuses.
4. Any canonical summary inherits the weakest live status of the claims it summarizes; prose compression cannot promote standing.
5. This source does not define any later expanded status vocabulary. Any expansion must be separately sourced and related to, not silently substituted for, this four-status control document.
