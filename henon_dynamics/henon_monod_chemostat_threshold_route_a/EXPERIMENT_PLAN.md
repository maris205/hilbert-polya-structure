# Experiment plan

The executable work tests a theorem; it does not fit data.

| Gate | Object | Independent check |
|---|---|---|
| G0 | source commit, evaluator hash, epoch, scope | literal and payload locks |
| G1 | `Q'=D(S_in-Q)` | fresh rational vector-field addition |
| G2 | three threshold regimes | 18 rational cases, six per regime |
| G3 | equilibria and spectra | direct substitution and characteristic polynomials |
| G4 | invariant-leaf transient | symbolic differentiation of both implicit laws |
| G5 | boundary faces and no-cycle proof | exact face equations plus analytic argument |
| G6 | implementation independence | separate checker, SymPy, byte replay |
| G7 | hostile integrity | at least 20 rehashed semantic corruptions |
| G8 | paper release | three distinct revisions, deterministic PDF, manifest closure |

The checker does not import the producer.  Fractions are parsed from the JSON
and reconstructed from a separately frozen case list.  No tolerance-based
acceptance, prime table, target-zero table, or stochastic sampling is used.
