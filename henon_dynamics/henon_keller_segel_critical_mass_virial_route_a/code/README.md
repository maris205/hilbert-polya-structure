# C363 executable lanes

Run from the package root:

```bash
python -B code/c363_keller_segel_producer.py
python -B code/c363_keller_segel_checker.py
python -B code/c363_keller_segel_sympy_crosscheck.py
python -B code/c363_keller_segel_replay.py
python -B code/c363_keller_segel_mutation.py
python -B code/c363_release_manifest.py
```

The producer writes canonical evidence bound to strict YAML.  The checker
independently reconstructs all rows and imports no producer module.  The
symbolic lane derives 17 identities; replay uses two isolated directories;
mutation repairs hashes after semantic corruption and attacks both parsers.
Every executable refuses optimized Python.
