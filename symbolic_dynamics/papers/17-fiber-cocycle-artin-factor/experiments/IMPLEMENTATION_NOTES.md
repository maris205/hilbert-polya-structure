# SD-C19 Implementation Notes

## Reproduction

From this paper directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python experiments/run_sdc19_exact_suite.py --verify-byte-determinism
```

The orchestrator generates exact results, analyzes them, runs all 14 tests,
checks JSON parsing and CSV LF endings, requires a cache-clean tree, compares
the scientific files against the frozen prototype after newline normalization
when it is available, writes
`results/SHA256SUMS.txt`, verifies the ledger, and repeats the entire run.

## Script boundary

- `code/sdc19_fiber_cocycle_artin_core.py`: exact algebra, primitive recurrence,
  naturality enumeration, and controls.
- `code/sdc19_fiber_cocycle_artin_experiment.py`: frozen grids and raw outputs.
- `code/analyze_sdc19_fiber_cocycle_artin_results.py`: comparison tables and
  claim-facing aggregates.
- `code/test_sdc19_fiber_cocycle_artin_experiment.py`: 14 exact unit tests.
- `code/run_sdc19_fiber_cocycle_artin_tests.py`: deterministic test JSON.
- `code/audit_sdc19_artifact_integrity.py`: parse/LF/cache/diff checks.
- `code/freeze_sdc19_fiber_cocycle_artin_artifacts.py`: SHA generation/check.

## Exactness and conventions

Every theorem certificate uses integers, rational numbers, sparse formal
polynomials, or exact SymPy matrices. CSV writers explicitly use LF. JSON keys
are sorted. Results contain no timestamp or elapsed-time field, so consecutive
runs are byte-identical on the recorded Python/SymPy environment.

`D_reg` is the determinant of the whole regular extension. `D_plus` and
`D_minus` are its isotypic block determinants. The positive “no mixed local
factor” statement is not promoted to an absence of mixed coefficients or
primitive lifts.

The `base_necklace_q_distribution_json` column groups base primitive necklaces
by lift multiplier; lifted-cycle multiplicities are reported separately.

## Data firewall

No network request, external dataset, target-zero table, zero fitting, or
target-derived parameter is used. The 16 seeds only generate exact rational or
shuffle controls.
