# P166 Review B: independent proof rederivation

## Starting point

This audit started only from the literal map

\[
T_n(x)=x+\operatorname{wt}(x){\bf1}
\quad\hbox{on }(\mathbb Z/n\mathbb Z)^n,
\qquad n\ge2.
\]

No author, Gate-A, or Review-A verifier was imported.  The earlier review was
read only after the derivation and the first independent exhaustive run had
closed.

## Phase conjugacy and the all-time target oracle

Fix a target `y`, put `m_j=#{i:y_i=j}`, and write `X_j=y-j1`.  The points
`X_j` are precisely the `n` points in the diagonal orbit of `y`.  Exactly
`m_j` coordinates of `X_j` vanish, so its integer weight is `n-m_j` and

\[
T_n(X_j)=X_j+(n-m_j){\bf1}=X_{j+m_j}.
\]

Thus `g_m(j)=j+m_j (mod n)` is an exact conjugate, not merely a quotient.
Coordinate differences are invariant, hence every source of `y` lies in this
one diagonal orbit.  Induction gives

\[
|(T_n^t)^{-1}(y)|=\#\{j:g_m^t(j)=0\},
\]

including `t=0`.

## Cycles, periods, and recurrence

On a nontrivial phase cycle every traversed increment `m_j` is positive.
Lifting one circuit to the integers, its increment sum is a positive multiple
of `n`, while it is at most the total occupancy mass `n`; it is therefore
exactly `n`.  All mass lies on that cycle and the positive occupancies are its
clockwise gaps.  Conversely, any nonempty support with those gap values gives
one cycle.  There cannot be two nontrivial cycles.  A remaining recurrent
phase is fixed exactly at an occupancy-zero position (or for the all-mass
entry).

For a period-`k` state anchored at phase zero, the positive occupancies form
an ordered positive composition `a_1+...+a_k=n`.  Labelling the coordinates
contributes `n!/(a_1!...a_k!)`.  Summation gives

\[
P_{n,k}=k!\,S(n,k)\quad(2\le k\le n).
\]

Fixed points are the zero state and every full-support state, so
`P_{n,1}=1+(n-1)^n`.  This also rederives the recurrent census, divisor formula
for fixed iterates, and the finite-map zeta product.  Nothing here uses that
`n` is prime.

## Complete depth census and the anchor attack

For a state anchored at its literal phase zero, a transient path of exact
length `d` encounters positive increments `a_1,...,a_d` of sum `s<n` and
then a zero occupancy.  The visited `d` coordinate labels are nonempty bins;
the endpoint is one fixed empty bin; the other `n-s` labelled coordinates may
occupy the remaining `n-d-1` bins.  For a fixed ordered composition the count
is

\[
\frac{n!}{a_1!\cdots a_d!}\,
\frac{(n-d-1)^{n-s}}{(n-s)!}.
\]

Summing ordered positive compositions and using
`sum s!/(a_1!...a_d!)=d! S(s,d)` yields exactly

\[
D_{n,d}=d!\sum_{s=d}^{n-1}{n\choose s}S(s,d)
(n-d-1)^{n-s}.
\]

This derivation anchors every literal state at its own phase zero, so it also
directly attacks the potentially dangerous factor of `n`: no unaccounted
rotation remains.  Equivalently, in the paper's lifted phase-pair count there
are `n` starting anchors and every literal state occurs under `n` anchors;
the factors cancel.  Since partial sums are strictly increasing below `n`,
`d<=n-2`.

At `d=n-2`, equality forces one zero at `z`, one entry two at `e`, all other
entries one, with `e != z-1`.  Phase `z+1` always has maximal depth; phase
`z+2` is an additional maximal phase exactly when `e=z+1`.  Counting profiles,
labelled realizations, and anchor pairs gives
`D_{n,n-2}=(n-1)n!/2`.  Direct boundary checks give depth zero for `n=2`
and six last-shell states for `n=3`.

## Every-target one-step fibres

A possible source of `y` is `x=y-k1`, where the integer weight `k` lies in
`{0,...,n}`.  For `1<=k<n`, its zero multiplicity is `m_k`, so it has weight
`k` exactly when `m_k=n-k`.  The congruent residue shifts at integer weights
zero and `n` must not be merged: the former gives the sole source of `y=0`,
whereas the latter occurs exactly for `m_0=0`.  These branches are disjoint.
This proves

\[
|T_n^{-1}(y)|=1_{y=0}+1_{m_0=0}
+\sum_{k=1}^{n-1}1_{m_k=n-k}.
\]

The factor `e^z+u-1` marks `m_0=0`; after setting `r=n-k`, each factor
`e^z+(u-1)z^r/r!` marks `m_k=r`.  The separate `(u-1)` changes the otherwise
unmarked all-zero target from indegree zero to one.  This recovers the exact
marked EGF and both its target-mass and source-mass checks.

If `h` middle conditions hold, their distinct prescribed positive counts
sum to at least `1+...+h`; hence `h<=floor((sqrt(8n+1)-1)/2)`.  Full support
adds at most one.  Prescribing counts `1,...,h_n` and placing any remainder
in the unprescribed symbol 1 constructs equality for every `n>=3`; when `n`
is triangular there is no remainder.  The exact equality criterion in the
paper follows.  The exceptional `n=2` map is a permutation and has maximum
fibre one.

## Boundary ledger

- `t=0`: the phase oracle is the identity count.
- all-zero target: the explicit correction gives exactly one source.
- `n=2`: all four states are recurrent; maximum depth zero and maximum fibre
  one.
- `n=3`: recurrent/fixed/last-shell counts are `21/9/6`; maximum fibre is
  three.
- `d=n-2`: the one-zero/one-two classification above is necessary and
  sufficient.
- composite `n`: no division or field step occurs; exhaustive `n=4,6` tests
  agree.
- triangular and nontriangular `n`: both witness constructions were checked
  through `n=150`, with triangular transitions at `3,6,10,15,21,28,36,45`.

No proof defect or counterexample was found.
