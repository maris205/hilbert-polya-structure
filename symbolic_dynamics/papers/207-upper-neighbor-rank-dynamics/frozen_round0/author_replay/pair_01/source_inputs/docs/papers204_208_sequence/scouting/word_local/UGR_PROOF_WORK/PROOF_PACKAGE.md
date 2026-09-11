# UGR — period-two core and a nonsharp uniform clock

2026-09-06 UTC. Author contributor: `batch197_fosp_gate`.
Existing root literal UGR; not a new rule, family, candidate number or seat.
Final research disposition: **HANDOFF_WITH_SOURCE_HOLD**.

## Claim

For $n\ge3$ and labelled cyclic words $x\in\{0,1,2\}^n$, define
$$U(x)_i=\mathbf1_{\{x_{i-1}>x_i\}}+
\mathbf1_{\{x_{i+1}>x_i\}},$$
synchronously with indices modulo $n$. Write
$h(x)=\min\{t\ge0:U^{t+2}(x)=U^t(x)\}$ when this set is nonempty,
and $H(n)=\max_x h(x)$.

The following statements hold.

1. Every orbit eventually has period one or two. In fact
   $$U^{4n+4}=U^{4n+2},\qquad H(n)\le4n+2.$$
   This is a **nonsharp, computer-assisted** uniform upper bound.
2. The only fixed point is $0^n$. The complete recurrent set is
   $\operatorname{Fix}(U^2)$, whose nonzero words have the exact cyclic
   block language in Step 4.
3. The eight-role graph in Step 5 has adjacency matrix $Q$, and
   $$|\operatorname{Fix}(U^2)|=1+\operatorname{tr}(Q^n),\qquad
   \det(I-zQ)=1-z^2-4z^3-2z^4+z^8.$$
   Thus there are precisely $\operatorname{tr}(Q^n)/2$ two-cycles.
4. $H(3)=1$. For every $n\ge4$, the explicit source
   $x=01^{n-1}$ has exact entrance
   $$h(01^{n-1})=\lfloor n/2\rfloor+1.$$
   Consequently $\lfloor n/2\rfloor+1\le H(n)\le4n+2$ for $n\ge4$.

## Status

**PROVABLE AS STATED, with the finite local lemma explicitly
computer-assisted.** The passage from that local certificate to every
cycle length is deductive and is detailed below. This does not claim a
closed handwritten proof of the local lemma, nor a sharp global clock.
In particular the observed $H(10)=6$ is not replaced by the upper bound
$4\cdot10+2=42$. The tempting formula
$H(n)=\max\{5,\lfloor n/2\rfloor+1\}$ for $n\ge4$ is **not proved or
claimed** here.

## Assumptions and ownership

- Comparisons are strict; the two neighbours are distinct because $n\ge3$.
- State heights are ternary. Higher alphabets and other neighbourhoods are
  not included in the claim.
- Positions remain labelled; no division by rotations is used.
- The input complement $Jx=2-x$ satisfies $U=F\circ J$ for LNR's lower-rank
  map $F$. Thus every one-step source set, fibre count and global fibre
  maximum transfers bijectively from LNR, with **zero new inverse credit**.
- Root's initial observation that strict extrema persist and reverse type
  is acknowledged and fully proved in Step 1. Root and this contributor
  are not independent reviewers of an eventual UGR contribution.
- LNR's direct local-rank owner comparison remains open as `LNR-S1`.
  That is not evidence that the unread lower-rank theorem covers UGR.
  UGR is the already executed literal in root's original pilot and still
  needs its own independent source/value assessment as a possible single
  rank-family representative.

## Notation

A site is a strict extremum if its height is strictly smaller than both
neighbours or strictly greater than both. Let $E(x)$ denote their set.
For a finite interval word, the same definition is used only at positions
whose two neighbours lie inside that interval.

For two consecutive states $x,y$, a temporal column is the pair
$(x_i,y_i)$. In a nonzero two-cycle the five possible column types will be
$$S_0=(0,2),\quad S_1=(2,0),\quad W_0=(0,1),\quad W_1=(1,0),\quad N=(1,1).$$
The subscript specifies the phase; $W$ sites come in adjacent equal-phase
pairs. These letters are proof notation, not additional state variables.

