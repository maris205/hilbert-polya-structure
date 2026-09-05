# Third-lane proof boundaries — no promoted theorem package

Author: `/root/batch197_fifth_scout`, 2026-09-05 UTC.
Status: the negative-control and restricted-family statements below are
**PROVABLE AS STATED**. A full-carrier two-axis contract for any of the seven
probes is **NOT CURRENTLY JUSTIFIED**. No numbered paper is proposed.

## Assumptions, notation and dependency map

All graphs are simple, undirected and labelled. Each update treats old
connected components separately and adds no edge across them. All predicates
concern distinct vertices. `DIA` retains pairs at the old component diameter;
`MMD` retains mutually locally maximally distant pairs; `RED` retains pairs
at maximum unit-network effective resistance in their component. `ODD` and
`EVEN` retain pairs at positive odd and even old shortest-path distance.

The proof route is direct metric calculation. ODD's retraction uses a first
edge of a shortest path. The cycle family uses its cyclic labelling and the
two paths in parallel resistance formula. None of these deductions uses
the enumerated functional graph, an unproved larger-size pattern, or an
inverse-fibre claim. The final geometry boundary uses the literal projection
formula, not Euclidean limit results over a finite field.

## 1. Immediate ODD retraction: zero contribution credit

**Claim.** ODD is extensive, preserves connected components, and satisfies
$O^2=O$. Its fixed graphs are exactly graphs whose connected components
have diameter at most two, counting a singleton's diameter as zero.

**Proof.** Every old edge has distance one and is retained. No cross-component
edge is created, so components are preserved. For vertices $u,v$ in one
component, an odd old distance gives an output edge. If their old distance
is even and positive, let $w$ be the first vertex after $u$ on a shortest
$u$--$v$ path. Then $d(w,v)=d(u,v)-1$: the path gives the upper bound and
the triangle inequality gives the lower bound. This is odd, so $u,w,v$ is
an output path of length two. Every output component therefore has diameter
at most two. On such a graph its only odd positive distances are one, so
the next update changes nothing. Conversely, a component of diameter at
least three contains two vertices at distance three along a shortest path;
ODD adds their missing edge. This proves the characterization. ∎

The label “closure control” means this immediate extensive retraction. It
does **not** assert that ODD is order-preserving under arbitrary edge addition.
ODD was killed when this was recognized during implementation. It was retained
only as an eighth negative control; EVEN replaced its live scouting seat.

## 2. Exact cyclic adapter defeats a universal period-two inference

**Claim.** Let $N=2h+1\ge3$ be odd. On the labelled cycle with edges
$\{i,i+s\}$ in $\mathbb Z/N\mathbb Z$, where $s$ is a unit, each of
DIA, MMD and RED replaces the step $s$ by $hs$. Starting from step one,
the exact period is the least $t\ge1$ for which $h^t\equiv\pm1\pmod N$,
equivalently $2^t\equiv\pm1\pmod N$. In particular each has a cycle of
exact period $k$ on $N=2^k-1$ vertices for every $k\ge3$.

**Proof.** Relabel by multiplication by $s^{-1}$. Cycle distances are
$\min(d,N-d)$ and reach their maximum $h$ exactly at offsets $\pm h$.
For a pair at distance $d<h$, the first endpoint has a neighbor farther
from the second, so this pair is not MMD. At distance $h$, both neighboring
distances are at most $h$, giving MMD. Finally the two cycle paths between
a pair at distance $d$ are disjoint except at the endpoints, have resistances
$d$ and $N-d$, and are in parallel. Solving their common-voltage current
equations gives effective resistance $d(N-d)/N$. For integers
$0\le d<h$, its increment is $(N-2d-1)/N>0$. Its distinct-vertex maximum
is therefore attained exactly at offsets $\pm h$ as well. These three
operators consequently agree on this entire cycle family.

Since $\gcd(h,2h+1)=1$, the next graph is again such a cycle. Induction
gives step $h^t$. Two step cycles have the same labelled edge set exactly
when their steps differ by sign, as can be read from the neighbors of zero.
This proves the first period formula. The relation $2h\equiv-1$ gives
the equivalent formula involving two.

For $N=2^k-1$, $2^k\equiv1$. If $1\le t<k$, then
$0<2^t-1<N$ and $0<2^t+1<N$ for $k\ge3$, so neither sign congruence
is possible. Thus the exact period is $k$. ∎

