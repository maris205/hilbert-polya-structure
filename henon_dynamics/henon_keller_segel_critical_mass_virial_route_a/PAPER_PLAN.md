# Paper plan: HCS-C363

## One-sentence contribution

Free-energy scaling and a symmetrized virial identity meet at exactly `8 pi`,
yielding an explicit supercritical classical breakdown time and a critical
stationary family whose infinite second moment closes the apparent endpoint
paradox.

## Claims--evidence matrix

| Claim | Analytic support | Finite receipt |
|---|---|---|
| Conservation and dissipation | integration by parts and gradient form | symbolic identities |
| Critical mass from scaling | exact mass-preserving dilation | 21 scaling rows |
| Virial obstruction | Newtonian-kernel symmetrization | 21 virial rows |
| Critical equilibria | direct Poisson and flux calculation | nine profile rows |
| Infinite-moment caveat | explicit truncated moment primitive | symbolic limit |
| Radial reduction | differentiate cumulative mass | nine radial rows |
| Route-A rejection | evaluator v0.2.0 | strict YAML and false flags |

## Revision plan

- Round 0: conservation, energy, scaling, and the mass threshold.
- Round 1: virial identity, quantitative supercritical bound, and critical
  stationary profiles with the moment caveat.
- Round 2: radial cumulative dynamics, singular boundaries, evidence,
  limitations, and Route-A closure.

The main relationships are one-dimensional formula chains rather than spatial
data.  A separate generated figure would be less exact than the native
equations and regime table, so the figure phase deliberately uses no raster
illustration.