## Proof strategy and dependency map

1. Strict extrema form a monotone set of permanently alternating sites.
2. A finite radius-six local lemma states that a failure of two-step
   equality after two updates creates a new strict extremum within four
   updates. The executable certificate checks every local case by a fully
   justified inner-window/extension decomposition.
3. At most $n$ strict additions to a set of sites are possible, giving a
   uniform nonsharp clock and ruling out longer periods.
4. A separate two-time-column argument classifies all points of
   $\operatorname{Fix}(U^2)$ exactly; it does not depend on the local lemma.
5. A finite graph encodes that proved core bijectively. Matrix traces and
   its rational generating function are routine enumeration of the graph.
6. A single-seed wave is solved explicitly, proving a linear lower bound
   and an exact all-length witness clock independently of finite atlases.

## Proof

### Step 1. Permanent extrema

If $x_i$ is a strict local minimum, $U(x)_i=2$. At either neighbour the
old center is strictly lower, so that neighbour can count at most its
other neighbour as greater; both new neighbouring values are at most one.
Thus the new center is a strict maximum. If $x_i$ is a strict local
maximum, its new value is zero, and each neighbour counts the old center
as greater, so both new neighbouring values are at least one. The new
center is a strict minimum. It follows that
$$E(x)\subseteq E(Ux).\tag{1}$$
Every site in $E(x)$ has values $0,2$ alternating after its first update.
Any value two in a first image came from a strict minimum and is such a
permanent site. These statements use local comparisons, not an energy
analogy or a finite cycle observation.

### Step 2. Finite local growth lemma and complete extension coverage

**Local lemma.** Let $w=(w_{-6},\ldots,w_6)\in\{0,1,2\}^{13}$.
Define the truncated forward cone by $v^0=w$ and
$$v^{t+1}_j=\mathbf1_{\{v^t_{j-1}>v^t_j\}}+
\mathbf1_{\{v^t_{j+1}>v^t_j\}},\qquad |j|\le5-t,\quad0\le t<4.$$
If $v^4_0\ne v^2_0$, there exist
$$1\le s\le4,\qquad |j|\le5-s$$
such that $j$ is a strict extremum in row $v^s$ but is not a strict
extremum in row $v^0$.

This is the one computer-assisted lemma. The complete executable is
[verify_ugr.py](verify_ugr.py); the canonical contains all exceptional
inner words and a literal witness for **each of their nine extensions**.
It imports no root code, old probe or canonical file. Its main evolution
uses edge signs: for $e_j=\operatorname{sign}(v_{j+1}-v_j)$,
$$U(v)_j=\mathbf1_{\{e_{j-1}=-1\}}+
\mathbf1_{\{e_j=+1\}},$$
and a strict extremum is exactly $e_{j-1}e_j=-1$. Witnesses are also
checked directly using the two height inequalities. The original probe
used direct neighbour comparisons instead.

The finite exhaustiveness argument is part of the proof, as follows.
Take the inner word $u=(w_{-5},\ldots,w_5)$. The program enumerates all
$3^{11}=177147$ such words in lexicographic order. Their four-step inner
cones have row domains $|j|\le5-t$. The two center values at times two
and four are fully determined inside this cone. For each inner word:

- If those two values coincide, the local lemma's premise is false for
  **every** choice of the two outside letters.
- If they differ and an inner cone has a new strict extremum at time
  $s$ and position $|j|\le4-s$, that witness and its original non-extremum
  test use only known inner coordinates. Its truth therefore persists
  under **every** choice of outside letters.
- Exactly 204 inner words have unequal center values but no such inner
  witness. For each one, the program explicitly checks every
  $(w_{-6},w_6)\in\{0,1,2\}^2$: 1836 extensions in total. Every extension
  has a witness with $|j|\le5-s$ in the full cone. The complete canonical
  records each of these witnesses, not just the count of successes.

For any thirteen-letter word, its unique inner word is in exactly one
of these three classes. The first two classes handle all nine outside
choices by equality of the overlapping local cones; the third class
handles all nine explicitly. Hence **all $3^{13}=1594323$ initial words
are covered**, without assuming that the letters outside the inner
window are irrelevant in the exceptional cases. This proves the stated
finite lemma subject to the checked executable certificate.

