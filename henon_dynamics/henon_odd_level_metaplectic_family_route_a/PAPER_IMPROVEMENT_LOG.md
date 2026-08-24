# Paper improvement log

No external reviewer score or model-family independence is claimed.  The two
rounds below are internal evidence-anchored hostile reviews.

## Round 0

The theorem, exact family receipt, and Route-A boundary were present.  The
first build was three pages but exposed a 2.21pt overfull scope identifier.

## Round 1 — uniformity and certificate readability

- Stated explicitly that Fourier orthogonality needs a primitive root, not a
  prime modulus.
- Defined the matrix max norm used in the no-alias proposition.
- Replaced a prose-only window list by a compact exact certificate table.
- Moved the long scope identifier to display math, eliminating the overfull
  box.  The rebuilt three-page PDF had no layout or reference warning.

## Round 2 — quantifier and converse audit

- Added the faithful-Weyl-label argument for composite odd levels.
- Marked the window as a sufficient one-sided certificate, not the first
  modular period.
- Strengthened the nonclaim: no relative central phase or projective
  intertwiner is supplied across levels.
- Rechecked the even-level statement so it excludes only the frozen
  half-phase convention.

## Preserved PDFs

- `paper/main_round0_original.pdf`: baseline.
- `paper/main_round1.pdf`: after Round 1.
- `paper/main_round2.pdf`: after Round 2 and identical in content to final.

## Release integrity reconciliation

- Replaced the provisional evaluator record by the exact
  `route-a-evaluator` v0.1.0 output schema and limited A1 evidence to inherited
  classical torus periodic structure; C131 itself has no primitive census or
  prime-like target.
- Closed checker schema keys at the evidence top level, certified receipts,
  check map, and scope map.
- Corrected the mutation accounting from an overstatement of 26 repaired-hash
  cases to 29 repaired-hash cases plus one stale-hash case.  The added four
  cases target the newly closed schemas.
- Rebuilt `main_round2.pdf` and the final PDF from the reconciled text while
  preserving the historical Round 0 and Round 1 artifacts.
