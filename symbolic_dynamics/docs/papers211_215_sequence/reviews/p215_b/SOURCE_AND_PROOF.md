# P215 Review B independent source and proof audit

2026-09-11 UTC. `SOURCE_ONLY / NO_EXECUTION`. The eligible B reviewer read the
accepted physical Round1 manuscript, proofs, source/collision records, author
verifier and exact Round1 manifest. It also read A's proof/verifier description
only to exclude A's reverse-BFS and record-maximum-automaton route.

## Turn-word clock

For a word `x`, retain the signs of the nonzero successive differences of
`(0,x)` and compress equal adjacent signs. Call this alternating word `S(x)`.
Every nonzero `x` has first sign `+`. Write `D_i=max(x_1,...,x_i)-x_i` and
`d_i=x_i-x_(i-1)`. Directly from the literal map,

`D_i=max(D_(i-1)-d_i,0)`.

View this as a reflected walk and retain only its turning skeleton. The first
ascending edge of `x` stays on the upper envelope and leaves no edge in `D`.
Every subsequent descending edge moves `D` upward; every subsequent ascending
edge moves `D` downward until possibly reaching the reflecting wall. The
intervening opposite edge is nonempty, so reflection can shorten a monotone
piece but cannot merge two surviving pieces. Thus, as an identity of ordered
sign words,

`S(Fx) = -tail(S(x))`.

Iteration now gives the stronger itinerary identity

`S(F^j x) = (-1)^j tail^j(S(x))`

for every `0<=j<=|S(x)|`. Hence the first empty turn word occurs exactly at
`|S(x)|`; an empty turn word with initial value zero is precisely the zero
state. This proves the pointwise clock and unique recurrence. At most `n`
nonzero alternating signs occur, and equality is equivalent to every one of
the `n` differences being nonzero with alternating signs. The alternating
word `(q,0,q,0,...)` supplies sharpness for `n,q>0`; `n=0` and `q=0` are the
separate singleton boundaries.

This representation treats the theorem as a shift/complement dynamics on the
turn word and verifies its complete iterate itinerary with Floyd cycle
detection. It does not use the author's per-source visited dictionary or A's
reverse graph layers.

## Flagged-subset inverse

Let a target `y` start at zero, with zero positions split into `k` blocks.
Write `B_j` for the prefix maximum of its first `j` block maxima. The standard
record-height necessity in the manuscript gives nondecreasing block heights
`B_j<=L_j<=q`, and `x_i=L_j-y_i` on block `j`; the converse follows by direct
prefix-maximum substitution.

For an independent discrete representation reverse and complement these
heights:

`a_i=q-L_(k+1-i)`, `c_i=q-B_(k+1-i)`.

Then `0<=a_1<=...<=a_k` and `a_i<=c_i`, where the ceilings `c_i` are
nondecreasing. Shift to `b_i=a_i+i-1`. The entire fibre is therefore in
bijection with the flagged strict subsets

`0<=b_1<...<b_k<=q+k-1`, `b_i<=c_i+i-1`.

This gives a reconstruction algorithm by enumerating increasing subsets,
undoing the shift/reversal/complement, and substituting in each block. It is
not the author's Cartesian height-box filter and not A's coordinate automaton.

The same flagged subsets have the determinant count

`det[ binom(c_i+1, j-i+1) ]_(1<=i,j<=k)`.

One proof expands the determinant into signed families of northeast lattice
paths. Intersecting families cancel under the first-intersection tail swap;
the surviving nonintersecting families are exactly the flagged strict subsets
above. Empty size has determinant one. This supplies an independent count.
Partitioning the same subsets by their first ceiling violation inside the
unrestricted last-ceiling family gives exactly the manuscript's displayed
binomial recurrence, including the empty-prefix case. Thus the determinant,
the recurrence and the explicit reconstructed list count the same objects.

Targets not starting at zero have no source because the first output
coordinate is zero. Hence the image has `(q+1)^(n-1)` elements for `n>0`.
At target zero all ceilings equal `q`, so the determinant/flagged-subset set
has `binom(q+n,n)` members. Any nonzero image target has fewer than `n` zero
blocks and at most `binom(q+k,k)`, strictly smaller for `n,q>0`; singleton
boundaries have one source. This proves the image and unique maximum fibre.

## Source and scope verdict

The manuscript states precisely these five results and handles plateaus,
reflection saturation, empty words, zero alphabets, targets outside the image,
and strict uniqueness. Its two sources are used narrowly for classical
drawdown and barrier-enumeration background. Classical primitives remain
deducted; there is no arbitrary-poset, stochastic, all-time inverse, global
priority or universal no-factor claim.

Current SOURCE findings are Critical 0 / Major 0 / Minor 0. The proposed exact
delta is empty. The accompanying B verifier is source only and has not been
parsed, imported, syntax-checked or executed. No finite result, canonical,
build, page view, final B verdict, Round2 or paper completion is claimed.
`HOLD_EXTERNAL`.
