# Proof Package: ORR second clock attempt

## Claim

Let $T:S_n\to S_n$ reverse every odd-length maximal strictly increasing
run, and hold every even-length run, simultaneously. Singletons and the
empty permutation are held. Let $\tau(x)$ be the number of nonfixed epochs
before the orbit of $x$ reaches a fixed point, and put
$H_n=\max_{x\in S_n}\tau(x)$.

The original conjecture remains
$$H_n=\left\lfloor\frac{n-1}{2}\right\rfloor\quad(n\ge1),\qquad H_0=0.$$

## Status

Original equality: **NOT CURRENTLY JUSTIFIED**. No counterexample to the
equality is established. The lower bound is now proved for every size.
A cross-parity inversion invariant gives the following corrected result,
which is **PROVABLE AS STATED**:
$$
\left\lfloor\frac{n-1}{2}\right\rfloor
\le H_n\le \binom{\lceil n/2\rceil}{2}\qquad(n\ge1),\qquad H_0=0.
$$
The upper bound remains quadratic. It does not close the requested sharp
linear clock and is not presented as a qualifying temporal axis.

## Assumptions

- Positions are linear; labels are distinct and comprise $[n]$.
- All maximal runs and all reversals use the old state.
- Position parity is preserved by every odd interval reversal.
- No trajectory, parameter family or endpoint class is silently substituted
  for the full carrier in the conjecture.
- All arguments below are symbolic. No old or new finite census is used as
  a proof of an all-parameter statement.

## Notation

For a finite set of labels $A$, its increasing listing is
$a_1<\cdots<a_{|A|}$. Concatenation is denoted by $\Vert$; an empty list
or concatenation is omitted. A run is active if its length is odd and at
least three. Ordinary inversion means a larger label precedes a smaller
label in the word.

For one initial state, colour each label by the parity of its initial
position. The colour classes $A$ and $B$ therefore remain respectively at
odd and even positions throughout its orbit, with
$|A|=\lceil n/2\rceil$ and $|B|=\lfloor n/2\rfloor$.
These are **position-colour classes, not numerical label parities**.
Let $J(x)$ count inversions whose two labels have different colours.

## Proof Strategy

For the lower bound, an explicit pair-block word has one active triple
per epoch. The triple moves right while its two larger labels join a
descending prefix. For the upper bound, every active reversal strictly
raises $J$, and independent sorting of the two colour classes bounds the
whole possible range of $J$ on their parity-preserving carrier.

The colour-sorting comparison is a proof device, not an additional
dynamical rule, extra experiment or claim that those sorting moves are
allowed ORR epochs. It bounds a statistic on a larger comparison class
containing the actual orbit.

## Dependency Map

1. The all-size lower bound uses only the displayed exact maximal-run
   decomposition and a permanent descent boundary for the even-size lift.
2. The upper bound uses the invariant position-colour classes, the exact
   $r(r+1)$ cross-colour inversion gain of a reversed $2r+1$ run, and the
   extremal range of $J$ over the fixed-colour carrier.
3. The final two-sided inequality follows by applying the range bound to
   each finite orbit. Neither the Fibonacci inverse theorem nor the first
   root note's local ancestry lemma is needed for this inequality.
4. The desired linear upper bound would require a further global argument.
   The explicit ancestry obstruction below is not used as a theorem that
   the desired bound is impossible.

## Proof

### Step 1. An exact all-size lower-bound trajectory

