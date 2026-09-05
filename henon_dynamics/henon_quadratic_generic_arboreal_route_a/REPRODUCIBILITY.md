# Reproducibility

Python 3.12.3, SymPy 1.14.0, mpmath 1.3.0, PyYAML 6.0.2;
LuaLaTeX/Poppler are required for the manuscript lanes.
Run from this package directory:

```bash
python -B code/c393_arboreal_producer.py
python -B code/c393_arboreal_checker.py
python -B code/c393_arboreal_sympy_crosscheck.py
python -B code/c393_arboreal_replay.py
python -B code/c393_arboreal_mutation.py
python -B code/c393_release_manifest.py --build-pdfs
python -B code/c393_release_manifest.py --write
python -B code/c393_release_manifest.py
```

Frozen source baseline `0c877206d202f732e21ea0b194f9c7fdf30467ee`;
fixed epoch `1788566400`. Six scripts each reject both -O and -OO.
The release manifest excludes itself and covers every physical payload.
No network is needed for reproduction; source links document prior verification.
Use the actual release receipts for PASS status, not this command list.
