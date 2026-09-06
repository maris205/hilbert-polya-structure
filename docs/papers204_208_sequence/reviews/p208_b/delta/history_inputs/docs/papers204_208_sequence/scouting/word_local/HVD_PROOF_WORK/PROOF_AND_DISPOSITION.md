# HVD: proved partial structure, not an admitted paper

2026-09-06 UTC. **Disposition: HOLD_PROOF / NO_ADMISSION.**
This bounded author task is complete as a partial-result dossier. It does
not supply an all-length recurrent classification, a sharp global clock,
or an independently valued extremal inverse theorem. No paper ID, reserve,
manuscript review, or global novelty clearance is created.

Author: `batch197_fifth_scout`. `root` is a proof contributor to the exact
active-set reduction in Proposition 3: root proposed that device during
this task and the author checked all cases. Earlier root counterexamples
alone were diagnostic. Both contributors are ineligible to provide a
nonself manuscript review of any paper using Proposition 3. The embedding
corollary and other proofs below were supplied by this author. No
independent mathematical acceptance is claimed for this dossier.

## 1. Literal system and evidence boundary

For integer $n\ge1$, let $X_n=\{0,\ldots,n-1\}^n$. For $x\in X_n$,
let $H(x)$ have vertices $0,\ldots,n-1$ and edge $i<j$ precisely when

$$x_k<\min(x_i,x_j)\qquad(i<k<j).$$

Let $F(x)$ be its ordered **undirected** degree sequence. Adjacent
vertices always have an edge; all ties are retained. Thus
$F:X_n\to X_n$. The literal is
[visibility_local_pilot.py](../visibility_local_pilot.py), not natural
visibility, out-degree, periodic visibility, or a decimation procedure.
Write $x^{(t)}=F^t(x)$ with the arbitrary input at time zero.

The old census contains only $n=1,\ldots,6$. It is read, not regenerated:

| $n$ | old image size | old fixed-point count | old maximum transient | old maximum fibre |
|---|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 1 |
| 2 | 1 | 1 | 1 | 4 |
| 3 | 2 | 1 | 2 | 22 |
| 4 | 6 | 1 | 3 | 130 |
| 5 | 22 | 2 | 3 | 791 |
| 6 | 90 | 4 | 4 | 4900 |

These are the HVD rows of
[VISIBILITY_LOCAL_CANONICAL.jsonl](../VISIBILITY_LOCAL_CANONICAL.jsonl).
The new verifier tests the statements below on the same 50,069 words;
it computes no cycles, global-height census, image census or all-target
fibre histogram. Named source or formula-derived examples at lengths
7 and 9 are individual sentinels, not additional complete boxes.

## 2. Endpoint erosion and permanent interior twos

**Proposition 1.** For $n\ge3$, every first-image state $y$ satisfies
$1\le y_0,y_{n-1}\le n-1$ and $2\le y_i\le n-1$ for
$0<i<n-1$. More generally, whenever a state $y$ has these lower bounds,

$$F(y)_0\le\max(1,y_0-1),\qquad
F(y)_{n-1}\le\max(1,y_{n-1}-1).$$

In particular both endpoints are permanently 1 by time $n-1$.
For $n=2$ the image is $(1,1)$ after one step; for $n=1$ the only
state is the fixed word $(0)$.

*Proof.* Image lower bounds follow from the Hamiltonian path and the
upper bound from graph degree. Consider the left endpoint of value $a$.
If $a\le2$, its adjacent interior neighbor has value at least 2 and
blocks every farther vertex. The degree is then 1.

Suppose $a\ge3$. Scan the visible vertices to the right. Those of value
less than $a$ have strictly increasing values: if earlier visible value
$b$ were at least a later visible value $c<a$, then $b$ would block
that later vertex. Every such visible value is at least 2. Indeed an
interior value is at least 2, and the far endpoint, if of value 1,
is blocked by an intervening interior vertex. There are therefore at
most $a-2$ visible values in $\{2,\ldots,a-1\}$. At most one further
visible vertex has value at least $a$, because that vertex blocks all
later ones. The total degree is at most $a-1$. Reflection proves the
right-endpoint assertion. Starting from time 1 with endpoint at most
$n-1$, at most $n-2$ additional steps give 1, which remains 1. ∎