Earlier shorter-cone conjectures were false and are not premises. Their
full outputs remain in `LOCAL_PROBE_CANONICAL.json` (290 counterexamples),
`LOCAL_PROBE_V2_CANONICAL.json` (1496) and
`LOCAL_PROBE_V3_CANONICAL.json` (204). The final radius-six extension is
essential to this certificate; no failed statement has been labelled PASS.

### Step 3. Deductive all-length consequence and the nonsharp bound

Consider any cycle and state $a$. Read thirteen cyclic coordinates around
an arbitrary center $i$, allowing repeated coordinates when $n<13$.
This produces a member of $\{0,1,2\}^{13}$, so the lemma applies. The
truncated cone agrees with the true cyclic trajectory wherever computed,
by induction on time and locality. Repeated coordinates do not invalidate
the implication: the finite certificate allowed every word, including
the consistent repetitions arising here.

If $E(U^4a)=E(a)$, then (1) implies no site became a new extremum in any
of the first four updates. The local lemma therefore rules out
$U^4(a)_i\ne U^2(a)_i$ for every $i$. Thus
$$E(U^4a)=E(a)\quad\Longrightarrow\quad U^4a=U^2a.\tag{2}$$

Apply (1) to the sets $E(U^{4q}x)$ for $q=0,1,\ldots,n+1$. They are
increasing subsets of an $n$-element set. Not all of the $n+1$ inclusions
can be strict, so for some $0\le q\le n$,
$E(U^{4q+4}x)=E(U^{4q}x)$. Set $a=U^{4q}x$ in (2). It gives
$$U^2(U^{4q+2}x)=U^{4q+2}x.$$
Thus this trajectory enters $\operatorname{Fix}(U^2)$ by time
$4q+2\le4n+2$. Once in that set, it remains there, since $U$ commutes
with its own square. This proves $U^{4n+4}=U^{4n+2}$ on the whole
carrier and excludes every period greater than two.

The proof uses no all-size inference from the original $n=3,\ldots,10$
cyclic atlas. The only finite exhaustive premise is the size-independent
local rule lemma, whose arbitrary-length embedding and complete coverage
were both proved explicitly.

### Step 4. Exact two-period core, by temporal columns

Let $y=Ux$ and suppose $Uy=x$. If $x_i=2$, then $y_i=0$; if $y_i=2$,
then $x_i=0$. The possible temporal columns are therefore
$S_0,S_1,W_0,W_1,N$ and $(0,0)$.

If a column is $(0,0)$, the equation $y_i=0$ at height $x_i=0$ forces
both its neighbours to have height zero in $x$. The reverse equation
$x_i=0$ at height $y_i=0$ forces both neighbouring heights zero in $y$.
Thus both neighbouring columns are also $(0,0)$, and connectedness of
the cycle makes every column $(0,0)$. Hence a nonzero core word uses
only the five displayed types.

A neutral column $N=(1,1)$ needs exactly one neighbour of height two in
$x$ and exactly one neighbour of height two in $y$. Those two neighbours
must be distinct, because a height-two column is $S_0$ or $S_1$. They
are therefore $S_0,S_1$ in either order. In particular a neutral column
cannot neighbour a weak column. This last exclusion uses the **neutral
neighbour's own equation**, not only the equation at a weak center.

At a $W_0=(0,1)$ site, exactly one $x$-neighbour is positive, because
its next value is one. Neither neighbouring $y$-value is two, because
the value one must next become zero. The zero $x$-neighbour is therefore
another $W_0$; the positive $x$-neighbour is $S_1$ or $W_1$. A neutral
neighbour has already been excluded by its own equation. Thus every
$W_0$ has exactly one $W_0$ neighbour, and the other neighbour has the
opposite phase. The same argument with $x,y$ exchanged applies to $W_1$.
Consequently weak sites form unique adjacent dimers of equal phase;
their outside neighbours have the opposite phase and are strong or weak.

At an $S_0=(0,2)$ site both $x$-neighbours are positive, so they are
$S_1,W_1$ or $N$. Exchanging the two times gives the corresponding rule
for $S_1$. These conditions are also sufficient, by substitution into
both literal rank equations.

