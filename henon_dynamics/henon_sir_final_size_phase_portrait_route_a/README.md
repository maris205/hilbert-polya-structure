# HCS-C198 — complete closed-SIR phase portrait and final-size branch

C198 treats the classical closed, mass-action SIR ordinary differential
equations for every positive transmission/removal parameter and every
nonnegative initial state with positive susceptible mass.  One exact scaling
reduces the family to `x'=-xy`, `y'=y(x-1)`.  One phase integral then closes
global positivity, the infection peak, time quadrature, the unique final state,
the correct Lambert branch, final-size sensitivity, equilibrium-line stability,
and the absence of nonconstant recurrence.

This is a mathematical dynamical-systems certificate.  It uses no clinical,
personal, fitted or outbreak data and gives no medical prediction or advice.

## Strict Route-A result

The removed coordinate is strictly monotone whenever infection is present, so
there is no nonconstant periodic-orbit layer.  Biological rate parameters do
not create prime arithmetic:

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)
ROUTE_A_REJECTED
```

Route B is false under `NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python code/c198_sir_producer.py
python code/c198_sir_checker.py
python code/c198_sir_sympy_crosscheck.py
python code/c198_sir_replay.py
python code/c198_sir_mutation.py
python code/c198_release_manifest.py
```

The final paper is `paper/main.pdf`; the release preserves all three
content-distinct manuscript rounds.
