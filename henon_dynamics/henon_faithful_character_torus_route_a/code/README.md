# C134 code

- `c134_character_producer.py`: Laurent/group-character evidence, scaled
  geometry, traces, coefficients, permutation recovery, and controls.
- `c134_character_checker.py`: independent standard-library reconstruction;
  imports no producer code.
- `c134_sympy_crosscheck.py`: independent matrix, Laurent, Newton, Gaussian,
  and mod-five reconstruction.
- `c134_replay.py`: byte-for-byte producer replay.
- `c134_mutation.py`: 47 repaired-payload-hash semantic mutations plus one
  stale-hash mutation.
- `c134_release_manifest.py`: self-excluded 27-payload release ledger.

All mathematical receipts use exact arithmetic.  No network or external
dataset is required.
