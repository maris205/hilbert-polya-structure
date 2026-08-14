# Artifact Schema — SD-C25

All CSV files are UTF-8, LF-terminated, headered, and deterministically
ordered. JSON files use sorted keys and a terminal newline.

## Candidate/source artifacts

- `canonical_word_certificates.csv`: one row for every (2\le k\le4096),
  including edge, word, marking, holonomy, and primitive certificates.
- `source_oracle_certificate.json`: AST policy audit, candidate/evaluator
  separation, exact source counts, and zero-data flags.

## Finite-memory artifacts

- `finite_state_periodicity.csv`: one row per unary map through four states.
- `boolean_relation_periodicity.csv`: all two-state Boolean relations.
- `finite_semigroup_controls.csv`: cyclic-group and non-group controls.
- `composite_witnesses.csv`: post-freeze (p(1+\lambda)) witnesses.
- `recurrence_certificates.csv`: characteristic polynomial, residual,
  rational-series, and minimal-order fields for 48 matrix cases.
- `nilpotent_memorizer_controls.csv`: cutoff, target family, realization,
  target SHA, exact-fit result, and mandatory `PROVES_TOO_MUCH` label.

## Operator and wrapper artifacts

- `canonical_block_traces.csv`: cyclic trace plus the complete coefficients
  of `det(I-w_k*B*A^(k-1))`; includes the trace-zero repetition firewall.
- `finite_block_power_traces.csv`: exact power traces through 32.
- `finite_block_determinants.csv`: Newton/direct determinant comparison.
- `trace_class_diagnostics.csv`: directed lower/upper prefixes and theorem
  labels; `finite_prefix_is_proof` is always false.
- `transient_wrapper_structure.csv`, `transient_wrapper_traces.csv`, and
  `recurrent_wrapper_controls.csv`: only the licensed Paper19/20 architectures.
- `wrapper_import_certificates.json`: paths and SHA-256 values of the imported
  Paper19/20 source, ledger, and integrity records.
- `roof_marker_mismatch.csv`: exact same-object monomial identity and
  one-dimensional post-freeze oracle-control flags.

## Reproducibility artifacts

- `run_parameters.json`, `environment_lock.json`, `summary.json`,
  `analysis_summary.json`, `test_summary.json`,
  `double_run_certificate.json`, `integrity_audit.json`, and
  `SHA256SUMS.txt`.
- `route_gate_summary.csv` and
  `evaluations/route_a/SD-C25/2026-08-14.yaml` use the frozen strict tuple.

The six target-zero/root metrics in the YAML are strings beginning with
`not_applicable;`, and `route_b_invocation_allowed` is false.

