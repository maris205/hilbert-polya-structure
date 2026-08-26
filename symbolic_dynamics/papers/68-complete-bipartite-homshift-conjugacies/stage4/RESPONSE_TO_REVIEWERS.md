# Response to Reviewers — Round 1

revision_round: 1

status: complete

word_count_delta: 151

new_references_added: 0

summary:

- resolved: 3
- limitations: 0
- deliberate_limitations: 0
- unresolvable: 1
- disagreed: 0

summary_of_changes: The revision makes the hierarchy among the four result
contracts explicit, adds singleton-part and minimal-target deterministic
controls, and supplies a statistical-mechanics dictionary for the phase and
pressure construction. The specialist exact-neighbor ownership HOLD remains
in place.

new_content_highlight:

- Introduction, result-contract roadmap
- One-site pressure and equilibrium states, opening dictionary
- Source boundary and limitations, deterministic-control description

The canonical ARS word count was computed after stripping every
`<!--...-->` marker and applying `len(body.split())`: the anchored draft has
2645 words and the revised draft has 2796 words, giving `2796 - 2645 = +151`.

## REV-P68-EIC-W1

reviewer_id: EIC

item_id: REV-P68-EIC-W1

roadmap_item_id: REV-P68-EIC-W1

reviewer_comment: Make the dependency hierarchy among the four result
contracts explicit.

status: RESOLVED

change_block_ids: [`B0005`]

location: Introduction, paragraph immediately before the four-contract list.

change_location: Introduction, block `B0005`.

summary: The product conjugacy classification and explicit two-sided dimer
code are now identified as central, the phase lemma as their mechanism, and
the remaining results as complementary packages.

author_response: We agree that the original phrase “four linked contracts”
did not convey priority or dependency. The revised introduction states the
central theorem, identifies the intrinsic-phase lemma as its mechanism, and
places exact counts, finite dependence, thermodynamics, and periodic data in
their supporting roles.

verification: The deterministic apply report records a `replace_block`
operation on `B0005` authorized solely by `REV-P68-EIC-W1`. Revised block
`B0005` contains the complete hierarchy before the enumerated roadmap.

## REV-P68-R1-W1

reviewer_id: R1

item_id: REV-P68-R1-W1

roadmap_item_id: REV-P68-R1-W1

reviewer_comment: Add singleton-part boundary cases to the deterministic
controls.

status: RESOLVED

change_block_ids: [`B0057`]

location: Source boundary and limitations — deterministic controls; companion
control program and control ledger.

change_location: Revised Markdown block `B0057`; TeX section
`sections/7_scope.tex`; control files `code/verify_complete_bipartite.py`,
`code/verify_complete_bipartite.out`, and `CONTROL_RESULTS.md`.

summary: The control now covers all 72 points of the `2 x 2`-torus dimer
bijection from `(1,6)` to `(2,3)`, both `(1,1)` torus points, and finite-shape
counts at the singleton boundary.

author_response: We generalized the dimer encoder and inverse from one fixed
factorization to arbitrary equal products. The replay now retains the existing
`(2,6)` to `(3,4)` case and adds the requested `(1,6)` to `(2,3)` and minimal
`(1,1)` cases. The finite-shape ledger was expanded to four parameter pairs.

verification: The deterministic apply report records a `replace_block`
operation on `B0057` authorized solely by `REV-P68-R1-W1`. The final control
run exits 0 with `ALL CHECKS PASS`, reports 72 singleton-boundary torus points
and two minimal torus points, and is frozen in `stage4/FINAL_CONTROL_RUN.out`.

## REV-P68-R2-W1

reviewer_id: R2

item_id: REV-P68-R2-W1

roadmap_item_id: REV-P68-R2-W1

reviewer_comment: Resolve the pending exact-neighbour hom-shift ownership
boundary before external contribution framing.

status: UNRESOLVABLE

change_block_ids: []

location: No revision operation; the existing specialist-audit limitation and
external-release HOLD remain in block `B0056`.

change_location: No manuscript change. Existing Source boundary and
limitations language retained.

summary: Exact-neighbor specialist clearance was unavailable within the
revision round; no priority conclusion or external-release clearance is
asserted.

author_response: We accept that an exact-neighbor audit is required before
external contribution framing. However, the missing evidence is external
specialist authorization across hom-shift conjugacy, checkerboard recoding,
intrinsic matching terminology, and finitely dependent processes. Internal
prose, control runs, or author self-certification cannot replace that external
review. The HOLD therefore remains explicit.

verification: The author adjudication records `REV-P68-R2-W1` as
`wont_address`; the apply report contains no operation citing it. Block
`B0056` remains byte-identical to the anchored draft and continues to state
that bounded search is not specialist clearance.

decline_justification: The requested ownership determination requires an
independent specialist audit that was not available in this round. Because
external authorization cannot be internally substituted, the evidence-safe
response is to preserve the no-priority and release-HOLD language.

## REV-P68-R3-W1

reviewer_id: R3

item_id: REV-P68-R3-W1

roadmap_item_id: REV-P68-R3-W1

reviewer_comment: Add an explicit statistical-mechanics dictionary for
checkerboard sectors and one-site pressure.

status: RESOLVED

change_block_ids: [`B0061`]

location: One-site pressure and equilibrium states, new paragraph following
the one-site activity definitions.

change_location: Fresh revised Markdown block `B0061`, inserted after anchor
block `B0041`; TeX section `sections/5_pressure.tex`.

summary: The new dictionary identifies the hard-constraint spin system,
checkerboard sector variable, single-site activities, equal-sector mixture,
and the absence of residual conditional interactions for complete bipartite
targets.

author_response: We added the requested cross-disciplinary bridge before the
pressure theorem. It also states the boundary of the dictionary: for a
non-complete bipartite target, conditioning on phase generally leaves
constraints between neighboring dimers, so the conditional model is not an
independent-spin system.

verification: The apply report records an `insert_after` operation anchored
at `B0041` and assigns the inserted paragraph the actual fresh block ID
`B0061`. Direct inspection of `B0061` confirms all five dictionary components
and the non-complete-target failure condition.

## Round receipt

The patch-format 1.1 document was mechanically applied once. The apply report
has authorization status `pass`, no structural flags, fresh block `B0061`,
and 58 of 60 original blocks preserved byte-identically. No references were
added. The control and TeX compilation receipts are included in Stage 4.
