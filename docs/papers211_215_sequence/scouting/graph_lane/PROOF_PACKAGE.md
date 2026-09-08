# Proof package — four graph literals, no admission

Author: `/root/round211_graph_scout`, 2026-09-08 UTC. Definitions are fixed
in INTAKE.md. Every argument here is author-side; no reviewer independence
is claimed. The scientific pilot covers CBF only.

## Claims, statuses and dependencies

| Literal | Mathematical status | Dependencies and value boundary |
|---|---|---|
| CBF | PROVABLE AS STATED: complete recurrence, sharp global height, full structural fibres/image and unique maximal target | Bridge forest; complement-of-forest classification; bridge-component reconstruction. The first-image clock is a short sparse/dense machine and the inverse is classical bridge decomposition. |
| ZFW | PROVABLE AS STATED: complete recurrent matching-cut criterion, height at most $n$, fixed Boolean-erosion adapter, two global fibre extrema on connected graphs | The one-white-neighbor predicate, reciprocal forcing pairs and two alternating AND maps. No sharp global height claimed. |
| MCS | NOT CURRENTLY JUSTIFIED as a two-axis contract | Switching-class confinement and a generic inverse-candidate test are proved; no full temporal theorem or evaluated inverse extremum. |
| CII | PROVABLE AS STATED: exact image and sharp two-step core bound; NOT CURRENTLY JUSTIFIED as a residual two-axis contract | Implicit-color identities, equivalence graphs and independent color permutation. The whole time axis is a canonical partition-kernel collapse. |

## 1. CBF: assumptions and notation

Let $G$ be a simple graph on $[n]=\{0,\ldots,n-1\}$. Write $B(G)$ for its
spanning bridge subgraph and $F(G)=\overline{B(G)}$, where complement is in
$K_n$. A bridge increases the number of components upon deletion; no
connectivity of $G$ is assumed. The empty graph is $E_n$. The entrance time
$\mu(G)$ is the least nonnegative time on the eventual cycle.

### 1.1 The bridge-forest image

Every bridge set is a forest: an edge on a cycle has an alternative path
between its endpoints and is not a bridge. Conversely, all edges of a forest
are bridges. Therefore

$$\operatorname{im}F=\{\overline D:D\text{ is a forest on }[n]\}.$$

This is a characterization, not a new formula for the number of forests.

### 1.2 Complement-of-forest lemma

For $n\ge5$ and every forest $D$, $B(\overline D)$ has at most one edge.

First suppose $C=\overline D$ is disconnected. If two components each had at
least two vertices, the complete bipartite graph between them in $D$ would
contain a cycle. If $C$ had three components, picking one vertex from each
would give a triangle in $D$. Thus there are exactly two components, one a
singleton $x$. All $n-1$ edges from $x$ are in $D$, so they exhaust the
possible edges of the forest. Hence $C=K_{n-1}\sqcup K_1$, which has no
bridge for $n\ge4$.

Now suppose $C$ is connected and $xy$ is a bridge. Deleting it partitions
the vertices into nonempty sets $A,B$, and $D$ contains every cross pair
except $xy$. If both sides have size at least two, the larger side has size
at least three. Choose two vertices of that larger side avoiding the
endpoint of the missing pair and two vertices of the other side. All four
cross edges form a cycle in $D$, a contradiction. Consequently every bridge
of $C$ is pendant. Its leaf has degree $n-2$ in $D$. Two different such
leaves would require at least $2(n-2)-1=2n-5>n-1$ edges in the forest.
There is therefore at most one pendant bridge. This proves the lemma.

### 1.3 Complete recurrent core and sharp height

For $n\ge5$, the lemma gives

$$F^2(G)\in\{K_n\}\cup\{K_n-e:e\in E(K_n)\},\qquad F^3(G)=K_n.$$

