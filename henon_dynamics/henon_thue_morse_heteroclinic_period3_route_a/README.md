# HCS-C154: an intrinsic period-three limit orbit in a heteroclinic closure

This package freezes one two-sided configuration with a period-three `234`
left tail and a Thue--Morse `01` right tail, then takes the closure of its
full shift orbit.  It proves the exact disjoint decomposition

```text
X = X_TM disjoint_union Orbit(x) disjoint_union Orbit(y_234),
Omega(sigma) = X_TM disjoint_union Orbit(y_234).
```

The interface orbit is dense as a full two-sided `Z`-orbit, isolated, and
wandering.  This is not standard forward topological transitivity: the open
singletons `U={sigma x}`, `V={x}` never meet under `sigma^n(U)` for `n>=0`.
All periodic points form the single period-three limit cycle, so
`Fix(n)=3` exactly when `3|n` and `zeta_X(z)=1/(1-z^3)`.

This improves on a freely disjoint attachment because the periodic skeleton
is generated inside one heteroclinic orbit closure.  The strict verdict is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_EXPLORATORY`.
Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`; `route_b_invocation_allowed=false`.
