# Experiment and proof plan

## Analytic contract

1. Define entire functions `C(k,t)` and `S(k,t)` by power series, including
   positive, zero, and negative `k` without branch ambiguity.
2. Form each segment transfer and multiply to obtain the exact monodromy and
   closed discriminant.
3. Use the real determinant-one characteristic polynomial to prove the
   elliptic/hyperbolic classification.
4. Split `Delta=+/-2` into scalar and nontrivial Jordan cases and state the
   correct bounded-line/generic-linear-growth behavior.
5. Prove the Chebyshev iterate, Floquet rates, swapped-order trace law, and
   all parameter faces.

## Executable contract

- Evaluate the full `6 x 6 x 5 x 5` all-sign grid at 90 decimal digits.
- Independently reconstruct segments from truncated power series rather than
  the producer's trigonometric/hyperbolic formulas.
- Check determinant, trace, class, and powers through `n=12` on all 900 rows.
- Verify six exact scalar/Jordan/hyperbolic boundary matrices and prove the
  general identities with SymPy.
- Require clean byte replay, repaired-hash mutation rejection, and three
  deterministic paper rounds built twice in fresh trees at fixed epoch.

The grid is a regression oracle, not a replacement for the continuum proof.
