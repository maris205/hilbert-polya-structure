# C419 — second full-manuscript review and revision verification

2026-09-08 UTC. Reviewer: the current-team spectral-lane agent,
not the C419 manuscript author or the original M1 proof author.
This is a different nonauthor reviewer from the first manuscript
round. Prior exposure to the batch and its planning is disclosed;
this is not blind review or an assertion of independent error
processes between members of the same AI-assisted team.

## Verdict

**PASS for the second full-manuscript review. All three adopted
round-one optional suggestions are addressed. Remaining mandatory
scientific corrections: zero. New revision requests: none.**

The current manuscript contains the complete direction-sensitive
integer exhaustion, positive-word realization, exact level
intersection argument, ordinary-cycle classifier and two-sided
proper-escape proof. Reading the entire revised manuscript and
actual revised PDF revealed no new mathematical gap, lost case,
unsupported strengthening or transcription regression.

The first review already had zero mandatory corrections. Its three
optional items were presentation and precision improvements, not
repairs to false theorems; this report preserves that distinction.
No additional flaw, revision or numerical improvement is invented
to make the second round appear more substantial.

This is an internal AI-assisted nonauthor manuscript review, not
human peer review, an external GPT-5.4 invocation, worldwide-priority
certification, a calibrated acceptance score or a final-release
certificate. Final identical-input builds, all-final-page visual
inspection, evaluation, archiving and sealing remain separate
coordinator-owned gates. This report requests no further author edit.

## Exact input and complete reading scope

Unless qualified otherwise, manuscript paths below are relative to
papers/C419_positive_trace_words/ under research_c419_c423/.

The actual review PDF was builds/round1/main.pdf, not the older
author-polished PDF. Its identity was independently checked:

| Artifact | Actual bytes / pages | SHA-256 |
| --- | --- | --- |
| builds/round1/main.pdf | 346150 / 11 | eaeee202c03e9b25c67a53c98199027297f96fe64baf670f235a249d5a41215d |
| builds/author_polished/main.pdf | Preserved earlier PDF | ed7db89ae850acb7530c11c703359faaee15f8dd3d4fe7e4a4ae2c59cb3146a0 |
| REVISION_ROUND1.md | Complete 43-line response read | 11ab0b43f552eeccf406bcd3da27c83f088991353b2870540884255ea636d294 |
| ../../manuscript_reviews/round1/C419_REVIEW.md | Complete 399-line report reread | 52a775d5cbfa00d282682a877a4c76ed0b464a0e9748cd44824963a08e8d50e6 |

All fourteen current production TeX/Bib files were read fully,
totaling 884 lines: master, macros, bibliography, all nine sections
and both separate table files. This includes the invariant-form and
low-level tables written inline in Section 5. The complete PDF text
was newly extracted directly to standard output in page groups 1–6
and 7–11 and read through the last bibliography entry. The source
review was not restricted to the three edited files or replaced by
the first-round PASS.

The complete PAPER_PLAN.md, SOURCES_AND_EVIDENCE.md and supplement
README were also read. The 526-line original PROOF_PACKAGE.md,
235-line original SOURCE_AUDIT.md, 52-line original CHECK_RECEIPT.md,
131-line current REVIEW_PROOF_AND_INCREMENT.md and 91-line current
source audit were read in full. Both copied implementation files
(126 and 130 lines) and the 52-line relocated receipt were fully
read without execution. These reads support the specific checks
below; reading an audit is not represented as freshly reading all
of the external papers mentioned by that audit.

### Reviewed production-source manifest

All fourteen live inputs are byte-identical to the corresponding
files in snapshots/round1/. A recursive comparison against
snapshots/author_polished/ shows exactly the three documented
changed files and no other source change. The complete revised
manifest is:

