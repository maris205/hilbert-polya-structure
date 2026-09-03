# Successor transfer on set partitions: derivation package

Internal status: **proof-complete candidate; novelty still provisional**.  This
file states the literal map, the sharp temporal theorem, the full recurrent
classification, and a target-by-target fibre formula.  The temporal and fibre
proofs use different information: the first factors through block loads and a
canonical-window sorting lemma, whereas the second retains the actual order of
all labels inside the target blocks.

## 1. Literal rule and canonical word form

Use the ground set `0,1,...,n-1`.  Write a set partition as

\[
  \pi=(B_0,B_1,\ldots,B_{k-1}),\qquad
  \min B_0<\min B_1<\cdots<\min B_{k-1}.
\]

In one **successor-transfer** step, every block of size at least two removes
its maximum and sends it to the next block, with subscripts modulo `k`; all
transfers are simultaneous.  Singleton blocks send nothing.  Sort within each
block and canonically order the output blocks.

The final reorder is in fact inert.  A donating block retains its minimum.  An
element entering block `i>0` is the maximum of block `i-1`, hence is strictly
larger than the (retained) minimum of block `i-1`; an element entering block
zero is larger than the minimum of block zero.  Thus the new block minima are
still strictly increasing.

Consequently, in the restricted-growth word `w=w_1...w_n` with alphabet
`0,...,k-1`, the literal rule is particularly short:

> For each letter occurring at least twice, change its final occurrence from
> `i` to `i+1 mod k`, simultaneously.

This operation preserves both the restricted-growth condition and `k`.

## 2. The load factor and its max-plus cone lemma

Let `c_i` be the multiplicity of letter `i`, put

\[
  z_i=c_i-1\geq0,\qquad m=\sum_i z_i=n-k,
\]

and write `b_i=1[z_i>0]`.  The load factor evolves on the directed `k`-cycle as

\[
 z_i(t+1)=z_i(t)-b_i(t)+b_{i-1}(t).                 \tag{2.1}
\]

Thus every nonempty excess queue sends one token clockwise.  The following
lemma supplies the finite-time part of the proof.

**Queue smoothing lemma.**  For (2.1):

- if `m<=k`, then after at most `m-1` steps every `z_i` is zero or one;
- if `m>=k`, then after at most `k-1` steps every `z_i` is positive.

**Proof.**  Lift the cycle periodically to the integers and choose heights
`H_i(0)` with

\[
 H_i(0)-H_{i-1}(0)=z_i(0),\qquad H_{i+k}(0)=H_i(0)+m.
\]

Equation (2.1) is equivalent to

\[
 H_i(t+1)=\max\{H_i(t)-1,H_{i-1}(t)\},
\]

so induction gives the max-plus solution

\[
 H_i(t)=\max_{0\le r\le t}
          \bigl(H_{i-r}(0)-(t-r)\bigr).             \tag{2.2}
\]

Set `X_r=H_{i-r}(0)+r`.  Taking the difference of (2.2) at `i` and `i-1`
gives

\[
 z_i(t)=1+\max_{0\le r\le t}X_r
          -\max_{1\le r\le t+1}X_r.               \tag{2.3}
\]

The two maxima share all interior terms.  Hence

\[
\begin{aligned}
z_i(t)=0&\Longrightarrow
  \sum_{r=0}^{t}z_{i-r}(0)\le t,\\
z_i(t)\ge2&\Longrightarrow
  \sum_{r=0}^{t}z_{i-r}(0)\ge t+2.                 \tag{2.4}
\end{aligned}
\]

If `m<=k`, use `t=m-1`: a surviving pile of height at least two would require
at least `m+1` of the `m` tokens.  If `m>=k`, use `t=k-1`: an empty queue would
force the total mass in the whole cycle to be at most `k-1`.  Both are
contradictions.  This proves the lemma.  \(\square\)

The two load regimes are forward invariant.  In the dense regime all `z_i>0`,
so the load vector itself is fixed.  In the sparse regime all `z_i<=1`, so the
binary excess pattern simply rotates.

## 3. Canonical-window sorting after load smoothing

There is one further, labelled phase, of length at most `k-1`.

**Dense case (`m>=k`).**  Reverse the restricted-growth word.  Since every
letter occurs at least twice, successor transfer increments the *first*
occurrence of every letter in the reversed word.  In its first `k` positions,
one token from each occupied colour moves clockwise.  Their occupancy vector
therefore obeys (2.1), now with exactly `k` tokens on `k` sites.  The queue
smoothing lemma says that after at most `k-1` steps each colour occurs exactly
once in this window.  Equivalently, the final `k` positions of the original
word are a permutation of all `k` letters.

