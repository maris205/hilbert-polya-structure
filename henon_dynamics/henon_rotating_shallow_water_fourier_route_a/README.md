# HCS-C217: rotating shallow-water Fourier flow on a torus

This package freezes the constant-`f` linear rotating shallow-water system on
the (2pi)-torus at its physical time clock.  Every Fourier block is a
three-dimensional skew-Hermitian matrix with one geostrophic zero branch and
two inertia--gravity branches.  The theorem records the projectors, exact
exponential, lattice-shell multiplicities, all degenerate faces, a precise
finite-support periodicity criterion, and the noncompact/Schatten boundary.

Reproduce the certificate from this directory:

```text
python3 code/c217_swe_producer.py
python3 code/c217_swe_checker.py
python3 code/c217_swe_sympy_crosscheck.py
python3 code/c217_swe_replay.py
python3 code/c217_swe_mutation.py
python3 code/c217_release_manifest.py
```

The route record is deliberately conservative:
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, with
`overall=ROUTE_A_REJECTED`.  No beta-plane Rossby mode, target arithmetic,
Euler factor, root number, automorphy, or Hilbert--Polya operator is claimed.
