# C420 independent full-manuscript review — round 2

Date: 2026-09-08 UTC. This is the full review text of the current-team
AI-assisted reviewer who performed manuscript round 1. The reviewer is
not the C420 manuscript author and made no author-source edit in this
round. This is not an external paid-model response, human peer review,
editorial acceptance, or worldwide-priority certification.

## Verdict

**PASS. No must-fix mathematical or presentation issue was identified.**
The revised manuscript still proves the full fixed-coordinate all-level
classification. The two adopted optional improvements from round 1 are
actually present in the source and PDF. The documented decision to retain
the short final bibliography page is acceptable.

This is a second complete manuscript reading, not a diff-only check and
not a relabeling of a historical proof review. It closes the requested
second full-text review for the exact artifact identified below. It does
not certify a subsequent final PDF or complete the coordinator's fresh
same-input build pair, final-page inspection, formal evaluation, release,
or batch-wide checks. No venue criteria were supplied:
`criteria_binding_unavailable` and `NOT_CALIBRATED` remain applicable.
No numerical review score is fabricated.

## Exact artifact and actual inspection

The reviewed PDF is
`papers/C420_scattering_commutativity/builds/round1/main.pdf`, relative
to the research-batch directory. The `builds/` and `paper/` directories
are siblings.

- PDF: 18 pages, 428401 bytes, SHA256
  `9753a3262ce775b5c289a0870bf4694066cb778c1cd10ada267d4ac5f5e74512`.
- Thirteen-input manifest: `builds/round1/source_inputs.sha256`, SHA256
  `ba887f152fc9fe7ca9e69cf74f14a96332bcf04c998f6352786358a65acc147e`.
- Author response: `REVISION_ROUND1.md`, SHA256
  `10186939454c7ff6fb55517235949adccf6383b2c64551db4e4772da1c3aea08`.
- Final compiler log: SHA256
  `b88018dfd68b9c40bf8c34e5ad730fdab2860c30c00c6d56d63b604df711d9a8`.
- Final BibTeX log: SHA256
  `afe9cfc935b5bf838c0e354b33aa5de9f0181595e15536fdc65374dfe9dbbe95`.

All 13 live inputs passed the actual manifest check. Recursive comparison
of `paper/` and `builds/round1/source_snapshot/` found no difference.
Comparison of the baseline-polished and round-1 snapshots found exactly
two differing files: Sections 7 and 8. Both complete diffs were inspected.
The original baseline source snapshot and PDF remain separate.

I read all 1394 lines of the 13 actual TeX/BibTeX inputs anew:
`main.tex`, `math_commands.tex`, `references.bib`,
`figures/latex_includes.tex`, and each of sections 0 through 8, including
every proof and all table macros. I read the full 946-line extracted
PDF text. A fresh `pdftotext -layout` extraction from the reviewed PDF
compared byte-for-byte equal to that retained text. I rendered this PDF
at 100 dpi into a diagnostic temporary directory and opened every one
of its 18 page images, in batches 01–06, 07–12 and 13–18.

I also reread the complete 307-line round-1 manuscript review, the complete
49-line author response, and `BIBLIOGRAPHY_VERIFICATION.md`. For the
frozen contract I freshly reread `AS2_PROOF_INDEX.md`,
`AS2_PARITY_CRITERION.md`, and `AS2_REPAIRED_CRITERION.md` in full.
The general analytic, principal, phase-parity, scalar, nonauthor-review
and source-audit dependencies were read in full for round 1, as listed
in that review. I do not describe them as a second fresh full reading
here. The present mathematical judgment comes from rereading and
checking their arguments as actually typeset in the complete article.

## Round-1 disposition, checked in the revised article

### O1 — preparation disclosure: implemented and closed

Anchor: `paper/sections/8_scope.tex:31–37`; PDF page 17.

The stale description of a first compiled baseline has been replaced by
stage-neutral language separating formal review, release and
reproducibility records from mathematical claims. The AI-assistance
disclosure remains. The text still denies that internal review constitutes
human peer review, an editorial decision or worldwide-priority
certification. It does not say that an unfinished release or evaluation
gate has passed. The PDF carries this exact revised meaning.

The source SHA256 is
`86dcfa03cc35503071d3a1aab238bfdf3f47e10c7843084ae770d653c94f1286`.

