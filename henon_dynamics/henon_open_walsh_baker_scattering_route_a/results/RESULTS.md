# C148 exact results

## Infinite exact statements

- `B_k` is a norm-one contraction of rank `2*3^(k-1)`.
- `B_k^k=A^(tensor k)` has rank `2^k`.
- Both subunitarity defects are rank-`3^(k-1)` orthogonal projections.
- For `d=gcd(n,k)`,
  `Tr(B_k^n)=Tr(A^(n/d))^d` for every `n>=1`.
- Newton recursion gives the exact degree-`2^k` secular polynomial and the
  algebraic zero multiplicity `3^k-2^k`.
- The signed/complex closed-walk trace and primitive-path product preserve all
  cancellations; the raw product is absolutely regroupable for
  `|z|<1/sqrt(3)`.

## Exact finite receipts

| Quantity | Value |
|---|---:|
| `k` values with complete polynomials | 5 |
| total coefficient cells, including zeros | 67 |
| nonzero coefficient cells | 50 |
| direct trace sentinels | 60 |
| direct basis-source checks of `B_k^k` | 363 |
| rooted `k=2` closed paths, periods 1--8 summed | 510 |
| primitive `k=2` path cycles, periods 1--8 summed | 71 |

The closed control is unitary.  The projector-order control is exactly
isospectral.  The moved-hole control preserves rank but changes the secular
linear coefficient.

## Corrected escape ledger

The one-step claim `rank(B_k)=2^k` is refuted by the frozen definition.  The
release does not silently repair it: the rejected and corrected statements
are both machine-checked.  The value `2^k` belongs to `rank(B_k^k)`.

## Conservative verdict

`(A1_WEAK,A2_FAIL,A3_FAIL,A4_UNITARY_OR_SCATTERING_CANDIDATE)`, overall
`ROUTE_A_EXPLORATORY`; `route_b_invocation_allowed=false`.
