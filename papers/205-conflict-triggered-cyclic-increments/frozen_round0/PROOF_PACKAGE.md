# CCI: conflict-triggered cyclic increments

Author: `/root/batch197_fifth_scout`, 2026-09-05 UTC.
Status: **PROVABLE AS STATED / P205_ADMITTED_DRAFTING / HOLD_EXTERNAL**.
This paper-local copy preserves the original author's mathematical proof.
Root's lifecycle update records the completed independent candidate gate;
it is not an independent manuscript review. The original scouting package
remains unchanged. No new static graph-counting theorem receives credit.

## Claim and assumptions

Let $G=(V,E)$ be a finite simple undirected graph, $n=|V|$, and $q\ge3$.
The carrier is $X=(\mathbb Z/q\mathbb Z)^V$. All updates use the same old state:
$$F(x)_v=x_v+\mathbf1\{\exists u\sim v:x_u=x_v\}\pmod q.$$
An isolated vertex always holds. A conflict means equality on an edge, not
the presence of a successor colour as in the usual cyclic cellular automaton.

For $x\in X$, let $S(x)$ be the endpoints of its monochromatic edges.
Give each directed version $(u,v)$ of an edge the nonnegative weight
$$w_x(u,v)=(x_v-x_u)\bmod q\in\{0,\ldots,q-1\}.$$
Let $d_x(v)$ be the minimum total weight of a path from $S(x)$ to $v$, with
$d_x(v)=\infty$ if no such path exists. A path of length zero is allowed.

**Temporal theorem.** The first time at which $v$ has a conflict is exactly
$d_x(v)$. For every integer $t\ge0$,
$$F^t(x)_v=\begin{cases}
x_v+\max(0,t-d_x(v))\pmod q,&d_x(v)<\infty,\\
x_v,&d_x(v)=\infty.
\end{cases}$$
The entrance time is $h(x)=\max\{d_x(v):d_x(v)<\infty\}$, with the maximum
of the empty set defined as zero. On each connected component a recurrent
state is either a proper colouring, which holds, or a colouring in which
every vertex has a same-coloured neighbor, which advances globally by one.
Every nonfixed recurrent orbit has exact period $q$. Over all graphs with
$n$ vertices and all sources, the sharp maximum entrance time is
$$H_q(n)=\begin{cases}0,&0\le n\le2,\\(q-1)(n-2),&n\ge3.\end{cases}$$

For a target $y$, let $H_y$ be the spanning subgraph of its monochromatic
edges. Let $D_y$ have the directed arc $u\to v$ whenever $u\sim v$ and
$y_v=y_u+1\pmod q$. A subset $A\subseteq V$ is admissible if:

1. $A$ is a vertex cover of $H_y$;
2. every vertex of $A$ has a neighbor in $A$ in $H_y$;
3. $v\in A$ and $u\to v$ in $D_y$ imply $u\in A$.

In (2), $A=\varnothing$ is allowed. Thus the first two conditions specify
a classical 2-total vertex cover; isolated vertices of $H_y$ cannot be in $A$.
The third condition is predecessor closure, including its transitive consequences.

**Inverse and extremal theorem.** The sources of $y$ are exactly, once each,
$$x_v=y_v-\mathbf1_A(v)\pmod q\qquad(A\text{ admissible}).$$
In particular this is a complete target-resolved binary-mask decoder, not
an assertion that the count can be evaluated in polynomial time. The uniform
largest one-step fibre over all $n$-vertex graphs and targets is
$$M(n)=\begin{cases}
1,&0\le n\le2,\\4,&n=3,\\2^{n-1}-1,&n\ge4.
\end{cases}$$
For $n=3$, equality holds exactly for a triangle and a constant target.
For $n\ge4$, equality holds exactly for a labelled star $K_{1,n-1}$ and
a constant target. No every-time fibre count or complete basin enumerator
is claimed.

## Strategy and dependencies

Permanent conflicted edges give irreversible activation. The first meeting
of an active clock with a still stationary neighbour is a weighted arrival
event; shortest paths then describe all activation times. This is the
temporal representation. Independently, in a one-step inverse each coordinate
either held or advanced; old equality can occur only between two advancing
vertices. The resulting total-cover/order constraint reduces a global fibre
extremum to a small-path exclusion bound on independent sets.

Shortest-path methods, monotone activation, total vertex covers, independent
sets and elementary subset bounds are prior primitives and receive zero credit.
The source/value report must determine the remaining conjunction. A familiar
algorithmic vocabulary is not in itself a formula-level collision.

## Proof

### 1. Permanent conflicts and first activation

