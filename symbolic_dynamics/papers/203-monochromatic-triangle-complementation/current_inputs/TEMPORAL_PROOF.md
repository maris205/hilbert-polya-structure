# MCT temporal proof pressure

## Claim and status

For each $n\ge0$, take the full set of simple labelled graphs on
$\{0,\ldots,n-1\}$. View absent/present edges as colours $0,1$.
Choose the lexicographically least three-vertex set whose three edges
have one colour and complement its three edges. If there is no such set,
hold. Write this map as $F$ and its maximum entrance time as $H(n)$.

**PROVABLE AS STATED:** $H(n)=0$ for $n\le3$ and $H(n)=n-3$ for
$n\ge3$. Every moving recurrent orbit is a two-cycle. Before entering
one, each strict selector change introduces a vertex that has never
appeared in the selected triangles before. Full proofs follow.

This is independent temporal proof pressure, not a Stage1 promotion,
paper number or manuscript review. Generic minimum-involution scheduling
is old background. The new proof being tested is the no-return mechanism
and sharp construction. A separate inverse/source gate remains necessary.

## Assumptions and notation

Triangle order is the lexicographic order of increasing vertex triples.
$T_t$ is the selected triangle at state $G_t=F^t(G_0)$, with colour $c_t$.
A strict transition means $T_{t+1}<T_t$. Vertex and edge labels stay fixed.
In a fixed-anchor trace, $s_i$ will denote the initial colour of the edge
from the anchor to its $i$th sequence vertex. All colour addition is mod two.

## Strategy and dependency map

1. The generic selector argument gives only fixed/two-cycle recurrence.
2. A two-step obstruction forbids repeated shared edges and later drops
   of the selected minimum.
3. A fixed anchor turns triangles into sliding vertex pairs. Same-parity
   decrease and colour parity exclude every repeated vertex.
4. A separate initial-minimum-drop argument excludes the one vertex not
   covered by that fixed-anchor trace.
5. A uniformly specified graph realizes $n-3$ strict changes for every n.

## Proof

### Step 1. Strict changes and exact entrance convention

Flipping a monochromatic triangle leaves it monochromatic, in the opposite
colour. The next selector is therefore at most the current one. Equality
means that the next flip reverses the previous flip, producing a two-cycle.
On a strict change, a newly selected triangle was not monochromatic before
the flip. It must share an edge with the flipped triangle, so it has exactly
two of its vertices. Its third vertex is smaller than the removed vertex,
because the common pair is fixed and its triple is lexicographically earlier.
Its shared edge has the new colour, so $c_{t+1}=1-c_t$.

The finite ordered selector cannot descend forever. Every moving orbit
therefore enters a two-cycle; it cannot enter a fixed point because the
last flipped triangle remains monochromatic. The recurrent moving states
are exactly those whose triangle is selected at both endpoints of its flip.
The entrance time is exactly the number of strict changes before the first
equal selector: distinct triangle masks cannot cancel in two consecutive
flips. This paragraph is generic prior scheduling, not novelty credit.

### Step 2. Two local obstructions

Two consecutive strict changes cannot use the same shared edge. Otherwise
write the three selectors as $abc$, $abd$, $abe$. Their colours are
$q,1-q,q$. The edges $ae,be$ were untouched by the first two flips, and
the edge $ab$ returns to its original colour q. Thus $abe$ was already
monochromatic before $abc$ and is lexicographically earlier, a contradiction.

The minimum vertex cannot drop after the first strict change. Suppose
$T_0=abc$, $T_1=dab$, and the minimum drops in $T_2$. By the previous
paragraph $T_2$ cannot use the shared edge $ab$ again. Relabel the common
vertices so that $T_2=eda$, where $e<\min T_1$. The first replacement
has $d<c$, so e is also smaller than every vertex of $T_0$.
Let the colour of $T_0$ be q. The edge $ea$ is untouched and must have
colour q for $T_2$. Since $T_0$ is initially least and e is smaller than
all its vertices, triangles $eab,eac$ force $eb=ec=1-q$. After flipping
$T_0$, the triangle $ebc$ is monochromatic in colour $1-q$, and it is
earlier than $T_1$ because $e<\min T_1$. This contradiction applies at
every consecutive pair of strict changes. Consequently all selectors
from $T_1$ onward have one common least vertex.

### Step 3. No return when a common anchor is present

Consider any entire strict trace with a common least vertex a. Write

$$T_t=\{a,v_t,v_{t+1}\}.$$

This sliding representation is obtained by orienting the first pair
according to the first removal. At the next change the retained non-anchor
vertex must be removed on the following change: otherwise the shared edge
would repeat, contradicting Step2. Each incoming vertex satisfies
$v_{t+2}<v_t$. Thus the even-index and odd-index subsequences are strictly
decreasing.

Suppose a first repeated sequence vertex occurs, $v_i=v_j$ with $j>i$.
Its two indices must have opposite parity, since same-parity terms strictly
decrease. For $i\ge1$, before leaving the selected pair the vertex has
appeared in triangles $T_{i-1},T_i$. Its anchor edge is flipped twice,
so while absent it retains its colour $c_{i-1}$ at first entry. Re-entry
at $T_{j-1}$ requires colour $c_{j-1}$, which is opposite because $j-i$
is odd. This is impossible. For $i=0$, its single initial flip leaves
anchor-edge colour $1-c_0$; the odd index j requires $c_{j-1}=c_0$,
again impossible. No selected vertex returns. A trace with no strict
change needs no sliding argument.

