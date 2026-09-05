# Reproducibility

From this package directory:

```bash
python -B code/c382_cm_producer.py
python -B code/c382_cm_checker.py
python -B code/c382_cm_sympy_crosscheck.py
python -B code/c382_cm_replay.py
python -B code/c382_cm_mutation.py
python -B -m unittest tests/test_c382_smoke.py
python -B code/c382_release_manifest.py --write --build-pdfs
python -B code/c382_release_manifest.py
```

Python3, SymPy, PyYAML, LuaLaTeX, Latin Modern and Droid Sans Fallback fonts, and Poppler are required. No network or GPU is used at reproduction time. Source epoch1788566400 and UTC are frozen. Every arithmetic value is exact. Compilers create artifacts in fresh temporary directories; generated files are copied only into this owned package.