This is an endpoint bound, **not** a claimed sharp global transient
bound. In particular the complete word need not stabilize when an
individual endpoint does.

**Proposition 2.** After the first step, an interior coordinate equal
to 2 remains equal to 2 forever. Consequently
$A_t=\{i:0<i<n-1,\ x_i^{(t)}>2\}$ is decreasing for $t\ge1$.
On a periodic orbit, both endpoints are 1 and $A_t$ is constant.

*Proof.* Let an interior coordinate have value 2 while every interior
coordinate is at least 2. Any nonadjacent candidate edge incident to
it has an intervening interior value at least 2; this is not strictly
below the smaller endpoint value. Exactly the two adjacent edges
remain, so the next value is 2. Monotonicity of $A_t$ follows. On a
cycle, Proposition 1 forces endpoints 1 and a decreasing finite set
must be constant. ∎

These two monotonicities do not force all active values to stop changing.

## 3. Exact active-set reduction and its unsolved part

**Proposition 3 (joint device, root and author).** Suppose $n\ge3$,
$x_0=x_{n-1}=1$, and all interior values are at least 2. List
$A=\{i:0<i<n-1,\ x_i>2\}$ as $a_1<\cdots<a_m$, and put
$z=(x_{a_1},\ldots,x_{a_m})$, with the empty graph understood when
$m=0$. For an active site define

$$b_j=\mathbf1_{a_j-1\notin A}+\mathbf1_{a_j+1\notin A}.
\tag{1}$$

Then

$$F(x)_{a_j}=\deg_{H(z)}(j)+b_j.\tag{2}$$

Inactive interior sites update to 2 and endpoints to 1. If $A$ stays
constant over subsequent times, the vector $b$ is constant, and the
active values follow the inhomogeneous feedback $z\mapsto\deg H(z)+b$.

*Proof.* Every inactive interior value equals 2. Between two active
values, removing inactive values does not change visibility: those
removed values are strictly below both active endpoints. Thus the
active-active edges are precisely the edges of $H(z)$, including the
edge between consecutive active sites even when a nonempty gap of 2s
separates them in the full word.

An active site sees an inactive full-word neighbor by adjacency. It
cannot see any other inactive interior site: an intervening interior
value is at least 2, while the inactive endpoint is 2. A nonadjacent
boundary endpoint of value 1 is likewise blocked. Therefore the
remaining incident edges are exactly those counted by (1), proving
(2). The other coordinates follow from Propositions 1 and 2. ∎

This proof includes empty and singleton active sets, adjacent active
sites, arbitrarily long gaps of 2s, and gaps adjacent to either boundary.
No complete word is reconstructed from an undirected degree target.

**Corollary 3a (separated active subclass).** If $m\ge2$ and every
two consecutive active sites have a nonempty intervening gap, then
$b\equiv2$. All active values remain greater than 2, and subtracting
2 from them gives exactly the ordinary length-$m$ HVD update.

*Proof.* Each active site has an inactive immediate neighbor on both
sides. Equation (2) applies with $b=2$. All degrees in a graph containing
the path on $m\ge2$ vertices are at least 1, so no active site vanishes.
Strict visibility is invariant under a common height translation. ∎

Equivalently, for a positive word $z$ of length $m\ge2$, define

$$E(z)=(1,z_1+2,2,z_2+2,2,\ldots,2,z_m+2,1).$$

Then $F(E(z))=E(F(z))$. Positivity is essential: if a coordinate of
$z$ is zero, it ties an inserted 2 and can destroy an edge that would
be an adjacent edge in the shorter word. With $z\in X_m$ positive,
$E(z)\in X_{2m+1}$ and the positive subcarrier is forward invariant.
For example $E(1,2,1)=(1,3,2,4,2,3,1)$ is a fixed word. This named
length-seven check is not an enlarged census.

