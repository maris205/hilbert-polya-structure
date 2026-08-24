# C126 executable certificate

Run from this package root:

```text
python3 code/c126_chebyshev_skew_producer.py
python3 code/c126_chebyshev_skew_checker.py
python3 code/c126_sympy_crosscheck.py
python3 code/c126_replay.py
python3 code/c126_mutation.py
python3 code/c126_release_manifest.py
```

The checker imports no producer code.  The SymPy program independently
reconstructs the composition, derivative, control, and route-boundary
identities.  Replay compares canonical bytes, while the hostile suite requires
all eighteen corrupted receipts to be rejected.
