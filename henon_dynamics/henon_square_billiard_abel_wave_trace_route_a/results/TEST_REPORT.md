# C157 test report

The deterministic producer and fresh-path replay pass with evidence SHA-256
`de4f1a278c576fd4584e7a20ff5d35144f68b4369a4e93a5acdcf625f09af567`.

- Full producer-independent checker: **1022 assertions**.
- Independent SymPy path: **1,198 checks**.
- Hostile suite: **104/104 rejected**, consisting of 103 repaired-hash semantic
  mutations and one stale-hash control.

The checker reconstructs every occupied sum-of-two-positive-squares shell by a
different loop order, verifies primitive/repetition uniqueness, and recomputes
both complex sentinels with larger boxes.  SymPy differentiates the
Laplace--Bessel transform, verifies the Fourier constant, principal-branch
scaling, boundary-pole residue, and all exact shells through squared norm 500.
Every claim-bearing nested dictionary has an exact key ledger.  Frozen text is
matched exactly rather than by prefix, while the two frozen complex receipts
also undergo independent larger-cutoff reconstruction on the full path.  The
analytic truncation bounds are rigorous; the `mpmath` centers are deterministic
55-decimal sentinels rather than interval-arithmetic outputs, with an explicit
`1e-34` serialization/rounding margin in independent-center comparisons.

The dual numerical receipt is not an empirical-agreement proof.  It subtracts
the first two complex binomial terms, bounds the integral Taylor remainder by
`15|s|^4/(8*3^(7/2)|m|^7)` for `|m|>=M>=|s|`, counts exactly `8k` lattice
points on each max-norm square, and uses
`sum_(k>M)k^-6 <= 1/(5M^5)`.  After the outer trace coefficient this gives the
recorded rigorous error `|s|^5/(2*pi*3^(5/2)*M^5)`.
