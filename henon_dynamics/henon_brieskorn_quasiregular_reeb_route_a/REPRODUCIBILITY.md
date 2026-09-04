# Reproducibility

Run from the package root using ordinary nonoptimized Python:

```bash
python -B code/c370_brieskorn_reeb_producer.py
python -B code/c370_brieskorn_reeb_checker.py
python -B code/c370_brieskorn_reeb_sympy_crosscheck.py
python -B code/c370_brieskorn_reeb_replay.py
python -B code/c370_brieskorn_reeb_mutation.py
python -B -m unittest tests/test_c370_smoke.py
python -B code/c370_release_manifest.py --build-pdfs
python -B code/c370_release_manifest.py --write
python -B code/c370_release_manifest.py
```

Install Python dependencies from `requirements.txt`. The PDF lane additionally
requires LuaLaTeX, `pdfinfo`, `pdffonts`, `pdftotext`, and `pdftoppm`.

The producer streams every fixed-time cell into canonical SHA-256 ledgers and
stores exact row summaries. The checker imports no producer code and rebuilds
all 5,469,178 cells. The SymPy lane independently checks contact normalization,
the tangent identities, rotation determinant, lcm/denominator facts, count
identity, and principal index identity. Replay builds two isolated byte copies.
Mutation attacks repair inner hashes before rejection.

The release gate refuses optimized Python, strictly parses JSON and YAML,
locks evaluator bytes and semantics, builds each conditional manuscript twice
under epoch `1788480000`, audits warnings, fonts, extracted text and page
rasters, and closes a self-excluding 35-payload manifest.
