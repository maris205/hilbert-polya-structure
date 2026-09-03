# HCS-C350: Schnakenberg Neumann Turing modes

This package proves the complete **linear** diffusion-driven instability atlas
of the positive Schnakenberg equilibrium on a one-dimensional Neumann
interval.  It separates the continuous wavenumber window from the actual
finite-domain cosine modes, counts every unstable and neutral mode exactly,
and closes kinetic, equal-diffusion, double-wall, length-threshold, and
zero-diffusion boundaries.  Separate exact witnesses exercise the lower and
upper neutral walls, and spectral exhaustion is stated after complexifying
the real linearized operator.

The theorem does not assert a nonlinear patterned branch, nonlinear orbital
stability, or a global theorem for the nonlinear PDE.  Finite exact rows are
implementation receipts for the analytic proof.

The Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, the overall verdict is
`ROUTE_A_REJECTED`, Route B is false, and the fixed scope is
`NO_BAD_EULER_OR_ROOT_NUMBER`.

Run the final gate from this directory with

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c350_release_manifest.py --write
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c350_release_manifest.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c350_release_manifest.py
```
