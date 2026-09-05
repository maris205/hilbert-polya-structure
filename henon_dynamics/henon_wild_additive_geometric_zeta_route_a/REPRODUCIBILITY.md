# Reproduction

Use Python 3, SymPy, PyYAML, LuaLaTeX, Latin Modern/Droid Sans Fallback fonts and Poppler. Commands run from this package directory:

```sh
python -B code/c384_wild_producer.py
python -B code/c384_wild_checker.py
python -B code/c384_wild_sympy_crosscheck.py
python -B code/c384_wild_replay.py
python -B code/c384_wild_mutation.py
python -B -m unittest tests/test_c384_smoke.py
python -B code/c384_release_manifest.py --write --build-pdfs
python -B code/c384_release_manifest.py
```

Epoch 1788566400 and UTC are set by the release script. Each PDF round is built twice in fresh directories, with two settled LuaLaTeX passes per build. Raw settled compiler logs have .txt suffixes so Git does not ignore them. The release manifest excludes only itself and locks the exact payload set.

Default release mode performs full recomputation and fresh PDF comparisons without writing. Python -O/-OO must be refused, not used to disable validation.
