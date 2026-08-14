# SD-C24 experiment artifact schema

## Exact cycle ledgers

- `simple_cycle_holonomy.csv`: cutoff, canonical directed cycle, length,
  cofactor word, exact `Q`, telescoped value, and `Q=2` classification.
- `atomic_holonomy_witnesses.csv`: both enumerated and predicted directions
  for post-freeze atoms `2,3,5,7`.
- `rooted_cycle_ledger.csv`: every rooted word through period 8, its canonical
  primitive root, temporal repetition, rotation index, mass, and holonomy.

## Trace and determinant ledgers

- `group_trace_coefficients.csv`: exact nonzero group-algebra coefficients.
- `atomic_trace_coefficients.csv`: observed/closed-form atomic coefficients.
- `neutral_determinant.csv`: neutral traces and determinant coefficients.
- `fourier_reconstruction.csv`: alias-free character inversion diagnostics.
- `finite_determinant_checks.csv`: direct and Newton finite determinants.

## Analytic and control ledgers

- `gauge_identity.csv`, `unitary_gauge.csv`: exact and unitary gauge checks.
- `trace_class_diagnostics.csv`: row, fixed-row, and successor prefixes.
- `pure_cofactor_spine.csv`: non-trace-class and conditional noncompactness.
- `pure_cofactor_series.csv`, `induced_return_exact.csv`,
  `factorial_damping.csv`: the three Fredholm-trilemma regimes.
- `unitary_phase_spine.csv`: phase blindness on all tested canonical cycles.
- `inventory_controls.csv`, `presentation_transport.csv`: support universality
  and naturality controls.

## Aggregate and integrity artifacts

- `summary.json`: deterministic raw counts and explicit target-data firewall.
- `analysis_summary.json`: observations, interpretations, implications, and
  the strict Route-A outcome.
- `test_summary.json`: exact collected/pass/fail counts.
- `route_gate_summary.csv`: one row per Route-A gate.
- `integrity_audit.json`: source, scope, schema, provenance, and science gates.
- `SHA256SUMS.txt`: hashes of all Python and result artifacts except itself.

Every floating field is diagnostic. Exact theorem audits use integers or
rational strings. Empty target-zero metrics are never encoded as numerical
zeros; they use the explicit not-applicable sentinel.