Every edge of $K_n-e$ lies on a triangle for $n\ge4$, so that graph has no
bridge. Also $K_n$ has no bridge for $n\ge3$. It follows that $K_n$ is the
unique recurrent state for $n\ge5$. More precisely,

$$\mu(G)=\begin{cases}
0,&G=K_n,\\
1,&G\ne K_n,\ B(G)=\varnothing,\\
2,&B(G)\ne\varnothing,\ B(F(G))=\varnothing,\\
3,&B(F(G))\ne\varnothing.
\end{cases}$$

These cases are disjoint: a nonempty bridge set makes $F(G)\ne K_n$, and a
nonempty bridge set of $F(G)$ makes $F^2(G)\ne K_n$.

The small orders are determined without extrapolation. At $n=0,1$ the sole
graph is fixed. At $n=2$ the two graphs are interchanged. At $n=3$, $K_3$
is fixed, $E_3$ enters it in one step, and each single edge is interchanged
with its complementary two-edge path (three two-cycles). At $n=4$ the
unlabelled forest shapes are $E_4$, one edge, two disjoint edges,
$P_3\sqcup K_1$, $K_{1,3}$ and $P_4$. Their complements have respectively
zero, zero, zero, one, zero and three bridges. The complement of $P_4$ is
another $P_4$. If $B(G)$ is a spanning $P_4$, then $G=P_4$: an additional
edge would close a cycle and destroy one of those bridges. Thus the
recurrent graphs are precisely $K_4$ and the twelve labelled $P_4$ graphs,
the latter forming six complement pairs. Every other graph enters $K_4$
within three steps.

For every $n\ge4$, take $G$ to be the star with $n-2$ leaves together with
one isolated vertex $y$. Its complement has one pendant bridge, from the
old star center to $y$. The next graph is $K_n$ minus that edge, and only
the third image is $K_n$. Hence

$$\max_G\mu(G)=\begin{cases}0,&n\le2,\\1,&n=3,\\3,&n\ge4.\end{cases}$$

### 1.4 Full structural inverse and its extremum

Let $b_k$ count connected bridgeless labelled simple graphs on a specified
$k$-element set; $b_1=1$ and $b_2=0$. For a target $H$, put $D=\overline H$.
If $D$ is not a forest, its fibre is empty. Otherwise let $\Pi(D)$ be the
partitions $\pi$ of $[n]$ such that contracting every block in the prescribed
edge set $D$ creates a loopless forest with no parallel edges. Then

$$|F^{-1}(H)|=\sum_{\pi\in\Pi(D)}\prod_{C\in\pi}b_{|C|}.$$

For $n=0$, the empty partition contributes the empty product $1$.
The formula is a bijection. Given a predecessor $G$, remove all of its
bridges $D$. The remaining components are connected and bridgeless: every
remaining edge lies on a cycle and a cycle contains no removed bridge.
Their vertex blocks give $\pi$. Contracting these blocks leaves exactly the
bridges, so the quotient is a forest. Conversely choose such a partition
and choose a connected bridgeless graph independently inside each block.
Adjoin precisely the prescribed edges of $D$. The forest quotient makes
each such edge a bridge, while the chosen internal edges remain on cycles.
These two constructions are inverse, proving the complete fibre law.

For a fixed nonempty forest $D$, deletion of $D$ injects its fibre into the
class of all bridgeless graphs on $[n]$. The complete graph is not in this
injection's image, since all edges in $D$ are absent after deletion. For
$n\ge3$, $K_n$ itself is bridgeless. Thus $H=K_n$ is the unique maximum
fibre target, with value equal to the number of all labelled bridgeless
graphs. At $n=2$ both fibres have value $1$; at $n=0,1$ the single fibre is
$1$. The static bridge decomposition, forest count and named $b_k$ counts
receive no independent novelty credit.

## 2. ZFW: full recurrent criterion and erosion subtraction