If $x_u=x_v$ on an edge, then both endpoints advance, so their next values
are again equal. Induction shows that this edge remains monochromatic
forever. Hence the active set, the endpoints of monochromatic edges, only
grows. Before its first conflict a vertex is stationary; after it, that
vertex advances at every step.

Let $\tau(v)$ be the first conflict time, or infinity if no conflict ever
occurs. The preceding observation gives the displayed iterate formula with
$\tau$ in place of $d_x$. All vertices of $S(x)$ have $\tau=0$.

Suppose a vertex $u$ has become active at time $s$, whereas its neighbor
$v$ has not yet become active. At time $s$ the old colour of $u$ is still
its initial colour $x_u$, and its subsequent colours are $x_u+t-s$.
Within the next $q-1$ steps it therefore meets the still stationary colour
$x_v$, at time $s+w_x(u,v)$. If $w_x(u,v)=0$, that edge was already
monochromatic initially and both vertices belong to $S(x)$. Thus the
zero-weight case introduces no spontaneous activation away from the seeds.
Even when $v$ was activated earlier by someone else, the inequality
$$\tau(v)\le\tau(u)+w_x(u,v)$$
still follows. Applying it along a seed path gives $\tau(v)\le d_x(v)$.

Conversely, if $\tau(v)=s>0$, a same-coloured neighbor $u$ at time $s$
must have $\tau(u)<s$. Two vertices with first conflict at $s>0$ were both
stationary before $s$; equality between them at $s$ would then be their
initial equality, contradicting $s>0$. Put $a=\tau(u)$. Since $v$ was
stationary on $[a,s]$, its first meeting with the advancing neighbour $u$
is exactly at $a+w_x(u,v)$; an earlier congruent meeting would already have
activated it. Therefore $s=a+w_x(u,v)$. Repeating this choice strictly
decreases first-conflict times until a seed is reached. The resulting
directed seed path has total weight $s$, so $d_x(v)\le\tau(v)$.
No activation can arise in an initially proper connected component.
Consequently $\tau=d_x$ at every vertex, including infinity.

### 2. Recurrence, exact entrance and the sharp global clock

Every vertex in a connected component containing a seed has finite distance
and eventually becomes active. At the last activation time all vertices of
that component have same-coloured neighbors; all advance thereafter and all
existing equalities persist. An initially proper component holds forever.
This proves that the state at time $h=\max d_x(v)<\infty$ is recurrent,
with componentwise action as claimed.

Before $h$, a seeded component with an as-yet inactive vertex has an active
set that will strictly increase at a later time. Such a state cannot lie
on a periodic orbit, because its active set is monotone. This proves exact
entrance, not merely eventual stabilization. Conversely, every state whose
components have the two stated forms is periodic immediately. If at least
one component advances, equality of a state with its $p$-step iterate forces
$p\equiv0\pmod q$ at any advancing vertex; hence its period is exactly $q$.

A seeded component has at least two seeds. A shortest path from the seed
set to a nonseed may be chosen simple and to contain no other seed after its
start. It uses at most $n-2$ edges, each of weight at most $q-1$. Thus
$h\le(q-1)(n-2)$ when a nonseed exists. At $n\le2$ no component can contain
both a seed edge and a nonseed, giving height zero.

For $n\ge3$, take the path $0-1-\cdots-(n-1)$ and set
$x_0=x_1=0$ and $x_i=-(i-1)\pmod q$ for $i\ge2$. The sole initially
monochromatic edge is $01$. Every forward edge after it has weight $q-1$,
and the unique simple route to the last vertex uses $n-2$ such edges.
Backtracking only adds a positive total weight. Hence its distance is
$(q-1)(n-2)$, proving sharpness for every $n,q$ in the claimed range.

### 3. Exact one-step binary-mask reconstruction

For any source $x$ of $y$, let $A$ be its set of advancing vertices. Then
$x=y-\mathbf1_A$, uniquely. Every monochromatic source edge has both
endpoints in $A$. When both endpoints are in $A$, source equality is
equivalent to target equality. When both are outside $A$, target equality
would contradict their holding. Finally, if $u\notin A$ and $v\in A$,
source equality is equivalent to $y_v=y_u+1\pmod q$. Such an edge is
forbidden because $u$ would have to advance.

It follows that $V\setminus A$ is independent in $H_y$, that each vertex
of $A$ needs an $H_y$ neighbor in $A$ to trigger its advance, and that no
arc $u\to v$ of $D_y$ may enter $A$ from outside. These are precisely the
three listed conditions. Conversely, those conditions ensure that the old
monochromatic edges in the reconstructed $x$ cover exactly $A$. All and
only its vertices advance, so its image is $y$. Distinct masks give distinct
sources since $q\ge3$.

