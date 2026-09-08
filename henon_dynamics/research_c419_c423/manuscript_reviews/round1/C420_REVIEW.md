# C420 independent full-manuscript review — round 1

Date: 2026-09-08 UTC. This is the complete review text produced by a
current-team AI-assisted manuscript reviewer, not an external-model response,
human peer review, acceptance decision, or worldwide-priority certification.
The reviewer did not edit the C420 manuscript. Historical proof reviews were
read as evidence to be checked, not adopted in place of reading the article.

## Verdict

**PASS for the mathematical manuscript, with no must-fix issue found and
three optional presentation items.** The article actually contains the
central proofs required by the frozen AS2 classification. Its statements
retain the full cusp space, fixed width-one coordinates, exponent parity,
imprimitive-square factors, and all regular parameter pairs.

This verdict applies to the exact baseline artifact below. It does not
complete round 2, bytewise reproducibility, release, formal evaluation or
batch checks. No venue rubric was supplied; `criteria_binding_unavailable`
and `NOT_CALIBRATED` apply. No numerical score is invented.

## Artifact and actual reading

The actual PDF is
`papers/C420_scattering_commutativity/builds/baseline_polished/main.pdf`:
`builds/` is a sibling of `paper/`, not a subdirectory of it.

- PDF: 18 pages, 428469 bytes, SHA256
  `08967fffb8542a60bdedc4142f2efd7149d26fb9057276bb6ab27fbcce5f10ff`.
- Input manifest: `builds/baseline_polished/source_inputs.sha256`, SHA256
  `9d94846bd6fe52a6a9c30e5a7385bd369c3aa8a767e5cd85a5a404a7d1003994`.
- All 13 live inputs passed the manifest check. A recursive comparison of
  `paper/` with the preserved `source_snapshot/` returned no difference.

Read all 13 actual TeX/Bib inputs in full: `main.tex`, `math_commands.tex`,
`references.bib`, `figures/latex_includes.tex`, and sections 0 through 8.
Read the complete 946-line extracted PDF text and opened all 18 retained
page images, in batches 01–06, 07–12 and 13–18. Thus this is not a review
of only the abstract, proof index, build receipt or author summary.

Read the complete AS2 proof-index dependencies:

- `arithmetic_spectral/AS2_PROOF_INDEX.md`;
- `arithmetic_spectral/independent_review/REPAIRED_CLASSIFICATION.md`;
- `arithmetic_spectral/oldform_review/PROOF_PACKAGE.md`;
- `arithmetic_spectral/oldform_review/TWIST_PARITY_LEMMA.md`;
- `arithmetic_spectral/independent_review/PROOF_PACKAGE.md`, including the
  imprimitive scalar lemma and the separate level-50 counterexample;
- `arithmetic_spectral/AS2_PARITY_CRITERION.md`;
- `arithmetic_spectral/AS2_REPAIRED_CRITERION.md`, including its explicit
  finite-group facts and the status of the false first repair;
- `arithmetic_spectral/non_author_review/REVIEW.md`;
- `arithmetic_spectral/non_author_review/SOURCE_SUBSTANCE_AUDIT.md`;
- `arithmetic_spectral/AS2_SOURCE_AUDIT.md`.

Also read the C420 `COMPILE_REPORT.md` and
`BIBLIOGRAPHY_VERIFICATION.md`. Their checks were not silently relabelled
as checks newly executed by this reviewer.

## Must-fix findings

None identified. In particular, no new computation, theorem weakening,
extra exception, or omitted-proof appendix is requested.

## Mathematical findings and precise manuscript anchors

All section paths below are relative to the C420 `paper/` directory.

### R1. The two main statements preserve the actual contract

Anchors: `sections/1_introduction.tex:11–55` and
`sections/6_arithmetic.tex:64–95`; PDF pages 1–2 and 15.

The definition of regularity concerns the actual meromorphic matrix,
not the denominators of a chosen factorization. The theorem quantifies
over every positive integer and every regular complex parameter pair.
The prime bounds are exactly 9, 3, 3 and 1 in the stated cases. Clause 2
does include prime two when its exponent is odd. Clause 3 applies only
to odd primes. Neither congruence is imposed at even exponents, and
the conductor-one character and level one are included.

The abstract and both tables describing the classification agree with
these quantifiers. The article has not replaced either failed earlier
criterion with an unlabeled apparent proof of it.

### R2. The full cusp decomposition really is a fixed similarity

Anchors: `sections/2_fixed_cusp_blocks.tex:28–59,87–135,137–190`;
PDF pages 3–5.

For each denominator, unique primitive inducing characters exhaust the
entire finite residue-group dual. The equivalence between the conductor
dividing the cusp gcd and the divisor labels gives all rows, including
the nonprincipal rows. The Fourier matrix has no spectral powers.

