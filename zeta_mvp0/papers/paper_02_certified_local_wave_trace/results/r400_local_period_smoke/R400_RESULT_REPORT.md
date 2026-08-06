# R400 Near-Well Period/Action Smoke Report

## Decision

\[
\boxed{\text{R400 numerical/asymptotic smoke PASS; arithmetic P not evaluated.}}
\]

The run used no prime table, von Mangoldt values, zeta zeros, or spectral
peak locations.  It certifies a reversible classical orbit family near the
bottom of the fixed \(a=1.02\) one-step Hénon-warped well.

## Analytic oracle

| Quantity | Value |
|---|---:|
| \(c_a\) | 0.842534080710379 |
| \(s_-\) | 0.663843976679299 |
| \(s_+\) | 1.506378057389677 |
| \(T_+^0\) | 0.663843976679299 |
| \(D_+^0\) | 3.862722044515503 |
| \(T_+^0/\sqrt{D_+^0}\) | 0.337768612642777 |
| \(dT_+/dE\vert_{2\pi}\) | -0.027445075628370 |
| \(d(S_+/\delta)/d\delta\vert_0\) | -0.013722537814185 |

## Cells

| \(E-2\pi\) | Period | Action | \(\det(I-P)\) | Scaled closure | Gate |
|---:|---:|---:|---:|---:|:---:|
| 0.01 | 0.663569791794 | 0.006637068400 | 3.863271395158 | 6.15e-15 | PASS |
| 0.02 | 0.663296137324 | 0.013271397604 | 3.863819675707 | 3.04e-15 | PASS |
| 0.05 | 0.662478336652 | 0.033158002890 | 3.865458088008 | 2.18e-15 | PASS |
| 0.10 | 0.661125761054 | 0.066248051402 | 3.868167294053 | 1.10e-15 | PASS |
| 0.20 | 0.658458850575 | 0.132226862270 | 3.873504814887 | 2.28e-16 | PASS |
| 0.40 | 0.653271667900 | 0.263396733088 | 3.883854226235 | 3.97e-15 | PASS |

Worst numerical diagnostics were:

- shooting residual: `4.441e-14`;
- scaled closure: `6.153e-15`;
- energy drift/excess: `1.776e-13`;
- symplectic defect: `8.118e-15`.

## Small-energy extrapolation

Quadratic fits use only \(\delta=0.01,0.02,0.05\).

| Quantity | Fitted intercept | Exact intercept | Absolute error | Gate |
|---|---:|---:|---:|:---:|
| \(T_+(\delta)\) | 0.663843973386761 | 0.663843976679299 | 3.293e-09 | PASS |
| \(S_+(\delta)/\delta\) | 0.663843975854219 | 0.663843976679299 | 8.251e-10 | PASS |
| \(\det(I-P)\) | 3.862722043051477 | 3.862722044515503 | 1.464e-09 | PASS |

The fitted first slopes are `-0.027444515448498` for the period
and `-0.013722397476346` for \(S/\delta\), versus the
Poincaré--Lindstedt oracles `-0.027445075628370` and
`-0.013722537814185`.

The entire computed branch remains in the preregistered physical-time window
\([0.60,0.75]\), separated from the radial harmonic return time \(1\).

## Claim boundary

A pass is a numerical certificate for the local period, action, monodromy,
and limiting Gutzwiller amplitude.  The analytic promotion still requires
the written Lyapunov-centre and microlocal trace arguments.  Even after that
promotion, the result is a **fixed-energy semiclassical local trace bridge**,
not the high-energy fixed-time prime-power bridge.  No Hilbert--Pólya,
zeta-zero, prime trace, or RH claim follows.
