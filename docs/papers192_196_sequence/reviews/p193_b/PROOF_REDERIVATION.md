# P193 Review-B proof rederivation

This derivation uses the cut-bit word and weighted interval groupings.  It is
separate from the author implementation and Review A's program.

## 1. Cut bits force the active pairs

For a permutation `pi`, put a cut after `r` exactly when the running maximum
of the first `r` entries equals `r`.  The runs between successive cuts are
the direct-sum indecomposable intervals.

Suppose `(i,j)` is mutually nominated and write `b=pi_j`.  Earliest-earlier-
larger nomination puts every entry before `i` below `b`; smallest-later-
smaller nomination puts every value below `b` before `i`.  Hence the first
`i-1` positions are exactly `[b-1]`, so `i=b`.  If `i` were not the first
position of its cut interval, the preceding `b-1` values would create an
internal cut.  Thus `i` is the interval start and `b` is its minimum.

Conversely, a nontrivial cut interval cannot start with its minimum.  Its
first entry nominates that minimum, and the minimum nominates the interval's
first position.  No inversion crosses an old cut, so these are all active
pairs and they are disjoint.

## 2. Refinement and the clock tree

Swapping first/minimum puts the interval minimum first.  Relative to its
alphabet, this sets a new cut bit after the first position, while all old cut
bits remain set.  Every nonidentity epoch therefore strictly adds cut bits.
Only the all-one cut word, the identity, is recurrent.

Build a rooted decomposition tree whose sequence nodes are old cut intervals
and whose unary surgery node removes the newly exposed leading singleton.
Parallel evolution takes the maximum height over sequence children and adds
one at a surgery node.  Induction on interval size gives the exact absorption
time and the bound `n-1`.  The interval `(2,3,...,n,1)` realizes every level.

For a deepest source, the top interval must be indecomposable.  Its child is a
deepest permutation of size `n-1`.  The parent count below gives `n-1`
choices, so `d_n=(n-1)d_(n-1)` and `d_n=(n-1)!`.

## 3. Parent count in cut-bit coordinates

Start from `1 direct-sum gamma` and exchange its leading `1` with position
`r` of `gamma`.  A cut before the moved `1` is impossible because the prefix
omits `1`.  A later cut survives exactly when `gamma` has a cut at or after
`r`.  Consequently the reconstructed parent is indecomposable exactly when
`r` lies in the terminal cut interval of `gamma`, giving its terminal length
as the parent count.

## 4. Depth OGFs from the decomposition tree

Depth-at-most-`t` permutations are sequences of indecomposable objects, so
`A_t(1-B_t)=1`.  An indecomposable object at depth at most `t+1` is either a
singleton or is reconstructed from `1 direct-sum gamma`: an arbitrary prefix
sequence contributes `A_t`, its terminal interval marked at one of its
positions contributes `x B_t'`, and the exposed singleton contributes `x`.
Thus

```text
B_(t+1) = x + x^2 A_t B_t'.
```

The reviewer expands these coefficient identities independently and compares
them with the literal orbit census through degree eight.

## 5. Recursive target grouping

Write the target interval sizes as `(c_1,...,c_s)`.  A source interval maps to
a consecutive group of target intervals whose first interval is a singleton;
a group ending at interval `e` has `c_e` parents by the cut-bit parent count.
Therefore a target has no parent if `c_1>1`.  Otherwise recursively either
continue the current group or, immediately before a singleton interval, start
a new one.  The terminal weights of all groupings sum to

```text
c_s product_(j>=2,c_j=1) (1+c_(j-1)).
```

This recursion is implemented directly before comparison with the product.
It is positive precisely when the first value is `1`, and hence the image has
`(n-1)!` targets.  Finally `1+c<=2^c` and `c_s<=2^(c_s-1)` bound the product
by `2^(n-1)`.  Equality leaves no uncounted positive interval, so every target
interval is a singleton and the identity is the unique maximizer.

All claims survive this route.  Enumeration is counterexample pressure, not
the all-parameter proof and not an ownership claim.
