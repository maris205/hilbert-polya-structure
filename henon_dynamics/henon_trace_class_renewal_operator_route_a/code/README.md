# C142 code

Run, in order:

```bash
python3 code/c142_renewal_producer.py
python3 code/c142_renewal_checker.py
python3 code/c142_sympy_crosscheck.py
python3 code/c142_replay.py
python3 code/c142_mutation.py
python3 code/c142_release_manifest.py
```

The checker and SymPy reconstruction import no producer module.  All reported
values use exact integer or rational arithmetic.
