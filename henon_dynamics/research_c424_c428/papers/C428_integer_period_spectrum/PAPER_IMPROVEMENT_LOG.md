# C428 manuscript improvement log

Status: `final_build_complete_pending_seal`. 2026-09-09 UTC.

This records the actual nonauthor review of the actual first manuscript,
its adjudicated revision and real PDF builds. Earlier proof-admission
and outline reviews are not relabelled manuscript rounds. The local
`auto-paper-improvement-loop` skill supplies the preserve/revise/build/
log workflow; the authorized batch plan overrides external-model,
ML-score, venue-cap and notification defaults. No external reviewer
API, invented score, human peer-review claim or mathematical execution
is involved.

## Complete first review and disposition

The coordinator is not the C428 manuscript or IH6 proof author. The
complete actual report is preserved unchanged as `reviews/round1/REVIEW.md`,
a byte copy of `../../manuscript_reviews/round1/C428_REVIEW.md`, SHA-256
`1bfe9d8b9396e78711f1970268381af170d74693b47023b0e7c81c642868f6f7`.
The author read the full report. Its verdict is zero analytic/certificate
theorem must-fix findings, one manuscript algorithm-interface must-fix
P1, and one minor bibliography correction P2. The coordinator adopted
both and authorized this revision without a certificate rerun.

| Item | Actual source change | Actual revised-PDF check |
| --- | --- | --- |
| P1: numerical map interface | Appendix A.1 specifies a map keyed by actual integer letters and compares coordinate support to `set(E)`. A.2 constructs `v := {e[j]: values[j] ...}` before `FULL_CYCLES(E,v,a)`. | The argument is unambiguous for nonconsecutive alphabets such as `(0,2)`; it no longer treats actual coordinate 2 as a list index. |
| P1: affine/template interface | A.3 uses temporary endpoint-distance values `eta[b]`, constructs the map `h` keyed by actual affine letters, and assigns the right value to `D-b`. A.4 explicitly initializes `V`, binds the target-letter loop and constructs `v := {u(D0): V[u](D0) ...}` at each exceptional diameter. The pruning loop uses `V.values()`. | Complete A.1--A.4 read and viewed across pages 12--14. Both signs, endpoint zero remainder, dictionary keys, numerical evaluation, identity arrows and pruning semantics agree with the already-proved procedure. |
| P2 | Both IH6 bibliographic descriptive fields retain `9 September`, with the unchanged `year={2026}` supplying the year once. | References [4] and [5] now print `9 September, 2026`; title, path, source ownership and internal/unpublished disclosure remain. |
| Author self-check T1 | The introduction's source `secant-` newline `affine` became intact `secant-affine`. | The inherited spurious hyphen-space is absent; no mathematical wording or conclusion changed. |

The exact three-file diff is `reviews/round1/source_changes.diff`,
SHA-256 `8bf5c669abf9687f51b20022981bcf2e48d8572b9cc02509b84afb55cee31ed9`.
Only `sections/A_pseudocode.tex`, `references.bib` and
`sections/01_theorem_sources.tex` differ among the 15 active editable
inputs. The other 12 were individually byte-compared unchanged with
`builds/round1_revised/baseline_source/`, extracted from the intact
original archive. Theorems, reduction, exact tables, witnesses,
scope and the three historical mathematical executions are unchanged.
No new source result or computational evidence was introduced.

## Actual builds and inspection

Three actual changed-input revision builds succeeded. Each used three
pdfLaTeX and two BibTeX passes under the initial deterministic settings.
Their PDFs, transcripts and intermediate input archives remain; the
full ledger gives each change, byte count and SHA-256. Rejected patch
attempts and the harmless companion-path lookup error are recorded
there, not concealed as successful operations or labelled failed builds.
There were no failed compilations. The cumulative six drafting/revision
invocations used eighteen engine and twelve BibTeX passes.

