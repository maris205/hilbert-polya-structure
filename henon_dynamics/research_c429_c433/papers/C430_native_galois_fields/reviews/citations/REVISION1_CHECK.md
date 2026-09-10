# C430 citation revision-1 check

Checked 2026-09-09 21:33 UTC against the actual revision-1 files below.
Scope: the coordinator-authorized, bounded ARS academic-paper Phase 5a
citation follow-up. This is not a second mathematical manuscript pass,
new source-applicability review, release seal, or full-pipeline certificate.
The original 235-line [citation report](REPORT.md) remains immutable.

## Result

**C430-CIT-01 through C430-CIT-04 are CLOSED ON THE BOUND REVISION-1
BYTES.** All four repaired DOI URLs are present in the actual BBL and
PDF text, visibly legible in the existing bibliography renders, and
correct in the PDF's actual link destinations. The approved Keating-2009
consulted-version note is also correctly implemented. No new citation
must-fix was found within this affected-output check.

Nine bibliography entries and fourteen citation commands remain, with
the same keys and alphabetical `plain` ordering and no citation orphans.
Retraction coverage remains partial: **RETRACTION_DATABASE_UNCHECKED /
ACCESS_UNAVAILABLE**. Closing metadata repairs does not close that
separate limitation or certify successful access to every destination.

## Actual checks and read extent

The complete ARS router, academic-paper workflow, citation-compliance
role, and citation-format switcher were used; the assigned report-only
scope overrides automatic manuscript correction. Repository and batch
boundaries were retained. No other workflow phase was invoked.

Read in this follow-up: the complete original citation report, the
154-line `PAPER_IMPROVEMENT_LOG.md`, the 121-line
`PAPER_IMPROVEMENT_STATE.json`, all 95 lines of the current bibliography,
and all 73 lines of the final revision BBL. Both complete source diffs
against the baseline were read: `references.bib` and
`sections/07_eventual_tower.tex`. The latter adds only the ordinary
metric/two-directed Hausdorff definition; its citation interface and
theorem/proof text are unchanged. The first 85 lines of the current
Section 7, including the imported interface, were also read directly.

Read-only byte comparisons confirm that all twelve manuscript source
files equal the final build snapshot. The ten sources other than those
two changed files equal their baseline copies. The actual final AUX
citation, bibliography-style/data and numbered-entry records were
checked. This is reuse of the first audit's full-source reading for
unchanged content, not a claim to have reread every proof in this check.

Fresh `pdftotext -layout` output from the actual C430 PDF was read for
the entire bibliography and surrounding closing prose. Both existing
final bibliography JPEGs were actually viewed. No clipping, collision,
missing identifier or misleading version label was observed there.
The display line breaks in the Debaisieux and LRL DOI URLs preserve
the complete identifiers. `pdfinfo -url` independently confirms their
full URI targets without spurious line-break characters or terminal
punctuation. `pdftohtml -stdout -i` also exposes the actual companion
PDF link, which is not listed by `pdfinfo -url`.

The actual C430 PDF is 18 pages and 408109 bytes. No new build, rendering,
PDF-reading preflight, all-page visual inspection or compiler-log audit
was run. The author's two-build/all-page account remains its own
receipt. Locators below are TeX/BBL line numbers and reference numbers,
not certified PDF page anchors.

## Finding-by-finding closure

Primary metadata and cited-version evidence here reuse this reviewer's
actual primary accesses in the original audit. No new broad search,
publisher access, retraction query or version-equivalence check is
represented as having occurred in this follow-up.