First let $n=2k+1$ with $k\ge0$. For $0\le j\le k$, define
$$
x^{(j)}=
(2k+1,2k,\ldots,2k-2j+2)
\;\Vert\;(1)\;\Vert\!
\mathop{\Vert}_{r=k-j,k-j-1,\ldots,1}(2r,2r+1).
$$
In particular,
$$x^{(0)}=(1,2k,2k+1,2k-2,2k-1,\ldots,2,3).$$
The prefix in $x^{(j)}$ has exactly $2j$ entries. Fix $j<k$ and put
$m=k-j\ge1$. The prefix is decreasing, and its last label, when present,
is $2m+2>1$. The next three labels are $(1,2m,2m+1)$, an increasing
triple. If another label follows, it is $2m-2<2m+1$; hence this triple
is a maximal increasing run. Every later run is exactly one of the
increasing pairs $(2r,2r+1)$, because the boundary between consecutive
pairs is a descent. All prefix runs are singletons. Thus the triple is
the unique active run.

ORR replaces it by $(2m+1,2m,1)$ and holds everything else. The descending
prefix gains its next two labels, giving exactly
$$T(x^{(j)})=x^{(j+1)}.$$
Each of these $k$ epochs is nonfixed, since its triple changes. The last
word is
$$x^{(k)}=(2k+1,2k,\ldots,2,1),$$
which is fixed. Therefore $\tau(x^{(0)})=k$. The case $k=0$ is the
singleton word and gives entrance time zero.

For even $n=2k+2$, prepend the new maximum $2k+2$ to the odd-size
construction on $[2k+1]$. It remains a singleton maximal run, because
it is larger than every label in the suffix at every time. The boundary
is permanently decreasing, so no maximal run crosses it. The suffix
executes the same $k$-epoch trajectory. This includes $n=2$.
The empty permutation at $n=0$ is held by definition. Consequently
$$H_n\ge\left\lfloor\frac{n-1}{2}\right\rfloor\quad(n\ge1).$$

### Step 2. Exact cross-parity inversion gain

An odd interval reversal preserves the parity of each position because
its endpoint sum is even. The initial position colours are therefore
fixed throughout the orbit.

Consider an active run of length $2r+1$ with $r\ge1$. One colour occurs
$r+1$ times and the other $r$ times. Before reversal its labels are
increasing, so none of its internal pairs is an inversion. After reversal
all of them are inversions, including exactly $r(r+1)$ cross-colour pairs.
A label outside the interval remains entirely before or entirely after
each label inside it, so no inside/outside pair changes its order. Two
different reversed intervals also retain their order relative to each
other. Hence, if the active run lengths in an epoch are $2r_i+1$,
$$J(T(x))-J(x)=\sum_i r_i(r_i+1).$$
In particular, every nonfixed epoch raises $J$ by at least two. This also
proves convergence: $J$ is a bounded integer, so infinitely many nonfixed
epochs are impossible. The orbit stops precisely at a fixed point.

### Step 3. Extremal range on one position-colour carrier

Fix the two label sets $A,B$ and consider all permutations placing $A$ at
odd positions and $B$ at even positions. Let $u$ place each colour class
in increasing order within its own positions, and let $v$ place each class
in decreasing order within its own positions. We prove
$$J(u)\le J(x)\le J(v)$$
for every word $x$ in this fixed-colour carrier.

Consider two adjacent positions within one colour class. In the full word
they have one intervening label of the opposite colour, giving a triple
$(a,b,c)$. If $a<c$, replacing it by $(c,b,a)$ raises $J$ by two when
$a<b<c$, and leaves $J$ unchanged when $b<a$ or $b>c$. This follows by
checking the two cross-colour pairs with $b$; all other cross-colour labels
are outside the three-position interval and keep their order relative to
$a$ and $c$. The reverse swap weakly lowers $J$.

Sorting the odd-position subsequence increasingly by adjacent
out-of-order swaps therefore never raises $J$. Sorting the even-position
subsequence increasingly has the same property, whether or not the first
subsequence has already been sorted. The final word is $u$. Sorting both
subsequences decreasingly, using the other direction of the same swaps,
never lowers $J$ and produces $v$. This establishes the two inequalities.

For odd $n=2m+1$, the whole-word reversal of $u$ is exactly $v$.
It reverses the order of every cross-colour pair. There are $m(m+1)$ such
pairs, so
$$J(v)=m(m+1)-J(u),\qquad J(v)-J(u)\le m(m+1).$$

