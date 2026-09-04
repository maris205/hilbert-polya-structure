# Code lanes

- `c374_kummer_arboreal_producer.py`: canonical exact evidence.
- `c374_kummer_arboreal_checker.py`: independent recomputation; imports no
  producer.
- `c374_kummer_arboreal_sympy_crosscheck.py`: separate symbolic backend.
- `c374_kummer_arboreal_replay.py`: two isolated byte-identical builds.
- `c374_kummer_arboreal_mutation.py`: repaired-hash hostile tests.
- `c374_release_manifest.py`: all-lane release, PDF, and membership gate.

Every executable refuses `python -O` and `python -OO`.
