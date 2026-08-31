# Verification commands

Run from the package root with Python 3:

```bash
python3 -B code/c260_pgl2_producer.py
python3 -B code/c260_pgl2_checker.py
python3 -B code/c260_pgl2_sympy_crosscheck.py
python3 -B code/c260_pgl2_replay.py
python3 -B code/c260_pgl2_mutation.py
```

Expected sentinels are `C260_PRODUCER_PASS`, `C260 independent checker: PASS`, `C260_SYMPY_PASS`, `C260 byte replay: PASS`, and `PASS 40/40`.

The producer uses trace/determinant and finite-field algebra. The checker deliberately does not import it: it rebuilds every field, matrix representative, projective permutation, cycle list, type/order census, and canonical record hash. The quick checker is only the semantic hostile preflight; release runs the full enumeration.

After PDFs and documentation are final, close the content-addressed package with:

```bash
python3 -B code/c260_release_manifest.py
```