### 4. The static total-cover extremum

For any simple graph $H$, write $T(H)$ for the number of vertex covers
$A$ such that $H[A]$ has no isolated vertex, allowing $A=\varnothing$.
Every isolated vertex of $H$ is forced outside $A$. Equivalently,
$I=V(H)\setminus A$ is independent and $H-I$ has no isolated vertex.
The decoder gives $|F^{-1}(y)|\le T(H_y)$; for a constant target the
predecessor arcs are absent and equality holds with $H_y=G$.

We prove the required bound on $T$ directly. If $H=K_{1,k-1}$ with
$k\ge3$, every admissible cover consists of the centre and a nonempty
subset of the leaves, so $T(H)=2^{k-1}-1$. For $K_2$, its unique admissible
cover is the full set, so $T(K_2)=1$. For connected graphs on three
vertices, $T(P_3)=3$ and $T(K_3)=4$.

Every connected nonstar graph on at least four vertices contains a
four-vertex path as a (not necessarily induced) subgraph. To justify this,
if a longest path has only three vertices $a,b,c$, every additional vertex
can be adjacent only to $b$: adjacency to $a$ or $c$ would extend the path.
Connectedness attaches all further vertices to $b$; an edge between two
such leaves, including $a$ and $c$, would again produce a four-vertex path.
Thus the graph would be a star, a contradiction.

Suppose now that a connected nonstar graph has $k\ge5$ vertices. Choose
one such path and, by connectedness, an edge from its vertex $u$ to a vertex
$v$ outside it. The four-vertex path has eight independent sets, and at
least two of them contain each chosen vertex $u$. If all other edges were
ignored, there would be $8\cdot2^{k-4}$ possible independent sets. The
additional edge forbids at least $2\cdot2^{k-5}$ of them, those containing
both $u$ and $v$. Therefore
$$T(H)\le i(H)\le7\cdot2^{k-4}<2^{k-1}-1,$$
where the strict inequality follows from $2^{k-4}\ge2$.

At four vertices the six connected unlabelled graphs are the star, path,
paw (a triangle with one pendant edge), four-cycle, diamond and complete
graph. Their respective $T$ values are $7,4,6,5,6,5$, obtained by listing
the independent complements. Thus the star alone attains seven. This
six-case enumeration is a finite boundary proof, not an extrapolation.

For disconnected $H$, $T(H)$ is the product of the counts of its components;
isolates contribute one. Each nontrivial component of size $k$ has
$T\le2^{k-1}$. If there are at least two nontrivial components and $n\ge4$,
the product is at most $2^{n-2}<2^{n-1}-1$. If there is just one nontrivial
component plus isolates, the strict bound follows from its smaller size,
including the $K_3$ value four. With no edges, $T(H)=1$.
Hence for $n\ge4$, $T(H)\le2^{n-1}-1$, with equality precisely when $H$
is a spanning star. The corresponding statement at $n=3$ singles out $K_3$.

### 5. Equality transfer back to the dynamical fibres

If a target attains the uniform extremum for $n\ge4$, then $H_y$ must be
a spanning star. As $H_y$ is connected and all its edges are monochromatic,
$y$ is constant on all vertices. Therefore $H_y=G$, so $G$ itself is a star.
Every constant target on a star has exactly its $T(G)=2^{n-1}-1$ sources.
The same argument at $n=3$ gives precisely a triangle and a constant target.
At $n\le2$, an edgeless graph has the identity map; on its sole possible
edge, unequal colours hold and equal colours advance together, a permutation.
Thus all fibres have size one in that range. This completes both the inverse
decoder and all equality cases of the sharp uniform extremum.

## Corrections, limitations and open risks

No known source is used without its indicated hypotheses. The proof does not
claim that CCI is ordinary CCA, Greenberg--Hastings, or a successful graph
colouring algorithm: it generally creates permanent conflicts. A generic
conflict-detection model does contain this literal update as one possible
local rule. The elementary total-cover extremal lemma is not asserted to
be a new general graph theorem without an independent source gate.

The inverse result concerns time one. The temporal formula handles all times
but does not itself enumerate their fibres. No claim of exactly solved
general 2-total-cover counting or efficient target recognition is made.
The independent candidate gate permitted the narrow P205 contract after
deducting the existing model, tools and total-cover object/complexity.
The temporal formula and target inverse/extremum survive within that
bounded audit; external originality remains uncertified. Manuscript A/B
reviews and all terminal evidence remain pending. The author of this
package and root as manuscript contributor may not review P205.
