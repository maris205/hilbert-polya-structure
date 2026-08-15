# Experiment artifact schema — SD-C36

## Scientific payloads

The following 19 files are generated independently in runs A, B, and C and
must be byte-identical:

```text
ANALYSIS_REPORT.md
analysis.json
boundary_controls.json
code_clock_ledger.csv
connector_construction_counterexamples.csv
counterexamples.json
evaluation.json
graph_census.csv
graph_witness_samples.csv
graph_witness_summary.json
inventory_controls.csv
kraft_clock_summary.csv
marker_ledger.csv
neutral_recognizer.json
parameters.json
pruning_polynomials.json
raw_data_table.csv
source_evaluator_firewall.json
test_report.json
```

## Run and seal metadata

```text
artifact_inventory.json
double_run_certificate.json
cold_start_certificate.json
environment_lock.json
research_lock.json
metadata_seal_stability.json
idempotence_certificate.json
integrity_audit.json
SHA256SUMS.txt
aggregate_sha256.txt
```

The exact canonical result set is the union of these lists: 29 files. The
Route-A YAML is an external metadata card and is excluded from the Stage-1 SHA
ledger so that the future paired provenance replacement can be metadata-only.

## Research-document lock

`research_lock.json` schema v2 records exactly six current inputs, both as
named pointer fields and as a path/hash ledger:

```text
PREREGISTRATION.md
SOURCE_LOCK.md
DERIVATION_PACKAGE.md
PROOF_PACKAGE.md
LITERATURE_AUDIT.md
experiments/EXPERIMENT_PLAN.md
```

The integrity auditor recomputes all six SHA-256 values from the current bytes
and requires exact agreement with both representations. The fresh-double-run,
cold-start, and metadata-seal certificates each bind the resulting research
lock hash.

## Dependency scope

`environment_lock.json` distinguishes the dependency-free scientific pipeline
from the metadata layer. `scientific_dependencies` is the empty list because
source generation, independent evaluation, tests, and analysis use only the
Python standard library. `seal_audit_dependencies` records `PyYAML: 6.0.2`
because Route-A sealing and integrity auditing parse YAML. The seal and final
auditor both compare the recorded version with the installed runtime version.

## Route-A v0.2 metrics

The Route-A `a2.metrics` map contains all nine mandatory v0.2 fields:
`zero_error_train`, `zero_error_validation`, `zero_error_test`,
`extra_zero_count`, `missing_zero_count`, `root_count_discrepancy`,
`cutoff_drift`, `precision_drift`, and `control_margin`. Because no target-zero,
floating-precision, fitted-cutoff, or fitted-margin comparison is performed,
each field is an explicit string beginning with `not_applicable;`.

## Ledger scope

`SHA256SUMS.txt` covers every experiment Python source, experiment control,
report/registry document, and non-meta result payload. It excludes itself,
`aggregate_sha256.txt`, `artifact_inventory.json`, `idempotence_certificate.json`,
`integrity_audit.json`, and the Route-A card. `research_lock.json` records the
read-only frozen research-document hashes.

## Text canonicalization

Every canonical experiment artifact is UTF-8, uses LF only, contains no C0/C1
control bytes other than TAB/LF, has no trailing whitespace, and ends in
exactly one LF byte. Python and pytest cache directories are forbidden.
