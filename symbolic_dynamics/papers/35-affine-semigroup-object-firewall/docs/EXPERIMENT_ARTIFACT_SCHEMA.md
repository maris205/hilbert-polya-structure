# Experiment artifact schema — SD-C37

## Scientific payloads

Twenty-three files are generated independently in fresh A, fresh B, and
cache-free cold start C. Their complete SHA maps must be byte-identical before
publication:

```text
ANALYSIS_REPORT.md
admissible_word_census.csv
analysis.json
backtrack_ledger.csv
bc_diagonal_fixtures.json
bc_firewall.json
boundary_controls.json
commutation_witnesses.json
control_evaluation.json
counterexamples.json
evaluation.json
exact_summary.csv
fock_marker_firewall.json
full_monoid_boundary.json
height_dag_ledger.csv
monoid_relation_controls.json
operator_certificates.json
quotient_ledger.csv
relation_witnesses.json
source_evaluator_firewall.json
source_manifest.json
source_parameters.json
test_report.json
```

## Run and seal metadata

Six non-self result payloads join the scientific files:

```text
cold_start_certificate.json
double_run_certificate.json
environment_lock.json
metadata_seal_stability.json
prototype_bridge.json
research_lock.json
```

Five self/meta files are excluded from the non-self ledger:

```text
SHA256SUMS.txt
aggregate_sha256.txt
artifact_inventory.json
idempotence_certificate.json
integrity_audit.json
```

The exact result inventory is therefore 34 files. The non-self ledger contains
47 typed paths: ten Python sources, eight experiment controls, and twenty-nine
result payloads.

## Route and provenance

`evaluations/route_a/SD-C37/2026-08-15.yaml` is excluded from the Stage-1
ledger so a future root-owned metadata-only operation can replace all three
`PENDING_FIRST_ARTIFACT_COMMIT` fields simultaneously. The route card is still
hashed by `metadata_seal_stability.json` and checked by the strict integrity
auditor.

## Canonical text contract

Every canonical artifact is a regular UTF-8 file, uses LF only, contains no
C0/C1 control bytes other than TAB/LF, has no trailing whitespace, and ends in
exactly one LF. Symlinks and Python/test caches are forbidden.
