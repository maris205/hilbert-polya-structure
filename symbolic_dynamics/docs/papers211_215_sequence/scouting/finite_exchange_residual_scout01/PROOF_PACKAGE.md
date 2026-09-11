# Retained-market top-choice exchange: negative-control proof package

Author and sole proof contributor: /root/round211_finite_matching_scout.
Date: 2026-09-09 UTC. SOURCE/PROOF ONLY; OWNER_AMBER / HOLD_EXTERNAL.
This is one desk literal, not an admitted paper or an independent review.

## Claim

For every positive integer $n$ and every fixed favorite map
$h:[n]\to[n]$, the retained-market exchange map $T_h$ defined below satisfies
$T_h^2=T_h$. Its fixed allocations are exactly those whose favorite-owner
graph has no directed cycle of length greater than one.

For a fixed allocation $\rho$, put
$S_\rho=\{i\in[n]:\rho(i)=h(i)\}$ and $s_\rho=|S_\rho|$.
For every integer $k\geq1$,

$$
|(T_h^k)^{-1}(\rho)|=s_\rho!.
$$

Every nonfixed target has zero positive-time predecessors. Let
$J=h([n])$, $d=|J|$, and $m_j=|h^{-1}(j)|$ for $j\in J$. Then the
maximum positive-time fibre is exactly $d!$, and the number of targets
attaining that maximum is exactly

$$
(n-d)!\prod_{j\in J}m_j.
$$

The complete temporal classification has only fixed recurrent states and
transient depth zero or one. This is a negative-control theorem, not a
qualifying temporal advance.

## Status

PROVABLE AS STATED for the displayed literal.
NO_PROMOTION / NO_RESERVE for the research candidate gate.

## Assumptions and notation

1. The agents and houses are separately labelled by $[n]=\{1,\ldots,n\}$,
   with $n\geq1$. The empty market is excluded rather than silently using an
   undefined favorite.
2. Each agent has a fixed strict preference order on all houses.
   Only its unique global favorite $h(i)$ is used. Equivalently, any fixed
   map $h:[n]\to[n]$ supplies all data needed for this theorem.
3. A state is a bijection $\pi:[n]\to[n]$ from agents to houses, so the
   carrier is the entire allocation set $S_n$. The labels of houses are
   not changed after a trade.
4. Define $f_\pi=\pi^{-1}\circ h$. Its directed graph has the unique edge
   $i\to f_\pi(i)$ at each agent. Let $C_\pi$ be the set of all vertices
   on directed cycles, including self-loops.
5. Simultaneously carry out every such cycle:

$$
T_h(\pi)(i)=
\begin{cases}
h(i),&i\in C_\pi,\\
\pi(i),&i\notin C_\pi.
\end{cases}
$$

All agents and houses remain present after every epoch. Favorites are never
restricted to a remaining submarket. There is no removal, priority phase,
exogenous scheduler, tie-breaking ambiguity, or preference feedback.
The conventional full TTC mechanism removes allocated cycle agents and
houses; its subsequent rounds are not the iterates of this literal.

## Proof strategy and dependency map

The argument uses only finite directed graphs and bijections.

1. A functional graph's cycle set is invariant under its successor
   permutation; this proves closure of the exchange on allocations.
2. Inside the old cycle set, new favorite-owner edges are self-loops.
   Outside it, edges either remain unchanged or are redirected into that
   set. This proves idempotence and identifies the entire new satisfied set.
3. A preimage is exactly an arbitrary permutation of the houses assigned
   to satisfied agents. This gives both directions of an inverse bijection.
4. Distinct satisfied agents have distinct favorite houses. Selecting one
   favorite-demanding agent per demanded house constructs and counts all
   largest-fibre targets.

No external theorem about core allocations, Pareto efficiency, random
markets, or full TTC inversion is invoked.

## Proof

### Step 1. Closure and preservation of the cycle-house set

Since $\pi$ is bijective, $f_\pi$ is a well-defined function on a nonempty
finite set. Starting at any vertex and repeatedly applying $f_\pi$ must
repeat a vertex; the segment between its first two appearances contains a
directed cycle. Hence $C_\pi$ is nonempty.

