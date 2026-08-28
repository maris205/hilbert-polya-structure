# Executable audit

- `c222_double_integrator_producer.py` writes the canonical source-local JSON.
- `c222_double_integrator_checker.py` imports no producer and recursively
  closes the schema while reconstructing every branch and state.
- `c222_double_integrator_sympy_crosscheck.py` proves the generic algebra on
  both switching sides.
- `c222_double_integrator_replay.py` reproduces canonical bytes in a clean
  subprocess and temporary directory.
- `c222_double_integrator_mutation.py` repairs hashes after semantic/schema
  corruption, checks unknown keys, and separately tests a stale hash.
- `c222_release_manifest.py` reruns every gate and freezes exactly 27 payload
  files plus its self-excluded manifest.

Use Python with bytecode disabled (`python3 -B`).  No network or external
dataset is required.
