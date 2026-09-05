# Reproduction
Python 3 with requirements.txt; LuaLaTeX with TeX Gyre Pagella, TeX Gyre Pagella Math, Droid Sans Fallback. Epoch 1788566400. Executable audit needs no network.

From the package directory:

    python -B code/c386_szego_producer.py
    python -B code/c386_szego_checker.py
    python -B code/c386_szego_sympy_crosscheck.py
    python -B code/c386_szego_replay.py
    python -B code/c386_szego_mutation.py
    python -B -m unittest tests/test_c386_smoke.py
    python -B code/c386_release_manifest.py --build-pdfs
    python -B code/c386_release_manifest.py --write
    python -B code/c386_release_manifest.py

The final command rebuilds three revisions twice and reruns every lane. Write mode first enforces the fixed raw YAML hash with independent strict parsing. Named generated outputs remain within the package. The manifest excludes itself and includes every other payload file.

Prose/review judgments are auditable, not byte-reproducible across models. JSON and frozen-environment PDFs are deterministic.