The restriction $f_\pi|_{C_\pi}$ is a permutation of $C_\pi$, being the
disjoint union of the successor permutations on its directed cycles.
For $i\in C_\pi$ one has $h(i)=\pi(f_\pi(i))$. Thus

$$
h(C_\pi)=\pi(C_\pi),
$$

and $h|_{C_\pi}$ is injective. In $T_h(\pi)$ the agents in $C_\pi$
receive exactly the old houses of $C_\pi$, once each. Agents outside it
retain the complementary set of houses. Therefore $T_h(\pi)$ is again
a bijection, so the displayed rule defines an autonomous map on $S_n$.

### Step 2. The new cycle set consists only of self-loops

Write $C=C_\pi$ and $\rho=T_h(\pi)$.
For every $i\in C$, $\rho(i)=h(i)$, so $f_\rho(i)=i$.

Take $i\notin C$. If $f_\pi(i)\notin C$, then the old owner of $h(i)$
lies outside $C$ and keeps that house. Consequently
$f_\rho(i)=f_\pi(i)$. If $f_\pi(i)\in C$, then
$h(i)\in\pi(C)=\rho(C)$, so $f_\rho(i)\in C$.
Thus every edge outside $C$ either stays unchanged or points into $C$.

A directed cycle of $f_\rho$ that meets $C$ must be the self-loop at its
first vertex in $C$. A directed cycle wholly outside $C$ would consist
entirely of unchanged edges and hence would already be an $f_\pi$ cycle,
contradicting the definition of $C$.
Therefore the only cycles of $f_\rho$ are the self-loops at $C$.

There are no additional satisfied vertices outside $C$: if
$\rho(i)=h(i)$ there, then $\pi(i)=h(i)$, and $f_\pi(i)=i$ would put
$i$ in $C$. We have proved the useful exact identity

$$
S_\rho=C_\pi.
$$

### Step 3. Fixed states and the full time law

If every cycle of $f_\pi$ is a self-loop, then every vertex selected
for exchange already owns its favorite, and the other vertices retain
their houses. Hence $T_h(\pi)=\pi$.

Conversely, suppose $f_\pi$ has a cycle of length greater than one.
Every vertex $i$ on that cycle satisfies $f_\pi(i)\ne i$, whence
$h(i)=\pi(f_\pi(i))\ne\pi(i)$. Its assignment changes, and
$T_h(\pi)\ne\pi$.
This establishes the fixed-state criterion.

Step 2 shows that $T_h(\pi)$ always satisfies that criterion. Hence
$T_h^2=T_h$, and

$$
T_h^k(\pi)=T_h(\pi)\qquad(k\geq1).
$$

Every recurrent state is fixed: a state on a positive-length orbit cycle
is an image, while every image is fixed. The transient depth is zero
for fixed states and one for nonfixed states. No period greater than one
occurs, for any $n$ or $h$.

### Step 4. Exact inverse parametrization

Fix a fixed target $\rho$, and write $S=S_\rho$.
The fixed-state criterion and existence of a functional-graph cycle imply
$S\ne\varnothing$. Since $\rho$ is injective and
$h(i)=\rho(i)$ on $S$, the favorites of agents in $S$ are distinct.

For every permutation $\sigma:S\to S$, define

$$
\pi_\sigma(i)=
\begin{cases}
\rho(\sigma(i)),&i\in S,\\
\rho(i),&i\notin S.
\end{cases}
$$

This is a bijection. For $i\in S$,
$f_{\pi_\sigma}(i)=\sigma^{-1}(i)$, so all vertices of $S$ lie on
$f_{\pi_\sigma}$ cycles.

For an agent outside $S$, a favorite-owner edge that stays outside $S$
is exactly its edge in $f_\rho$. An edge whose old endpoint lies in $S$
is merely redirected to another vertex of $S$.
The fixed-state criterion for $\rho$ says that $f_\rho$ has no cycle
wholly outside $S$. Therefore neither does $f_{\pi_\sigma}$.
Its cycle set is exactly $S$.
Executing its cycles restores each agent in $S$ to $h(i)=\rho(i)$
and leaves all other assignments unchanged. Thus
$T_h(\pi_\sigma)=\rho$.

