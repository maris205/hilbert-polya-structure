# MCT: independent all-parameter rederivation

2026-09-05 UTC. Candidate Stage1 gate, not a manuscript review. The gate
read the exact frozen contract, inverse proof, and temporal proof, but no
author or temporal-pressure verifier source. This document does not extend
the candidate's contribution claims. In particular the auxiliary root-zero
observation below is an alternative audit argument, not a needed repair.

## 1. Literal and zero-credit recurrence

The carrier at $n\geq0$ is all binary colours on the pairs of
$[n]=\{0,\ldots,n-1\}$. Let $Q(G)$ be the least increasing triple whose
three pair colours agree. If it exists, $F(G)$ reverses those three colours;
otherwise $F(G)=G$. All three changes are simultaneous. The labels are
fixed, and lexicographic order is reapplied to the current graph.

Write $G^Q$ for a reversal and $Q_t=Q(G_t)$. A moving selector survives
its own reversal, hence $Q_{t+1}\leq Q_t$. Equality returns to $G_t$ on
the next step. A strict change replaces one vertex by a smaller one,
shares exactly one edge with $Q_t$, and reverses the selected colour.
Indeed a new earlier monochromatic triple must contain a changed edge;
two distinct triples share at most one edge. A nonholding source cannot
have a fixed output. Finite selector descent therefore ends in a strict
two-cycle. A moving state is recurrent exactly when its selector is
unchanged at the next state. Its entrance time $h$ equals the number of
strict selector transitions before that first equality. There is no extra
step at the recurrent endpoint. All of this is generic least-involution
bookkeeping, deducted entirely.

For $n<3$ all states hold. At $n=3$ the two monochromatic states exchange
and the other six hold. Thus all small-parameter fibres have size one and
$H(n)=0$ for $n\leq3$.

## 2. Temporal proof, independently challenged

### A two-step obstruction

Suppose consecutive strict transitions used the same shared edge:
$abc\to abd\to abe$, of colours $q,1-q,q$. The edges $ae,be$ are
untouched during the first two reversals and $ab$ is restored. Thus
$abe$ was already monochromatic before the first reversal, although it
precedes $abc$. This contradiction rules out repeated shared edges.

### An alternative anchor argument

After one update of any moving state, the selected triple contains vertex
$0$. If the old selector already contains $0$, this follows from selector
nonincrease. Otherwise let the old triple have colour $q$. At most one
of its three spokes to $0$ has colour $q$, since two such spokes would
make a smaller monochromatic triple before the update. At least two
spokes therefore have colour $1-q$. Their joining edge becomes $1-q$
on reversal, producing a monochromatic triple containing $0$. The new
least selector contains $0$. Subsequent moving selectors keep it.

The frozen author's weaker anchor-stabilization argument is also complete
without this observation. To check its most delicate local step, write
$Q_0=abc$, $Q_1=dab$, and suppose $Q_2$ has a smaller minimum. The
shared-edge obstruction permits $Q_2=eda$ after renaming common vertices.
Here $d<c$ and $e<\min Q_1$, so $e$ is below all of $Q_0$. If $Q_0$
has colour $q$, the unchanged edge $ea$ has colour $q$. Initial
minimality forces $eb=ec=1-q$. After the first reversal, $ebc$ is
monochromatic and precedes $Q_1$, a contradiction. This is a valid
standalone proof that the minimum cannot drop after the first strict
change. The gate does not supply a missing lemma to the frozen proof.

### No return in an anchored segment

In a segment with a common least vertex $a$, orient the first two
nonanchor vertices according to the first departure. The prohibition on
repeated shared edges makes the segment a sliding pair:

$$Q_t=\{a,v_t,v_{t+1}\},\qquad v_{t+2}<v_t.$$

The even and odd subsequences separately decrease. A first repeated
vertex $v_i=v_j$ must thus have opposite-parity indices. For $i\geq1$
its anchor edge is flipped on entry and departure, restoring its first
entry colour $c_{i-1}$ while it is absent. The returning triple would
require $c_{j-1}$, its opposite. For $i=0$ the initial vertex receives
only the departure flip, retaining $1-c_0$; an odd return index requires
$c_{j-1}=c_0$. Both cases contradict eligibility. Consecutive equal
vertices cannot occur in a triple, so the endpoint conventions do not
hide an exception.

