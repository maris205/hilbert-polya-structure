# Paper 38 proof package — SD-C40

## 1. Scope and notation

For `r>=1`, let

```text
G_r = BS(1,r) = <u,v | vuv^{-1}=u^r>
```

and let `T_r` be the Bass--Serre tree of this original ascending HNN
splitting over `A=<u>≅Z`.  The full oriented-edge Hashimoto operator is

```text
B delta_e = sum_{o(f)=t(e), f!=bar(e)} delta_f
```

on `ell^2(E^or T_r)`.  The symbolic system is the full two-sided sequence of
actual oriented tree edges with this transition rule.  It is not the quotient
loop, a graph-of-groups edge space, or a group-conjugacy ledger.

The canonical height homomorphism is `h(u)=0`, `h(v)=1`.  We choose the
modular convention `Delta(g)=r^{h(g)}`.  Replacing `Delta` by its inverse
changes `s` to `-s` below and changes no conclusion.

## 2. Main theorem

### Theorem — Bass--Serre terminal trilemma

For every `r>=1`, the presentation-canonical full-tree candidate has the
following properties.

1. Its positive-length primitive periodic ledger is empty.
2. Its undamped Hashimoto operator is noncompact and not trace class.
3. Every nonzero per-step weighting supplied only by the canonical modular
   cocycle remains noncompact and non-trace-class.
4. The ordinary Fredholm determinant `det(I-zB)` and its allowed modular
   analogue are therefore not owned.
5. Bass and Clair--Mokhtari-Sharghi tree-lattice determinants cannot be
   imported as same-object evidence.  For `r>=2`, the action is faithful and
   its image in `Aut(T_r)` is non-discrete.  For `r=1`, the action has kernel
   `<u>`, its translation image `Z` is discrete, but the original `Z^2` action
   is non-proper and fails the finite-stabilizer hypotheses; quotienting to
   the image changes the acting group and orbital ledger.
6. If recurrence is replaced by positive-height group conjugacy classes, then
   `r>=2` gives the generic necklace product `(1-z)/(1-rz)`, while `r=1`
   gives infinitely many classes at every positive height.
7. Bass--Serre translation length is `|h(g)|` and is incompatible with the
   old Cayley generator-step marker.

Consequently the candidate has no nonempty source-selective primitive sector
and no same-object ordinary Fredholm determinant.  The strict route is
rejected and the entire affine branch closes.

## 3. Full-tree periodic emptiness (`SD-C40-C1`)

### Lemma 1

The full oriented-edge geodesic shift on a tree has no periodic point of
positive period.

### Proof

Let `(e_i)_{i in Z}` be a period-`n` point.  The transition rule makes
`e_0,...,e_{n-1}` a reduced edge path.  Periodicity gives
`e_n=e_0`, so the terminal vertex of `e_{n-1}` equals the initial vertex of
`e_0`.  One period is therefore a positive reduced closed path.  A connected
graph is a tree precisely when it has no such path.  Contradiction.  The
primitive ledger is empty. `square`

The statement concerns actual edges of the full tree.  A path that closes
only after applying a group element belongs to an orbital or quotient
ledger, not to this shift.

## 4. Noncompactness and Fredholm failure (`SD-C40-C2`)

### Lemma 2

The full-tree Hashimoto operator is noncompact.  More precisely, there is an
orthonormal edge family `(delta_{e_j})` for which the vectors
`B delta_{e_j}` are pairwise orthogonal and have squared norm `r`.

### Proof

The original HNN loop has incidence indices `1` and `r`, so `T_r` is
`(r+1)`-regular for `r>=2` and is a line for `r=1`.  Choose infinitely many
oriented edges with distinct terminal vertices; edges along a ray suffice.
Every basis edge in the support of `B delta_{e_j}` starts at `t(e_j)`.
Distinct terminal vertices therefore give disjoint supports.  At each
terminal vertex there are `deg(t(e_j))-1=r` legal continuations, whence

```text
||B delta_{e_j}||_2^2 = r.
```

The image sequence has pairwise distance `sqrt(2r)` and no convergent
subsequence.  Thus `B` is not compact.  Since every trace-class operator is
compact, `B` is not trace class. `square`

### Lemma 3

A nonzero scalar edge weighting obtained only from the canonical modular
cocycle does not make the full-tree Hashimoto operator trace class.

### Proof

A geodesic step changes the HNN height by `+1` or `-1`.  At a fixed cocycle
parameter `s`, the permitted transition magnitudes therefore belong to the
two-element set

```text
{r^{-Re(s)}, r^{Re(s)}}
```

for `r>=2`; for `r=1` the magnitude is one.  Restrict the family in Lemma 2
to one oriented transition type with nonzero weight.  The weighted images
remain pairwise orthogonal and have one fixed positive norm.  The same
compactness contradiction applies. `square`

