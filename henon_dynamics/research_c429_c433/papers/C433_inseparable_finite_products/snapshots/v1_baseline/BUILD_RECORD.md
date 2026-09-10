# C433 first-build record

Status: first manuscript baseline built, checked, and frozen for review.
Final checks completed by 2026-09-09 20:44:53 UTC (actual tool clock).

The paper uses an anonymous English 11 pt article with one-inch margins,
modular section files, and numbered citations. The complete central proof
is typeset in the article. No external venue's ML page limit or artificial
figure/table quota is applied. The single comparison table clarifies the
distinct certificate interfaces. No generated figure is required.

Available tools were checked before authoring: `/usr/bin/pdflatex`,
`latexmk`, `bibtex`, `pdfinfo`, `pdffonts`, `pdftotext`, and `pdftoppm`.
Required LaTeX packages were found with `kpsewhich`; none was installed.
Engine: pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian.
Latexmk: version 4.76, 20 November 2021.

Build environment is fixed to `SOURCE_DATE_EPOCH=1788912000`, `TZ=UTC`,
and `LC_ALL=C`. This is a deterministic PDF timestamp setting corresponding
to 2026-09-09 00:00:00 UTC, not the actual wall-clock execution time.
The actual `pdfinfo` output displays the equivalent instant as
2026-09-09 08:00:00 CST. It is not the wall-clock build time.

The first PDF is a review input. It is not either of the two final clean
reproducibility builds and does not certify zero manuscript-review issues.

## Actual build attempts

All commands were run from this C433 paper directory. No old build was
cleaned or deleted. Distinct build directories preserve the actual attempts.

1. Initial attempt:
   `env SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/first main.tex`.
   It exited 12 because `\mathscr` was undefined at the extractor display.
   The engine log is preserved at `build/first/main.log`. The command's
   stdout was returned by the execution tool, not separately redirected.
   No PDF was produced by this attempt. First-pass unresolved references
   and citations were expected before the fatal stop and are not hidden.
2. Corrected attempt:
   `env SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/second main.tex 2>&1 | tee build/second/compile.log`,
   run with shell `pipefail`. The extractor notation was changed to the
   already available `\mathcal`; the comparison table was set ragged-right
   to remove an underfull box. This exited 0 and produced an 11-page PDF.
   Its final engine pass had no warnings. The full output, engine log,
   bibliography log, PDF, extracted text, and all 11 page renders remain.
3. Author's final baseline formatting pass:
   `env SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build/third main.tex 2>&1 | tee build/third/compile.log`,
   again with `pipefail`. This retained the complete main theorem on one
   page, clarified the abstract's product-index range and one introduction
   sentence, and printed verified DOI/preprint links with explicit
   preprint-version section attribution. No mathematical assertion or
   bound changed. The command exited 0; the final PDF was available by
   the actual clock check at 20:42:45 UTC. Its normal first-pass
   cross-reference/citation warnings resolved through latexmk's passes.

The two successful author builds above are baseline authoring attempts,
not an assertion that the two later clean reproducibility gates passed.
No fourth baseline compilation or manuscript revision was performed.

## Final baseline checks

- `main.pdf` is the actual `build/third/main.pdf`: 11 pages, 374341 bytes,
  PDF 1.5, US Letter, unencrypted, with no JavaScript or forms reported.
- All 22 font entries reported by `pdffonts` are embedded, subsetted,
  and have Unicode mappings. The full output is
  `build/third/pdffonts.txt`.
- `build/third/main.log` and `build/third/main.blg` contain zero matches
  for warnings, overfull/underfull boxes, undefined items, fatal errors,
  or errors. This checks the final engine/BibTeX logs, not the cumulative
  multipass stdout, which truthfully retains resolved early warnings.
- The extracted PDF and source contain no `??`, `[?]`, `[VERIFY]`, `TODO`,
  or `TBD` markers. Both numbered bibliography entries and all cross-
  references resolved. The generated `.bbl` was read back.
- `main.tex` includes all eight actual section files; no orphaned section
  was found. The bibliography contains only the two source-audited entries.
- All 11 final pages were rendered with
  `pdftoppm -r 95 -png main.pdf build/third/visuals/page` and individually
  viewed. Equations, table, theorem, fonts, margins, and bibliography were
  legible without clipping or overlap. The complete theorem now begins
  page 3 rather than splitting its enumerated statement across pages.
- The text and complete proof were read through in the generated PDF/text.
  Main text and the development disclosure continue onto page 11, where
  references also begin. There is no appendix or omitted proof payload.
- Frozen report/reviewer/source-report hashes in `SOURCE_AUDIT.md` were
  recomputed and remain unchanged. No older research artifact was edited.

## Frozen review input

The root-requested `main_round0_original.pdf` is byte-identical to
`main.pdf`, checked with `cmp`. The exact sources, bibliography, PDF,
original-PDF copy, and audit records are preserved in
`snapshots/v1_baseline/`; section-copy equality was checked with `diff -qr`.
The original baseline and current source/bibliography/PDF are frozen
pending root's manuscript-pass-1 assignment. This is a local author
baseline record, not the batch's canonical final release manifest or seal.

| File | SHA256 |
| --- | --- |
| `main.pdf` and `main_round0_original.pdf` | `8e58c361b89fe132183451f08b4817699ac02164e224a8cc6589d62e3bdb99f7` |
| `main.tex` | `a8bc69d20c0e71385fbaed7e3a9c16987226af49b49d60142a407cbe5ee16dbf` |
| `references.bib` | `89c47eaeca9645bc2579504a9edb789f5ef6225d67b868da13b07ece4f44d128` |
| `sections/01_introduction.tex` | `057a027bfd646613a80dcdd9f1375f7ffa061d39d9664ddec2486dddae10f682` |
| `sections/02_statement.tex` | `3d6d5d65a715adb9a0c98f6257ab4f122491f02e81d9ff6e7458c8a0217b9f2a` |
| `sections/03_cycles.tex` | `49bccc2a0ba02bb8634b78cdc69cd38fa217691db0df7df27ea4ab47e6f2486c` |
| `sections/04_extractor.tex` | `20fc9ff6342288314cd71efcbdc1f9388455245b8186bf749809c103e662cb69` |
| `sections/05_transfer.tex` | `d56317d4ec6ad9375b564472a48564fbeef60c314e4e533d2671fc94d891769e` |
| `sections/06_rank.tex` | `53141c1b73f968333b4af2c180c678a50967df211c78f8190d95935b254fcc88` |
| `sections/07_decision.tex` | `88b84763f2ab5919de79d8d31b73ff40f6cfd06664b03e308dfb01c6b9477f4c` |
| `sections/08_conclusion.tex` | `d3b4d85628883a31ada3e68e211528cdf70ac9350f3d453128e3195a178d8ffb` |
| `SOURCE_AUDIT.md` | `fc5a379ed7889cb256aa0195e4b95988f3445a6446ad5c9238a3c8c77687104c` |

No mathematical experiment, new agent, external model/API, package
installation, Git operation, formal evaluator action, shared final
manifest/seal, or external submission occurred. Manuscript review and
release acceptance remain with the coordinator.
