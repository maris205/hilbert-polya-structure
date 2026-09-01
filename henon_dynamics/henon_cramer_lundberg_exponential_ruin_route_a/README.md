# HCS-C282 — exponential Cramér–Lundberg ruin atlas

This package solves the classical compound-Poisson surplus process with
exponential claims through one joint transform

`Phi_{q,s}(u)=E_u[exp(-q tau-s D); tau<infinity]`.

The selected quadratic root gives an exact formula for every discount, deficit
penalty, initial reserve, and safety-loading chamber.  Ultimate ruin,
memoryless overshoot independence for positive claim intensity, conditional
first means of ruin time, the critical
infinite-mean wall, the adjustment martingale, and the dual supremum mixture
all follow in the same theorem.  The no-claim and zero-reserve faces are
included; conditional laws are undefined on the no-claim face, and zero
premium is explicitly outside the frozen convention.
The Route-A owner is explicitly the process killed at ruin; the transform is a
first-passage functional of the underlying surplus.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/c282_ruin_producer.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c282_ruin_checker.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c282_ruin_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c282_ruin_replay.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c282_ruin_mutation.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c282_release_manifest.py
```

The route tuple is `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, with
`ROUTE_A_REJECTED`.  Scope is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is not
authorized.
