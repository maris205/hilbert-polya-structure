# C429 paper improvement log

Status: `round1_revised_pending_second_review`. One actual nonauthor manuscript review and one authorized author revision have occurred. No second review, second revision, numerical score, final-release build, or release approval is recorded.

The auto-paper-improvement-loop, paper-write, and paper-compile skills guide preservation, response tracking, and real compilation. The coordinator's explicit staged authorization overrides their automatic two-round, external-model, ML-venue, numerical-score, notification, and final-release defaults. This record stops at the required second-review checkpoint.

## Actual review record and authority

- Full raw manuscript review, retained without alteration: [reviews/round1/REVIEW.md](reviews/round1/REVIEW.md), 194 lines, SHA-256 `edbae0516b3ac82f0196ac14871b7b63094591392f932a18a44555c3a17e8b4f`.
- Nonauthor reviewer: `/root/c429_e4_cover_review`. The review records a 2026-09-09 20:59 UTC checkpoint and recommends **Minor revision**, with zero Critical, zero Major, and three Minor findings. It states that the central theorems and complete typeset proofs pass that review. Numeric score: not supplied; calibration: `NOT_CALIBRATED`. This is current-team AI review, not human peer review, a calibrated evaluation, or publication acceptance.
- Full raw citation audit, retained without alteration: [reviews/citations/REPORT.md](reviews/citations/REPORT.md), 195 lines, SHA-256 `2ecb0559cee12b7a75ce3acdc65f5b5a97a59191476bd8290aa6694ad834d7ee`. Its bounded result requests no additional citation must-fix.
- The author read both reports in full for this revision; W1–W3 and the source-access qualifications were checked before editing. The coordinator explicitly adjudicated them and authorized only W1–W3, preservation of the original PDF, actual recompilation, checks, and this handoff record. No fresh review or source search was substituted for that adjudication.

The linked files are the complete raw reports, not excerpts or replacement summaries. Their hashes were checked before editing and again after compilation. They remain immutable inputs under this task's freeze. Their full read extents, strengths, detailed proof checks, access qualifications, and other observations remain available there.

## Round 0 preservation

Before any manuscript edit, all 23 frozen baseline files passed `sha256sum --check --status BASELINE_FILES.sha256`. The active baseline PDF was compared with `snapshots/author_baseline/main.pdf`. Since `main_round0_original.pdf` did not exist, it was copied from that frozen PDF, then hash-checked. No existing unequal file was overwritten.

`main_round0_original.pdf` SHA-256: `118733318d139821d5cb29ab8deccc9d46fe577230563fbd38858df7ea431a02`.

The original `AUTHOR_RECORD.md`, `SOURCE_AND_PDF.sha256`, and `BUILD_INPUTS.sha256` are retained unchanged as **round-0 records**, not current-round validation records. The frozen snapshot, original build attempts, raw reviews, and upstream research files have not been edited. The current round's records live under `revisions/round1_author_revision_01/` and in the sole live state file `PAPER_IMPROVEMENT_STATE.json`.

## Round 1 findings and implemented responses

| Finding | Severity and original anchor | Authorized repair actually made | Author check / remaining gate |
|---|---|---|---|
| W1 | Minor; abstract, former `main.tex` lines 32–35 | The finite-certificate clause now says “for any integer `M >= 1` and `deg h <= M`.” | Domain matches Theorem 1.2; all bounds and zero-input conventions unchanged. Visible on revised p. 1. Implemented, pending reviewer verification. |
| W2 | Minor; Section 1.1, `sections/01_introduction.tex` lines 151–154 | “equal to the leading normal coefficient” becomes “equal to a nonzero scalar multiple of the leading normal coefficient,” retaining the characteristic-power clause. | Correctly summarizes the unchanged `alpha a_D^P` in Proposition 6.1; no assertion that `alpha=1` was introduced. Visible on revised p. 3. Implemented, pending reviewer verification. |
| W3 | Minor; Section 1.1, residue citation at line 138 | Locator is now “Section 4 of the accessible preprint.” | Published reference and accessible-preprint link remain unchanged. Revised p. 3 states the inspected version explicitly; no published-numbering claim is inferred. Implemented, pending reviewer verification. |

Only `main.tex` and `sections/01_introduction.tex` differ among the ten active mathematical/BibTeX files. The other eight files were byte-compared with the frozen baseline and match. All theorem, proof, parameter, derivative-test, ordinary-cycle, finite-bound, bibliography-data, and source-access statements outside these three repairs remain unchanged.

