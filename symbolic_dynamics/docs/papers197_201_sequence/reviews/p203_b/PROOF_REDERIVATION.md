# P203 B: all-parameter proof rederivation

Target: physically frozen repaired Round1, main.tex SHA-256
70c22a62adc3b6218278a6fd91b08dfa8d02efddf03ba7cc115bd35a3ab6de54.
Status: the printed statements below are established under their stated
hypotheses. Finite checks corroborate them but are not premises.

This is a fresh manuscript audit, following earlier familiarity from the
reviewer's MCT Stage1 gate. The original author temporal proof and inverse
proof have both been reread completely, along with their manuscript
transcription. The optional reviewer observation about vertex zero is not
used below: no missing author step is being supplied by that observation.
The reasoning is organized as an edge-event accounting audit, followed by
an independent target-forbidden-pattern reconstruction.

## 1. Literal carrier and the zero-credit recurrent engine

For every integer $n\geq0$, the carrier is all assignments of a bit to
each unordered pair of distinct vertices in $[n]=\{0,\ldots,n-1\}$.
There are no forest, parity-class, degree, tournament or connectedness
restrictions. A selected triple is the least sorted triple whose three
pair bits agree. Its three bits are complemented simultaneously; all
other bits are unchanged. An empty selector means hold.

The flipped triple remains monochromatic. Thus on a moving orbit its
selectors cannot increase. If two consecutive selectors agree, the second
flip undoes the first and those two distinct states are recurrent. If a
selector decreases, that state cannot be recurrent: returning would
require increasing the selector. A moving state cannot reach a holding
state. Consequently the entrance time is exactly the number of strict
selector transitions before the first equal transition. This convention
counts the first recurrent state at time $\tau$, not $\tau+1$.

These facts are generic least-involution consequences and receive zero
research credit. They only set up the substantive vertex budget.

On a strict transition $Q\to Q'$, the new triple was previously mixed.
Distinct triples share zero or one pair, so it must share exactly one
flipped pair with $Q$. The unchanged two bits now equal the complemented
shared bit. The selected colour alternates, and the new vertex is smaller
than the removed vertex. This is the local event rule used below.

## 2. Two local prohibitions, with no all-size extrapolation

**Repeated shared edge.** Suppose three consecutive strict selectors are
$abc,abd,abe$, with colours $q,1-q,q$. Strict order gives $e<d<c$,
so $e$ differs from every vertex of the first two triples. At the third
selector, $ae,be$ have never changed, while $ab$ has changed twice.
All three therefore already had colour $q$ initially. But $abe<abc$,
contradicting the initial least choice.

**A second minimum drop is impossible.** Consider any two consecutive
strict transitions. Write the first two triples $abc,dab$, where $d<c$.
If the minimum drops at the third triple, the previous prohibition
excludes sharing $ab$ again. Interchanging $a,b$ if needed, the third
triple is $eda$, with $e<\min(d,a,b)$. In particular $e$ is below all
of $a,b,c,d$. If the first colour is $q$, the third is $q$ and its
untouched edge $ea$ has colour $q$. Initial leastness rules out both
$eab$ and $eac$, forcing $eb=ec=1-q$. Immediately after flipping
$abc$, the triple $ebc$ has colour $1-q$ and precedes $dab$:
contradiction. Applying this at each adjacent pair of strict transitions
proves that the minimum is constant after the first transition.

## 3. No return, including the initially retired vertex

First take a strict trace whose least vertex $a$ is constant from its
start. Orient its first two other vertices according to which one is
removed first, not by numerical order. No repeated shared edge forces
the sliding form
$$
 Q_t=\{a,v_t,v_{t+1}\},\qquad v_{t+2}<v_t.
$$
Both parity subsequences strictly decrease. If the first repeated vertex
has indices $i<j$, then their parities are opposite. For $i\geq1$, its
anchor edge is flipped on entry in $Q_{i-1}$ and on departure in $Q_i$.
Thereafter that edge retains colour $c_{i-1}$. Return in $Q_{j-1}$
requires colour $c_{j-1}$, the opposite value because the index parities
differ. For $i=0$, the single departure flip leaves colour $1-c_0$,
whereas odd $j$ requires $c_{j-1}=c_0$. Both are impossible.

The remaining case is exactly the exception stressed in the manuscript.
Suppose the first transition changes the minimum:
$$
 Q_0=\{r,u,v\},\quad Q_1=\{a,u,v\},\quad a<\min(r,u,v).
$$
Write the initial colour $q$ and $\gamma=1-q$. In $G_1$, all five
edges $au,av,uv,ru,rv$ have colour $\gamma$, and $ar$ is unchanged.
Initially no monochromatic triple contains $a$, since each such triple
precedes $Q_0$. Thus each initial anchor-colour class $k$ has all
internal pair colours $1-k$.

