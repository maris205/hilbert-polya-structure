# P158 author-side self-QA

**Date:** 2026-09-02 UTC.  **Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Contract audit

- The literal update is repeated intersection with fresh independent fair
  vertex cuts, starting from labelled `K_n`.
- `R=2^(t-1)` and every `A_R` boundary convention are explicit.
- The absorption CDF, first-hit law, tail, and mean series match the freeze.
- The fibre formula is every-target and retains zero fibres.
- The image criterion includes `z=0 or r<R` rather than only `r<=R`.
- The `n=5,t=2` two-edges-plus-isolate nonimage is printed beside the theorem.
- The image EGF contains a separate isolate-free `r=R` term.

## Proof-interface attacks

1. **Can two target components share a word pair?** No.  Complement-side
   cross edges would connect them.
2. **Can an isolate use a consumed pair?** No.  Either word is complementary
   to the nonempty opposite component side.
3. **Does component orientation overcount an equal-size bipartition?** No.
   The two orientations assign distinct history words to fixed labelled sides.
4. **Does the converse create unintended isolate edges?** No.  `A_(R-r)(z)`
   enforces one-sided occupancy on every unused pair.
5. **Is the mean formula off by one?** No.  `T` is positive and
   `E[T]=1+sum_(t>=1)P(T>t)`.
6. **Does the EGF allow isolates at top resource?** No.  The `B(x)^R/R!`
   term lacks the factor `e^x`.

## Source and artifact audit

All three bibliography entries were checked through DOI/Crossref and DBLP or
the primary arXiv record.  They are cited and explicitly subtracted.  The
manuscript contains no novelty, priority, first, or ownership-completeness
claim.  The verifier uses exact standard-library arithmetic, and its fresh
stdout must match `verification_output.txt` byte for byte.

This is author-side QA only.  It is not a hostile review and does not
authorize external release.
