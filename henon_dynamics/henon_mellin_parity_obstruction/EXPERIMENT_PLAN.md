# Experiment plan

**Problem:** Decide the natural H6 Mellin/parity scattering divisor.

**Method thesis:** Scaling covariance turns the infinite cubic boundary orbit
into a two-sign Mellin multiplier, but its natural reciprocal scattering
ratio has a zeta-relevant off-critical divisor.

**Date:** 2026-08-13.

## Claim map

| Claim | Minimum convincing evidence | Blocks |
|---|---|---|
| C1: natural parity scattering has an extra divisor | one certified simple even-channel zero, mirror nonzero, odd channel nonzero | B1--B3 |
| C2: the point is genuinely extra | exact linear-parent formula and certified completed-\(\xi\) nonvanishing | B4 |

## Run order

| Milestone | Goal | Decision gate | Cost | Risk |
|---|---|---|---|---|
| M0 | reproduce \(z_0\) by three formulas | residuals agree at 50 digits | seconds | branch/sign mismatch |
| M1 | complex-ball/Rouché certificate | unique zero in disc | minutes | loose derivative bound |
| M2 | certify no cancellation | all three companion factors exclude zero | seconds | parity convention |
| M3 | parent controls | parent factors exclude disc | seconds | reference ambiguity |
| M4 | optional strip census | argument-principle count stable | minutes | boundary near zero |

## Success criterion

A single certified disc contained in \(0<\operatorname{Re}z<1\), disjoint
from \(\operatorname{Re}z=1/2\), containing exactly one zero of \(A\), with
\(A(1-z)B(z)B(1-z)\) nonzero there.

## Failure interpretation

If the local certificate fails, the high-precision signal remains only a
numerical observation and no theorem-level Route-A rejection is issued.

## Compute budget

CPU only, under one minute for the core local certificate; no GPU, prime
table, or Riemann-zero data.
