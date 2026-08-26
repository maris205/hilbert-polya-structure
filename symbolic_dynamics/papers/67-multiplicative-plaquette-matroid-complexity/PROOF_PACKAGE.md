# Proof package

## Main claim

Let `a,b>=2` be coprime integers, let `K=F_q` be a finite field, and define

```text
X = {x in K^N : x_n-x_(an)-x_(bn)+x_(abn)=0 for every n>=1}.
```

Put

```text
R = {r>=1 : a does not divide r and b does not divide r},
B = {n>=1 : ab does not divide n}.
```

Then restriction `rho_B:X->K^B` is a topological-group isomorphism.  For an
arbitrary finite `F subset N`, write every `n in F` uniquely as
`n=r a^i b^j`.  For each root `r`, let `E_r(F)` be the resulting set of pairs
`(i,j)`, and form the bipartite graph `G_r(F)` with one row vertex for every
used `i`, one column vertex for every used `j`, and edge set `E_r(F)`.  If
`c_r(F)` is its number of connected components, then

```text
dim_K pi_F(X)
 = sum_r (|I_r(F)|+|J_r(F)|-c_r(F)),
|pi_F(X)| = q^dim.
```

The allowed finite labels are exactly those whose alternating sum on every
simple cycle of every `G_r(F)` is zero.  Here the coordinate matroid is the
vector matroid of the restricted evaluation maps `x -> x_n`, with ground set
`F`; it is the direct sum of the graphic matroids of the graphs `G_r(F)`.

If `mu` is normalized Haar measure on `X`, then

```text
H_mu(x_F)=dim_K(pi_F(X)) log q,
TC_mu(x_F)=sum_r beta_1(G_r(F)) log q.
```

Consequently, the coordinates in `F` are jointly independent if and only if
every `G_r(F)` is a forest.  In particular, every two distinct coordinates
are independent.

The main special cases are

```text
|pi_[1,N](X)| = q^(N-floor(N/(ab)))
```

and, for
`Q_r(M,N)={r a^i b^j:0<=i<M,0<=j<N}`,

```text
|pi_Q(X)|=q^(M+N-1),
TC_mu(x_Q)=(M-1)(N-1) log q.
```

## Status

**PROVABLE AS STATED.**

Every infinite assertion has a direct algebraic/topological proof below.
The deterministic companion program supplies finite regression checks only.

## Assumptions and notation

- `N={1,2,...}` and `N_0={0,1,...}`.
- `a,b>=2` and `gcd(a,b)=1`.
- `K` is an arbitrary field for the structural and rank theorems; it is the
  finite field `F_q` for counting and Shannon entropy.
- Products carry the product topology, and finite fields are discrete.
- `pi_F` denotes coordinate restriction to a finite set `F`.
- The cycle rank of a finite graph is
  `beta_1=|E|-|V|+number_of_components`.
- Shannon entropy uses natural logarithms.

## Dependency map

1. Unique root coordinates depend only on coprimality.
2. Global free coordinates depend on root coordinates and the integrated
   mixed-difference identity.
3. The finite-projection theorem depends on the vertex-potential
   representation and the rank of a finite incidence matrix.
4. The cycle characterization and graphic-matroid statement depend on a
   harmless sign change on the column vertices.
5. Haar entropy and independence depend on the finite-projection theorem and
   uniform Haar pushforward.
6. The prefix and rectangle formulas are independent specializations of the
   same rank theorem; the prefix formula also has a direct free-axis proof.

## Proof

### Step 1. Unique multiplicative root coordinates

For `n>=1`, let `i` be the largest integer for which `a^i` divides `n`, and
let `j` be the largest integer for which `b^j` divides `n`.  Coprimality makes
`a^i b^j` divide `n`; set

```text
r=n/(a^i b^j).
```

If `a` divided `r`, then `a^(i+1)` would divide `n`, contradicting maximality;
similarly `b` does not divide `r`.  Conversely, in a representation
`n=r a^i b^j` with `r in R`, the integer `r b^j` is not divisible by `a`:
since `gcd(a,b^j)=1`, divisibility by `a` would force `a|r`.  Hence `i` is
exactly the maximal `a`-power exponent of `n`, and similarly `j` is the
maximal `b`-power exponent.  The representation is unique.

Thus the map

```text
R x N_0 x N_0 -> N,   (r,i,j) -> r a^i b^j
```

is a bijection.

### Step 2. Integrate the plaquette equation

Fix `r in R` and write

```text
y_ij=x_(r a^i b^j).
```

The defining relation at `r a^i b^j` becomes

