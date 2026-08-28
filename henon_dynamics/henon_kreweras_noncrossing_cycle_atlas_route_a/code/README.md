# C209 code contract

| Script | Role | Independence boundary |
|---|---|---|
| `c209_kreweras_producer.py` | closed-form JSON producer (`n<=24`) | source formula implementation |
| `c209_kreweras_checker.py` | schema, formula, coordinate, and direct `NC(n)` checker (`n<=8`) | no producer import; independent set-partition implementation |
| `c209_sympy_crosscheck.py` | exact q-Catalan/cyclotomic and period/spectrum audit | SymPy implementation, no producer/checker import |
| `c209_replay.py` | byte-for-byte producer replay | isolated temporary output |
| `c209_mutation.py` | repaired/stale hash tamper tests | subprocess checker calls |
| `c209_release_manifest.py` | file/PDF/hash closure | self-excludes manifest and build sidecars |

All scripts use integer arithmetic.  The only optional dependency is SymPy for
the independent symbolic audit; `pdfinfo` and `lualatex` are needed for the
release build.
