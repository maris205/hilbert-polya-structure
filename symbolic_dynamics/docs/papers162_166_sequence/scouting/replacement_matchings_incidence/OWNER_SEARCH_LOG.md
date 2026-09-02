# Bounded owner-search log — matchings and incidence replacement lane

**Search date:** 2026-09-03 UTC  
**Boundary:** P1–P161 plus all visible P162–P166 exclusion ledgers  
**External state:** `HOLD_EXTERNAL`

This is an early hostile owner gate, not a systematic literature review,
novelty opinion, priority claim, or freedom-to-operate search.  Primary papers
and primary repository records were used to identify standard ingredients and
proof engines.  A query non-hit never contributes positive novelty evidence.

## Search strings used

The bounded pass used spelling, notation, and singular/plural variants of:

```text
perfect matching association scheme union alternating cycles coset type
number mth roots permutations explicit formula square root cycle type
composition two random fixed-point-free involutions cycle structure
product two fixed-point-free involutions factorization enumeration
Hurwitz action braid group factorizations symmetric group
graph operator exactly one common neighbor iteration
Boolean relation exactly one two-walk adjacency square
projective plane polarity graph subsets exact one neighbor
finite incidence structure subset operator threshold dynamics
set system private elements ordered family membership columns
```

## `M01 OMD`: decisive proof-engine collision

### Primary records inspected