```text
y_ij-y_(i+1,j)-y_(i,j+1)+y_(i+1,j+1)=0.      (1)
```

Equation (1) says that the horizontal increment
`y_(i+1,j)-y_(i,j)` is independent of `j`.  Summing the increments from
`0` to `i-1` gives

```text
y_ij-y_0j=y_i0-y_00,
```

or

```text
y_ij=y_i0+y_0j-y_00.                           (2)
```

Conversely, every array defined by (2) satisfies (1).  Equivalently, after
the gauge choice `v_0=0`, all solutions are

```text
y_ij=u_i+v_j,
u_i=y_i0,
v_j=y_0j-y_00.
```

The formula works in every characteristic, including characteristic two.

### Step 3. Global product homeomorphism

In root coordinates, `ab` divides `r a^i b^j` exactly when `i>=1` and
`j>=1`.  Indeed, if `i=0`, then coprimality and `a` not dividing `r` prevent
`a` from dividing `r b^j`; the other case is symmetric.  Therefore `B`
consists precisely of the two axes in every root component.

Restriction `rho_B:X->K^B` is injective by (2).  Given arbitrary
`z in K^B`, define, for the unique root representation of `n`,

```text
x_(r a^i b^j)=z_(r a^i)+z_(r b^j)-z_r.        (3)
```

All three indices on the right belong to `B`, and (3) agrees with `z` when
`i=0` or `j=0`.  Step 2 shows that it defines a point of `X`, so restriction
is surjective.

Both maps are homomorphisms.  Restriction is continuous, and every output
coordinate of its inverse depends on only three input coordinates, so the
inverse is continuous in the product topology.  Hence `rho_B` is a
topological-group isomorphism.  The same argument can also be phrased as

```text
X is isomorphic to the product over r in R of
K^(N_0) x K^(N),
```

where the second factor records the positive part of the column axis.

### Step 4. Arbitrary finite projections

Fix a finite `F subset N`.  For each root represented in `F`, define

```text
E_r={(i,j):r a^i b^j in F},
I_r={i:(i,j) in E_r for some j},
J_r={j:(i,j) in E_r for some i}.
```

Let `G_r(F)` be the simple bipartite graph with left vertices `I_r`, right
vertices `J_r`, and one edge for each pair in `E_r`.  The restriction of a
component solution to `E_r` is the image of

```text
Phi_r:K^(I_r) direct_sum K^(J_r) -> K^(E_r),
Phi_r(u,v)_(i,j)=u_i+v_j.                      (4)
```

Every image in (4) extends to a global component solution by assigning
arbitrary values, say zero, to unused potentials.  Thus `im Phi_r` is exactly
the `r`-component of `pi_F(X)`.

On a connected component of `G_r(F)`, a kernel vector obeys
`u_i=-v_j` on every edge.  Connectivity forces all row potentials to equal
one scalar `t` and all column potentials to equal `-t`.  Hence the kernel has
one dimension per connected component.  Rank--nullity gives

```text
rank Phi_r=|I_r|+|J_r|-c_r.
```

Distinct roots use disjoint variables, so their ranks add.  This proves the
finite-projection dimension and, over `F_q`, the exact pattern count.

### Step 5. Cycle equations and the graphic matroid

Replace each column potential `v_j` by `-w_j`.  Then (4) becomes

```text
edge(i,j)=u_i-w_j,
```

the coboundary map for the orientation from row vertices to column vertices.
Its values telescope around every graph cycle.  In the original variables,
if a cycle is

```text
(i_1,j_1),(i_2,j_1),(i_2,j_2),...,(i_k,j_k),(i_1,j_k),
```

set `i_(k+1)=i_1`.  The corresponding condition is the unambiguous
alternating sum

```text
sum_(ell=1)^k [z_(i_ell,j_ell)-z_(i_(ell+1),j_ell)]=0.   (5)
```

In characteristic two, the minus signs equal plus signs and the same
statement remains valid.

Conversely, assume an edge labelling satisfies (5) on every cycle.  Choose a
spanning forest and a base vertex in each component.  Set its potential to
zero and integrate edge labels along the unique forest paths.  Every nonforest
edge closes one fundamental cycle, and (5) says that the integrated endpoint
potentials reproduce its label.  Hence every cycle-compatible labelling lies
in `im Phi_r`.

With potentials indexed by columns and edge values by rows, the rows of (4)
represent the restricted coordinate evaluation maps.  The transpose of this
matrix, after the column-vertex sign change, is an oriented vertex--edge
incidence matrix.  Its column matroid is the graphic matroid of `G_r(F)`, in
every characteristic.  The coordinate linear forms are independent exactly
on forests, and a basis is a maximal spanning forest.  Taking distinct roots
gives the direct sum of these graphic matroids.  Finally,