For even $n=2m$, write
$$u=(a_1,b_1,a_2,b_2,\ldots,a_m,b_m),\qquad
v=(a_m,b_m,a_{m-1},b_{m-1},\ldots,a_1,b_1).$$
Each diagonal cross-colour pair $(a_i,b_i)$ has $a_i$ before $b_i$ in both
words, so its inversion contribution is unchanged. The relative order of
each off-diagonal pair $(a_i,b_j)$ with $i\ne j$ is reversed. There are
$m(m-1)$ off-diagonal pairs, each contributing at most one to the increase.
It follows that
$$J(v)-J(u)\le m(m-1).$$

Together, the two parity cases give the uniform capacity bound
$$J(v)-J(u)\le 2\binom{\lceil n/2\rceil}{2}.$$
The displayed proof also covers $n=1,2$; the empty carrier has no inversions.

### Step 4. The proved global upper bound

For an orbit with $h$ nonfixed epochs, Step 2 gives
$$2h\le J(T^h(x))-J(x).$$
Every state in the orbit lies in the same fixed-colour carrier, so Step 3
gives
$$J(T^h(x))-J(x)\le J(v)-J(u)
\le 2\binom{\lceil n/2\rceil}{2}.$$
Dividing by two and maximizing over all initial states yields
$$H_n\le\binom{\lceil n/2\rceil}{2}.$$
With Step 1 this proves exactly the stated corrected two-sided bound.
For $n=0$, the sole state is fixed and $H_0=0$. $\square$

## Corrections or Missing Assumptions

No additional assumption repairs the original conjecture here. The
quadratic bound is a proved weaker conclusion on the unchanged full
carrier, not the claimed linear upper bound under another name.

The first root note's local ancestry lemma gives a valid corollary: an
active successor run has the same endpoint-position parity as each of
its active parents. In the even-central-run case, it takes a single old
active endpoint and has even distance between its new endpoints; in the
singleton-central-run case, its two inherited endpoints are two positions
apart. Thus the endpoint parity propagates through the ancestry graph.
This colours the ancestry but does not bound its height.

The preserved seven-label trajectory is
$$
(2,5\mid1,4,7\mid3,6)
\longmapsto(2,5,7\mid4\mid1,3,6)
\longmapsto(7\mid5\mid2,4,6\mid3\mid1)
\longmapsto(7\mid5,6\mid4\mid2,3\mid1).
$$
Follow the valid active-parent chain with label sets
$$\{1,4,7\}\longrightarrow\{2,5,7\}\longrightarrow\{2,4,6\}.$$
Its last node adds only the one new label $6$ to the union of preceding
nodes; label $4$ returns after being absent in the middle node. The union
contains six labels, not the seven demanded by adding two fresh labels at
each of three active epochs. The other parent at the last step is
$\{1,3,6\}$ and supplies the seventh label to the full ancestry.

Therefore a single-chain distinct-label charge is false even though
inversions of individual label pairs are never deleted. The full branching
ancestry might still support an appropriate height bound, but no such
overlap-counting inequality is proved by this attempt. This trajectory
refutes the proposed charge, not the conjectured value of $H_7$.

## Open Risks

- The required bound $H_n\le\lfloor(n-1)/2\rfloor$ remains unproved.
- Cross-parity capacity counts possible pair events and gives a quadratic
  ceiling; it does not impose a linear bound on their sequential depth.
- Endpoint-parity inheritance does not prevent label reuse or merging of
  different ancestry branches. An injection assigning sufficiently many
  distinct labels to every depth has not been constructed.
- No structural closed form for the full recurrent entrance time or
  all-time normal form follows from the lower-bound family alone.
- These are author-level deductions. There is no new candidate gate,
  source clearance, admission or manuscript review.
