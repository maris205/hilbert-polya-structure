# HCS-C280 — Jeffery–Bretherton planar-orientation atlas

This package proves the complete projective dynamics of a passive
axisymmetric spheroid in an arbitrary steady incompressible planar linear
flow.  The nonlinear director equation on `RP2` is exactly the
projectivization of one traceless `2 x 2` matrix exponential.  The sign of a
single invariant then closes every elliptic, hyperbolic, nilpotent, identity,
strobe, simple-shear, and aspect-ratio boundary.

For `r=1`, the retained `RP2` state is explicitly a marked material director;
an unmarked sphere has no intrinsic shape axis.  Nonzero-shear period formulas
apply to equatorial directors and nonvertical oriented vectors, while the
vertical vector is fixed.

The retained result is an all-parameter source theorem, not a finite grid
report.  The evidence file contains 625 exact parameter cells, 320
high-precision orbit cells, 10 shear-period cells, five strobe cells, and six
boundary cells.  A producer-independent checker reconstructs them without
importing producer code and enforces each exact orbit/shear/strobe key set and
boundary meaning; SymPy, fresh-path replay, and repaired-hash mutations provide
separate gates.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/c280_jeffery_producer.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c280_jeffery_checker.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c280_jeffery_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c280_jeffery_replay.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c280_jeffery_mutation.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c280_release_manifest.py
```

Route-A verdict:
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, `ROUTE_A_REJECTED`.
The scope literal is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is not authorized.