The final candidate `builds/round1_revised_03/main.pdf` has 16 pages,
389314 bytes and SHA-256
`cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af`.
Both final engine and BibTeX logs are clean. All 19 fonts are embedded
Type 1. The full 788-line extracted PDF text was read and every one
of the 16 final page images actually viewed, including all pseudocode
continuations. The source diffs, unchanged inputs, exact table data,
all seven bibliography items and two-hyphen command were checked.
The old two author scripts and independent checker/full output were
rehashed to their unchanged manuscript SHA-256 values, read-only.

`main_round0_original.pdf` preserves the original PDF, SHA-256
`d5aeb4ae86009dc9f229a54c50083ccb03eba1f3bdc562d13a12400140dd8cde`.
`builds/initial_03/source.tar` remains unchanged, SHA-256
`8b39c36f7186e3754818ee139793165bfd55844208b483b64f6b2bf62e664adc`.
`main_round1.pdf` and current `main.pdf` are byte copies of the actual
final revision PDF. The revised source archive preserves all editable
inputs and this review/change/build documentation, without overwriting
the original or intermediate archives.

## Actual second manuscript review and no-change closure

The coordinator completed and formally adopted the separately scheduled
second actual manuscript review. Its complete report is preserved as
`reviews/round2/REVIEW.md`, a byte copy of
`../../manuscript_reviews/round2/C428_REVIEW.md`, SHA-256
`724dc2ba066ba48d25822664e12f2a36a727e30ccd43b3a45595c6f1b1178042`.
The author read the report in full before final-build preparation.

P1 and P2 are closed; T1 is verified. Remaining must-fix and new
optional findings are both zero, and no new manuscript-source change
was requested or made. The second reviewer followed the whole revised
numerical/affine key interface, including `(0,2)`, right-hand `D-b`
values, endpoint placeholders, the explicit target loop, evaluated
exceptional-diameter map and value-wise pruning. The complete PDF-text
diff and all 15 archive members were checked; the visual second-pass
scope was the six affected pages 2 and 12--16, not a newly claimed
full 16-page inspection. The final builder's all-page pass is separate.

`main_round2.pdf` is a no-change byte alias of the reviewed
`main_round1.pdf`, SHA-256
`cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af`.
It is not an additional source revision or compile. Both actual
manuscript-review rounds are now closed. No mathematical program was
run to answer either review. The unchanged historical proof and exact
certificate dependencies retain their original evidence status.

## Final-build and release gates

The coordinator authorized exactly two fresh fixed-input final builds
after this review closure. Both were actually completed in new
`builds/final_01/` and `builds/final_02/` directories, each exiting 0
after three pdfLaTeX and two BibTeX passes. Their PDFs compare
byte-identical with each other and the reviewed round-two alias:
16 pages, 389314 bytes, SHA-256
`cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af`.
`main.pdf` was explicitly copied from `builds/final_02/main.pdf`.
No source edit, failed build, retry, third final build or mathematical
program execution occurred. Cumulative typesetting executions are eight
successful latexmk invocations, twenty-four engine passes and sixteen
BibTeX passes; these are not eight reviews or mathematical tests.

All 15 fixed-input checks passed before each build, after both builds
and after final visual inspection. Both independent input archives and
all forty-five member comparisons with active sources and the reviewed
revision archive passed. Both final engine/BibTeX logs are clean;
all 19 font resources are embedded Type 1. The complete 788-line final
text was read and all 16 newly rendered final page images were
actually viewed. These full final-builder checks are separate from
the second reviewer's six-page affected-page inspection.

The exact commands, versions, counts, archive/log hashes, inspection
scope and preserved diagnostic history are recorded in
`FINAL_BUILD_REPORT.md`; none of the three changed-input revision builds
substitutes for this fresh pair. Formal Route A evaluation, payload
sealing, independent membership verification and Git integration remain
coordinator-owned. No final release is certified here. The writer stops.
