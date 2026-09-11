# P192 Review-B proof rederivation

This proof package uses residual cycle splitting and a path-equality lattice.
The history-set conjecture is not an input to any proved conclusion.

## 1. Carrier from residual cycle splitting

Suppose `tau_1 ... tau_(n-1)=c_n`.  Multiplying on the left by `tau_1`
leaves the residual product `tau_2 ... tau_(n-1)=tau_1 c_n`.  Minimality
forces `tau_1` to split one cycle of the residual permutation: a transposition
changes cycle count by one, and the remaining `n-2` factors must finish the
route to the identity.  Repeating gives a chain of `n-1` cycle splits.

Conversely, choose at each residual permutation a transposition whose two
endpoints lie in the same cycle and left-multiply.  Each choice increases
cycle count by one.  After `n-1` steps the residual is the identity, and
reversing the displayed equations gives an ordered factorization of `c_n`.
Thus residual split chains are exactly the carrier, without first invoking a
Hurwitz orbit or testing arbitrary transposition words.

Under rightmost-first composition,

```text
(1,2)(2,3)...(n-1,n) = (1 2 ... n),
```

while the reversed word is the inverse cycle for `n>=3`.  This pins the
orientation rather than treating it as notation.

## 2. Advancing collision boundary

At the selected index write the two distinct factors as `(a,b),(a,c)` with
`a<b,c`.  They cannot coincide because cancellation would express an
`n`-cycle in fewer than `n-1` transpositions.  The right Hurwitz move gives

```text
((a,b),(a,c)) -> ((a,c),(b,c)).
```

Its new lower endpoints are `a,min(b,c)`, so the selected equality disappears.
Every earlier factor is fixed, and the comparison immediately to the left is
also fixed because position `i` retains lower endpoint `a`.  Since `i` was the
first old collision, the next collision index is strictly larger.  Hence all
orbits terminate at fixed states after at most `n-2` moves.

For `n>=3`, the moving edge in
`((1,n),(1,2),(2,3),...,(n-2,n-1))` advances from `(j,n)` to `(j+1,n)` at
successive positions, producing history `1,...,n-2` and the canonical chain.
For `n=2`, there is no adjacent position and the sole factorization is fixed.

## 3. Fixed count by equality-lattice inclusion--exclusion

Put `N=n-1` and use the classical lower-endpoint parking-function bijection.
For a subset `S` of the `N-1` adjacent coordinate boundaries, require equality
across every boundary in `S`.  These requirements merge the coordinates into
`N-|S|` path blocks.

In the circular parking model, choose one preference for each block, then
translate all preferences together modulo `N+1`.  Translation is free,
preserves the prescribed equalities, and every orbit has exactly one ordinary
parking representative.  Therefore the number of parking functions satisfying
all equalities in `S` is

```text
(N+1)^(N-|S|-1).
```

Möbius inversion on the path-edge Boolean lattice, equivalently ordinary
inclusion--exclusion, gives the adjacent-unequal count

```text
sum_S (-1)^|S| (N+1)^(N-|S|-1) = N^(N-1).
```

This equals `(n-1)^(n-2)`.  The independent verifier checks the same count by
parking-content vectors and a last-letter multiset DP, not by circular words.

## 4. Target-resolved inverse atlas

For a target adjacent pair `(u,v)`, the unique inverse Hurwitz pair is
`(uvu,u)`.  Write `u=(a,b)`, `a<b`.  Apart from the impossible coincident
case, the two inverse factors have common lower endpoint exactly when `v`
contains `b` and its other endpoint `c` is larger than `a`; the inverse pair
is then `(a,c),(a,b)`.

An inverse at position `i` changes neither earlier factors nor the lower
endpoint seen in the comparison at `i-1`.  It is therefore selected precisely
when the target has no collision through position `i`, i.e. when `i` precedes
the target's first collision.  Distinct indices give distinct sources because
the source itself recovers its least collision.  A self-source occurs exactly
for a collision-free target.  These disjoint cases prove the displayed
every-target fibre, including empty fibres and the `n=2` sentinel case.

## 5. Fibre maximum

A fixed target has its self-source and at most one inverse at each of `n-2`
positions; a nonfixed target has no self-source and a shorter admissible
prefix.  Thus indegree is at most `n-1`.  Every adjacent pair of the canonical
chain is reverse-admissible, so equality occurs there.

If equality holds, the target is fixed and every position is admissible.
Writing its lower endpoints as `a_i`, admissibility forces
`a_1<a_2<...<a_(n-1)`.  This word is a parking function, so positivity gives
`a_i>=i` while the sorted parking inequalities give `a_i<=i`.  Hence
`a_i=i`; injectivity of the classical lower-endpoint correspondence leaves
only the canonical chain.

## 6. Orientation and conjecture firewalls

The local clock lemma alone is convention-specific through the chosen right
move and normalized lower endpoints.  The carrier and parking correspondence
also require the displayed long-cycle orientation.  The verifier's `n=4`
inverse-cycle probe has a different history support and tail, so results are
not silently transported by reversing the product.

Finally, no step above counts complete history sets.  The formula
`(n-1)^(n-2-|I|)`, its binomial depth sum, and general unique-deepest
consequence remain conjectures despite exact checks through `n=9`.

All four proved axes survive this rederivation.  Computation supplies bounded
counterexample pressure only.
