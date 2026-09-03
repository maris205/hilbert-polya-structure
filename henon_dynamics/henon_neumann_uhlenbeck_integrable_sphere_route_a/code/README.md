# Reproduction commands

Run from the package root with `PYTHONDONTWRITEBYTECODE=1`:

```text
python3 -B code/c349_neumann_producer.py
python3 -B code/c349_neumann_checker.py
python3 -B code/c349_neumann_sympy_crosscheck.py
python3 -B code/c349_neumann_replay.py
python3 -B code/c349_neumann_mutation.py
python3 -B code/c349_release_manifest.py --write --build-pdfs
python3 -B code/c349_release_manifest.py
```

Repeat the final no-write command to certify stability.  Every entry point
refuses optimized Python. The checker is producer-independent.
