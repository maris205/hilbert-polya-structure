# C278 executable certificate

Run from any directory with Python 3:

```bash
python -B code/c278_camassa_holm_producer.py
python -B code/c278_camassa_holm_checker.py
python -B code/c278_camassa_holm_sympy_crosscheck.py
python -B code/c278_camassa_holm_replay.py
python -B code/c278_camassa_holm_mutation.py
python -B code/c278_release_manifest.py
```

The checker reconstructs the identities independently and never imports the
producer.  It also freezes the complete model, proof, theorem, nonclaim,
scope, nested regression, and reference-metadata contracts.  The mutation
suite sends repaired-hash payloads through that actual checker.  Finite rows
are regression controls; the arbitrary-parameter result is carried by the
proof in `THEOREM_PACKAGE.md`.