If $ar=\gamma$, the monochromatic triples $aru,arv$ in $G_1$ force
$r>u$ and $r>v$ by minimality of $auv$. The two strictly decreasing
subsequences of the later fixed-anchor trace cannot introduce $r$.

If $ar=q$, orient that later trace as $v_0=u,v_1=v$ according to
first removal. Suppose $r$ first returns at relative selector time $k$.
The unchanged anchor edge requires odd $k$. Hence $r=v_{k+1}$ has
even position, its partner $w=v_k$ has odd position, and $w\leq v$.
If $w\in\{u,v\}$, the unchanged edge $rw=\gamma$ blocks the required
colour-$q$ triple. Otherwise $w<v$. Its first entry was at even time
$k-1$ and its anchor edge was untouched beforehand, so its initial
anchor colour was $\gamma$. The initial colour-class rule gives
$wu=wv=q$. If initially $rw=q$, then $ruw$ was a colour-$q$
triple preceding $ruv$ because $w<v$, impossible. Therefore
$rw=\gamma$; since $r$ was absent, this edge has not changed and
again blocks return.

This handles the only vertex not covered by the fixed-anchor first-repeat
argument. There is no reliance on the optional vertex-zero observation.
The author proof is complete without a repair or a reviewer-supplied lemma.

## 4. Sharp entrance time, including small parameters

The first selected triple uses three vertices. Each strict transition uses
one additional distinct vertex, so $\tau\leq n-3$ for $n\geq3$.
For $n<3$ every state holds. At $n=3$, either the sole triple is mixed
and holds or the two constant states interchange; all states are recurrent.

For a sharp witness at every $n\geq3$, put $N=n-1$,
$v_i=n-1-i$ for $0\leq i<N$, and use anchor 0. Set its spoke colours
$s_0=s_1=0$, $s_i=(i-1)\bmod2$ for $i\geq2$. For $i<j$ set
$$
 x_{v_i v_j}=
 \begin{cases}
 i\bmod2,&j=i+1,\\
 1-s_i,&j>i+1,\ s_i=s_j,\\
 s_i,&j>i+1,\ s_i\ne s_j.
 \end{cases}
$$
The intended selector at time $t$ is $0v_tv_{t+1}$, with colour
$t\bmod2$, for $0\leq t\leq n-3$.

Initially the only monochromatic anchor triple is $0v_0v_1$.
For induction at $t\geq1$, the carry $v_t$ has one anchor flip,
retired vertices $v_i$ for $1\leq i<t$ have two, the exceptional
$v_0$ has one and therefore colour 1, and future vertices have none.
No two future vertices are eligible: equal spokes have opposite pair
colour. A retired/future pair is also ineligible by the unchanged
equal-class pair rule; the exceptional $v_0$ has colour-zero edges to
all future colour-one spokes. Any eligible retired/retired or
carry/retired pair is later than the intended pair, since retired labels
exceed future labels.

Future spokes matching the carry are indexed $t+1,t+3,\ldots$.
The first has the correct consecutive pair colour. For $j\geq t+3$,
the initial classes differ and the pair has $s_t=1-(t\bmod2)$,
which is wrong. Non-anchor triples are later regardless of colour.
Thus the entire itinerary is proved, not just its last state.
Its last triple is 012, the least possible triple, and is selected again
after the flip. Exactly $n-3$ preceding transitions were strict, proving
$H(n)=\max(0,n-3)$.

## 5. A target-first inverse derivation

Fix a target $Y$. A moving predecessor must be $Y^Q$ for a triple
$Q$ that is monochromatic in $Y$. Distinct triples toggle distinct
pair sets, so their reconstructed sources are distinct. Let its target
colour be $c$ and inspect each earlier triple $P<Q$.

If $P$ shares no pair with $Q$, it is untouched and must be mixed
in $Y$. If it shares a pair $xy$, that is the only bit that changes.
An earlier target-monochromatic $P$ is destroyed by that change.
An earlier mixed $P=\{u,x,y\}$ becomes monochromatic exactly when
both untouched bits $y_{ux},y_{uy}$ equal $1-c$. No other case exists.

Accordingly the necessary and sufficient conditions are exactly D and C
in the paper: D destroys every earlier target-monochromatic triple;
C excludes every new earlier monochromatic triple. These conditions make
$Q$ the least triple in the reconstructed source, proving sufficiency
as well as necessity. They do not run the source selector.

