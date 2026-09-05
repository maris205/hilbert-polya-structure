# Reproducibility

Run from this package with Python 3 and the pinned requirements. The LaTeX
engine is LuaLaTeX with TeX Gyre Pagella text/math and Droid Sans Fallback CJK.
Poppler supplies PDF text, font and raster audits. Epoch is 1788566400.

```bash
python -B code/c388_algebraic_producer.py
python -B code/c388_algebraic_checker.py
python -B code/c388_algebraic_sympy_crosscheck.py
python -B code/c388_algebraic_replay.py
python -B code/c388_algebraic_mutation.py
python -B -m unittest discover -s tests
python -B code/c388_release_manifest.py --build-pdfs
python -B code/c388_release_manifest.py --write
python -B code/c388_release_manifest.py
```

The producer emits deterministic source certificates. The checker never
imports the producer. Every release, including write mode, reruns all lanes,
strict raw and parsed YAML, exact file membership, and fresh double builds of
all three substantively different paper revisions. The manifest excludes
only itself. Final main.pdf equals round two byte for byte.

Source and evidence hashes may change only through an explicit rebuilt
release. Optimized Python is refused by each release-lane script. Unchanged
floating outputs are controls, not exact proofs. The source-page structural
preflight had an unavailable dependency; this advisory is retained separately
from the actual successful raster inspection.
