# Code map

- `c296_hard_rod_producer.py`: deterministic exact scenarios, pair
  coincidences, event blocks, shape signatures, stabilizers, and returns.
- `c296_hard_rod_checker.py`: producer-independent reconstruction with strict
  duplicate-rejecting JSON/YAML and exact recursive contracts.
- `c296_hard_rod_sympy_crosscheck.py`: cyclic-start, invariant, CRT, irrational,
  and quotient-return identities.
- `c296_hard_rod_replay.py`: two isolated byte-replay builds.
- `c296_hard_rod_mutation.py`: repaired-hash and raw duplicate-key attacks.
- `c296_release_manifest.py`: deterministic three-round PDF and 27-payload
  closed-world release gate.

All commands are standard-library Python except for PyYAML and SymPy.  They do
not import one another's computational routines.
