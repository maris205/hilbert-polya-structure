# Exact proof-spike ledger — Papers 92–96

The canonical executable controls live with their papers:

| ID | Control | Primary exact gate |
|---:|---|---|
| P92 | `papers/92-primitive-recurrence-avoidance-shifts/code/verify_primitive_avoidance.py` | primitive state/dual Singer orbits, hyperplane weights, full integer characteristic polynomials, traces, mixing, and first anomaly |
| P93 | `papers/93-random-push-pop-stack-cocycles/code/verify_push_pop.py` | all finite normal forms, literal labelled maps, image/fibre multiplicities, ballot sums, tilted identities, and critical laws |
| P94 | `papers/94-marked-symmetric-s-adic-shifts/code/verify_marked_s_adic.py` | literal/cyclic marker phases, exact normalized incidence action, finite inverse-limit biases, and the two product examples |
| P95 | `papers/95-minimal-slack-no-repeat-shifts/code/verify_no_repeat.py` | right-action orientation, positive reachability, sparse/literal periods, statewise first returns, and full-grid two-gap renewal |
| P96 | `papers/96-finite-subset-circle-expansion/code/verify_finite_subset_circle.py` | binary/multiset Euler coefficients, literal rational-circle subsets, formal zeta signs and rigidity, and temporal Möbius reconstruction |

The controls are regression, orientation, and endpoint guards. They do not
replace the all-parameter analytic proofs. P93's five and P94's one floating
values are explicitly non-evidentiary diagnostics and are excluded from the
368,659 exact-assertion total.