| Input | SHA-256 |
| --- | --- |
| main.tex | e034a05eb06d2643847b55c4068bf1635ed477c124e1fb4a44913e28be5ee7c5 |
| math_commands.tex | cda6d69f13969136256cefea61a9c69023c9c8e50b9b5565375fe1c71e378e40 |
| references.bib | d2df438c5200ecb51cd11b3571738395de6c7bc186baf0341c4b4ebcf2e89e65 |
| sections/0_abstract.tex | f35554fd5f9c05ab52c57c8483de1ec5761d9ed0f693152770e5fd2551bfbb20 |
| sections/1_introduction.tex | 7e6b6400379c69f5fb97d7a89ec61cc389641d76b7f1ac65b1b37eeb3959bc3f |
| sections/2_conventions.tex | 051a29e706f17c0969200a6dfca242499c2b4724ca9c948c7ad41eda8409dfbc |
| sections/3_escape_descent.tex | 6d3334dec931822dcdca9c2f33fc7a02c6c9078f406d714bf99e36ade5627de7 |
| sections/4_locus.tex | 30846f2d9d58627b715537c5702d04c958aa798b51ce332a2995fa0c61056cd6 |
| sections/5_levels.tex | 931591e142cfecf5de455749ece415985abbb69c78293c49d88ad688cf906acc |
| sections/6_classifier.tex | c5816cba44b783daeaa9b025c04ea58aad97db266261f6ce6ad57dd357751fd2 |
| sections/7_two_sided.tex | e41b725037c37856f394c7b56179789db0fcb32ac3a92296ac90c7287b3dc0f1 |
| sections/8_scope.tex | a36f96984547cdfe8779ef117b98718e1eef42104c809cf86f8e3ecf4a805b6c |
| tables/realize.tex | 3c42ac44ce77355dba5407b9d2c91c9912d7877daa978446ad5e4ef9cf23be75 |
| tables/source_scope.tex | 6b0899d3a699a0012a96b461751effd969876b1b32e744cb8cf408911dad752f |

## Verification of the first-round optional items

| Item | Checked evidence | Second-round disposition |
| --- | --- | --- |
| O1: keep equation (4.2) with its predicate/conclusion, or prevent the next-section table from separating that material | sections/4_locus.tex has the local samepage group. The actual revised page 7 places the whole premise, equation (4.2), predicate and proof conclusion together below Table 3. Current page images 6 and 7 were personally viewed. | Addressed by the first stated alternative. Table 3 still floats above the paragraph; neither the author nor this report claims that all such floating was prohibited. |
| O2: state the pairwise level-family assertion explicitly | Lemma 5.1 now says the families are pairwise disjoint above four. All three pairwise factorization arguments remain present in both source and PDF. | Addressed; the strengthened clarity matches the already existing proof. |
| O3: identify the inaccessible period-two-curve follow-up | Section 8 now names Humphries–Manning (2015), Curves of period two points for trace maps. The primary-metadata provenance recorded in the original source audit was reread; the revised PDF text continues the sentence across pages 10–11. | Addressed. Identification does not turn unavailable theorem text into inspected evidence, and that limitation remains explicit. |

None of these changes alters a displayed mathematical formula,
proof branch, classifier implementation, cited theorem dependency
or word quantifier. The actual snapshot diff agrees with the author
response rather than merely being inferred from it.

## Full mathematical re-audit

### Quantifiers, coordinates and clocks

The maps are full-trace polynomial automorphisms with the displayed
integer polynomial inverses, and both preserve
K = x^2 + y^2 + z^2 - xyz. The exchange J genuinely interchanges
the two maps and their first/second-coordinate cases.

The word convention is consistently chronological: for
w = l_1 ... l_s, W = l_s composed with ... composed with l_1.
Both letters must occur. Ordinary time means one W application.
The reversed product of exponent matrices and forward product of
point-indexed row-action matrices have their distinct conventions
stated, so the order difference is not a transcription mistake.
The matrix trace argument yields positive reciprocal eigenvalues
for an admissible matrix, not uniform hyperbolicity of every orbit
on a real level surface.

The locus is existential over admissible words: every listed point
is fixed by some such word, and every point periodic for any one
word is listed. It is not a claim that every candidate is periodic
for every word, nor that a finite whole-group-orbit theorem has
classified a specified word's periodic points.

### Common cone and complete integral descent

