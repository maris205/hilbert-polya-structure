# Fresh68: prefix drawdown proof handoff and a separate interval negative

2026-09-11 UTC. Author: `/root/current_round_two_seats_scout`.
Scope: two materially different literal finite maps, desk mathematics and
bounded original-source subtraction only. No scientific code, import,
pilot, build, child agent, central edit, count change or Git action occurred.
There is no paper number, nomination, reserve or independent verdict here.
`HOLD_EXTERNAL` remains in force.

**Disposition:** A has a complete author proof of an exact pointwise clock
and every-target inverse recurrence. The one-step drawdown operation and
static barrier enumeration are owned background. The inspected evidence
does **not** identify an old theorem/map factor consuming A's exact clock;
its residual value needs a noncontributor gate. B is a separate elementary
interval-complement negative, not a fallback seat. An initial author
inclination to dismiss A merely as generic run erasure was not an
evidence-backed collision conclusion and is not adopted here.

## A. Literal map, claim and proof status

For integers $n,q\ge0$, let $X_{n,q}=\{0,\ldots,q\}^n$. For $n>0$ define
$$F(x)_i=M_i-x_i,\qquad M_i=\max_{1\le j\le i}x_j\quad(1\le i\le n).$$
For $n=0$, the empty word is fixed. Labels and order are retained; there is
no sorting, cyclic boundary, random input, externally driven schedule or
additional threshold step. Since $0\le M_i-x_i\le q$, this is a finite
autonomous deterministic self-map on the stated carrier.

For a word $x$, adjoin $x_0=0$, form the differences
$x_i-x_{i-1}$, delete zero differences, and replace every maximal consecutive
block of differences having the same sign by a single sign. Let $R(x)$ be
the length of this sign word; $R(0^n)=0$. Every nonempty sign word starts
with $+$ because the entries are nonnegative. Let $h(x)$ be the least
number of iterates needed to reach a recurrent state.

**Claim, PROVABLE AS STATED:**

1. For $x\ne0^n$, $R(Fx)=R(x)-1$. Consequently $h(x)=R(x)$,
   and $0^n$ is the only recurrent state.
2. For $n\ge1,q\ge1$, the sharp height is $n$. Equality holds precisely
   when all $n$ differences of $(0,x_1,\ldots,x_n)$ are nonzero and
   alternate signs. For $n=0$ or $q=0$, the height is zero.
3. The complete one-step inverse is the record-height bijection below;
   its cardinality is evaluated by the explicit binomial recurrence below.
4. For $n\ge1$, the image is exactly $\{y:y_1=0\}$ and has
   $(q+1)^{n-1}$ states. For $q\ge1$, the unique maximum fibre is at
   $0^n$, with size $\binom{q+n}{n}$. The singleton-carrier boundaries
   have their unique fibre of size one.

Strategy and dependencies: the drawdown recurrence gives an exact
transformation of sign runs, not merely a triangular upper bound.
Record heights then reconstruct every source. Reverse-complementing these
heights gives an ordinary upper-barrier counting problem; first violation
provides a self-contained evaluated recurrence. These are author proofs,
not finite observations or a completed candidate gate.

### A1. Complete sign-run clock proof

**Step 1: local differences.** Extend the running maximum by $M_0=0$ and
put $y=Fx$, $y_0=0$. If $d_i=x_i-x_{i-1}$, then
$$y_i=\max(y_{i-1}-d_i,0). \tag{A1}$$
Indeed $M_i=\max(M_{i-1},x_i)$ and
$M_{i-1}-x_i=y_{i-1}-d_i$. Thus an input plateau gives an output plateau;
a negative input difference gives a strictly positive output difference;
and a positive input difference gives a nonpositive output difference,
strictly negative whenever the preceding output is positive.

**Step 2: track whole sign runs, including plateaus.** Deleting zero input
differences does not affect the output analysis: across each such
difference (A1) leaves the output unchanged. We may therefore discuss the
consecutive nonzero differences, retaining their original order.
In the first positive run, (A1) starts at zero and stays zero. Every
negative input run produces a nonempty strictly increasing output run.
Every positive input run after the first follows a negative input run,
so its first step starts with positive output and strictly decreases it.
The rest of that positive input run decreases the output until zero, if
zero is reached, and then leaves it zero. Its nonzero output differences
therefore form one nonempty negative run. Between two negative input runs
there is such a nonempty negative output run, so the resulting positive
output runs cannot merge. Between two positive input runs there is a
nonempty positive output run, so those negative output runs cannot merge.
This also handles a terminal incomplete run and arbitrary plateaus.

