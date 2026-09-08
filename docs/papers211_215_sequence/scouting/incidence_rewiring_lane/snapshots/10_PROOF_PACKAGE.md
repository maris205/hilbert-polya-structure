# ONI: proved boundary, not a two-axis admission

Author: thirty_first_finite_scout. The proofs below are author deductions;
no independent candidate or manuscript review is claimed.

## Claim, assumptions and status

Let $F$ be the literal map of INTAKE.md on all simple graphs on $[n]$,
$n\ge0$. We prove edge inflation, complete fixed/recurrent classification,
the generic finite edge-count entrance bound, exact isolated-set
preservation, and the complete inverse of every complete bipartite target
with any specified isolated vertices. These stated boundary claims are
**PROVABLE AS STATED**. A new nontransferable structural temporal theorem,
an all-target inverse or a global fibre maximum are **NOT CURRENTLY
JUSTIFIED**. The proved parts are not a paper contract.

## Notation and dependencies

$N_G(u)$ is an open neighbourhood; $N_G[u]=N_G(u)\cup\{u\}$.
$\overline G$ is the simple complement on the same labelled vertices.
$\tau(G)$ is the least $t\ge0$ for which $F^t(G)$ is recurrent.
$P_4$ is the four-vertex path, and $2K_2$ is two disjoint edges.
$S(a,k)$ is the Stirling number of the second kind.

1. Adjacent-pair witnesses imply inflation and the generic clock.
2. Four distinct witness vertices identify the classical fixed class.
3. Inflation plus the empty neighbourhood gives isolate preservation.
4. For bipartite targets, inflation forces a bipartite source; isolate
   preservation supplies nonempty row and column supports; within-part
   comparisons supply the classical Ferrers/lonesum representation.
5. Ordered row classes and nonempty incremental column blocks count that
   representation. No empirical step is used in any proof.

## 1. Inflation and complete recurrence

If $uv\in E(G)$, then $v\in N_G(u)\setminus N_G(v)$ and
$u\in N_G(v)\setminus N_G(u)$, since the graph has no loops. Both
differences are nonempty, and $uv\in E(F(G))$. Thus
$$
E(G)\subseteq E(F(G)).
$$
Each nonfixed iterate adds at least one edge and no edge is deleted.
Writing $m=\binom n2$ gives
$$
\tau(G)\le m-|E(G)|.
$$
Every periodic orbit must have the same edge set at consecutive times,
and therefore consists of a single fixed graph. This is the generic
finite inflationary-chain argument, not a sharp structural clock. For
$n=0,1$ there is one empty graph and $\tau=0$.

## 2. Exact fixed class via four-vertex witnesses

We claim
$$
F(G)=G\quad\Longleftrightarrow\quad
G\text{ has no induced }P_4\text{ and no induced }2K_2.
$$

Suppose $uv$ is a newly added edge. It was a nonedge, and there are
$x\in N_G(u)\setminus N_G(v)$ and
$y\in N_G(v)\setminus N_G(u)$. These four vertices are distinct:
$x$ is neither $u$ (no loop) nor $v$ (old nonedge), and likewise for $y$;
$x=y$ would require membership and nonmembership in $N_G(u)$ at once.
Among them, $ux,vy$ are edges while $uv,uy,vx$ are nonedges. If $xy$
is absent they induce $2K_2$; if present they induce the path $u,x,y,v$.

Conversely, in an induced $2K_2$ with edges $ux,vy$ the nonedge $uv$
has witnesses $x,y$. In an induced path $u,x,y,v$ the same endpoints
have those witnesses. Extra vertices outside these four cannot erase a
membership or nonmembership already specified on the four vertices.
Thus either forbidden subgraph causes a new edge, proving equivalence.

Complementation fixes the isomorphism type of $P_4$ and sends $2K_2$
to $C_4$. Therefore the fixed/recurrent carrier is exactly the complements
of trivially perfect graphs. The classical forbidden-subgraph and rooted
decomposition theory is explicitly deducted, not attributed to this
scout. It is directly stated in Dumas--Perez, §2, archived primary body.

For another exact representation, put $H=\overline G$. Since
$N_G(u)=[n]\setminus N_H[u]$, complements reverse inclusion. Hence
$$
uv\in E(\overline{F(G)})
\quad\Longleftrightarrow\quad
N_H[u]\subseteq N_H[v]\ \text{or}\ N_H[v]\subseteq N_H[u]
\qquad(u\ne v).
$$
Such a comparable closed-neighbourhood pair must be adjacent in $H$:
the smaller neighbourhood contains its own vertex. Thus this is exact
simultaneous edge deletion in the complement, retaining precisely
closed-neighbourhood-comparable edges. It is not vertex dismantling,
and no source proving the whole time sequence by vertex dismantling is
asserted.

## 3. Exact isolated-set preservation and empty fibre