Exact source differences are retained in [SOURCE_DIFF.patch](revisions/round1_author_revision_01/SOURCE_DIFF.patch); the full extracted-text comparison is retained in [PDF_TEXT_DIFF.patch](revisions/round1_author_revision_01/PDF_TEXT_DIFF.patch). The latter shows only the requested wording and resulting reflow through page 4. Separate extraction of pages 5–16 has identical SHA-256 for baseline and round 1: `cbadb66767d331cb2f7ca627b34dc01be1b674e54c2262c6a1fb87aa919f88f0`.

The review's substantive strengths and mathematical checks require no manuscript edits beyond W1–W3. The optional Li–Zhang bibliography spacing was deliberately left unchanged under the narrow authorization.

## Actual fresh revision build

The path `revisions/round1_author_revision_01/` was explicitly checked not to exist, then created. All ten revised input files were copied to `source/` before compilation and to the initially empty `build/`. No old auxiliary file was carried into that build directory and no cleanup command deleted previous evidence.

Working directory: `revisions/round1_author_revision_01/build/`.

```sh
set -o pipefail
SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex 2>&1 | tee compile.log
```

This was one actual successful latexmk invocation, with three pdfLaTeX passes and two BibTeX passes. The invocation ran during 2026-09-09 21:14–21:15 UTC. The fixed epoch is build metadata, not a claim that the revision occurred at that epoch. Installed tools were used without installation. Full invocation output, final-pass log, bibliography output/log, auxiliary files, recorder, and latexmk database remain in `build/`.

The converged PDF has 16 letter-size pages and 423,936 bytes. It was copied to `main_round1.pdf` and live `main.pdf`; these and `build/main.pdf` are byte-identical. Live auxiliary/log copies were refreshed from this real build. No `main_round2.pdf` was created.

Round-1 PDF SHA-256: `635f6868081c83ac0d76adde5ffe6a80e8eb7077a5c72dd44f7e7f19d75a36c6`.

## Actual verification

- Final log: zero LaTeX errors, undefined references/citations, multiply-defined labels, overfull boxes, or hyperref warnings. First-pass unresolved cross-references remain honestly visible in the full invocation log; they converged.
- One pre-existing underfull hbox remains, badness 2173, `main.bbl` lines 33–38, Li–Zhang bibliography entry. It is readable and not suppressed. No new warning was introduced.
- `pdffonts`: all 25 listed font resources embedded. `pdfinfo`: anonymous author metadata, no encryption or PDF JavaScript, 16 letter pages.
- The complete 816-line `pdftotext -layout` output was screened for unresolved markers and compared against the full baseline extraction. No `??`, `[?]`, `[VERIFY]`, `TODO`, `TBD`, or `FIXME` occurs in the text or active source. The entire resulting diff was read.
- Revised pages 1–4, affected by the edits/reflow, and bibliography pages 15–16 were freshly rendered at 96 dpi and individually viewed. The new cap, scalar wording, locator, table, mathematical symbols, page-break continuations, and references are legible without clipping or collisions. This is an affected-page author check, not a new independent all-page review or structural-preflight PASS.
- The selected page images and full text remain in `visual/` and `main_round1.txt`. The 171-entry `BUILD_INPUTS.sha256` is relative to this revision's `build/`; it covers recorder inputs and the added bibliography/compiler/render-tool inputs. `SOURCE_REVIEW_INPUTS.sha256` records the live source/PDFs, immutable review hashes, and selected skills, with paths relative to the paper directory.
- After the build, all 23 frozen baseline checks still passed and `main_round0_original.pdf` still matched the frozen original. Both full raw review hashes remained unchanged.

## Preserved qualifications and next gate

The 1994 Levin–Sodin–Yuditskii full text remains unavailable; its abstract-only access, direct 1998 attribution, and lack of proof dependency are unchanged. The citation audit's other limits also remain: failed individual DOI opens, IOP publisher-status access, unavailable Retraction Watch database screening and Crossmark clearance, its unavailable PDF structural preflight, and the neutral Li–Zhang arXiv administrative overlap note. A bounded public screen is not a guarantee of unretracted status, validity, or priority. This author revision does not turn any unavailable check into PASS or transfer the citation audit wholesale to the changed PDF.

The author has implemented all three authorized minor repairs and performed the documented technical checks. Their independent closure remains for the **same nonauthor reviewer's actual second manuscript review**, assigned by the coordinator. Status is `round1_revised_pending_second_review`; author editing is frozen at handoff. The source snapshot and real build evidence are retained under the revision directory, with `FILES.sha256` as a technical file inventory rather than a release seal. Its paths are relative to the paper directory; it also binds the single live improvement log/state, the PDFs, and the immutable review inputs without duplicating a live state file.

No new agent, external model/API, upload, mathematical program, Git operation, formal evaluation, second review, final release build, or publication action was performed in this revision.
