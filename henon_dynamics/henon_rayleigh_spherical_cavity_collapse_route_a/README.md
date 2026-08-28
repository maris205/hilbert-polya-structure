# HCS-C219: Rayleigh spherical-cavity collapse

This release freezes the source-local inviscid spherical-cavity equation

\[
 R\ddot R+\frac32\dot R^2=-\Pi/\rho,
 \qquad R(0)=R_0>0,\quad \dot R(0)=0,
\]

with density `rho>0` and constant pressure difference `Pi`.  The physical
cavitation branch is `Pi>0`; the zero and negative signs are retained as
explicit equilibrium and expansion controls.  The package closes the first
integral, the exact incomplete-Beta collapse clock, the terminal `2/5`
Puiseux law, volume and finite-liquid-energy identities, the Lagrangian, and
the `L^p` integrability thresholds.  `R0=0` is recorded as a singular
boundary and is not silently treated as a classical initial state.

Reproduce the certificate from this directory:

```text
python3 code/c219_rayleigh_producer.py
python3 code/c219_rayleigh_checker.py
python3 code/c219_rayleigh_sympy_crosscheck.py
python3 code/c219_rayleigh_replay.py
python3 code/c219_rayleigh_mutation.py
python3 code/c219_release_manifest.py
```

The three LuaLaTeX revision PDFs are built at the fixed epoch recorded in
`paper/README.md`; `paper/main.pdf` is byte-identical to round 2.  Route A is
intentionally rejected with
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.  The source Beta clock is
not target continuation/divisor/counting law, so the inverse-Beta formula is
not an A3 analytic-structure match.  No target arithmetic, Euler factors,
root numbers, automorphy, or Hilbert--Pólya operator is claimed.
