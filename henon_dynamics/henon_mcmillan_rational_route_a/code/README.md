# C115 code

Run from the package directory:

```bash
python code/c115_mcmillan_producer.py
python code/c115_mcmillan_checker.py
python code/c115_sympy_crosscheck.py
python code/c115_replay.py
python code/c115_mutation.py
python code/c115_release_manifest.py
```

The checker is independent of the producer.  It accepts an optional evidence
path solely so the mutation harness can require rejection of altered receipts.
The replay copies the producer to a temporary package and demands byte identity.
