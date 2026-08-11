# HCS-C29 Phase-2 checkpoint

## Decision

**Phase 2: PASS, WITH A SCOPED ROUTE-A STOP.**

The algebraic reopening proposed in Phase 1 is exact and reproducible.  The
new symmetric non-backtracking Rauzy path groupoid has primitive
identity-holonomy cycles, and its dimension-normalized finite-Weil determinant
has a nonconstant locally uniform limit germ.  This result survives an
independent reconstruction and adversarial mutation testing.

The same investigation also closes the apparent natural-extension shortcut:
the genuine two-sided natural extension retains the positive chronological
cocycle products, so its regular-group periodic-product determinant germ
remains exactly one.

## Certified advances

1. **C25 identity-holonomy systole within the checked window.**  Exact
   enumeration through length nine gives

   ```text
   n:    1  2  3  4  5  6  7  8   9
   N_n:  0  0  0  0  0 24  0 32 144
   ```

   The two explicit length-six primitive cycles prove `N_6 >= 24`; the
   exhaustive length-six enumeration proves equality.  Neither statement uses
   extrapolation beyond the declared window.

2. **C26 return-level group relation.**  Programmatic expansion of the exact
   rank-one braid `K Y K = Y K Y`, followed by substitution into the frozen
   `A,B,C` return matrices, gives a primitive cyclically reduced length-24
   identity word.  It proves `N_24 >= 48`; no complete length-24 census is
   claimed.

3. **Nonconstant normalized determinant.**  For each fixed path length, the
   C28 normalized finite-Weil character tends to the identity-holonomy
   indicator.  The finite Hashimoto degree supplies a uniform power-series
   majorant.  Thus

   ```text
   exp[p^(-2) Log_0 det(I-u B_p)]
       -> exp[-sum_(n>=1) N_n u^n/n]
   ```

   locally uniformly on `|u|<1/3` for C25 and `|u|<1/5` for C26.  The common
   certified disc is `|u|<1/5`.

4. **Repetition firewall.**  `C1^2` enters the all-cycle determinant moment but
   not the primitive census.  The C26 element `Delta` has exact order four,
   and the correct fourth-repetition atom is `Theta_p(Delta^4)`, not
   `Theta_p(Delta)^4`.

5. **Natural-extension no-go.**  A genuine two-sided symbolic natural
   extension adds histories; it does not insert formal inverse cocycle
   letters into the forward orbit product.  C25 positive-monoid freeness
   therefore forces every positive-degree regular trace moment to vanish exactly as
   in the one-sided coding.

## Verification state

- exact producer: complete;
- independent checker: `14/14 PASS`;
- regression and mutation suite: `38/38 PASS`;
- exact matrix-inverse fuzz: `250/250 PASS`;
- source metadata audit: `18/18` records verified by DOI plus official
  metadata;
- original full-text source verification: `0/18`, explicitly disclosed;
- canonical payload SHA-256:
  `d3bde8d574b64fc146a9a65e1215654ee3516a20b3c07a4cb1f0a76ff0f2ab35`;
- certificate SHA-256:
  `412840c37d2e474462b39ce7072614323023ac8e3f968bc16a9219cc3a0c0cca`.

## Route-A evaluation

The Phase-2 tuple is

```text
(A1_WEAK,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FORMAL_HINT)
```

with overall status `ROUTE_A_EXPLORATORY`.

This is a meaningful mathematical result but not a Hilbert--Pólya candidate
ready for Route B.  It proves an exact groupoid/determinant structure, not a
prime-orbit correspondence, a xi divisor, a self-adjoint operator, or RH.

## Next large gate

Do not extend the length-nine C25 census or scan more primes as the next move.
The next question is structural:

> Can the formal inverse return arrows be realized by a genuine reversible
> dynamical system with an intrinsic positive roof and a two-sided flat-trace
> or nuclear determinant theorem?

The stop/go rule is:

- if both the roof and the trace theorem are obtained without importing the
  one-sided C26 Bergman nuclearity, proceed to a weighted arithmetic test;
- if the inverse dynamics necessarily destroys the relevant summability or
  no intrinsic clock exists, record the obstruction and pivot to a different
  dynamics.

The manuscript remains gated until the original sources needed for theorem
wording are acquired and checked at theorem/page level.  Phase 2 supplies a
paper-ready theorem skeleton, not a submission-ready paper.