Write $W(S)$ for the frontier on a fixed graph $G$. Then
$W(S)\cap S=\varnothing$. If $v\in W(S)$, some $u\in S$ satisfies
$N(u)\setminus S=\{v\}$. If this $v$ forces $w$ on the next step, its
unique neighbor outside $W(S)$ must be $u$, since $u\notin W(S)$. Therefore
$w=u\in S$ and

$$W^2(S)\subseteq S.$$

The even and odd subsequences consequently decrease. Every orbit ends in
period one or two; the empty subset is the only fixed subset. A nonempty
recurrent pair $S\leftrightarrow T$ has the following exact description:
$S\cap T=\varnothing$, their union is a union of connected components of
$G$, and the cross edges between $S$ and $T$ are a perfect matching.

To prove necessity, take $u\in W^2(S)=S$ and a forcing witness $v\in T$.
Since $v\in W(S)$ it had some witness $u'\in S$. The condition
$N(v)\setminus T=\{u\}$ forces $u'=u$. Thus
$N(u)\setminus S=\{v\}$ and $N(v)\setminus T=\{u\}$. The same argument
starting from $T$ covers every vertex on both sides, and uniqueness gives a
perfect matching. The two neighborhood conditions forbid edges from
$S\cup T$ to the outside. Conversely these conditions force every matched
partner and no other vertex, giving the asserted two-cycle.

If the entrance time is $\mu$, then for each $0\le t<\mu$ the inclusion
$W^{t+2}(S)\subset W^t(S)$ is strict. Summing the size losses gives

$$\mu\le |S|+|W(S)|-|W^\mu(S)|-|W^{\mu+1}(S)|\le n.$$

For a nonempty eventual two-cycle the last bound improves to $n-2$.
Neither bound is claimed sharp.

### 2.1 Exact fixed-dependency erosion adapter

Set $A=S$, $B=W(S)$ and define reciprocal pairs by

$$u\in A,\ v\in B,\quad N(u)\setminus A=\{v\},\quad
N(v)\setminus B=\{u\}.$$

They form a matching with endpoint sets $U\subseteq A$, $V\subseteq B$
and bijection $p:U\to V$. The preceding witness proof gives $W^2(S)=U$.
For every $C\subseteq U$ and $D\subseteq V$ one has exactly

$$W(C)=\{p(u):u\in C,\ N(u)\cap A\subseteq C\},$$
$$W(D)=\{p^{-1}(v):v\in D,\ N(v)\cap B\subseteq D\}.$$

Indeed, each $u\in C$ already has the white neighbor $p(u)$; it forces
exactly when none of its old internal $A$ neighbors has been lost. The
second equation follows by the same explicit argument with the displayed
reciprocal neighborhood condition for $v$.

Identify $V$ with $U$ via $p$. The first equation is a coordinatewise AND
of the current bit and the bits of a fixed list of $A$ neighbors. A neighbor
in $A\setminus U$ contributes a permanent zero. The second equation is
another fixed AND map, with permanent zeros from $B\setminus V$.
Complementing bits turns them into two alternating OR-propagation maps.
Their two-step composition is a single fixed Boolean-relation propagation
map with constant seeds. Thus, after the two-step reciprocal-pair intake,
the entire temporal mechanism is ordinary fixed-graph erosion/reachability,
not a new nonlinear forcing clock. This exact reduction, not a title match,
is the decisive temporal subtraction.

### 2.2 Two global inverse extrema on connected graphs

Fix $n\ge2$ and allow every connected graph on $[n]$. The maximal empty
target fibre is $2^n-n$, attained uniquely by $K_n$. For each vertex $v$,
$S=[n]\setminus\{v\}$ has frontier $\{v\}$, since connectedness provides
a neighbor of $v$. These $n$ distinct sources cannot lie over the empty
target, proving the upper bound. In $K_n$ all other subsets have empty
frontier, so equality holds. If a connected graph is not complete, choose
a vertex $u$ with $1\le d(u)\le n-2$ and a neighbor $v$. Let

$$S=\{u\}\cup(N(u)\setminus\{v\}).$$