Translate these columns into the single word $x$. A zero run is either
one $S_0$, of length one, or one $W_0$ dimer, of length two. A positive
run consists of one $S_1$ with an optional neutral site on either end,
or one $W_1$ dimer. Therefore the exact nonzero core language is:

- every maximal zero run has length one or two;
- every maximal positive run is one of
  $$2,\quad11,\quad12,\quad21,\quad121;$$
- a positive run $12$ or $121$ has a **singleton zero run on its left**;
- a positive run $21$ or $121$ has a **singleton zero run on its right**.

The last two conditions ensure that a neutral site neighbours a strong
$S_0$, not a weak dimer. Conversely, from any word in this cyclic
language, assign strong columns to singleton zeros and twos; weak columns
to $00$ and $11$ dimers; and neutral columns to the remaining isolated
ones adjacent to twos. Every column condition above holds, proving
$U^2x=x$. The assignments recover the original coordinates uniquely.
There is no zero-free exception: every image of $U$ has a zero at a
global maximum of its source.

Finally a fixed point cannot contain two, because two always maps to
zero. Without twos, every one also maps to zero. Thus $0^n$ is the only
fixed point. Every other word of the classified core has exact period two.

### Step 5. Evaluated finite graph for the core

Use eight roles in the order
$$S_0,S_1,W_{0L},W_{0R},W_{1L},W_{1R},N_{01},N_{10}.$$
The two $W$ roles distinguish the left and right sites of their unique
dimer; $N_{01}$ lies between $S_0$ on the left and $S_1$ on the right,
and $N_{10}$ has the reverse bounds. Their emitted heights in $x$ are
$0,2,0,0,1,1,1,1$. The complete allowed transitions are

| Role | Following roles |
|---|---|
| $S_0$ | $S_1,W_{1L},N_{01}$ |
| $S_1$ | $S_0,W_{0L},N_{10}$ |
| $W_{0L}$ | $W_{0R}$ |
| $W_{0R}$ | $S_1,W_{1L}$ |
| $W_{1L}$ | $W_{1R}$ |
| $W_{1R}$ | $S_0,W_{0L}$ |
| $N_{01}$ | $S_1$ |
| $N_{10}$ | $S_0$ |

Let $Q$ be this zero-one adjacency matrix. Each labelled closed walk of
length $n$ emits a nonzero core word by the column conditions. Conversely
the proved language recovers each site's role, including which end of
a weak dimer it occupies. Thus this is a bijection on **labelled words**,
not a count of rotation classes, and
$$c_n:=|\operatorname{Fix}(U^2)|=1+\operatorname{tr}(Q^n).\tag{3}$$
Flipping all phase labels applies $U$ on the emitted word and exchanges
the two members of every nonzero cycle. This also explains why the
trace is even.

Eliminating the deterministic dimer and neutral intermediate roles gives
a two-type block transfer
$$B(z)=\begin{pmatrix}z(1+z)&z^2\\z&z^2\end{pmatrix}.$$
A strong block has length one, a weak block length two, and a neutral
site may be inserted only between two successive strong blocks.
Successive blocks have opposite phases. The full block matrix is
$\begin{pmatrix}0&B(z)\\B(z)&0\end{pmatrix}$, so
$$\det(I-zQ)=\det(I-B(z))\det(I+B(z))
=(1+z^4)^2-(z+2z^2)^2
=1-z^2-4z^3-2z^4+z^8.\tag{4}$$
This can also be verified directly by the finite eight-by-eight Leibniz
determinant; the certificate does so with exact integers.

