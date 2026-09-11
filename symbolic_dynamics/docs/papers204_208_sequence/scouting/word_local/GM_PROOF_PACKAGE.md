# Proof Package — general-graph synchronous mex (GM)

Root mathematical contribution, 2026-09-05. **Candidate only; no paper ID.**

## Claim and status

**PROVABLE AS STATED** for the claims below. Candidate value, independent
proof audit, and primary-source subtraction remain pending. In particular,
the known multipartite map in P118 is the same literal local rule on a
restricted graph class; no new local rule is claimed.

Let $G=(V,E)$ be a finite simple undirected graph, with maximum degree
$\Delta$, $n=|V|$, and $s$ isolated vertices. Fix
$q\ge\max\{3,\Delta+1\}$ and write $[q]_0=\{0,\ldots,q-1\}$.
The autonomous map on $[q]_0^V$ is
$$F(c)(v)=\operatorname{mex}\{c(u):u\in N(v)\}.$$
All updates use the previous whole colouring. Put $c_t=F^t(c)$.

1. $c_{t+2}(v)\le c_t(v)$ for every $t\ge0$ and $v$.
   If $c_{t+2}(v)<c_t(v)$, then $c_t(v)\ge t+1$.
   Consequently $c_{t+2}(v)=c_t(v)$ whenever
   $t\ge\max\{1,\deg(v)\}$. Every recurrent period is one or two,
   and the global entrance time is at most $\max\{1,\Delta\}$.
2. For every $d\ge2$ there is a finite graph of maximum degree $d$
   and a colouring whose entrance time is exactly $d$.
   The degree-one bound is attained on one edge with palette size $q\ge3$.
3. Among all target colourings, the maximum one-step fibre is
   $q^s(q-1)^{n-s}$, attained uniquely at the all-zero target.
   This includes the empty graph and $n=0$.

## Assumptions and notation

The graph is undirected and has no loops; neither arbitrary directed graphs
nor scheduler-dependent updates are covered. A recurrent point is periodic.
Entrance time is the least $h\ge0$ with $F^{h+2}(c)=F^h(c)$ once the
period-one/two classification has been proved. The palette hypothesis
ensures closure, since a neighbourhood of size at most $\Delta$ has mex at
most $\Delta$. The $q\ge3$ condition is used in the uniqueness argument
for the inverse extremum, not in the temporal proof.

## Proof strategy and dependency map

The temporal proof uses an exclusion along an undirected edge, followed by
a backward chain of strictly decreasing colour values. Sharpness uses a
delayed signal on a labelled chain with permanently coloured clique
attachments. The inverse result instead bounds each source vertex's
allowed palette and treats the equality case.

1. Symmetric edge exclusion implies two-step coordinatewise descent.
2. A strict descent at time $t$ has a lower-colour strict-descent witness at
   time $t-1$; induction gives the local deadline.
3. Clique anchors stay fixed; a direct chain recurrence gives sharpness.
4. Forbidden palettes bound all target fibres; a missing-zero assignment
   makes the bound strict at every nonzero target.

No external theorem is needed for these deductions. That fact is not a
novelty assertion: static Grundy colouring and possible earlier synchronous
mex results must still be checked against primary sources.

## Proof

### 1. Two-step descent

Fix $v$, put $k=c_t(v)$, and let $u\in N(v)$. Undirectedness gives
$v\in N(u)$, so $c_{t+1}(u)\ne k$ by the definition of mex.
No neighbour of $v$ has colour $k$ at time $t+1$. Since $k$ is absent,
the least absent nonnegative colour is at most $k$, proving
$c_{t+2}(v)\le c_t(v)$.

### 2. A strict descent forces a high colour

We prove by induction on $t\ge0$ that strict descent implies
$c_t(v)\ge t+1$. At $t=0$, a nonnegative integer which strictly decreases
is at least one.

Suppose $t\ge1$ and let $l=c_{t+2}(v)<c_t(v)=k$. Because
$c_t(v)=\operatorname{mex}c_{t-1}(N(v))$ and $l<k$, some neighbour $u$
has $c_{t-1}(u)=l$. Because $l=c_{t+2}(v)$, no neighbour has colour $l$
at time $t+1$. In particular $c_{t+1}(u)\ne l$. Step 1 gives
$c_{t+1}(u)\le c_{t-1}(u)=l$, so this inequality is strict.
The induction hypothesis at time $t-1$ yields $l\ge t$, and hence
$k\ge l+1\ge t+1$.

For $t\ge1$, the local mex bound gives $c_t(v)\le\deg(v)$.
Thus strict descent is impossible when $t\ge\max\{1,\deg(v)\}$.
All coordinates are two-periodic from $\max\{1,\Delta\}$ onward.
A periodic trajectory with coordinatewise descent every two steps must
have equality in every such step, so its period divides two.

### 3. Sharpness at every maximum degree

