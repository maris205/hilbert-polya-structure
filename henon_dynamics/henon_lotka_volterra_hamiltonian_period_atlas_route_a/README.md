# HCS-C211: a Hamiltonian period atlas for positive Lotka--Volterra flow

This release freezes the two-species positive Lotka--Volterra system

`x' = x(a-b y),   y' = y(-c+d x)`, with `a,b,c,d>0`.

The theorem package proves a strict, proper exponential Hamiltonian in log
coordinates, compact periodic ovals for every positive non-equilibrium energy,
an exact Lambert-W inverse-branch quadrature for the period and enclosed area,
the action identity `J'(h)=T(h)/(2 pi)`, the center-period limit, and exact
cycle averages. Axis and zero-rate boundaries are kept separate. Period
monotonicity and high-energy asymptotics are deliberately not claimed.

Reproduce the certificate with:

```bash
python3 code/c211_lv_producer.py
python3 code/c211_lv_checker.py
python3 code/c211_lv_sympy_crosscheck.py
python3 code/c211_lv_replay.py
python3 code/c211_lv_mutation.py
python3 code/c211_release_manifest.py
```

The scope guard is `NO_BAD_EULER_OR_ROOT_NUMBER`. The Route-A record is
`overall=ROUTE_A_REJECTED` and `route_b_invocation_allowed=false`.
