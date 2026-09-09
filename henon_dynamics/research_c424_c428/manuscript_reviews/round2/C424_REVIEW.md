# C424 second manuscript pass: unchanged-object regression review

2026-09-09 UTC. Reviewer: the assigned current-team nonauthor who performed
the first actual C424 manuscript review, neither the C424 manuscript author
nor the AM1 proof author. This is the separately authorized second pass after
coordinator adoption of the first-pass PASS/no-change disposition. It is not
a copied first report, a newly generated mathematical certificate, an external
model service, human external peer review, or a formal Route-A evaluation.

## Disposition

**PASS for the second manuscript-review round; no author change requested.**
The first round required zero corrections. The author correctly preserved
the actual object rather than introducing an artificial cosmetic revision.
This pass independently checked that no mathematical, source, evidence or
PDF change was hidden by the no-change label, then re-examined the principal
claim/count/dependency interfaces. No new defect or unresolved adopted
finding was identified.

The two manuscript-review passes can now be submitted to coordinator
adjudication. This review does not mark the author state completed, perform
the later formal evaluation, or certify the final build/release gates.

## Exact object and fresh identity checks

Paths below are relative to `papers/C424_integer_valued_quadratic/`.

| Artifact inspected now | SHA-256 |
| --- | --- |
| Current `main.pdf`, 21 pages, 463423 bytes | `3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b` |
| Complete 29-entry `INPUT_MANIFEST.sha256` | `ea282bedc12d736c9a0e421e5448744504ef742b593d6ebaf07368b27b090f63` |
| Initial `AUTHOR_REPORT.md` | `87c1661675c9c7fbe95974291c74e8a8b5f6914d3faabbc3deb4be98fb7015fa` |
| Actual first nonauthor review | `6e2a02043cb2c42f0e6f4ed77d3705a0287f494eceb4903172aac40c3a1ecfd6` |
| New author `PAPER_IMPROVEMENT_LOG.md` | `79a53e24c7f741082ce00907e04674725b864a2ae046c8cc4a3981e35d26a4d4` |
| New author `PAPER_IMPROVEMENT_STATE.json` | `52fc3f8ef9a266f4e7d69eac7f197495b9cd4aa9e047cbb11a4ec7ebff3f013b` |

The first four identities agree with the first-pass record. I read both new
author disposition files fully, as well as the complete first report. Their
`pending_round2`, zero corrections, zero additional builds and preservation-
copy descriptions are accurate; the copies are not presented as new builds.

Fresh `sha256sum -c` verified **all 29 current inputs**. Separate byte
comparisons checked each of those actual input files against its counterpart
in `baseline/round0_layout1/`, with 29/29 matches. This covers all sections,
appendices, macros, bibliography, receipt table, build/formatting scripts and
the twelve proof/evidence files, not just the main TeX entry.

Current `main.pdf` compares equal to `main_round0_original.pdf`,
`main_round1.pdf`, `baseline/round0_layout1/main.pdf` and
`build/round0_layout1/main.pdf`. The current manifest compares equal to both
round-labelled manifest aliases and the frozen layout-1 snapshot manifest.
A fresh read-only PDF-to-text stream compares byte-for-byte equal to the
saved 1107-line manuscript text read completely in round 1. There is therefore
no revised source or newly generated PDF requiring a second LaTeX build.

All twelve evidence copies were again compared with the exact original paths
given by `CITATION_AUDIT.md`: six files in the batch's `arithmetic_maps/`,
five in `arithmetic_spectral/AM1_REVIEW/`, and the complete C412 PDF from
`continuation_c409_c413_round2/papers/C412_integer_henon/`. Every comparison
passed. The C412 copy retains SHA-256
`66788e384cc8016240b17695decac08962f9289fef40a6782eeb108bd3ab699a`.

## Fresh substantive regression checks

The present pass reread the actual abstract, introduction and both cycle
tables, normalization, annulus and complete local-word sections, finite-core
section, all count/equality proofs, scope section, both appendices, citation
audit and bibliography. It does not claim a second full line-by-line reading
of both unchanged Python programs, all JSON payload details or the entire
predecessor: those complete readings are documented in
[the first report](../round1/C424_REVIEW.md), and their byte identities were
verified again here. The following are the second pass's targeted questions.

1. **Does the abstract still match the domain and proof?** Yes. It ranges
   over every degree-exactly-two integer-valued polynomial and all rational
   initial points, while integrality is asserted only for the normalized
   half-form. The native determinant is +1 and no iterate replaces the time
   unit. Both signs of nonzero `m` remain valid in the affine inverse. The
   distinction from arbitrary rational-coefficient quadratics is explicit.
   The no-cutoff statement is supported by a proved all-parameter reduction,
   not by treating a finite search window as evidence of completeness.