Consequently the compressed output sign word is obtained by deleting the
first $+$ of the input sign word and reversing each remaining sign. It
has exactly $R(x)-1$ letters when $x\ne0^n$.

**Step 3: termination and recurrence.** $R(x)=0$ means all differences
from initial zero vanish, hence $x=0^n$. Iterating Step 2 reaches zero in
exactly $R(x)$ steps, and no earlier state is zero. Zero is fixed. Every
orbit reaches it, so no other recurrent state exists, establishing the
claimed interpretation of $h$.

There are only $n$ differences, hence $R(x)\le n$. Equality requires no
zero difference and a sign change at every adjacent pair of differences;
these conditions are also sufficient. For $q\ge1$, the word
$(q,0,q,0,\ldots)$ attains them. The empty and zero-alphabet carriers are
singletons. This proves all clock and equality statements.

As a hand illustration, not an executed test, $(2,0,1)$ maps to
$(0,2,1)$, then $(0,0,1)$, then zero. The signs of $(0,2,0,1)$ are
$+,-,+$, giving the exact time three. An increasing nonzero word has
time one, regardless of length; the claim is stronger than $F^n=0$.

### A2. Every-target source reconstruction

Take $n\ge1$ and $y\in X_{n,q}$. If $y_1\ne0$, its fibre is empty.
Suppose $y_1=0$, and enumerate its zero positions as
$$1=z_1<\cdots<z_k,\qquad z_{k+1}=n+1.$$
Define block barriers and their prefix maxima by
$$b_j=\max_{z_j\le i<z_{j+1}}y_i,
\qquad B_j=\max_{1\le r\le j}b_r\quad(1\le j\le k).$$
The fibre is in bijection with the integer sequences
$$0\le L_1\le\cdots\le L_k\le q,\qquad L_j\ge b_j, \tag{A2}$$
equivalently $L_j\ge B_j$. Its source is
$$x_i=L_j-y_i\quad(z_j\le i<z_{j+1}). \tag{A3}$$

**Necessity.** At an index with $y_i>0$, the running maximum of a source
cannot increase: an increase forces $x_i=M_i$, hence $y_i=0$. Therefore
the running maximum is constant in each displayed block, at some $L_j$.
These values are nondecreasing and bounded by $q$, and $x_i\ge0$ forces
$L_j\ge b_j$. Formula (A3) is then forced. Nondecreasing $L_j$ satisfying
the separate lower barriers satisfy their prefix maxima, and the converse
follows from $B_j\ge b_j$.

**Sufficiency and uniqueness.** Given (A2), (A3) lies in $X_{n,q}$.
At $z_j$, it has value $L_j$ because $y_{z_j}=0$. All earlier coordinates
are at most $L_j$. Every other coordinate in that block is less than
$L_j$ because its target value is positive. Thus its actual running
maximum throughout the block is precisely $L_j$, proving $Fx=y$.
The actual running maxima recover all $L_j$, so different height
sequences cannot give the same source. This proves the bijection without
an unevaluated inverse search.

### A3. Evaluated binomial recurrence for every fibre

Put
$$c_i=q-B_{k+1-i}\quad(1\le i\le k).$$
Then $0\le c_1\le\cdots\le c_k$. The substitution
$a_i=q-L_{k+1-i}$ converts (A2) into
$$0\le a_1\le\cdots\le a_k,\qquad a_i\le c_i.$$
Define $A_0=1$ and, successively for $1\le m\le k$,
$$A_m=\binom{c_m+m}{m}
 -\sum_{i=1}^{m-1}A_{i-1}
       \binom{c_m-c_i+m-i}{m-i+1}. \tag{A4}$$
Then $|F^{-1}(y)|=A_k$. The usual binomial convention is zero when the
lower index exceeds the nonnegative upper index. The recurrence uses only
explicit integer binomial coefficients and previously evaluated entries;
it is not a functional-graph enumeration or an unspecified matrix product.

