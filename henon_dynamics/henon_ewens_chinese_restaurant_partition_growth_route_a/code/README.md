# Verification code

- `c353_ewens_crp_producer.py`: canonical exact evidence producer.
- `c353_ewens_crp_checker.py`: independent reconstruction and strict parsers.
- `c353_ewens_crp_sympy_crosscheck.py`: Stirling, PGF, factorial-moment, and boundary identities.
- `c353_ewens_crp_replay.py`: two-directory byte replay.
- `c353_ewens_crp_mutation.py`: repaired-hash semantic and parser attacks.
- `c353_release_manifest.py`: full 27-payload and PDF release gate.

All executables explicitly refuse optimized Python because scientific assertions must remain active.
