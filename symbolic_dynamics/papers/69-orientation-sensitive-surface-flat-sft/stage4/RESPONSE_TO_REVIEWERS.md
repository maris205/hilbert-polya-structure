# Response to Reviewers — Round 1

- schema: Schema 8 — Response to Reviewers
- status: complete
- revision_round: 1
- word_count_delta: +51
- new_references_added: 0
- summary: `{resolved: 2, limitations: 1, deliberate_limitations: 1, unresolvable: 1, disagreed: 0}`
- new_content_highlight: Introduction proof roadmap; Exact finite regression controls

The canonical whitespace count, after removing every `<!--...-->` marker, is
3,866 words for `stage3/ANCHORED_REVIEW_DRAFT.md` and 3,917 words for
`stage4/REVISED_DRAFT.md`. The revision therefore adds 51 words. The response
below covers all four source-ordered roadmap items.

## REV-P69-EIC-W1

- reviewer_id: EIC
- item_id: REV-P69-EIC-W1
- roadmap_item_id: REV-P69-EIC-W1
- status: RESOLVED
- change_block_ids: `[B0010]`
- location: Introduction, proof-roadmap paragraph
- change_location: Introduction, proof-roadmap paragraph
- summary: Corrected the stated proof structure from two layers to three successive stages.
- verification: Apply-report operation 0 replaces B0010 and introduces no fresh block; the revised block names the rooted-gauge reduction, cover-topology/surface-formula derivation, and inverse moment reconstruction as three successive stages. The TeX mirror is in `sections/1_introduction.tex`, and the final compile receipt exits successfully.

**Reviewer comment.** Correct the proof roadmap's stage count so that it
matches the three operations described in the paragraph.

**Author response.** We agree. The opening sentence now says “three successive
stages,” matching the rooted-gauge count, the cover/topology and surface-formula
derivation, and the inverse moment reconstruction already explained in the
same paragraph.

## REV-P69-R1-W1

- reviewer_id: R1-methodology
- item_id: REV-P69-R1-W1
- roadmap_item_id: REV-P69-R1-W1
- status: RESOLVED
- change_block_ids: `[B0097]`
- location: Scope, ownership, and finite controls — Exact finite regression controls
- change_location: Scope, ownership, and finite controls — Exact finite regression controls
- summary: Added an exact two-degree mixed-indicator Vandermonde fixture and recovered every positive, negative, and zero coefficient.
- verification: Apply-report operation 1 replaces B0097 and introduces no fresh block. `FINAL_CONTROL_RUN.out` records bases 1 and 1/4, P/Q/R moment pairs, recovery of the two ledgers `(2,1,1)` and `(1,2,1)`, and terminates with `ALL CHECKS PASS`. The matching TeX inventory and executable implementation are identified in `TEX_TRANSPORT_RECEIPT.md`.

**Reviewer comment.** Exercise the multi-degree mixed-indicator inversion
ledger end to end rather than testing the zero-indicator and parity branches
only in separate examples.

**Author response.** We added an exact synthetic two-degree fixture. Its
indicator ledgers are `(2,1,1)` at degree one and `(1,2,1)` at degree two.
The control constructs the exact P, Q, and R moment pairs, solves all three
known-base Vandermonde systems over the rationals, and recovers every ledger
coefficient. The manuscript explicitly identifies this as algebraic branch
coverage, not as the character ledger of an asserted finite group.

## REV-P69-R2-W1

- reviewer_id: R2-domain
- item_id: REV-P69-R2-W1
- roadmap_item_id: REV-P69-R2-W1
- status: UNRESOLVABLE
- change_block_ids: `[]`
- location: No Round 1 manuscript change; the existing Release posture remains unchanged at B0101
- change_location: No Round 1 manuscript change; the existing Release posture remains unchanged at B0101
- summary: Specialist collision clearance was not claimed; the non-priority language and external-release HOLD remain in force.
- verification: The apply report contains no operation citing REV-P69-R2-W1 and no operation on B0101. The revised manuscript still states that specialist review remains mandatory before external release.
- decline_justification: The requested forward-and-backward specialist review is an external expert-clearance event. Internal editing or deterministic controls cannot substitute for that independent authorization. The evidence therefore supports preserving the explicit HOLD, not declaring the item completed.

**Reviewer comment.** Resolve the specialist collision-review boundary before
using external contribution framing.

**Author response.** We agree that this gate matters, but it cannot be closed
within an internal revision round without the requested external specialist
review. We have not represented specialist clearance as completed. The bounded
search statement, non-priority wording, and external-release HOLD remain
unchanged.

## REV-P69-R3-W1

- reviewer_id: R3-perspective
- item_id: REV-P69-R3-W1
- roadmap_item_id: REV-P69-R3-W1
- status: DELIBERATE_LIMITATION
- change_block_ids: `[]`
- location: No Round 1 manuscript change; optional insertion after B0104 was not made
- change_location: No Round 1 manuscript change; optional insertion after B0104 was not made
- summary: Deferred the optional transfer checklist to keep this accepted-paper revision bounded to the proof-roadmap correction and deterministic control.
- verification: The apply report contains no operation citing REV-P69-R3-W1 and no insertion after B0104. No theorem or core claim was extended to another surface or cover tower.
- decline_justification: The roadmap classifies this item as optional (`consider`). Adding a reusable transfer program would broaden the discussion beyond the two decision-bearing corrections authorized for this round. Deferral preserves the theorem's current scope and avoids implying an unproved extension.

**Reviewer comment.** Optionally extract a bounded checklist for assessing
other cover towers.

**Author response.** We considered the suggestion and deliberately deferred
it. The present round remains limited to the corrected proof roadmap and the
multi-degree inversion control; it makes no transfer theorem or design claim
for other cover families.

## Summary of Changes

Two authorized items are resolved, one optional expansion is recorded as a
deliberate limitation, and one external specialist-clearance item is recorded
as unresolvable within this internal round. No references were added, no
declined item supplied write authority, and the external-release HOLD remains
unchanged.