### The initially retired vertex

It remains possible that the first transition drops the least vertex:
$Q_0=\{r,u,v\}$, $Q_1=\{a,u,v\}$ with $a<\min Q_0$. Put
$q=c_0$ and $\gamma=1-q$. In $G_1$ all of $au,av,uv,ru,rv$ have
colour $\gamma$, while $ar$ is unchanged. Initially every set of
vertices whose spokes to $a$ have colour $k$ has all internal edges of
colour $1-k$: an exception would precede $Q_0$.

If $ar=\gamma$, then $aru$ and $arv$ are monochromatic at $G_1$.
Minimality of $auv$ forces $r>u,v$, and neither decreasing subsequence
can introduce $r$.

If $ar=q$, take the anchored segment beginning at $G_1$ and orient it
as $v_0=u,v_1=v$. A first entrance of $r$ at relative time $k$ requires
$k$ odd. Its partner $w=v_k$ lies in the odd decreasing subsequence,
so $w\leq v$. If $w=u$ or $v$, the edge $rw$ already has colour
$\gamma$ and blocks the return. Otherwise $w<v$, and at its first
entry, time $k-1$, its anchor spoke has colour $\gamma$; before first
entry that spoke was untouched. Consequently $u,v,w$ belong to the
same initial $a$-spoke class, and $wu=wv=q$ initially. If $rw=q$
initially, then $ruw$ was monochromatic before $Q_0$ and replaces
$v$ by the smaller $w$, contradicting minimality. Hence $rw=\gamma$.
This edge remains unchanged while $r$ is absent and again blocks its
return. This accounts for the only old vertex outside the first anchored
triple; merely decreasing labels would not have sufficed.

Every strict transition therefore introduces a genuinely unused vertex.
The initial triple uses three, proving $h\leq n-3$ on every moving
state for $n\geq3$.

### Uniform attainment, not extrapolation

Let $N=n-1$, $v_i=n-1-i$ for $0\leq i<N$, and use anchor $0$.
Assign spokes $s_0=s_1=0$, $s_i=(i-1)\bmod2$ for $i\geq2$.
For $i<j$, assign the rim edge

$$b_{ij}=\begin{cases}
i\bmod2,&j=i+1,\\
1-s_i,&j>i+1,\ s_i=s_j,\\
s_i,&j>i+1,\ s_i\ne s_j.
\end{cases}$$

Initially the only eligible pair of spokes is $v_0v_1$. At time
$t\geq1$, $v_t$ is the carry vertex, whose spoke was flipped once;
retired vertices other than $v_0$ had two flips and recover their
original spoke colours; $v_0$ has spoke colour one; future spokes retain
their assigned colours. Two future vertices cannot be eligible. A
retired/future pair is ineligible by the same-colour/opposite-rim rule,
including the exceptional $v_0$, whose edges to future colour-one
spokes are zero. Eligible retired pairs are later in label order.

The future vertices with the carry's current colour are indexed
$t+1,t+3,\ldots$. The consecutive rim edge has colour $t\bmod2$.
Every later such rim edge has colour $s_t=1-(t\bmod2)$ and is
ineligible. A carry/retired pair is later. Thus the selector at every
$0\leq t\leq n-3$ is exactly
$\{0,v_t,v_{t+1}\}$, with colour $t\bmod2$. The last selector is
$\{0,1,2\}$ and necessarily repeats after reversal. The source has
exact tail $n-3$. This proves $H(n)=\max\{n-3,0\}$ at every parameter.

## 3. Every-target inverse from forbidden local patterns

Take a target $Y$. A nonholding predecessor must reverse a target
monochromatic triple $Q$, of colour $c$. For each earlier triple $P<Q$:

- If $P$ shares no edge with $Q$, it must be mixed in $Y$.
- If it shares the edge $e$, its two other edges must not both have
  colour $1-c$.