### O2 — sentence-initial table reference: implemented and closed

Anchor: `paper/sections/7_boundary_levels.tex:3`; PDF page 15.

The command is now `\Cref{tab:boundary}`, and the rendered sentence
begins with capitalized “Table 4”. The target, table data, formulas and
theorems are unchanged. The source SHA256 is
`33d913a4377193b23dc242f6e7ed26d7ba279ef5495f08c4e43b1b64bd72a73f`.

### O3 — short final bibliography page: reasoned decline accepted

Anchors: `paper/main.tex:36–37`, `paper/references.bib:1–10`;
PDF pages 17–18; author response lines 18–20.

The complete Young entry remains on page 18. This was expressly optional
in round 1. No page quota has been imposed, all seven entries remain
readable, and preserving a complete bibliography is a sufficient reason
not to compress the article. I accept the recorded decline. This is
not an unresolved mandatory item or a mathematical defect.

## Fresh mathematical assessment of the full article

Section paths in this section are relative to `paper/`.

### 1. Statements, quantifiers and the original object

Anchors: `sections/0_abstract.tex:1–17`,
`sections/1_introduction.tex:11–55`,
`sections/2_fixed_cusp_blocks.tex:3–26`; PDF pages 1–3.

The abstract and the two main theorems agree. They concern all positive
integer levels, the full weight-zero trivial-nebentypus cusp space,
fixed width-one cusp coordinates, and every regular complex parameter
pair. Regularity is defined using the entries of the actual meromorphic
scattering matrix, not arbitrary factors in a calculation. The row
constant-term convention is explicit. No moving normalization or
principal-only substitute has entered the statement.

The level bounds are 9 at two, 3 at three and five, and 1 at all primes
at least seven. The modulo-five condition includes prime two when its
exponent is odd; the modulo-eight condition selects odd primes only.
The two extra congruences do not constrain even exponents. Level one
and the conductor-one character are expressly retained.

### 2. Complete fixed Fourier blocks and their normalization

Anchor: `sections/2_fixed_cusp_blocks.tex:28–190`;
PDF pages 3–5.

For a fixed cusp denominator, unique primitive inducing characters
exhaust the residue-group dual. The condition that their conductors
divide the cusp gcd is exactly the divisor-label condition used in
the Fourier rows. Thus the fixed transform is square and invertible
on every cusp, with no spectral powers hidden in its entries.

The local valuation calculation in the imported divisor sum gives
the ramified exponent `a + max(b,e-b)` and the unramified coefficient
`c^{|b-k|} p^{s(max(k,e-k)-|b-k|)}`. In particular, it has not dropped
the conductor factor or exchanged a character with its conjugate.
The descending row elimination gives `(1-z^2)^e`; generic invertibility
also covers exponent zero and the empty product.

The completion uses the equal-character trivial-nebentypus convention,
while its L-function involves the character square. The functional
equation is applied to incoming oldform data, not as an alleged fixed
similarity. Comparing outgoing cusp coefficients really identifies
the resulting block as a block of `T Phi_N(s) T^{-1}`. Real characters
contribute single sectors and nonreal conjugates paired sectors. No
nonprincipal cusp direction is omitted.

### 3. All-exponent principal basis, including the central channels

Anchor: `sections/3_principal_basis.tex:18–218`;
PDF pages 5–8.

The difference-channel identities follow by subtracting adjacent
columns and reversing the finite geometric sum. The comparison never
divides by a potentially zero finite sum. The even central totient
vector and both odd central vectors are explicitly supplied; their
reciprocal polynomial identities produce the stated eigenvalues.
The rational display of the odd polynomial introduces no additional
exclusion at `X^2=p`.

The boundary cases can be read directly from these formulas: for
exponent zero the matrix is the identity; for exponent one the two
sum/difference vectors have eigenvalues `(Y+1)/(X+1)` and
`(Y-1)/(X-1)`. These are algebraic checks of the printed formulas,
not a numerical experiment or substitute for the general proof.
The support and coordinate-sum arguments establish completeness for
every exponent, regardless of coincident eigenvalues.

The separate cusp-height calculation reproduces the width-one
incoming exponent. Its multiplicity normalization is a fixed diagonal
similarity in the stated row convention. The composite tensor formula
is correctly identified as a principal-sector statement and is not
used to infer full-family commutativity by itself.

