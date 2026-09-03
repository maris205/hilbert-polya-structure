# HCS-C347 / HEN-O331 — noisy mean-field Kuramoto phase transition

This package closes one theorem-scale source-dynamics result for the identical-frequency noisy mean-field Kuramoto equation. For every (D>0), (K\geq0), it proves the global classical probability flow, the exact free-energy dissipation identity, the complete positive stationary atlas, the sharp threshold (K=2D), the uniform Fourier spectrum, and the two-term critical expansion. The result is analytic; exact finite ledgers are regression receipts only.

The Route-A tuple is

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`

and the overall verdict is `ROUTE_A_REJECTED`. The canonical scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is locked off.

## Reproduce

```bash
python -B code/c347_kuramoto_producer.py
python -B code/c347_kuramoto_checker.py
python -B code/c347_kuramoto_sympy_crosscheck.py
python -B code/c347_kuramoto_replay.py
python -B code/c347_kuramoto_mutation.py
SOURCE_DATE_EPOCH=1788393600 python -B code/c347_release_manifest.py
```

The release gate additionally rejects optimized Python, rebuilds every paper round twice in fresh directories, checks fonts/text/raster output, and verifies the exact 27-payload manifest closure.

## Boundaries

- The theorem is for identical frequencies, sinusoidal attraction, (D>0), and (K\geq0).
- It does not claim convergence of every initial density, any Hopf or time-periodic branch, disorder, delay, inertia, finite-(N) dynamics, or a (D=0) atomic classification.
- The Fourier eigenvalues are linearization data, not a target spectral model.
- No target arithmetic local data, Euler factors, root number, automorphy, target divisor, target zero match, Hilbert–Pólya operator, or Route B appears.

The reconstruction is source-local and makes no novelty or priority claim.
