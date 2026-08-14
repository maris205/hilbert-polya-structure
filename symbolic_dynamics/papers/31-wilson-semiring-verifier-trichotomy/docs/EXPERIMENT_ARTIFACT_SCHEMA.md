# Experiment Artifact Schema — SD-C33

## Sixteen fresh-run artifacts

Fourteen legacy artifacts reproduce the frozen cutoff-4096 prototype. The
seven JSON files are byte-identical; the seven CSV files have identical
parsed rows after the unique CRLF-to-LF authority canonicalization:

- CSV: `wilson_ledger`, `composite_controls`,
  `fermat_pseudoprime_controls`, `bare_ufd_addition_failure`,
  `matched_semiring_clone`, `entropy_budget_dilution`, and
  `formal_trace_ledger`;
- JSON: `semiring_controls`, `random_operation_controls`,
  `marker_change_certificate`, `universal_wrapper_controls`,
  `source_oracle_certificate`, `test_report`, and `summary`.

Authority adds `evaluation.json`, independently recomputed without importing
candidate code, and `analysis.json`, organized as
Observation–Interpretation–Implication–Next step.

## Exact census

Expected rows are 4,095 Wilson candidates, 3,531 composite controls, 13
base-2 pseudoprimes, 144 bare-addition pairs, 169 matched-clone operations,
1,692 dilution rows, and 16 formal trace orders. JSON controls contain seven
named semirings, 33 operation-table records, two marker comparisons, and five
universal wrappers. Legacy tests must pass `18/18`.

## Authority metadata and freeze

`double_run_certificate.json`, `environment_lock.json`,
`run_parameters.json`, `research_lock.json`,
`prototype_equivalence.json`, `artifact_inventory.json`, and
`integrity_audit.json` supply deterministic provenance and hygiene evidence.
`SHA256SUMS.txt` hashes exactly eight Python sources and 23 result/metadata
artifacts, excluding the ledger itself: 31 entries total.

All JSON is sorted-key UTF-8 with one terminal LF. All CSV is UTF-8 LF-only.
No cache, CRLF, control byte, timestamped result, or surplus EOF blank line is
permitted.

Inventory comparison excludes the self-generated `integrity_audit.json` and
`SHA256SUMS.txt` symmetrically from actual and expected names. The auditor is
therefore an idempotent final-state gate: running it on the complete frozen
tree must return zero and reproduce `status: PASS`.
