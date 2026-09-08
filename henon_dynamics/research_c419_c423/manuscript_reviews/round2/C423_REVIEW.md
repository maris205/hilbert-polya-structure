# C423 — second full-manuscript review and revision verification

2026-09-08 UTC. Reviewer: the same current-team spectral-lane
nonauthor reviewer as in the first manuscript round. I also
previously reviewed CP9's proof. This disclosed continuity is
not a claim of a new reviewer identity or independent error
processes across rounds.

This is internal AI-assisted review, not blind or human peer
review, an external GPT-5.4 invocation, a calibrated numerical
score, formal evaluation or final-release certification. Reusing
the same team/model family can preserve correlated blind spots;
the second full reading does not eliminate that limitation.

## Verdict

**PASS for the second full-manuscript review. O1 and O2 are
addressed. Remaining mandatory corrections: zero. New requested
edits: none.**

The revised article retains the complete arbitrary-field
classification, its two separately attributed external inputs,
the exact two-cycle/escape argument, both nonzero-difference
cases and the elementary proof of sufficiency. Both accepted
edits improve the explicit presentation without changing a
hypothesis or conclusion. No new regression, omitted case or
remaining mathematical transcription issue was found in the
actual second complete manuscript reading.

The first review also had zero mandatory corrections. Its
optional suggestions are not reclassified as repairs of false
theorems, and no flaw, extra edit or score increase is invented
to make this clean second pass appear more substantial.

The coordinator still owns current/final visual checking,
final build/reproducibility, evaluation and release gates.
This report completes the assigned second review, not those
remaining workflow actions.

## Actual revised input and read extent

Paths below are relative to papers/C423_two_cycle_preperiodicity/
under research_c419_c423/, unless stated otherwise.

The selected review PDF was builds/round1/main.pdf:

- Six pages, 317422 bytes; anonymous 11-point mathematical article.
- SHA-256: 36c2088ca4d794087a698413431d55e7d7e00ed1d2c4b1e3a5cfa5b9f8814e98.
- It is not the earlier builds/author_polished/main.pdf, whose
  hash remains b0aa1ace124faa50d14ff50873a5acaa70c5691c01772cd96cd74bd03626f408.

The complete 42-line REVISION_ROUND1.md was read first. Its
SHA-256 is:

    01dbd2c81084412af120b468042f5614ef7f4b1634a45ab6658b17fd435740e3

Every current production TeX/Bib file was then read fully:
main.tex, math_commands.tex, references.bib, all six sections
and tables/source_scope.tex. These ten files total 440 lines.
The entire six-page text was newly extracted directly from
builds/round1/main.pdf to standard output and read through
the bibliography. This included unchanged material as well as
the two revised passages; it was not a delta-only check.

The first-round report's verdict/input passages and its
optional-item/source-access passages were reread. Its path
relative to research_c419_c423/ is
manuscript_reviews/round1/C423_REVIEW.md; its unchanged hash is:

    59809633d137276f3d55cf8d920ce1608f35bc6bd84c5f9b6eac01afc78dd9a2

This round does not claim another complete reading of every
historical CP9 proof/review document or of every external paper.
Their earlier actual access remains recorded in that report.
The new evidence surface is the complete revised manuscript.

### Exact production identifiers and revision scope

All ten working input hashes agree with the corresponding
snapshots/round1/ files:

| Input | SHA-256 |
| --- | --- |
| main.tex | dc722535544c9cd6def684c3808e5e281f53033b642bbc0b19f66f8d71d5c31c |
| math_commands.tex | 5f1b7b35077808bd827b7d7ddf2b01310b52c33b148e28da411fc4c8f3fcb006 |
| references.bib | 4437129d8e6274755fc6a57ffd2c371d5aa678027ce689026ab82215b88bf3e5 |
| sections/0_abstract.tex | 2686b4e620bf1f555f4e86454ce3368403a3bd3ff113841d57707c6b086f3b3a |
| sections/1_result.tex | 1c7d7a71f75bb6e44b7545d4238f25aec0dbd27391491121f0689600bc237d07 |
| sections/2_inputs.tex | 6a5b0a6d52e636e0f061efb95b0b8e6c11d559c067981e862df6081a9fb8818e |
| sections/3_witness.tex | 7dd6ee8d2fee48b4e9a1dc2c4fcc17409bbf193924179de1035ed71b11b6d3c9 |
| sections/4_classification.tex | 6cc16c60e7c0b3f41c8ff12585d34089e6c3141876fd98808d2939b418f4d155 |
| sections/5_scope.tex | d5b86ea9e52594b30213189a7dc194306405de7ecebc116597ad61bfc000837c |
| tables/source_scope.tex | 79ba16c90c7569ad4d620b0d55d3eec9adc295a16a49abf5c2574f9a62397788 |

