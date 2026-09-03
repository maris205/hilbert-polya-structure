# Verification code

- `c341_lamplighter_producer.py` creates canonical exact evidence.
- `c341_lamplighter_checker.py` independently reconstructs every coordinate.
- `c341_lamplighter_sympy_crosscheck.py` supplies a separate algebra system.
- `c341_lamplighter_replay.py` compares two isolated producer runs bytewise.
- `c341_lamplighter_mutation.py` runs repaired-hash hostile attacks.
- `c341_release_manifest.py` closes the 27-payload release ledger and PDFs.

Every Python entry point explicitly refuses `-O` and `-OO` execution.
