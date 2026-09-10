# C430 manuscript improvement log

Status at 2026-09-09 21:21:44 UTC: **author revision 1 complete and frozen;
actual manuscript pass 2 pending**. This log records current-team
nonauthor reviews and the coordinator-author response. It assigns no
numerical score and makes no external-peer-review, acceptance, final-build,
formal-evaluation or release-seal claim.

## Original input and immutable full reviews

The actual reviewed round-zero source is `baseline/src/`. Its PDF is
`baseline/main.pdf` = `main_round0_original.pdf`, SHA256
`54bc61f0d9c89405047fdf116bbcaf38d9e658c6d401b70862b22659f2574c8e`.
The original 171-line `SOURCE_BUILD_RECORD.md` remains unchanged,
SHA256 `5f022836036b81e2e79b2cf4bc3100e9ae8891ef1b53e4df3c9700ff652a0957`;
it is the historical first-draft receipt, not a description of revision 1.

The following original reports are retained in full, unedited at their
assigned immutable paths. They were read completely by the author before
the revision; their hashes were checked both before and after it.
The concise response table below is not a replacement for either report.

| Actual review | Full raw report | SHA256 |
| --- | --- | --- |
| E2 nonauthor mathematical manuscript pass 1, 304 lines | [reviews/round1/REVIEW.md](reviews/round1/REVIEW.md) | `9bbaf68049838b3448e99cda27289000137a7bcf6a9d00cdb6eebaaaf32221e9` |
| E1 bounded citation audit, 235 lines | [reviews/citations/REPORT.md](reviews/citations/REPORT.md) | `6fed8b6c647e0168065c52dc1188ce888fbd7bbca680059b96b27b213be8c62a` |

E2 found no mathematical must-fix and offered R1-E1 as a nonblocking
editorial clarification. E1 found four metadata/rendered-identifier
repairs; its source applicability conclusions and explicit access limits
remain distinct from a mathematical verdict. The coordinator authorized
R1-E1, all four citation fixes, and the precise Keating-2009 author-version
locator. No other change was authorized or made.

## Round 1 response to the coordinator's adjudication

| Finding | Authorized implementation | Actual author verification |
| --- | --- | --- |
| R1-E1 | Added the ordinary metric `d(x,y)=|x-y|` and both directed terms defining Hausdorff distance for nonempty compact subsets of the completed algebraic closure, immediately before Theorem 7.1. | Source diff contains only this added paragraph/display in Section 7. The theorem and all proof paragraphs are unchanged. The same two-directed distance and the threshold independent of every Galois element remain in Section 7.3. Definition is visible on PDF page 14. |
| C430-CIT-01 | Converted the existing Elder–Keating entry to *Archiv der Mathematik* 126(5) (2026), 461–469; added/printed journal DOI `10.1007/s00013-026-02234-1`. Retained the original 21 March 2025 arXiv v1 and explicitly bound theorem/section numbering to that author version. | Correct journal/year/volume/issue/pages, DOI and v1 note are present in the rebuilt BBL and PDF page 17. No claim of reading the subscription version-of-record proof was added. |
| C430-CIT-02 | Added and printed Keating-2006 DOI `10.1016/j.jnt.2005.03.003`, retaining arXiv:math/0312391v2. | DOI is in the BBL and PDF page 17. The original citation audit's direct-publisher 403 qualification remains unchanged. |
| C430-CIT-03 | Made LRL's existing DOI `10.1112/S0010437X15007575` visible through its rendered note, retaining the v3 theorem-numbering qualification. | Actual BBL and PDF page 18 display the DOI; bibliography style/order and citation key are unchanged. |
| C430-CIT-04 | Added and printed the explicitly labelled arXiv DOI `10.48550/arXiv.2603.03873` for Debaisieux, retaining v2 and its 22 April 2026 date. | BBL and PDF page 17 contain the DOI, v2 URL and date. It is not described as a journal DOI. |
| Approved optional Keating-2009 locator | Retained the publisher URL and added arXiv:0805.2932v1 (19 May 2008), explicitly identifying it as the consulted theorem/section numbering. | BBL and PDF page 17 contain the exact author-version locator. No assertion of independently checked published-numbering equivalence was introduced. |

Only `references.bib` and `sections/07_eventual_tower.tex` changed
among the manuscript sources. The ten other source files retain their
round-zero hashes. No proof, theorem statement, quantifier, companion
interface, numerical invariant or scope claim was changed.

## New public checks and preserved limitations

