# P189 Round-0 author self-QA

**Decision:** `PASS_INTERNAL / ROUND0_AUTHOR_FREEZE`  
**External state:** `OWNER_AMBER / HOLD_EXTERNAL`

## Mathematical attack before freeze

- Reimplemented the transition directly from matrix entries; no scouting
  module or stored transition table is imported.
- Exhausted all matrices for `n=1,2,3,4` and compared every entry of the first
  four literal iterates with a separately implemented height-vector formula.
- Searched for false stronger identities and found explicit `n=2`
  counterexamples to both `F^2=F` and `F^3=F`; the manuscript claims only
  `F^4=F^2`.
- Permuted rows with the same row-sum multiset to verify that time one and the
  exact depth predicate retain labelled order, while time two forgets it.
- Attacked every target, including column-hole targets, all-zero/all-one
  heights, empty fibres, repeated row sums, `n=1`, and post-height epochs.
- Verified both fibre mass identities independently and checked partition
  conjugation/self-conjugate counts beyond the complete matrix boxes.

The two fresh verifier processes are byte-identical to the canonical
transcript and report **5,336,613** assertions.

## Source and manuscript QA

- Anonymous `amsart`; no identifying author, affiliation, acknowledgements,
  PDF metadata, or self-citation.
- All four citation keys equal the four verified bibliography records.
- Standard Ferrers, conjugation, diagonal-hook, and line-sum results are
  explicitly zero credit.
- The bounded owner-search non-hit is not called novelty or clearance.
- All displayed symbols are defined before use; square/labelled/synchronous
  scope and the `n=1` boundary are explicit.
- PDF: four A4 pages, visually inspected page by page; no clipping, collision,
  unresolved reference/citation, bad box, form, JavaScript, or unembedded
  font.
- Two source-only cold builds reproduce the live and immutable Round-0 bytes.

## Lifecycle boundary

This is an author-side Round-0 handoff, not an independent review.  No Review
A/B, Round 1/2, final manifest, submission, circulation, or external novelty
claim has been created or authorized.
