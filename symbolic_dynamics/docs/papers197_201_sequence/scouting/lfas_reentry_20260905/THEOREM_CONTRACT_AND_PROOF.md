# LFAS re-entry: invariant pivot, sharp width-uniform tail, full inverse atlas

Date: 2026-09-05 UTC. **THEOREM_SPIKE / STAGE1_GATE_PENDING / HOLD_EXTERNAL**.
This strengthens the unchanged reserved LFAS map. It is not a new breadth
row, a selected candidate, or a completed manuscript.

## Literal map

Let `r,s>=2`. On all labelled binary `r x s` matrices, order rectangles
`(i,k,a,b)`, `i<k`, `a<b`, lexicographically in this displayed order. If a
rectangle is alternating (`10/01` or `01/10`), complement its four entries.
At each epoch switch the least alternating rectangle; if none exists, hold.
Write `F` for this map and `tau` for first entrance time to a periodic orbit.
All coordinates range from zero. Row support `A_i` is a subset of `[0,s-1]`.
Comparable means containment in either direction.

For incomparable rows `A_i,A_k`, put `D=A_i\A_k`, `E=A_k\A_i`.
The least alternating rectangle in this row pair uses columns
`min D` and `min E`. Thus the scheduler first chooses the least incomparable
row pair and then swaps these two exclusive elements between its rows.
The binary 2-switch, row/column margins, lonesum characterization, and
classical lonesum census are all owned background, with zero novelty credit.

## Theorem 1: invariant pivot and complete recurrent criterion

For a nonfixed state, let `(i,k)` be its least incomparable row pair.
Along its entire orbit:

1. the first row index `i` stays constant;
2. the partner index `k` is nonincreasing;
3. every periodic orbit has period 1 or 2; no nonfixed state feeds a fixed
   state;
4. put `j<ell` for the first two columns where rows `i,k` differ. The state
   is recurrent if and only if these two differences have opposite types
   (`10` then `01`, or vice versa) and the pivot row after switching these
   two columns is comparable with every row `h` satisfying `i<h<k`.

Proof. For `h<i`, the row `A_h` is comparable with all rows, in particular
with the incomparable `A_i,A_k`. It must be contained in their intersection
or contain their union: either mixed ordering would make `A_i,A_k`
comparable. A switch preserves their intersection and union, so `A_h`
remains comparable with both changed rows, and with every unchanged row.
The switched rows remain incomparable. Therefore the first pivot is still
`i`, and its least partner can only decrease because partner `k` remains
available.

The switched rectangle itself remains alternating, so the whole rectangle
index cannot increase. If the next selector is the same rectangle, the
next switch restores the starting matrix, giving a strict two-cycle.
If it decreases, the starting matrix cannot be periodic. A finite strictly
decreasing selector cannot continue forever. The selector is unchanged
exactly when its row pair remains least and its column pair remains least.
The first condition is the displayed comparability test. The column pair
remains least exactly when the first two differences are already opposite:
otherwise, after the switch, the second differing column supplies a new,
earlier opposite difference. This proves the stated iff test. A nonfixed
image still contains the rectangle that was switched, so cannot be fixed.
Fixed states are precisely matrices whose row supports form a containment
chain, equivalently matrices with no alternating rectangle. QED.

## Theorem 2: a sharp bound uniform in the width

For every `r,s>=2` and every matrix,

```text
tau(A) <= 2r-3.
```

More precisely, if a nonfixed orbit visits `p` distinct partner rows up to
and including its first recurrent state, then `tau(A)<=2p-1`, where
`p<=r-i-1` and `i` is its
invariant pivot. For every `r>=2` and every `s>=r+1`, equality `2r-3` is
attained. Hence `max_A tau(A)=2r-3` throughout the wide regime `s>=r+1`.
No exact maximum is asserted here for `s<=r`.

Proof of the upper bound. Fix a row pair while it remains the selected
pair, and list its differing columns in increasing order, each marked by
which row contains it. The first differing column is unchanged under any
switch in this pair. The first switch exchanges the first difference with
the first difference of the opposite type. If the opposite type was already
second, the column selector is unchanged and this is a two-cycle unless an
earlier row partner appears. If the opposite type occurred later, the
second differing column becomes opposite to the new first one. The next
switch in this same pair therefore uses the first two differing columns.
After that switch its column selector stays unchanged. Thus either an
earlier partner appears, or the current state is already on a two-cycle.

Among the selector states at times `0,...,tau`, each distinct partner can
therefore occur at most twice. Partners decrease and never reappear.
There are `tau+1` such selector states, so `tau+1<=2p<=2(r-i-1)`.
The all-fixed case has `tau=0` and separately satisfies the displayed bound.

Proof of sharpness. On columns `0,...,r`, take

```text
A_0 = {r},
A_k = {0,k} union {k+2,...,r},              1<=k<=r-1.
```

Every extra column when `s>r+1` is zero. The selectors, up to and including
the first recurrent state, are exactly

```text
(0,r-1,0,r), (0,r-1,0,r-1),
(0,r-2,0,r-1), (0,r-2,0,r-2),
 ...,
(0,1,0,2), (0,1,0,1).
```

