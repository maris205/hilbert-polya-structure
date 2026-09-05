# Reproduction

From this package directory, with the declared Python requirements and
LuaLaTeX/Poppler/fonts installed:

```bash
python -B code/c385_lozi_producer.py
python -B code/c385_lozi_checker.py
python -B code/c385_lozi_sympy_crosscheck.py
python -B code/c385_lozi_replay.py
python -B code/c385_lozi_mutation.py
python -B -m unittest tests/test_c385_smoke.py
python -B code/c385_release_manifest.py --build-pdfs
python -B code/c385_release_manifest.py --write
python -B code/c385_release_manifest.py
```

The final command is nonwrite and rebuilds the evidence/PDFs in temporary
directories before checking the exact self-excluding ledger. Generative prose
is not claimed byte-reproducible. Optimized Python is refused. Frozen epoch
1788566400 applies to PDFs; raw compiler logs preserve actual tool output.
