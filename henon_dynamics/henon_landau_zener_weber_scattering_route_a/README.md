# HCS-C224 — Landau–Zener–Weber scattering

This package takes one large Route-A step for a genuinely nonautonomous
dynamical subtype.  For

\[
i\dot\psi(t)=\bigl((vt/2)\sigma_z+g\sigma_x\bigr)\psi(t),
\qquad v>0,
\]

the scalar elimination is a parabolic-cylinder (Weber) equation.  Its
connection formula gives the exact asymptotic diabatic survival law
`P_diabatic=exp(-2*pi*g^2/v)` and the Gamma-controlled Stokes phase.  A
separate deterministic RK4 ledger checks finite windows `[-T,T]`, matrix
entries, and norm residuals; it is explicitly not called an exact finite-time
formula.

Run from this directory:

```text
python3 -B code/c224_landau_zener_producer.py
python3 -B code/c224_landau_zener_checker.py
python3 -B code/c224_landau_zener_sympy_crosscheck.py
python3 -B code/c224_landau_zener_replay.py
python3 -B code/c224_landau_zener_mutation.py
python3 -B code/c224_release_manifest.py
```

The five parameter cases include slow/strong, fast/weak, a negative-coupling
gauge check, and the uncoupled boundary.  The strict verdict is
`ROUTE_A_REJECTED` with tuple
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`.
No arithmetic target, Hilbert–Pólya operator, or Route-B invocation is made.
The model is nonautonomous and therefore not another autonomous
Jaynes–Cummings excitation-block calculation (C223).

Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
