# Proof package: metric reconstruction controls

Author: /root/round211_rational_scout/relation_primary_sources/lyndon_primary_check/pointer_e1_native_chain/p212_verifier_source.
2026-09-09 UTC. Author deductions, not independent review or candidate admission.

## Claim

Three precise controls are established: shortest-path RNG reconstruction is
the identity; diameter-two strong resolution has its known complement/twin
form; on labelled odd cycles strong resolution is exactly inverse to the old
degree-two shortcut. A separate connected-carrier counterexample and a
separator from old MEG delimit those claims.

## Status

**PROVABLE AS STATED** for the controls under the assumptions below.
**NOT CURRENTLY JUSTIFIED** for promoting any entrance to a fresh two-axis
paper, or for importing any all-graph eccentrication theorem from unread text.

## Assumptions and notation

Graphs are finite, simple, undirected and labelled. For fixed $n\ge1$, let
$\mathcal G_n^c$ be all connected graphs on $[n]$ with unit edge lengths.
$d_G$ is shortest-path distance; $N_G(u)$ and $N_G[u]$ are open and closed
neighborhoods. Complementation retains all labels and has no loops.

For a finite metric $d$ on $V$, define $R(d)$ by, for distinct $u,v$,
$$uv\in E(R(d))\quad\Longleftrightarrow\quad
d(u,v)\le\max\{d(u,x),d(v,x)\}\quad\text{for every }x\in V.$$
The weak inequality, including ties, is the source convention. Define
$T(G)=R(d_G)$ on $\mathcal G_n^c$.

For connected $G$, define $F(G)$ on the full label set by joining distinct
$u,v$ exactly when both conditions hold:
$$d_G(v,w)\le d_G(u,v)\quad(\forall w\in N_G(u)),\qquad
d_G(u,w)\le d_G(u,v)\quad(\forall w\in N_G(v)).$$
These are mutually maximally distant vertices. This is the source's
$G_{SR+I}$ convention, not its boundary-only $G_{SR}$ convention.

For an odd integer $q\ge3$ and an invertible residue $s\bmod q$, let
$C(q,s)$ have vertex set $\mathbb Z/q\mathbb Z$ and edges
$\{i,i+s\}$ for every $i$. Put $k=(q-1)/2$. Let $D$ be the old
degree-two neighbor-pair shortcut, restricted here to these cycles.

## Proof strategy and dependency map

1. RNG identity: positive integral distances retain edges; an internal
   shortest-path point excludes each nonedge. No external theorem needed.
2. Diameter-two formula: distance-two pairs are maximal; adjacent maximal
   pairs are exactly true twins. This rederives the read primary Proposition 14.
3. Odd cycles: identify the maximally distant positions, then calculate
   labelled step multiplication. The actual old proof supplies $D:s\mapsto2s$.
4. Scope checks: explicit $C_4$ and four-vertex paw calculations. No
   extrapolation from graph isomorphism or a pilot is used.

## Proof

### 1. RNG identity on the whole connected unit-graph carrier

Step 1. If $uv$ is an edge, $d_G(u,v)=1$. For $x=u$ or $x=v$ the maximum
in the definition is $1$. For any other $x$, both distances are positive
integers, so the maximum is at least $1$. Thus every edge is retained.

Step 2. If distinct $u,v$ are nonadjacent, set $m=d_G(u,v)\ge2$.
Take a shortest path $u=x_0,x_1,\ldots,x_m=v$ and choose $x=x_{m-1}$.
The shortest-path subpath property gives $d_G(u,x)=m-1$ and $d_G(v,x)=1$.
Both are less than $m$, so this $x$ violates the RNG inequality. No nonedge
is introduced. Hence $T(G)=G$.

Step 3. For $n=1$, there are no vertex pairs and the same equality holds.
Thus $T$ is an endomorphism of $\mathcal G_n^c$, every state is fixed,
and for every target $H\in\mathcal G_n^c$, $T^{-1}(H)=\{H\}$.
This is an identity control, not a temporal contribution. Arbitrary
real-valued metric spaces are not silently substituted as a finite carrier.

### 2. Diameter-two strong resolution: known exact formula

Assume $G$ is connected of diameter exactly two.

Step 1. A nonedge $uv$ has distance two. Every distance in the two maximality
tests is at most two, so $u,v$ are mutually maximally distant.

