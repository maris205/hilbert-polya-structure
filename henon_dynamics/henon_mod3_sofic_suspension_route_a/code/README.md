# C140 executable audit

Run, in order:

```bash
python3 code/c140_sofic_producer.py
python3 code/c140_sofic_checker.py
python3 code/c140_sympy_crosscheck.py
python3 code/c140_replay.py
python3 code/c140_mutation.py
python3 code/c140_release_manifest.py
```

The checker and SymPy reconstruction import no producer module.  They keep the
three-state cover trace distinct from the intrinsic label fixed-point trace.
The finite period-15 prefix is a sentinel, not the proof of the all-period
exceptional-orbit correction.