A target with no monochromatic triple has only its self-source, since a
nonholding output always contains the flipped monochromatic triple.
For a moving target, its fibre is empty exactly when no $Q$ passes D/C.
For its least triple, D is vacuous and C is precisely the condition for
equal consecutive selectors. This proves the image and recurrent iff
statements with no missing holding or empty-fibre cases.

## 6. Static bound, realizability, and all maximum targets

If $P<Q$ are admissible inverse triples, D for $Q$ forces them to
share a pair. Their family is therefore a clique of the classical Johnson
graph on triples. This static classification and capacity are fully owned
background, not another contribution axis.

For completeness, take two members $abc,abd$. Any further member either
contains $ab$ or is $acd$ or $bcd$. If one of the latter occurs, any
common-$ab$ member has its third vertex among $c,d$, so the entire
family lies in the four-set. Otherwise every member contains $ab$.
Families of at most two also lie in such a containing star or top.
Thus the capacities are $n-2$ and 4. For $n\leq3$ the map is a
permutation. This yields $M_n=1$ there and the upper bound
$\max(4,n-2)$ for $n\geq4$.

Both capacities are realized for every $n\geq4$.
For the full star on 01, give all edges incident with 0 or 1 colour $c$
and all remaining edges colour $1-c$. Each $01z$ passes D/C.
For the four faces of 0123, give all edges colour $c$ except $0z$
for $z\geq4$, which have colour $1-c$. Each face passes D/C:
triples with 0 and an outside vertex are mixed; a triple without 0 but
outside 0123 comes later than 123. These are all-size constructions,
not empirical extrapolations.

To verify the *complete* target classification, inspect all potential
interfering triples under a reversal, not merely the extremal examples.

For a proposed star on $a<b$, S1 makes all its triples monochromatic.
Under S1, reversing a star triple creates no earlier monochromatic
triple: any putative newly monochromatic triple sharing an incident edge
has another unchanged colour-$c$ spoke. Other star triples are destroyed
through $ab$. The surviving non-star triples with an endpoint are
$axy,bxy$ where $x,y$ are outside and $y_{xy}=c$; they survive
reversal of $abz$ exactly when $z\notin\{x,y\}$. Since $axy<bxy$,
requiring every such survivor to be later than $abz$ is exactly S2.
Wholly outside monochromatic triples never change; they must be later
than every star triple, equivalently later than its last one, exactly S3.
Thus S1--S3 are iff for the entire star being admissible.

For a proposed four-set $S$, K1 makes its four faces monochromatic.
Other faces are destroyed upon reversing one face. Triples with at most
one vertex of $S$ never change and yield K2. A triple $uxy$ with two
vertices in $S$ changes exactly when $xy$ belongs to the reversed face.
If its two outside spokes both have colour $c$, it is monochromatic
exactly for faces not containing $xy$. If both have colour $1-c$,
exactly for faces containing $xy$. Mixed spokes are never eligible.
The required ordering in these two cases is precisely K3. Hence K1--K3
are iff for all four faces being admissible.

An equality family fills a containing star or top of largest capacity.
At $n=4,5$ only a full top can have maximum size; at $n=6$ either
capacity is 4; at $n\geq7$ only a full star can maximize. Together
with the separate $n\leq3$ permutation case, this proves every
alternative of Theorem 4.2, in both directions. No formula counting
all equality targets for unbounded $n$ is claimed.

## 7. Independent exact control and its limits

The reviewer-owned program uses symmetric row strings and character
replacement for the literal map. Integers only enumerate/store states.
It discovers recurrent components by Kosaraju SCCs and entrance distances
by reverse BFS; periods and depths are not built from the theorem.
The inverse program instead evaluates target forbidden-colour clauses.
All candidate stars and four-sets are tested against that family, not
only those targets that happened to maximize the measured fibre.

Two fresh final executions cover all $33,868$ MCT states for $0\leq n\leq6$.
Each performs 1,502,359 assertions, with identical bytes. They check full
predecessor sets, empty fibres, image iff, least-triple C iff, cycles,
depths, mass conservation, strict new-vertex traces, initial-retired
nonreturn, all S/K iff tests, and every finite maximum target.
The all-size sharp family is additionally checked for $3\leq n\leq80$;
both extremal constructions are tested in both colours for $4\leq n\leq24$.
The optional vertex-zero check is expressly an extra finite pressure,
not a premise of Sections 2--4.

At $n=6$ there are 418 maximum-fibre targets: 158 star-certified,
260 face-certified, and none satisfying both. The measured depth layers
are 17,740, 13,620, 1,362, 46, summing to 32,768. These are finite
observations, not a new all-size census. No unresolved proof dependency
or required mathematical repair was found.
