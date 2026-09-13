# Citation Verification

## Verification protocol

The literature search was bounded and frozen on **2026-08-17**.  It used
primary journal pages, author or institutional copies, and arXiv records and
full text.  Query families combined generalized Hénon maps, consecutive torus
survival, finite-rank multiplicative groups, unit equations, sparse polynomial
images, cyclotomic points, semigroup integrality, and rational or integral
periodic points.  Citation chaining was used around the unit-equation and
arithmetic-dynamics sources named below.

The result is a verification record, not an exhaustive bibliography and not a
global priority claim.  Unpublished, unindexed, or differently phrased work can
remain undiscovered.

## The unique external proof input

### Francesco Amoroso and Evelina Viada (2009)

- Work: *Small points on subvarieties of a torus*.
- Publication: *Duke Mathematical Journal* 150(3), 407--442 (2009).
- DOI: <https://doi.org/10.1215/00127094-2009-056>.
- Primary full text: <https://amoroso.users.lmno.cnrs.fr/files-heightGmn/Duke.pdf>.
- Exact location: Theorem 6.2.
- Verified content: for an algebraically closed field of characteristic zero,
  fixed nonzero coefficients, and a rank-`R` subgroup of the `q`-torus, the
  number of nondegenerate solutions of a `q`-term linear equation equal to one
  is at most
  `A(q,R)=(8q)^(4q^4(q+R+1))`.
- Role here: this is the **only external theorem used in a proof**.  It supplies
  the rank-`2r` sparse-image estimate and the rank-`3r` local Hénon estimates.

#### Mandatory arbitrary-field bridge

Theorem 6.2 is not quoted as though it were stated directly for every
characteristic-zero field.  Given the field `K` in this project, choose an
algebraic closure `Kbar` and include `K*` and `Gamma` into `Kbar*`.  The
inclusion preserves the abstract rank of `Gamma`; every tuple group used in
the proof is a homomorphic image of `Gamma^2` or `Gamma^3`, hence has rank at
most `2r` or `3r`.  Every solution over `K` maps injectively to a solution over
`Kbar`.  Applying Amoroso--Viada over `Kbar` therefore bounds the original
solution set.  No descent or algebraic-closure equality of solution sets is
claimed.

The theorem permits arbitrary fixed coefficients in the linear equation.
Consequently, `a`, `c`, and the `b_j` are not inserted into the variable group,
and no coefficient-membership assumption on `Gamma` is needed.

## Historical quantitative predecessor

### Jan-Hendrik Evertse, Hans Peter Schlickewei, and Wolfgang M. Schmidt (2002)

- Work: *Linear equations in variables which lie in a multiplicative group*.
- Publication: *Annals of Mathematics* 155(3), 807--836 (2002).
- Primary journal page: <https://annals.math.princeton.edu/2002/155-3/p04>.
- DOI: <https://doi.org/10.2307/3062133>.
- Verified content: explicit uniform finiteness of nondegenerate linear
  equations in characteristic-zero finite-rank multiplicative groups.
- Role here: historical and conceptual predecessor only.  The displayed
  Paper16 constants use the sharper Amoroso--Viada theorem, so ESS is not an
  additional proof input.

## Closest one-dimensional sparse-image context

### Holly Krieger, Aaron Levin, Zachary Scherr, Thomas J. Tucker, Yu Yasufuku,
and Michael E. Zieve (2015)

- Work: *Uniform Boundedness of S-Units in Arithmetic Dynamics*.
- Publication: *Pacific Journal of Mathematics* 274(1), 97--106 (2015).
- Primary preprint: <https://arxiv.org/abs/1406.1990>.
- DOI: <https://doi.org/10.2140/pjm.2015.274.97>.
- Verified content, with theorem numbers checked against the published text:
  Theorem 1.7 gives a uniform `S`-unit image bound for degree-`d` monic
  polynomials in the ring of `S`-integers, excluding a single repeated-root
  form.  Theorem 1.8 is a local non-Archimedean valuation statement for a
  polynomial having exactly one coefficient of negative valuation, whose
  index is not `d-1`.  Corollary 1.9 turns that local statement into the
  exceptional-coefficient number-field orbit conclusion, bounding the
  `S`-units in the specified orbit by one.  The paper also gives a conditional
  route to its broader uniformity conjectures.
- Boundary distinction: Theorem 1.7 concerns a one-variable image set, while
  Theorem 1.8 and Corollary 1.9 concern one fixed one-variable orbit in the
  exceptional-coefficient setting.  Paper16 instead treats a two-dimensional invertible Hénon
  recurrence, arbitrary characteristic-zero fields, arbitrary finite-rank
  subgroups, a fixed short orbit window, explicit degeneracy strata, and a
  support-size threshold.  This source does not state PC1 or its four-case
  local automaton.
- Role here: neighboring motivation only, not proof input.

## Fixed-orbit subgroup intersections

### Jason P. Bell and Dragos Ghioca (2024)

- Work: *Intersections of orbits of self-maps with subgroups in semiabelian
  varieties*.
- Publication: *Bulletin of the London Mathematical Society* 56, 783--795
  (2024).
- Primary preprint: <https://arxiv.org/abs/2210.03152>.
- DOI: <https://doi.org/10.1112/blms.12964>.
- Exact result checked: Theorem 1.1 fixes one starting point and a finitely
  generated subgroup.  Part (i) writes the hitting-time set as finitely many
  arithmetic progressions together with a residual set of Banach density zero.
  Part (ii), when the rational self-map is regular, makes the residual set
  finite.  It does **not** say that the entire hitting-time set is finite.
