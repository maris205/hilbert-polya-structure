# P195 Review-A proof rederivation

## 1. Parity geometry

Deleting an edge splits a tree of odd order into one odd and one even side.
Orienting toward the odd side therefore gives one direction per edge.  The
literal update follows an outgoing edge, using the least endpoint label only
to break multiple choices.  A directed cycle would induce an undirected tree
cycle, so every orbit reaches a sink; sinks are exactly roots with all branch
orders even.

At even order both sides of an edge have the same parity.  The eligible edges
are exactly the odd/odd cuts in `H`.  At a vertex, branch sizes sum to the odd
number `n-1`, so an odd number of branches are odd.  Thus every `H`-degree is
odd and positive.  Since `H` is a forest, the least-neighbour function has no
cycle longer than a reciprocal edge and no fixed point.

## 2. Sharp time

For odd `n`, after crossing into an odd side, the reverse side is even.  Every
subsequent chosen odd side is a proper nested subset.  Consecutive odd sizes
differ by at least two, beginning at most `n-2`; there are at most
`(n-1)/2` moves.

For even `n`, write a tail into its two-cycle as
`v_0,...,v_d,v_(d+1)`.  Each `v_i`, `1<=i<=d`, already has two path neighbours
in `H`, while its `H`-degree is odd, so it needs a third neighbour.  Forest
acyclicity makes these `d` off-path witnesses distinct.  Therefore
`n>=2d+2`, or `d<=n/2-1`.  The manuscript's two caterpillars meet the two
bounds; direct parity checks confirm their advertised motion.

## 3. Recurrent counts

Let `R=z exp(R)` be the EGF of rooted labelled trees and split it into its odd
and even order parts `O,E`.  An odd-order fixed root has a SET of even-order
branches, giving `z exp(E)`.

For even order, orient a recurrent mutual edge `u->v` and cut it.  Each side is
an odd rooted tree.  If the `u`-side has `k_A` odd branches at its root, `u`
chooses cross-root `v` exactly when `v` is least among it and those branch
roots.  Across all label orders this has weight `1/(k_A+1)`.  Marking odd
branches by `x` and integrating `x` from zero to one gives
`W=z exp(E)(exp(O)-1)/O`.  The comparison set for the other side is disjoint,
so the two relative-order events are independent.  Restrict both sides to odd
order and take the ordered labelled product, yielding `W_odd^2`.  An oriented
mutual edge is one recurrent root state; pairing orientations gives the zeta
exponent `r_n/2`.

The reviewer verifier also computes, before using the product, the exact
finite weighted sum `sum 1/(k+1)` over every rooted labelled side through
order eight.  It matches `n![z^n]W` coefficientwise.

## 4. Inverse atlas and maximum fibre

A predecessor of `(T,v)` either already has root `v`, possible exactly when
all `v`-branches are even, or has root at a neighbour `u`.  The latter maps to
`v` exactly when the `v`-side seen from `u` is odd and `v` is the least-labelled
eligible neighbour of `u`.  These cases are disjoint and exhaustive.

For even order there is no self term and at most every neighbour of `v`
contributes, giving `n-1`, attained by a star.  For odd order, every
contributing neighbour lies in an even branch at `v`; at most `(n-1)/2` such
branches exist, plus the self term.  A centre joined to `(n-1)/2` two-edge
branches, with least centre label, attains `(n+1)/2`.

## 5. Counterexample pressure

The review independently searched connected components of `H`.  The first
one with two mutual least-neighbour edges occurs at order six:

```text
tree edges: 1-3, 2-4, 3-4, 3-5, 4-6
mutual edges: 1-3 and 2-4
```

Thus Remark 2.2 correctly rejects component-level uniqueness, and none of the
EGF or inverse arguments depends on it.

Conclusion: all mathematical claims survive.  The P123/P159 firewall and
exact release-state string have been repaired and accepted.  Review A is
`PASS` with zero open findings.