**Sparse case (`m<=k`).**  Every total letter multiplicity is now one or two.
Look at the first `k` positions of the original word.  Its colour occupancies
lie in `{0,1,2}` and sum to `k`.  A colour occurring twice in this prefix sends
its later copy clockwise; a colour occurring at most once in the prefix sends
no prefix token.  Regard a `2` as one excess particle and a `0` as a hole.
Every excess particle advances one site per step through nonholes and
annihilates when it reaches a hole; holes do not move before annihilation.
There are equally many excesses and holes.  On a `k`-cycle all are therefore
gone within `k-1` steps.  The first `k` letters are then distinct, and the
restricted-growth condition forces them to be `0,1,...,k-1` in that order.

These are sorting lemmas only for the temporal axis; they play no role in the
fibre formula in Section 5.

## 4. Sharp clock and complete periodic classification

Let `tau(pi)` be the least time at which the orbit of `pi` enters its eventual
cycle.

**Theorem A (sharp clock in every stratum).**  For `1<k<n`,

\[
 \max_{\pi\in\Pi_{n,k}}\tau(\pi)
   =\min\{n-2,\,2k-2\}.                             \tag{4.1}
\]

For `k=1` and `k=n`, every state is fixed.  In particular, for every `n>=2`,

\[
 \max_{\pi\in\Pi_n}\tau(\pi)=n-2.                 \tag{4.2}
\]

**Proof.**  The load phase lasts at most `min(m,k)-1`; Section 3 then costs at
most `k-1`.  This is `n-2` when `m<=k` and `2k-2` when `m>=k`, proving the
upper bound.  For the lower bound use the restricted-growth word

\[
  0^{m+1}12\cdots(k-1).                             \tag{4.3}
\]

Here all excess tokens begin in colour zero.  For
`0<=t<=min(m-1,k-1)`, direct application of the last-occurrence rule gives

\[
 T^t(0^{m+1}12\cdots(k-1))
 =0^{m+1-t}1^2 2^2\cdots t^2(t+1)(t+2)\cdots(k-1). \tag{4.4}
\]

Thus the load phase takes exactly `m-1` steps when `m<=k` and exactly `k-1`
steps when `m>=k`.  In the sparse case, at that time the first-`k` occupancy
word has the form `2^r 1^(k-2r) 0^r`, where
`r=min(m,floor(k/2))`.  Under the excess-particle description, the rear
particle starting at colour zero is the last to meet the last hole, at colour
`k-1`, exactly `k-1` steps later.

In the dense case write `d=m-k`.  After its load phase the word is
`0^(d+2)1^2... (k-1)^2`; for `1<=s<=k-1`, another direct induction gives

\[
 T^{k-1+s}(w)=
 0^{d+1}12\cdots(s-1)s^2(s+1)^2\cdots(k-1)^2
 01\cdots(s-1).                                    \tag{4.5}
\]

The terminal window first becomes a permutation at `s=k-1`.  Hence the total
is `m+k-2=n-2` for `m<=k` and `2k-2` for `m>=k`; (4.3) realizes (4.1).
\(\square\)

**Theorem B (all recurrent states and all periods).**  Apart from the one-block
and all-singleton fixed points, a `k`-block state is recurrent exactly as
follows.

- If `n>=2k`, its first `n-k` letters form a surjective restricted-growth word
  on all `k` letters and its final `k` letters are a permutation of them.
- If `n<=2k`, its first `k` letters are `0,1,...,k-1` and its final `n-k`
  letters are distinct.

Every such nontrivial state has **exact period `k`**.  The recurrent-state
count in the `k`-block stratum is

\[
 R_{n,k}=\begin{cases}
 k!\,S(n-k,k),&n\ge2k,\\[2mm]
 (k)_{n-k}=\dfrac{k!}{(2k-n)!},&n\le2k,
 \end{cases}                                      \tag{4.6}
\]

with the two formulas agreeing at `n=2k`.  Thus the number of `k`-cycles is
`R_{n,k}/k` for `1<k<n`; across `Pi_n` the possible periods are precisely
`1,2,...,n-1`.

**Proof.**  A periodic orbit must already lie in the forward-invariant smoothed
load regime and in the terminal canonical-window regime, otherwise Sections 2
and 3 would move it irreversibly into those regimes.  This gives the two stated
forms.  Conversely, in either form successor transfer freezes the indicated
prefix and adds one modulo `k` to every letter in the terminal permutation or
injection.  The form is invariant and the exact period is `k`.  Counting the
dense prefix and suffix gives `S(n-k,k) k!`; counting the sparse injected suffix
gives `(k)_{n-k}`.  \(\square\)

