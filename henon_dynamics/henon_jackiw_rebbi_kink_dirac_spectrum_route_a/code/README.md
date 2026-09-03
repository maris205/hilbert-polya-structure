# Verification code

- `c352_jackiw_rebbi_producer.py`: canonical exact JSON producer.
- `c352_jackiw_rebbi_checker.py`: independent strict-schema reconstruction.
- `c352_jackiw_rebbi_sympy_crosscheck.py`: factorization, Darboux, threshold, and symmetry lane.
- `c352_jackiw_rebbi_replay.py`: isolated two-directory byte replay.
- `c352_jackiw_rebbi_mutation.py`: repaired-hash and parser attacks.
- `c352_release_manifest.py`: full evidence/PDF/payload release gate.

Every executable refuses `python -O` and `python -OO`; assertions are part of the scientific contract.
