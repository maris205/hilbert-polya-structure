# Verification code

- `c294_three_disk_producer.py` creates canonical exact JSON evidence.
- `c294_three_disk_checker.py` independently rebuilds word, Möbius,
  geometry, optical, scope, YAML, and document contracts; it imports no
  producer code.
- `c294_three_disk_sympy_crosscheck.py` verifies matrix, determinant, series,
  chamber, Möbius, and symmetric-orbit identities symbolically.
- `c294_three_disk_replay.py` reproduces evidence twice and requires byte
  equality with the archived JSON.
- `c294_three_disk_mutation.py` attacks repaired-hash semantic fields and raw
  duplicate/missing/unknown JSON/YAML structure.
- `c294_release_manifest.py` runs every lane, performs six fresh LuaLaTeX
  builds, checks logs/fonts/text/pages/hashes, and closes the 27-payload / 28-
  physical-file ledger.

All commands are CPU-only.  Run them from any directory with Python 3,
PyYAML, mpmath, SymPy, LuaLaTeX, and Poppler tools installed.