A weight depending on absolute distance from a chosen root is not the
canonical cocycle on one transition: it introduces a basepoint.  Such radial
damping is forbidden by the source lock and would define a different object.

### Corollary 1

Neither `det(I-zB)` nor an allowed modularly weighted version is an ordinary
Fredholm determinant.

The usual Fredholm determinant `det(I+K)` requires trace-class `K`.  The fact
that the formal diagonal of every `B^n` vanishes does not supply a trace: the
operator is not trace class.  Declaring every such formal trace to be zero
and the determinant to be one is an unowned regularization.

## 5. Discrete tree-lattice hypothesis failure (`SD-C40-C3`)

Let `rho_r:G_r->Aut(T_r)` be the action homomorphism and
`H_r=rho_r(G_r)`.  Vertices of `T_r` are cosets of `A`, so the stabilizer for
the original action is

```text
Stab(gA) = gAg^{-1} ≅ Z.
```

Edge stabilizers are conjugates of the associated cyclic subgroup and are
also infinite.  The compact-open criterion says that a subgroup of the
automorphism group of a locally finite tree is discrete if and only if one
(equivalently every) stabilizer inside that subgroup is finite.  It applies
to `H_r`, not directly to a possibly nonfaithful `G_r`-action.

For `r>=2`, the kernel is the core of `A` and satisfies

```text
ker(rho_r) = core_{G_r}(A)
  subset intersection_{n>=0} v^n A v^{-n}
  = intersection_{n>=0}<u^{r^n}> = {1}.
```

The action is therefore faithful.  The base-vertex stabilizer in `H_r` is
`rho_r(A)≅Z`, so the faithful image is non-discrete in `Aut(T_r)`.

For `r=1`, the relation makes `G_1=A times <v>≅Z^2` and `T_1` is a line.
Every element of `A=<u>` fixes the line pointwise, while `v` translates it by
one edge.  Hence

```text
ker(rho_1)=A,  H_1≅<v>≅Z,
```

and `H_1` is discrete.  The original `G_1`-action is nevertheless non-proper:
every vertex and edge stabilizer contains the infinite kernel `A`.  It is not
a discrete tree-lattice action with finite stabilizers.  Replacing it by the
faithful image `G_1/A` changes the acting group and collapses the distinct
elements `(b,k)` in the original conjugacy ledger.

The distinction is decisive.  Bass's uniform tree-lattice zeta and the
Clair--Mokhtari-Sharghi extension begin with a discrete group action and use
finite stabilizer volumes.  Their determinant cannot be relabeled as the
ordinary full-tree Fredholm determinant.

For `r>=2`, the ascending action also fixes a common end.  Its
signed-translation kernel contains

```text
union_{j>=0} v^{-j} A v^j ≅ Z[1/r].
```

Thus the fixed-end kernel in the standard end weight is infinite as well.
The expression `1/|G_epsilon^0|` is not defined by the finite-cardinality
formula.  At `r=1`, the infinite kernel `A` already fixes every vertex and
edge, so the same finite-stabilizer obstruction remains even though the
quotient image is discrete.

### PROVES_TOO_MUCH corollary

Interpreting `1/|Z|` as zero erases every vertex, edge, and end term for every
GBS control with infinite cyclic stabilizers.  It produces the same trivial
answer for ascending, balanced, and non-ascending presentations.  This rule
destroys the invariant and is rejected.

## 6. Positive-height orbital classification (`SD-C40-C4`)

This section deliberately changes objects.  It counts conjugacy classes in
the group, not periodic points of the full-tree edge shift.

For `r>=2`, use

```text
G_r ≅ Z[1/r] semidirect Z,
(a,l)(b,k) = (a+r^l b,l+k).
```

Direct multiplication gives

```text
(c,m)(b,k)(c,m)^{-1} = (r^m b + (1-r^k)c,k).
```

At a fixed positive height `k`, conjugacy classes are therefore the orbits of
multiplication by `r` in

```text
Z[1/r]/(r^k-1)Z[1/r] ≅ Z/(r^k-1)Z.
```

The isomorphism holds because `r` is invertible modulo `r^k-1`.

### Lemma 4 — Burnside count

Let `C_r(k)` be the number of positive-height conjugacy classes at height
`k`.  Then

```text
C_r(k) = (1/k) sum_{j=0}^{k-1} (r^{gcd(j,k)}-1)
       = N_r(k)-1,
```

where `N_r(k)` is the number of length-`k` necklaces on `r` symbols.

### Proof

Multiplication by `r` has order exactly `k` modulo `r^k-1`: for
`0<j<k`, the positive integer `r^j-1` is smaller than `r^k-1`.  The fixed
points of its `j`th power solve

