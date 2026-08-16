# Paper 38 derivation package — SD-C40

## 1. Original HNN tree

Fix

```text
G_r=<u,v | vuv^{-1}=u^r>,  A=<u>≅Z.
```

The original loop of groups has incidence indices `1` and `r`.  The
Bass--Serre tree `T_r` therefore has degree `r+1`; `r=1` gives a line.  There
is one vertex orbit and one unoriented-edge orbit.  Every vertex and edge
stabilizer is infinite cyclic.

The height homomorphism and modular convention are

```text
h(u)=0, h(v)=1, Delta(g)=r^{h(g)}.
```

The full tree, the quotient loop, the set of hyperbolic conjugacy classes,
and the common-end action are kept as four distinct state spaces.

## 2. Full-tree shift and trace obstruction

For actual oriented edges, define

```text
B delta_e = sum_{f:e->f reduced} delta_f.
```

A period-`n` sequence would produce a positive reduced closed tree path, so
the periodic ledger is empty.  Nevertheless the operator is not zero.  For
infinitely many edges with distinct terminal vertices,

```text
<B delta_ei, B delta_ej> = 0, i!=j,
||B delta_ej||^2 = r.
```

Thus `B` is noncompact and not trace class.  The formal equalities

```text
(B^n)_{e,e}=0
```

do not imply an operator trace, because the diagonal sum is not a trace-class
trace.  Consequently the formal expression

```text
exp(sum_{n>=1} z^n Tr(B^n)/n)=1
```

is not an ordinary Fredholm determinant.

The canonical per-step modular weights are `r^{-s}` and `r^s`.  They are
nonzero constants on the two oriented step types, so the same orthogonal
family proves noncompactness.  Absolute-height damping would select a root
and is not this cocycle.

## 3. Tree-lattice determinant firewall

Let `rho_r:G_r->Aut(T_r)` be the action homomorphism and let
`H_r=rho_r(G_r)`.  For a subgroup of the automorphism group of a locally
finite tree,

```text
H discrete in Aut(T)  iff  one/every H-vertex stabilizer is finite.
```

The criterion applies to the image `H_r`, so faithfulness must be handled
before using the stabilizers of the original `G_r`-action.  For `r>=2`,

```text
ker(rho_r)=core_{G_r}(A)
  subset intersection_{n>=0} v^n A v^{-n}
  = intersection_{n>=0}<u^{r^n}>={1}.
```

Thus the action is faithful.  Its image stabilizer at the base vertex is the
infinite group `rho_r(A)≅Z`, and `H_r` is non-discrete in `Aut(T_r)`.

For `r=1`, instead, `G_1=A times <v>≅Z^2`, the tree is a line, and

```text
ker(rho_1)=A=<u>,  H_1≅<v>≅Z.
```

The image `H_1` is the discrete translation subgroup of `Aut(T_1)`.  The
original `G_1`-action nevertheless has infinite vertex and edge stabilizers
`A`, hence is non-proper and does not satisfy the finite-stabilizer
tree-lattice action hypotheses.  Passing to `H_1=G_1/A` would change the
acting group and the group-conjugacy ledger.

For `r>=2`, the ascending action fixes one distinguished end.  Its
zero-translation kernel includes

```text
N_r=union_{j>=0} v^{-j} A v^j ≅ Z[1/r].
```

Hence the standard end average with denominator `|Gamma_epsilon^0|` falls
outside its finite-cardinality definition.  For `r=1`, the action kernel
`A=<u>` already fixes the whole line and is infinite.  Replacing either
infinite denominator by zero is a `PROVES_TOO_MUCH` convention, not a
derivation.

## 4. Semidirect-product conjugacy boundary

For `r>=2`, identify

```text
G_r=Z[1/r] semidirect Z,
(a,l)(b,k)=(a+r^l b,l+k),
(a,l)^{-1}=(-r^{-l}a,-l).
```

Then

```text
(c,m)(b,k)(c,m)^{-1}
  =(r^m b+(1-r^k)c,k).
```

At height `k>0`, addition by `(1-r^k)c` passes to the quotient

```text
Q_{r,k}=Z[1/r]/(r^k-1)Z[1/r].
```

Since `gcd(r,r^k-1)=1`, every localized residue has an integer representative
and

```text
Q_{r,k}≅Z/(r^k-1)Z.
```

The remaining conjugation by height `m` is multiplication by `r^m`.

## 5. Residues, necklaces, and Burnside

Let `M=r^k-1`.  Multiplication by `r` on `Z/MZ` has exact order `k`.  Its
`j`th power fixes

```text
gcd(r^j-1,M)=r^{gcd(j,k)}-1
```

residues.  Burnside gives

```text
C_r(k)=(1/k)sum_{j=0}^{k-1}(r^{gcd(j,k)}-1).
```

For digits `0<=d_i<r`, set

```text
Phi(d_0...d_{k-1})=sum_{i=0}^{k-1}d_i r^i mod M.
```

Cyclic rotation corresponds to multiplication by `r`.  The integer range of
the digit sum is `[0,M]`, so `Phi` is one-to-one except that `0^k` and
`(r-1)^k` both map to zero.  Therefore

