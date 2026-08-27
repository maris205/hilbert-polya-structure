# Results

The proof classifies the declared one-dimensional mass-`M` profile class for
every `m>0`: compact Barenblatt profiles for `m>1`, the Gaussian for `m=1`,
and algebraic Barenblatt profiles for `0<m<1`.  Exact Beta/Gamma integrals
give all absolute moments.  In fast diffusion the `r`-th moment is finite
exactly for `r<(1+m)/(1-m)`, logarithmically divergent at equality, and power
divergent above; hence `m=1/3` is the logarithmic second-moment boundary.

The deterministic ledger contains 18 profiles, 90 sampled profile cells, and
108 moment cells.  It also records porous support radii and boundary speeds,
chemical-potential constants, tail powers, and every sampled convergence
status.  It computes at 100 working decimal digits and serializes 82
significant digits across 382 nonzero decimal fields (plus 42 canonical zero
fields).  The independent checker recursively locks the theorem,
scope, grids, regime schema, and reconstructed values; the symbolic path also
checks the transformed Beta integrals and both energy first variations.  All
executable validation layers pass: 3,462 checker assertions, 56 SymPy checks,
byte-exact replay, and 33 repaired-hash plus one stale-hash rejection.  The
finite ledger audits
formulas and conventions; the all-parameter proof is analytic.

Route-A tuple:

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`

Overall verdict: `ROUTE_A_REJECTED`; Route B is not invoked.
