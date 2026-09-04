# Code lanes

- `c376_flat_magnetic_torus_producer.py`: canonical exact JSON producer.
- `c376_flat_magnetic_torus_checker.py`: importing-independent, fail-closed reconstruction.
- `c376_flat_magnetic_torus_sympy_crosscheck.py`: independent symbolic mechanics, signed magnetic-translation, zero-field boundary, ladder, heat, zeta, and revival identities.
- `c376_flat_magnetic_torus_replay.py`: isolated byte-for-byte replay.
- `c376_flat_magnetic_torus_mutation.py`: repaired-hash semantic and parser attacks.
- `c376_release_manifest.py`: full release and PDF gate plus self-excluded manifest.

All scripts refuse `python -O` and `python -OO`, because assertions are part of the validation contract.
