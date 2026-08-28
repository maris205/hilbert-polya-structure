# P26 Round-4 conclusion

## Paper-level advance

Round 4 upgrades the Round-3 oriented conjugacy owner to a correctly normalized
Hecke-correspondence theorem. For every prime `p` not dividing 11,

```text
integral_(T_(p,*) C) alpha_f = a_p integral_C alpha_f.
```

For a hyperbolic owner `M`, the double-coset right action decomposes
`T_(p,*) C_M` into an explicit finite sum of oriented closed-geodesic owners
`delta_O in Gamma_0(11)`. Thus the exact relation is

```text
sum_O I(delta_O) = a_p I(M),
```

not a one-prime/one-primitive-orbit identity.

## Finite result

For the 11 frozen positive-word owners and `p={2,3,5,7,13}`:

- 385/385 exact branch-gluing identities pass;
- 320/320 eta-product Hecke coefficient identities pass;
- 138 closed cycle-owner instances are produced and all 138 receive exact
  finite primitive-root certificates; full cross-instance conjugacy
  deduplication is not claimed;
- 55/55 direct complex period-sum checks pass;
- maximum primary complex residual is `2.229752420147902e-14`;
- 8/8 tests pass; and
- two full result trees are byte-identical with SHA-256
  `4cd45da8e7fa82e4688bc6975dae44c4206837b40652979167432ffe7b07f20e`.

## Kill result

The relation is structural but not discriminative. Since `X_0(11)` has genus
one and the Hecke eigenvalues are real, `T_p` acts by the same scalar `a_p` on
all real compact cohomology. Every legitimate smooth closed-form control
extending over `X_0(11)` obeys the same period relation. The registered control
`3 Re(omega_f)+4 Im(omega_f)` passes exactly for that reason.

A target-free nonmodular q-series control fails 302/320 exact coefficient rows
and separates every direct period row, but it lacks a `Gamma_0(11)` quotient
owner. Its failure cannot restore discriminative arithmetic evidence.

Therefore:

```text
HECKE_CORRESPONDENCE_CYCLE_RELATION=PROVED
DISCRIMINATIVE_HECKE_EULER_EVIDENCE=STOP_SCOPED
PRIMITIVE_EULER_FACTORIZATION=NOT_ESTABLISHED
```

## Route boundary

P26 remains in ARS Stage 1 and Proposal Stage 1 / Route A A0--A1. The formal
Route-A tuple is unassigned, A2 was not run, and Route B remains `NOT_RUN` with
invocation disallowed. No prime-to-one-orbit map, complete conjugacy-class
enumeration, dynamical-zeta Euler product, target-zero use, or manuscript draft
is claimed.
