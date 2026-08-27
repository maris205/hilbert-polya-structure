# C202 executable paths

- `c202_fisher_kpp_producer.py`: exact/high-precision deterministic ledger;
- `c202_fisher_kpp_checker.py`: producer-independent Fraction/Decimal checker
  with recursive exact-schema closure;
- `c202_fisher_kpp_sympy_crosscheck.py`: separate symbolic reconstruction;
- `c202_fisher_kpp_replay.py`: isolated byte replay;
- `c202_fisher_kpp_mutation.py`: repaired-hash, unknown-key and stale-hash
  hostile tests;
- `c202_release_manifest.py`: 27-payload content-addressed release closure.

The code validates formulas and artifacts.  It is not a numerical proof of
continuous traveling-wave existence and claims no independent peer review.