**Proof of (A4).** There are $\binom{c_m+m}{m}$ nondecreasing length-$m$
sequences between zero and $c_m$, by multiset counting. An invalid one
has a unique first index $i$ with $a_i>c_i$. Necessarily $i<m$.
Its prefix of length $i-1$ is one of the $A_{i-1}$ valid prefixes.
The suffix of length $m-i+1$ is an arbitrary nondecreasing sequence in
$\{c_i+1,\ldots,c_m\}$, counted by the binomial coefficient in (A4).
For $i>1$ the prefix is bounded above by $c_{i-1}\le c_i$; for $i=1$
the prefix is empty. Thus every such prefix and suffix concatenate
monotonically. This decomposition is bijective,
and summing its disjoint classes proves the subtraction formula.

**Image and extremum.** Choosing $L_j=q$ in (A2) works for every target
with $y_1=0$, proving the image claim. At zero there are $k=n$ zero
positions and no positive barriers, giving all nondecreasing length-$n$
height sequences and hence $\binom{q+n}{n}$ sources. Any nonzero image
target has $k<n$, so its fibre is at most $\binom{q+k}{k}$, strictly
less than $\binom{q+n}{n}$ when $q\ge1$. Targets outside the image have
zero sources. At $q=0$ or $n=0$ the carrier and fibre are singletons.

## A4. Actual original-source subtraction and its limits

The main project workflow and proof-writer skill were applied: the exact
carrier, all boundary cases, source reconstruction, clock proof and
evidence limits are separate. No source is represented as a global
novelty certificate. Native source responses are conversation evidence,
not locally frozen PDF captures or independent source-review artifacts.

**External primary texts actually retrieved.**