The proof includes the integer boundary, not only strict
large-coordinate inequalities. In the common cone, the third
modulus after A is ac-b >= c. Equality forces a=2 and b=c.
A bounded integer sequence would eventually plateau there, but
the next B occurrence gives c^2-2>c because c>2. Thus the argument
establishes a limit to infinity for repeated admissible schedules,
not merely an unbounded subsequence. The conjugate B case is exact.

The all-large descent explicitly covers negative product,
third-coordinate maximum, a tie between the first two maxima,
strict first-coordinate maximum and its conjugate. For a strict
first maximum and the permitted B direction, d=bc-a is divided
into all four ranges. In particular d<=-2 is correctly excluded
because the next phase has negative product and the following
letter enters the cone; it is not falsely called an immediate
descent. The possible image with all moduli two is excluded by
invariance and bijectivity of E. In the surviving all-large case
the integer maximum strictly decreases.

The small-set exit inequality is strict at |x|=|z|=2 and
|y|<=1, as needed. Expanding an ordinary periodic word orbit into
all letter phases is essential: the cone and one-way small-set
argument force every phase outside E to remain in S. The inverse
formulas then exclude a phase whose sole small coordinate is the
third. No endpoint-only argument has been substituted here.

### Exactly 39 lines and the converse realization

At a small fixed first coordinate c in {-1,0,1}, the printed
2-by-2 matrices have orders dividing 4, 6 and 3. Their finite
coordinate lists give the stated obstruction at the next B.
This produces the two direction-sensitive slanted families in
addition to the 27 axis-parallel lines; it does not produce a
third six-line slanted family. The unique-small-second case
follows through J. The four exceptional signed all-two points
are kept separately.

All five rows of the realization table agree with direct symbolic
substitution in the free parameter. A^12 and B^12 are identities
on the required small-coordinate planes. With
F = B^12 composed with A^12, the image G^r(P) has its first two
coordinates small, and the coordinate preserved by G is small
already on the original line. Consequently
G^(12-r) composed with F composed with G^r fixes the entire line.
This is a positive word containing both letters even when r=0.
The squares of the two letter actions on E give the separate
pointwise realization. The proof is not based on interpolation
at finitely many parameter values.

### All levels and the candidate bound

The two invariant restrictions are algebraically quadratic on
the stated parametrizations. Counting their forms gives
3, 16 and 20 lines for t^2, t^2+1 and t^2-t+2, allowing parameter
sign reversal. The three pairwise comparisons have only common
levels 1, 4 and 2 respectively. The signed factor pairs of 1,
-7 and -3 cover negative parameters as well.

Above level four, only one form family is active, giving the
respective candidate bounds 6, 32 and 40. At low levels, the
absolute-coordinate patterns and signs in Table 4 are disjoint:
the cardinalities at 0, 1, 2 and 4 are 1, 6, 16 and 26. The
last count includes E exactly once. Negative levels and level
three are excluded by the forms, not by a search radius.

The discriminant test includes zero discriminants and parity
of both candidate numerators. Substitution on all 39 lines,
pointwise deduplication and addition of E only at k=4 establish
the exact finite X_k. The manuscript consistently treats 40 as
a universal candidate bound and hence a least-period upper
bound, not as an attained 40-cycle or a proved optimal period.

### Exact ordinary-cycle classification and zeta

Each restricted letter is a partial injection. A word transition
is retained only if every intermediate point remains in X_k.
The periodic cover already proved for all phases makes this
restriction complete for genuine periodic orbits. Conversely,
a cycle of the partial word map is an actual ordinary W-cycle
with the same distinct vertices and least period.

Chains cannot enter cycles in a partial injection, since the
joining vertex would have two predecessors. This justifies the
implementation's global used set and chain disposal. Cycle
identification is only by cyclic rotation, not by reversal.
Pointwise treatment handles intersections of affine lines and
does not assume a generic line return fixes its parameter.

