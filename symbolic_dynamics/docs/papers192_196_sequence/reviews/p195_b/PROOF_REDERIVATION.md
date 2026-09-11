# P195 Review-B proof rederivation

This proof route starts from oriented edge-size arrays and labelled shuffles,
not from repeated deletion of an edge or Review A's implementation.

## 1. Oriented side-size array

Root the underlying tree temporarily at label `1` and compute every subtree
size `s(v)`.  For a parent-child edge `uv`, the oriented size from `u` toward
`v` is `s(v)` and the reverse oriented size is `n-s(v)`.  This single array
gives the literal update from every distinguished root.

When `n` is odd the two entries on an edge have opposite parity, so every edge
has one arrow toward its odd side.  A selected orbit cannot traverse the
reverse edge and cannot close a cycle in a tree; it ends exactly at a vertex
whose incident outgoing sizes are all even.

When `n` is even the two entries have the same parity.  Keeping the odd/odd
edges gives a forest `H`.  At a vertex the incident side sizes sum to `n-1`,
so an odd number are odd and every `H` degree is positive and odd.  Least-
neighbour motion has no fixed point, and a directed cycle of length at least
three would be an undirected cycle in `H`.  Thus recurrence is exactly on
mutual least-neighbour edges.

## 2. Sharp tail by a vertex budget

In odd order, after entering an odd side the reverse side is even.  Subsequent
odd sides are strictly nested and their odd sizes drop by at least two, from
at most `n-2` to at least one.  This gives `(n-1)/2` moves.

In even order, a tail of length `d` followed by its reciprocal edge uses
`d+2` path vertices.  Each of the `d` vertices from the first internal vertex
through the first cycle endpoint already has two `H` path neighbours; its odd
`H` degree supplies a third neighbour.  Forest acyclicity prevents two path
vertices from sharing such a witness, so at least another `d` vertices are
needed.  Hence `n>=2d+2`.

For odd `n=2d+1`, a spine of `d+1` vertices with a leaf on its first `d`
vertices realizes the nested sequence.  For even `n=2d+2`, a spine of `d+2`
vertices with leaves on its `d` internal vertices has every degree odd;
decreasing spine labels and larger leaf labels realize a tail of `d`.  The
review control constructs and tests both families directly.

## 3. Recurrent labelled shuffles

Let `R=z exp(R)` and split its positive-order coefficients into odd `O` and
even `E`.  An odd-order sink is a root with a labelled set of even branches,
so its EGF is `z exp(E)`.

For an oriented even-order recurrent edge `u->v`, cutting the edge gives two
odd rooted sides.  If the `u` side has `k` odd root branches, the competing
labels for `u`'s choice are `v` and those `k` branch roots.  Every relative
order occurs equally often under labelled shuffling, so the required weight
is `1/(k+1)`.  Integrating the odd-branch marker gives

```text
W = z exp(E) integral_0^1 exp(x O) dx
  = z exp(E) (exp(O)-1)/O.
```

The candidate set for the reverse choice contains `u` and roots of odd
branches on the other side.  The two candidate sets are disjoint.  Internal
orders induced by a uniform global labelling on two disjoint sets are
independent (each pair of internal orders admits the same number of
interleavings).  Therefore the oriented recurrent-root EGF is `W_odd^2`.
Opposite orientations pair into cycles, giving the `r_n/2` zeta exponent.
The reviewer expands these series over exact rationals and compares all
coefficients through order eight with the literal dynamics.

## 4. Target-local inverse and maxima

A predecessor of `(T,v)` is either `v` itself or a neighbour root `u`.  The
self case occurs precisely when every branch at `v` is even.  The neighbour
case occurs precisely when the oriented `u->v` side is odd and label `v` is
smaller than every other odd-side neighbour of `u`.  These disjoint cases are
the displayed fibre formula and exhaust all roots because the tree is fixed.

For even order there is no self term and at most `deg(v)<=n-1` neighbours;
an even star attains the bound.  For odd order every contributing neighbour
lies in an even branch at `v`; such branches use at least two vertices each,
so there are at most `(n-1)/2`, plus the possible self predecessor.  A
least-labelled centre with `(n-1)/2` two-edge branches attains `(n+1)/2`.

Finally, the six-vertex tree with edges
`1-3, 2-4, 3-4, 3-5, 4-6` has one connected odd-cut component but two mutual
edges, `1-3` and `2-4`.  This confirms that the manuscript's warning is
essential and that no enumeration step may count `H` components as cycles.

All stated claims survive.  The finite reconstruction is falsification
pressure only, not an all-parameter proof or ownership certificate.
