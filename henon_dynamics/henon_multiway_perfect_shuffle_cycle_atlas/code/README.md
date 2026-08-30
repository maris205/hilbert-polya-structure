# C239 code

`c239_shuffle_producer.py` writes the deterministic cross-parameter receipt.
`c239_shuffle_checker.py` independently reconstructs the modular permutation,
literal packet interleave, gcd/order formulas, primitive counts and spectral
factors.  `c239_shuffle_sympy_crosscheck.py` checks congruence and polynomial
identities (including all 1,100 packet positions in the 50-grid),
`c239_shuffle_replay.py` checks byte determinism, `c239_shuffle_mutation.py`
runs 44 hostile tamper tests, and `c239_release_manifest.py` closes the
27-payload/28-physical-file manifest.

All commands use `python3 -B` and `PYTHONDONTWRITEBYTECODE=1`; no target
arithmetic data are read.
