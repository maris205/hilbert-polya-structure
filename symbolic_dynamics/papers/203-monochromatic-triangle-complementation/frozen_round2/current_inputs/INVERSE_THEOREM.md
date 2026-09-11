# Monochromatic triangle complementation: the complete inverse axis

Date: 2026-09-05 UTC. **PROVABLE AS STATED** for this inverse theorem.
The all-parameter sharp temporal theorem is proved in the separately
pinned collaborator file
`../../reviews/mct_temporal_pressure_20260905/PROOF_PACKAGE.md`, fully read
and challenged by this inverse author. This document does not allocate a
paper or certify two-axis admission. External state: `HOLD_EXTERNAL`.

## Literal map and assumptions

For $n\geq0$, a state is an arbitrary simple, loopless, undirected labelled
graph on $[n]=\{0,\ldots,n-1\}$. Equivalently, assign each pair a colour
$y_{ij}\in\{0,1\}$. This is the **complete graph carrier** of
$2^{\binom n2}$ assignments, not the smaller carrier of acyclic forests.
An unordered triple is compared lexicographically after sorting its labels.
It is monochromatic if its three pair colours coincide.

The map $F$ complements all three pairs of the lexicographically first
monochromatic triple; it holds if there is no such triple. Let $Y^Q$
denote complementation on the triple $Q$, and let $\mathcal M(Y)$ be the
set of monochromatic triples of $Y$.

## Strategy and dependencies

1. Undo a proposed monochromatic triple, separating destruction of existing
   earlier monochromatic triples from creation of new ones. This gives
   every predecessor set without simulating an orbit.
2. Any two admissible inverse triples must share a pair. The familiar
   star/top classification of cliques of the Johnson graph $J(n,3)$ then
   bounds their number. The static classification is classical, zero credit.
3. Explicit colourings realize both competing bounds.
4. Target-only star/top certificates characterize every equality case,
   including the crossover $n=6$ and all small ranks.

## 1. Every-target source set

For $Q\in\mathcal M(Y)$ of colour $c$, call $Q$ admissible when:

**D.** Every $P\in\mathcal M(Y)$ with $P<Q$ shares exactly two vertices
with $Q$.

**C.** For every pair $\{x,y\}\subset Q$ and $u\notin Q$ such that
$\{u,x,y\}<Q$, the two colours $y_{ux},y_{uy}$ are not both $1-c$.

Write $\mathcal A(Y)$ for this explicitly defined family. Then

$$F^{-1}(Y)=
\begin{cases}
\{Y\},&\mathcal M(Y)=\varnothing,\\
\{Y^Q:Q\in\mathcal A(Y)\},&\mathcal M(Y)\ne\varnothing.
\end{cases}$$

All displayed predecessors are distinct. In particular, a nonfixed target
is in the image exactly when $\mathcal A(Y)$ is nonempty, and its fibre
size is $|\mathcal A(Y)|$. This includes zero fibres.

### Proof

A nonholding move leaves its selected triple monochromatic in the output.
Thus every nonholding predecessor is $Y^Q$ for a monochromatic target
triple $Q$. Different triples change different sets of three edges and
yield different sources. The triple $Q$ is monochromatic in $Y^Q$;
it is selected exactly when no earlier triple is monochromatic there.

An earlier monochromatic target triple either shares no edge with $Q$,
in which case it survives, or shares one edge, in which case its other
two same-coloured edges are unchanged and it becomes mixed. (Distinct
triples cannot share two edges.) Condition D is therefore exactly the
requirement to destroy all existing earlier monochromatic triples.

A previously mixed triple can become monochromatic only if it shares an
edge $xy$ with $Q$. That edge changes from $c$ to $1-c$, while its other
two edges are unchanged; creation occurs exactly when those two edges
already have colour $1-c$. Condition C excludes every such earlier
creation. These alternatives exhaust all triples, proving necessity and
sufficiency. If the target has no monochromatic triple it cannot be the
output of a nonholding move, so its only predecessor is its hold source.

