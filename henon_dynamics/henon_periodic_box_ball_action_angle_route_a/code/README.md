# C182 deterministic code

- `c182_periodic_bbs_producer.py` constructs the canonical all-sector regression evidence with exact integer algebra.
- `c182_periodic_bbs_checker.py` imports no producer code.  It rebuilds the formulas with rational elimination and independently enumerates the actual periodic carrier on every binary state through `L=9`.
- `c182_sympy_crosscheck.py` reconstructs determinants, Smith forms, translation orders, Möbius inversion, primitive points, and finite cycle determinants with SymPy.
- `c182_replay.py` requires a byte-for-byte producer replay.
- `c182_mutation.py` requires rejection of 64 repaired-hash semantic mutations and one stale-hash mutation.
- `c182_release_manifest.py` closes exactly 27 payload files plus the self-excluded manifest.

All scripts use exact arithmetic.  The finite ledger is a deterministic regression sentinel for the all-parameter theorem, not its proof.
