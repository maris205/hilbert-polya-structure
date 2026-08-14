# Candidate registry

| Candidate | Frozen object | Current status | Route-B allowed | Evidence |
|---|---|---|---:|---|
| `henon_homotopy_v2_shadow_transport` | (H_{a,\rho}=(1-a x^2-\rho y,x)), (a=u_c) | `ROUTE_A_REJECTED`; sealed endpoint carrier unavailable and neighbor specificity failed | No | [definition](../evaluations/route_a/henon_homotopy/candidate_definition.md), [source lock](../papers/1-symp-vs-diss/experiments/source_lock.json), [results](../papers/1-symp-vs-diss/notes/RESULTS.md) |
| `pcf_markov_baker_v1` | Three-state PCF Markov factor and constant-slope compact piecewise exact-symplectic baker | `ROUTE_A_REJECTED`; structural carrier verified, exact all-prime multiplier clock proved impossible for the frozen finite-memory class | No | [definition](../evaluations/route_a/pcf_markov_baker/candidate_definition.md), [evaluation](../evaluations/route_a/pcf_markov_baker/2026-08-13-final.yaml), [results](../papers/2-branch-baker/results/EXPERIMENT_RESULTS.md), [proof](../papers/2-branch-baker/PROOF_PACKAGE.md) |

The generic area-preserving Hénon map, its periodic-orbit ledger, and its
standard dynamical zeta are baselines rather than separate arithmetic
candidates. The weaker parity-shadow gate did not pass, so the multiplier-to-
rational-prime, zeta, and quantization branches are closed for this candidate.

The PCF Markov--baker remains a reusable exact structural control.  Its parent
zeta and boundary correction are prior-art reproduction baselines; its Route-A
closure follows from the finite-rank clock obstruction, not from a failed
numerical prime fit.
