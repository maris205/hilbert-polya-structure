# Reproducibility code

- `c301_fragmentation_producer.py` creates canonical exact JSON evidence using
  direct fair-bit enumeration for the one-step tables.
- `c301_fragmentation_checker.py` imports no producer code.  It constructs set
  partitions by a different recursion, recovers transitions from the refinement
  predicate, checks every formula, and enforces strict JSON/YAML contracts.
- `c301_fragmentation_sympy_crosscheck.py` independently builds rational
  matrices and verifies characteristic polynomials, determinants, squarefree
  annihilators, eigenspaces, semigroup powers, and occupancy identities.
- `c301_fragmentation_replay.py` runs the producer twice and compares both runs
  with the archive byte-for-byte.
- `c301_fragmentation_mutation.py` requires the checker to kill semantic,
  type-confusion, parser, scope, route, and formula mutations.
- `c301_release_manifest.py` performs the end-to-end closed-world release.

All scripts run with Python 3.  The checker/release additionally require
PyYAML, and the symbolic cross-check requires SymPy.  PDF audit requires
LuaLaTeX plus Poppler tools (`pdfinfo`, `pdffonts`, `pdftotext`, `pdftoppm`).