The trace counts, finite cycle product and determinant are
standard consequences on this proved state space. Nilpotent
chain blocks contribute determinant one, a d-cycle contributes
1-u^d, and an empty state space gives both zeta and determinant
one. They are formal-power-series identities and rational
functions of the ordinary word clock; no target Euler factor
or arithmetic zero identification is inferred.

### Forward and backward proper escape

The forward proof does not assume backward recurrence. A
cone-free trajectory eventually remains in S. After another
letter the sole-small-third configuration is impossible, and
the next occurrence of the other letter gives exactly the
same finite-rotation obstruction used in the periodic cover.
Thus all sufficiently late phases lie in D at one fixed level,
so the ordinary forward orbit is eventually finite. Applying
the inverse iterate to a repeated pair makes the original
point periodic. This closes the nonperiodic proper-escape
dichotomy without a hidden bounded-orbit premise.

The involution R(x,y,z)=(x,y,xy-z) conjugates each letter to
its inverse. The manuscript correctly uses the reversed word
U in W^(-1)=RUR; it does not commute A and B. The explicit
bound on Q when R(Q) has norm at most M proves properness of
R on the integer lattice. Applying forward escape to R(P)
under U and then properness proves the backward limit.

### Separating examples and the supported increment

A^6 composed with B^6 fixes (1,1,m), while A composed with B
sends it to (m,m-1,m^2-m-1), in the common cone for m>=3.
This establishes the whole-group/single-word distinction by
an actual calculation. The chronological word ABB has the
printed four distinct points for every nonzero m and level
m^2+1. The restriction |m|>=2 correctly removes the low-level
overlap when comparing with the predecessor families.

Its exponent matrix has trace four, unlike even positive
Fibonacci-matrix powers with traces 3, 7, 18, ...; odd powers
have determinant minus one. These are valid separation tests,
not by themselves a worldwide novelty proof. The stronger
content remains the complete all-word integer classification,
whose proof is present in the article.

## Supplement, historical evidence and source boundaries

The original proof and source records checked in this round have
the following identities. The first three are in
henon_dynamics/continuation_c414_c418_round2/mapping_class/;
the next two are in research_c419_c423/mapping_class_review/.

| Supporting artifact | SHA-256 |
| --- | --- |
| Original PROOF_PACKAGE.md | 619172d8a1d9a99015917069df6fe9d648a689dd680b4bd8bf6e05962628409e |
| Original SOURCE_AUDIT.md | 8699961aac4b7d73138ff72263a8041418a8963f5482bd13fac75df50ec9854e |
| Original CHECK_RECEIPT.md | 0843ee15f81b610b39e637ecaa1d1e6f5fd6c698e460b821e55dd13bd8043625 |
| Current REVIEW_PROOF_AND_INCREMENT.md | 86ad170b5b968037a320950530ffcbc7dcc3ce14133bdcb6cd3c5969a883c434 |
| Current SOURCE_AUDIT.md | cf4ad25b70487d60eaa4daf0d1c80c349d3be33c6e39ccb3476eb7e0f02fc6d3 |
| supplement/classify_word.py | 65f61434a4acb513f3d46d2546a68f6661fca8459f4685e821f567323debcbbc |
| supplement/line_automaton.py | 3e260e709b07c7b71a5a7977d8377fc95407262751fd32037676b5a06beb4e0a |
| supplement/CHECK_RECEIPT.md | ec096d5f3d65e3b96f69f6c18e494f0a9d284d55af37f3e944e6332883c7e2b2 |
| supplement/README.md | 062bb018bf7ea421eac2744f81f3ed70b6df48cc1fa45e0bf48119ba0613c855 |

Both Python hashes equal their original frozen counterparts.
Static inspection confirms that the classifier uses lines()[:39],
integer square roots, parity tests, a set of actual triples and
immediate rejection of a transition leaving that set. The helper
constructs 45 lines for an older generic diagnostic, but its first
39 are precisely the proved families. Its independent generic
period histogram is not called by the pointwise classifier and
is not promoted to a theorem. Its quadratic coefficient routine
is valid here because the cubic cancellation on the selected
lines is already proved explicitly; sampled interpolation is
not being used to certify a polynomial degree.