The ten snapshots/author_polished/ hashes still agree with
the first-round inputs. A recursive comparison of the two
snapshots identified exactly the abstract and classification
section as changed. The complete unified diff of each was
read. The remaining eight input files, including both external
propositions, the witness, table and bibliography, are unchanged.

## Revision checklist

| Original optional item | Revised anchor | Result |
| --- | --- | --- |
| O1: qualify the abstract's exclusion and pole argument locally | sections/0_abstract.tex:8 | Addressed: the nonzero differences are explicitly considered when the marks are not both constant, and the exclusion is restricted to that case. |
| O2: explain the relative algebraic closure assertion | sections/4_classification.tex:85 | Addressed: the new sentence explicitly applies transitivity to roots over the relative closure. |

### O1 — addressed

The abstract now states that the residual nonzero differences
arise when the marks are not both constant, and explicitly
restricts their elimination to that nonconstant case. The
preceding classification still retains all pairs algebraic
over the prime field.

This fixes the isolated-reading ambiguity without imposing
an extra hypothesis on Theorem 1.1. In the nonzero-difference
branch, the body proves that neither mark can be constant;
the pole construction therefore has its required transcendental
mark. The following abstract sentences inherit a clear local
scope. No constant pair is incorrectly excluded.

### O2 — addressed

The added text says that a root in the chosen algebraically
closed ambient field of a polynomial over the relative algebraic
closure is still algebraic over K by transitivity. By definition
it therefore belongs to that same relative closure.

Together with existence of the root in the ambient algebraically
closed field, this proves the relative closure is algebraically
closed and algebraic over K, hence an algebraic closure of K.
The explanation is valid for inseparable algebraicity as well.
It neither assumes that the original L is finitely generated
nor shrinks the original infinite parameter set. This is the
requested reason, not merely a repetition of the assertion.

## Observations from the second complete reading

### 1. Classification and external-input boundary

The field L remains arbitrary of characteristic three. Constants
are defined inside its chosen algebraic closure; geometric
parameters are not mistakenly required to belong to L.
Both sufficient alternatives remain in the theorem.

The weights remain equal, so neither strict-weight regime is
applied to this family. The necessary relation and local-height
proposition remain distinct attributed inputs with their prior
source-version boundary preserved.

In particular, Proposition 2.2 still gives equality for every
relevant place and every parameter in the completed algebraic
closure. It is not weakened to the original common-preperiodicity
set, which would invalidate the separating-parameter argument.
The subsequent proof constructs the required function field
before invoking the proposition. No new source theorem or
source-access claim appears in the revision.

### 2. Two-cycle and exact escape height

All characteristic-three translation identities and both orbit
segments remain present and consistent. The first two points
are distinct for transcendental a, so the stated period is
least period two. The positive-difference relation alone gives
the second path through -a-1 and 0 to the chosen parameter.

At a pole with C=|a|_v>1, that parameter has absolute value
C^6. Once outside radius C, the sixth-power term is the unique
largest term, giving exact growth at every subsequent step.
The third iterate of b is already of size C^6; thus the
printed exponent 6^(n-2) for n>=3 and the height log(C)/36
are correct. No finite orbit sample or assumption of a discrete
extended value group has replaced the escape proof.

The witness's parameter is in the constructed K. Universal
height equality therefore produces the intended contradiction.
The negative difference still reduces to the positive one by
swapping the marks, both of which have been shown nonconstant.

### 3. Arbitrary-field descent

