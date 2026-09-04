# Reproducibility

Run from the package root with ordinary nonoptimized Python:

```bash
python -B code/c373_higgs_oscillator_producer.py
python -B code/c373_higgs_oscillator_checker.py
python -B code/c373_higgs_oscillator_sympy_crosscheck.py
python -B code/c373_higgs_oscillator_replay.py
python -B code/c373_higgs_oscillator_mutation.py
python -B -m unittest tests/test_c373_smoke.py
python -B code/c373_release_manifest.py --build-pdfs
python -B code/c373_release_manifest.py --write
python -B code/c373_release_manifest.py
```

Install Python dependencies from `requirements.txt`. LuaLaTeX and Poppler
utilities are required for PDF release checks. The checker imports no producer
code. The symbolic lane verifies both the abstract Jacobi ODE and direct
radial Schrödinger substitutions. The replay uses isolated output directories,
and hostile tests repair internal hashes before requiring rejection.
The source-text lane also rejects unescaped TeX spacing commands while its
mutation controls retain legal `\quad` and `\qquad` uses.

The manifest excludes itself and closes exactly 35 payloads plus one manifest.
