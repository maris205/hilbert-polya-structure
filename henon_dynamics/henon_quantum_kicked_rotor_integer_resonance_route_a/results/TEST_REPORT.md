# C337 test report

All commands are run with `PYTHONDONTWRITEBYTECODE=1`.

- `python3 -B code/c337_kicked_rotor_producer.py`: PASS; deterministic evidence SHA-256 `7395dd85f963d8085027133380044839ddc80c2423603fd49dd1df8154e3ecc8`.
- `python3 -B code/c337_kicked_rotor_checker.py`: PASS; 47,531 producer-independent assertions and 70 evaluator leaves.
- `python3 -B code/c337_kicked_rotor_sympy_crosscheck.py`: PASS; 13,188 exact symbolic identities.
- `python3 -B code/c337_kicked_rotor_replay.py`: PASS; two isolated outputs equal the checked-in evidence byte for byte.
- `python3 -B code/c337_kicked_rotor_mutation.py`: PASS; 133/133 hostile changes rejected.
- Every Python entry point refuses `python3 -OO` before substantive work.

The release gate additionally reconstructs all three PDFs twice in fresh directories, verifies exact checked-in bytes, zero warning/layout/reference/missing-glyph matches, embedded/subset fonts, clean extracted text, per-page rasterization, exact revision tokens, the 27-payload ledger and the self-excluding evidence payload hash.