- Goldberg and Mahmoud, *Drawdown: From Practice to Theory and Back Again*,
  [arXiv:1404.7493 PDF](https://arxiv.org/pdf/1404.7493), rendered date
  September 22, 2016. Printed p. 5, Definition 2.2 defines the running
  maximum minus current path value. This owns the one-step operation;
  bounded integer words are a finite restriction, not a newly invented
  statistic. The selected definition does not establish the repeated
  whole-path sign-run clock. Only the relevant initial pages were read.
- Pemantle and Wilf, *Counting nondecreasing integer sequences that lie
  below a barrier*, [arXiv:0905.0609 PDF](https://arxiv.org/pdf/0905.0609).
  Printed pp. 1–5, especially Theorem 1 and its proof, were read. The
  target counting problem after (A2) is exactly their static problem.
  Its evaluated enumeration and the multiset extremum receive no new
  mechanism credit. Formula (A4) has its own elementary first-violation
  derivation above; it is not claimed as a new barrier-counting method.

Queries included literal prefix-maximum-minus-current, iterated running
maximum/drawdown, monotonicity runs and upper-barrier counts. Some broad
search displays were truncated; relevant source bodies were then opened
directly. The Berkeley `2015-04.pdf` fetch failed with HTTP 502, so it is
not claimed as read; the arXiv drawdown PDF succeeded. Search results about
stochastic drawdown stopping times are not evidence for autonomous
iteration of the whole vector. No exact-clock ownership was located in
this bounded search, which is an unresolved scope statement, not novelty.

**Local original checks, not recovery-summary reliance.**

- P93 `papers/93-random-push-pop-stack-cocycles/main.tex`, lines 121–212:
  the actual rule is a driven composition of push/pop maps on infinite
  words; $M_n-S_n$ records the surviving stack length of the driving
  walk. Its normal form owns that reflected-walk primitive but does not
  feed the entire drawdown word back into itself. No factor transporting
  its cocycle theorem to the exact clock above is supplied or asserted.
- The original S2 in `docs/papers107_111_sequence/scouting/STOCHASTIC_SCOUT.md`,
  lines 213–290, uses externally driven clipped nearest-neighbour maps;
  its synchronization clock is a driving-walk range passage. It is not
  literal A. Its Skorokhod/reflection language is deducted as background.
- P117 `papers/117-odd-run-reversal-cyclic-words/main.tex`, lines 1–235,
  flips odd-length **cyclic** constant runs. It has two-cycles (already
  at length one), whereas A has only one fixed recurrent state. Thus
  the same-length full binary carriers are not conjugate. This distinction does
  not rule out all conceivable factors; none yielding A was found here.
- P132 `papers/132-prefix-majority-dynamics/main.tex`, lines 53–143,
  thresholds prefix sums and has $n+1$ fixed points. For binary carriers
  it is not conjugate to A, which has one. A generic triangular-prefix
  bound is not the sign-run equality proof.
- P138 `papers/138-palindromic-prefix-xor-feedback/main.tex`, lines 101–173,
  has a complement quotient $Q(y)_i=y_i\oplus1\oplus p_i(y)$.
  On its normalized length-three carrier, every output is zero. A on
  normalized binary words is not that rule: $F(010)=001\ne000$.
  The original P138 has a strict recurrent two-cycle, also excluding
  a conjugacy of the original full binary carriers.
- P185 `papers/185-prefix-diversity-delay/main.tex`, lines 58–164, counts
  distinct symbols of the strict prefix and, on its first image, has
  $d'_i=d_{i-1}+1$. A's image is every word starting at zero and is not
  constrained to zero-one rises. On the common carrier with $q=n-1$
  and $n\ge3$, A has height $n$, while P185 has height $n-1$; hence
  there is no same-carrier conjugacy. No claimed clock factor is borrowed.
- The complete original `root_zigzag/INTAKE.md` was read. It reverses
  greedy nonoverlapping alternating-comparison permutation factors;
  this is neither A's literal nor its sign-run transformation.
- `finite_parking_allocation_scout01/PROOF_AND_SUBTRACTION.md`, lines
  1–110, was read through its explicit record-height reconstruction.
  It supplies the useful warning that monotone height coordinates and
  gap deletion can exhaust a candidate. Its update decreases entries
  above the first deficient rank, preserving a parking core; it is not
  A's drawdown update. Static monotone-height enumeration is deducted
  here, without claiming an unproved dynamic conjugacy.

All paths in the last two bullets are below this batch's `scouting/`.
Targeted local searches covered drawdown, running/prefix maximum,
reflection, monotonicity/alternating runs and prefix-OR terminology.
Absence of a search hit does not certify absence from the archive. The
listed explicit distinctions are narrower than a universal no-factor
claim. In particular the binary restriction is
$$F(x)_i=\left(\bigvee_{j\le i}x_j\right)\mathbin{\oplus}x_i.$$
An exact old owner of this restriction or a factor supplying the general
sign-run clock would be a material gate finding; it has not been ruled
out by assertion. All $q$ share the clock statistic, so a binary-control
subtraction deserves explicit scrutiny before any admission.

## B. Interval-hull complement: separate negative

On all subsets of $[n]$, put $C(\varnothing)=\varnothing$ and
$$C(S)=[\min S,\max S]\setminus S\quad(S\ne\varnothing).$$
This preserves the fixed finite ambient carrier. Let $r(S)$ count the
nonempty interval components of $S$. A nonempty source with $r$ occupied
runs has exactly $r-1$ nonempty intervening gaps, which are the occupied
runs of its output. Thus $r(CS)=r(S)-1$, the unique recurrent state is
empty, and the exact clock is $r(S)$, with sharp maximum $\lceil n/2\rceil$.

For nonempty target $Y$ with extrema $l,u$, every source is uniquely
$$[a,b]\setminus Y,\qquad 1\le a<l\le u<b\le n.$$
Necessity follows because both source hull endpoints are removed from
the target. Conversely such a source has endpoints $a,b$ and complement
exactly $Y$ in its hull. Therefore its fibre is $(l-1)(n-u)$.
The empty-target fibre consists of the empty set and all nonempty
intervals, of size $1+n(n+1)/2$.

The original `docs/papers204_208_sequence/scouting/set_partition_sixth/INTAKE.md`,
lines 38–75, explicitly lists convex-hull complement/defect among desk
exclusions. Its full `SCOUT_REPORT.md` was also read: the UPC rule there
is complement of upper closure on chain intervals, **not** this literal
interval-hull complement, and is not presented as an exact-map owner.
The direct proof above reduces B entirely to deleting the two end runs
after complementing an interval word and choosing two outer endpoints.
There is no additional residual claimed and no nomination for B.

## Handoff and open risks

A's mathematical claims are author-proved as stated; no finite execution
has checked them. Its static inverse mechanism and one-step statistic are
explicitly attributed. Whether the exact sign-run clock survives a
noncontributor old-map/factor and primary-source gate remains open; no
independent PASS or paper suitability is claimed. This scoped handoff is
not permission for a scientific run or a larger search. B is closed as an
elementary negative. Historical manuscripts and accepted evidence were
not edited.