```text
codim pi_F(X)
 = sum_r (|E_r|-|I_r|-|J_r|+c_r)
 = sum_r beta_1(G_r(F)).                       (6)
```

The same representation gives the exact one-edge update law.  Deleting an
edge that lies on a cycle preserves graphic rank and lowers cycle rank by one;
deleting a bridge lowers graphic rank by one and preserves cycle rank.  On
addition, an edge whose endpoints were already connected preserves rank and
raises cycle rank by one.  Any other new edge raises rank by one and preserves
cycle rank.  This includes edges introducing a vertex or a new root component.

### Step 6. Haar entropy and independence

Let `mu` be normalized Haar measure on the compact group `X`.  A continuous
surjective homomorphism from a compact group to a finite group sends Haar
measure to normalized counting measure.  Therefore `pi_F(mu)` is uniform on
the subspace `pi_F(X)`, and

```text
H_mu(x_F)=dim_K(pi_F(X)) log q.                (7)
```

Every one-coordinate projection is all of `F_q`, so every coordinate has
entropy `log q`.  The total correlation is consequently

```text
TC_mu(x_F)
 = sum_(n in F) H_mu(x_n)-H_mu(x_F)
 = (|F|-dim_K pi_F(X)) log q
 = sum_r beta_1(G_r(F)) log q.                 (8)
```

A finite collection of uniform finite-valued variables is jointly independent
if and only if its joint entropy is the sum of its marginal entropies.  By
(8), this happens exactly when every cycle rank is zero, equivalently when
every `G_r(F)` is a forest.  Any two distinct coordinates give at most two
distinct edges of simple bipartite graphs, hence a forest; all distinct pairs
are independent.  A four-corner rectangle is a cycle and has one deterministic
plaquette relation, so pairwise independence does not extend to full
independence.

### Step 7. Arithmetic prefixes

For `F_N={1,...,N}`, every coordinate in `F_N` is determined by the free
coordinates `B intersect F_N`: formula (3) uses only indices no larger than
the target coordinate.  Conversely every assignment on `B intersect F_N`
extends by choosing arbitrary free coordinates outside the prefix and applying
(3).  Hence

```text
|pi_F_N(X)|=q^|B intersect F_N|
           =q^(N-floor(N/(ab))).               (9)
```

As an independent check of the local constraint-matrix rank, the prefix
contains one internally visible constraint for each `n<=N/(ab)`.  This check
does not by itself prove that every local solution extends; that extension was
proved in Step 3.  In a nontrivial linear combination, choose the largest index
`n` with nonzero coefficient.  The coordinate `abn` cannot occur in a row
with a smaller index except as that row's own pivot, and any row in which it
occurs as `m`, `am`, or `bm` has index larger than `n`; its coefficient is
zero by maximality.  Thus the coefficient at `abn` forces the chosen row
coefficient to vanish, a contradiction.  The rows are independent and have
rank `floor(N/(ab))`.  Combined with Step 3 and the first paragraph of this
step, this confirms that the local kernel is exactly the prefix projection.

Dividing the logarithm of (9) by `N` gives

```text
h_prefix=(1-1/(ab)) log q.                     (10)
```

Equation (10) is an arithmetic-prefix complexity.  It is not labelled a
topological entropy without a separately specified invariant action and
averaging sequence.

### Step 8. Exponent rectangles

For a root `r` and `M,N>=1`, let

```text
Q_r(M,N)={r a^i b^j:0<=i<M,0<=j<N}.
```

Its incidence graph is the connected complete bipartite graph `K_{M,N}`.
Step 4 gives

```text
dim pi_Q(X)=M+N-1,
|pi_Q(X)|=q^(M+N-1).                           (11)
```

The cycle rank is

```text
MN-(M+N)+1=(M-1)(N-1),                        (12)
```

so (8) gives the stated Haar total correlation.  Formula (11) has boundary
order in exponent coordinates:

```text
(1/(MN)) log |pi_Q(X)|=((M+N-1)/(MN)) log q -> 0
```

when both side lengths diverge.  Rectangles on distinct roots contribute
independent direct-product factors, so their dimensions and logarithmic
counts add.

## Stop rules

- Do not remove the coprimality assumption without replacing the root
  decomposition.
- Do not call the arithmetic-prefix rate a multiplicative topological entropy.
- Do not call the exponent-box boundary law a prefix entropy.
- Do not present the elementary factorization or `u_i+v_j` representation as
  a priority claim.
- Do not convert the bounded exact-source search into a novelty certificate.
