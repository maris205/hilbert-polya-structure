# HCS-C273 — Sparre–Andersen universal fluctuation laws

This package proves and independently certifies the classical distribution-free
fluctuation laws for a random walk with iid, continuous increments symmetric
about zero.  The no-ties hypothesis is frozen: strict positivity, nonnegative
survival, and the time of the maximum coincide only because all finite partial
sums are almost surely distinct.

The main theorem closes, for every `n`:

- `q_n = P(S_1>0,...,S_n>0) = binom(2n,n)/4^n` and its square-root generating
  function;
- the first strict descent law;
- the common discrete-arcsine law of the number of positive partial sums and
  the unique maximum time;
- the `Beta(1/2,1/2)` scaling limit;
- an explicit simple-symmetric-walk counterexample when atoms create ties.

The status is **PROVABLE AS STATED**.  Exact finite enumeration is a regression
and convention oracle, not the proof of distribution-free universality.  The
proof is in [THEOREM_PACKAGE.md](THEOREM_PACKAGE.md), executable evidence is in
`results/`, and the paper is `paper/main.pdf`.

The Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and the verdict is
`ROUTE_A_REJECTED`.  Route B is disabled.  The scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`; probability generating functions are not
renamed as arithmetic Euler products or target determinants.
