# Code lanes

- `c350_schnakenberg_producer.py`: canonical exact evidence producer.
- `c350_schnakenberg_checker.py`: producer-independent strict checker.
- `c350_schnakenberg_sympy_crosscheck.py`: independent symbolic identities.
- `c350_schnakenberg_replay.py`: two-directory byte replay.
- `c350_schnakenberg_mutation.py`: repaired-hash and parser attacks.
- `c350_release_manifest.py`: all-lane, PDF, and 27-payload release gate.

Every executable refuses optimized Python.  The checker does not import the
producer.  Generated evidence is finite and is not a proof of the continuum
theorem.
