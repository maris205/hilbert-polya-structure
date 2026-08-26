# Round 1 hostile review

## Provenance and scope

`independent cross-agent review; requested GPT-5.4 child unavailable due agent thread cap`

This is a cross-author audit: the reviewer did not author P67.  No model score
or external-review provenance is inferred.  The audit covers the complete
manuscript, proof package, claims/evidence ledger, bibliography and citation
audit, deterministic control code and frozen output, build instructions, and
round-0 QA artifacts.  The preserved baseline is
`main_round0_original.pdf`.

## Verdict

**MAJOR REVISION, with the principal theorem contract retained.**  The global
coordinate theorem, arbitrary finite-projection rank formula, cycle-space
description, Haar formulas, prefix count, and rectangle count all survive a
hostile proof reconstruction.  The round-0 manuscript nevertheless contains
one false matroid-deletion sentence, an overstatement about the logical
independence of the prefix pivot argument, an insufficiently explicit
definition of the represented coordinate matroid, and source-boundary gaps.
Those defects block use of the round-0 PDF as the reviewed manuscript.

External release remains **HOLD**.

## Theorem-by-theorem audit

1. **Root decomposition — PASS.**  For composite as well as prime coprime
   multipliers, maximal divisibility by the whole powers `a^i` and `b^j` is
   well-defined.  Coprimality ensures their product divides `n`; Euclid's
   lemma proves uniqueness of the residual root.
2. **Plaquette integration — PASS.**  Vanishing mixed difference makes each
   horizontal increment independent of the other exponent.  Telescoping gives
   `y_ij=y_i0+y_0j-y_00`; the converse is immediate in every characteristic.
3. **Global free-axis homeomorphism — PASS.**  The equivalence
   `ab | r a^i b^j` iff `i,j>=1` is valid under the stated root exclusions and
   coprimality.  The three-coordinate inverse is algebraic and coordinatewise
   continuous.
4. **Finite projection rank — PASS.**  For each root, the edge-value map from
   row and column potentials has one-dimensional kernel on every connected
   component, hence rank `|I|+|J|-c`.  Unused potentials can be extended
   arbitrarily, so there is no hidden global-extension obstruction.
5. **Cycle equations — PASS, with a presentation fix required.**  After a
   sign change on the column vertices, the map is a graph coboundary.  Forest
   integration plus fundamental cycles proves sufficiency.  The manuscript
   should say explicitly that simple cycles/fundamental cycles are meant.
6. **Coordinate matroid — PASS, with a definition fix required.**  The rows of
   the potential map represent restrictions of the coordinate evaluation
   functionals; equivalently they are the columns of its transpose.  After
   vertex-column rescaling, this transpose is an oriented incidence matrix.
   The result is the graphic matroid, but the ground-set representation must
   be stated to avoid confusing it with the dual matroid of linear
   constraints.
7. **Haar entropy and independence — PASS.**  Projection is a surjective
   homomorphism onto a finite subgroup, so Haar pushes to uniform counting
   measure.  Since each marginal is uniform, entropy deficit equals graph
   cycle rank.  Two distinct arithmetic coordinates are distinct edges in
   simple root-wise graphs and hence form a forest.
8. **Prefix formula — PASS; alternative proof wording is incomplete.**  The
   free-axis proof gives both the exact dimension and global extendability.
   The triangular row argument proves independence of the internally visible
   constraints, but by itself does not prove that every vector satisfying
   those internal rows extends to an infinite solution.  It is an independent
   rank consistency check only after the preceding extension theorem (or
   after a separate extension argument is added).
9. **Rectangle law — PASS.**  The incidence graph is `K_{M,N}`, with graphic
   rank `M+N-1` and cycle rank `(M-1)(N-1)`.
10. **Nonrectangular-shape commentary — FAIL AS WRITTEN.**  Deleting a cycle
    edge cannot raise projection dimension.  If the deleted edge belongs to a
    cycle, rank stays fixed and cycle rank falls by one; deleting a bridge
    lowers rank by one and leaves cycle rank fixed.

## CRITICAL issues

### C1. False deletion statement in the published mathematical narrative

Section 5 says that deleting an edge from a cycle “raises the projection
dimension by one.”  A coordinate deletion maps a projection to a smaller
coordinate set and cannot have that behavior.  In graphic-matroid terms,
deleting a non-coloop cycle edge preserves rank and lowers nullity by one;
deleting a bridge lowers rank by one and preserves nullity.  Replace the
paragraph with the exact deletion/addition dichotomy.

## MAJOR issues

### M1. Define the coordinate-dependence matroid on its actual ground set

