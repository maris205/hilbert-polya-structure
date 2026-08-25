# C140 exact results

## Infinite exact statements

- `X3` is strictly sofic with a three-state right Fischer cover.
- Cover determinant: `D_cov(u,v)=1-u-v^3`.
- All-period intrinsic correction:
  `F_n=Tr(B^n)+(1-3*1_[3|n])v^n`.
- Intrinsic zeta:
  `Z_140=(1+v+v^2)/(1-u-v^3)`.
- Intrinsic inverse zeta:
  `D_140=(1-u-v^3)/(1+v+v^2)=D_cov*(1-v)/(1-v^3)`.
- Primitive label-orbit product at every period.
- Nonlattice label roof from fixed-cycle lengths `1,sqrt(2)`.

## Exact finite sentinels through period 15

| Quantity | Value |
|---|---:|
| admissible intrinsic rooted points | 969 |
| primitive label cycles | 74 |
| rooted `(N1,N0)` cells | 60 |
| primitive `(N1,N0)` cells | 32 |

Cover fixed counts are
`1,1,4,5,6,10,15,21,31,46,67,98,144,211,309`; intrinsic label fixed counts
are `2,2,2,6,7,8,16,22,29,47,68,96,145,212,307`.  The difference is exactly
the all-zero correction.  The prefix tests implementation only.

## Conservative verdict

`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`; `route_b_invocation_allowed=false`.
