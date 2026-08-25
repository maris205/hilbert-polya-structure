# C167 code

- `c167_rectangle_producer.py` writes the canonical evidence.
- `c167_rectangle_checker.py` independently reconstructs the exact fibres,
  branch constants, schemas, and source locks.
- `c167_sympy_crosscheck.py` performs separate symbolic collision and
  principal-branch checks.
- `c167_replay.py` requires byte-identical deterministic replay.
- `c167_mutation.py` requires repaired-hash semantic mutations and a stale
  payload-hash control to be rejected.
- `c167_release_manifest.py` closes the exact 27-file payload ledger.

Run all scripts from the repository root with Python 3.  No external dataset
is used.
