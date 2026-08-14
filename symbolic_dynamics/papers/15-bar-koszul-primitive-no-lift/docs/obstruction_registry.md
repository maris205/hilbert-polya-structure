# SD-C17 Obstruction Registry

## O17.1 — Primitive/power-layer obstruction

At `p^2q^2`, the primitive signed sum is `-1`, while the two `r=2`
repetitions from `pq` contribute `+1/2+1/2`. Scalar cancellation therefore
crosses primitive multidegree and power layers.

**Type:** proved obstruction with exact finite certificate.

**Decision:** `STOP_PRIMITIVE_LEVEL_INVOLUTION`.

## O17.2 — Atom-equivariance obstruction

At `pqr`, positive necklaces have `S_3` orbit profile `1+2` and negative
necklaces have profile `3`. Their virtual character is `(0,0,3)`, so the
permutation representations are not isomorphic and no atom-equivariant
sign-reversing bijection exists.

**Type:** proved representation-theoretic obstruction.

**Decision:** `STOP_EQUIVARIANT_SIGN_REVERSAL`.

## O17.3 — Scalar/parity power obstruction

An ordinary negative scalar edge contributes `(-w)^r`; an odd line
contributes supertrace `-w^r`. They disagree at every even power. The exact
two-term contraction `dh+hd=I` has zero supertrace at all powers but lacks the
mixed primitives of the signed scalar alphabet.

**Type:** proved ledger-type obstruction.

**Decision:** `STOP_PARITY_SUBSTITUTION`.

## O17.4 — Universal Koszul cancellation

The identity `D_k=product_i(1-x_i)` holds for arbitrary formal variables.
All 112 frozen rational inventories and their presentation shuffles pass
exactly. It cannot distinguish tensor arithmetic from generic inventories.

**Type:** proved adversarial obstruction.

**Decision:** `STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`.

## O17.5 — Route-A global structure absent

SD-C17 has no completed functional equation, Gamma factor, trivial-zero
treatment, target counting law, intrinsic Weil compression, or natural
unitary/operator lift.

**Type:** open theorem obligations for any successor; absent in the frozen
candidate.

**Decision:** `A3_FAIL`, `A4_FAIL`, `ROUTE_B_LOCKED`.
