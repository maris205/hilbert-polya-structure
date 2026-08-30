# R2 infinite-family proof report: odd-run reversal

**Status:** theorem gate passed; manuscript numbering remains unfrozen  
**External status:** `HOLD_EXTERNAL`

## Literal map

For a labelled cyclic binary word of length `n`, flip in parallel every bit
belonging to a cyclic run of odd length.  A nonconstant word has an even
number `r` of runs.  Write their cyclic lengths as

\[
  (\ell_0,\ldots,\ell_{r-1}).
\]

A boundary between two consecutive runs survives one update if and only if
the two incident run lengths have the same parity.  No new boundary is ever
created.

## Recurrence and periods

Because the boundary set can only shrink, a recurrent word must retain every
boundary.  It does so exactly when all run lengths have the same parity.
Conversely, such a word is recurrent:

- if all run lengths are even, no bit flips and the word is fixed;
- if all run lengths are odd, every bit flips, so the word and its complement
  form a 2-cycle.

Hence every orbit has eventual period at most two, and the equal-parity
criterion is exact.

For odd `n`, a nonconstant cyclic binary word cannot have all run lengths of
one parity: it has an even number of runs, so either choice would have even
total length.  The only recurrent states are therefore the two constant
words, which form one 2-cycle.

For `n=2m`, fixed words are exactly those whose nonempty boundary set is an
even subset of one of the two parity classes of cyclic positions, together
with the two constant words.  Thus

\[
  f_{2m}=2^{m+1}-2.
\]

If there are `r` odd runs, where `r` is even, the ordered odd-composition
count is

\[
  \binom{(n+r)/2-1}{r-1}.
\]

Choosing a labelled boundary and the initial bit, then dividing by the `r`
choices of distinguished boundary, gives the exact number of period-two
states

\[
  p_{2m}=\sum_{\substack{2\le r\le 2m\\r\ \mathrm{even}}}
  \frac{4m}{r}\binom{m+r/2-1}{r-1}.
\]

The number of 2-cycles is `p_(2m)/2`, and therefore

\[
  \zeta(z)=(1-z)^{-f_{2m}}(1-z^2)^{-p_{2m}/2}.
\]

## Sharp odd-length transient

At every nonrecurrent step at least two boundaries disappear.  For odd `n`,
a nonconstant word has at most `n-1` boundaries.  Therefore

\[
  \tau\le (n-1)/2.
\]

This is sharp.  Put `n=2t+1` and take cyclic run lengths consisting of one
part `2` and `2t-1` parts `1`.  At each step the unique even run coalesces
with its two neighbouring odd runs, remains even, and removes exactly two
boundaries.  It reaches a constant word after exactly `t` steps.

## Boundary-parity eroder for even length

For even `n`, list the surviving boundary positions cyclically as
`b_0,...,b_(r-1)` and put `q_i=b_i mod 2`.  This parity label is intrinsic on
`Z/nZ`.  Since the parity of the run between `b_i` and `b_(i+1)` is
`q_i xor q_(i+1)`, the boundary `b_i` survives precisely when

\[
  q_{i-1}=q_{i+1}.
\]

Thus the boundary dynamics is the shrinking rule `D` that deletes each
symbol of a cyclic binary word whose two neighbours differ.  Constant and
alternating `q` are exactly the recurrent boundary patterns.

For a mixed even-length `q`, let

\[
  e(q)=\#\{i:q_i=q_{i+1}\},\qquad C(q)=|q|+e(q).
\]

Every realization by boundary positions has length at least `C(q)`: a gap
between equal parity labels is a positive even integer and costs at least
two, while a gap between unequal labels costs at least one.

**Cost-drop lemma.**  If `q` is mixed, then

\[
  C(Dq)\le C(q)-4.
\]

To see this, decompose `q` into cyclic constant runs.  A singleton run
survives; a run of length two disappears; and a run of length at least three
loses its two endpoints.  If at least two runs are nonsingletons, at least
four symbols disappear, while every new equal adjacency can be charged
injectively to an old equal adjacency (a bridge across vanished length-two
runs is charged to one such run).  If exactly one run is nonsingleton, the
even total length and even number of binary runs force its length to be odd
and at least three; it loses two symbols and exactly two equal adjacencies.
Both cases give the displayed drop.

A mixed even-length cyclic binary word has at least four symbols and at least
two equal adjacencies, so `C(q)>=6`.  Applying the cost-drop lemma until the
last mixed state shows that depth `t>=1` requires

\[
  n\ge C(q)\ge 6+4(t-1)=4t+2.
\]

Consequently

\[
  \tau\le \left\lfloor\frac{n-2}{4}\right\rfloor.
\]

The bound is sharp.  For `t>=1`, take

\[
  q=0^{2t+1}1.
\]

It has cost `4t+2`, and each shrinking round removes the two endpoints of
the zero run, so it reaches the alternating word `01` after exactly `t`
steps.  Realize it with gap length two for equal adjacent parity labels and
gap length one for unequal labels.  This gives a cyclic word of length
`4t+2`.  Adding two to any one gap preserves every boundary parity and gives
the `4t+4` case with the same depth.  These are precisely the two even
lengths for which `floor((n-2)/4)=t`.

## Independent route division

1. The run-composition coalescent proves monotone boundary loss, recurrence,
   odd-length sharpness, and the recurrent census.
2. The intrinsic boundary-parity eroder proves the even-length clock through
   a cost inequality and supplies sharp witnesses independently of the run
   count bound.

The existing exhaustive verifier through `n=16` checks every finite orbit,
the recurrence criterion, both census formulas, and both sharp depth laws.
It is control evidence only; the arguments above supply the infinite-family
proofs required by the owner gate.

No claim of novelty or priority is made.  Shrinking cellular automata and
static run enumeration remain explicitly zero-credit background.
