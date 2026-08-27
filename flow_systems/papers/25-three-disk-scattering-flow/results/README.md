# P25 results — Rounds 2 and 3

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
