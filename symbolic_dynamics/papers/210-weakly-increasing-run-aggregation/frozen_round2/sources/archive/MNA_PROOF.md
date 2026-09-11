# MNA all-size author proof before scientific code

The literal and source boundary are fixed in `THIRD_LITERAL_CONTRACT.md`.
Here `F` sums maximal weakly increasing runs of old positive composition
parts. Blocks are intervals in the original `[N]`, and mass means interval
length. Round `t` maps time `t-1` to time `t`. A block is *new in round t*
if it is the union of at least two old blocks in that round. Coarsening
means an original cut, once deleted, never returns.

## 1. Closedness, fixed points and convergence

All output masses are positive and still sum to `N`. A composition is fixed
exactly when every adjacent pair is a strict descent. If not fixed, at least
one cut disappears, so the number of blocks strictly decreases. Thus every
orbit reaches a fixed point; no cycle of length greater than one exists.
Write `tau(a)` for the number of nonfixed updates before first fixation.

This decreasing-length argument alone is generic and has no admission
credit. The next argument is mass-sensitive and substantially sharper.

## 2. Delayed mergers force triangular mass

**Lemma A(t).** If a cut is deleted in round `t >= 1`, its old left block
at time `t-1` has mass at least `t`.

For `t=1` positivity proves the statement. Suppose `t>=2` and the claim is
proved at `t-1`. Let `A,B` be adjacent blocks at time `t-1` whose boundary
is now deleted, so `|A|<=|B|`. At time `t-2`, let `a` be the rightmost
parent block of `A` and `c` the leftmost parent block of `B`. Their common
boundary survived round `t-1`, so `|a|>|c|`.

First, `B` must be new in round `t-1`. Otherwise `B=c`, while
`|A|>=|a|>|c|=|B|`, contradicting deletion of the cut in round `t`.
Since `B` is new, its first internal cut was deleted in round `t-1` and
has left block `c`. Induction gives `|c|>=t-1`; integrality then yields
`|A|>=|a|>=|c|+1>=t`. This proves the induction. It also proves the useful
fact that the right block of every cut deleted in round `t>=2` is new in
round `t-1`. No unproved assumption about all other parents is used.

**Lemma B(t).** Every block new in round `t>=1` has mass at least

`M_t = 1 + t(t+1)/2`.

For `t=1` a new block has at least two positive parents, so mass at least
`2=M_1`. For `t>=2`, take the first two parents `A_1,A_2` of a new block.
Their boundary is deleted in round `t`; Lemma A gives `|A_1|>=t`.
The fact just proved implies `A_2` is new in round `t-1`, so induction
gives `|A_2|>=M_(t-1)`. They are disjoint intervals, hence the output block
has mass at least `t+M_(t-1)=M_t`. Extra parents only increase it.

**Theorem 1 (sharp all-size maximum).** Put

`H(N) = max{h>=0 : 1+h(h+1)/2 <= N}`.

Then every composition of `N` satisfies `tau(a)<=H(N)`, and equality is
attained for every `N>=1`. Equivalently,
`H(N)=floor((sqrt(8N-7)-1)/2)`.

If `tau=t>=1`, round `t` is nonfixed and creates a block of mass at least
`M_t`, so `N>=M_t`. This is the upper bound. For `N=1`, the only state
is `(1)` and `H=0`. For `h=H(N)>=1`, let `r=N-M_h>=0` and start from

`a=(h,h-1,...,2,1,1+r)`.

At time `t`, for `1<=t<=h`, the state consists of the unchanged strictly
decreasing prefix `(h,h-1,...,t+1)` followed by the single suffix mass

`r + 1 + t(t+1)/2`.

At the first update only `(1,1+r)` merges, proving the formula for `t=1`.
For `1<=t<h`, the suffix mass is at least `t+1`. Thus the last prefix block
`t+1` and the suffix form one increasing pair. Every earlier prefix pair
is a strict descent, so exactly this one old prefix block joins. Its new
mass is `r+1+(t+1)(t+2)/2`. Induction proves the formula. There are exactly
`h` nonfixed updates, ending with `(N)`. This works for all surplus `r>=0`,
not just at triangular thresholds.

Root checked this A/B route after the author sent it. The route, induction,
and all-surplus witness were authored here before scientific code. Root's
explicit first/rightmost-parent check is collaborative confirmation; neither
participant counts as an independent review of this candidate.

## 3. All target fibres as increasing refinements