These clauses are necessary and sufficient for no earlier monochromatic
triple in the proposed source. No other pair changes. This is exactly the
author's D/C decomposition into destruction and creation, but the gate
verifier directly uses forbidden target equalities without evaluating a
source selector. Reversing distinct triples produces distinct graphs.
If $Y$ has no monochromatic triple, no moving source reaches it, so its
only source is itself. Otherwise the accepted reversals give its entire
fibre, possibly empty. This supplies an exact target image test as well.
Undo-and-priority-filter as a general method receives zero credit.

For the least monochromatic triple of a target, the first clause is
automatic; the second clause is exactly its recurrent-state test. This
is checked but is not a separate credited theorem axis.

## 4. Classical cap, literal attainment, and every equality target

If accepted inverse triples satisfy $P<Q$, the monochromatic $P$ must
be destroyed by reversing $Q$. They therefore share an edge. The family
is a clique in $J(n,3)$. The familiar classification gives a common-edge
star or containment in the faces of a four-set. Explicitly, relative to
$abc,abd$, any further triple either contains $ab$ or is $acd$ or
$bcd$; in the latter cases every further star member must stay inside
$\{a,b,c,d\}$. The capacities $n-2$ and $4$, their crossover, and
this static classification are all owned background, not MCT discoveries.

Literal attainment needs more than the static bound. For a full star,
make every edge incident to $0$ or $1$ colour $c$, and all other edges
colour $1-c$. Every $01v$ is an accepted inverse. For a full top, make
every edge colour $c$ except $0v$ for $v\geq4$, which has colour
$1-c$. All four faces of $\{0,1,2,3\}$ are accepted. To check the
last face $123$, any earlier outside triple containing $0$ is mixed;
any remaining potential earlier triple shares an edge with $123$ and
is destroyed. These give the asserted cap as an actual fibre maximum,
not just a bound on abstract set families.

For completeness, the all-target equality tests can be derived without
running the map. Fix $a<b$, outside set $U$, and $c=y_{ab}$. All star
faces are monochromatic exactly when $y_{az}=y_{bz}=c$ for every
$z\in U$. Then a reversal cannot create a new monochromatic triple:
an unchanged incident edge has colour $c$. The possible surviving
competitors are $axy,bxy$ with $y_{xy}=c$, when the reversed face's
outside vertex is not $x$ or $y$; since $axy<bxy$, these yield exactly
S2. Monochromatic triples wholly inside $U$ must be later than the
last star face, exactly S3. Thus S1--S3 are an iff for a full accepted
star, for arbitrary labels, not merely the witness's edge $01$.

For a four-set $S$, all faces monochromatic is equivalent to one colour
on its six edges. A competing triple with at most one vertex in $S$
is untouched by every reversal and must follow the last face, giving
K2. A triple $uxy$ with exactly two vertices inside has equal external
spokes or unequal ones. Unequal spokes never give eligibility. If both
equal the internal colour, exactly the faces not containing $xy$ leave
it eligible; if both have the opposite colour, exactly the faces
containing $xy$ make it eligible. Excluding earlier eligibility in
those respective face collections is K3. Internal faces are destroyed
by each other. This proves K1--K3 in both directions.

Equality now forces a full largest star or a full top. Hence all targets
maximize for $n\leq3$; for $n=4,5$ exactly the certified tops maximize;
at $n=6$ the certified stars or tops maximize; for $n\geq7$ exactly the
certified stars maximize. No count of those targets for arbitrary $n$ is
claimed. The finite counts in the canonical transcript are not formulas.

## 5. Adversarial boundary

The frozen proofs are complete without the gate's anchor observation.
No theorem repair, carrier restriction, larger-box extrapolation, or
changed entrance convention is needed. Generic scheduling, source undo,
Johnson cliques, Ramsey counts and graph complementation are deducted.
The temporal no-return argument and literal ordered-colour equality
certificates have separate mechanisms; neither proves the other. This is
a candidate-level correctness/value judgement subject to the separate
bounded owner audit, not a novelty or publication certificate.
