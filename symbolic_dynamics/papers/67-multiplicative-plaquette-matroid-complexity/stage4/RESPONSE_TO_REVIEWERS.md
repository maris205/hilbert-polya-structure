# Response to Reviewers — Round 1

revision_round: 1

status: complete

word_count_delta: 59

new_references_added: 0

summary:

- resolved: 2
- limitations: 1
- deliberate_limitations: 1
- unresolvable: 1
- disagreed: 0

summary_of_changes: The revision defines total correlation before its first
theorem-level use and adds an exact deterministic control over the nonprime
extension field `F_4`. The specialist ownership boundary and external-release
HOLD remain in place, and the optional adjacent-domain application was not
added.

new_content_highlight:

- Introduction, immediately before the main theorem
- Comparison, scope, and controls — Deterministic controls

The canonical ARS word count was computed after stripping every
`<!--...-->` marker and applying `len(body.split())`: the anchored draft has
3849 words and the revised draft has 3908 words, giving `3908 - 3849 = +59`.

## REV-P67-EIC-W1

reviewer_id: EIC

item_id: REV-P67-EIC-W1

roadmap_item_id: REV-P67-EIC-W1

reviewer_comment: Define the total-correlation notation before it appears in
the main theorem.

status: RESOLVED

change_block_ids: [`B0005`]

location: Introduction, paragraph immediately before the finite-shape main
theorem.

change_location: Introduction, block `B0005`.

summary: The revision now defines `TC_mu(Z_F)` as the entropy deficit for the
normalized Haar random vector before the theorem uses the notation.

author_response: We agree that the notation order impeded first-pass reading.
The revised introduction identifies normalized Haar measure, defines
`Z_F=(x_n)_(n in F)`, and displays the exact total-correlation formula before
the main theorem. The formula agrees with the detailed definition retained in
the finite-projection section.

verification: The deterministic apply report records a `replace_block`
operation on `B0005` authorized solely by `REV-P67-EIC-W1`. Direct inspection
of revised block `B0005` confirms that the definition precedes the theorem.

## REV-P67-R1-W1

reviewer_id: R1

item_id: REV-P67-R1-W1

roadmap_item_id: REV-P67-R1-W1

reviewer_comment: Exercise or explicitly delimit the extension-field branch
of the deterministic controls.

status: RESOLVED

change_block_ids: [`B0092`]

location: Comparison, scope, and controls — Deterministic controls; companion
control program and control ledger.

change_location: Revised Markdown block `B0092`; TeX section
`sections/6_scope.tex`; control files `code/verify_plaquette_matroid.py`,
`code/verify_plaquette_matroid.out`, and `CONTROL_RESULTS.md`.

summary: An exact branch over `F_4 = F_2[u]/(u^2+u+1)` now checks prefix
ranks, every subset of `[1,12]`, exponent rectangles, and Haar forest/cycle
counts.

author_response: We added polynomial-basis field addition, multiplication,
inversion, and Gaussian elimination over the nonprime extension field. The
replayed control covers 80 prefix ranks, 4096 finite projections, 36
rectangles, and three exact Haar enumerations. The manuscript and control
ledger state this coverage while preserving the limitation that finite
regression evidence does not replace the proofs.

verification: The deterministic apply report records a `replace_block`
operation on `B0092` authorized solely by `REV-P67-R1-W1`. The final control
run exits 0 with `ALL CHECKS PASS`; `code/verify_plaquette_matroid.out`,
`stage4/CONTROL_RUN.out`, and `stage4/FINAL_CONTROL_RUN.out` report the same
F4 case counts.

## REV-P67-R2-W1

reviewer_id: R2

item_id: REV-P67-R2-W1

roadmap_item_id: REV-P67-R2-W1

reviewer_comment: Resolve the open specialist owner boundary before external
contribution framing.

status: UNRESOLVABLE

change_block_ids: []

location: No revision operation; existing ownership boundary and release HOLD
remain in blocks `B0089` and `B0098`.

change_location: No manuscript change. Existing Comparison/scope and
Conclusion language retained.

summary: Specialist exact-neighbor clearance was not available within the
revision round, so the manuscript continues to withhold external-release and
priority clearance.

author_response: We accept the importance of the requested ownership audit,
but the missing evidence is an external specialist authorization, not an
internal prose or computational task. Internal restatement, another bounded
search, or author self-certification cannot substitute for independent
specialist clearance. We therefore retain the explicit HOLD and make no
priority claim.

verification: The author adjudication records `REV-P67-R2-W1` as
`wont_address`; the apply report contains no operation citing it. Blocks
`B0089` and `B0098` remain byte-identical to the anchored draft, preserving
the specialist-review contingency.

decline_justification: The requested evidence requires external specialist
review across multiplicative symbolic dynamics, algebraic actions,
finite-field coding, and matroidal probability. That external authorization
cannot be manufactured or replaced by an internal revision, so retaining the
HOLD is the only evidence-bounded disposition.

## REV-P67-R3-W1

reviewer_id: R3

item_id: REV-P67-R3-W1

roadmap_item_id: REV-P67-R3-W1

reviewer_comment: Optionally add one bounded worked translation of the
graphic-matroid result into an adjacent application language.

status: DELIBERATE_LIMITATION

change_block_ids: []

location: No revision operation; the Matroid and information-theoretic
ingredients discussion remains at block `B0086`.

change_location: No manuscript change; optional application omitted by scope
decision.

summary: The revision deliberately does not add a linear-code,
completion-pattern, or entropic-matroid application because it would introduce
a new interpretive package beyond the adjudicated theorem-and-control repair.

author_response: We appreciate the potential expository value, but the item
was explicitly optional and would broaden the paper beyond its present claim
boundary. The existing comparison already separates the transferable
incidence-matroid mechanism from the multiplicative root decomposition. We
therefore preserve the narrow scope instead of adding an application that
would require its own validation and ownership audit.

verification: The author adjudication records `REV-P67-R3-W1` as
`wont_address`; the apply report contains no operation citing it and no fresh
application block. Block `B0086` remains unchanged.

decline_justification: The proposed application is optional and would enlarge
the interpretive and literature-audit surface without being needed to verify
the central theorem. Preserving the paper's bounded scope is a deliberate,
documented limitation.

## Round receipt

The patch-format 1.1 document was mechanically applied once. The apply report
has authorization status `pass`, no structural flags, two touched blocks, and
96 of 98 original blocks preserved byte-identically. No references were
added. The control and TeX compilation receipts are included in Stage 4.