For $d\ge2$, create chain vertices $v_1,\ldots,v_d$ with edges
$v_kv_{k+1}$, and two further vertices $u,w$ with edges $v_1u,uw$.
For every $k\in\{2,\ldots,d\}$ and every $j\in\{0,\ldots,k-2\}$,
take a separate clique $K_{j+1}$ whose vertices carry distinct labels
$0,\ldots,j$, and join its label-$j$ vertex to $v_k$.
All these cliques are pairwise disjoint and disjoint from the chain.
Initialize $c_0(v_k)=k$, $c_0(u)=c_0(w)=0$, and each clique vertex at its
label. The number of vertices is $d+2+\binom{d+1}{3}$.

The graph has maximum degree $d$: $v_d$ has degree $d$; for
$2\le k<d$, $v_k$ has degree $k+1\le d$; $v_1,u$ have degree two;
$w$ has degree one. An attached clique vertex has degree at most
$j+1\le d-1$.

The complete proposed orbit is as follows. Every clique vertex keeps its
label, and for $1\le k\le d$,
$$c_t(v_k)=k-\mathbf1\{t\ge k+1\text{ and }t\equiv k+1\pmod2\}.$$
Also $c_t(w)=t\bmod2$, while $c_t(u)=0$ at even times, equals two at
time one, and equals one at all odd times at least three. These formulas
hold initially. We verify all their updates together, which proves them
by induction on time.

An anchor joined to $v_k$ has label $j\le k-2$, and its additional
neighbour has colour at least $k-1>j$. Its clique supplies all lower
colours and none equal to its own label, so its update keeps that label.
At $v_k$, $k\ge2$, the anchors supply $0,\ldots,k-2$; its left neighbour
is in $\{k-2,k-1\}$ and its right neighbour, if any, is in
$\{k,k+1\}$. Thus
$$c_{t+1}(v_k)=
\begin{cases}k,&c_t(v_{k-1})=k-1,\\
k-1,&c_t(v_{k-1})=k-2.
\end{cases}$$
This is exactly the displayed formula with $t$ replaced by $t+1$.
At even times $u=0$ and $v_2=2$, so $v_1$ next takes one; at odd times
$u$ and $v_2$ are both nonzero, so $v_1$ next takes zero.
At time zero $u$ sees colours one and zero and next takes two; at
positive even times it sees two zeros and next takes one; at odd times
it sees two ones and next takes zero. Finally $w$ sees zero at even
times and a positive colour at odd times, giving its stated update.
This completes the simultaneous induction.

The first departure of $v_k$ from $k$ is at time $k+1$.
In particular $c_{d-1}(v_d)=d$ but $c_{d+1}(v_d)=d-1$.
The trajectory is not recurrent at time $d-1$. Step 2 puts it in the
recurrent set at time $d$, proving exact entrance time $d$.

For $d=1$, on a single edge start from $(0,2)$. One step gives $(0,1)$,
which is fixed, so the entrance time is one. For an edgeless nonempty
graph, every nonzero colouring enters the all-zero fixed point in one
step. The empty graph has one state and entrance time zero.

### 4. Unique maximal one-step fibre

Fix a target $y$. Any source $c$ with $F(c)=y$ must obey, at each source
vertex $u$,
$$c(u)\notin B_u(y):=\{y(v):v\in N(u)\}.$$
There are no forbidden colours at an isolated vertex and at least one at
every nonisolated vertex. Thus
$$|F^{-1}(y)|\le\prod_{u\in V}(q-|B_u(y)|)
\le q^s(q-1)^{n-s}.$$
The zero target attains equality: every nonisolated source vertex can
choose any nonzero colour, while each isolated source is unrestricted.

Suppose a target attains equality. Then every nonisolated $u$ has
$|B_u(y)|=1$; otherwise the second bound is strict. The first bound must
also be exact, meaning that every assignment avoiding these forbidden
singletons is a source. If $y(v)>0$ at some vertex $v$, this is impossible.
An isolated $v$ always has output zero. At nonisolated $v$, choose at each
neighbour $u$ a colour different both from zero and from its sole forbidden
colour. Such a choice exists since $q\ge3$. Extend arbitrarily within
the allowed palettes at the other vertices. This assignment avoids all
forbidden colours but places no zero in $N(v)$, so its output at $v$ is
zero, not $y(v)$. Thus the first bound is strict. Every maximizing target
must therefore be all zero.

## Corrections or missing assumptions

Do not omit undirectedness, or use the local deadline at time zero without
checking the initial palette. Do not claim uniqueness of the inverse
extremum for $q=2$: on a single edge the binary map is bijective.
The explicit construction does not claim the minimum possible number of
vertices for a sharp example.

## Open risks

The equations have not yet received an independent candidate audit.
Static Grundy colouring, symmetric-network period-two results,
and any existing degree-time theorem must be deducted. The sharp clock and
inverse extremum may still fail the project's value/duplication gate even
if both are correct. No all-graph image or exact depth distribution is
claimed.
