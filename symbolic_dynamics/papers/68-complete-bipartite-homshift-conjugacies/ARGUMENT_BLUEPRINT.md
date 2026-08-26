# Argument blueprint

## A. Structural reduction

Every nearest-neighbour step changes target part. Since all lattice paths from `0` to `v` have parity `sum(v_i) mod 2`, a configuration has one of two global phases. On every nonempty finite shape, including a disconnected one, the restriction inherits that single global phase; colours are otherwise free. Thus its extendible-pattern count is `m^|F cap E| n^|F cap O| + n^|F cap E| m^|F cap O|`, not a product over induced components.

## B. Dimer classification

Assume `mn=rs` and choose `f:A x B -> A' x B'`. Every `A`-site anchors the edge to `v+e_1`; apply `f` to that ordered pair and distribute its two outputs back over the same dimer. Membership in `A` is visible locally, so translating a point translates its anchors. The construction with `f^{-1}` is the inverse. Entropy gives the converse.

## C. Finite-dependence rigidity

At every even displacement `u`, the indicators `1{x_0 in A}` and `1{x_u in A}` coincide. At distance beyond the dependence range they are independent, forcing `p=p^2`. Hence phase is deterministic. Odd translations exchange phases, giving the subgroup obstruction; parity-wise iid colours give sufficiency.

## D. Thermodynamics and periodic data

Replace cardinalities `m,n` in the global-phase restriction count by weighted sums `Z_A,Z_B`. Følner parity densities give pressure. A joint dimer Gibbs inequality and entropy-rate equality force the two conditional product measures, while full-action invariance forces their equal mixture. On `Z^d/L`, odd periods are impossible; if `L<=E`, the quotient has `[E:L]` vertices of each parity.
