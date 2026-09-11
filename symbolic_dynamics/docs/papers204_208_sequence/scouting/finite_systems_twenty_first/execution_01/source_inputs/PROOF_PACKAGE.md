# NED partial proof package and non-promotion boundary

## Claim

For the map and state space in `INTAKE.md`, every target has an exact,
nonredundant predecessor decoder below. If $M<n$, the map is a permutation
and every state is recurrent (entrance time zero). These two mathematical
claims are `PROVABLE AS STATED`. A complete recurrent-core/clock theorem for
all $M\ge n$ is `NOT CURRENTLY JUSTIFIED` and is not claimed.

## Assumptions and notation

Let $n\ge1$, $M\ge0$, and identify indices with $\mathbb Z/n\mathbb Z$ in the
clockwise increasing order. A target is $y\in X_{n,M}$. Put
$E_y=\{j:y_j<n\}$, $d_y(j)=y_j+1$ for $j\in E_y$, and
$p_y(j)=j-d_y(j)\pmod n$. Consider the directed graph on $E_y$ retaining an
edge $j\to p_y(j)$ only when its endpoint also lies in $E_y$.
A code is a directed simple cycle $Z$ of this graph satisfying
$\sum_{j\in Z}d_y(j)=n$. Cycles are identified by vertex set, not choice of
starting vertex. A self-loop is allowed. A code is nonempty by definition.

For a code define $x^Z_j=0$ for $j\in Z$ and $x^Z_i=y_i+1$ otherwise.
If all coordinates of $y$ are positive, also allow the separate predecessor
$x=y$. This fixed predecessor is not a cycle code.

## Proof strategy and dependency map

1. The previous old zero before each old zero determines its integer gap.
2. Winding exactly once forces a proposed cycle to traverse consecutive
   zeros in the actual ring order, with no skipped or overlapping gaps.
3. Reconstruction gives a bijection between codes and zero-containing
   predecessors, separately from the all-positive hold case.
4. Disjointness of cycles of a partial functional map bounds their number;
   the bound gives at most one predecessor when $M<n$.
5. A finite injective self-map is surjective and all its orbits are periodic.

## Proof

### 1. Necessity of a code

Suppose $x$ has zero set $Z\ne\varnothing$ and maps to $y$. For $i\notin Z$,
$y_i=x_i-1$. For $j\in Z$, let $r$ be the previous zero counterclockwise,
where $r=j$ when $Z=\{j\}$. The clockwise integer distance from $r$ to $j$
is one plus the number of intervening positive coordinates; use distance $n$
when there is only one zero. The update rule gives this distance as $y_j+1$.
Thus $1\le y_j+1\le n$, $j\in E_y$, and $p_y(j)=r$. These edges form one
directed simple cycle on $Z$. Its gap sum is the circumference $n$, as the
consecutive zero-to-zero intervals partition the ring. Reconstruction gives
exactly $x^Z$.

### 2. Sufficiency of a code and absence of interleaving

Take a code and list its vertices in the directed order
$j_0,j_1,\ldots,j_{k-1}$ with $j_{r+1}=p_y(j_r)$, indices modulo $k$.
Lift $j_0$ to an integer $a_0$ and set
$a_{r+1}=a_r-d_y(j_r)$. Positivity of every gap makes
$a_0>a_1>\cdots>a_k=a_0-n$. Therefore these lifts list all code vertices
strictly in counterclockwise order within one turn. No additional code
vertex is inside an interval $(a_{r+1},a_r)$: every code vertex appears in
this single strictly descending list, and consecutive entries have none
between them. Thus the integer interval immediately before zero $j_r$
contains exactly $d_y(j_r)-1=y_{j_r}$ other coordinates, all outside $Z$.

All coordinates outside $Z$ of $x^Z$ are positive, so the positive-run
dispatch sends exactly $y_{j_r}$ chips into zero $j_r$. Positive coordinates
decrement to $y_i$. The mass of $x^Z$ is
$$\sum_{i\notin Z}(y_i+1)=M-\sum_{j\in Z}y_j+n-|Z|=M,$$
where the code condition says $\sum_{j\in Z}y_j=n-|Z|$. Hence $x^Z$ is a
valid predecessor in the same finite state space.

### 3. Completeness, nonredundancy and the hold case

Steps 1 and 2 give all zero-containing predecessors and no others. Different
codes have different zero sets and hence different reconstructed states.
An all-positive source is held by definition, so it is a predecessor of $y$
if and only if $y$ itself is all positive. It is distinct from every decoded
zero-containing state. Consequently
$$|T^{-1}(y)|=\#\{\text{winding-one codes for }y\}+
\mathbf1_{\{y_i>0\text{ for every }i\}}.$$
The formula is an evaluated cycle decoder, not a sum over candidate source
states or an inclusion--exclusion tautology.

### 4. A general bound and the low-mass permutation theorem

Distinct directed cycles in a partial functional graph have disjoint vertex
sets: if they shared a vertex, uniqueness of its successor would make their
entire forward cycles agree. If there are $k$ codes with union size $L$, then
$L\le n$ and summing their winding conditions gives
$$kn-L=\sum_{j\text{ in the union}}y_j\le M.$$
Therefore $k\le\min\{n,\lfloor M/n\rfloor+1\}$. This is only an upper
bound, not a claimed sharp extremum. If $M<n$, all-positive states are
impossible and $k\le1$. Step 3 then shows that every target has at most one
predecessor: $T$ is injective on $X_{n,M}$. This set is nonempty and finite,
so its image has its full cardinality; $T$ is also surjective. In a finite
permutation every orbit is a cycle, proving entrance time zero for every
state. The statement includes $M=0$, whose unique state is fixed, and $n=1$,
where the low-mass case is only $M=0$.

## Corrections and missing claims

The dense-only-positive-core hypothesis is false. At $n=M=3$,
$(2,1,0)\to(1,0,2)\to(0,2,1)\to(2,1,0)$ is a nonconstant cycle containing
zeros. Also $(3,0,0)\to(2,1,0)$ shows at least one nonrecurrent state in this
box, so the low-mass conclusion cannot simply be extended to all mass.
No complete dense recurrent classification, sharp entrance bound,
all-parameter cycle enumeration, or sharp all-parameter fibre maximum is
proved. Finite-pilot cycle/extremum tables do not supply those missing steps.

## Source and open risks

The fixed-ring local primitive coincides with the Montréal-solitaire run
update described by a secondary survey; the primary 1992 body remains
unread. Neither low-mass recurrence nor the inverse formula is certified as
a literature advance. The exact labelled-ring boundary is not itself an
adequate novelty certificate. The author proofs above are useful negative/
partial evidence only. Without full source clearance and a substantive
complete temporal mechanism beyond a likely known primitive, disposition
is NO_PROMOTION, not an admissible paper contract.
