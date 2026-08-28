# Stage 2.5 bounded hostile audit — Papers 82–86

Status: **mathematical audit complete; all five retained after corrections**.

## Independent verdicts

| Paper | Main adversarial target | Correction or strengthening applied | Final gate |
|---:|---|---|---|
| P82 | layer order, ring-size-one endpoint, spatial/temporal zeta boundary, Fredkin ownership | independently reconstructed the local rule and rank-two spectrum; corrected the historical control convention to original control-on-zero versus present control-on-one | `GO_INTERNAL / HOLD_EXTERNAL` |
| P83 | recurrence classification, maximal probability, formal zeta, smallest-modulus singularity | supplied renewal-tower normalization and entropy, defined the base cylinder, and proved uniqueness of the positive smallest-modulus pole | `GO` |
| P84 | Ramanujan multiplicities, exact period, sharp correlation rate, rigidity | derived every divisor multiplicity, restricted the sharp equality to real uniform-`L^2` vertex observables, and used `limsup` in the period-two case | `GO` |
| P85 | block alignment, intrinsic clock period, full characteristic polynomial | proved the non-wrap and wrap coordinate identities, recovered the intrinsic period, and supplied the phase-indicator/sum-zero invariant-space decomposition | `GO` |
| P86 | low-index complexity recurrence, complete-past conditioning, nonprime field, entropy gap | directly counted `L_3,L_4,L_5`, exposed cancellation of arbitrary earlier-past dependence, expanded all-label context controls, and added an independent `F_4` implementation | `GO_INTERNAL / HOLD_EXTERNAL` |

Independent hostile reviewers, separate from the final integrating pass,
re-derived the proof-critical formulas and modified the manuscripts only where
the derivation exposed a gap or ambiguous boundary.  Each paper records the
full audit in its own `HOSTILE_REVIEW.md`.

## Control upgrades caused by audit

- P82 retained its literal `m=1,...,6` functional-graph census: 299,592
  states and 1,878,811 instrumented assertions.  A separate tuple
  implementation reproduced fixed counts `5,19,80,343,1475` through `m=5`.
- P83 retained 1,369 exact assertions and its two boundary sequences through
  the advertised order.
- P84 increased to 19,901 exact assertions by adding every Ramanujan divisor
  multiplicity and exact rational sharp-rate checks.
- P85 increased to 5,242 exact assertions across 340 schedules by adding
  positive- and negative-index block-alignment checks.
- P86 increased to 199 exact `(a,b,r)` context checks over four fields.  A
  separate `F_4` implementation checked 765 arbitrary-earlier-past
  conditionals, age masses through `r=5`, and finite-past entropy convergence.

## Surviving claim boundaries

P82's zeta is spatial, not the temporal zeta of its finite-ring permutation.
P83 is a countable-state loop shift and uses Gurevich entropy.  P84 does not
re-own the unitary Cayley spectrum.  P85 classifies unconstrained periodic
alphabet schedules only.  P86 distinguishes one-dependence from finite
Markov order and does not claim a finite-context VLMC classification.

The audit establishes internal coherence, not worldwide novelty.  Public
posting, submission, venue selection, editor or author contact, and absolute
priority remain outside the authorization boundary.
