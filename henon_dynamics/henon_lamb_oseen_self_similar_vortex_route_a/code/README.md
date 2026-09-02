# Code ledger

- `c299_lamb_oseen_producer.py` deterministically generates the 213-cell evidence file.
- `c299_lamb_oseen_checker.py` independently reconstructs every receipt and strictly parses JSON/YAML; it does not import the producer.
- `c299_lamb_oseen_sympy_crosscheck.py` checks the governing identities symbolically.
- `c299_lamb_oseen_replay.py` requires two fresh outputs to match the archived evidence byte for byte.
- `c299_lamb_oseen_mutation.py` subjects semantic values and parser boundaries to hostile mutations.
- `c299_release_manifest.py` closes the exact file ledger, builds, hashes, document claims, and evaluation semantics.

All scripts run with the Python standard library plus `mpmath`, `sympy`, and `PyYAML`.  No network access or training data is used.
