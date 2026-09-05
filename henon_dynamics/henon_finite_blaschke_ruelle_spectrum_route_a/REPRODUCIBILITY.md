# Reproduce C380

From this package directory, with Python and requirements.txt plus LuaLaTeX and Poppler:

```bash
python -B code/c380_blaschke_producer.py
python -B code/c380_blaschke_checker.py
python -B code/c380_blaschke_sympy_crosscheck.py
python -B code/c380_blaschke_replay.py
python -B code/c380_blaschke_mutation.py
python -B -m unittest discover -s tests
python -B code/c380_release_manifest.py --write
python -B code/c380_release_manifest.py
```

The write release generates PDFs and reports only after the mathematical executable lanes pass. The default release is non-mutating and verifies existing bytes, reports and the exact ledger. All executables refuse -O and -OO. Frozen source epoch is 1788566400. No GPU, training, target data or network is needed for reproduction.
