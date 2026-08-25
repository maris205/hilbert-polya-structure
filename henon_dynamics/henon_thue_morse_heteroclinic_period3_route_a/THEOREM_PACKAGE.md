# C154 proof package

## Claim and status

Let `t_n` be binary digit-sum parity for `n>=0`, let
`y_j=(2,3,4)_[j mod 3]`, and define the two-sided point

```text
x_j=y_j for j<0,       x_j=t_j for j>=0.
```

For the left shift `sigma`, put `X=closure{sigma^n x:n in Z}` and let
`X_TM` be the two-sided Thue--Morse language subshift.  Then

```text
X = X_TM disjoint_union Orbit_sigma(x) disjoint_union Orbit_sigma(y),
Omega(sigma) = X_TM disjoint_union Orbit_sigma(y).
```

The full `Z`-orbit of `x` is dense, but standard `n>=0` topological
transitivity fails.  Every interface-orbit point is isolated and wandering.
The periodic points are exactly the three phases of `y`; hence

```text
Fix_X(n)=3 if 3|n and 0 otherwise,     zeta_X(z)=1/(1-z^3).
```

There is one primitive cycle, of least period three.  **PROVABLE AS STATED.**

## Lemma 1: positive and negative escape

Use `(sigma^n x)_j=x_(j+n)`.  If `n_k -> +infinity`, then every fixed
coordinate window eventually lies wholly in `{0,1}` and is a factor of `t`;
every limit therefore belongs to `X_TM`.  Conversely, every finite central
word of every point in `X_TM` occurs in `t`.  Primitive-substitution uniform
recurrence gives occurrences arbitrarily far to the right.  Choosing nested
occurrences and taking a diagonal subsequence realizes every point of
`X_TM` as a positive-shift limit of `x`.

If `n_k -> -infinity`, every fixed window eventually lies wholly in the
period-three tail.  Passing to one residue class of `n_k` modulo three makes
the window eventually equal to one phase of `y`; each phase is obtained by
such a residue-class sequence.  Finally, a convergent sequence of distinct
integer shifts has an unbounded subsequence; after taking a further
subsequence it tends to `+infinity` or `-infinity`.  This proves that there
are no other orbit-closure points and establishes the displayed disjoint
decomposition, since the three pieces use respectively only binary symbols,
both alphabets, or only `2,3,4`.

## Lemma 2: interface topology and recurrence

Every `sigma^n x` has the cross-alphabet pair `40` exactly once, at
coordinates `-n-1,-n`; neither pure limit component contains such a pair.
The cylinder requiring `40` at those coordinates therefore contains only
`sigma^n x`.  The shifts are distinct because their unique interface
locations differ.  Thus each singleton is open and its positive iterates are
disjoint: every interface point is wandering.

The Thue--Morse component is minimal and every one of its points is
nonwandering; the finite orbit of `y` is periodic and nonwandering.  Lemma 1
exhausts `X`, so their union is exactly `Omega(sigma)`.  The period-three
orbit is a proper nonempty closed invariant set, proving nonminimality.

The full two-sided orbit is dense by the definition of `X`.  This must not be
confused with the standard forward open-set definition of topological
transitivity.  Take the open sets `U={sigma x}` and `V={x}`.  Since
`sigma^n(sigma x)=sigma^(n+1)x != x` for every `n>=0`, forward transitivity
fails.

## Lemma 3: exclusion of other periodic points

The interface orbit is wandering and hence contains no periodic point.  The
period-three component contributes exactly its three phases.  It remains to
exclude a periodic point from `X_TM`.  For a proposed period `p`, choose odd
`k>bit_length(p)` and set `d=p(2^k-1)`.  Binary subtraction gives
`popcount(d)=k`, so `t_d != t_0` although `p|d`.  If
`b=bit_length(d)`, every interval of `t` of length `2^(b+1)` contains a full
`2^b`-aligned block.  The symbols at offsets `0,d` in that block are
opposite and have distance divisible by `p`.  Hence no such interval is
`p`-periodic, excluding a `p`-periodic language point.

## Theorem 4: all-period ledger and zeta

The three phases of `y` are fixed by `sigma^n` precisely when `3|n`.
Lemma 3 proves that there are no other fixed points.  Möbius inversion gives
`P_X(3)=3` and all other exact-period counts zero, so division by three gives
one primitive orbit.  Formally,

```text
sum_(n>=1) Fix_X(n) z^n/n
 = sum_(q>=1) 3 z^(3q)/(3q)
 = -log(1-z^3),
```

and exponentiation gives `zeta_X(z)=1/(1-z^3)`.

## Route-A conclusion

Unlike a free disjoint attachment, the periodic component is an actual limit
set of one dense full heteroclinic `Z`-orbit.  The structural gain is real but
small: minimality and forward transitivity fail, the interface is wandering,
and the one-factor source zeta has no target comparison.  The tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`, overall `ROUTE_A_EXPLORATORY`;
`route_b_invocation_allowed=false`.
