# C139 exact results

## Infinite exact statements

- Eight-state determinant:
  `1-x00-x11-x01*x10+x00*x11+(1-y)*x00*x01*x10*x11`.
- At `y=1`, exact reduction to the C135 directed-edge determinant.
- Rooted trace identity and primitive product at every period.
- Rational independence of
  `(1,sqrt(2),sqrt(3),sqrt(6),sqrt(5))`.
- Coding-relative forward-memory theorem: `001011` and `001101` agree in all
  cyclic block populations through width three but have marker counts `0,1`.
- Nonlattice witness: fixed-cycle lengths `1,sqrt(6)`.

## Exact finite sentinels through period 12

| Quantity | Value |
|---|---:|
| rooted closed words | 8,190 |
| primitive cycles | 747 |
| rooted feature cells | 258 |
| primitive feature cells | 229 |
| first same-feature primitive collision period | 7 |

The retained period-seven collision is `0101111`, `0110111`, with common
feature vector `(0,2,2,3,0)`.  The prefix checks implementation only; it is not
the proof of an infinite identity.

## Conservative verdict

`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`; `route_b_invocation_allowed=false`.