These are labelled cycles. Their unlabelled isomorphism type is constant;
discarding labels would hide the period. The restricted dynamics is exactly
multiplication by $h$ on $(\mathbb Z/N\mathbb Z)^\times/\{\pm1\}$.
This cyclic arithmetic is an old power-map mechanism, not a surviving new
temporal theorem, and gives no all-graph inverse/extremal theorem.

The single proof-directed $C_7$ check in the canonical is not a new exhaustive
cutoff. DIA/MMD/RED send step $1\to3\to2\to1$. EVEN instead sends
$1\to2\to4\to1$, since the only positive even distance in a seven-cycle
is two. Hence EVEN also has a genuine three-cycle. We make no general EVEN
period formula beyond this sentinel.

## 3. Do not identify MMD with old MEG

The old RX12 MEG predicate was $d(u,v)=e(u)=e(v)$. MMD uses local comparisons
with neighbors, not the global eccentricities. Consider the tree with edges
$01,12,23,14$. The leaves $0,4$ have distance two and eccentricity three.
They are not MEG adjacent. Their only neighbor is $1$, at distance one from
the other leaf, so they are MMD adjacent. This is an exact formula distinction,
not an ownership conclusion. MMD itself is precisely the classical strong
resolving graph with isolated original vertices retained, applied per component.

For DIA and MMD the fixed graphs are disjoint unions of cliques. For DIA,
any retained old edge in a fixed nontrivial component forces diameter one.
For MMD, an adjacent pair is MMD exactly when its closed neighborhoods
coincide; propagation across each component then makes the component a clique.
Conversely every clique is fixed by both maps. The resulting Bell census is
static partition counting and earns no separate enumerative credit.

## 4. Geometric totalization and source-transfer limits

Let $p\equiv3\pmod4$ be prime, $V=\mathbb F_p^2$, and write
$Q(v)=v_x^2+v_y^2$. This form is anisotropic: a nonzero isotropic vector
with nonzero second coordinate would give a square root of $-1$, impossible
because its order would be four in a group of order $p-1\equiv2\pmod4$;
a zero second coordinate forces the first coordinate zero too.

For $b\ne c$, the perpendicular projection is
$$\pi_{bc}(a)=b+\frac{(a-b)\cdot(c-b)}{Q(c-b)}(c-b).$$
For $b=c$, define $\pi_{bb}(a)=b$, the projection onto that singleton.
The two literal maps are
$$\mathrm{PED}(a,b,c)=(\pi_{bc}(0),\pi_{ca}(0),\pi_{ab}(0)),$$
$$\mathrm{REF}(a,b,c)=(2\pi_{bc}(a)-a,2\pi_{ca}(b)-b,
                         2\pi_{ab}(c)-c).$$
Thus every ordered triple is in the carrier, including collinear and repeated
points, with no excluded denominator. There is no arbitrary isotropic-line
completion at these primes.

If $b=c\ne a$, REF sends $(a,b,b)$ to $(2b-a,b,b)$ and then back. The two
states differ since the characteristic is odd. Nicollier's real-plane paper
instead declares every repeated-vertex triangle fixed. Its regular geometric
rule is a direct owner, but its boundary convention is not this rule and its
real limit/orbit theorems are not finite-field theorems.

Neuberg's third fixed-point pedal triangle similarity is a direct classical
iteration neighbor for PED. We do not claim that an angle-chasing real theorem
automatically proves the finite-field totalized carrier's three-step scalar
identity, clock, exceptional fibers or inverse atlas. No such full proof was
completed. The periods 24 and 144 and the observed height three are finite
data only. REF's observed periods one/two and heights one/four likewise do
not imply any all-prime assertion. Adding denominator exceptions or a field
parameter does not itself repair either candidate's missing independent axes.

## Open risks and disposition

TWO lacks a proved all-graph temporal classification and inverse mechanism.
For DIA/EVEN/MMD/RED, the first five-vertex pattern is explicitly insufficient;
the all-size restricted cycles have an old arithmetic adapter, and no separate
full-carrier inverse/extremal theorem is proved. PED/REF have direct classical
iteration neighborhoods and unresolved full finite-field contracts. All seven
probes and the ODD control are **NO_PROMOTION**, not reserves. Larger cutoffs
are not authorized by a weak silhouette and were not used to rescue one.
