# HCS-C155: full-period concentration in Mersenne Rule 90

For Rule 90 on every Mersenne ring `L=2^r-1`, `r>=2`, this package upgrades
the exact periodic-image theorem to an asymptotic orbit-geometry theorem.  If
a periodic state is sampled uniformly from the `2^(L-1)`-point image, then

```text
Pr(exact period < L) <= 2L 2^(-L/3),
Pr(exact period = L) -> 1.
```

Burnside's lemma also shows
`|L*C_L/2^(L-1)-1| <= 2L 2^(-L/3)`, where `C_L` is the total number of
primitive cycles.  Consequently the cycle-averaged period divided by `L`
tends to one.  Exact Möbius/Burnside ledgers through `r=8` and the
power-of-two nilpotent control are retained.

The strict verdict is `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall
`ROUTE_A_EXPLORATORY`.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`;
`route_b_invocation_allowed=false`.
