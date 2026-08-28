# Paper improvement log

## Round 0 — original

Introduced fixed-point Brownian resetting, renewal propagator, first-passage
transform, MFPT, universal optimum, and the scope firewall.

## Round 1 — realization and moment audit

Separated the free stationary process from the killed search process; added the
explicit sub-Markov warning.  Replaced a generic “moments by derivatives”
sentence by the exact signed identities for `F` and `S` with the correct
`n>=0` indexing, and stated the `s=0` survival limit.

## Round 2 — release audit

Added the closed erfc integral including the cancellation-safe `x=0` branch,
the independent quadrature certificate, boundary ledger, hostile unknown-key
tests, and explicit wording that the Laplace denominator is not a dynamical
zeta or Fredholm determinant.  Tightened source attribution and the
non-arithmetic Route-A verdict.
