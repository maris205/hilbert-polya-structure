# Code map

- `c267_wannier_producer.py`: deterministic 90-digit receipt producer.
- `c267_wannier_checker.py`: independent phase/PDE/eigen/shell checker; imports no producer code.
- `c267_wannier_sympy_crosscheck.py`: symbolic convention and identity checks.
- `c267_wannier_replay.py`: byte-for-byte evidence replay.
- `c267_wannier_mutation.py`: repaired-hash hostile mutation suite.
- `c267_release_manifest.py`: full release, PDF, command, and hash closure.

All scripts use only the finite receipt as regression evidence.  The infinite-dimensional proof is in
`THEOREM_PACKAGE.md` and `paper/main.tex`.