The relocated receipt differs from the original only in its two
retargeted local links. Its reserve-stage status and old execution
claims remain historical, as the adjacent README explains.
Those finite checks were not rerun in this manuscript-review
round and do not prove the all-word result. No old PASS is
backdated into a new execution or used as a substitute for the
complete manuscript reading.

No new external search query or primary-source request was made
in this second round. Bibliographic and source-positioning checks
reuse the explicitly recorded primary-access evidence in the
fully reread source audits and first manuscript review. The
following boundaries remain material:

- Full traces and half traces require the stated coordinate
  scaling. The generator formulas, invariant, conic rotations,
  reversible substitutions and general escape framework are
  credited as classical, not claimed anew.
- Whole-group finiteness or boundedness and periodicity for one
  chosen positive word have different quantifiers. Finiteness
  of a collection of group orbits is also not finiteness of each
  orbit. The manuscript's concrete separator is the relevant
  argument; title differences alone would not suffice.
- The audits' statement-level Cantat–Loray checks retain their
  recorded preprint-version boundary. The manuscript cites the
  2009 journal record as contextual group dynamics and does not
  attach a preprint theorem number to that journal version.
- Humphries is bibliographically labeled a preprint; the
  Ghosh–Sarnak entry identifies the inspected arXiv v3 and its
  related journal DOI without inventing final pagination.
  C413 is identified as a research manuscript, not a published
  journal result. Its single-map classification is deducted.
- The Humphries–Manning period-two-curve follow-up is now
  identifiable, but its unread theorem list remains a source
  coverage limit. This review does not silently exclude it or
  assert worldwide priority. No external uninspected escape
  theorem is a hidden premise of the self-contained proof.

The allowed scientific claims are therefore the theorem and
algorithm for the stated positive-word/integer/ordinary-clock
domain, together with the bounded comparison against inspected
prior statements. Rational nonintegral points, complex schemes,
finite-field dynamics, whole-group finite orbits, optimal period
40, target L-functions and Hilbert–Pólya conclusions remain outside
the asserted result.

## PDF, diagnostics and review procedure

The PDF has 11 letter-sized pages, no encryption, and all 19
listed font entries are embedded, subset and Unicode-mapped
according to pdffonts. Full extracted text was inspected for
every page, including the Section 8 continuation and references.
The existing current-build PNGs of pages 6, 7 and 10 were
personally opened and visually inspected. They are legible and
show the actual O1 placement and O2 wording. No new rendering
or modification of the build directory was performed here.

This is not an all-eleven-page visual certificate: the remaining
pages were fully text-read, not newly raster-viewed by this
reviewer. The coordinator's final all-page gate remains explicit.

Read-only scans of the final main.log and main.blg found no
actual LaTeX/BibTeX warning, overfull/underfull box, undefined
reference, citation or error diagnostic. A broad case-insensitive
search for the bare words warning/error also matches harmless
package/banner text and BibTeX's zero warning-function counter;
those are not warnings. Diagnostic-pattern scans returned no
match. This reviewer did not launch another LaTeX build, so the
author's recorded successful build is not relabeled as a fresh
reviewer compilation.

The research-review skill's evidence-backed criticism and
documentation discipline was used under the repository's
current-team review arrangement. The ARS reviewer guidance
informed read-only evidence/provenance checks only; no full
five-reviewer panel, three-gate ARS evaluation, mandatory model
override, external review thread or ML scoring exercise is
claimed. The current team has correlated-blind-spot risk, even
though this round's reviewer differs from the first round's.

Only this raw review report was written. No manuscript, original
proof, supplement, numerical record, primary-source file or Git
state was changed. Mathematical programs executed in this round:
zero. New scientific experiments requested: zero.

## Handoff

Second full-manuscript review is complete: PASS, all three adopted
optional items closed, zero mandatory corrections, zero new
optional requests. The reviewed object is exactly the fourteen
inputs and 11-page PDF identified above. Proceed to the separate
final build, complete final-page inspection, evaluation and
archival gates without describing this report as their completion.
