# Exact evidence plan — HCS-C285

## Claims-to-tests matrix

| Claim | Producer evidence | Independent reconstruction | Proof owner |
|---|---|---|---|
| `Z_N=h_N(w)` and product form | all states of 9 rational networks | Fraction traffic solve, generator RREF left nullspace, global balance | Theorem 1 |
| three exact `Z_N` routes | direct composition sum, convolution, Newton | separately ordered implementations of the same three definitions | generating identity/Newton proof |
| all occupancy derivatives | means, covariance, 165 joint factorial cells | enumeration plus coefficient derivative | finite differentiation |
| throughput and directed flows | busy probabilities, station/edge ledgers, currents | exact `Z_(N-1)/Z_N`, row/column conservation | decrement identity |
| exact reversal | `P*`, detailed-balance defects, involution flag | independent traffic solve and second reversal | Theorem 2 |
| tied/unique condensation | 4 weight families at `N=0,1,2,4,8,16,32` | exact finite coefficient and conditional-composition moments | Theorem 3 |
| boundary semantics | 12 explicit faces | exact ordered ledger | boundary atlas |

## Frozen finite cases

The case grid deliberately includes:

- `N=0` and `N=1` with an irreducible nonreversible routing matrix containing
  both zeros and self-loops;
- a dense nonreversible rational routing matrix;
- a reversible three-station line with self-loops;
- a deterministic four-cycle with a unique maximal weight;
- the same cycle with two tied maximal weights;
- an all-equal three-station weight vector;
- periodic embedded routing with zero edges;
- `m=1`, where all service events are self-routes.

The condensation grid adds unique, two-tied, three-tied, and all-equal weight
families. Common scaling of weights is present so the checker cannot assume
`w*=1`.

## Independence requirements

The checker does not import the producer. It must:

1. reject duplicate JSON keys and enforce exact key sets at every stored
   level;
2. solve `e=eP`, `sum e=1` with exact Fractions;
3. build every finite row-generator, including aggregation of routes but
   excluding self-events from state changes;
4. compute the full nullspace of `Q^T` by its own RREF and prove it is
   one-dimensional;
5. normalize that null vector and compare every state probability;
6. reconstruct all `Z`, moment, flow, reversal, condensation, and boundary
   cells independently;
7. reject row duplication, row-count-preserving drop/replace, truncated or
   empty vectors, semantic mutations with repaired payload hashes, a stale
   payload hash, and duplicate raw JSON keys.

## Commands

From this package directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_gordon_newell_producer.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_gordon_newell_checker.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_gordon_newell_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_gordon_newell_replay.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_gordon_newell_mutation.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_release_manifest.py
```

## Acceptance gates

- canonical JSON payload hash verifies;
- producer and independent checker agree on every exact cell;
- two unrelated fresh output paths reproduce the evidence byte for byte;
- all hostile attacks fail closed;
- three manuscript revisions compile twice from fresh directories to the
  archived bytes at `SOURCE_DATE_EPOCH=1788307200`;
- every PDF font is embedded and subset, no LaTeX/layout/citation warning is
  present, and extracted text plus rendered-page inspection passes;
- 27 payload files and 28 physical files close in the self-excluded manifest.

No finite test is promoted to the all-parameter proof.
