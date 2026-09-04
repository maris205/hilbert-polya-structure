# Code map

- `c369_s4_frobenius_producer.py`: pure-Python modular polynomial powering,
  gcd classification, exact orbit ledgers, and canonical evidence.
- `c369_s4_frobenius_checker.py`: independent low-level SymPy finite-field
  factorization of every prime row; it never imports the producer.
- `c369_s4_frobenius_sympy_crosscheck.py`: exact algebra, group classes,
  permutation matrices, determinant/logarithm, and boundary checks.
- `c369_s4_frobenius_replay.py`: two isolated byte-identical producer runs.
- `c369_s4_frobenius_mutation.py`: repaired-hash semantic and parser attacks.
- `c369_release_manifest.py`: full evidence, test, PDF, report, and file-ledger
  closure.

All executable lanes refuse optimized Python because assertions and schema
checks must not be weakened.