For a purely evaluated counting recurrence, put $a_n=\operatorname{tr}(Q^n)$
and $D(z)=1-z^2-4z^3-2z^4+z^8$. Then
$$\sum_{n\ge1}a_nz^n=-\frac{zD'(z)}{D(z)}.$$
This identity follows by expanding $\log\det(I-zQ)$ as a formal power
series, or by the characteristic polynomial and the initial traces.
In particular
$$a_n=a_{n-2}+4a_{n-3}+2a_{n-4}-a_{n-8}\qquad(n\ge9),$$
with $a_1,\ldots,a_8=0,2,12,10,20,62,84,154$. Equation (3) is asserted
for the original carrier only when $n\ge3$. Matrix traces, determinant
identities and periodic-point bookkeeping are standard tools and receive
no independent novelty credit.

### Step 6. An exact single-seed wave and the lower clock

Let $n\ge4$, $m=\lfloor n/2\rfloor$, and start from the seed
$z^0=20^{n-1}$. Write $d(i)=\min\{i,n-i\}$ for cyclic distance from
the seed, taking indices $0,\ldots,n-1$. For $0\le s<m$ the exact
profile is
$$z_i^s=\begin{cases}
2\mathbf1_{\{s\text{ even}\}},&d(i)=0,\\
2\mathbf1_{\{s-d(i)\text{ even}\}},&0<d(i)<s,\\
1,&d(i)=s>0,\\
0,&d(i)>s.
\end{cases}\tag{5}$$

At $s=0$ this is the stipulated seed. To prove the induction before the
two fronts meet, each already interior site alternates with opposite
neighbour phases. An advancing boundary one has two zero neighbours,
so becomes zero; the next outer zero has one positive neighbour and
one zero neighbour, so becomes one. At the site just inside the old
front, the new two comes from a zero with two positive neighbours.
The seed itself alternates by Step 1. Sites farther ahead have only
zero neighbours. These cases exhaust the profile and prove (5).

At $s=m$, for even $n=2m$ the two fronts meet at the single remaining
zero, which sees two ones and becomes two. The entire word is alternating
zero/two. For odd $n=2m+1$, the two remaining adjacent zeros each see
one front one and become the weak dimer $11$; all other sites are
alternating strong sites. In both cases the resulting word belongs to
the proved core language.

For $1\le s<m$, a frontier one in (5) has two zero neighbours, including
at $s=m-1$ for both parities. It is a strict maximum of height one.
Its second iterate is two by Step 1, so the word is not in
$\operatorname{Fix}(U^2)$. At $s=0$, the seed's nonempty remaining zero
run has length $n-1\ge3$, excluding it from the core language. Hence
$$h(20^{n-1})=m.$$
The source $01^{n-1}$ maps in one step to that seed; because the seed is
not initially in the core, the source has exact entrance $m+1$.

For $n=3$ the cycle is the complete three-vertex graph. Equal source
heights give $000$. Two equal lower heights and one higher height give
a rotation of $110$; one lower and two equal higher heights give a
rotation of $200$. Three distinct heights give a permutation of $210$.
These are all in the proved core. The source $001$ is not in the core
but its first image is, so $H(3)=1$. This completes every claimed
mathematical statement. $\square$

## Corrections and preserved failed evidence

The shorter local-cone growth statements failed and remain archived as
described in Step 2. An initial integrated verifier also imposed the
weak-column classification on a center triple without requiring its
neutral neighbour's own equation. The complete core proof above always
requires that equation. The failed checker and output are preserved as
`verify_ugr.failed_v1.py`, `FAILED_V1.stdout`, and `FAILED_V1.stderr`.
The corrected certificate checks sufficiency on all five-type triples
and necessity on all five-column windows whose three central equations
hold. This is an explicit correction of the test's domain, not suppressed
evidence or a claim that the failed test passed.

## Open risks and research disposition

The upper clock is not sharp. The generic finite graph enumeration and
LNR-transferred inverse results are not new independent axes. The local
growth lemma is a computer-assisted finite theorem, with its coverage
argument exposed for independent reproduction; it has not had an actual
independent UGR candidate review in this package.

UGR's own independent source/value assessment has not occurred. See
[SOURCE_HOLD.md](SOURCE_HOLD.md) and the unmodified LNR gate. The open
LNR-S1 finding is preserved, but an unread lower-rank theorem neither
establishes ownership of UGR nor automatically disposes of its distinct
temporal claims. The proven LNR global fibre comparison may remain part
of one rank-family representative; transporting it to UGR creates no
additional axis or second seat. The final handoff is
**HANDOFF_WITH_SOURCE_HOLD / NO_PROMOTION / HOLD_EXTERNAL**, pending that
actual assessment, not a mathematical or source admission or a proved
UGR killing adapter.
