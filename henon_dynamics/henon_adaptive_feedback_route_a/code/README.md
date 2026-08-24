# C122 code

Run, in order:

```bash
python3 code/c122_adaptive_producer.py
python3 code/c122_adaptive_checker.py
python3 code/c122_sympy_crosscheck.py
python3 code/c122_replay.py
python3 code/c122_mutation.py
python3 code/c122_release_manifest.py
```

The checker and SymPy reconstruction do not import the producer.  All model
arithmetic is exact in `Q(sqrt(5))`; no randomness or tolerance is used.
