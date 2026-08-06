# Result inventory

Status: **first round and C02C finite-window stage complete; artifacts retained
for positive and negative outcomes**.

## `c02_projective/`

- `pilot_summary.json` -- exact rational domain constants and gate decision;
- `memory_bounds.csv` -- uniform itinerary-memory bounds for \(m=1,\ldots,8\);
- `state_disk_bundle.csv` -- all six chronological graph edges;
- `periodic_monodromy.csv` -- 17 primitive cycles through period 8;
- `independent_check.json` -- independent exact audit;
- `RESULTS.md` -- theorem, limitations, and decision.

Decision: retain the real-base/complex-fibre contraction lemma; no Schottky,
nuclearity, or Route-A A2 promotion.

## `c02_complex_base/`

- `complex_polydisc.json` -- exact/dyadic radicand disks, margins,
  contraction, and cyclic chronology through length 12;
- `independent_check.json` -- 18-check algebraic/chronological audit;
- `RESULTS.md` -- proved bridge and next-theorem boundary.

Decision: the complex signed-root self-map theorem is proved and has been
extended by C02C; it did not by itself imply nuclearity.

## `c02c_finite_window/`

- `certificate.json` -- complete producer configuration, exact constants,
  case IDs, maxima, expected-fail controls and artifact hashes;
- `open_windows.csv` -- 432 exhaustive center-endpoint cases plus persisted
  localization and projective-chain diagnostics;
- `cyclic_matching.csv` -- 120 complete cyclic words through period 8,
  including chronological period-one/two conventions and matching/Hill data;
- `gluing_controls.csv` -- direct two-coordinate gluing and the scalar-average
  and reversed-order expected failures;
- `independent_check.json` -- separate Newton solver, complete-ID checks,
  high-precision worst-case rechecks and truncation/tamper rejection;
- `RESULTS.md` -- theorem additions, conditioning record, scope and decision.

Decision: all frozen checks pass.  Retain the explicit \(H_6\) endpoint,
matching/Hill and complex-projective theorem as an effective specialization;
its novelty delta is unconfirmed because the real SFT/uniqueness and general
pinning/residue mechanisms collide with prior art.  Hold the manuscript until
a signed, aggregate trace-compatible operator approximation theorem adds a
genuinely new estimate.

## `c03_finite_field/`

- `c03_census.json` -- full configuration, local factors, aggregates,
  controls, firewall, and decision;
- `c03_prime_summary.csv` -- one row per prime;
- `c03_cycle_counts.csv` -- raw, symmetric, and paired cycle factors;
- `c03_fix_counts.csv` -- fixed counts through iterate 64;
- `c03_random_controls.csv` -- all 1,728 frozen controls;
- `c03_independent_check.json` -- independent 54-prime tuple-state census;
- `RESULTS.md` -- raw diagnostics and reversible-null obstruction.

Decision: reject the naive global Euler product.  A revival must retain
Frobenius extension degree and dynamical iterate as distinct variables.

## `c05_maslov/`

- `phase_ledger.csv` -- 2,240 primitive/repeat rows;
- `determinant_coefficients.csv` -- formal determinant coefficients through
  degree 20;
- `cutoff_evaluations.csv` -- frozen cutoff/probe evaluations;
- `controls.json` -- orientation, constant-roof, shuffled-action, random-phase,
  and gauge controls;
- `summary.json` -- exact/numerical checks and Route-A ceiling;
- `RESULTS.md` -- Hill theorem, gauge obstruction, and local Maslov collapse.

Decision: reject an intrinsic fixed-\(z\) absolute phase.  Retain the exact
phase ledger and obstruction theorems as controls.

## Consolidated analysis

`../refine-logs/EXPERIMENT_RESULTS.md` contains the cross-candidate raw tables,
numbered findings, interpretations, implications, next tests, and conservative
Route-A screening, including the C02C addendum.  Negative results are also
registered in `../../docs/obstruction_registry.md`.
`first_round_summary.csv` is the compact first-round machine-readable table.
