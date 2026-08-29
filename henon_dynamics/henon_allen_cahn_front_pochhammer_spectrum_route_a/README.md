# HCS-C231 — Allen–Cahn front and Pöschl–Teller spectrum

This package closes the equal-well Allen–Cahn front
(u_t=u_{xx}+u-u^3) and its (epsilon)-scaled family.  It proves the tanh
heteroclinic, equal-well speed selection (c=0), gradient-flow energy
dissipation, translation uniqueness, and the one-dimensional Pöschl–Teller
linear spectrum.  The front is heteroclinic, not a primitive periodic orbit;
the Route-A verdict is `ROUTE_A_REJECTED` with `A4_FORMAL_HINT`.

Run from this directory:

```text
python3 -B code/c231_allen_cahn_producer.py
python3 -B code/c231_allen_cahn_checker.py
python3 -B code/c231_allen_cahn_sympy_crosscheck.py
python3 -B code/c231_allen_cahn_replay.py
python3 -B code/c231_allen_cahn_mutation.py
python3 -B code/c231_release_manifest.py
```

The release contract is 27 payload files plus the self-excluded manifest, with
three revision PDFs and no build sidecars.  Scope is locked to
`NO_BAD_EULER_OR_ROOT_NUMBER`.
