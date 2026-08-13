# Results and Decision Record

## Outcome

The frozen Stage-1 candidate failed its entry gate. The formal outcome is
**A0_SHADOW_FAIL_CARRIER_UNAVAILABLE**.

The preregistered parent-derived ensemble did not supply an adequately exposed
carrier at the symplectic endpoint. This is not a theorem that no bounded invariant
set can carry arithmetic information, and it is not a disproof of an arithmetic
conjecture. Under the frozen candidate and protocol, however, it stops the
multiplier-prime, dynamical-zeta, and quantization branches.

## Raw split table for the frozen parameter

For return gaps to \(L=\{x<0\}\), the primary statistic is

\[
P=\frac{N_{\rm even}-N_{\rm odd}}{N_{\rm even}+N_{\rm odd}}.
\]

Uncertainty resamples whole trajectories.

| Split | \(\rho\) | Exposure | Survival | \(P\) | 95% cluster-bootstrap CI | Gaps |
|---|---:|---:|---:|---:|---:|---:|
| Development | 0 | 1.000000 | 1.000000 | 1.000000 | [1,1] | 459,896 |
| Development | 0.2 | 1.000000 | 1.000000 | 0.998913 | [recorded in JSON] | 1,041,067 |
| Development | 0.5 | 0.725006 | 0.722656 | -0.896959 | [recorded in JSON] | 2,795 |
| Development | 1 | 0.011573 | 0 | -0.709911 | [recorded in JSON] | 9,928 |
| Validation | 0 | 1.000000 | 1.000000 | 1.000000 | [1,1] | 460,130 |
| Validation | 0.2 | 1.000000 | 1.000000 | 0.998890 | [0.998799,0.998982] | 1,041,214 |
| Validation | 0.5 | 0.713842 | 0.711426 | -0.877537 | [-0.894156,-0.860045] | 2,907 |
| Validation | 1 | 0.011447 | 0 | -0.707447 | [-0.717086,-0.697476] | 10,111 |
| **Test** | **0** | **1.000000** | **1.000000** | **1.000000** | **[1,1]** | **460,189** |
| **Test** | **0.2** | **1.000000** | **1.000000** | **0.998907** | **[recorded in JSON]** | **1,041,094** |
| **Test** | **0.5** | **0.734622** | **0.732422** | **-0.904517** | **[recorded in JSON]** | **2,723** |
| **Test** | **1** | **0.011724** | **0** | **-0.706648** | **[-0.716253,-0.696785]** | **9,988** |

The confirmatory endpoint failed both availability conditions: exposure was far below
0.80 and the return count was below 10,000. Its polarity lower confidence bound was
also far below 0.98. The pre-escape \(P(1)\) value is descriptive and may not be used
as a survivor-conditioned transport success.

## Neighbor controls and multiplicity

At \(\rho=0.1\) and \(0.2\), all four clean neighbor parameters reproduced polarity
above 0.997 in validation and test. At \(\rho=1\), every neighbor had approximately
one-percent exposure, zero endpoint survivors, and negative polarity. In the sealed
test analysis, all four one-sided neighbor-specificity diagnostics had Holm-adjusted
value 1.0. Neither the small-dissipation persistence nor endpoint collapse is
specific to \(u_c\). The broad pattern triggers the **PROVES_TOO_MUCH** warning in
addition to the carrier-unavailability decision.

The Holm quantities are bootstrap sign-tail diagnostics, not exact randomized-
treatment p-values. Effect sizes and cluster-bootstrap confidence intervals in
results/analysis/transport_test_analysis_v1_paired.csv are the principal comparison
outputs.

## Dynamical mechanism

For the positive fixed point, Jury stability gives the exact flip threshold

\[
\rho_{\rm PD}=\sqrt{4a/3}-1.
\]

At \(a=u_c\), this is \(0.43466094145\ldots\). A distinct post-validation diagnostic
ensemble followed the sequence unresolved/high-period
\(\to 8\to 4\to 2\to\) positive fixed point. The period-2/fixed-point switch lies
between \(0.43\) and \(0.44\), bracketing the analytic threshold. All four neighbors
switched on corresponding adjacent grid cells around their thresholds. This is an
ordinary dissipative bifurcation skeleton, not a \(u_c\)-specific arithmetic signal.

At \(\rho=1\), 256/256 secondary diagnostic trajectories escaped. A periodic sink is
also analytically impossible because every period-\(n\) monodromy has determinant
one. The dissipative attractor story therefore cannot simply continue into the
conservative endpoint.

## Periodic-orbit software control

At \((a,\rho)=(6,1)\), the finder recovered the exact primitive binary-necklace counts
\(2,1,2,3,6,9,18,30,56,99\) through period 10. The independent 80-digit audit
refined all 226 cycles, with maximum residual \(7.04\times10^{-61}\). This is not
interval certification.

At \((u_c,1)\), binary seeds found \(2,0,2,2,2,3,4,5\) cycles through period 8,
versus reference counts \(2,1,2,3,6,9,18,30\). All 20 found cycles passed the
high-precision residual audit, but the ledger is explicitly incomplete and cannot
support a cycle expansion or determinant.

## Evidence-level transitions

| Claim | Before | After |
|---|---|---|
| Parent has the declared parity fixture at \(u_c\) | OPEN | NUMERICAL_OBSERVATION, reproduced across three splits |
| Parity shadow reaches the symplectic endpoint in the frozen ensemble | OPEN | STOP_SCOPED: carrier unavailable |
| Small-\(\rho\) persistence is \(u_c\)-specific | OPEN | REFUTED in the tested neighbor panel |
| High-\(a\) orbit implementation passes its control | OPEN | NUMERICALLY_CERTIFIED for cutoff/regime |
| Frozen-\(u_c\) ledger is complete | NOT_TESTABLE | remains NOT_TESTABLE |
| Riemann-targeted zeta/quantization should be constructed | STOP_SCOPED | remains closed by A0 stop rule |

## Reproducible artifacts

- results/transport/transport_test_frozen_v2.json
- results/analysis/transport_test_analysis_v1.json
- results/analysis/transport_test_analysis_v1_raw.csv
- results/analysis/transport_test_analysis_v1_paired.csv
- results/attractors/attractor_diagnostics_v1.json
- results/ledger_positive_a6_rho1_n10_audit80.json
- results/ledger_uc_rho1_n8_audit80.json
- experiments/test_access_log.md

## Next-experiment boundary

No more arithmetic work is justified inside this candidate under the current source
lock. A future study would need a genuinely different compact/invariant carrier or a
branch-labeled natural extension and therefore constitutes a new candidate, not a
repair of this failed endpoint. The present project proceeds only to documentation,
independent review, and publication of the controlled negative result.
