# Code

- `c270_heisenberg_producer.py`: deterministic 90-digit evidence producer with
  an explicit per-row numeric-field schema.
- `c270_heisenberg_checker.py`: independent reconstruction of all 876 rows and
  independent schema-based numeric-cell recount.
- `c270_heisenberg_sympy_crosscheck.py`: symbolic bracket, flow, Jacobian, and
  distance derivations.
- `c270_heisenberg_replay.py`: byte-for-byte producer replay.
- `c270_heisenberg_mutation.py`: repaired-hash hostile mutations.
- `c270_release_manifest.py`: full 27-payload/28-file release closure.

Run scripts with `PYTHONDONTWRITEBYTECODE=1 python -B ...` from the package root.
