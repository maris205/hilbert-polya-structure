# Paper improvement log

The configured external review transport was unavailable, so both passes were
genuine internal theorem-and-scope reviews.  No external independence,
acceptance score, or reviewer score is claimed.

## Round 0

The original three-page draft stated the trace-class factorization,
determinant, primitive product, and noncompact control.  It was mathematically
consistent but compressed two proof obligations.

## Round 1 review and repair

Priority issue: the order-zero statement cited a coefficient test without
displaying the limiting calculation, and the primitive-product paragraph did
not expose the absolute-convergence bound.

Repair:

- inserted
  `limsup m log m / (m(m+1)log(2)/2)=0`;
- inserted `|Tr(T^n)| <= ||T^n||_1 <= ||T||_1^n`;
- stated that nonnegative path weights justify regrouping before invoking the
  primitive repetition identity.

The rebuilt snapshot is `paper/main_round1.pdf`.

## Round 2 review and repair

Priority issue: quasinilpotence of the weighted shift should be demonstrated,
not merely named.  The negative control also needed an explicit
compact-perturbation argument so that its rational scalar expression could
not be mistaken for an owned determinant.

Repair:

- added `||S^k||=2^{-k(k+1)/2}` and the spectral-radius conclusion;
- added the contradiction obtained by subtracting the rank-one return from a
  hypothetically compact control operator;
- renamed the rational control expression as a formal first-return series.

The rebuilt snapshot is `paper/main_round2.pdf`, byte-identical to
`paper/main.pdf`.

## Remaining boundary

No source-facing target comparison, prime-like orbit law, or natural unitary
lift is available.  These are retained as failures rather than paper-writing
defects.
