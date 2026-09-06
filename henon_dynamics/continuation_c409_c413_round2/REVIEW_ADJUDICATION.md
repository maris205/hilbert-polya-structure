# Five-manuscript review adjudication

Recorded against the 2026-09-06 manuscript snapshots. This is the coordinator's
decision after reading the actual reports, not an external or human review.
The initial four source contracts remain frozen in
[the first research checkpoint](../research_c409_c413/PROVISIONAL_ADJUDICATION.md).
The fifth source admission is [the trace-map review](REVIEW_TRACE_ROOT.md).
The independent [outline review](positive_characteristic/REVIEW_BATCH_OUTLINE.md)
preceded the full manuscripts and is not substituted for their reviews below.

## Actual full-manuscript reviews

| Paper | Author / non-author reviewer | Report and disposition |
|---|---|---|
| C409 | Arithmetic / positive-characteristic agent | [Full manuscript and source review](positive_characteristic/REVIEW_C409_MANUSCRIPT.md): complete proof supported; two narrow repairs, both confirmed in the appended affected-passage check. |
| C410 | Positive-characteristic / nonlinear-geometry agent | [Full manuscript and source review](nonlinear_geometry/REVIEW_C410_MANUSCRIPT.md): all three theorems supported; one optional precision edit selected and confirmed in §9. |
| C411 | Arithmetic / positive-characteristic agent | [Full manuscript and source review](positive_characteristic/REVIEW_C411_MANUSCRIPT.md): PASS, no required repair. |
| C412 | Nonlinear-geometry / root coordinator | [Actual full-proof and scoped-source review](REVIEW_C412_MANUSCRIPT_ROOT.md): PASS, no required repair. |
| C413 | Root coordinator / positive-characteristic agent | [Full manuscript and source review](positive_characteristic/REVIEW_C413_MANUSCRIPT.md): complete proof supported; finite-check wording repaired and confirmed. |

The coordinator read all five reports completely, including their targeted
confirmation addenda. For C412 the coordinator directly reviewed the whole
manuscript proof and the five cited primary sources at the explicitly recorded
depths. For the other non-root drafts the non-author agents performed the
full manuscript/source reviews; the coordinator does not relabel their source
reading as his own. C413 is the coordinator's authored manuscript and has a
different non-author reviewer. The final all-page visual inspection is another
gate, recorded separately from mathematical review.

## Review-driven revisions actually made

- **C409:** the introduction now asserts complete grids along an unbounded
  sequence of supported conductors, not at every sufficiently large conductor.
  The no-wild deduction cites BCH Propositions 10.2.1 and 10.2.2 separately,
  explains the latter's integral-wild hypothesis when the wild exponent is zero,
  and explicitly handles the empty prime set. See
  [revision notes](papers/C409_wild_fad/REVISION_NOTES.md). Neither the Fourier
  proof nor the accepted theorem was enlarged.
- **C410:** Lemma 3.1 now proves directly that its displayed three roots are
  distinct: `beta != 0` implies `z not in F_3`, and their differences are the
  nonzero quantities `a(z+1)`, `a(1-z)`, and `az`. See
  [revision notes](papers/C410_wild_cubic/REVISION_NOTES.md). No extra constant
  field or square root of `a` was introduced. The optional descent parenthesis
  was not needed for the already complete proof and was not added.
- **C413:** the finite-graph paragraph now counts cycles wholly contained in
  the chosen cube. Leaving that cube does not imply global nonperiodicity;
  the manuscript supplies a point of the larger cycle `B_3` as a witness.
  See [revision record](papers/C413_integral_trace/REVISION_RECORD.md).
  The earlier proper-escape assertion remains restricted to nonperiodic
  integral points.

C411 and C412 required no manuscript repair. The revisions above do not
invalidate unchanged mathematical test inputs in the frozen research package;
those old tests were not rerun. New source paragraphs must, and do, enter the
coordinator's final builds. The historical author-build hashes and initial
review snapshots are not represented as current final-PDF hashes.

## Ownership and completion boundaries

All five contracts retain a substantial independent question after the
classical deductions specified in the batch plan. This is not a certificate
of worldwide priority. In particular, the missing final BCH book, the unread
Silverman subscription text, and final-version/preprint differences remain
disclosed in the respective citation records. Existing orbit families, group
definitions, S-unit bounds, height theory and Fourier/complex-analytic tools
are credited, not recounted as separate new papers.

The arithmetic finite-lattice inverse candidate remains unnumbered with
[its older-source gate open](arithmetic/SOURCE_AUDIT.md), despite the separate
[mathematical PASS](positive_characteristic/REVIEW_FINITE_LATTICE_CENSUS.md).
The stopped positive-characteristic cocycle and spectral-filter screens
remain research notes, not substitutes for a sixth paper.

The separate [evaluation consistency review](arithmetic/REVIEW_EVALUATION_CONSISTENCY.md)
also passes within its semantic scope. Its reviewer authored C409/C411 but did
not author any evaluation; this is not a self-review of those papers. All
strict tuples, missing target metrics, incomplete controls and false target /
Route-B flags remain unchanged. Mathematical review, deterministic PDF
identity and a valid payload manifest do not establish a Riemann divisor or
Hilbert–Pólya operator. The remaining release gates are tracked in the batch
README and final build report, not inferred from the word PASS here.
