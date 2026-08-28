# C215 code

`c215_kingman_producer.py` emits the canonical all-`n<=12` regression payload.
The checker is producer-independent: it reconstructs rates, partial fractions,
semigroup identities, Bell numbers, MRCA/tree-length moments and the exact
maximum-of-exponentials CDF while recursively rejecting unknown keys.
`c215_kingman_sympy_crosscheck.py` audits rational transforms, derivatives and
the beta-integral.  Replay checks clean-process bytes; the mutation harness
tests repaired hashes, stale hashes, semantic fields and unknown keys; the
release script closes the 28-file ledger and three-PDF build.

Only integer/rational source-local sentinels are used.  No prime/zero data or
target-fitting routine is read.