### 4. Nonreal-square necessity at every containing level

Anchor: `sections/4_nonreal_square.tex:10–189`;
PDF pages 8–11.

The inducing primitive character, its conductor, and every missing
Euler prime are kept distinct from the primitive character whose
square is being studied. The functional equation is applied to the
primitive inducing character. At each missing prime the exact
reciprocal identity retains the numerator with exponent `2-2s`.
The remaining spectral factor is identical in the two conjugate
directions and cancels in their scalar ratio.

Commutativity of the paired block forces the displayed determinant
quotient to be constant. Its four incoming determinants have the
correct numerator/denominator orientation. The tensor determinant
power is integral, ramified contributions cancel, and the remaining
oldform factors are supported only at primes of the level. All stated
Dirichlet expansions converge absolutely in `Re(s)>1`, including
denominators involving `p^{2-2s}`. Normalization at positive real
infinity forces the resulting constant to be one.

At an outside-level prime the coefficient is exactly
`d (ell-1) (xi(ell)-bar(xi)(ell))`. A finite product at level primes
cannot contribute to that prime coefficient. The least-nonzero-index
uniqueness argument has the needed absolute-convergence control.
CRT supplies an integer coprime to the whole level with nonreal value;
one prime factor must also have nonreal value. This closes the
contradiction without a prime-density theorem or an assumption that
imprimitive factors mysteriously fail to cancel.

### 5. The exact odd-exponent phase obstruction and tensor assembly

Anchor: `sections/5_phase_parity.tex:7–226`;
PDF pages 11–14.

The reciprocal Gauss-sum ratios in a quartic paired sector are constants,
and the common meromorphic scalar is not identically zero. The block
diagonal transforms and the subsequent Walsh transform are all fixed.
Conjugating the character does not conjugate the complex parameter.
The resulting local factor satisfies the printed fixed phase identity,
with the two arguments of the principal family still having product p.

For real character values, and for imaginary character values at even
exponent, the residual phase matrix is the identity. At odd exponent
it is minus the identity on the left half-chain and plus the identity
on the right. It exchanges the two central eigenvectors with minus
signs. Their invariant two-dimensional block has the nonconstant ratio
`(p+X)(X-1)/((p-X)(X+1))`: the quadratic and linear coefficient tests
would otherwise force `p=1`. This proves a fixed-subspace obstruction,
not merely that a convenient moving basis fails.

The tensor lemma excludes cancellation between bad primes. Generic
invertibility gives a common regular invertible parameter. The tensor
multiplicative commutator equals the identity; partial traces make
every factor scalar. Determinant one restricts each scalar to a finite
root-of-unity set, and continuity near the diagonal forces it to be one.
Thus simultaneous odd imaginary phases cannot repair one another.
The proof does not require independence of prime logarithms.

The converse explicitly reassembles every real and quartic Fourier
sector. Meromorphic continuation is applied to the actual two-parameter
commutator, so removable singularities of intermediate inverses do not
exclude any regular pair. The necessity direction has the same scope.

### 6. Both directions of the arithmetic classification

Anchor: `sections/6_arithmetic.tex:4–95`; PDF pages 14–15.

The permitted primitive conductors are exactly those dividing the
square-root level M. Their characters exhaust its unit-group dual,
and the fourth-power condition is equivalent to unit-group exponent
dividing four. The odd prime-power groups and the small powers of two
give exactly the exponent bounds in the first theorem.

For a selected prime of odd exponent, the second condition uses only
the prime-to-that-prime part of M. Character separation yields
`p^2=1` in that unit group. Resolving its factors gives the conditional
congruences modulo five and sixteen, the latter written as the two
allowed classes modulo eight. CRT proves sufficiency as well as
necessity. There is no demand for nonzero character values at ramified
primes and no covert reintroduction of the false all-exponents repair.

### 7. Exact boundary examples and evidence scope

Anchor: `sections/7_boundary_levels.tex:8–99`; PDF pages 15–16.

The level-50 incoming matrices retain their factor `10^s`. The common
scattering scalar is converted by the primitive functional equation
before evaluation, so no separate zero-times-pole expression is used.
Absolute convergence and nonvanishing justify the scalar being nonzero
at 2 and 3, and both parameters are regular for the full matrix. The
two displayed rational values yield the diagonal commutator with entries
`384i/221` and `-384i/221`, multiplied by the nonzero common scalars.

