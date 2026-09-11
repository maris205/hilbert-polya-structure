# Proof package — a source-owned firefly comparison

Author and proof contributor: `/root/round211_finite_matching_scout`.
2026-09-09 UTC. Source-only negative scout; no manuscript number.

## Claim

For the published firefly cellular automaton on any fixed finite simple
graph, all one-step predecessors admit the constrained dominating-set
description below. Its largest target fibre is the number of dominating
sets of the underlying graph, with all maximizing targets characterized.
These are independently written deductions for a known comparison system,
not a newly nominated literal or a novelty claim.

## Status

`PROVABLE AS STATED` for the one-step decoder and extremum stated here.
`NOT CURRENTLY JUSTIFIED` for a new two-axis paper contract: no independent
residual all-parameter temporal/entrance theorem has been established.
Decision: `ZERO_NEW_LITERAL / NO_PROMOTION / HOLD_EXTERNAL`.

## Assumptions

- $G=(V,E)$ is a finite simple undirected graph, including the empty graph.
- $k\ge3$ is an integer; colours are $0,\ldots,k-1$ in this fixed order.
- All tests use the same old state, and the graph and $k$ stay fixed.
- A dominating set $D\subseteq V$ means every vertex outside $D$ has a
  neighbour in $D$; vertices in $D$ do not need a neighbour in $D$.
  The empty graph has one dominating set, namely the empty set.

## Notation

Put $b=\lfloor(k-1)/2\rfloor$ and $X=\{0,\ldots,k-1\}^V$.
The known FCA rule, identified in the primary body cited in
[SOURCES_AND_SUBTRACTION.md](SOURCES_AND_SUBTRACTION.md), is
$$
 F(x)_v=\begin{cases}
 x_v,&x_v>b\text{ and some }u\sim v\text{ has }x_u=b,\\
 x_v+1\pmod k,&\text{otherwise}.
 \end{cases} \tag{1}
$$
For $S\subseteq V$, let $N(S)=\bigcup_{s\in S}N(s)$ be its open
neighbourhood. The set $N(S)$ may intersect $S$; it is not $N(S)\setminus S$.
For a target $y$, set
$$C=C_y=\{v:y_v=b+1\},\qquad Z=Z_y=\{v:y_v=0\}.$$
Let $d(G)$ denote the number of dominating sets of $G$, and let
$I\subseteq V$ denote its isolated vertices.

## Proof strategy

Recover the old blinking set before recovering other colours. The one-step
trigger forces all remaining source coordinates, except that an old
blinking vertex can be chosen only among the target's $b+1$ vertices.
The admissibility constraints are domination inside that induced graph
and exclusion next to target zero. Extending an admissible set outside
$C$ injects the inverse fibre into the dominating sets of $G$.

## Dependency map

1. The disjoint target-colour cases of (1) give the exact decoder.
2. The decoder gives the fibre count by a bijection, not by experimentation.
3. A set-extension injection gives the fixed-graph upper bound.
4. Removing one nonisolated vertex gives strictness for every other target.
5. Isolated coordinates and the empty graph settle all boundary cases.
6. Elementary subset counting gives the complete-graph and star controls.

## Proof

### Step 1. Exact predecessor theorem

Define
$$
 \mathcal B_y=\{B\subseteq C:
 C\subseteq B\cup N(B),\quad N(B)\cap Z=\varnothing\}. \tag{2}
$$
Thus $B$ dominates the induced graph $G[C]$ and contains no vertex
adjacent to $Z$. For each $B\in\mathcal B_y$ define $x(B)$ as follows:
$$
 x(B)_v=\begin{cases}
 b,&v\in B,\\
 b+1,&v\in C\setminus B,\\
 y_v,&b+2\le y_v\le k-1\text{ and }v\in N(B),\\
 y_v-1,&b+2\le y_v\le k-1\text{ and }v\notin N(B),\\
 y_v-1,&1\le y_v\le b,\\
 k-1,&y_v=0.
 \end{cases} \tag{3}
$$
An empty colour interval in this display contributes no case. Then
$$F^{-1}(y)=\{x(B):B\in\mathcal B_y\},\qquad
|F^{-1}(y)|=|\mathcal B_y|, \tag{4}$$
and distinct admissible sets give distinct predecessors.

To prove necessity, take $F(x)=y$ and put $B=\{v:x_v=b\}$. Blinking
vertices always advance, so $B\subseteq C$. A target colour $b+1$ can
come only from old colour $b$ advancing or old colour $b+1$ holding.
Every vertex of $C\setminus B$ must therefore have an old blinking
neighbour. This gives $C\subseteq B\cup N(B)$.

A target zero can only come from old colour $k-1$ advancing, since zero
cannot hold under (1). Consequently it has no neighbour in $B$. This
gives $N(B)\cap Z=\varnothing$ and the last case of (3).
For $1\le y_v\le b$, holding cannot produce that colour, so the source
is $y_v-1$. For $b+2\le y_v\le k-1$, both possible old colours
$y_v$ and $y_v-1$ exceed $b$. If the vertex sees $B$, it must hold and
the old colour is $y_v$; if it does not, it must advance and the old
colour is $y_v-1$. These exhaust the colour cases and prove (3).

