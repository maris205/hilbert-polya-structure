# Test report

Run from the package root:

```text
python3 -B code/c263_polya_producer.py
python3 -B code/c263_polya_checker.py
python3 -B code/c263_polya_sympy_crosscheck.py
python3 -B code/c263_polya_replay.py
python3 -B code/c263_polya_mutation.py
python3 -B code/c263_release_manifest.py
```

The checker is independent of the producer, all probability comparisons use
exact rational arithmetic, the symbolic pass reconstructs generic identities,
and the release gate checks the PDFs, fonts, scope flags, file closure, and
canonical hashes.
