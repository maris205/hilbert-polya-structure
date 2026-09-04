# HCS-C362: Cucker--Smale flocking threshold

This package proves an all-particle flocking theorem for the normalized
Cucker--Smale system with communication weight
`psi(r)=(1+r^2)^(-beta)`.  The exact theorem contains global existence,
mean-velocity conservation, velocity-variance dissipation, a diameter
comparison principle, the tail-integral confinement barrier, the endpoint
`beta=1/2`, and a scalar two-body theorem showing that the short-range
threshold is sharp.

The evidence is a deterministic implementation receipt.  The analytic proof,
not a finite experiment, owns the arbitrary-`N`, arbitrary-dimension theorem.
The Route-A verdict is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)` and
`ROUTE_A_REJECTED`; Route B is locked by
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Release commands

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c362_cucker_smale_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c362_cucker_smale_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c362_cucker_smale_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c362_cucker_smale_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c362_cucker_smale_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c362_release_manifest.py
```

The final paper is `paper/main.pdf`.  The release manifest self-excludes and
hashes exactly 27 payload files inside this 28-file package.