**Gap.** When active sites are adjacent, $b$ is generally mixed in
$\{0,1,2\}$, and subtraction of a single constant does not reduce
(2) to the homogeneous HVD map. Neither a convergence theorem for
these weighted systems nor a classification of all their cycles is
proved here. Finiteness of the carrier and eventual constancy of $A$
alone do not supply either assertion.

## 4. A complete low-degree fixed subfamily

**Proposition 4.** For $n\ge2$, every fixed word with maximum value
at most 3 has endpoints 1 and interiors in $\{2,3\}$. List its
positions of value 3 as $h_1<\cdots<h_m$. Such a word is fixed if
and only if either $m=0$, or $m=2q\ge2$ and

$$h_{j+1}-h_j\ge2\quad\Longleftrightarrow\quad j\text{ is odd}
\qquad(1\le j<m).\tag{3}$$

Its number is

$$C_n=1+\sum_{q=1}^{\lfloor(n-2)/3\rfloor}
\binom{n-2q-1}{q+1}.\tag{4}$$

For $n=1$ the separate fixed word is $(0)$.

*Proof.* Fixed words satisfy the endpoint and interior bounds already
proved. For a word of the stated form, vertices of value 1 or 2 have
only their path edges. The only extra edges join consecutive positions
of value 3 when those positions have a nonempty gap of 2s. A third 3
blocks visibility past itself. Let $\delta_j$ indicate a nonempty gap,
and set $\delta_0=\delta_m=0$. The degree at $h_j$ is
$2+\delta_{j-1}+\delta_j$. It equals 3 exactly when the two flags
sum to 1. Beginning with $\delta_0=0$, they must alternate
$1,0,1,0,\ldots,1$, and the final boundary condition forces $m$ even.
This proves (3) in both directions.

For $m=2q>0$, the $q$ odd gaps each contain at least one 2, the
$q-1$ even gaps contain none, and the leading and trailing interior
2-blocks have arbitrary nonnegative lengths. After placing $2q$
threes and the $q$ mandatory twos, the remaining $n-2-3q$ twos are
distributed among $q+2$ uniquely specified blocks. Stars and bars
gives the summand in (4). The case $m=0$ is the unique path-degree
word, counted separately. ∎

The values $C_n=1,1,1,1,2,4$ for $n=1,\ldots,6$ match the old
fixed-point census, but this is not an all-degree classification.
The fixed word in Corollary 3a already has maximum 4.

## 5. Exact path-target fibre; no global maximum theorem

Let $p_n=(1,2,\ldots,2,1)$ for $n\ge2$ and $p_1=(0)$.
Here allow an arbitrary alphabet size $N\ge1$ when counting input
words; the autonomous carrier is recovered by setting $N=n$.

**Proposition 5.** For $x\in\{0,\ldots,N-1\}^n$, the following
are equivalent: $F(x)=p_n$; $H(x)$ is the path; $x$ is weakly
unimodal (weakly increasing up to some position and then weakly
decreasing). Moreover

$$|F^{-1}(p_n)|=
U(n,N):=\sum_{a=0}^{N-1}\binom{2a+n-1}{n-1}.\tag{5}$$

*Proof.* The graph always contains the path. Its ordered degree
sequence equals that of the path if and only if no extra edges occur,
as can also be seen by summing degrees.

A weakly unimodal word has, in every interval of length at least
three, an interior value at least the smaller endpoint value: use the
neighbor of an endpoint when the interval is on one monotone side,
or a peak when the interval straddles a peak. Thus no extra edge occurs.
Conversely, compress equal consecutive entries into runs. If the word
is not weakly unimodal, the sequence of nonzero adjacent comparison
signs has a decrease followed later by an increase. At a change from
decrease to increase, there is a constant valley run bounded by
strictly larger values. Those two bounding positions see each other
over the valley run and give a nonadjacent edge. This proves equivalence.