Fix a target `s=(s_1,...,s_m)`. A preimage consists uniquely of a weakly
increasing positive refinement `lambda_i` of each `s_i`, with strict
descent between consecutive refinements. Indeed, output cuts are old input
cuts at the same absolute cumulative sums, so these segments are uniquely
specified by `s`. They are exactly the maximal weakly increasing runs iff
each is weakly increasing and the cross-boundary inequalities are strict.
This proves both necessity and sufficiency without overcounting.

For positive integers `s,a,b`, let `P_s(a,b)` count weakly increasing
sequences of total `s` with first part `a` and last part `b`. Put it zero
unless `1<=a<=b<=s`. When `a=b`,

`P_s(a,a) = 1` if `a` divides `s`, and `0` otherwise.

When `a<b`,

`P_s(a,b) = [z^s] z^(a+b) product_(j=a)^b (1-z^j)^(-1)`.

For the latter formula first reserve one part `a` and one part `b`, and
choose any further multiplicities of each size between them. Sorted order
is unique; this is the ordinary restricted-partition generating function.
For `a=b`, every part equals `a`, explaining the separate case.

**Theorem 2 (every-target one-step fibre).** With all sums finite,

`|F^(-1)(s)| = sum_(1<=a_i<=b_i<=s_i) product_i P_(s_i)(a_i,b_i)
                                  product_(i<m) 1{b_i>a_(i+1)}`.

The unique refinement decomposition proves this identity immediately after
the coefficient lemma. It is a formula on the target parts, not a sum over
the original whole carrier. A useful evaluation form is

`v_m(a)=sum_b P_(s_m)(a,b)`,

`v_i(a)=sum_b P_(s_i)(a,b) sum_(c<b) v_(i+1)(c)` for `i=m-1,...,1`,

`|F^(-1)(s)|=sum_a v_1(a)`.

Endpoint multiplicities are unrestricted and positive minima/maxima are
already included; singleton refinements and empty fibres need no exceptions.
This recurrence is just an evaluation of the exact theorem, not by itself
a second novelty claim. No largest-fibre assertion is made.

## 4. Closed image threshold, with constructive sufficiency

For a suffix `(s_i,...,s_m)` call a tuple of refinements *feasible* when
its internal boundary descents hold. Let `r_i` be the minimum first part of
its first refinement over all feasible tuples, or undefined if none exists.

**Theorem 3 (linear target image test).** Initialize `r_m=1`. For
`i=m-1,...,1`, once `r_(i+1)` exists, define

* if `s_i <= r_(i+1)`, fail: the target has empty fibre;
* if `s_i = r_(i+1)+1`, put `r_i=s_i`;
* if `s_i >= r_(i+1)+2`, put `r_i=1`.

The target lies in the image exactly when this scan never fails. Thus this
is a closed `O(m)` integer-comparison image test, with no enumeration of
partitions or input compositions.

Proof: the last target part has refinement consisting entirely of ones,
so its minimum first part is exactly `1`. Suppose a feasible suffix to the
right has minimum first part `r`. A new refinement of `s_i` must end in
a part `b>c` for some feasible right first part `c>=r`, hence it must have
`b>=r+1`. Conversely, any weakly increasing refinement ending at least
`r+1` can be concatenated with a suffix attaining the minimum `r`.

If `s_i<=r`, no such last part exists. If `s_i=r+1`, that last part must
equal the entire sum, so the unique possible refinement is singleton
`(s_i)` and the minimum first part is `s_i`. If `s_i>=r+2`, the refinement
`(1,s_i-1)` is weakly increasing and ends at least `r+1`; hence the minimum
is `1`, the smallest positive value. These cases are exhaustive, establish
the stated meaning of `r_i` inductively, and construct a feasible input
whenever the scan succeeds. Failure cannot be avoided by selecting a
larger right first part. This proves both directions.

For example, targets `(2,3,2)` and `(2,2,3)` have the same total and same
multiset of masses, but the first passes and the second fails. Explicitly,
`(2,1,2,1,1)` maps to `(2,3,2)`, whereas for `(2,2,3)` the backward
thresholds are `1,2` and then failure. Position-sensitive inverse constraints
are therefore not determined by the temporal total-mass bound.

## 5. Scope of the proved claims

Sections 1–4 are all-size deductive claims, not extrapolations from a table.
Their ordinary ingredients (positive coarsening, partition coefficients,
boundary composition) are explicitly subtracted from novelty credit.
The triangular delayed-merger argument and threshold collapse are the
candidate-specific theorem signals. A bounded source nonhit is not global
novelty proof. There is no admitted manuscript, independent candidate review,
all-time fibre theorem, largest-fibre formula or classified set of all
maximizers. An exact fixed-box pilot follows only to try to falsify these
already stated contracts.
