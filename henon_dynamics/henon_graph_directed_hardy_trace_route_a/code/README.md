# C124 code

- `c124_hardy_producer.py`: deterministic exact evidence producer.
- `c124_hardy_checker.py`: independent standard-library reconstruction; it
  imports no producer code.
- `c124_sympy_crosscheck.py`: fresh symbolic reconstruction and explicit
  polynomial finite-section matrices.
- `c124_replay.py`: byte-for-byte evidence replay.
- `c124_mutation.py`: hostile mutation rejection suite.
- `c124_release_manifest.py`: content-addressed release ledger.

Every command is run from the package root.  No random seed, numerical
tolerance, web input, or external dataset is used.
