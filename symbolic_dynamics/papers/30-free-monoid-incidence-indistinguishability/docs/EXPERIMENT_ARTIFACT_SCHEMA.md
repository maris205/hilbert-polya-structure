# Experiment Artifact Schema — SD-C32

## Seventeen fresh-run artifacts

The two isolated canonical runs each generate exactly these 17 files:

- JSON: `sanity`, `baseline`, `finite_controls`, `free_monoid_controls`,
  `clone_certificate`, `predicate_masks`, `analytic_ownership`, `summary`,
  `evaluation`, `test_report`, and `analysis`.
- CSV: `baseline_subset_ledger`, `finite_control_subset_ledger`,
  `free_monoid_control_ledger`, `predicate_mask_ledger`,
  `marker_ownership_ledger`, and `comparison_table`.

Every JSON file is UTF-8, sorted-key, two-space-indented, and newline
terminated.  Every CSV file is UTF-8, LF-only, and newline terminated.
Exact rational values are serialized as numerator, denominator, and canonical
text rather than floating-point approximations.

## Authority metadata

- `run_parameters.json` freezes cutoffs, seeds, ranks, masks, eta, marker, and
  the Route tuple.
- `environment_lock.json` freezes deterministic standard-library execution.
- `source_oracle_certificate.json` records source selection, forbidden-oracle,
  evaluator-separation, target-zero, and Route-B firewalls.
- `research_lock.json` records the frozen research-package and prototype
  hashes and the expected fresh-run aggregate.
- `double_run_certificate.json` records the hashes of the 17 fresh artifacts
  from both isolated runs.
- `integrity_audit.json` verifies Route-A v0.2, exact censuses, source
  separation, clone equality, LF/control/cache/EOF hygiene, and all scientific
  gates.
- `SHA256SUMS.txt` contains exactly 31 hashes: eight Python source files and 23
  result/metadata artifacts, excluding the ledger itself.

## Exact census

The expected canonical row counts are 241 baseline subsets, 118 finite-control
subsets, 45 free/UFD inventories, 186 predicate masks, and 165 markers.
The independent evaluator must pass 1,616 of 1,616 checks and the unit suite
must pass 28 of 28 tests.