## 5. Independent every-target fibre formula

Fix a target `C=(C_0,...,C_{k-1})` in canonical minimum order, with `k>=2`.
If a source block `B_i` donated, call its donated maximum `x_i`; in the target
it lies in `C_{i+1}`.  A predecessor is reconstructed from a cyclic selection
`(x_i)` by

\[
 B_i=\bigl(C_i\setminus\{x_{i-1}\}\bigr)\cup\{x_i\},               \tag{5.1}
\]

omitting either deletion or addition when the adjacent source is inactive.

Only five states are needed to remember a selected incoming token relative to
its target block:

\[
 \mathcal S=\{\bot,\ \mathrm{s},\ \mathrm{min},\
                    \mathrm{max},\ \mathrm{int}\}.
\]

For a nonempty block `D`, define candidate sets

\[
\begin{array}{c|c}
a&E_a(D)\\ \hline
\bot&\{\bot\}\\
\mathrm{s}&D\quad\text{if }|D|=1,\text{ else }\varnothing\\
\mathrm{min}&\{\min D\}\quad\text{if }|D|\ge2\\
\mathrm{max}&\{\max D\}\quad\text{if }|D|\ge2\\
\mathrm{int}&D\setminus\{\min D,\max D\}\quad\text{if }|D|\ge3.
\end{array}                                                       \tag{5.2}
\]

Let `R(D,a)` denote `D` when `a=bot`, and `D\{x}` for any `x in E_a(D)`
otherwise.  Its size, minimum, and maximum depend only on `a`, even in the
interior state.

Define a `5 x 5` nonnegative-integer matrix `M_i=M_i(C)` whose row is the state
`a` of `x_{i-1}` relative to `C_i` and whose column is the state `b` of `x_i`
relative to `C_{i+1}`.  Its entry is the number of `x in E_b(C_{i+1})`
satisfying all of the following local tests, where `R=R(C_i,a)`:

1. if `b=bot`, then `|R|=1`;
2. if `b!=bot`, then `R` is nonempty and `x>max R`;
3. if `i<k-1`, then `R(C_{i+1},b)` is nonempty and
   `min R < min R(C_{i+1},b)`.

The last matrix deliberately omits a cyclic minimum comparison: canonical
block order is linear, although donations are cyclic.

**Theorem C (target-fibre trace formula).**

\[
 \boxed{\quad |T^{-1}(C)|=\operatorname{tr}
      \bigl(M_0(C)M_1(C)\cdots M_{k-1}(C)\bigr).\quad}             \tag{5.3}
\]

Consequently, `C` lies in the image exactly when the trace in (5.3) is
positive.  For `k=1` the unique target has fibre one.

**Proof.**  In an actual predecessor, `x_i` is either absent or belongs to one
of the four nonempty categories in (5.2).  Formula (5.1) shows that source
block `i` is inactive precisely when its retained target part is a singleton;
when active, its selected outgoing token must strictly exceed the retained
maximum.  The source blocks are canonically ordered precisely when their
retained minima increase.  These are exactly the three matrix tests.

Conversely, a cyclic state sequence contributing to the trace, together with
the locally counted choices of the `x_i`, reconstructs by (5.1) nonempty,
canonically ordered blocks for which every selected `x_i` is exactly the
maximum of a non-singleton source block.  Applying successor transfer returns
`C`.  Selection tuples and predecessors determine one another uniquely.
Summing their local multiplicities around the cycle is exactly the matrix
trace.  \(\square\)

This is not a formula in coarse block sizes.  For example, the two targets

\[
  025\mid134,\qquad 035\mid124
\]

have identical ordered triples `(block size, minimum, maximum)` for both
blocks, but their fibre sizes are respectively two and one.  Thus the fibre
axis sees labelled interlacing that the load/clock proof discards.

## 6. Verification boundary

`verify_stf.py` checks:

- the literal map, recurrent forms, exact periods, recurrent counts, and sharp
  clock in every stratum for every partition through `n=10` (115,975 states at
  `n=10`);
- the max-plus cone identity and both implications in (2.4) on 532,467
  bounded queue cases;
- (5.3) against literal predecessor enumeration for every one of the 26,442
  targets through `n=9`;
- the sharp family (4.3) in every nontrivial stratum through `n=50`.

It reports 1,217,023 passing assertions.  The finite checks validate the
implementation and catch statement errors; the proofs above carry the
all-parameter claims.
