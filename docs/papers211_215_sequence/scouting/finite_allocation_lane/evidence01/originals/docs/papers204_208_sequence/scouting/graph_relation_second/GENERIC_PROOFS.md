# Zero-credit deductions and rejected proof routes

These are author scout notes, not retained paper theorems or independent
reviews. They explain why short orbits alone did not promote three probes.

## MGE: matching exchange and a classical energy

The selected mutual pairs are vertex-disjoint. A globally greatest edge
under the shared strict priority is chosen by both its endpoints; if any
edge has load gap at least two, at least one selected pair therefore fires.
On a pair with loads $a\ge b+2$, a unit transfer changes the square sum by
$$ (a-1)^2+(b+1)^2-a^2-b^2=-2(a-b)+2\le-2.$$
Selected pairs are disjoint, so their changes add. The square sum is a
nonnegative integer, hence every orbit becomes fixed; fixed states are
exactly the integer graph-Lipschitz loads $|x_u-x_v|\le1$ on every edge.

This is a literal match-and-balance algorithm. The proof is the centralised
unit-transfer argument of Feuilloley--Hirvonen--Suomela applied to a matching
in parallel. The priority affects scheduling, not the energy engine. No
sharp clock or new inverse theorem has been proved. It is killed without
claiming that the source contains this precise tie-breaking scheduler.

## RMA: monotone support, then independent support

Let $U=\{v:x_v>0\}$. A positive pile always chooses another vertex in $U$,
since its closed neighbourhood contains itself. On $U$, every nontrivial
chosen arrow strictly increases $(x_v,-v)$; the resulting functional graph
has only self-loop cycles. If some pile moves, its map on $U$ is not the
identity and cannot be a permutation (a nontrivial permutation would have
a longer cycle). Hence its image has fewer than $|U|$ vertices. All piles
are positive, so this image is exactly the next support.

Thus every nonfixed update loses at least one support point. A state is
fixed exactly when its positive support is independent: any edge between
positive piles makes its lower-ranked endpoint choose a different vertex;
without such an edge every positive pile chooses itself. The height bound
$|U|-1$ for nonzero mass is generic finite support erosion.

If $i_k(G)$ is the number of independent $k$-subsets, the number of fixed
mass-$M>0$ states is
$$\sum_{k\ge1} i_k(G)\binom{M-1}{k-1}.$$
It only assigns positive compositions to an independent support. This
static bookkeeping is not a materially separate inverse theorem. No
all-parameter sharp $n,M$ entrance formula or maximum fibre was proved.

## DGO: exact symmetric threshold representation

Fix for each edge $e=\{u,v\}$, $u<v$, an incidence column $b_e$ with $+1$
at $u$ and $-1$ at $v$. Set $s_e=+1$ for $u\to v$ and $-1$ for $v\to u$,
and let $B$ be the incidence matrix. If $g$ is the undirected degree vector,
then the old outdegree vector is $d=(g+Bs)/2$.

DGO points an unequal-outdegree edge from the lower-degree endpoint to the
higher-degree endpoint and retains its orientation at a tie. Consequently
its exact edge-spin update is
$$s'=\operatorname{sign}\bigl(-B^{\mathsf T}g-B^{\mathsf T}Bs+\frac{1}{2}s\bigr).$$
The untied degree difference contributes an even nonzero integer; the
half-unit self term resolves a zero difference in favour of the old sign.
There is no zero input to the sign. The matrix
$-B^{\mathsf T}B+\frac{1}{2} I$ is symmetric. Changing from $\{-1,+1\}$ to
$\{0,1\}$ preserves symmetry of the threshold weights and merely shifts
thresholds. Thus Goles--Olivos's symmetric threshold theorem directly gives
eventual period at most two. The pilot's period pattern is inherited.

P112 points unequal-score tournament edges in the opposite direction.
It has fixed-only recurrence, whereas DGO on a single edge is a strict
two-cycle. Neither a literal identity nor a complement conjugacy with P112
is asserted. The score-feedback neighborhood is deducted, and the exact
symmetric-threshold adapter is independently decisive. No nontransferable
sharp clock, full recurrent classification or fibre theorem has been found.

## ECD, LRC and GLD: what is not proved

ECD's strict three-cycle and GLD's larger unrelated periods rule out the
initial short-cycle guesses. They do not rule out other future theorems.
For LRC no all-parameter temporal proof or independently evaluated inverse
was found. Fixed-only recurrence through four vertices is recorded solely
as a finite observation. It is not a proof of a linear clock. None of these
three rules received a larger cutoff after this absence of a two-axis proof.
