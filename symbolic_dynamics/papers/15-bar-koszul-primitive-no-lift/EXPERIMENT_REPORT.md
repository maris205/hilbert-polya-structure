# SD-C17 Experiment Report

## Frozen outcome

The squarefree subset shift has an exact scalar Koszul determinant but no
natural primitive-cycle lift of that cancellation:

```text
GO_SCALAR_KOSZUL_DETERMINANT
STOP_PRIMITIVE_LEVEL_INVOLUTION
STOP_EQUIVARIANT_SIGN_REVERSAL
STOP_PARITY_SUBSTITUTION
STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH
ROUTE_A_REJECTED
ROUTE_B_LOCKED
```

No Riemann-zero data, target root search, fitted pairing, fitted phase, or
cross-family repair is used.

## 1. The first pairing and its power obstruction

At multidegree `pq`, exact enumeration gives the tempting pair

```text
[p][q]  sign +1,
[pq]    sign -1.
```

At `p^2q^2`, however, the target-degree primitive necklaces are exactly

```text
[p][p][q][q]  sign +1,
[p][q][pq]    sign -1,
[p][pq][q]    sign -1.
```

Their signed primitive contribution is `-1`, so no sign-reversing bijection
exists even before imposing naturality. The two degree-`pq` primitives each
repeat twice with scalar trace-log weight `1/2`; their total `+1` cancels the
target-degree `-1`. Thus the complete `p^2q^2` log coefficient is zero only
because cancellation crosses primitive degree and repetition layers.

## 2. The `S_3` obstruction

At squarefree `pqr`, the positive necklaces split into atom-permutation orbit
sizes `1+2`, while the negative necklaces form one orbit of size `3`. Fixed
counts in class order identity, transposition, three-cycle give the exact
virtual character

```text
positive-negative = (0,0,3) = 1 + sign - standard.
```

The nonzero three-cycle character forbids an `S_3`-equivariant positive-to-
negative bijection. A frozen lexicographic pairing fails equivariance on four
of the six permutations, with three failed images in each case. It is a
presentation rule, not a natural contraction.

## 3. General scalar cancellation

The exact Stirling certificate verifies all 12 rows through `k=12`, with
mixed squarefree coefficients zero for every checked `k>=2`. Independent
cyclic-partition enumeration verifies all 27 block-count rows through `k=7`:

| `k` | total cyclic partitions |
|---:|---:|
| 2 | 2 |
| 3 | 6 |
| 4 | 26 |
| 5 | 150 |
| 6 | 1,082 |
| 7 | 9,366 |

Every count equals `(m-1)!S(k,m)` at fixed block count `m`. This confirms the
scalar identity while the `S_3` certificate shows why equality of signed
dimensions does not imply a natural orbitwise pairing.

## 4. Scalar sign is not chain parity

For `r=1,...,8`, the negative scalar rule `(-w)^r` and the odd-line
supertrace rule `-w^r` disagree at all four even repetitions. At `r=2` their
coefficients are `+1` and `-1`, a difference of `2`; a non-power-compatible
pairing leaks exactly `1` after the `1/r` trace-log factor.

The true contractible two-term control is computed from

```text
d=[[0,1],[0,0]],  h=[[0,0],[1,0]].
```

Matrix multiplication verifies `dh+hd=I`; `d` commutes with `T=wI`; and all
eight frozen supertrace coefficients vanish. This block has no mixed
length-two primitive. The scalar alphabet `{+w,-w}` does have the primitive
`[+w][-w]`, so aggregate trace equality does not identify their primitive
ledgers.

## 5. Universality control

All 112 exact rational controls, using `k=2,...,8` and 16 frozen seeds per
cutoff, satisfy

```text
1-sum_(S nonempty)(-1)^(|S|+1)x_S=product_i(1-x_i)
```

and remain invariant under presentation shuffles. The determinant mechanism
therefore succeeds for arbitrary inventories and supplies no arithmetic
selectivity: `STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`.

## Route-A interpretation

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_FAIL,
 A2_ANALYTIC_DETERMINANT,
 A3_FAIL,
 A4_FAIL)

ROUTE_A_REJECTED
```

- A0 is analytic at the source level: tensor-indecomposable full shifts give
  the atoms and entropy supplies the additive clock without target data.
- A1 fails: subset necklaces are the primitives, and the scalar cancellation
  cannot be lifted to a power-compatible, atom-equivariant primitive pairing.
- A2 is analytic: every finite subset shift has its declared scalar Fredholm
  determinant, exactly `product_p(1-x_p)` at `z=1`.
- A3 fails: there is no completed functional equation, Gamma factor, global
  target divisor theorem, counting law, or intrinsic Weil compression.
- A4 fails: no natural unitary, scattering, Hamiltonian, or self-adjoint lift
  is defined.

All target-zero metrics are strictly `not_applicable`. Route B is locked.

## Next smallest experiment

Stay within Symbolic Dynamics and freeze a genuinely chain-enhanced grammar
*before* cyclic reduction. Its differential and contraction must commute with
the full atom-permutation action and with temporal power maps. The first
decisive reruns are the same `p^2q^2` power ledger and `pqr` character test;
failure of either test stops that successor without any root computation.

## Verification

- Unit tests: 10/10 passed.
- Code/result checksum entries: 11/11 passed.
- CSV format: LF only.
- Exact arithmetic: integers and `Fraction` only.
- Riemann-zero data: none.
