# C156 code

- `c156_primary_module_producer.py`: exact matrix, cocycle, CRT-primary, and
  histogram evidence.
- `c156_primary_module_checker.py`: implementation-independent full checker;
  `--quick` is reserved for hostile semantic tests.
- `c156_sympy_crosscheck.py`: symbolic polarization, Smith/Hermite, local
  histogram, and parity-lemma path.
- `c156_replay.py`: fresh-path byte replay.
- `c156_mutation.py`: repaired-hash semantic mutations and stale-hash control.
- `c156_release_manifest.py`: self-excluded content-addressed release ledger.

All arithmetic used for claims is integer or exact rational arithmetic.