For the converse, suppose $T_h(\pi)=\rho$.
The exact identity in Step 2 gives $C_\pi=S_\rho=S$.
The exchange changes no assignment outside $S$, so
$\pi(i)=\rho(i)$ there. Closure in Step 1 gives
$\pi(S)=\rho(S)$. Hence there is a unique permutation
$\sigma=\rho^{-1}\circ\pi|_S$ of $S$ such that
$\pi=\pi_\sigma$.

This proves a bijection between $T_h^{-1}(\rho)$ and the permutation
group of $S$. Its cardinality is $|S|!$.
Step 3 makes every positive iterate equal to $T_h$, giving the same
fibre for every $k\geq1$.
A nonfixed target is not an image at all, so its positive-time fibres
are empty.

### Step 5. Sharp maximum and all maximizing targets

For any fixed $\rho$, distinct members of $S_\rho$ receive distinct
houses $h(i)$. Thus

$$
1\leq |S_\rho|\leq d.
$$

Step 4 bounds each positive-time fibre by $d!$; nonfixed targets have
zero fibres.

To achieve the bound, choose, for each $j\in J$, one agent
$r_j\in h^{-1}(j)$. These chosen agents are all distinct because the
sets $h^{-1}(j)$ are disjoint. Assign $\rho(r_j)=j$.
Assign the $n-d$ houses outside $J$ bijectively to the remaining
$n-d$ agents in any order. Every chosen agent is satisfied.
Every remaining agent receives a house outside $J$, while its favorite
belongs to $J$, so it is not satisfied and its favorite-owner edge
points to a chosen satisfied agent.
The result is fixed with exactly $d$ satisfied agents, and its fibre
has size $d!$.

For $d\geq2$, the factorial is strictly increasing on the integers
from $1$ to $d$, so a target attains $d!$ exactly when it is fixed
and has $d$ satisfied agents. Such an allocation necessarily assigns
every house in $J$ to one of its demanders; these agents determine
the unique choices $r_j$ above. All other houses lie outside $J$
and may be assigned arbitrarily. There are therefore precisely

$$
\left(\prod_{j\in J}m_j\right)(n-d)!
$$

maximizers.

If $d=1$, every graph $f_\pi$ points all agents to the sole owner of
the one demanded house. It has only that self-loop, so every allocation
is fixed, with one satisfied agent and fibre size $1=1!$.
The same formula gives $m_j(n-1)!=n!$, exactly all allocations.
This also covers $n=1$. The theorem follows. $\square$

## Boundary checks and distinction from full TTC

If $d=n$, then $h$ is bijective and every $f_\pi$ is a permutation.
All agents are in cycles, so $T_h(\pi)=h$ for every $\pi$:
the unique target has fibre $n!$.
If $d=1$, the map is the identity, as proved above.
These are deductions for the same literal, not additional desk attempts.

The retained-market fixed states need not be Pareto optimal under the full
preference lists. As a hand-derived example, let $n=3$, let every agent's
global favorite be house $1$, and start at the identity allocation.
Give agent $2$ the order $1\succ3\succ2$ and agent $3$ the order
$1\succ2\succ3$; give agent $1$ any strict order with house $1$ first.
The map is the identity because $d=1$, yet agents $2$ and $3$ strictly
improve by exchanging their houses. Full TTC removes agent $1$ and house
$1$ before processing that later exchange.
Thus neither full-TTC Pareto theorems nor full-TTC inverse formulas may be
silently attributed to the retained-market map.

## Corrections or missing assumptions

None for the displayed theorem. Strict preferences may be replaced by the
weaker assumption that a single favorite $h(i)$ is fixed in advance, but no
state-dependent choice among tied favorites is included.

## Open risks and disposition

The all-parameter arguments above are authored desk proofs and have not had
an independent process-separated review or a scientific execution.
They establish no novelty or publication claim. The exact factorial inverse
and extremum do not repair the temporal axis: it is a one-step retraction of
a known trading-cycle primitive. Keep NO_PROMOTION / NO_RESERVE.
