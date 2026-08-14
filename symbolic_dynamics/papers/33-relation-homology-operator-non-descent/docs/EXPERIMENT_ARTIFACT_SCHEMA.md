# Experiment Artifact Schema — Paper 33

## Pipeline boundary

- `code/cycle_quotient_core.py`: frozen candidate core.
- `code/generate_results.py`: byte-exact research prototype bridge only; not
  invoked by the canonical pipeline.
- `code/source_generator.py`: canonical source-only raw generator.
- `code/audit_source_separation.py`: AST-based source/classifier firewall.
- `code/post_census_classifier.py`: post-census arithmetic labels and
  prototype-compatible aggregate outputs.
- `code/independent_evaluator.py`: no project imports; reconstructs every
  finite invariant and arithmetic label.
- `code/run_tests.py`: candidate-aware unit and integration checks.
- `experiments/run_exact_suite.py`: full fresh double-run certificate.

## Raw source payloads

- `modulus_source_census.csv`: 191 rows with source invariants and no
  arithmetic evaluator class.
- `matched_clone.csv`: 191 opaque relabel naturality rows.
- `random_action_controls.csv`: 64 generic transitive `C2*C3` controls.
- `twist_census.csv`: six honest and fifteen virtual character rows, with
  cycle-word and chain-norm semantics separated.
- `cross_square_complex.json`: exact cross graph and boundary ranks.
- `source_summary.json`: source-only aggregates.
- `source_test_report.json`: source-only checks.
- `source_oracle_certificate.json`: byte-compatible research core scan.
- `source_separation_certificate.json`: physical source/classifier audit.

## Post-census and independent-evaluation payloads

- `modulus_homology_census.csv`: raw columns plus independently timed
  arithmetic labels.
- `classification_certificate.json`: raw-column preservation, labels, and
  class counts.
- `summary.json` and `test_report.json`: eight-payload prototype-compatible
  aggregates and 25/25 firewall.
- `prototype_bridge_certificate.json`: core, runner, payload, and test bridge.
- `evaluation.json`: 8349-check independent reconstruction.
- `evaluation_comparison.csv`: per-stratum raw statistics.
- `unit_test_report.json`: 1932 authority unit/integration assertions.

## Reproducibility payloads

- `environment_lock.json`, `run_parameters.json`, and `research_lock.json`:
  fixed environment, parameters, prereg hash, and research bridge hashes.
- `double_run_certificate.json`: 20-payload full-pipeline byte identity.
- `SHA256SUMS.txt`: paper-root-relative ledger covering all canonical Python
  sources, experiment controls, reports, and non-meta results.
- `aggregate_sha256.txt`: SHA-256 of the ledger.
- `artifact_inventory.json`: typed source/control/result inventory.
- `integrity_audit.json`: full ledger, schema, provenance, cache, LF, control,
  and EOF audit.
- `idempotence_certificate.json`: empty-results six-stage cold start plus
  two-run freeze/integrity idempotence.

The five meta-integrity files (`SHA256SUMS.txt`, `aggregate_sha256.txt`,
`artifact_inventory.json`, and the two audit certificates) are excluded from
their own ledger to avoid circular self-hashing; the integrity audit validates
them directly.  The root-owned `PAPER_MANIFEST.sha256` is excluded from both
the scientific ledger and canonical-text count so the later metadata-only
commit binding is hash-stable.
