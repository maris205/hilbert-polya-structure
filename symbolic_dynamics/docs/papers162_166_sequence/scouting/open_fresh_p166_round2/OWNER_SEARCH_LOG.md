# Owner and portfolio audit — P166 replacement round 2

**Search date:** 2026-09-03.  **External status:** `HOLD_EXTERNAL`.

This is a bounded owner/value audit, not a novelty certificate.  A query
non-hit is never used as evidence of novelty.  The gate asks the stronger
question: after direct operations, standard parameters, and internal proof
engines are assigned zero credit, is a paper-sized conjunction left?  Here
the answer is no.

## Search strings

The following clusters were searched against journal/author/repository pages:

```text
acyclic orientation reverse all sources parallel source reversal dynamics
source-to-sink click acyclic orientations chip firing
directed relation exact powers square roots Boolean relation composition
simplicial complex C vee D sigma union tau chromatic number cover faces
k-fold self union simplicial complex
matroid simplification cosimplification parallel series extensions
minimum partition matroid independent subsets Edmonds
convex geometry extreme point operator anti-exchange
convex layers remove extreme points onion peeling
```

## 1. PFR has a direct literal owner

Eric Goles and Erich Prisner, “Source reversal and chip firing on graphs,”
*Theoretical Computer Science* 233 (2000), 287--295,
[DOI 10.1016/S0304-3975(99)00122-X](https://doi.org/10.1016/S0304-3975(99)00122-X).

The abstract asks what happens when one repeatedly reorients **all arcs
starting at sources**, labels the subject discrete dynamics/parallel
iteration, and connects it to chip firing.  That is the `PFR` literal rule,
not merely adjacent background.  Restricting initial orientations to acyclic
ones does not create an owner firewall: source reversal preserves acyclicity.

M. Develin, M. Macauley and V. Reiner, “Toric partial orders,”
*Transactions of the AMS* 368 (2016), 2263--2280,
[author offprint](https://www-users.cse.umn.edu/~reiner/Papers/toric-posets-offprint.pdf),
also records source-to-sink flips/click equivalence and points to Pretzel and
earlier work.  This is not needed for the kill, because Goles--Prisner already
own the parallel iteration itself.

**Subtraction:** the operator, preservation context, dynamical question, and
chip-firing connection all receive zero credit.  The derived target fibre is
only dominating-set inclusion--exclusion on sources versus sinks.

**Gate:** `KILL_DIRECT_OWNER`.

## 2. USC's operation and clock parameter are explicit

Ron Aharoni and Eli Berger, “The intersection of a matroid and a simplicial
complex,” *Transactions of the AMS* 358 (2006), 4895--4917,
[article copy](https://www.researchgate.net/publication/250750417_The_intersection_of_a_matroid_and_a_simplicial_complex).

The paper explicitly defines

```text
C vee D = {sigma union tau : sigma in C, tau in D}
```

and the `k`-fold self-product of a complex.  Its Definition 8.5 defines the
chromatic number of a complex as the smallest number of faces whose union is
the ground set.  These are exactly the two ingredients in
`T^t(K)=vee^(2^t)K` and the threshold `2^t>=chi(K)`.

Jack Edmonds, “Minimum partition of a matroid into independent subsets,”
*Journal of Research of the National Bureau of Standards B* 69B (1965),
67--72, [primary PDF](https://nvlpubs.nist.gov/nistpubs/jres/69B/jresv69Bn1-2p67_A1b.pdf),
owns the matroid independent-set cover theorem that would control the desk
candidate `MUS`.  This makes the matroid-union specialization weaker, not a
replacement.

**Subtraction:** `vee`, its repeated self-product, complex chromatic/covering
number, Dedekind counts, and support inclusion--exclusion receive zero credit.
The remaining arbitrary-time root problem was not solved.

**Gate:** `KILL_DIRECT_INGREDIENT_AND_P97`.

## 3. ASD is standard simplification/cosimplification

The standard definitions used in contemporary primary matroid work are:

- simplification deletes loops and all but one member of each parallel class;
- cosimplification is the dual operation, equivalently
  `co(M)=si(M^*)^*`.

For a representative primary use, see J. Geelen, A. M. H. Gerards and
G. Whittle, “Matroids representable over GF(3) and other fields,”
[author PDF](https://homepages.ecs.vuw.ac.nz/~whittle/pubs/matroids_representable_over_GF%283%29_and_rationals.pdf).
The definitions are also recorded in Stefan van Zwam’s thesis,
[Partial Fields in Matroid Theory](https://www.matroidunion.org/stefan/pdf/thesis-online.pdf),
§5.1.5--5.1.6; this second item is a terminology check, not the primary basis
of the gate.

The round-two map is just simplification followed by duality.  Its inverse
product counts absent elements, loops, and parallel extensions of a fixed
simple matroid.  No direct source for this exact least-label finite map was
located in the bounded search, but that non-hit gives no novelty credit: the
entire proof is the standard classification of a matroid above its
simplification, and the temporal part is alternating parallel/series rank
erosion.

**Gate:** `KILL_STANDARD_SIMPLIFICATION_RANK_EROSION`.

## 4. CGP is the established extreme operator plus peeling

P. H. Edelman and R. E. Jamison, “The theory of convex geometries,”
*Geometriae Dedicata* 19 (1985), 247--270,
[article copy](https://www.researchgate.net/profile/Paul-Edelman/publication/225269790_The_theory_of_convex_geometries/links/54eb2a300cf2f7aa4d5a6ff5/The-theory-of-convex-geometries.pdf),
develops finite convex geometries/antimatroids, their convex-set lattices,
and their extreme-point foundation.

K. Ando, “Extreme point axioms for closure spaces,” *Discrete Mathematics*
306 (2006), 3181--3188,
[DOI 10.1016/j.disc.2006.04.034](https://doi.org/10.1016/j.disc.2006.04.034),
studies the extreme-point operator for closure spaces, matroids, and
antimatroids/convex geometries.

For the repeated geometric specialization, J. Matoušek et al., “Peeling
Sequences” describes convex layers as iteratively computing a convex hull
and removing its vertices,
[open article](https://pmc.ncbi.nlm.nih.gov/articles/PMC11914258/), and
records the earlier convex-layer/onion-peeling algorithmic literature.  The
precise abstract-convexity operator is already supplied by Edelman--Jamison
and Ando; the geometric peeling source is included only to show that the
iteration is not a new dynamical viewpoint.

**Subtraction:** convex geometry, extreme points, the extreme operator, and
parallel extreme-layer peeling receive zero credit.  No geometry-uniform
target fibre survived.

**Gate:** `KILL_DIRECT_PEELING_OWNER_THIN`.

## 5. PSE is both externally and internally occupied

Martin Kutz, “Computing roots of directed graphs is graph isomorphism hard,”
[arXiv:math/0207020](https://arxiv.org/abs/math/0207020), defines exact
directed graph powers by `k`-step directed walks and explicitly identifies
them with iterated binary-relation composition / Boolean-matrix powers.
Thus arbitrary target inversion is the directed-root problem.

More importantly, the exact strict-poset map is already in the local
P127--P131 algebraic scout as `S03`:

```text
R -> R intersect R^2;
for strict transitive R this equals R^2;
T^t(R)=R^(2^t);
KILL: direct relation powers.
```

`PSE` was replayed only as a sentinel and contributes no new candidate.

## Internal P1--P165 collision matrix

| round-two map | closest occupied/permanent lane | collision |
|---|---|---|
| `PFR` | P145 vertex-push/click background; graph orientation owner firewall | local orientation flips and established graph dynamics; direct external owner is already fatal |
| `USC` | P97 sumset squaring | associative self-product, `2^t`-fold iterate, generation/cover threshold to a closure core |
| `USC` | P110 join iteration | repeated join/product closure, though P110's translation orbit is different |
| `ASD` | P148 contraction and permanent matroid greedy/rank-erosion exclusions | canonical deletion followed by duality; inverse merely counts extensions |
| `CGP` | P114 forest-leaf peeling, P159 odd-vertex pruning, prior MEP/SFP | simultaneous removal layers; clock from number of peel layers |
| `PSE` | prior scout `S03`, `TR1`, and relation-power kills | exact same map/mechanism, not only a silhouette |

## Final owner/value conclusion

- `PFR` is a literal direct-owner hit.
- `USC` is assembled entirely from an explicitly defined operation and its
  explicitly defined controlling parameter, and internally repeats P97.
- `ASD` is a standard rank-eroding matroid primitive with a decorative
  least-label convention.
- `CGP` is the abstract version of classical extreme-layer peeling and has no
  inverse axis.
- `PSE` is a prior literal kill.

Therefore the only defensible round-two result is
**`KILL_ALL / HOLD_EXTERNAL`**.

