# C198 hostile audit

## Attacks

1. **Wrong Lambert branch.**  A second implementation solves each side of the
   minimum of `x-log x` without Lambert W.
2. **Hidden zero-infection error.**  `I0=0,x0>1` stays fixed on the upper branch;
   the paper never applies the positive-infection `W_0` formula there.
3. **Threshold overstatement.**  At `x0=1` the first derivative of infection is
   zero, but susceptible mass immediately falls and infection then decays.
4. **Finite-state overreach.**  Twenty-four branch sentinels test conventions;
   they do not prove global convergence.
5. **Explicit-time overclaim.**  The package gives an exact quadrature, not an
   elementary closed formula for all three components versus time.
6. **Medical laundering.**  No clinical data, calibration, prediction or
   intervention claim is present.
7. **Determinant laundering.**  Lambert W solves a terminal-state equation; it
   is not a target Zeta or Fredholm determinant.
8. **Proves-too-much control.**  Arbitrary rescaled, prime-labelled and
   composite-labelled rates share the same theorem.
9. **Hash-only defense.**  Semantic attacks repair the payload hash first.

## Outcome

All tested attacks are closed.  The strict Route-A rejection and medical-safety
boundary survive.  This is internal hostile review, not external peer review.