- Boundary distinction: PC1 varies all initial points in `Gamma^2`, asks for
  consecutive coordinatewise survival for a fixed two-transition window, and
  allows finite rank without finite generation.  It is a uniform cardinality
  theorem, not a structure theorem for the return times of one orbit.
- Applicability caution: although `H` is polynomial on affine space, its
  restriction as a self-map of `G_m^2` is generally only rational because its
  first coordinate may vanish.  Bell--Ghioca's regular-map clause therefore
  cannot simply be imported for that restriction.
- Role here: arithmetic-dynamics boundary only.

## Recent cyclotomic Hénon rigidity

### Zhuchao Ji, Junyi Xie, and Geng-Rui Zhang (2025/2026)

- Work: *Cyclotomic integral points for affine dynamics*.
- Primary record: <https://arxiv.org/abs/2511.13443>.
- Version checked: v2, 2026-01-20.
- Exact result checked: Theorem 1.8 proves that the periodic points over the
  maximal cyclotomic extension `K^c` for the stated Hénon-type automorphisms are
  not Zariski dense.  Corollary 1.9 specializes the conclusion to plane
  polynomial automorphisms of positive entropy.
- Boundary distinction: those results concern cyclotomic integral points,
  density, and periodic/preperiodic dynamics.  Neither Theorem 1.8 nor
  Corollary 1.9 gives finiteness, a finite-rank subgroup bound, or a fixed-window
  cardinality.  PC1 concerns arbitrary
  finite-rank multiplicative subgroups and all initial points surviving two
  consecutive transitions, with an explicit cardinality bound.
- Role here: closest recent Hénon/torus boundary, not proof input.

## Recent semigroup integrality and multiplicative dependence

### Jorge Mello and Yu Yasufuku (2026)

- Work: *On higher dimensional integrality and multiplicative dependence in
  semigroup algebraic dynamics*.
- Primary record: <https://arxiv.org/abs/2604.03745>.
- Version checked: v1, submitted 2026-04-04.
- Exact conditional structure checked: Theorems 1.1--1.2 and Corollary 1.3 use
  the paper's `Hyp_epsilon` in the range
  `epsilon >= (1+c)/2`.  Theorem 4.2 together with Vojta is formulated only for
  sufficiently small `epsilon` and under additional divisor hypotheses.  For
  this source audit, that range/hypothesis mismatch is explicitly unresolved;
  the latter result is not treated as automatically discharging the former
  hypothesis in the range needed by Theorems 1.1--1.2.
- Boundary distinction: the setting is semigroup-orbit integrality and
  multiplicative dependence, with the conditional structure just recorded.  It
  does not give the unconditional fixed-window finite-rank Hénon count PC1 or
  the support-size dichotomy.
- Role here: current higher-dimensional boundary only.

## Recent rational periodic-point constructions for Hénon maps

### Hyeonggeun Kim, Holly Krieger, Mara-Ioana Postolache, and Vivian Szeto
(2024/2025)

- Work: *Hénon maps with many rational periodic points*.
- Primary record: <https://arxiv.org/abs/2412.01668>.
- Version checked: v2, 2025-07-08.
- Exact results checked: Theorem A constructs, for odd `d>2`, a rational Hénon
  map of degree at most `d` with at least `(d-4)^2` rational periodic points.
  Theorem B constructs, when `d` is congruent to `1` modulo `6`, an integer
  cycle of length `(8d+10)/3` for the stated Hénon construction.
- Boundary distinction: these are periodic-point lower-bound constructions for
  selected maps and parameter ranges; they are not bounds for all rational or
  integral periodic points.  PC1 is a coefficient-uniform upper bound on short torus
  survival and expressly makes no periodic-classification claim.
- Role here: Hénon arithmetic context and nonclaim boundary only.

## Direct-collision audit

No checked primary source states all of the following package:

1. `H(x,y)=(c+sum b_jx^(e_j)+ay,x)` with every displayed coefficient nonzero;
2. arbitrary characteristic-zero `K` and arbitrary finite-rank `Gamma<=K*`;
3. uniform finiteness already at `T_2` for every actual support size `s>=2`;
4. the explicit bound `d A(s+2,3r)+M(e)S_*`;
5. the exact contrast with support one, where `T_4` is uniformly finite but
   `T_3` may be infinite.

The bounded search therefore supports a provisional novelty decision.  It
does not establish priority, exhaust all languages or databases, or rule out
an unpublished or unindexed collision.

## Citation hygiene for a later manuscript

- Cite Amoroso--Viada at every first use of `A(q,R)` and state the algebraic-
  closure bridge.
- Cite ESS as a predecessor, not as the source of the displayed constant.
- Describe all other works as neighboring scope; do not imply that they prove
  any part of PC1--PC3.
- Do not collapse Bell--Ghioca's finite residual into finiteness of the entire
  hitting-time set, or treat a polynomial affine Hénon map as automatically a
  regular self-map of the torus.
- Do not turn Ji--Xie--Zhang non-density into finiteness, suppress the unresolved
  epsilon-range issue in the Mello--Yasufuku comparison, or generalize the
  degree/congruence ranges of the Kim et al. constructions.
- Keep arXiv version dates for the 2025--2026 works until a journal version is
  verified.
- Re-run the recent-literature search immediately before any manuscript source
  lock or submission decision.
