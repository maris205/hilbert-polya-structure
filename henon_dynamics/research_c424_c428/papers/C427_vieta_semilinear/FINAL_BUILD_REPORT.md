# C427 — final identical-input double build

2026-09-09 UTC. Coordinator-owned typesetting and final document checks.
**FINAL_BUILD_COMPLETE_PENDING_SEAL**. Both manuscript reviews were
accepted before these builds. This report is the final-build authority;
the earlier build ledger and improvement records retain their historical
milestones. It does not award a mathematical or Route-A grade.

## Actual builds, not copies of old build directories

The complete `build_final.sh` was read before use. It accepts only the
two stated labels and refuses an existing output directory. Both paths
were absent before invocation; neither build reused an auxiliary file.

| Actual command | Engine-build UTC start/end | Top-level exit | pdfLaTeX / BibTeX | Final PDF |
| --- | --- | ---: | ---: | --- |
| `bash build_final.sh final_01` | 07:15:03 / 07:15:05 | 0 | 3 / 2 | 13 pages, 346694 bytes |
| `bash build_final.sh final_02` | 07:19:55 / 07:19:57 | 0 | 3 / 2 | 13 pages, 346694 bytes |

The saved start/end timestamps bound the engine invocation; text/font
extraction and rendering follow inside the same successful wrapper.
Each build actually produced 12 pages / 314141 bytes in pass 1,
13 / 346794 in pass 2 and 13 / 346694 in pass 3. Complete raw output is
retained in each `compile.log`, including normal first-pass unresolved
references. The final logs, not the historical raw warnings, determine
convergence. There was no failed final invocation, retry or third final
directory. The final pair totals six pdfLaTeX and four BibTeX executions;
the mathematical certificate/exploration execution count increased by zero.

## Fixed input and byte identities

The unchanged ten manuscript inputs are the nine TeX files and one
bibliography in [INPUT_MANIFEST.sha256](INPUT_MANIFEST.sha256), SHA256
`c802d78cd7ec2e4d6c3a87a1c243c657e14d7247f78514f08f6075d52627b1f9`.
The wrapper SHA256 is
`de7c38fd7df14ebb93108995114a16a4ddf95cd793b79885f73631b36403700d`.
Both wrappers ran `sha256sum -c` before and after compilation, saved
those manifests, and compared them. Cross-build before/after manifest
comparison also passed. The wrapper is typesetting-only and does not
import or execute any mathematical program.

Each independent deterministic `source.tar` contains all ten inputs,
the wrapper and the manifest (12 regular files, plus directory entry).
The two archives compare byte for byte, SHA256
`45ea5513ef46f3f061c4e8c1ee6f043abb2e90f68841e6f897d3a8e68d54e0b8`.
For every manuscript input I additionally extracted and compared the
two final archive members and the already-reviewed `round1_revised`
archive member against the active source: all 30 member comparisons
passed. Neither a proof edit nor an undisclosed bibliography edit was
introduced after review.

`cmp builds/final_01/main.pdf builds/final_02/main.pdf` returned 0.
Both final PDFs have SHA256
`cae339b829dd8a4ca0c57accc75b3a9a3ced62173f49402e853e6d63c2d91bd1`.
The active `main.pdf` was explicitly selected by copying `final_02`;
it matches that file and the already-reviewed first revision. The
no-change `main_round2.pdf` is a review-stage alias, not a new build.

## Environment and actual document inspection

Both invocations use `SOURCE_DATE_EPOCH=1788912000`,
`FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`. Source-level PDF metadata
suppression remains unchanged. Archives use sorted members, mtime
1788912000, owner/group 0 and numeric ownership. Observed tools:
latexmk 4.76; pdfTeX 3.141592653-2.6-1.40.22;
BibTeX 0.99d; TeX Live 2022/dev/Debian; Poppler 22.02.0;
Linux 5.15.0-78-generic x86_64.

Each final directory retains the engine/BibTeX logs, `.aux`, `.bbl`,
recorder/build metadata, complete console, `pdfinfo.txt`, `pdffonts.txt`,
`main.txt` and all 13 newly rendered page PNGs at 85 dpi.
Both final engine and BibTeX logs passed the wrapper's check for
Warning, Error, undefined, Overfull, Underfull and fatal diagnostics.
No diagnostic suppression or log deletion was used.

All 19 font resources are embedded. The document is an unencrypted,
letter-size PDF 1.5 with anonymous authorship metadata. I read all 645
lines of `final_02/main.txt`; a fresh extraction from that PDF matched
the saved text. The complete pair has identical bytes, so one all-page
inspection covers the identical selected PDF, not a different revision.

I actually viewed every newly rendered `final_02` page 1–13. Pages 1–2
contain the complete statement and ownership table; 3–4 the block proof;
5–6 classical finite constructions; 7–8 tagging and least-period labels;
9–10 source counts, limitations and references; page 11 the remaining
references; and 12–13 the complete auxiliary height argument. The short
reference-only page 11 follows the intentional clear page before the
appendix. Formulas, tables, links and special symbols are readable;
there is no clipped object, missing item or unresolved citation marker.
No venue or externally imposed page-limit certification is claimed.

## Handoff and limits

All local C427 mathematical/TeX inputs and the final PDF are frozen.
The remaining coordinator operations are batch-level evaluation
adjudication, exact release membership verification and authorized Git
integration. No old C421 certificate, exploratory atlas, external source
service or other paper was modified or rerun for these final builds.
Byte reproducibility certifies this document artifact, not worldwide
novelty, human peer review, Euler factors or a Hilbert–Pólya model.
