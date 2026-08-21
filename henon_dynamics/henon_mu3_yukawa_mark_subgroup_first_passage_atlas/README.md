# HCS-C88 subgroup first-passage atlas

C88 computes the complete exact first-passage law for every one of the twenty
actual subgroup targets in the frozen sixteen-label model.  For a uniform
random ordering and prefix support `A_k`, the target variable is

```text
T_H = min{k : H <= Phi(A_k)}.
```

The canonical evidence stores, for every target, all `17` exact permutation
counts and reduced probabilities, hit and survival counts by prefix size,
the exact expectation, attainable time range, pivotal statistics, the full
`65536`-bit hit indicator, and the minimal hitting-support antichain.

Subgroup inclusion gives a pointwise order: `H <= K` implies
`T_H <= T_K` for every permutation.  All `102` comparable ordered pairs pass
the subsetwise, CDF, survival, and expectation checks.  The trivial-target
row is concentrated at zero.  The top-target row is entrywise identical to
the final C83 assembly law and has expectation `36499/3960`.

Canonical evidence SHA-256:
`4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b`.

The producer, independent minimal-antichain checker, SymPy check, clean
replay, and `40/40` hostile-mutation audit pass.  This is an up-set hitting
atlas, not an exact-closure hit/skip atlas.  Scope firewall:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
