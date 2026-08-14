# SD-C34 experiment artifact schema

## Sixteen fresh artifacts

- Candidate/source: `candidate_census.csv`, `matched_clone.csv`,
  `random_relation_controls.csv`, `candidate_diamonds.json`,
  `source_oracle_certificate.json`, and `bare_ufd_control.json`.
- Source-separated evaluation: `modulus_census.csv`,
  `cross_modulus_diamonds.json`, `stratum_controls.csv`,
  `static_selector_firewall.csv`, `trace_class_diagnostics.csv`,
  `fredholm_ownership.json`, and `evaluation.json`.
- Tests/analysis: `test_report.json`, `summary.json`, and `analysis.json`.

CSV files are UTF-8, LF-only, with one header and one terminal newline. JSON
uses sorted keys, two-space indentation, and one terminal newline.

## Exact finite census

Expected rows are 191 candidate/evaluated moduli, 191 matched transports, 48
random relation controls, 31 diamonds, 191 stratum rows, 191 selector rows,
and ten finite trace-norm diagnostic rows. Expected arithmetic strata are 43
prime, 14 prime-power composite, and 134 mixed-composite moduli. Exact tests
must pass `13/13`.

Each matched row certifies all `n^2` additions, all `n^2` multiplications, and
both projective edges at every state. Hashes keep the serialized ledger small;
the independent evaluator reconstructs every table entry and edge rather
than trusting candidate booleans.

## Metadata and complete-tree gate

Six deterministic metadata files precede the integrity output:
`double_run_certificate.json`, `environment_lock.json`,
`run_parameters.json`, `research_lock.json`,
`prototype_equivalence.json`, and `artifact_inventory.json`.
`integrity_audit.json` is the 23rd non-ledger result artifact.
`SHA256SUMS.txt` hashes eight Python sources and those 23 artifacts: 31
entries total.

Inventory comparison excludes `integrity_audit.json` and `SHA256SUMS.txt`
from both actual and expected names. Thus the audit is an idempotent
final-state gate and must exit zero on the complete frozen tree. Cache
directories, CRLF, control bytes, timestamps, missing terminal newlines, and
surplus EOF blank lines are forbidden.
