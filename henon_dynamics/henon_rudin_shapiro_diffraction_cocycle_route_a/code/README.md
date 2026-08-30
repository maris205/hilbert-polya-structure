# C248 code contract

The six scripts are intentionally small and deterministic:

* `c248_rs_producer.py` writes the sorted-key JSON evidence ledger using only
  integer arithmetic.
* `c248_rs_checker.py` reconstructs rules, words, polynomials, Laurent
  correlations, and route/scope fields without importing the producer.
* `c248_rs_sympy_crosscheck.py` expands the cocycle and correlation identities
  with exact SymPy expressions.
* `c248_rs_replay.py` performs a clean byte replay in a temporary directory.
* `c248_rs_mutation.py` runs 42 semantic/repaired-hash attacks against the
  checker.
* `c248_release_manifest.py` runs the controls and closes the 27-file payload
  ledger around the self-excluded manifest.

All scripts accept no network input and set `PYTHONDONTWRITEBYTECODE` in
subprocesses where relevant.  They never infer a target divisor, zero set,
Euler factor, root number, or Hilbert–Pólya operator.
