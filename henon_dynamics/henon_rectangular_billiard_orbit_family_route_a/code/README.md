# C147 exact code

- `c147_billiard_producer.py` builds the canonical 979-direction ledger.
- `c147_billiard_checker.py` independently reconstructs every row, count,
  collision group, minimality range, aspect control, and scope flag.
- `c147_sympy_crosscheck.py` independently checks symbolic claims.
- `c147_replay.py` demands byte-identical producer replay.
- `c147_mutation.py` runs repaired-hash semantic mutations and a stale hash.
- `c147_release_manifest.py` closes 27 payload files while excluding itself
  and transient LaTeX files.

Calculations are exact integer or symbolic operations and use no network or
target data.