Read-only primary retrieval during revision independently confirmed
Elder–Keating's journal record and issue in the
[Springer article](https://link.springer.com/article/10.1007/s00013-026-02234-1)
and [volume 126, issue 5](https://link.springer.com/journal/13/volumes-and-issues/126-5).
The subscription proof was not accessed. The exact preprint versions and
Debaisieux's arXiv-issued DOI were checked at
[Debaisieux v2](https://arxiv.org/abs/2603.03873v2) and
[Keating-2009 v1](https://arxiv.org/abs/0805.2932v1).
The [LRL DOI landing page](https://doi.org/10.1112/S0010437X15007575)
resolved to Cambridge's matching journal metadata.

The Keating-2006 DOI landing-page request failed in the retrieval tool.
A successful primary-domain search returned the
[ScienceDirect-indexed record](https://www.sciencedirect.com/science/article/pii/S0022314X05000831)
with the exact DOI, title, author, issue and pages. This is indexed primary
metadata, not successful direct publisher full-text access. The citation
audit's reported direct-publisher 403 is preserved, not rewritten.

The initial source receipt and citation report retain their distinctions
between actual primary text reads and inherited checked source audits.
Retraction-database status remains **unchecked/access unavailable** as in
the citation audit; there was no new comprehensive retraction,
forward-citation, withdrawal or worldwide-priority search.
The coordinator and companion author confirmed that C431's revision is
prose/bibliography only: its Theorem 1.1 and Sections 5–6 mathematics are
unchanged. This revision does not overwrite the original C431 hash
binding; the coordinator will bind the final companion bytes later.

## Actual revision builds and affected-output inspection

Both real revision invocations ran in new source snapshots, with the
following exact shell command and fixed environment:

```sh
set -o pipefail
env SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tee ../compile.log
```

| Attempt | Working directory relative to the paper | Actual result |
| --- | --- | --- |
| Revision 1, attempt 1 | `qa/revision_round1/source/` | Successful exit 0; three pdfLaTeX and two BibTeX passes. One final underfull box, badness 1308, in the newly expanded Elder–Keating entry. No compiler error or unresolved citation. Actual PDF/log/source are preserved. |
| Revision 1, attempt 2 | `qa/revision_round1/attempt02/source/` | After moving the same DOI URL to the end of that same bibliography note, successful exit 0; three pdfLaTeX and two BibTeX passes. Final TeX/BibTeX logs contain zero warnings, missing characters, undefined references/citations, overfull or underfull boxes. |

No diagnostic was suppressed. The within-entry DOI relocation changed
neither metadata nor access/version qualifications. These are two actual
build attempts within one author revision, not two manuscript-review rounds.
No final deterministic release-build pair was run.

The final revision PDF is **18 pages, 408109 bytes**, Letter, PDF 1.5.
All 20 font resources are embedded subset Type 1 with Unicode mappings;
there are no Type 3 fonts. The body ends and bibliography begins on
page 17; references continue on page 18. Anonymous metadata is retained.

`pdftotext -layout` extraction is retained as
`qa/revision_round1/main.txt`. Its full diff against round zero was
read: changes are the Hausdorff definition, requested bibliography edits
and their resulting line/page reflow. All nine references remain present,
with unchanged citation keys/order; all four new/previously hidden DOI
URLs were checked in the actual BBL and PDF, not merely the database.
No `??`, `[?]`, `[VERIFY]`, `TODO` or `FIXME` remains.
All section files are still included.

Every revision page was rendered with
`pdftoppm -r 95 -jpeg -jpegopt quality=82` into
`qa/revision_round1/pages/page-*.jpg`. Renders 1–13 compare
byte-identically with the already inspected round-zero renders.
All changed pages 14–18 were actually viewed; the metric definition,
two-directed transfer, equations and bibliography identifiers are legible,
without clipping, collisions or excessive spacing. The first attempt's
bibliography page was separately viewed before its line-breaking repair.

The current sources compare byte-identically with the complete final
snapshot `qa/revision_round1/attempt02/source/`.
The current `main.pdf`, `main_round1.pdf` and that snapshot's PDF
are identical. The baseline, historical source receipt and both full raw
review reports retain their original hashes.

## Round-one output binding

| File | SHA256 |
| --- | --- |
| `main.pdf` = `main_round1.pdf` | `fa509f73b5fc818493b0943e312846f1c9a366449fdf92c18d0dc0b67a04d841` |
| `references.bib` | `cd4a651d11cf0dbafbcfea0434d849ddcadb6bfb021425c4562e05acd80fe48e` |
| `sections/07_eventual_tower.tex` | `3da06d30779a59c5f87282e143d2f902e1283ea5c1af3476e7f2712f4e9b9b5d` |
| `qa/revision_round1/attempt02/source/main.bbl` | `7f2ad8b3f7aef75509ae3f00f1a260bc7ff4961176bbe9e7baf57a832e53b5a4` |
| `qa/revision_round1/attempt02/source/main.log` | `1be5839f3e3db2523d707981b4db02cea9c7b18b4891f978410d2d0ade72b8e1` |
| `qa/revision_round1/attempt02/compile.log` | `456ade8dd02cefe879c6f1ddbdcf79768727d59366bf7609927f330f4b815134` |
| `qa/revision_round1/source/main.pdf` (actual first attempt) | `120bc526ddee3459c91663212be825ff1e1571e23fc287a1a2d01c5e40a0bdb1` |
| `qa/revision_round1/source/main.log` (actual first attempt) | `9001cba9c32ab5ca4286005a940a0446cb4f41dcb3885183d35b22edbdd7c5ce` |
| `qa/revision_round1/compile.log` (actual first attempt) | `47451c35895fe95bd06ad197048eaf4f4226a552a4a5ac6d1b8dc17ecf2aab34` |

The full live source binding and pending status are in the single
`PAPER_IMPROVEMENT_STATE.json`. The selected improvement-loop
instructions govern preservation of actual reviews/versions and honest
state; the coordinator's scoped current-team mathematics workflow
supersedes external-model, numerical-score and ML-venue defaults.
No mathematical program, new agent, package installation, external model
API, formal evaluator, Git action, shared-proof edit or seal was used.

**Next gate:** the coordinator assigns the same E2 reviewer an actual
pass 2 on these revised source/PDF bytes. That pass has not yet occurred
and is not represented by a placeholder report or inferred approval.