For the count, fix the maximum letter $a$. A weakly unimodal word
has a unique nonempty plateau of maximum letters, preceded by $l$
weakly increasing letters from $\{0,\ldots,a-1\}$ and followed by
$r$ weakly decreasing such letters, where $l+r\le n-1$.
For $a\ge1$, the count at specified $l,r$ is
$\binom{a+l-1}{l}\binom{a+r-1}{r}$. Summing first at $l+r=s$
by the ordinary binomial convolution and then over $0\le s\le n-1$
gives $\binom{2a+n-1}{n-1}$. For $a=0$, the constant zero word
is the unique word and the same displayed binomial equals 1.
Summing over $a$ proves (5), including $n=1$ and $n=2$. ∎

At $N=n$, (5) gives $1,4,22,130,791,4900$ through length 6.
It agrees with the old maximum-fibre values only in those checked
boxes. No injection of every other fibre into this fibre, global
upper bound, or all-length maximizing-target theorem is supplied.
Unimodal words, stars-and-bars counting, and this one static inverse
adapter receive no separate novelty credit.

## 6. Invalid global shortcuts, retained as falsifying evidence

The checked outputs are in [SENTINELS_CANONICAL.json](SENTINELS_CANONICAL.json).
Indices below are zero-based.

* Root's word $(0,2,1,1,0,2)$ maps to $(1,3,2,3,2,3)$ and then
  $(1,3,2,4,2,2)$. Edge $(1,3)$ appears in the first update.
  The squared norms of the two image states are 36 and 38. Thus
  decreasing edge containment and decreasing squared norm both fail.
* The derived word $(0,2,1,2,2,2,1,2,0)$ has the path plus chords
  $(1,3)$ and $(5,7)$. Its image $(1,3,2,3,2,3,2,3,1)$ additionally
  has chord $(3,5)$; the number of edges rises from 10 to 11.
  A decreasing edge-count potential also fails.
* The two source-given length-seven words
  $(3,2,2,1,2,2,3)$ and $(2,1,2,2,2,1,2)$ have different HVGs but
  the same ordered degree sequence $(2,2,3,2,3,2,2)$.
  Canonical or distinct-height graph reconstruction cannot be used
  unconditionally on this carrier; see the primary-source record.

No failure is deleted or reinterpreted as a new proof direction.

## 7. Static deductions, historical collision, and final gate

The source/assumption table is in [SOURCE_AND_REPLAY.md](SOURCE_AND_REPLAY.md).
Canonical HVG degree reconstruction, distinct-height reconstruction,
arbitrary-HVG realizations and enumeration, and merge-tree weak duality
are established static neighbors and are fully deducted as mechanisms.
They do not assert repeated application of $F$ to its own output.

The nearby [LUB proof](../LUB_PROOF_WORK/PROOF_AND_DISPOSITION.md) uses
component hierarchy and tree-height order-polynomial labels to count
an inverse fibre. Those generic static tools do not become a second
HVD contribution. In HVD, an arbitrary undirected degree target may
represent multiple graphs, so graph/tree recovery is not automatic.
One could sum realization counts over all compatible graphs and
their height-order classes, but such an unevaluated finite sum is
not a new inverse theorem. No all-target evaluated adapter is claimed.

What remains after those deductions is the proved partial temporal
structure (Propositions 1–3) and a low-degree fixed subfamily, not a
closed general temporal theorem. The exact path fibre is evaluated
but is a static unimodality calculation, and the global extremum is
unproved. Therefore the required two-part candidate contract is
**not met**. The appropriate bounded handoff is HOLD_PROOF, with no
automatic atlas enlargement and no paper admission.

To reopen, supply a proved all-length convergence/core theorem or a
meaningful sharp temporal theorem, plus a materially independent
evaluated inverse/extremal residual after the above deductions.
Finite agreement, a new title, or a larger cutoff does not reopen it.