```text
(r^j-1)x = 0 mod (r^k-1),
```

so their number is

```text
gcd(r^j-1,r^k-1) = r^{gcd(j,k)}-1.
```

Burnside's lemma proves the first equality.  The usual necklace count has the
same sum without `-1` in each summand, proving the second. `square`

The digit map sends a word `(d_0,...,d_{k-1})` to
`sum_i d_i r^i mod r^k-1`.  Its only duplicated endpoint is `0^k` versus
`(r-1)^k`; cyclic rotation corresponds to multiplication by `r`.  This gives
the explicit necklace model.

### Lemma 5 — primitive and repetition ledger

Let `P_r(k)` count primitive positive-height group-conjugacy classes.  Then

```text
P_r(1) = r-1,
P_r(k) = (1/k) sum_{d|k} mu(d) r^{k/d},  k>1,
C_r(k) = sum_{d|k} P_r(d).
```

### Proof

A necklace of minimal period `d|k` is the `k/d`-fold repetition of a unique
primitive necklace.  Under the digit map, repetition multiplies the base
value by `1+r^d+...+r^{k-d}`, exactly the translation coordinate obtained by
taking the corresponding semidirect-product power.  The endpoint collision
belongs to period one, so for `k>1` the primitive classes are the ordinary
primitive `r`-ary necklaces.  Möbius inversion gives the formulas. `square`

### Proposition 1 — rational orbital collapse

The positive-height primitive Euler product is

```text
Z_{+,r}(z) = product_{k>=1}(1-z^k)^{-P_r(k)}
           = (1-z)/(1-rz).
```

### Proof

The classical necklace identity uses primitive counts `L_r(k)` and gives

```text
product_{k>=1}(1-z^k)^{-L_r(k)} = 1/(1-rz).
```

Here `P_r(k)=L_r(k)` for `k>1`, while `P_r(1)=L_r(1)-1=r-1` because the two
endpoint words merge.  Removing one degree-one primitive factor multiplies
the product by `1-z`. `square`

The modular weight `Delta^{-s}=r^{-sk}` only substitutes
`z -> r^{-s}z`:

```text
Z_{+,r,s}(z) = (1-r^{-s}z)/(1-r^{1-s}z).
```

This law is reproduced by every matched cyclic index-`r` ascending HNN
control.  It depends smoothly on the numeric index and has no prime/composite
fork or presentation-selective residue.  It is therefore generic under the
frozen verdict rule.

## 7. Balanced and marker controls (`SD-C40-C5`)

For `r=1`, the group is `Z^2` and conjugacy is equality.  At every positive
height `k`, the elements `(b,k)`, `b in Z`, give infinitely many classes.
The orbital product is not locally finite.  Quotienting the infinite kernel
leaves only the generic line translation and changes the object.

### Proposition 2 — translation length

Every `g=(a,k)` has Bass--Serre translation length `|k|`.

### Proof

The Busemann height changes by one on each tree edge, so every displacement is
at least `|k|`.  If `k=0`, then `a in Z[1/r]` lies in a conjugate of `A` and
fixes a vertex.  If `k!=0`, choose `j>=0` with `r^j a=m in Z`.  Conjugation by
`v^j` sends `g` to `(m,k)=u^m v^k`.  The element `u^m` fixes the base vertex,
and `v^k` moves it through exactly `|k|` HNN edges.  Translation length is
conjugacy invariant, so the lower bound is attained. `square`

Hence

```text
ell_T(u^m)=0,
ell_T(u^m v)=1,
ell_T(vuv^{-1}u^{-r})=0.
```

The corresponding displayed Cayley paths have `m`, `m+1`, and `r+3`
generator steps.  The new tree clock is many-to-one and cannot inherit the
old marker.

## 8. Controls, route, and non-claims

The same full-tree emptiness and non-Fredholm proof applies to the deliberate
`BS(p,q)` controls, whose trees have degree `p+q` and infinite cyclic
stabilizers.  Random one-relator words without a canonical cyclic GBS form
are ineligible rather than negative examples.  Prime and composite rows obey
one necklace law; `r=1` is the divergent boundary.

The theorem does not exclude every zeta function, determinant, or invariant
associated with `BS(1,r)`.  In particular, finite quotients, graph-of-groups
operators, von Neumann determinants, groupoid traces, double-coset Dirichlet
series, and finite-total-weight graph zetas are different categories.  It
constructs no arithmetic Euler product, target divisor, functional equation,
self-adjoint carrier, critical-line mechanism, or RH implication.

The strict decision is

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL),
overall=ROUTE_A_REJECTED,
route_b_invocation_allowed=false,
branch=CLOSE_ENTIRE_AFFINE_BRANCH.
```
