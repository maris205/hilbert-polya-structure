# Experiment Artifact Schema — SD-C31

## Flat exact ledgers

- `baseline_pair_ledger.csv`: 76 baseline cutoff/pair rows.
- `control_pair_ledger.csv`: 47 pair rows across four control classes.
- `scheme_shift_ledger.csv`: 15 frozen local finite-scheme rows.
- `coefficient_grid_ledger.csv`: 49 `(alpha,beta)` rows.
- `determinant_power_ledger.csv`: powers one through four and ownership status.
- `route_gate_summary.csv`: frozen five-component tuple.
- `analysis_comparison_table.csv`: seven baseline/control aggregate rows.
- `raw_counterterm_table.csv`: compact seven-object exact table.

Every CSV is UTF-8 with LF line endings and no carriage-return byte.

## Structured exact artifacts

`incidence_checks.json`, `baseline_cutoffs.json`, `scheme_shifts.json`,
`control_ledgers.json`, `coefficient_search.json`, and
`determinant_ownership.json` contain the complete exact ledgers.  Rational
values are serialized as numerator, denominator, and canonical text; radical
amplitudes also record the squarefree radicand.

`source_oracle_certificate.json`, `run_parameters.json`,
`environment_lock.json`, and `theorem_ledger.json` freeze scope and
provenance.  `evaluation.json` is recomputed independently of candidate code;
`test_report.json` and `analysis.json` record test and interpretation layers.

`double_run_certificate.json` compares two cleared-output runs.
`integrity_audit.json` validates Route-A v0.2, row counts, source separation,
LF/control-byte/cache hygiene, and scientific gates.  `SHA256SUMS.txt` hashes
all Python sources and result artifacts except itself.
