# HCS-C376: flat magnetic torus Landau closure

This independent theorem package treats one charged particle on a rectangular flat two-torus in a nonzero constant magnetic field. It proves, in one fixed physical normalization, the complete clean classical return theorem, the sharp integral-flux condition, the Bochner Landau ladder and multiplicity, finite magnetic translations, heat trace, Hurwitz spectral zeta, zeta determinant, two least revival times, and all singular boundary faces.

The exact Route-A tuple is `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)` and the overall verdict is `ROUTE_A_REJECTED`. First-Chern integrality is topological, not arithmetic provenance. Route B is not invoked. The scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python -B code/c376_flat_magnetic_torus_producer.py
python -B code/c376_flat_magnetic_torus_checker.py
python -B code/c376_flat_magnetic_torus_sympy_crosscheck.py
python -B code/c376_flat_magnetic_torus_replay.py
python -B code/c376_flat_magnetic_torus_mutation.py
python -B -m unittest tests/test_c376_smoke.py
python -B code/c376_release_manifest.py --build-pdfs
python -B code/c376_release_manifest.py --write
python -B code/c376_release_manifest.py
```

`paper/main.pdf` is the final round-two paper. The other two PDFs are frozen, substantive intermediate papers rather than cosmetic snapshots.
