# C165 exact-code contract

Run from the package root:

```bash
python code/c165_margolus_producer.py
python code/c165_margolus_checker.py
python code/c165_sympy_crosscheck.py
python code/c165_replay.py
python code/c165_mutation.py
python code/c165_release_manifest.py
```

- `c165_margolus_producer.py` constructs the canonical exact evidence from
  the two staggered swap layers.  Its finite state enumeration is a sentinel,
  not the authority for the all-parameter proof.
- `c165_margolus_checker.py` imports no producer code.  It independently
  reconstructs both layers, their composition, the four-letter pairing,
  fixed and exact periods, reflection, bounds, determinant factors, schema,
  route tuple, and scope closure.
- `c165_sympy_crosscheck.py` separately rebuilds site and Koopman permutation
  characteristic polynomials, Moebius inversion, trace-log coefficients,
  and reversibility.
- `c165_replay.py` regenerates evidence in a temporary directory and demands
  canonical byte equality.
- `c165_mutation.py` repairs the payload hash after each semantic mutation,
  requires all 57 such cases to fail, and separately rejects a stale hash.
- `c165_release_manifest.py` records all 27 payload files and excludes itself
  and transient build/cache artifacts.

No script reads target prime or zero tables or authorizes Route B.
