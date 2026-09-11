# P193 Review-A proof rederivation

This derivation starts from the two nomination extrema, not from the author's
block implementation.

## 1. Active pairs

No inversion crosses a direct-sum cut.  Standardize one indecomposable block
`beta`.  Its minimum cannot occupy the first position unless the block is a
singleton.  Hence the first position nominates the minimum, and the minimum
nominates the first position.

For any active `(i,j)`, put `b=beta_j`.  Earliest-left nomination places every
position before `i` below `b`.  Smallest-right nomination puts no value below
`b` after `i`; `beta_i>b`.  Thus the `b-1` values below `b` occupy exactly the
`i-1` earlier positions.  Therefore `i=b`.  If `i>1`, those positions form the
proper cut `[b-1]`, contradicting indecomposability.  Thus `i=b=1` and the only
active pair is first/minimum.  Different blocks give disjoint pairs.

## 2. Lyapunov statistic and pointwise time

A changed indecomposable block maps to `1 direct-sum gamma`.  Every old block
boundary survives, while each changed block acquires a new boundary, so the
number of direct-sum components strictly increases off the identity.  The
identity is the only state whose blocks are all singletons, hence the only
recurrent state.

Because blocks update independently in one epoch, the time of a direct sum is
the maximum of the component times.  For one nontrivial indecomposable block it
is one plus the time of `gamma`.  This is exactly the recursive height.

Induction on size gives height at most `n-1`; `(2,3,...,n,1)` realizes equality.
Every deepest state must be indecomposable.  If `gamma` is deepest on `n-1`
letters, it is indecomposable and has `n-1` indecomposable parents, giving
`d_n=(n-1)d_(n-1)` and `d_n=(n-1)!`.

## 3. Parent lemma

Start with `1 direct-sum gamma` and exchange the initial `1` with position `r`
of `gamma`.  A prefix before the relocated `1` cannot be a sum cut.  A prefix
after it is a cut exactly when `gamma` has a cut at or after `r`.  Hence the
parent is indecomposable precisely for the positions in the last component of
`gamma`, and there are `lambda(gamma)` of them.  Conversely, block surgery
forces every indecomposable parent to have this form.

## 4. Depth series

A permutation of depth at most `t` is an ordered sequence of indecomposable
blocks of depth at most `t`, so `A_t=1/(1-B_t)`.  At depth zero only the
singleton block exists.  A nontrivial block at depth at most `t+1` maps to
`1 direct-sum gamma`, where `gamma` is an arbitrary prefix sequence followed
by one last block.  Marking one of the last block's `r` positions yields
`x B_t'`; multiplying by the arbitrary prefix and the new initial letter gives
`x^2 A_t B_t'`.  Adding the singleton proves the recurrence.

## 5. Every-target fibre

Write target block sizes `(c_1,...,c_s)`.  Every image block begins in a
singleton, so `c_1=1` is necessary.  When it holds, partition consecutive
target blocks into source groups, each starting at a singleton.  A group
ending at block `e` has `c_e` parents by the parent lemma; a singleton group
has the same weight `1`.  Boundaries before a singleton `j>=2` are optional.
Expanding their binary choices gives

```text
c_s * product over j>=2 with c_j=1 of (1+c_(j-1)).
```

This is positive exactly for targets beginning in `1`, hence the image size is
`(n-1)!`.  Using `1+c<=2^c` and `c_s<=2^(c_s-1)` gives the `2^(n-1)` bound.
Equality in the exponent budget forces every target component to be a
singleton; the identity uniquely realizes it.

## 6. Independent finite reconstruction

`verify_review_a_p193.py` detects direct-sum cuts by prefix sums, enumerates
nominations literally, and imports no author code.  It reconstructs every
functional graph through `S_8`, checks the series independently, and is byte
equal to `CANONICAL.txt`.

Conclusion: all mathematical claims are derivable as stated.  P193-A1 has
been repaired and accepted, so the Review-A decision is `PASS` with zero open
findings.