- Srinivasan, “The perfect matching association scheme,” *Algebraic
  Combinatorics* 3 (2020), 559–591,
  [DOI 10.5802/alco.104](https://doi.org/10.5802/alco.104).  The orbital/coset
  type of a pair of perfect matchings is indexed by the partition whose parts
  are the half-lengths of their alternating union cycles.  This owns the
  matching-overlay coordinate used by the scout.
- Lugo, “The cycle structure of compositions of random involutions,”
  [arXiv:0911.3604](https://arxiv.org/abs/0911.3604).  The paper explicitly
  models products of fixed-point-free involutions by 2-regular alternating
  graphs and studies their cycle structure.  This is a direct structural
  owner for passing from two matchings to permutation cycles.
- Leaños, Moreno, and Rivera-Martínez, “On the number of mth roots of
  permutations,” *Australasian Journal of Combinatorics* 52 (2012), 41–54,
  [author preprint arXiv:1005.1531](https://arxiv.org/abs/1005.1531).  It gives
  explicit expressions and generating functions for numbers of permutation
  roots, including prime-power exponents.  This owns the generic inverse
  engine after the scout map is factored as a power map.
- Burnette, “Factoring permutations into the product of two involutions: a
  probabilistic, combinatorial, and analytic approach,” Drexel University PhD
  dissertation (2021),
  [institutional record](https://researchdiscovery.drexel.edu/esploro/outputs/doctoral/Factoring-permutations-into-the-product-of/991014632685504721).
  Its fixed-point-free factorization result records the even-multiplicity
  condition for every cycle length.  This is an additional control for the
  scout's matching-coset restriction.

### Exact reduction

For a fixed matching `F`, a state matching `M`, and `P=FM`, the proposed map
is

```text
T(M)=MFM=F P^2,
F T^t(M)=P^(2^t).
```

The equation is an isomorphism of the dynamical problem with repeated
squaring on the reversible coset of permutations `P` satisfying
`FPF=P^(-1)`.  Squaring a cycle of even length splits it into two cycles and
squaring an odd cycle preserves its length.  Conversely, permutation square
roots are assembled by leaving odd cycles single or pairing equal cycles;
the scout's factors `(2r)^j` are exactly the labelled interleavings/orientations
of those pairs.

Accordingly:

- the 2-adic transient is the ordinary cycle-splitting clock;
- the eventual period is the multiplicative order of 2 on odd cycle lengths;
- the even-part multiplicity image criterion is the square-root criterion;
- the every-target fibre product is a cyclewise permutation-root count; and
- all `T^ell` fixed counts reduce to `P^(2^ell)=P`.

No exact-title hit for the notation `M -> MFM` is needed.  The entire claimed
theorem package factors through an owned generic engine.  Decision:

```text
M01: KILL_GENERIC_PERMUTATION_SQUARE_ROOT_ENGINE
```

## `M02 HUR`: direct named action

Baumeister, Dyer, Stump, and Wegener, “A note on the transitive Hurwitz action
on decompositions of parabolic Coxeter elements,”
[arXiv:1402.2500](https://arxiv.org/abs/1402.2500), studies the braid-group
Hurwitz action on factorizations.  A standard Hurwitz generator sends

```text
(g,h) -> (h,h^(-1) g h).
```

Since a perfect matching is a fixed-point-free involution, `h^(-1)=h`, and
the scout's `(A,B)->(B,BAB)` is literally this generator.  Its singleton
fibres and period at most three in the tested rank do not supply any residual
axis.  Decision: `KILL_DIRECT_HURWITZ_ACTION`.

## Polarity and common-neighbour controls

- Tait and Timmons, “Independent sets in polarity graphs,”
  [arXiv:1601.05058](https://arxiv.org/abs/1601.05058), and Loucks and Timmons,
  “Triangle-free induced subgraphs of polarity graphs,”
  [arXiv:1703.06347](https://arxiv.org/abs/1703.06347), explicitly define a
  polarity graph through point–polar-line incidence.  This standard geometry
  receives zero credit in `S03`, `S04`, and `I03`.
- Boros, Gurvich, and Zverovich, “Friendship Two-Graphs,” *Graphs and
  Combinatorics* 26 (2010), 617–628,
  [DOI 10.1007/s00373-010-0914-0](https://doi.org/10.1007/s00373-010-0914-0),
  treats graphs in which pairs have exactly one common neighbour and records
  the adjacency-matrix equation for the two-colour analogue.  It does not
  appear to study the scout endofunction `G -> 1_{A(G)^2=1}`; this is recorded
  only as a bounded exact-map non-hit.
- Alipour and Tittmann, “Graph Operations and Neighborhood Polynomials,”
  [arXiv:1807.03971](https://arxiv.org/abs/1807.03971), is a nearby primary
  control on common-neighbour subsets under graph operations, not an owner of
  the iteration used here.

The non-hits do not rescue `R02`, `S03`, `S04`, or `I03`: their exact finite
signatures fail the independent all-parameter theorem-axis gate.

## Internal portfolio and within-lane collision audit

The following were decisive without relying on literature absence:

- `M03/M04` reduce the alternating components of two perfect matchings to a
  selected component subfamily in one step.  Their only clock is idempotence,
  and the component mechanism is directly adjacent to P130's matching
  component interface.
- `S01` and `S06` are conjugate.  Complement maps the 2-subsets of `[5]` to
  the 3-subsets; two 2-subsets are disjoint exactly when their complementary
  3-subsets intersect in one point.  `S06` is not counted as a distinct
  system in the 25-class total.
- `O01`–`O04` factor over ground elements into powers of a fixed finite map on
  membership columns.  This is the generic coordinate-product engine;
  `O04` additionally uses a cyclic-interval/necklace action.  Large target
  fibres arising by multiplication across columns are not independent mass.
- `H01/H02` erase the hypergraph to vertex-degree or pair-codegree summaries
  and collapse to a fixed point within depth two in the tested carrier.  This
  is a summary/retraction phenomenon, not a target-resolved inverse atlas.
- `R01`, `R03`, `R04`, `S01`–`S05`, and `I01`–`I06` have nontrivial small
  functional graphs, but no tested invariant predicts their period/depth
  strata across parameters and no every-target fibre law was found.  They are
  killed on theorem mass before novelty.
- The relation/matrix systems are nonlinear predicates, so the decision does
  not invoke the generic linear-map exclusion.  The rank-changing incidence
  systems are likewise not generic closure/core/pruning; they fail on their
  own signatures.

The repository-title/ledger sweep separately checked P1–P161 for matchings,
incidence, transversals, finite geometry, graph transforms, blockers,
partitions, and set systems.  Direct proximity was found to P130, P136, and
the P157–P161 scouting exclusions, as recorded above.  No absence is promoted
to a novelty statement.

## Final owner gate

```text
M01: DIRECT PROOF-ENGINE OWNER / KILL
M02: DIRECT NAMED-ACTION OWNER / KILL
M03-M04: INTERNAL COMPONENT-RETRACTION COLLISION / KILL
S06: WITHIN-LANE CONJUGATE DUPLICATE / KILL
all remaining systems: INSUFFICIENT TWO-AXIS THEOREM MASS / KILL
SURVIVOR: none
EXTERNAL: HOLD_EXTERNAL
```

