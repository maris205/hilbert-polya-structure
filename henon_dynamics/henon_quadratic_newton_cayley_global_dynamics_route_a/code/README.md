# C257 exact verification code

- `c257_newton_producer.py`: writes the canonical exact evidence, including
  periods $1\ldots16$ and root orders $1\ldots128$.
- `c257_newton_checker.py`: producer-independent schema and semantic checker.
- `c257_newton_sympy_crosscheck.py`: reconstructs conjugacy, errors,
  multipliers, boundary map, and zeta coefficients symbolically.
- `c257_newton_replay.py`: regenerates evidence in a clean process and compares
  bytes.
- `c257_newton_mutation.py`: repaired-hash hostile mutation suite.
- `c257_release_manifest.py`: reruns all gates and hashes the closed release.

All scripts are deterministic and require no prime or target-zero table.
