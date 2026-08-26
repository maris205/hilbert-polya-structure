# Narrative report

## Problem

Multiplicative symbolic constraints are naturally sampled in two incompatible
geometries.  Arithmetic prefixes retain coordinates `1,...,N`; valuation
coordinates instead arrange one multiplicative component in an exponent
lattice.  For the finite-field plaquette rule

```text
x_n-x_an-x_bn+x_abn=0,
```

the two geometries initially give very different counts: a positive-volume
prefix exponent and a boundary-order exponent rectangle.  The task is to
explain both without treating either as an isolated calculation.

## Structural reduction

Coprimality gives a unique representation `n=r a^i b^j` with neither `a` nor
`b` dividing `r`.  On a fixed root, the constraint is the vanishing mixed
difference on `N_0^2`.  Its global solutions are exactly

```text
y_ij=y_i0+y_0j-y_00.
```

Thus the two coordinate axes are free.  Across all roots, the free axes are
precisely the integers not divisible by `ab`, and restriction to those
coordinates is an explicit topological-group isomorphism.

## Main advance

The manuscript does not stop at prefixes and rectangles.  For an arbitrary
finite set `F`, each selected coordinate becomes an edge of a root-wise
bipartite graph: the `a`-exponent is its row endpoint and the `b`-exponent is
its column endpoint.  Allowed labels are vertex-potential sums.  Their
dimension is therefore `|V|-components`, and their codimension is the cycle
rank.  Equivalently, the linear-dependence matroid of the selected coordinates
is a direct sum of graphic matroids.  Consequently, deleting a cycle edge
preserves projection dimension while deleting a bridge lowers it by one, with
the dual dichotomy for adjoining a coordinate.

This arbitrary-shape theorem provides an exact probabilistic interpretation.
Under Haar measure, every finite image is uniform, every forest of coordinates
is jointly independent, and each graph cycle contributes exactly one
finite-field unit of total correlation.  In particular, all distinct pairs of
coordinates are independent even though a four-corner plaquette satisfies one
deterministic relation.

## Specializations

For the prefix `[1,N]`, exactly `floor(N/(ab))` coordinates are nonfree, so

```text
|pi_[1,N](X)|=q^(N-floor(N/(ab))).
```

For an `M x N` exponent rectangle on one root, the incidence graph is
`K_(M,N)`, so

```text
|pi_rectangle(X)|=q^(M+N-1),
cycle defect=(M-1)(N-1).
```

These are two normalizations of the same rank invariant, not two competing
entropy formulas.

## Residual contribution and restraint

The surrounding multiplicative-subshift, entropy, valuation-coordinate, and
correlation frameworks are established context.  The internal residual result
is the explicit arithmetic pullback together with the all-finite-shape
graphic-matroid projection law and its Haar consequences.  A bounded search
did not locate this exact theorem, but the manuscript makes no “first” or
worldwide novelty claim.  External release remains on hold for specialist
review.