| Finding | Current source / BBL locator | Actual repaired output and evidence | Status |
| --- | --- | --- | --- |
| C430-CIT-01, [4] | `references.bib:40–53`; BBL `26–32` | Elder–Keating is now *Archiv der Mathematik* **126(5)** (2026), 461–469, with visible/correct destination `https://doi.org/10.1007/s00013-026-02234-1`. This matches the previously checked [Springer article](https://link.springer.com/article/10.1007/s00013-026-02234-1) and [issue record](https://link.springer.com/journal/13/volumes-and-issues/126-5). The note expressly retains [arXiv:2503.16830v1](https://arxiv.org/abs/2503.16830v1), 21 March 2025, for theorem/section numbering. Moving the DOI to the end of the note changes neither identity nor qualification. | CLOSED |
| C430-CIT-02, [5] | `references.bib:13–25`; BBL `34–39` | The DOI `https://doi.org/10.1016/j.jnt.2005.03.003` is stored, visibly printed, and an exact PDF URI target. It matches the original audit's [publisher-indexed record](https://www.sciencedirect.com/science/article/pii/S0022314X05000831). The author-version URL [math/0312391v2](https://arxiv.org/abs/math/0312391v2) remains. The original direct-publisher 403 is not reclassified as successful access. | CLOSED |
| C430-CIT-03, [7] | `references.bib:1–12`; BBL `50–57` | The formerly suppressed DOI now prints as `https://doi.org/10.1112/S0010437X15007575`, with that exact PDF URI target, matching the original [Cambridge landing-page check](https://doi.org/10.1112/S0010437X15007575). The [arXiv v3](https://arxiv.org/abs/1311.4478v3) theorem-numbering qualification is preserved. | CLOSED |
| C430-CIT-04, [3] | `references.bib:54–63`; BBL `18–24` | The visible/correct destination `https://doi.org/10.48550/arXiv.2603.03873` is expressly labelled **arXiv DOI**. The cyclo-tame title, [v2 URL](https://arxiv.org/abs/2603.03873v2), and 22 April 2026 version date remain correct against the original primary version-page check. No journal publication is invented. | CLOSED |

The approved optional [6] change at `references.bib:26–39` / BBL
`41–48` adds [arXiv:0805.2932v1](https://arxiv.org/abs/0805.2932v1),
**19 May 2008**, and explicitly binds theorem/section numbering to that
consulted author version. The date agrees with the primary version
page and HTML header actually inspected during the first audit. It
does not replace the correct 2009 journal issue year. The publisher
URL containing DOI `10.5802/jtnb.693` remains visible and intact.

LRL issue `1` and a canonical DOI display for [6] were optional in the
original report, not unresolved mandatory findings; their omission
does not reopen the four repairs. Citation keys and bibliography order
were preserved, and no redundant preprint entry was introduced.

## Current companion binding and unchanged interface

The actual C430 PDF contains both destinations
`../C431_optimal_cycle_measures/main.pdf` and
`../C431_optimal_cycle_measures/main.tex`. From the delivered C430 paper
directory, these resolve to the real C431 files hashed below. This
checks package destinations, not a universal browser/viewer ability
to follow local-file links. The companion must still accompany the
distributed paper; a nested QA snapshot or isolated C430 PDF is not
the complete cross-linked delivery layout.

For C431, read the complete current `main.tex` and introduction, and
fresh actual-PDF text containing Theorem 1.1. The introduction's full
baseline diff adds notation and narrows a background attribution;
the theorem itself is unchanged. Its title/number and compactness,
full-sequence Hausdorff limit, and infinite native adding-machine
conclusions still match C430's explicit interface. Sections 5 and 6
compare byte-identically with baseline and retain the exact hashes
of the proofs fully read in the original citation audit. They were
not re-proved or counted as a new mathematical review here.

The C431 PDF hash below updates the companion binding for this check;
it does not overwrite the first report's historical binding. The
bibliography still honestly identifies C431 as an anonymous,
unpublished companion, not accepted or externally peer reviewed.

## Exact input binding

Paths are relative to the C430 paper directory unless prefixed `C431/`;
that prefix denotes `../C431_optimal_cycle_measures/`. Log/state hashes
identify the receipts read at this check, not an immutable future
coordinator status. Their later authorized status updates do not alter
the PDF/bibliography closure binding.

| Actual input | SHA256 |
| --- | --- |
| `main.pdf` = `main_round1.pdf` = `qa/revision_round1/attempt02/source/main.pdf` | `fa509f73b5fc818493b0943e312846f1c9a366449fdf92c18d0dc0b67a04d841` |
| `references.bib` | `cd4a651d11cf0dbafbcfea0434d849ddcadb6bfb021425c4562e05acd80fe48e` |
| `sections/07_eventual_tower.tex` | `3da06d30779a59c5f87282e143d2f902e1283ea5c1af3476e7f2712f4e9b9b5d` |
| `qa/revision_round1/attempt02/source/main.bbl` | `7f2ad8b3f7aef75509ae3f00f1a260bc7ff4961176bbe9e7baf57a832e53b5a4` |
| `qa/revision_round1/attempt02/source/main.aux` | `fb6ef68557ecdcf80a2d1265b51cb583781c12992a3c2a0e77f19a40b22e47ce` |
| `qa/revision_round1/pages/page-17.jpg` | `1f7d62d76c548a5742439163bc2de547993ebe121f0feebcbec8f62d8ca5f57f` |
| `qa/revision_round1/pages/page-18.jpg` | `cad92462dbc2fcf7f233b62f87c2fda998b4e751f998236ab7ba3dc86f847ec9` |
| `PAPER_IMPROVEMENT_LOG.md` | `e13d3cbaa22d090e66faefb85fb159ecc3a392df01b7ecd5072acd91471042fd` |
| `PAPER_IMPROVEMENT_STATE.json` | `4d5e6800f1cdd79d37bb2b9585d7895cbb9338d6358ff84a0c6f678260820ff4` |
| `C431/main.pdf` | `dba1f729d54b44b12cd800273041e3a514846613a4cdad0cd2454d9aa28a0915` |
| `C431/main.tex` | `665ecb1d163a5345d5871bb5c8155ca99eb0a30f5e367840d600d52c65ab1c81` |
| `C431/sections/1_introduction.tex` | `40d85d94398f31bb838c5a9779f7533f22523b7de141763b4e73506b524e1308` |
| `C431/sections/5_compact_limit.tex` | `3eaf9f89737f7d62791a4ec83a95afccd470afcc77cf914dfdc781f58b8e938c` |
| `C431/sections/6_adding_machine.tex` | `a665bb19ca294784768d01353c35b83f92db3be4def838bb67b7818a75be3c8b` |
| Original `reviews/citations/REPORT.md`, unchanged | `6fed8b6c647e0168065c52dc1188ce888fbd7bbca680059b96b27b213be8c62a` |
| Original `SOURCE_BUILD_RECORD.md`, unchanged | `5f022836036b81e2e79b2cf4bc3100e9ae8891ef1b53e4df3c9700ff652a0957` |
| `baseline/main.pdf` = `main_round0_original.pdf`, unchanged | `54bc61f0d9c89405047fdf116bbcaf38d9e658c6d401b70862b22659f2574c8e` |

## Limits and handoff

All original access limits remain: Retraction Watch's endpoint was
unavailable; no database clearance or article-specific CrossMark record
was obtained. The primary-page/retraction searches were partial, not
exhaustive negative evidence. Keating-2006's direct publisher access
failed; Elder–Keating's subscription VOR proof was not read; and the
Keating-2009 publisher-PDF retrieval failed. Author-version numbering
is now explicit where authorized, not certified equivalent to every
published version. No new withdrawal, forward-citation, plagiarism,
worldwide-priority or comprehensive live-link search was performed.

Only this new follow-up report was written. No manuscript, author log,
state, original report, baseline, shared proof/index, evaluator or Git
state was edited. No mathematical program, new agent, external-model
upload, API client, package installation, build or preflight was run.

The bounded citation-repair gate is complete for the exact revised
bytes above. Separate manuscript review, final build/release checks,
and coordinator integration remain separate authorities and tasks.
