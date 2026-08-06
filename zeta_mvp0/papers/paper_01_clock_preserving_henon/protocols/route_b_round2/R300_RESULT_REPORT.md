# R300 Result Report: Relative Heat-Activity Carrier

**Executed:** 2026-08-06  
**Frozen parameter:** \(a=51/50\)  
**Original numerical status:** `PARTIAL_PASS`  
**Post-proof status:** `PASS_AFTER_R300_P1`  
**Runtime:** below one second for the production calculation; about one second
for the 60-digit independent checker

## Outcome

| Gate | Result | Evidence |
|---|---|---|
| R300-A exact carrier identity | PASS | maximum raw-polar versus reduced-integral relative error \(5.03\times10^{-15}\) |
| R300-B coefficient/sign | PASS | all brackets positive, all formal relative carriers negative, frozen tail diagnostic monotone toward one |
| R300-C uniform noncompact heat remainder | PASS AFTER R300-P1 | direct Brownian-amplitude proof gives \(O_{a,h}(tL^4)\); two independent proof audits found no substantive gap |

The arbitrary-precision checker used an independent log-radial variable and
did not import the production package.  Its internal maximum relative error
was \(1.17\times10^{-61}\); its maximum discrepancy from the double-precision
production bracket was \(3.67\times10^{-16}\).

## Exact carrier confirmed

For

\[
L=\log\frac1{2\pi t},
\qquad
r_a=\frac1{1+\sqrt{1+a}},
\]

R300 confirms

\[
I_a(t)-I_0(t)
=\frac{2a^2}{t^2}
\left[A_2(2\pi t)+4\pi r_a^2A_1(2\pi t)\right]>0.
\]

At \(a=1.02\), the stored constants are

\[
r_a=0.4130069023090093,
\]

\[
-\frac{a^2}{24\pi}=-0.013798733566067325,
\]

\[
\beta_a=2.989073584856035,
\qquad
\kappa_a=1.729920960977324.
\]

Thus the full proved relative asymptotic is

\[
Q_a(t)
=-0.013798733566067325
\left[L^2+2.989073584856035L+1.729920960977324\right]
+O_{h}(tL^4).
\]

This coefficient is independent of a fixed semiclassical parameter \(h>0\)
in two dimensions: the \(h^2\) in the first gradient correction cancels the
\(h^{-2}\) free heat-kernel prefactor.

## Frozen numerical table

| \(t\) | exact bracket | raw polar bracket | relative error | formal carrier |
|---:|---:|---:|---:|---:|
| \(10^{-2}\) | 17.6605636159 | 17.6605636159 | \(1.41\times10^{-15}\) | -0.2436934120 |
| \(3\times10^{-3}\) | 29.3713805519 | 29.3713805519 | \(9.68\times10^{-16}\) | -0.4052878547 |
| \(10^{-3}\) | 42.5878363403 | 42.5878363403 | \(1.67\times10^{-15}\) | -0.5876582068 |
| \(3\times10^{-4}\) | 59.8441309078 | 59.8441309078 | \(2.97\times10^{-15}\) | -0.8257732179 |
| \(10^{-4}\) | 78.1199715877 | 78.1199715877 | \(3.82\times10^{-15}\) | -1.0779566741 |
| \(3\times10^{-5}\) | 100.9207759465 | 100.9207759465 | \(1.83\times10^{-15}\) | -1.3925788986 |
| \(10^{-5}\) | 124.2559140769 | 124.2559140769 | \(5.03\times10^{-15}\) | -1.7145742524 |

## Interpretation

R300 kills the possibility that the first Hénon heat carrier is a numerical
angular-cancellation artifact.  The radial and Hénon-warped potentials have
the same complete classical heat integral, yet the first quantum gradient
carrier is strictly nonzero and has a fixed negative sign in the relative
trace convention.

The frozen quadrature alone did not prove the boxed full heat-trace
asymptotic.  R300-P1 subsequently closed that exact gate: it uses the common
area-preserving coordinate to cancel the classical term pointwise, expands in
the Brownian amplitude \(h\sqrt t\), and bounds the fourth derivative over the
moving effective region and its incomplete-Gamma tail.  The resulting
remainder is \(O_{a,h}(tL^4)\).

## Claim effect

- **Allowed now:** exact, independently reproduced, nonzero first-gradient
  Hénon heat carrier and the full relative heat asymptotic with a uniform
  \(O_{a,h}(tL^4)\) remainder.
- **Proved and independently reviewed:** strict ground-state rearrangement
  establishes \(\lambda_1(H_{a,h})>\lambda_1(H_{0,h})\) for every
  \(a>-1\), \(a\ne0\), and fixed \(h>0\).
- **Proved after the frozen numerical run:** the displayed full relative
  heat-trace asymptotic.
- **Still open:** rational-prime P and explicit-formula Z.

## Reproducibility

- protocol: `PILOT_PROTOCOL.md`
- uniform remainder proof: `R300_P1_UNIFORM_REMAINDER_PROOF.md`
- independent proof review: `R300_P1_INDEPENDENT_REVIEW.md`
- R300-P1 machine summary: `results/r300_p1_uniform_remainder/summary.json`
- source: `src/hp_candidate_search/heat_activity.py`
- runner: `scripts/run_r300_heat_activity.py`
- independent checker: `scripts/check_r300_heat_activity_independent.py`
- data: `results/r300_heat_activity/records.csv`
- machine summary: `results/r300_heat_activity/summary.json`
- immutable postcheck hashes:
  `results/r300_heat_activity/postcheck_manifest.json`