Step 2. If $uv$ is an edge, the maximality of $u$ from $v$ is equivalent to
$N_G(u)\subseteq N_G[v]$. Mutual maximality gives both corresponding
inclusions, and, since $u,v$ are adjacent, these are equivalent to
$N_G[u]=N_G[v]$. Conversely that equality makes both tests hold.

Step 3. True-twin equality partitions vertices into classes, and each
non-singleton class is a clique of $G$. Therefore
$$E(F(G))=E(\overline G)\ \cup
\{uv:u\ne v,\ N_G[u]=N_G[v]\}.$$
In particular, if $G$ is true-twin-free, $F(G)=\overline G$. This is the
full-label form of the primary source's Proposition 14; deleting its isolated
vertices gives that source's boundary-only version. It is not asserted that
all diameter-two inputs have diameter-two or connected outputs.

### 3. Exact inverse collision on labelled odd cycles

Step 1. Since $s$ is invertible, positions $i+js$ give cyclic order in
$C(q,s)$. Distances from position $0$ are $\min(j,q-j)$, whose maximum is
$k$. At either maximum position $k$ or $k+1$, each neighbor has distance at
most $k$. At a distinct nonmaximum position, one neighbor increases the
distance by one. Consequently two distinct vertices are mutually maximally
distant exactly when their cyclic separation is $k$.

Step 2. It follows as an equality of labelled edge sets that
$$F(C(q,s))=C(q,ks).$$
The integer $k$ is coprime to $q$, because any common divisor divides both
$q$ and $2k=q-1$. Hence the output remains in this restricted class.

Step 3. The two neighbors of $i$ at step $s$ are $i-s,i+s$, so their
neighbor-pair edge has step $2s$. This is exactly the old proof's
$D(C(q,s))=C(q,2s)$. Since $2k\equiv-1\pmod q$ and steps differing
by sign give the same undirected graph,
$$D(F(C(q,s)))=F(D(C(q,s)))=C(q,s).$$
Thus $F=D^{-1}$ on this labelled cyclic class. The equality does not claim
an inverse relationship for arbitrary graphs.

Step 4. Two invertible steps $a,b$ give the same labelled graph exactly when
$a\equiv\pm b\pmod q$: compare the two neighbors of label $0$.
Thus the exact period of $F$ is the least positive $t$ for which
$k^t\equiv\pm1\pmod q$. Since $(2k)^t\equiv(-1)^t\pmod q$, this
is equivalent to $2^t\equiv\pm1\pmod q$, namely the old signed order
$$\rho(q)=\min\{t\ge1:2^t\equiv\pm1\pmod q\}.$$
It is finite because $2$ is invertible modulo odd $q$. At $q=3$, $k=1$
and the triangle is fixed. All restricted states are recurrent and every
restricted target has exactly one preimage, its image under $D$.
No unrestricted preimage count follows from this calculation.

### 4. Carrier and collision boundaries

Step 1. In $C_4$, precisely the two opposite vertex pairs are mutually
maximally distant. An adjacent pair fails because the other neighbor of
one endpoint is distance two from the other endpoint. Therefore
$F(C_4)=2K_2$, which is disconnected. The connected-input definition of
$F$ is not an endomorphism of all $\mathcal G_n^c$. The source's general
notation allows infinite intercomponent distances, but no additional
disconnected-graph iteration convention is adopted or analyzed here.

Step 2. The old MEG control uses $d(u,v)=1$ on edges and $2$ on nonedges,
and requires mutual global farthestness. Its old formula is
$M(G)=\overline G\cup K_{U(G)}$, with $U(G)$ the universal set.
Take the paw on labels $p,q,b,c$ with edges $pq,pb,qb,bc$.
Its only universal vertex is $b$; $p,q$ are nonuniversal true twins.
Thus $E(M(G))=\{pc,qc\}$, while section 2 gives
$E(F(G))=\{pc,qc,pq\}$. This separates the literals even in diameter two.
The odd-cycle inverse collision, not a false all-graph identity with MEG,
is the decisive local subtraction.

## Corrections or missing assumptions

The connected unit-edge assumption is essential to the RNG argument as
stated. The full-label convention is essential to the strong-resolving
identity. The cycle period calculation requires invertible steps and odd
$q$. No formula is inferred merely from $F(C_q)\cong C_q$.

## Open risks

No all-graph temporal law or evaluated all-target fibre law for strong
resolution has been proved here. No theorem from the incompletely accessed
eccentrication sources is used. These limits prevent promotion; they are not
filled by bigger cutoffs, a monotonicity slogan or an independent-review claim.
