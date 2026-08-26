# Response to Reviewers — Round 1

- schema: Schema 8 — Response to Reviewers
- status: complete
- revision_round: 1
- word_count_delta: +372
- new_references_added: 0
- summary: `{resolved: 3, limitations: 0, deliberate_limitations: 0, unresolvable: 1, disagreed: 0}`
- new_content_highlight: Introduction contribution framing; Coefficient phase diagram and finite controls; Ownership and scope theorem-component comparison

The canonical whitespace count, after removing every `<!--...-->` marker, is
2,497 words for `stage3/ANCHORED_REVIEW_DRAFT.md` and 2,869 words for
`stage4/REVISED_DRAFT.md`. The revision therefore adds 372 words. The response
below covers all four source-ordered roadmap items.

## REV-P70-EIC-W1

- reviewer_id: EIC
- item_id: REV-P70-EIC-W1
- roadmap_item_id: REV-P70-EIC-W1
- status: RESOLVED
- change_block_ids: `[B0007, B0008, B0056, B0074, B0075]`
- location: Introduction contribution list; Scope, limitations, and declarations — Ownership and scope
- change_location: Introduction contribution list; Scope, limitations, and declarations — Ownership and scope
- summary: Added a theorem-component owner comparison using only the verified local ledger and bounded the contribution language without claiming priority clearance.
- verification: Apply-report operations 0, 1, and 4 replace B0007, B0008, and B0056; operation 4 creates B0074 and B0075 for the comparison matrix and bounded residual statement. The matrix covers the weighted formula, character term, determinant, corank-one lemma, and regular-multiplicity jump, with coefficient-field/operator/output differences. The final text explicitly keeps specialist and priority clearance unresolved.

**Reviewer comment.** Establish the theorem-level owner boundary for the
weighted cross-characteristic nullity formula with a component-by-component
comparison against the closest verified sources.

**Author response.** We added the requested five-row matrix using only sources
already verified in the local source ledger and bibliography. Each row names
the closest owned component and states the P70 difference in coefficient field,
operator, and output invariant. The introduction now labels the contributions
as bounded and identifies the computational audit as regression evidence. The
matrix is not a priority finding, and specialist exact-neighbour clearance and
external-release HOLD remain explicit.

## REV-P70-R1-W1

- reviewer_id: R1-methodology
- item_id: REV-P70-R1-W1
- roadmap_item_id: REV-P70-R1-W1
- status: RESOLVED
- change_block_ids: `[B0073]`
- location: Coefficient phase diagram and finite controls, inserted after anchor B0053
- change_location: Coefficient phase diagram and finite controls, inserted after anchor B0053
- summary: Added an exact non-split F4/F2 character enumeration and matched its two solutions to the ground-field gcd degree.
- verification: Apply-report operation 3 inserts fresh block B0073 after B0053. `FINAL_CONTROL_RUN.out` lists `mu_3=[1,a,1+a]`, the pairs `(a,1+a)` and `(1+a,a)`, `gcd_degree=2 PASS`, and terminates with `ALL WEIGHTED HEISENBERG CONTROLS PASS`. The code and TeX mirror locations are recorded in `TEX_TRANSPORT_RECEIPT.md`.

**Reviewer comment.** Add an independent non-split character-enumeration
control and compare the enumerated extension-field solutions with the
ground-field gcd degree.

**Author response.** We added the exact case `(ell,p)=(3,2)`. The nontrivial
cube roots lie in `F_4`; enumerating every pair in `mu_3 × mu_3` finds exactly
`(a,1+a)` and `(1+a,a)` as solutions of `1+u+v=0`. Their count two equals the
degree of the displayed gcd over `F_2`.

## REV-P70-R2-W1

- reviewer_id: R2-domain
- item_id: REV-P70-R2-W1
- roadmap_item_id: REV-P70-R2-W1
- status: UNRESOLVABLE
- change_block_ids: `[]`
- location: No change authorized by this item; B0056 was changed only for REV-P70-EIC-W1 under collateral authorization COLLATERAL-AUTH-P70-EIC-over-R2-B0056
- change_location: No change authorized by this item; B0056 was changed only for REV-P70-EIC-W1 under collateral authorization COLLATERAL-AUTH-P70-EIC-over-R2-B0056
- summary: External specialist exact-neighbour clearance remains unresolved; the EIC comparison matrix preserves the non-priority boundary and release HOLD.
- verification: No apply-report operation cites REV-P70-R2-W1. Operation 4 cites only REV-P70-EIC-W1 and records `COLLATERAL-AUTH-P70-EIC-over-R2-B0056`; B0075 explicitly states that specialist clearance remains unresolved and external release remains on hold.
- decline_justification: The requested specialist review is an independent external expert-clearance event. Internal source comparison, manuscript editing, or deterministic controls cannot replace that authorization. The collateral authorization permits only the EIC-required B0056 edit while preserving this declined item's unresolved substance.

**Reviewer comment.** Complete specialist exact-neighbour review while
preserving bounded ownership language.

**Author response.** We have not claimed that this external gate was completed.
The EIC-required comparison matrix overlaps B0056 only under
`COLLATERAL-AUTH-P70-EIC-over-R2-B0056`, cites no authority from the declined
domain item, and expressly retains the unresolved specialist status,
non-priority wording, and external-release HOLD.

## REV-P70-R3-W1

- reviewer_id: R3-perspective
- item_id: REV-P70-R3-W1
- roadmap_item_id: REV-P70-R3-W1
- status: RESOLVED
- change_block_ids: `[B0072]`
- location: Coefficient phase diagram and finite controls, inserted after anchor B0047
- change_location: Coefficient phase diagram and finite controls, inserted after anchor B0047
- summary: Added a bounded coding/spectral transfer box containing only quantities implied by the proved kernel formula and an explicit unknowns list.
- verification: Apply-report operation 2 inserts fresh block B0072 after B0047. The block states code length `ell^3`, code dimension equal to the proved nullity, the rate-like quotient, and zero-eigenvalue geometric multiplicity; it explicitly excludes minimum distance, weight enumerator, decoding performance, the nonzero spectrum, algebraic multiplicities, and spectral gap.

**Reviewer comment.** Operationalize the coding and spectral bridge without
adding new theorem claims.

**Author response.** We added a compact transfer box. Quotient size `ell^3`
is identified as code length, the proved nullity as code dimension, their ratio
as a rate-like normalized quantity, and nullity as the geometric multiplicity
of the zero eigenvalue. The box explicitly lists the coding and spectral
quantities not determined by the theorem.

## Summary of Changes

Three authorized items are resolved and the external specialist-clearance item
is recorded as unresolvable within this internal round. No references were
added. The B0056 overlap is limited by the exact collateral authorization, and
neither priority nor specialist clearance is claimed.
