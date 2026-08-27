# C193 code

- `c193_markoff_producer.py` creates the canonical tree and bounded-scan
  evidence.
- `c193_markoff_checker.py` independently rebuilds the tree and solves the
  bounded quadratic in a different variable.
- `c193_sympy_crosscheck.py` reconstructs Vieta identities and every stored
  edge symbolically.
- `c193_replay.py` requires byte-identical isolated production.
- `c193_mutation.py` performs repaired-hash semantic attacks and a stale-hash
  control.
- `c193_release_manifest.py` closes the self-excluded 27-payload ledger.

The producer honors `C193_OUTPUT`.  All arithmetic is exact integer or SymPy
polynomial arithmetic.  The bounded census is a regression oracle and imports
no mod-prime data.
