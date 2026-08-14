# SD-C17 Experiment Plan

**Candidate:** tensor-atom squarefree subset shift with scalar Koszul signs

**Date:** 2026-08-14

**System family:** Symbolic Dynamics only

**Compute:** deterministic CPU; no GPU

**Target-zero data:** forbidden and unused

## Claim map

| Claim | Minimum convincing evidence | Block |
|---|---|---|
| C1: scalar Koszul cancellation is not a primitive-cycle cancellation | exact `pq`, `p^2q^2`, and repetition ledgers | B1 |
| C2: no atom-natural sign-reversing pairing exists already at `pqr` | exact `S_3` orbits, fixed characters, and pairing audit | B2 |
| C3: mixed squarefree scalar coefficients cancel in every degree | Stirling identity plus independent cyclic-partition enumeration | B3 |
| C4: a scalar sign cannot be reinterpreted as chain parity | power audit and an explicitly contracted two-term complex | B4 |
| C5: the scalar identity is not arithmetically selective | fixed-seed arbitrary rational inventories and relabelings | B5 |

## Frozen object

For a finite tensor-atom set `P={p_1,...,p_k}`, the one-vertex edge alphabet
is the set of all nonempty subsets `S` of `P`. An edge has formal monomial

```text
x_S=product_(p in S) x_p
```

and ordinary scalar sign

```text
epsilon(S)=(-1)^(|S|+1).
```

Words are identified only under cyclic rotation. Reflection is not
quotiented. Repetition uses the actual scalar power `w(gamma)^r`, not a
supertrace convention. The frozen determinant is

```text
F_k=sum_(S nonempty) epsilon(S)x_S,
D_k(x,z)=1-z F_k,
D_k(x,1)=product_p(1-x_p).
```

## Frozen cutoffs

- Explicit multidegrees: `pq`, `p^2q^2`, and squarefree `pqr`.
- Cyclic set-partition enumeration: `k=2,...,7`.
- Stirling certificate: `k=1,...,12`.
- Scalar/supertrace powers: `r=1,...,8`.
- Rational controls: `k=2,...,8` and seeds `15100,...,15115`, giving
  exactly 112 controls.
- Arithmetic: integer and `Fraction` only; no floating comparison.

## Experiment blocks

### B1 — Primitive/power ledger

Enumerate necklaces at `pq` and `p^2q^2`, preserving scalar signs and least
periods. The decisive certificate is:

- `pq`: `[p][q]` has sign `+1`; `[pq]` has sign `-1`;
- `p^2q^2`: one positive primitive and two negative primitives, signed sum
  `-1`;
- the two `r=2` repeats from `pq` contribute `1/2+1/2=1`;
- only the full primitive-plus-power log coefficient is zero.

### B2 — `S_3` naturality obstruction

Enumerate squarefree `pqr` cyclic partitions and compute the atom-permutation
action. Require exact orbit profiles `1+2` on the positive side and `3` on
the negative side, with virtual character

```text
(0,0,3)=1+sign-standard
```

in class order identity, transposition, three-cycle. Audit a lexicographic
matching as an explicitly non-natural control.

### B3 — General scalar identity

Compute Stirling numbers recursively and certify

```text
sum_(m=1)^k (-1)^(k+m)(m-1)!S(k,m)=delta_(k,1)
```

through `k=12`. Independently enumerate cyclic partitions through `k=7` and
verify every block-count row against `(m-1)!S(k,m)`.

### B4 — Scalar sign versus supertrace

Compare `(-w)^r` with the odd-line supertrace `-w^r` through `r=8`. Freeze
the actual two-term matrices, in basis `(even,odd)`,

```text
d = [[0,1],[0,0]],   h = [[0,0],[1,0]],
```

and verify `dh+hd=I`, commutation with `T=wI`, and zero supertrace for every
frozen power. Compare its primitive ledger with the scalar `{+w,-w}` alphabet,
which has the additional mixed primitive `[+w][-w]`.

### B5 — Universality controls

For all 112 exact rational inventories, verify

```text
1-sum_(S nonempty)(-1)^(|S|+1)x_S=product_i(1-x_i)
```

and invariance under a frozen presentation shuffle. Universal success forces
`STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`.

## Run order

| Milestone | Runs | Decision gate | Cost |
|---|---|---|---|
| M0 | subset and rotation sanity | exact identities only | under 1 s CPU |
| M1 | `pq`, `p^2q^2`, `pqr` | primitive and symmetry obstructions reproduced | under 1 s CPU |
| M2 | Stirling and cyclic partitions | every row exact | under 1 s CPU |
| M3 | scalar/supertrace and chain block | power and contraction certificates exact | under 1 s CPU |
| M4 | 112 rational controls | mandatory `PROVES_TOO_MUCH` verdict | under 1 s CPU |

## Decision rules

```text
GO_SCALAR_KOSZUL_DETERMINANT
STOP_PRIMITIVE_LEVEL_INVOLUTION
STOP_EQUIVARIANT_SIGN_REVERSAL
STOP_PARITY_SUBSTITUTION
STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH
ROUTE_B_LOCKED
```

Every target-zero error, missing/extra-zero count, and root-count field is
`not_applicable`. No target roots are loaded, searched, fitted, or reported.