To verify this inductively, at the start of partner `k` the pivot is the
singleton `{k+1}` and every earlier partner row contains it. Row `k` lacks
`k+1`, and its first exclusive element is 0. Its first switch sends the
pivot to `{0}`, still contained in all earlier rows; the next switch sends
it to `{k}`. Its own row then becomes `{0,k+1,...,r}`. Now row `k-1` is
the first earlier row missing the new pivot; every row before it contains
that pivot. At `k=1`, the second listed rectangle is already recurrent.
There are `2r-2` listed selector states, so the tail is `2r-3`. QED.

## Theorem 3: explicit inverse sources without running the selector

A fixed target has its unique self-source. For a nonfixed target `Y`, let
`i` be its invariant pivot and put `P=Y_i`. For every `k>i` with `P,Y_k`
incomparable, form

```text
D_k=P\Y_k,  E_k=Y_k\P,  j_k=min(D_k union E_k).
```

Let `S_k` be the one of `D_k,E_k` containing `j_k`, and `O_k` the other.
Set `b_k=min(S_k\{j_k})`, with `b_k=s` when this set is empty. Define

```text
T_k(Y) = {ell in O_k : ell<b_k and
          P triangle {j_k,ell} is comparable with Y_h
          for every i<h<k}.
```

Every one-step source is obtained uniquely by choosing `k` and
`ell in T_k(Y)` and reversing the rectangle `(i,k,j_k,ell)`. In particular,

```text
|F^(-1)(Y)| = sum_(k>i) |T_k(Y)|,           Y nonfixed.
```

The image iff condition is: `Y` is fixed or at least one `T_k(Y)` is
nonempty. This is a target-local column interval and row comparability
formula; it does not invoke a full selector computation on each candidate.

Proof. A nonfixed source has the same invariant pivot as its image. Its
switched rows remain incomparable in the target. Consider a candidate
target rectangle with exclusive columns `a in D_k`, `b in E_k`. The source
exclusive sets after reversing it are
`(D_k\{a}) union {b}` and `(E_k\{b}) union {a}`. For that rectangle to be
the first alternating one in this pair, it is necessary and sufficient that
`b<min(D_k\{a})` and `a<min(E_k\{b})`. Thus one chosen column is the first
difference `j_k`, and the other is precisely an opposite-type column before
the next same-type difference; these are the interval conditions above.

Earlier pivot rows `h<i` remain comparable with all rows under the inverse
switch by the intersection/union proof of Theorem 1, applied to the two
incomparable target rows. Among partner rows before `k`, only the pivot
changes. Their comparability with that new pivot is exactly the remaining
displayed test. These conditions ensure the reconstructed source schedules
the chosen rectangle, and are also necessary. Different choices flip
different sets of matrix entries and give different sources. A fixed target
has no alternating rectangle and cannot be the image of a switch. QED.

## Theorem 4: sharp fibre maximum and all equality cases

For every `r,s>=2`,

```text
max_Y |F^(-1)(Y)| = (r-1)(s-1).
```

When `(r,s)!=(2,2)`, there are exactly two maximizing targets. Their row
supports are

```text
({0}, {1,...,s-1}, ..., {1,...,s-1})
```

and the entrywise complement of this matrix. At `r=s=2`, every one of the
16 matrices has fibre one and maximizes.

Proof. Theorem 3 has at most `r-i-1` partner terms, and each term has at
most `s-1` columns. A fixed target has fibre one. This proves the bound.
For the displayed target, every partner has `j_k=0`, `S_k={0}`, and
`O_k={1,...,s-1}`. Every choice of `ell` gives reconstructed pivot `{ell}`,
contained in all earlier partner rows. All `(r-1)(s-1)` choices are valid;
entrywise complementation preserves the scheduler and the same count.

If `(r-1)(s-1)>1`, a maximizing target is nonfixed. Equality in both bounds
forces `i=0` and exactly `s-1` admissible columns for every partner. Therefore
`j_k=0`, its same-type difference set is `{0}`, and the opposite-type set is
all remaining columns. There are no common entries: row 0 and every other
row must be complementary, with row 0 either `{0}` or `{1,...,s-1}`. Its
fixed value determines the same choice for every partner, giving only the
two targets stated. For `r=s=2`, there is only one rectangle; its two
alternating matrices are exchanged and the remaining 14 hold, so the map
is bijective. QED.

## Claim limits and discarded exploratory reasoning

The exact formula `2min(r,s)-3-1{r=s}` for the maximum tail is **CONJECTURE**
only. Small exhaustive boxes and heuristic larger witnesses support it;
no symmetric upper bound or exact square maximum is used in this contract.
An early proposed proof claiming that an unchanged column pair during a
partner descent forces immediate recurrence was false and is withdrawn.
The wide witness above itself refutes that intermediate assertion.

Transposition does not conjugate the row-first scheduler: exact enumeration
gives image size 3292 for `3x4` and 3290 for `4x3`. No argument may transpose
the row bound to obtain a column bound. The only sharp tail result claimed
is the proved row bound with equality for every `s>=r+1`.

This package improves a reserve by proving new all-parameter lemmas; it does
not override the need for a process-separated Stage-1 collision/owner gate.