The divisor-sum valuation calculation correctly retains the conductor
power in ramified factors and the absolute-distance phase in unramified
ones. Descending row elimination gives generic invertibility, including
the empty and exponent-zero cases. Comparing outgoing coefficients of
the functional equation identifies the displayed blocks as blocks of
the original row-convention scattering matrix. The parameter-dependent
incoming matrices are never substituted for a fixed similarity. A real
character contributes one block, not two artificial conjugate copies.

### R3. The principal lemma supplies a complete all-exponent basis

Anchors: `sections/3_principal_basis.tex:24–175,177–218`;
PDF pages 5–8.

The left/right column differences produce the displayed geometric sums
and generalized eigenvalue identities without division by a vanishing
finite sum. The reciprocal polynomial identities give the even central
channel and both odd central channels, with the cases zero and one
included. Clearing the rational presentation of the odd polynomial does
not introduce an exception at the square-root parameter.

The support and coordinate-sum arguments show independence of all
displayed vectors; coincident eigenvalues do not undermine the basis.
The width-one cusp-height calculation reproduces the stated exponent.
The cusp multiplicity normalization is fixed and its left/right factors
agree with the row convention. The composite tensor statement is
expressly restricted to the principal sector, so it is not used to
discard a nonprincipal obstruction.

### R4. Nonreal-square necessity survives larger levels and imprimitive squares

Anchors: `sections/4_nonreal_square.tex:10–99,103–189`;
PDF pages 8–11.

The proof applies the primitive functional equation to the character
inducing the square, not to a possibly imprimitive square. The missing
Euler factors are carried through the exact identity and both products
in the normalized scalar. The remaining parameter-dependent factor is
the same for the two conjugate directions and really cancels.

The determinant quotient has the correct four incoming determinants.
The tensor determinant exponent is an integer. Ramified factors cancel;
all phase-sensitive oldform factors remain supported at level primes.
Their rational expansions, and those of the scalar quotient, converge
absolutely in the stated half-plane. After normalization at positive
real infinity, constancy forces the series to be one.

At a prime outside the level the coefficient is exactly the oldform
dimension times the prime-minus-one factor times the difference of the
two conjugate character values. No level-prime factor can contribute to
that coefficient. The least-index uniqueness argument has the required
absolute-convergence tail control. Finally CRT produces an integer
coprime to the entire level with nonreal value; a prime factor of that
integer supplies the contradiction. No density-of-primes assertion or
unsupported noncancellation premise is hidden here.

### R5. The phase obstruction has exactly the claimed parity boundary

Anchors: `sections/5_phase_parity.tex:34–96,98–185`;
PDF pages 11–13.

For a quartic pair, the reciprocal Gauss ratios are constants, the
common scalar is not identically zero, and both block transformations
are fixed. Replacing the character by its conjugate does not conjugate
the spectral parameter. The resulting local identity uses fixed
diagonal matrices and arguments whose product remains the prime.

The residual phase is the identity for real phases and for imaginary
phases at even exponent. At odd exponent it acts with opposite signs
on the half chains and exchanges the two central eigenvectors with
minus signs. The off-diagonal ratio is nonconstant: quadratic and
linear coefficient comparisons would otherwise force the prime to be
one. This is a fixed invariant two-dimensional obstruction, not a
failure of a chosen moving eigenbasis. Real-character sectors are also
proved commuting for arbitrary oldform exponents.

### R6. Tensor cancellation and exceptional regular parameters are closed

Anchors: `sections/5_phase_parity.tex:7–32,188–226`;
PDF pages 11 and 13–14.

The tensor lemma uses generic invertibility at a common parameter.
The tensor multiplicative commutator identity gives nonzero traces;
partial traces make each factor scalar. Determinant one and continuity
in a connected neighborhood of the diagonal force the scalar to be
one. Thus scalar anticommutation or cancellation between two bad primes
is not an escape. No independence of prime logarithms is needed.

The converse reassembles every fixed Fourier block. Meromorphic
continuation is explicitly applied to the actual commutator in two
parameters, including removable singularities introduced by intermediate
inverses or scalar quotients. Necessity has the same full parameter scope.

### R7. The arithmetic conversion has both directions and the correct prime exclusions

Anchors: `sections/6_arithmetic.tex:4–95`; PDF pages 14–15.

Characters with permitted primitive conductors constitute the complete
dual of the square-root level's unit group. The fourth-power condition
is exactly the unit-group exponent condition, giving the stated
prime-power bounds. The second test uses the prime-to-the-selected-prime
part of that level. Character separation yields the square congruence
only for a selected prime of odd exponent.

Resolving the remaining factors modulo five and sixteen produces the
displayed modulo-five and modulo-eight clauses. CRT proves sufficiency
as well as necessity. No nonzero character value is demanded at a
ramified prime. This matches the final parity-sensitive proof rather
than the false all-exponents first repair.

### R8. Levels 50 and 100 are exact controls of different directions

