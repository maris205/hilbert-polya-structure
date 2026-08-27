# Code and reproducibility

- `c192_hyperplane_producer.py` builds the canonical exact-rational evidence.
- `c192_hyperplane_checker.py` imports no producer code and reconstructs the
  sign-vector semigroup, flats, Möbius data, matrices, sampler, and mixing rows.
- `c192_sympy_crosscheck.py` is a separate symbolic oracle for characteristic
  polynomials, determinants, traces, and eigenspace dimensions.
- `c192_replay.py` reruns the producer and requires byte identity.
- `c192_mutation.py` repairs payload hashes after semantic attacks and requires
  every attack, plus one stale-hash attack, to be rejected.
- `c192_release_manifest.py` creates the self-excluded 27-payload manifest.

All arithmetic in producer and checker uses `fractions.Fraction`.  No script
imports an arithmetic-prime table, local data, Euler factors, root numbers, or a
target divisor.  Coordinate and braid enumeration is regression only.