## 2. Sharp maximum and the source-family geometry

For all $n\geq0$ the largest fibre size is

$$M_n=\begin{cases}1,&n\leq3,\\ \max\{4,n-2\},&n\geq4.\end{cases}$$

For a nonfixed target, $\mathcal A(Y)$ is a pairwise edge-intersecting
family of triangles. It is contained either in a common-edge star
$\{\{a,b,v\}:v\notin\{a,b\}\}$ or in the four faces of a four-set.

### Proof of the upper bound

If $P<Q$ are both admissible, then $P$ is monochromatic in $Y$ and must
not remain monochromatic in $Y^Q$. Hence $P,Q$ share an edge. To check the
elementary star/top alternative directly, take two distinct triples
$abc,abd$. Every triple sharing an edge with both either contains $ab$
or is $acd$ or $bcd$. If one of the latter is present, every common-edge
triple must use $c$ or $d$ as its third vertex, so the entire family lies
in $\binom{\{a,b,c,d\}}3$. If neither occurs, the family has common edge
$ab$. Families of size zero or one satisfy the containment assertion
without choosing two members. Thus the two capacities are $n-2$ and $4$.

For $n\leq2$ the map is the identity. For $n=3$ the one possible triangle
is complemented on its two monochromatic states, and every mixed state
holds. This is a permutation, so every fibre has size one. For $n\geq4$
fixed targets still have fibre one, below the asserted upper bound.

### Explicit witnesses for both lower bounds

For the common-edge bound, give every edge incident with $0$ or $1$ the
same colour $c$, and every edge on $\{2,\ldots,n-1\}$ colour $1-c$.
The monochromatic triangles involving $0$ or $1$ are exactly $01v$.
Complementing any one $01v$ destroys all earlier such triangles, creates
no new earlier triangle, and leaves only possible monochromatic triangles
whose least vertex is at least $2$, later than $01v$. Every $01v$ is
therefore admissible, supplying $n-2$ distinct predecessors.

For the four-face bound, set every edge to colour $c$ except
$\{0,v\}$ for $v\geq4$, which have colour $1-c$. Let
$S=\{0,1,2,3\}$. Complement any of its four triangles $Q$.
Other triples contained in $S$ become mixed. A triple containing $0$,
an outside vertex and a vertex of $S\setminus\{0\}$ is mixed before
and after the complementation: its edge to the outside vertex has colour
$1-c$, the edge from that vertex to the other inside vertex has colour
$c$. A triple containing $0$ and two outside vertices is also mixed.
Every remaining triple not contained in $S$ has least label at least $1$
and at least one label at least $4$; it is later than $Q$ when $0\in Q$,
and later than $123$ when $Q=123$, unless it contains two labels of $123$.
In that last case its edge on $Q$ is complemented and it is mixed.
Thus every face of $S$ is admissible. The two constructions together
prove the lower bound at every $n\geq4$.

## 3. Target-only certificates for every maximum-fibre target

The following tests use the target colours and label comparisons only;
they do not invoke $F$, its inverse, or the size of $\mathcal A$.

### Full-star certificate

Choose $a<b$, put $U=[n]\setminus\{a,b\}$, and let $c=y_{ab}$.
For $n\geq4$, write $Q_z$ for the sorted triple $\{a,b,z\}$ and
$Q_* = Q_{\max U}$. The edge $ab$ is certified if all three hold:

**S1.** $y_{az}=y_{bz}=c$ for every $z\in U$.

**S2.** Whenever $x<y$ belong to $U$, $y_{xy}=c$, and
$z\in U\setminus\{x,y\}$, one has
$Q_z<\{a,x,y\}$ (with the latter triple sorted).

**S3.** Every monochromatic triple contained in $U$ is later than $Q_*$.

These conditions are equivalent to **all** $n-2$ triangles $Q_z$ being
admissible.

