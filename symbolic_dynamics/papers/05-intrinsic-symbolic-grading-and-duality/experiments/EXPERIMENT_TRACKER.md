# Experiment Tracker

| Run ID | Milestone | Purpose | Variant | Cutoff/grid | Metrics | Priority | Status |
|---|---|---|---|---|---|---|---|
| GSD-R001 | M0 | hand-check chain conventions | canonical divisor complex | \(p,p^2,pq,pqr\) | \(\partial^2\), Betti, reduced Euler | MUST | PASS |
| GSD-R002 | M1 | exact factorization topology | canonical | \(N=64,128,256,512\) | chain counts, Betti, \(\mu\) accuracy | MUST | PASS 511/511 |
| GSD-R003 | M2 | orientation control | global parity flip + 16 gauges | same \(N\) | sign reversal, selector status | MUST | PASS CONTROL |
| GSD-R004 | M2 | proves-too-much controls | random/multiplicity/shifted/additive | same \(N\) | prefix accuracy, invariance | MUST | PASS CONTROL |
| GSD-R005 | M3 | finite dual symmetry | \(R_P(s)\) | frozen grid, nested \(P\) | symmetry/modulus residual, phase drift | MUST | FINITE ALGEBRA ONLY |
| GSD-R006 | M4 | nuclear overlap | \(L_s,L_{1-s}\) | frozen strip grid | partial trace norms + theorem | MUST | FAIL G4 / THEOREM STOP |
| GSD-R007 | M2 | mixed-cycle cancellation | free-mixing pairs | first 8 atoms | semiprime residual by parity source | MUST | PASS CONTROL 28/28 |

Final mechanical outcome:

~~~text
G0 PASS
G1 PASS
G2 PASS
G3 EULER HALF-PLANE ONLY
G4 FAIL
SCOPED_THEOREM_STOP / ROUTE_B_LOCKED
~~~
