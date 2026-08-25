# C155 paper plan

## Title and thesis

**Full-Period Concentration in Mersenne Rule 90.**  The exact periodic image
has exponentially concentrated full periods, an asymptotically sharp
Burnside cycle count, and mean cycle length asymptotic to the circumference.

## Claims--evidence matrix

| Claim | Proof or evidence |
|---|---|
| periodic image has size `2^(L-1)` | Frobenius and multiplier-kernel proof |
| fixed spaces depend on `gcd(j,L)` | polynomial Bézout identities |
| proper fixed dimension at most `2L/3` | cleared polynomial degree and odd proper divisor |
| full-period state concentration | union bound |
| cycle count and mean-length limits | Burnside plus reciprocal normalization |
| exact implementation | matrices, SymPy, replay, mutations |

The compact finite table is a sentinel, not the argument.