### Step 4. The initially retired vertex when the minimum drops

The only case not covered by Step3 for the whole trace is
$T_0=\{r,u,v\}$, $T_1=\{a,u,v\}$ with $a<\min T_0$. Let
$T_0$ have colour q and put $\gamma=1-q$. In $G_1$, the edges
$au,av,uv,ru,rv$ all have colour $\gamma$. The edge ar is unchanged.

Initially there was no monochromatic triangle containing a, since every
such triangle precedes $T_0$. Therefore every initial a-colour class k
induces only edges of colour $1-k$.

If $ar=\gamma$, then triangles $aru,arv$ are monochromatic in $G_1$.
For $T_1$ to be least, r must exceed both u and v. The two decreasing
subsequences of Step3 can never introduce such a vertex, so r cannot return.

It remains that $ar=q$. Apply Step3 to the trace beginning at $G_1$,
orienting its initial pair as $v_0=u,v_1=v$; swapping u and v is harmless.
Suppose r first enters this trace at relative time k. Its anchor edge is
unchanged and equals q, so k is odd. Thus r is the new even-position
vertex $v_{k+1}$ and its partner $w=v_k$ is in the odd subsequence,
with $w\le v$. If $w\in\{u,v\}$, its edge to r has colour $\gamma$
after the first flip and cannot form a q triangle. Otherwise $w<v$ and
its initial anchor colour is $\gamma$, as follows from first-entry colour
$\gamma+(k-1)=\gamma$. Hence $wu=wv=q$ in $G_0$, because u,v,w lie
in that initial a-colour class. If $rw=q$, the triangle $ruw$ was also
monochromatic in $G_0$, and replaces v in $T_0$ by the smaller w. It
would precede $T_0$, a contradiction. Thus $rw=\gamma$ and this edge
is never changed while r is absent. It again prevents r from entering a
q triangle. This proves that the initially retired vertex cannot return.

Combining Steps3--4, every strict selector change adds a previously unseen
vertex. The initial triangle uses three vertices, so there are at most
$n-3$ strict changes. Thus $H(n)\le n-3$ for $n\ge3$.

### Step 5. Uniform sharp construction

Fix $n\ge3$, put $N=n-1$, choose anchor $a=0$, and let
$v_i=n-1-i$ for $0\le i<N$. Set the initial anchor-edge colours to
$s_0=s_1=0$ and $s_i=(i-1)\bmod2$ for $i\ge2$.
For $i<j$, give edge $v_iv_j$ colour

$$b_{ij}=\begin{cases}
i\bmod2,&j=i+1,\\
1-s_i,&j>i+1\text{ and }s_i=s_j,\\
s_i,&j>i+1\text{ and }s_i\ne s_j.
\end{cases}$$

In particular $b_{01}=0$. These formulas specify every edge of one graph,
without a search or implicit choice. Its selected triangles are exactly

$$T_t=\{0,v_t,v_{t+1}\},\qquad c_t=t\bmod2,
\qquad 0\le t\le n-3.$$

Here is the induction. Initially the only monochromatic triangle containing
0 is $0v_0v_1$: every other pair with equal anchor-edge colours has the
opposite pair-edge colour. Hence $T_0$ is least. Assume the printed trace
through $T_{t-1}$. At state t, for $t\ge1$, $v_t$ is the carry vertex,
whose anchor edge has been flipped once; vertices $v_i$ with $1\le i<t$
are retired and their anchor edges have been flipped twice, restoring
$s_i$. The exceptional retired vertex $v_0$ has colour one. Future vertices
retain their initial colours.

No pair avoiding the carry and consisting of two future vertices can
be eligible. Nor can a retired/future pair be eligible: their edge is
unchanged, same initial anchor classes have opposite pair-edge colour,
and the exceptional $v_0$ has edges of colour zero to every future
vertex of anchor colour one. Retired/retired eligible pairs have both
labels larger than the carry and the next future vertex, so are later.

The future vertices matching the carry's current colour have indices
$j=t+1,t+3,\ldots$. The consecutive edge has colour $t\bmod2$ and is
eligible. For $j\ge t+3$, the initial anchor colours of $v_t,v_j$ differ
and their edge has colour $s_t=1-(t\bmod2)$, so they are ineligible.
Every eligible carry/retired pair is later than the carry/next-future pair
because a retired vertex has a larger label. Non-anchor triangles also
come later. Therefore the least triangle is exactly $T_t$, completing
the induction. The final one is $\{0,1,2\}$; after its flip it remains
the first possible triple and is selected again. The source tail is exactly
$n-3$.

For $n=0,1,2$ no triangle exists, so every graph is fixed. At $n=3$ only
one triangle can be selected and every moving state is already in its
two-cycle. Thus $H(n)=0$ for $n\le3$, with the same formula at n=3.

## Corrections, ownership and open risks

The conjectured sharp temporal statement survives without changing the
carrier. The earlier coarse sum-label bound is not used as the sharp proof.
No general statement that a lex-decreasing sequence cannot revisit vertices
is asserted; Step4 and the colour bookkeeping are essential.

The author scout independently challenged the initial-retired argument and
independently obtained the same sharp construction. That helpful check is
not a second manuscript review or a substitute for a frozen independent
gate. This package proves only the temporal pressure task. Its generic
scheduler core is already present in old Q01/LFCTR, while exact MCT
ownership and the separate inverse/equality package still need joint
adjudication. No promotion, number, global novelty or external release is
authorized here.
