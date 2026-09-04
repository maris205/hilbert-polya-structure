# C364 executable lanes

- `c364_gauss_reduction_producer.py`: canonical exact evidence producer.
- `c364_gauss_reduction_checker.py`: producer-independent form-coefficient
  enumeration and strict schema checker with recursive JSON leaf-type locking.
- `c364_gauss_reduction_sympy_crosscheck.py`: symbolic transformation, stabilizer, multiplier, trace, and cyclic-determinant identities.
- `c364_gauss_reduction_replay.py`: two isolated byte reproductions checked independently.
- `c364_gauss_reduction_mutation.py`: repaired-hash JSON/YAML hostile attacks,
  including explicit bool/int/integral-float collisions, and stale-hash
  control.
- `c364_release_manifest.py`: PDF, lane, source, strict-checker, and exact
  27-payload self-excluding release gate.

Every executable refuses optimized Python. Run from the package root or repository root; no network access is used.
