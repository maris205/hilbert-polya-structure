# Argument blueprint

## Main dependency graph

```text
coprime multipliers a,b
    -> unique n=r a^i b^j decomposition
    -> N splits into independent root components
    -> plaquette rule becomes Delta_i Delta_j y=0
    -> y_ij=y_i0+y_0j-y_00
    -> axes are global free coordinates
    -> restriction X -> F_q^{n:ab does not divide n} is a homeomorphism

finite coordinate set F
    -> root-wise edge sets E_r in N_0 x N_0
    -> bipartite incidence graphs G_r(F)
    -> edge labels are vertex-potential sums
    -> rank = |vertices|-components
    -> codimension = cycle rank
    -> coordinate matroid = direct sum of graphic matroids
    -> exact bridge/cycle deletion and addition laws
    -> Haar entropy and independence are exact

F=[1,N]
    -> free coordinates are exactly n<=N with ab not dividing n
    -> |pi_F(X)|=q^{N-floor(N/(ab))}

F={r a^i b^j:0<=i<M,0<=j<N}
    -> G_r(F)=K_{M,N}
    -> |pi_F(X)|=q^{M+N-1}
    -> cycle defect=(M-1)(N-1)
```

## Exact component integration

For a root `r`, write `y_ij=x_{r a^i b^j}`.  The defining equation becomes

```text
y_ij-y_(i+1,j)-y_(i,j+1)+y_(i+1,j+1)=0.
```

The same identity on the rectangle from `(0,0)` to `(i,j)` telescopes to

```text
y_ij=y_i0+y_0j-y_00.
```

Conversely this formula satisfies every plaquette equation.  The coordinates
on the two axes, with the origin counted once, are therefore free.  Under the
integer decomposition, their union is exactly `B={n:ab does not divide n}`.
The inverse to restriction is coordinatewise:

```text
x_(r a^i b^j)=z_(r a^i)+z_(r b^j)-z_r.
```

This proves both algebraic bijectivity and continuity in the product topology.

## Arbitrary finite-shape layer

For each root `r`, make a bipartite graph with row vertices `i`, column
vertices `j`, and an edge `(i,j)` for every selected coordinate
`r a^i b^j`.  The map from vertex potentials to edge values is

```text
(u_i,v_j) -> (u_i+v_j)_(i,j).
```

On each connected component its kernel consists of one scalar choice:
`u_i=t` on every row vertex and `v_j=-t` on every column vertex.  Hence the
image dimension is `|I|+|J|-c`.  Rescaling the column variables by `-1`
turns the matrix into an oriented incidence matrix, whose row matroid is the
graphic matroid.  Fundamental cycles give all compatibility relations.

## Haar layer

Normalized Haar measure pushes forward uniformly to every finite image.
Every single coordinate is uniform on `F_q`; therefore

```text
H(x_F) = rank(F) log q,
TC(x_F) = (|F|-rank(F)) log q = cycle_rank(F) log q.
```

Thus a finite family is jointly independent exactly when its edge set is a
forest.  Since a simple bipartite graph has no two-edge cycle, any two
distinct coordinates are pairwise independent, although every four-corner
plaquette is dependent.

## Geometry firewall

- Prefixes `[1,N]` are arithmetic intervals and yield a positive normalized
  prefix rate.
- Exponent rectangles are boxes inside one multiplicative orbit component
  and yield a boundary-order count.
- Neither calculation is automatically a topological or measure entropy for
  a multiplicative semigroup action.  Such an entropy needs its own action and
  averaging convention.

## Proof risk policy

- Coprimality is structural; without it, root coordinates need not be unique.
- The field is finite only for counting and Shannon entropy.  The rank theorem
  itself holds over any field.
- No finite enumeration is used to infer an infinite result.
- Exact-source search remains bounded and supplies no priority certificate.
