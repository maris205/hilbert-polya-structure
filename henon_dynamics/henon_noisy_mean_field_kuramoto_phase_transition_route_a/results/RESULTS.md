# Exact results

## Canonical artifact

`c347_kuramoto_evidence.json` is a canonical, self-hashed exact receipt bound to the raw and semantic hashes of the Route-A YAML.

| ledger | rows | arithmetic |
|---|---:|---|
| Bessel coefficient ratios | 17 | rational |
| formal (I_1/(\kappa I_0)) quotient | 9 | rational |
| positive-series tail brackets | 7 | rational intervals |
| nonzero self-consistency roots | 4 | certified rational brackets |
| uniform Fourier blocks | 162 | rational |
| **total** | **199** | **no floating point** |

For each (I_0,I_1) tail, the lower endpoint is a positive partial sum and the upper endpoint is a next-term geometric majorant. Each stationary-root row has a certified positive lower bound for (aR(\kappa)-\kappa) on its left endpoint and a certified negative upper bound on its right endpoint. Analytic strict monotonicity owns uniqueness.

## Theorem result

The proof establishes global classical probability flow, free-energy dissipation, von Mises stationary exhaustion, the threshold (K=2D), the complete uniform Fourier spectrum, and

\[
\kappa^2=4\delta+\frac23\delta^2+O(\delta^3),\qquad
r^2=\delta-\frac56\delta^2+O(\delta^3).
\]

The finite ledger is explicitly marked `finite_evidence_proves_continuum_theorem: false`.

## Evaluation result

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`; overall `ROUTE_A_REJECTED`; Route B false. All nine forbidden scope flags are false.
