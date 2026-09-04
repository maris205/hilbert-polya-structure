# Reproduction

From the package root, with bytecode disabled:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/c356_qwz_producer.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c356_qwz_checker.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c356_qwz_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c356_qwz_replay.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c356_qwz_mutation.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c356_release_manifest.py
```

Maintainers regenerate the whole release with `--write --build-pdfs`. All scripts explicitly refuse optimized Python.