#### Proof

All $Q_z$ monochromatic is exactly S1. With S1, reversing one of them
cannot create a different monochromatic triangle: for a shared edge
incident with $a$ or $b$, the unchanged edge from that endpoint to the
outside vertex has colour $c$, precluding colour $1-c$ after reversal.
Other star triangles are destroyed through $ab$.

The other existing monochromatic triples with an endpoint $a$ or $b$
are $axy,bxy$ for outside edges $xy$ of colour $c$. A reverse triangle
$Q_z$ destroys them when $z\in\{x,y\}$, and leaves them unchanged
otherwise. Since $axy<bxy$ for $a<b$, neither may precede $Q_z$ exactly
when S2 holds. Monochromatic triples entirely in $U$ are unchanged by
every star reversal; excluding them before every $Q_z$ is exactly S3.
This proves both directions.

### Full-four-face certificate

Choose a four-set $S$, list its four triples in lexicographic order, and
call the last one $Q_*$. It is certified if the following hold:

**K1.** All six edges within $S$ have one colour $c$.

**K2.** Every monochromatic triple $P$ with $|P\cap S|\leq1$ is later
than $Q_*$.

**K3.** For every $u\notin S$ and pair $\{x,y\}\subset S$, put
$P=\{u,x,y\}$ in sorted order. If $y_{ux}=y_{uy}=c$, then $P$ is
later than every face $Q$ of $S$ that does **not** contain $\{x,y\}$.
If $y_{ux}=y_{uy}=1-c$, then $P$ is later than every face $Q$ that
**does** contain $\{x,y\}$. Mixed pairs impose no condition.

These conditions are equivalent to all four faces being admissible.

#### Proof

All four faces monochromatic is equivalent to K1. Every other face of
$S$ shares one edge with the reversed face and becomes mixed. Triples
with at most one vertex of $S$ do not change under any face reversal,
so K2 is necessary and sufficient for those triples. A triple $uxy$
with exactly two vertices in $S$ changes only when the reversed face
contains $xy$. If its two outside edges have colour $c$, it is
monochromatic precisely when $xy$ is not flipped; if both have colour
$1-c$, it is monochromatic precisely when $xy$ is flipped. If their
colours differ it is never monochromatic. K3 is exactly the needed
earlier-triple exclusion in these cases, completing the proof.

### Complete equality classification

- If $n\leq3$, **every** target is a maximizer.
- If $n=4,5$, a target is a maximizer exactly when it has a certified
  four-set K1–K3.
- If $n=6$, a target is a maximizer exactly when it has a certified edge
  S1–S3 **or** a certified four-set K1–K3.
- If $n\geq7$, a target is a maximizer exactly when it has a certified
  edge S1–S3.

Indeed, equality forces the inverse family to fill a largest star or top
in the containment classification; the only capacity tie is $n=6$.
Conversely the certificates provide that many actual predecessors, and
the already proved upper bound excludes any excess. This gives all
equality cases without asserting a formula for their total number.

## Temporal and ownership limitations

The selector stays the same or decreases, giving fixed points and
two-cycles by a generic involution-selection lemma. This earns zero
contribution credit. The complete temporal proof is in the collaborator
file pinned above: after the first strict change the least vertex is
constant; alternating edge colours and a separate initial-retired-vertex
argument exclude all returns; explicit colourings attain tail $n-3$ for
every $n\geq3$. The finite $n\leq6$ boxes corroborate those statements
but are not their proof. The temporal collaborator is a co-contributor,
not this candidate's independent reviewer.

The Johnson star/top classification and clique number are classical
static input, explicitly compared in `SOURCE_OWNER.md`. The residual
inverse work is the admissible-source mapping, attainability colourings
and full target certificates, not a new Johnson-graph theorem. Whether
this is sufficient alongside the temporal theorem remains for the
process-separated gate; these true formulas do not themselves promote MCT.
