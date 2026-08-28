# P25 results — Rounds 2 through 5

Generated artifacts:

- `three_disk_primitive_ledger_round2.csv` — 2,241 geometry rows;
- `three_disk_controls_round2.csv` — 747 complete three-parameter control rows;
- `round2_metrics.json` — residual envelope, control metrics, software versions,
  and Route boundary.

The primary ledger includes:

```text
d_over_a,topological_word_length,cyclic_word,reverse_oriented_word,
symbolic_primitive,center_polygon_proxy_status,center_polygon_proxy_length,
actual_billiard_orbit_status,collision_points,actual_flight_length,
independent_flight_length,stationarity_residual,reflection_residual,
minimum_other_disk_clearance,monodromy_trace,unstable_multiplier,
monodromy_determinant_high_precision,
monodromy_determinant_residual_high_precision,
monodromy_double_trace_relative_residual,
half_density_statistic_id,half_density_value,
finite_difference_validation_status,stability_evidence_status,
topological_cutoff_complete,geometric_completeness_boundary
```

The same schema and topological cutoff `<=12` were used at
`d/a=5.8,6.0,6.2`.  All 747 words have certified actual-orbit solutions in all
three geometries.  Center-polygon proxy fields remain present so no downstream
analysis can silently substitute center distance for physical flight length.
The monodromy fields expose both the 80-digit unit-determinant residual and the
relative trace disagreement against a binary64 rebuild; neither replaces the
separately labeled finite-difference return-map status.

The control ledger uses no rational-prime list.  Guaranteed composites are
constructed algebraically as consecutive-factor products; random phases,
stabilities, periods, and integer labels are SHA-256 deterministic.  The
neighboring-parameter persistence crosses the frozen stop threshold, so the
half-density statistic is `[STOP_SCOPED] / PROVES_TOO_MUCH` as arithmetic
evidence.  This does not test or establish the separately frozen
`[MODELING_CHOICE] ABSENT_BY_CONSTRUCTION` A0-source status.

## Round-3 direct stability ledger

- `three_disk_return_map_validation_round3.csv` — 2,241 row-by-row direct
  return-map checks, three difference scales, refinement method, parity factor,
  determinant residual, trace residual, and explicit failure tier;
- `round3_stability_metrics.json` — counts by word length, geometry, and source
  trace-conditioning tier plus the certified residual envelope.

All 2,241 rows are `NUMERICALLY_CERTIFIED` under the frozen Round-3 contract;
2,232 are newly closed relative to Round 2.  The direct physical trace obeys
`(-1)^word_length` times the positive-reflection paraxial trace.  The high-
precision direct calculation is an independent dynamical calibration, not an
exact determinant or arithmetic-specific result.

## Round-4 conditioning audit

- `round4_conditioning_by_length.csv` gives the complete length-2-through-12
  partition, including method counts and residual envelopes;
- `round4_fallback_audit.csv` exposes every one of the 39 fallback rows; and
- `round4_conditioning_metrics.json` records the static dependency audit,
  descriptive partitions, shared acceptance checks, inference boundary, and
  unchanged Route firewalls.

The method split is 2,202 direct-Newton rows and 39 stationarity-fallback rows.
The fallback rows occur only at lengths 11 and 12 and all pass the frozen final
contract.  These are `NUMERICALLY_CERTIFIED` ledger facts; the aggregate
half-density remains a `NUMERICAL_OBSERVATION`.

## Round-5 universal half-density theorem ledger

- `round5_universal_half_density_ledger.csv` records 6,723 branches: 2,241
  primitive owners times `r=1,2,3`, with primitive/repetition class, physical
  eigenvalue sign, leading half-density, positive and physical exact
  amplitudes, correction, and theorem residual;
- `round5_universal_half_density_by_repetition.csv` gives the three frozen
  repetition summaries; and
- `round5_universal_half_density_metrics.json` records input hashes, theorem
  statement, residual envelope, paper disposition, and route firewalls.

The algebraic identity is `[PROVED]`; the replay is
`[NUMERICALLY_CERTIFIED]`.  The maximum leading-factor relative correction is
about `1.1093e-2`, `1.2305e-4`, and `1.3650e-6` for `r=1,2,3`.  These artifacts
use no prime or Riemann-zero table.
