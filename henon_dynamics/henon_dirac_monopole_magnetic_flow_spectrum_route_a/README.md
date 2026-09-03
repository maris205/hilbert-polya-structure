# HCS-C331 — Dirac-monopole magnetic flow and spectrum

This package proves the conserved Poincaré vector, every magnetic small circle and its least period, Chern quantization, the fixed-curvature gauge-equivalence bridge, the Friedrichs/essentially-self-adjoint operator realization, the complete monopole-Laplacian spectrum and multiplicities, heat trace, charge reversal, and all frozen boundaries.

Route-A tuple:

`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`

Overall verdict: `ROUTE_A_REJECTED`; Route B remains locked under `NO_BAD_EULER_OR_ROOT_NUMBER`.

Run:

```bash
python3 -B code/c331_dirac_monopole_producer.py
python3 -B code/c331_dirac_monopole_checker.py
python3 -B code/c331_dirac_monopole_sympy_crosscheck.py
python3 -B code/c331_dirac_monopole_replay.py
python3 -B code/c331_dirac_monopole_mutation.py
python3 -B code/c331_release_manifest.py
```

The package has 28 physical files and 27 self-excluding manifest payloads.
