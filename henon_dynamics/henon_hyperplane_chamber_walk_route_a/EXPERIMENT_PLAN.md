# Experiment plan

## Claim-driven gates

| Gate | Exact check | Release condition |
|---|---|---|
| E0 provenance | candidate/date/commit/evaluator/scope exact maps | no stale or enlarged provenance |
| E1 face dynamics | covector alphabet, chamber census, face-product closure, stochastic rows | every serialized cell reconstructed |
| E2 intersection geometry | support flats, inclusion poset, Möbius recursion, Zaslavsky sum | flat count and multiplicities exact |
| E3 operator identities | transition matrix, flat factorization, characteristic polynomial, determinant, traces | producer/checker/SymPy agree exactly |
| E4 stationarity | separating predicate, weighted-order sampler, stationary equation | six separating fixtures pass |
| E5 mixing | direct TV, nonchamber DP, Möbius formula, hyperplane union bound | all 24 rows satisfy both inequalities |
| E6 boundary | `A0` hyperplanes, component keys, stationary-simplex vertices | two nonseparating fixtures pass |
| E7 hostile audit | repaired-payload semantic mutations and one stale-hash mutation | every attack rejected |
| E8 publication | three content-distinct PDFs, fixed-epoch double build, fonts/log/layout/visual checks | all artifacts close under manifest |

## Independent implementations

The producer constructs coordinate covectors by sign cubes and braid covectors
by ordered set partitions.  It computes weighted-order laws by permutation
enumeration.  The checker imports no producer code: it reads generic sign
vectors, rebuilds products and support lattices, uses an alternate recursive
Möbius calculation, and obtains the sampler through subset dynamic programming.
The SymPy program separately reconstructs exact matrices, characteristic
polynomials, determinants, traces, and eigenspace dimensions.

## Frozen census

Eight fixtures cover dimensions/ranks up to four: four separating coordinate
cases, one nonseparating coordinate case, two separating braid/Tsetlin cases,
and one nonseparating braid case.  The expected aggregate is 316 faces, 94
chambers, 75 flats, 1,604 transition cells, 62 nonzero stationary probabilities,
24 mixing rows, and 48 trace rows.

Enumeration is explicitly a regression oracle.  Failure on any fixture stops
release; success does not replace the cited all-family proof.