```text
C_r(k)=N_r(k)-1,
N_r(k)=(1/k)sum_{j=0}^{k-1}r^{gcd(j,k)}.
```

## 6. Primitive roots and Euler product

If a digit word of length `d` represents `b`, its `m`-fold repetition at
`k=md` represents

```text
b(1+r^d+...+r^{(m-1)d}).
```

The same geometric sum is the first coordinate of `(b,d)^m`.  Minimal digit
period therefore matches primitive group height, modulo conjugacy.  With
`P_r(k)` denoting primitive classes,

```text
C_r(k)=sum_{d|k}P_r(d),
P_r(1)=r-1,
P_r(k)=(1/k)sum_{d|k}mu(d)r^{k/d}, k>1.
```

The Witt necklace identity yields

```text
product_{k>=1}(1-z^k)^{-P_r(k)}=(1-z)/(1-rz).
```

Equivalently, ordinary primitive necklace counts have `r` degree-one
classes; merging the two endpoint words removes one and multiplies the
standard product `1/(1-rz)` by `1-z`.

## 7. Modular rescaling

At positive height `k`, the canonical modular weight is

```text
Delta^{-s}=r^{-sk}.
```

It depends only on the same integer already used as the orbital length.  The
weighted product is therefore

```text
Z_{+,r,s}(z)
 = product_{k>=1}(1-r^{-sk}z^k)^{-P_r(k)}
 = Z_{+,r}(r^{-s}z)
 = (1-r^{-s}z)/(1-r^{1-s}z).
```

At `s=1` it becomes `(1-z/r)/(1-z)`.  No cancellation or new support appears;
the zero and pole simply rescale with the index.

## 8. Balanced, prime/composite, and generic controls

For `r=1`, `G_1≅Z^2`.  At each positive height, `b in Z` gives a distinct
conjugacy class, so the orbital coefficient is infinite.  The full-tree
ledger remains empty and its line Hashimoto operator remains noncompact.

For all `r>=2`, the same polynomial formulas govern prime and composite
values.  The first six total/primitive rows used in the writer audit are

| `r` | `C_r(1:6)` | `P_r(1:6)` |
|---:|---|---|
| 2 | 1, 2, 3, 5, 7, 13 | 1, 1, 2, 3, 6, 9 |
| 3 | 2, 5, 10, 23, 50, 129 | 2, 3, 8, 18, 48, 116 |
| 4 | 3, 9, 23, 69, 207, 699 | 3, 6, 20, 60, 204, 670 |
| 5 | 4, 14, 44, 164, 628, 2634 | 4, 10, 40, 150, 624, 2580 |
| 6 | 5, 20, 75, 335, 1559, 7825 | 5, 15, 70, 315, 1554, 7735 |

These values are checks of one generic index law, not evidence for a
prime/composite classifier.

## 9. Translation length and marker collision

Let `beta` be the Busemann height on the tree.  Since one edge changes `beta`
by one,

```text
ell_T(a,k)>=|k|.
```

Choose `j>=0` with `r^j a=m in Z`.  Conjugation by `v^j` gives `(m,k)`.  At
the base vertex, `u^m` fixes and `v^k` travels `|k|` edges, proving

```text
ell_T(a,k)=|k|.
```

Thus every `u^m` has new length zero and every `u^m v` has new length one.
The old displayed generator paths have lengths `m` and `m+1`.  The defining
relator has a path of `r+3` old steps but tree translation length zero.  The
markers are not transportable.

## 10. Versioned exact audit boundary

The original external separated prototype seed verifies:

- `277/277` exact checks;
- 11 parameter rows;
- 18 deliberate GBS controls;
- 64 seeded random one-relator eligibility controls;
- residue/Burnside agreement through the frozen direct range;
- primitive/repetition and rational-product identities through degree 12;
- finite-tree and orthogonal-column certificates;
- marker collisions; and
- byte-identical fresh A/B outputs with legacy scientific SHA-256
  `3485a1d925924459ce92ff3aeddb31302277589d61bd9d961ecb823b1e5bb089`.

The `3485...` digest is retained only as external seed provenance.  Its
action-boundary assertion contained the known overbroad `r=1`
image-non-discreteness claim.  The corrected authority evaluator implements
the two cases derived in Section 3, retains the `277/277` assertion count,
and has scientific SHA-256
`a9ffa66d826bcaf8eef0b00991aafa46cdbeaca7014430c68aacf070446adf24`.
The corrected digest, not the legacy seed, is the authority result eligible
for downstream integration.

The exact program does not infer an infinite theorem from finite truncation.
The no-cycle, noncompactness, `r`-split image/properness boundary, and all-`k`
necklace statements are proved independently.

## 11. Route consequence

```text
A0 = STRUCTURAL_ARITHMETIC_RELATION
A1 = FAIL  (empty full tree; generic/divergent orbital substitute)
A2 = FAIL  (no ordinary full-tree Fredholm ownership)
A3 = FAIL  (no control-robust selective sector)
A4 = FAIL  (new marker incompatible with inherited clock)
```

Therefore `ROUTE_A_REJECTED`, Route B is locked, and
`CLOSE_ENTIRE_AFFINE_BRANCH` is terminal.