The nonzero relation makes b algebraic over k(a). The union
of the unique iterated cube roots is the perfect closure of
k(a), and adjoining b is finite. Every common-preperiodicity
parameter satisfies a nonzero iterate-difference polynomial
over k(a): the leading T-degrees differ when the smaller
iterate is positive, and the zero-th iterate is constant.

The new relative-closure explanation fits after that argument.
All original parameters are retained in an algebraic closure
of K, including inseparable ones. A place above the pole of
a has C>1 with nonzero constants of absolute value one.
The manuscript does not assume the arbitrary ambient L is
already a one-variable function field.

### 4. Single-mark lemma and both sufficient cases

The finite-field argument for constant marks is unchanged.
For nonconstant a, the iterate polynomial is monic of degree
6^(n-1), and its unique fixed parameter is a simple root
because the printed derivative sum is a nonzero polynomial
in the transcendental a.

For each prime ell, including 3, degree greater than one
and simplicity of the fixed root give another geometric root
with least period ell. Distinct primes cannot yield the same
parameter. The proof requires neither all-root separability
nor a simultaneous choice of one parameter for all primes.

In the equal-f-value case, the one-point lemma is still
applied to the fixed marked point a. The orbit of b joins
after one iteration, establishing sufficiency without treating
a parameter-dependent image as a fixed mark.

### 5. English, attribution and scope

The abstract, theorem, two propositions, witness, parameter
lemma and proof conclusion agree on their quantifiers and
cases. The paper prints every nonexternal argument needed
for its classification. Neither new explanatory sentence
introduces a changed convention or an unavailable assumption.

The two bibliography entries remain relevant and cited. The
height statement's original attribution is retained while the
actual statement-access route through Lee–Nam is disclosed.
The original Ghioca–Hsia body is not represented as newly read.

The conclusion still concerns this fixed equal-weight binomial,
not all such families, quantitative bounds on the finite
exceptional sets, or target Euler factors, root numbers and
spectral realizations. Internal AI-assisted review is not
promoted to human peer review or global-priority certification.
No additional citation or optional wording change is requested.

## Actual diagnostics and limitations

The selected PDF's metadata confirm six unencrypted letter-size
pages. Its font inventory contains 20 entries; each is embedded,
subsetted and has Unicode mapping. Complete PDF-text reading
found no unresolved reference or obvious malformed statement.

The actual builds/round1/main.log and main.blg were searched
for Warning/Overfull/Underfull/undefined/LaTeX Error/Package
Error, with no matches. The no-match search exit was 1, not
a compiler failure. Exact final-log hashes are:

    main.log:
    a04e4b12130720c4e23ea78dcf2f98c8450f31cae13e8d854a9f809f2a92277a
    main.blg:
    5edc3348304d06303fc37602585873be8a88b5ae6b6df1bdc77f198164a4e00b

No compiler was invoked here. The author/coordinator's fresh
round-one build is the actual reviewed build; a filename,
snapshot or hash check is not called a second build.

No pages of this revised PDF were newly rasterized or visually
inspected by this reviewer. Earlier baseline-page observations
are not reused as current-PDF visual acceptance. Current/final
visual checking therefore remains an explicit coordinator gate.
No structural PDF-preflight certificate is claimed.

There were zero new web searches, primary-page opens, external
model calls or mathematical executions in this second review.
The first-round source-access record remains the source-verification
receipt; it is not relabeled as new access. The complete revised
manuscript was actually read independently of that historical
receipt.

## Procedure and handoff

The research-review skill was applied through the agreed
current-team mathematical-paper fallback. ARS reviewer guidance
informed the read-only, anchored-verification and provenance
boundaries. This review is not claimed to be an ARS five-seat
journal panel or its machine-checked three-gate contract.
The actual author-record-first order is disclosed rather than
called revision-blind or persuasion-blind. No venue or score
requirements were invented.

The only authored file is this report. No manuscript, source
snapshot, proof artifact, PDF, revision record, global ledger
or Git state was changed. The review found no reason for a
further author edit or a mathematical rerun.

Second-round status: PASS; O1 and O2 addressed; zero mandatory
corrections and no new requested edits. Preserve this raw
report and complete the remaining actual visual/build/release
checks under coordinator ownership.