Anchors: `sections/7_boundary_levels.tex:8–99`; PDF pages 15–16.

The level-50 proof keeps its actual conductor normalization and common
scalar. The primitive functional equation makes that scalar regular
and nonzero at parameters 2 and 3, avoiding a separate zero-times-pole
evaluation. The displayed rational values give the stated diagonal
commutator with entries plus/minus 384i/221. Holomorphy in the convergence
half-plane makes both parameters regular for the full matrix.

At level 100 the apparent moduli two and ten introduce no new primitive
characters. All actual sectors are covered, and the quartic factor at
prime two has even exponent. Its commutativity is proved, not inferred
from a parameter grid. The mixed even-power example is clearly labeled
a theorem consequence. No old numerical or exact-check program was run
for this review.

## Sources, ownership and article scope

Fresh bounded primary access checked the relevant mathematical locators:

- Young v2: definitions in Sections 3.1–3.2, the completion before
  Proposition 4.1, Proposition 4.2/(4.6), and the hypotheses and actual
  formulas (7.1)–(7.3). The conjugation, equal-character trivial
  nebentypus convention, divisor weights and fixed Fourier sums agree
  with the manuscript. [Primary text](https://arxiv.org/html/1710.03624v2).
- Booker–Lee–Strömbergsson v2: Section 2.7, Lemma 2.19 and Remark 2.20
  confirm the independent ordinary-group coefficient formula and its
  relation to Young. The principal factor-two comparison is correct;
  no extended-group parity restriction is imported.
  [Primary text](https://arxiv.org/html/1803.06016v2#S2.SS7).
- DLMF: equations 25.15.2 and 25.15.4–25.15.6 support nonvanishing,
  missing factors and the primitive scalar identities. The homepage
  confirms version 1.2.7, released 2026-06-15, agreeing with the BibTeX
  entry. [Formula section](https://dlmf.nist.gov/25.15),
  [version record](https://dlmf.nist.gov/).

These were direct opens/finds, not a new broad priority search. Other
bibliographic checks remain the accurately bounded author/source-audit
receipts. This reviewer does not claim a fresh full reading of Huxley,
Keil, Cakoni–Chanillo or Levitin–Strohmaier. In particular the unread
Huxley chapter and unread dissertation portions remain genuine limits.

The introduction, ownership table and Section 8 deduct the classical
reconstruction and squarefree channels. The residual is one all-level
classification, not separate admissions for the principal lemma, group
calculation or two examples. The article explicitly disclaims turning
the spectral parameter into native time or deriving target Euler factors,
root numbers or a Hilbert–Pólya realization. Those boundaries must remain.

## PDF and presentation findings

The 18 pages have readable equations, tables, bars, indices and matrix
entries; no clipping, overlap or unresolved reference was found. The
existing final log has no matches for `Warning`, `Overfull`, `Underfull`,
`undefined` or `Error`. All 27 font rows are embedded Type 1 fonts with
Unicode maps; no Type 3 font was found. These checks inspect the existing
build and do not claim a fresh compilation or reproducibility test.

### O1. Optional: make the preparation disclosure stage-neutral

Anchor: `sections/8_scope.tex:31–38`, PDF page 17.

The statement that this is the first compiled baseline is accurate for
the reviewed artifact, but would become stale if carried unchanged into
the final post-review draft. For the eventual release, replace only that
stage-specific sentence with wording such as: “Formal review, release
and reproducibility records are maintained separately from the
mathematical claims.” Preserve the AI-assistance disclosure, internal
review limitation and lack of human/editorial certification. This is
not a mathematical defect, and it must not assert gates as completed
before their actual completion. The coordinator independently flagged
the same artifact-consistency concern.

### O2. Optional: capitalize the opening cross-reference in Section 7

Anchor: `sections/7_boundary_levels.tex:3`, PDF page 15.

The sentence currently begins with lowercase “table 4”. Change the
sentence-initial `\cref{tab:boundary}` to `\Cref{tab:boundary}`. This is
a one-token typographic fix with no mathematical consequence.

### O3. Optional: avoid the nearly empty final bibliography page

Anchor: `main.tex:36–37`, `references.bib:1–10`; PDF pages 17–18.

The final Young entry alone occupies page 18. If desired, use a small
local bibliography-spacing or preceding-paragraph adjustment and inspect
the result. Do not delete a source, reduce proof content, impose an
invented page limit, or globally shrink mathematical text to save this
page. Retaining the current readable 18-page layout is acceptable.

## Handoff

No mandatory correction is open. The coordinator may accept or decline
the optional items. Any author changes require a fresh versioned build
and an exact response record; they do not themselves constitute the
second independent full-text review. This review wrote only this file.
It did not alter C420 sources, historical proofs, shared registries,
release artifacts, evaluator records or Git state, and did not launch
mathematical computations, paid models or external manuscript uploads.
