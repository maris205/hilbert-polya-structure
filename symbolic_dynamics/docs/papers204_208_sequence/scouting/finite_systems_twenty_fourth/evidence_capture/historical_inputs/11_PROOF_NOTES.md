# Proof notes and limitations

These are author derivations for a killed scouting lane, not paper claims.

## C01_DRF: provable convergence and complete one-step reconstruction

**Status: provable as stated.** In a decreasing run of length `k`, moving its
minimum to the front removes exactly `k−1` inversions. No inversion with an
outside position changes, because the run occupies the same interval. Hence
every nonidentity state strictly loses inversions, the only recurrent state is
the identity, and every tail is at most `n(n−1)/2`.

The source `(2,3,...,n,1)` takes exactly `n−1` steps: its only nonsingleton
decreasing run is the pair immediately before 1, which moves 1 left one
position per step. This is a lower bound witness, not proof of the observed
global `n−1` upper bound.

For any target `y`, cut its word into consecutive nonempty blocks `B`.
Replace each `B=(b_1,...,b_k)` by `B^-=(b_2,...,b_k,b_1)`. Accept the cut iff
each `B^-` is strictly decreasing and at every boundary the previous last
letter is less than the next first letter. The accepted words are exactly
the sources: the inequalities say precisely that the reconstructed blocks
are the source's maximal decreasing runs. Distinct accepted cuts cannot
produce the same source because that source has unique maximal runs.
The verifier uses this cut recursion, independently of forward iteration.

Over the identity, a block of length at least three fails because its
reconstruction begins with an increasing pair. Every singleton/domino
tiling succeeds, so the identity fibre is Fibonacci `F_(n+1)`, with
`F_1=F_2=1`. The observed statement that this is the unique global fibre
maximum is **not justified here**. Sorting plus this segmentation inverse
does not meet the requested new-mechanism threshold.

## C02_APR: two-step compression, not a recurrence theorem

**Status: the following lemma is provable as stated.** Set
`s_i=w_1−w_2+...+(−1)^(i−1)w_i`. Positivity gives
`s_(2j−1)>s_(2j)<s_(2j+1)` whenever the indices exist. Thus the first output
is alternating, with a peak at every odd position.

Apply the map to such an alternating permutation `v`. Consecutive even
partial sums differ by `v_(2j+1)−v_(2j+2)>0`, and consecutive odd partial
sums differ by `v_(2j+1)−v_(2j)>0`. Stable ranking preserves these strict
inequalities. Therefore after two steps both odd and even subsequences
increase, and the valley in each pair is below its peak.

For `n=2m`, write a core state as `(a_1,b_1,...,a_m,b_m)`, where both lists
increase and `b_j<a_j`. Choosing the lower list is equivalent to a ballot
word: every initial segment contains at least as many chosen lows as highs.
The standard reflection argument gives
`binom(2m,m)−binom(2m,m−1)=C_m` possible states. This set is invariant by the
same partial-sum calculation.

For odd size `2m+1`, the last peak after two steps exceeds all earlier peaks
and valleys, so it equals `2m+1`. If a core state is `u` followed by this
maximum, its final partial sum exceeds every earlier sum and ranking on the
prefix is unchanged. Thus `T_(2m+1)(u,2m+1)=(T_(2m)(u),2m+1)`.

Consequently every orbit reaches this explicit invariant carrier in at most
two steps. This does **not** classify recurrence inside that carrier. No
proof of eventual period at most two, uniqueness/multiplicity of recurrent
states, uniform sharp clock, ambient inverse fibres, or endpoint basins is
claimed. Exact data falsify a unique recurrent orbit from size 12 onward.
The Catalan reduction is insufficient to rescue this candidate.

## C03_BPC: provable bijection

A preorder outdegree word satisfies the open-slot criterion: beginning with
one slot, processing an outdegree `d` consumes one slot and creates `d`,
with positive slots before the final vertex and zero afterward. The same
criterion characterizes valid breadth-first degree words. In preorder use
a stack of pending slots; in breadth-first use a queue. Either algorithm
uniquely decodes the word. Therefore `T=preorder_decode o breadth_encode`
is a bijection with inverse `breadth_decode o preorder_encode`.

This proves no transients and singleton fibres for every size, but provides
no useful uniform classification of its cycles. C04 changes the encoding
by locally sorting siblings and so this inverse no longer applies.

## C06_LHP: exact old-literal even slice

The old LEW edge key is `(length,sum,endpoints)`; the current key is
`(length,endpoints)`. At fixed length `d`, sum is `2 low+d`, so the keys
order edges identically. Let ordered lows be `a_1,...,a_m` and highs
`b_1,...,b_m`. The two output words differ only by reversing the `b` list.
When `m` is even, adjacent unordered pairs in the reversed even list are
exactly the same pairs, and neither list has a boundary-crossing pair.
Hence the maps agree on every even-edge carrier, not merely in finite tests.
At odd sizes at least three they differ; the explicit smallest witness is
recorded in the canonical comparison file. This is a parity variant of an
already killed matching-rewiring family, not an independent new direction.

## C08_TIR: classical retraction with an involution

Let `p` be insertion-tableau projection, `r` bottom-to-top row reading, and
`j` tableau transpose. The standard identity `p r=id` and `j²=id` give
`T=r j p`, `T²=r p`, and `T³=T`. Its recurrent set is the set of row words.
For target `r(Q)`, the fibre is the RSK class with insertion tableau `jQ`,
so its size is `f^(shape Q)`; non-row-word targets have no parents. These
are formal consequences of classical insertion and the previously killed
row-word projection. They receive zero residual credit. No standard tableau
of size greater than one equals its transpose (a nontrivial symmetric shape
has distinct off-diagonal entries), so those recurrent words are paired.

## Other candidates

C04, C05 and C07 have valid literal updates and complete finite data but no
all-parameter temporal/fibre package. Their cycle tables are not proofs of
future complexity or impossibility; they are reasons to stop this bounded
intake without promoting unsupported conjectures.