At level 100 the apparent extra moduli two and ten introduce no new
primitive characters. The actual quartic unramified exponent is even,
and all remaining sectors are covered. Its positive conclusion is a
full-sector proof. The mixed even-power level is labeled a theorem
consequence. None of these statements relies on an expanded level
scan or a fresh mathematical-program execution.

## Source ownership, self-containedness and scientific limits

The current introduction, ownership table and Section 8 still credit
the classical scattering reconstruction, character-weighted cusp sums,
functional equations, squarefree channels and elementary unit-group
facts. The claimed residual remains one all-level classification.
The principal matrix lemma, arithmetic conversion and two small levels
are components, not independently asserted paper-sized discoveries.

All new central arguments required by the two main theorems are actually
typeset in the article. The source dossier is supporting provenance,
not a substitute for the principal proof, scalar obstruction, tensor
lemma, parity argument or arithmetic converse.

The source formulas and bibliography are unchanged by the revision.
The bounded primary reads executed during round 1 remain the source
verification for the sensitive imported formulas: Young v2, Sections
3.1–3.2, the completion and Proposition 4.2, and formulas (7.1)–(7.3);
Booker–Lee–Strombergsson v2, Section 2.7, Lemma 2.19 and Remark 2.20;
and DLMF 25.15.2, 25.15.4–25.15.6. See the linked
[Young primary text](https://arxiv.org/html/1710.03624v2),
[Booker–Lee–Strombergsson primary text](https://arxiv.org/html/1803.06016v2#S2.SS7),
and [DLMF formula section](https://dlmf.nist.gov/25.15).
This round made no fresh external source request and does not relabel
those earlier reads as new access or as full readings of those papers.

The unread Huxley chapter and unread dissertation portions remain
explicit limits. No conclusion about their lacking an equivalent result
is asserted. The squarefree result is properly deducted. The article
still denies that a spectral parameter is native chronological time or
that this classification supplies target Euler factors, a target root
number or a Hilbert–Polya realization. No zero correspondence is claimed. The
ordinary classical Euler factors used in the proof are not confused
with such an additional construction.

## PDF and build-log findings

Every current page was opened. The abstract, complete first theorem,
character criterion, all displayed matrices, polynomial calculations,
conjugation bars, parity table, arithmetic table and exact example are
legible. No clipped formula, overlapping item, broken cross-reference,
or missing glyph was found. The continuation of proofs across pages
does not omit content. The newly capitalized reference is visible on
page 15 and the new disclosure is visible on page 17. The sparse page
18 is the accepted optional bibliography-layout choice.

All 27 font rows are embedded Type 1 fonts with Unicode maps; no Type 3
font was found. A targeted scan of the final compiler and BibTeX logs
found no actual warning, error, undefined citation/reference, overfull
or underfull box. A broad case-insensitive search also encounters
harmless log vocabulary such as `file:line:error style messages enabled`
and BibTeX's `warning$ -- 0`; those are not compiler warnings. Literal
placeholder and stale-baseline searches found no match in the current
sources or extracted text.

For operational precision, the first manifest-check attempt was invoked
from `paper/`, although the manifest paths already start with `paper/`.
It therefore could not resolve the paths; the corrected check from the
C420 directory passed all 13 files. An initially overbroad diagnostic
placeholder regex was likewise replaced by a literal-pattern check.
Neither event changed a file, ran a mathematical test, or represents a
failed manuscript build. This reviewer inspected the existing round-1
build and did not run a new LaTeX compilation or reproducibility pair.

## Handoff

New critical findings: 0. New major findings: 0. New mandatory minor
findings: 0. Round-1 O1 and O2 are closed by verified edits; O3 is closed
by the accepted reasoned decline. No further author-source change is
requested for this review.

The coordinator may proceed to the final build and release workflow.
That workflow must attach its own actual final inputs, build-pair
comparison and final-PDF inspection; this PASS should remain bound to
the round-1 PDF hash above. A later mathematical source change would
require renewed substantive review.

The only persistent project file authored by this review is this report.
Diagnostic page images were generated in temporary storage. No C420
source, historical proof, shared registry, evaluator record, release
artifact or Git state was edited. No mathematical program, paid model,
external manuscript upload or notification was launched.
