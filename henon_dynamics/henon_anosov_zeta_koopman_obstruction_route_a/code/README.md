# Exact code — C125

Run from the package root in this order:

```bash
python code/c125_anosov_producer.py
python code/c125_anosov_checker.py
python code/c125_sympy_crosscheck.py
python code/c125_replay.py
python code/c125_mutation.py
python code/c125_release_manifest.py
```

The producer uses integer matrix arithmetic, an exact Lucas recurrence,
Möbius inversion, and exhaustive finite wrap-around controls.  The checker
imports no producer code and reconstructs the entire JSON object.  SymPy
independently checks the matrix powers, zeta logarithm, primitive counts,
Fourier action, parabolic control, and cyclic-aliasing tables.  The manifest
must run only after the final PDF, all three round snapshots, compile report,
and package-local Route-A YAML exist.