State that the ground set is `F` and that a subset is independent when the
restricted coordinate evaluation maps `x -> x_n` are linearly independent in
the algebraic dual of `X_{a,b}` (equivalently, when the corresponding rows of
the finite potential matrix are independent).  This removes a possible
graphic/cographic ambiguity.

### M2. Repair the prefix pivot proof's logical claim

The pivot computation establishes the row rank of the internal constraint
matrix.  It does not, without the already-proved global extension theorem,
identify that local kernel with the infinite-system projection.  Recast it as
an independent rank cross-check that uses the preceding extension result, or
add a self-contained downward-closed extension proof.

### M3. Add the omitted direct multiplicative pattern-generation neighbor

The source ledger skips Ban--Hu--Lin's *Pattern generation problems arising
in multiplicative integer systems*, which directly treats pattern generation,
spatial entropy, and Minkowski dimensions in multiplicative systems.  It is a
closer source for the prefix-count neighborhood than the two currently cited
later papers and must be included in the literature subtraction.

Verified primary record:
<https://doi.org/10.1017/etds.2017.74>.

### M4. Cite the standard sources behind the two imported terms

The paper is self-contained, but it currently introduces “graphic matroid”
and “total correlation” without any standard source.  Add Whitney's original
matroid paper and Watanabe's multivariate-correlation paper, and say plainly
that the incidence-matrix representation and the entropy functional are
standard ingredients.  The paper-specific content is their arithmetic
pullback and exact specialization, not the general terminology.

Verified records:

- Whitney, *On the Abstract Properties of Linear Dependence*:
  <https://doi.org/10.2307/2371182>.
- Watanabe, *Information Theoretical Analysis of Multivariate Correlation*:
  <https://doi.org/10.1147/rd.41.0066>.

### M5. Remove ownership-sounding prose from the manuscript

Phrases such as “that work owns” and “those results own” sound like priority
adjudication.  Replace them with neutral statements of established scope.
The internal audit may track owner subtraction, but the article itself should
only delimit what it uses and what it does not claim.

## MINOR issues

1. Replace “a graphic-matroid basis is a spanning forest” by “a basis is a
   maximal spanning forest”; arbitrary forests are independent sets, not
   necessarily bases.
2. Use one notation for the Haar random vector (`Z_F`) throughout the theorem
   and proof.
3. Note explicitly that the incidence representation works over every field,
   so characteristic two changes signs but not the represented matroid.
4. The controls exercise prime fields only.  Keep the existing explicit
   statement that controls are regression evidence; do not imply direct
   computational coverage of non-prime finite fields.
5. Update the review ledger, state file, QA report, and hashes only after the
   two real rounds have completed; do not retain the round-0 “NOT RUN” status.

## Source and claim-boundary audit

The following primary records were rechecked on 25 August 2026:

- Kenyon--Peres--Solomyak, multiplicative-integer invariant symbolic sets and
  dimension/variational theory: <https://arxiv.org/abs/1102.5136> and
  <https://doi.org/10.1017/S0143385711000538>.
- Ban--Hu--Lin, pattern generation and spatial entropy for multiplicative
  systems: <https://doi.org/10.1017/etds.2017.74>.
- Ban--Hu--Lai, multidimensional multiplicative integer subshift entropy:
  <https://doi.org/10.1007/s10955-021-02703-7>.
- Ban--Hu--Lai--Liao, axial products, entropy, and surface entropy:
  <https://arxiv.org/abs/2402.19324> and
  <https://doi.org/10.1063/5.0280667>.
- Mora Cuellar--Rojas Aravena--Yavicoli, prescribed densities,
  prime-valuation random models, higher-order correlations, symbolic
  realizations, and mixing/ergodicity criteria:
  <https://arxiv.org/abs/2607.19525>.

These records support the manuscript's separation of multiplicative-system
frameworks, entropy theories, and valuation-coordinate correlations from its
finite-field calculation.  A bounded search status is not a universal
novelty finding.  The reviewed manuscript must continue to make no “first,”
worldwide novelty, or release-readiness claim.

## Required Round-1 fixes

1. Correct the false deletion/addition paragraph.
2. Define the coordinate-function matroid precisely and repair “basis”
   terminology.
3. Recast the prefix pivot lemma as a rank cross-check, with extension logic
   made explicit.
4. Add and cite Ban--Hu--Lin (2019), Whitney (1935), and Watanabe (1960), with
   verified metadata and adjusted scope prose.
5. Neutralize ownership-sounding language.
6. Synchronize the proof package, claims/evidence ledger, citation audit, and
   bilingual summary where affected.
7. Rerun deterministic controls and a clean four-pass LaTeX/BibTeX build;
   require zero undefined citations/references and no material box warnings.