Then $u$ forces $v$, and $|S|=d(u)\le n-2$. This is an extra nonempty
frontier source, beyond the $n$ complements of singletons; equality fails.

The maximum over nonempty targets is $2^{n-1}-1$. If $W(S)=T\ne\varnothing$,
then $S$ is a nonempty subset of $[n]\setminus T$, giving at most
$2^{n-|T|}-1$ possibilities. A star with target its center attains
$2^{n-1}-1$, since every nonempty leaf subset has that frontier. Equality
forces $T=\{v\}$ and every singleton $\{u\}$ with $u\ne v$ to force $v$.
Hence every such $u$ has exactly the neighbor $v$, which characterizes the
star and its center. For $n=2$ either vertex is a center. The case $n=1$
is excluded: the only graph sends both subsets to empty, with fibre $2$.

These are complete global extrema, not a full target-by-target counting
formula. They do not restore contribution value after the exact erosion
reduction. No ZFW scientific execution occurred.

## 3. MCS: exact adapter and unclosed claims

For a subset $S$, let $G^S=G\mathbin\triangle\delta(S)$. The literal
selector chooses the minimum pair stated in INTAKE.md. Switching satisfies
$(G^S)^T=G^{S\triangle T}$, and $G^S=G^T$ exactly when
$S\triangle T$ is empty or all of $[n]$. Thus every orbit is confined to
one switching class of $2^{n-1}$ labelled graphs. Every triangle keeps the
parity of its number of edges, since a cut toggles zero or two of its pairs.
This is the classical cut-space action already used as zero-credit setup
in P145, specialized to the complete ambient pair set.

For a target $H$, every predecessor is exactly a graph $H^S$ whose own
selected minimum cut is $S$. This is a bounded inverse-candidate test, not
an evaluated fibre theorem. Neither a full temporal classification nor an
independent inverse extremum has been proved. The energy change under a
switch is $|S|(n-|S|)-2|E_G(S,\bar S)|$; minimizing the second term alone
does not fix its sign because cut sizes vary. No unjustified Lyapunov claim
is made. No pilot or recommendation.

## 4. CII: exact partition image and two-step clock

Forced equality in every optimal coloring is an equivalence relation, so
the output is a disjoint union of cliques. Every such clique partition is
realized: use the complete multipartite graph whose parts are its blocks.
Choosing one representative from each part gives a clique, so an optimal
coloring uses distinct colors on the parts and only one color per part.
Consequently the image is exactly all cluster graphs, with Bell-number
cardinality; this is static encoding, not a novel census.

For $n\ge2$, $E_n$ maps to $K_n$ and $K_n$ maps to $E_n$. Any nonempty
cluster graph has no pair forced to share a color: pairs in one clique
must differ, and for pairs in different components an independent
permutation of the at least two colors makes them differ. Thus its image
is empty. Every state enters the single $E_n\leftrightarrow K_n$ cycle
within two steps. At $n\ge3$, $P_3$ with isolates has an implicit-identity
edge between the path endpoints, hence a proper nonempty cluster first
image and entrance time two. At $n=2$ both states are already recurrent;
at $n=0,1$ the only graph is fixed. The sharp heights are therefore zero
for $n\le2$ and two for $n\ge3$.

The primitive is exactly chromatic implicit identity, not just a nearby
paper title. Full arbitrary-target inverse counts remain unproved, and a
canonical equivalence extraction followed by this two-state machine has no
eligible temporal residual. No pilot or recommendation.

## Final proof risks and disposition

CBF and ZFW contain valid all-parameter author deductions; neither is
claimed globally novel. CBF's inverse and ZFW's temporal evolution have
explicit owned-mechanism adapters. MCS lacks the required proofs. CII is a
canonical identity-kernel collapse. These four proposals do not supply an
admission recommendation. Value adjudication is not an independent review;
root may inspect the original arguments, but no seat is filled here.
