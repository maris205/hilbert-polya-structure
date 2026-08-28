# Experiment plan and evidence boundary

## Frozen owner

The owner is the real Hessian at the standing wave of the one-dimensional
focusing cubic NLS.  Parameters are \(\omega>0\), with physical time and
space; the source baseline is commit `86c7bb8a39cdd1b8e941e45833b068170ca06287`,
the route-a evaluator is v0.2.0 (SHA-256
`6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`), and the
scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.

| Claim | Independent deterministic test | Boundary/scope |
|---|---|---|
| sech profile solves the stationary ODE | explicit derivative identity and 15 probes | \(\omega>0\) |
| mass, Hamiltonian, action and VK slope | exact scaling integrals and SymPy substitution | real line; no periodic branch |
| Hessian eigenpairs | independent `mp.diff` residuals and symbolic kernels | continuum theorem, no finite-box proof |
| essential threshold and Morse index | operator form plus Pöschl–Teller factorization | \([\omega,\infty)\), one-dimensional |
| singular/degenerate faces | explicit boundary ledger | \(\omega\downarrow0\), defocusing, \(d\ge2\) |

The producer, independent checker, SymPy cross-check, byte replay and hostile
mutation harness are all source-local.  The finite rows are regression tests;
the manuscript carries the quantified theorem and its proof ledger.