2. **Are the two branch recoveries and the 17-point equality locus intact?**
   Yes. For even `m=2κ`, C412 is applied to the stated monic map and the
   coordinates are divided by nonzero `κ`; Appendix A's additional shift
   gives `(w-h)/κ`. For odd `m`, `q=n-(m+1)/2` and
   `A=mr+(3q-q²)/2` are integral, and the inverse is `(u-q)/m`.
   These rational bijections preserve exact periods and counts. C412's
   maximum 8 excludes even `m`; the complete equality condition remains
   precisely odd `m` with `A=-1`, not simply a condition on original `r`.
3. **Is the analytic/finite seam still exact?** Yes. The threshold
   `a<=-146` gives `ρ>=35/2`, where both the lower-annulus contradiction
   and exact coefficient separation are strict. The six local cases are
   still fully reproduced and attributed. The finite remainder is
   `-145<=a<=0`, plus the analytically proved control `a=1`; `a>=2` is
   separately empty. This is 147 stored residual/control records, with no
   hole or duplicated claim of a new analytic result at the control.
4. **Do the printed four families and eleven exceptions give the actual
   coexistence counts?** Yes. The `k=0` half-form three-cycles remain
   distinct. The exceptional four-cycles at `a=-11,-1` remain distinct
   from their parametric four-cycles. The indicator formulas in (7.2)
   therefore do not need overlap subtraction. At `a=-1` the disjoint
   cycle lengths remain 4, 4 and 9. The native period set is exactly
   `{1,2,3,4,5,6,7,9,10}`; it is a union across the coefficient class,
   not an assertion that every map has all nine periods.
5. **Do the two historical finite outputs still support the count interface?**
   Yes. A fresh read-only comparison of stored fields checked all 147
   ordered parameter labels, full oriented-word lists, period histograms,
   point counts and cycle counts, with no mismatch. Totalling those stored
   fields gives 306 points and 113 cycles across different maps, maximum
   17 only at `-1`, and 223587 already-recorded processed vertices. The
   complete stored exception list has eleven cycles. The producer/checker
   hashes in the unchanged files still match the displayed Appendix B
   identities. No map, recurrence, graph, pruning trajectory or cycle was
   recomputed by this comparison.
6. **Is the substantive C412 import still explicit and correct in form?**
   Yes. Appendix A retains both complete tables and the small-index
   restrictions, including `k>=1` for the second odd-branch three-cycle
   and the even-branch coincidences. The entire predecessor remains
   supplied, not replaced by a theorem summary. The annulus/symbol/
   finite-permutation machinery is visibly inherited, while this paper's
   completed result is one coefficient-class classification. The zeta
   identity remains an ordinary rational-point return-count consequence,
   not an arithmetic Euler product or a second independent contribution.

## Presentation and source-scope regression

I newly viewed the existing individual page images labelled 1, 2, 3, 9,
10, 11, 12, 17, 20 and 21. These targeted pages cover the abstract and
opening tables, finite proof boundary, complete count/equality argument,
both imported C412 tables, start/end of the receipt, source hashes and
bibliography. No clipping, collision, missing row, unresolved marker or
new claim mismatch was observed. All 21 pages were already viewed in the
first actual pass; this targeted reinspection is not falsely labelled a
second all-page inspection.

Fresh checks of the actual converged `main.log` and `main.blg` found no
warning/error, undefined reference/citation or over/underfull-box match.
The PDF still has 22 embedded Type 1 font resources, visible anonymous
authorship and blank Author metadata. All four bibliography entries remain
present in the actual `main.bbl` and PDF. The version-specific external
comparisons and their access limits have not changed. Ingram remains
canonical-height/determinant-minus-one context, and the Kim et al. v2
comparison remains growing odd degree, not this quadratic theorem. C412
and AM1 remain explicitly unpublished internal inputs. No new public-source
search, publisher-policy check or external manuscript upload was performed
or represented as performed during this identity/regression pass.

## Residual risks and coordinator boundary

- The finite exhaustion and imported C412 theorem remain substantive
  dependencies. Their preserved programs, full outputs, exact predecessor
  copy and inventory must accompany the eventual release. A matching hash
  supports migration integrity, not mathematical truth by itself; the
  first pass supplied the complete proof/code/output reading.
- The first-pass ARS structural PDF preflight returned `UNAVAILABLE`
  because `pypdf` was absent. The complete actual advisories remain in the
  first report. I did not install software, rerun that unchanged advisory
  or upgrade it to structural page-anchor certification. Section/theorem
  labels and the directly viewed renderings support the locators here.
- This is internal nonauthor review, not formal verification, external
  human peer review, a worldwide-priority certificate or a journal score.
  No new correction, computation contract or mathematical rerun is needed
  to resolve an identified manuscript defect in this pass.
- The final identical-input fresh-build pair, final all-page inspection,
  formal evaluation and review of that evaluation, release membership/
  manifest checks and Git integration are coordinator-owned gates. Their
  absence is not concealed by this manuscript PASS.

The `research-review` skill supplied the claim/evidence and residual-risk
discipline, adapted to the explicit current-team, no-change assignment.
Only this new round-2 report was written. No C424 author source, evidence,
baseline, improvement state, shared registry or Git state was modified;
mathematical-program executions and LaTeX builds in this review: **zero**.
