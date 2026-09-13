# Novelty Assessment

## Decision

**PROVISIONAL GO FOR SOURCE DESIGN; NOT A PRIORITY CLAIM.**

The bounded primary-source search through 2026-08-17 found no direct collision
for the exact theorem package.  The assessment is strongest for PC1: a
coefficient-uniform, explicit two-transition bound for genuinely sparse
generalized Hénon maps over arbitrary characteristic-zero fields and arbitrary
finite-rank multiplicative subgroups.  PC2 is a sharpness witness.  PC3 is an
absorbed predecessor result and is not presented as independently new.

## Separate assessments

| Axis | Assessment | Reason |
|---|---|---|
| Novelty | Provisional GO | No checked source combines the support-size jump, the `T_2` cardinality theorem, and the explicit degeneracy budget.  Search coverage is bounded, so this cannot become a global priority statement. |
| Standalone value | GO | PC1 has a clean hypothesis-to-bound statement, PC2 makes the window exact, and PC3 supplies the contrasting support-one regime with a complete reproduced proof. |
| Proof closure | GO subject to fresh source review | The author proof closes every nondegenerate and degenerate branch without computation.  The external dependency is isolated to one explicit unit-equation theorem and its algebraic-closure bridge. |

No numerical score is assigned: the relevant decision is whether each axis
clears its own gate, not an artificial average.

## What appears new

The conceptual contribution is not merely another application of a unit
equation.  It is the exact interaction between support size and the shortest
uniform escape window:

- for actual support `s>=2`, every first-local degeneracy is either a graph on
  which one coordinate is a genuinely multi-term sparse image, or a finite
  set of vertical fibers closed by the second recurrence;
- for support one, the analogous degeneracies admit the free words `BA`, `CB`,
  and then `CBA`, so four transitions are necessary and sufficient;
- the two regimes therefore have exact thresholds `T_2` and `T_4`, with
  explicit shorter-window counterexamples.

The explicit root/graph budget

`M(e)=2(2^s-1)+sum_{|J|>=2}(e_maxJ-e_minJ)+sum_{J nonempty}e_maxJ`

records the degeneration geometry instead of hiding it in an unspecified
constant.

## Closest literature and the remaining distance

| Literature lane | Genuine overlap | Missing from that lane |
|---|---|---|
| Amoroso--Viada; ESS | Quantitative nondegenerate unit equations in finite-rank torus groups. | Hénon recurrence, degenerate-subsum closure, support threshold, and sharp windows. |
| Krieger--Levin--Scherr--Tucker--Yasufuku--Zieve | Theorem 1.7 bounds `S`-unit images of monic `S`-integral polynomials; Theorem 1.8 and Corollary 1.9 handle a local exceptional-coefficient condition and its one-orbit number-field consequence. | Two-dimensional invertible recurrence, all initial torus states, arbitrary characteristic-zero fields and finite-rank groups, exact `T_2` bound, and four local degeneracy types. |
| Bell--Ghioca | Theorem 1.1 treats one fixed orbit and a finitely generated subgroup: arithmetic progressions plus a zero-Banach-density residual, made finite (not the whole set) for a regular map.  A Hénon restriction to `G_m^2` is generally rational, not automatically regular. | Varying all starting points, consecutive short-window survival, explicit cardinality, and finite-rank rather than finitely generated scope. |
| Ji--Xie--Zhang | In v2 (2026-01-20), Theorem 1.8 gives non-density of `K^c`-periodic points for the stated Hénon-type maps; Corollary 1.9 treats plane positive-entropy automorphisms. | Finiteness, arbitrary finite-rank groups, and a uniform finite-window count. |
| Mello--Yasufuku | Theorems 1.1--1.2 and Corollary 1.3 use `Hyp_epsilon` for `epsilon >= (1+c)/2`; Theorem 4.2 plus Vojta uses sufficiently small `epsilon` and extra divisor hypotheses, leaving a range/hypothesis mismatch for this comparison. | The unconditional Hénon theorem, local support automaton, and explicit bound. |
| Kim--Krieger--Postolache--Szeto | Theorem A gives at least `(d-4)^2` rational periodic points for odd `d>2` using degree at most `d`; Theorem B gives an integer cycle of length `(8d+10)/3` when `d=1 mod 6`. | Bounds for all rational/integral periodic points, torus-survival upper bounds, and the support-size threshold. |

## Direct-collision test

A direct collision would need to prove, at minimum, uniform finiteness of
`T_2` for every nonzero-coefficient `s>=2` sparse polynomial over arbitrary
characteristic-zero fields and finite-rank subgroups.  A result only about one
fixed orbit, roots of unity, number-field `S`-units, periodic points, density,
or nondegenerate unit equations is adjacent but not a collision.

No direct collision was located.  This conclusion must be rechecked before a
later source lock because the most relevant boundary papers include 2026
preprints.

## Standalone audit

The package is standalone for the following reasons:

1. The generalized Hénon normal form and `T_m` convention are fixed explicitly.
2. The sparse-image lemma is proved, including its degenerate subsums and
   torsion fibers.
3. The local tuple ranks are derived (`2r` and `3r`), rather than asserted.
4. The `Z/U/M_j` convention drives an exhaustive four-type proof.
5. Endpoint graphs `J=[s]` and `|J|=1`, vertical constant cancellation, and
   simultaneous zero subsums are handled explicitly.
6. The support-one A/B/C automaton and its free chains are fully reproduced.
7. Both threshold failures are direct infinite families.

The earlier support-one project is therefore provenance, not a logical
dependency.

## Novelty risks still requiring discipline

- A theorem phrased in a broader language of integral points on dynamical
  correspondences could imply PC1 without using the same terminology.
- Recent 2026 work may be revised after the freeze date.
- A general but non-explicit finiteness theorem would weaken the novelty of
  finiteness, while the explicit bound and exact window could remain distinct.
- Boundary results must not be strengthened in paraphrase: non-density is not
  finiteness, a finite residual is not a finite hitting-time set, conditional
  epsilon ranges cannot be merged, and selected Hénon constructions do not
  classify all rational or integral periodic points.
- The closed-form checksum for `M(e)` is not itself a novelty claim; the theorem
  uses the subset-sum definition.
- PC3 cannot be marketed as a parallel new result because it is absorbed from
  the hash-identified local predecessor.

## Absorption and no-parallel rule

The support-one predecessor has terminal-review SHA-256
`9cfb8b2cb492dc6bea84231a81c8f7b7c698eea5299a357d066339180b14260d`
and PDF SHA-256
`4e17ebdfec4aed386e57f0e5bb3b39a6f24ed6809db0fb379a598fe143041414`.
Paper16 absorbs its theorem and proof.  The predecessor must not be externally
submitted in parallel, and a later Paper16 manuscript must handle provenance
transparently.

## Claims excluded from the novelty decision

The assessment does not cover positive characteristic, zero constant term,
triangular maps with `a=0`, affine-conjugacy invariance, optimal constants,
effective enumeration, heights, periodic classification, arbitrary polynomial
automorphisms, or priority over unpublished work.
