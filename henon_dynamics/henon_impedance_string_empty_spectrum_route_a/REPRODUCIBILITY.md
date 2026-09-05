# Reproduction contract

Run from any working directory with Python 3, mpmath 1.3.0, SymPy 1.14.0
and PyYAML 6.0.2. Scripts locate their package by __file__.
From the package root:

```sh
python -B code/c396_producer.py
python -B code/c396_checker.py
python -B code/c396_sympy_crosscheck.py
python -B code/c396_replay.py
python -B code/c396_mutation.py
python -B -m unittest tests/test_c396_smoke.py
python -B code/c396_release_manifest.py --build-pdfs
python -B code/c396_release_manifest.py --write
python -B code/c396_release_manifest.py
```

Release gates the exact raw and independently parsed YAML before any build or
write. It also rejects all symlinks/unlisted physical files and rehashes the
live repository evaluator against the frozen SHA; the checker rehashes it
independently. No __pycache__ payload is exempt from membership. Date is a
quoted string; duplicate/alias/anchor/merge tokens are refused.
All six scripts reject both -O and -OO explicitly; twelve invocations are
actually tested, including the release script. Repaired payload hashes do not
replace field semantics or exact Boolean types.

LuaLaTeX, TeX Gyre Pagella/Math, Droid Sans Fallback, pdfinfo, pdffonts,
pdftotext and pdftoppm are used. Each draft is built in two fresh directories,
with two passes per directory. Epoch 1788566400; optional PDF metadata is
suppressed, and only transient build paths are normalized in retained logs.
Raw settled build logs have the .txt extension and belong to the manifest.
The final PDF equals round two byte-for-byte.

Only deterministic outputs promise identical bytes. Prose and single-family
internal judgments are retained artifacts, not deterministic-generation
claims. All visual review receipts distinguish rendering from actual viewing.
