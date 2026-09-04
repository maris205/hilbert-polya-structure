# Reproducibility

From this package directory run:

```bash
python -B code/c374_kummer_arboreal_producer.py
python -B code/c374_kummer_arboreal_checker.py
python -B code/c374_kummer_arboreal_sympy_crosscheck.py
python -B code/c374_kummer_arboreal_replay.py
python -B code/c374_kummer_arboreal_mutation.py
python -B -m unittest tests/test_c374_smoke.py
python -B code/c374_release_manifest.py --write --build-pdfs
python -B code/c374_release_manifest.py
```

The producer and checker share no imports.  The release gate runs both in
isolated processes, rejects optimized Python, strictly parses JSON and
YAML, checks the exact payload membership, and rebuilds each PDF in two
fresh directories with `SOURCE_DATE_EPOCH=1788480000`.
It also locks the full evaluator-v0.2 schema and A0 control receipts,
requires the `A1_WEAK` exploratory verdict, verifies bilingual
abstract/keyword layering, and checks an embedded subset CJK font.
