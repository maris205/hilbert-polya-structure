# C408 paper plan: alternating-zero local multiplicities

2026-09-06. Status: `OUTLINE_ACCEPTED_FOR_DRAFTING`.
This plan follows the coordinator's C408 admission in
[the complete proof review](../ROOT_CLUSTER_REVIEW.md). It does not assign a
new contract or alter the frozen round-2 papers. Mathematical inputs are the
admitted [proof package](PROOF_PACKAGE.md), its
[primary-source audit](SOURCE_AUDIT.md), and the completed controls recorded in
[COEFFICIENT_CHECKS.md](COEFFICIENT_CHECKS.md).

## One-sentence contribution

For every odd k >= 3 and every even clock n = 2m, determine the complete local
Artin length at every alternating-zero point of the unsaturated cyclic
exchange-relation algebra, including both adjacency-kernel resonances, and
sum these lengths into an explicit rational generating function.

## Audience, object, and ownership

Working title: **Alternating-zero local multiplicities in odd-power cyclic
exchange relations**. Anonymous mathematical research manuscript, C408;
no affiliation, human-review claim, submission venue, or arbitrary page target.
The mathematical article uses complete proofs in the body and three verified
primary references. A theorem table and two small control tables suffice;
there is no illustrative figure that would clarify the central proof.

The familiar alternating deep-point support belongs to Beyer--Muller. Ambient
rank-two cluster-surface singularities belong to
Benito--Faber--Mourtada--Schober. Birational dynamics of cluster mutation maps
is treated by Grigorev--Kalidindi--Quintero Santander--Roeder. None of these
background mechanisms is claimed as new. The increment is the nonreduced
local thickness of the *unsaturated finite cyclic relation algebra*. The
embedding-dimension obstruction will explicitly separate this object from
fixed schemes on a smooth cluster surface.

## Claim--evidence matrix

| Claim | Exact scope | Proof/evidence | Main-text location |
|---|---|---|---|
| Common local model | Both phases, every allowed root, all m | Unit-root implicit elimination and logarithm ideal equality | Section 3 |
| Subset decomposition | Nonreduced intersections, all subsets | Complete-intersection Cohen--Macaulay length additivity | Section 3 |
| Path weights 1, k-1, 2k-1 | Every path length | Hessian elimination; explicit cancelled coefficient r(k²-1)/2 or -23r | Section 4 |
| Cycle weights 1 or 4k+1 | Every m, including m=1,2 | Spectrum; period-four reduction; mixed and axis coefficients; four intersections | Section 5 |
| Full local length | Every odd k >= 3 and every m | Combine Sections 3--5, no interpolation | Theorem in Section 2; completion in Section 5 |
| Rational local-length series | Same local invariant, all m and native clocks | Labeled marked-separator double count and parity | Section 6 |
| Bounded corroboration | k=3,5,7 truncations; m<=8 words; six original-equation controls | Existing exact SymPy and independent Singular outputs | Section 7 |

## Narrative and section outline

1. **Introduction.** What: periodic exchange equations may retain nilpotent
   thickness at zero-coordinate points. Why: support alone and ambient
   cluster geometry do not determine this finite local algebra. So what:
   an all-clock formula isolates and computes one complete boundary stratum.
   Attribute support and ambient results immediately; preview the two
   resonance calculations without claiming a full boundary census.
2. **Cyclic relation algebras and the main theorem.** Define the unsaturated
   algebra, literal small-clock conventions, alternating support, common
   local length, path weights, cycle correction, and both rational series.
   Prove the elementary support count and finiteness; defer only the central
   theorem proof to the following self-contained sections.
3. **Formal reduction and intersection additivity.** Prove the completed
   logarithmic-gradient presentation, embedding dimension m, the general
   product-factor length lemma, and the exact reduction to path/cycle
   gradient colengths. State a formal elimination estimate with its proof
   so that later error-order claims can be checked directly.
4. **Path gradient colengths.** Treat even lengths, lengths 1 modulo 4, and
   lengths 3 modulo 4 separately. Give the complementary correction,
   endpoint check, residual orders, energy error, and the exceptional
   cubic unary term. No key calculation moves to an appendix.
5. **Cycle gradient colengths.** Include loop and double-edge Hessians;
   prove reduction from every m=4r to the four-cycle, graph-reflection
   symmetries, alpha=1/-8 and beta=(k²-2)/4/-5, and the four-term local
   intersection sum 4k+1. Finish the local-length theorem.
6. **Rational multiplicity-generating functions.** Prove the labeled
   separator identity, quartic D_k, the all-selected correction, and the
   native-clock parity formula. Call these multiplicity series, not
   Artin--Mazur zeta functions. Display the first four local lengths.
7. **Finite controls and limitations.** State exactly which checks completed,
   and that the direct k=3,m=4 standard-basis attempt was terminated without
   a result. Separate finite controls from the all-parameter proof. Explain
   other boundary supports, characteristic and parity exclusions, and the
   absent torus/fixed-scheme/ordinary-zeta identification.

The abstract will state the object, the run-weight/cycle formula and rational
series, then the precise boundary of interpretation. The conclusion is the
last paragraph of Section 7 rather than a duplicated section.

## Citation and verification plan

Use actual primary metadata for Beyer--Muller (published 2025, arXiv v1
Section 4/Corollary 4.6), Benito et al. (arXiv v2 Section 5/Theorem 5.2.3),
and Grigorev et al. (arXiv v2, 2026). Section numbering is version-qualified;
the references will link to those exact inspected versions. The first two
specified sections were fully read by author and coordinator. The third
provides bounded dynamical context, not a proof dependency. No padding with
unread references and no broad priority assertion.

Use `paper-plan` then `paper-write`: one source file per section, all symbols
defined before use, no fabricated experiments. Parent/local instructions
override their default ML venue, figure quota, external-model review, and
minimum-length suggestions. The current team reviews the outline and then
the full draft. Use `paper-compile` for a draft build in a newly created
temporary directory under /tmp, preserving its logs and reporting its exact
path. Final dual-build, all-page QA, evaluation, ledger and release remain
coordinator-owned. Do not alter or rerun the sealed round-2 payload.

## Internal outline review

The root coordinator read the complete plan and accepted its seven-section
structure. The review specifically retained the m=1 loop/m=2 double-edge
derivatives and the version-specific Beyer--Muller support locator. Three
references and no illustration were accepted. Unchanged completed controls
are not rerun merely to accompany the writing stage. Full-manuscript review
remains a separate pending gate.