Conversely take $B\in\mathcal B_y$ and construct (3). Its vertices
of colour $b$ are exactly $B$: the low case has colour at most $b-1$,
the $C\setminus B$ case has colour $b+1$, the high cases have colour
at least $b+1$, and $k-1>b$. The vertices of $B$ advance to $b+1$.
Those of $C\setminus B$ hold because of (2). The two high cases hold
or advance according to whether they see this exact blinking set.
The low cases always advance. The zero-target cases see no blink by
(2), so advance from $k-1$ to zero. Hence $F(x(B))=y$ at every vertex.
Recovering $B$ as the set of old colour $b$ proves distinctness and (4).

This is a structural all-target recognition/counting formula. It does not
claim polynomial-time counting or a formula for higher-time fibres.

### Step 2. The fixed-graph sharp maximum

For every $G$ and $k\ge3$,
$$\max_{y\in X}|F^{-1}(y)|=d(G). \tag{5}$$
The maximizing targets are exactly
$$y_v=b+1\quad\text{for every }v\in V\setminus I, \tag{6}$$
with arbitrary colours at the isolated vertices.

For the upper bound send $B\in\mathcal B_y$ to
$$\Phi_y(B)=B\cup(V\setminus C).$$
A vertex outside this set lies in $C\setminus B$ and has a neighbour
in $B$ by (2). Thus $\Phi_y(B)$ dominates $G$. The map is injective
because $\Phi_y(B)\cap C=B$. This proves $|F^{-1}(y)|\le d(G)$.
For the constant target $y\equiv b+1$, we have $C=V$ and $Z=\varnothing$;
(2) is precisely the dominating-set definition, so equality holds.

Suppose (6) fails. Choose a nonisolated $v\notin C$. The set
$D=V\setminus\{v\}$ dominates $G$, since its only outside vertex $v$
has a neighbour. But every $\Phi_y(B)$ contains $v$, as $v\notin C$.
This dominating set is missing from the injection image. The finite
upper bound is therefore strict.

Now suppose (6) holds. The graph on $V\setminus I$ is independent of
the isolated coordinates in (1). On every isolated vertex the rule is
the permutation $x_v\mapsto x_v+1\pmod k$, giving one predecessor for
each target colour. On the nonisolated part the target is constant
$b+1$, so Step 1 gives exactly $d(G[V\setminus I])$ sources.
Every dominating set of $G$ contains all of $I$, and deletion of $I$
is a bijection to the dominating sets of $G[V\setminus I]$.
Thus the fibre has size $d(G)$, proving sufficiency and all equality cases.

If $G$ is edgeless, all coordinates are independent cyclic permutations:
every target has one predecessor, $d(G)=1$, and (6) is vacuous.
This includes the empty graph, whose carrier and fibre are singletons.

### Step 3. Evaluated extremal controls

Over all simple graphs with $n\ge2$ labelled vertices and all targets,
$$\max_{G,y}|F^{-1}(y)|=2^n-1, \tag{7}$$
with equality exactly for $G=K_n$ and $y\equiv b+1$.
Indeed, the empty set does not dominate a nonempty graph, so
$d(G)\le2^n-1$. Equality means every nonempty subset dominates, hence
every singleton dominates. For each vertex that requires adjacency to
every other vertex, so $G=K_n$. Conversely every nonempty subset of
$K_n$ dominates. Since $K_n$ has no isolates when $n\ge2$, Step 2
gives the target equality condition. At $n=1$ the maximum is one and
every target attains it; at $n=0$ the sole empty state does.

For a star with $d\ge1$ leaves,
$$d(K_{1,d})=2^d+1. \tag{8}$$
A dominating set containing the centre may choose any leaf subset,
giving $2^d$ possibilities. A dominating set omitting the centre must
contain every leaf, giving one more. In particular, on one edge and
$k=3$ the target $(2,2)$ has exactly the three predecessors
$(1,1),(1,2),(2,1)$.

These elementary domination facts are static support, not a separately
claimed new graph-counting theorem.

## Corrections or missing assumptions

No all-source temporal theorem is proved here. Finite determinism alone
only gives eventual periodicity and cannot fill that gap. No pilot was run.
Restricted known tree synchronization and published nonsynchronizing
examples are source deductions, not new first-axis progress.

The open-neighbourhood convention and $k\ge3$ are essential to the
printed decoder. The maximum-target characterization explicitly excludes
isolates from the forced-colour condition; omitting that qualification
would make the statement false even on an edgeless graph.

## Open risks

This proof has not received an independent manuscript review and establishes
no novelty or priority. It is a bounded feasibility control on a published
literal. Existing binary-mask, domination and graph-subset methods receive
zero primitive credit. No new temporal mechanism remains to pair with the
inverse calculation, so no candidate is admitted or reserved. Root reception
of this negative packet is separate from its author's decision.
