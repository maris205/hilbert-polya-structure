# Verification code

- `c298_grassmann_producer.py` creates canonical exact JSON evidence.
- `c298_grassmann_checker.py` independently recomputes minors, matroid support,
  gaps, projections, modes, filtrations, occupancies, Morse--Bott dimensions,
  YAML, scope, and prose sentinels without importing producer code.
- `c298_grassmann_sympy_crosscheck.py` verifies global projector, exterior-
  power, Plücker, Lyapunov, linearization, and degeneracy identities.
- `c298_grassmann_replay.py` requires two fresh evidence files to equal the
  archive byte for byte.
- `c298_grassmann_mutation.py` attacks repaired-hash JSON semantics and strict
  JSON/YAML structure.
- `c298_release_manifest.py` runs all lanes, six fresh LuaLaTeX builds, PDF
  audits, and the exact 27-payload / 28-physical-file closure.

All commands are CPU-only and may be run from any working directory.
