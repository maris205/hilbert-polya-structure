# Experiment Artifact Schema — Paper 33

## Primary payloads

- `modulus_homology_census.csv`: one row per modulus with state counts, orbit
  counts, relation rank, relative/cuspidal Betti numbers, cusp witness,
  adjacency descent flag, and post-census arithmetic class.
- `matched_clone.csv`: opaque relabel naturality checks.
- `random_action_controls.csv`: transitive `C2*C3` controls.
- `twist_census.csv`: six honest characters and fifteen zero-superdimension
  differences.
- `cross_square_complex.json`: cross graph and diamond boundary ranks.
- `source_oracle_certificate.json`: forbidden-token source scan.
- `summary.json`: route and aggregate decision summary.
- `test_report.json`: deterministic prototype self-test summary.

## Derived payloads

- `evaluation.json`: independent payload evaluator output.
- `double_run_certificate.json`: isolated double-run byte identity certificate.
- `SHA256SUMS.txt`: authority result ledger.
- `aggregate_sha256.txt`: SHA-256 of `SHA256SUMS.txt`.
- `artifact_inventory.json`: result inventory written by `freeze_artifacts.py`.
- `integrity_audit.json`: ledger verification report.