If $u$ is isolated, its empty neighbourhood is contained in every other
neighbourhood, so it remains isolated. If it is not isolated, one old
incident edge survives by §1, so it cannot become isolated. Therefore
$$
\operatorname{Iso}(F(G))=\operatorname{Iso}(G).
$$
In particular the empty graph has the single predecessor itself at every
$n\ge0$. If a target has a specified isolate set $I$, every predecessor
has exactly the same isolates, and restriction to $[n]\setminus I$
is a bijection of fibres with the corresponding isolate-free target.
This is because the zero columns/rows contributed by $I$ do not change
any containment between the other neighbourhoods.

## 4. Complete bipartite target fibres: full classical adapter

Fix disjoint labelled nonempty sets $A,B$, of sizes $a,b$, and let the
target on $A\sqcup B$ be $K_{A,B}$. Then $F(G)=K_{A,B}$ if and only if
$G$ is a bipartite graph with this fixed bipartition, has no isolates,
and its $a\times b$ biadjacency matrix has pairwise nested row supports.

Necessity: by inflation every source edge is a target edge, so there are
no within-part source edges. No source vertex is isolated, by §3. Two
vertices in $A$ must remain nonadjacent in the output, which is precisely
comparability of their row supports.

For sufficiency, nested row supports imply nested column supports: if
columns $x,y$ had incomparable supports, rows $u,v$ could be chosen with
entries $1,0$ and $0,1$ at these two columns, contradicting row nesting.
Thus no output edge occurs within either part. For $u\in A,v\in B$,
their source neighbourhoods are nonempty subsets of disjoint sets $B,A$.
Nonempty disjoint sets are incomparable, so every cross edge is output.
These two observations recover exactly $K_{A,B}$.

An alternating $2\times2$ submatrix exists precisely when two row
supports are incomparable: choose one column from each strict set
difference for one direction, and read the two rows for the reverse.
Consequently the above source matrices are exactly the classical lonesum
matrices without any zero row or column. This entire inverse geometry is
already a mature static class, also explicitly deducted in P200.

Here is the exact count, including the full bijection rather than a mere
name or analogy:
$$
|F^{-1}(K_{A,B})|
=\sum_{k=1}^{\min(a,b)}(k!)^2S(a,k)S(b,k).
$$
Order the distinct nonempty row supports as
$R_1\subsetneq\cdots\subsetneq R_k$. Nonzero columns imply $R_k=B$.
For the row indices choose their nonempty ordered equality classes
$(A_1,\ldots,A_k)$, which has $k!S(a,k)$ possibilities. Put $R_0=\varnothing$;
the increments $D_i=R_i\setminus R_{i-1}$ are nonempty and partition $B$,
giving $k!S(b,k)$ ordered choices. These data recover the matrix uniquely
by assigning support $D_1\cup\cdots\cup D_i$ to all rows in $A_i$.
Every pair of ordered partitions yields a nonzero nested-row matrix,
so the construction is bijective. Sum over $k$.

Adding any specified isolate set leaves this count unchanged by §3.
If either part is empty the target is the empty graph; its count is one,
and the displayed positive-part formula is not used. For stars ($a=1$
or $b=1$) the count is one; for $K_{2,2}$ it is five. This is precisely
the no-zero-row/no-zero-column branch of Brewbaker's §3.2 ordered-class
enumeration, not a new inverse/extremal residual.

## 5. Why the old P143 temporal identity is not transferred

Let $T(A)_{uv}=1[N_G(u)\subseteq N_G(v)]$. Then
$$
F(A)_{uv}=(1-T(A)_{uv})(1-T(A)_{vu})\quad(u\ne v).
$$
P143 proves $T^3=T$ on all Boolean matrices because the full first image
is a preorder and the next iterate transposes it. ONI discards orientation,
loops and comparable pairs and then recomputes from a simple graph.
This is a one-step factorization, not a demonstrated conjugacy.
Indeed the original pilot contains the graph masks
$$
59\longmapsto571\longmapsto955\longmapsto955
$$
at $n=5$ with lexicographic edge bits. Thus $F^3(G)\ne F(G)$ for that
source. This explicit witness rules out the literal old cubic identity,
but does not create a fresh theorem by itself.

## 6. Honest boundary and disposition

The recurrent carrier is fully classified for all $n$, but its class is
classical and the convergence proof is only generic edge inflation. No
sharp all-size entrance formula, recursive pointwise clock or other
nontransferable temporal residual has been proved. The complete bipartite
inverse is fully solved but exactly old lonesum counting. The inverse for
arbitrary targets and its global sharp maximum remain unproved.

The bounded pilot refutes any blanket claim that complete graphs always
maximize fibres: at $n=4$ the three labelled $K_{2,2}$ targets maximize
with five predecessors. At $n=5$ the complete graph alone maximizes with
38, so even the small-box extremizers change form. These are exact
original-box facts, not an all-parameter extremal theorem.

Status: **HOLD_PROOF / NO_PROMOTION**. No larger box, source-clearance
claim, new candidate number or review task is justified by these results.
