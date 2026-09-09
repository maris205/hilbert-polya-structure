# C425 first manuscript build receipt

2026-09-09 UTC. Status: **STABLE_BASELINE_FOR_TWO_MANUSCRIPT_REVIEWS**.
This is not the final two-fresh-build release gate, a manuscript review,
a mathematical execution, or a Route-A evaluation.

## Delivered baseline

- [Active PDF](main.pdf): 12 pages, 378,216 bytes; text/body pages 1–11,
  references page 12, no omitted proof appendix.
- [Baseline PDF](baseline.pdf) is byte-identical to the active PDF and
  to `build_initial_04/main.pdf` by actual `cmp` calls.
- Both PDF copies have SHA-256
  `aa6c4ee4bbc6f55bcf2934caccc927bf36aef872bf230466541c0f3de7b2f207`.
- `baseline_source/` preserves all 12 manuscript inputs plus `build.sh`
  from the stable pre-review version. These are genuine copied inputs,
  not a reconstructed revision history.
- Anonymous English `article`, 11pt, one-inch margins, US letter.
  No venue or artificial page limit was selected.

## Actual build sequence

Each command was run from this manuscript directory. `build.sh` requires
a fresh simple `build_*` output name and refuses an existing directory.
It invokes `latexmk -pdf -interaction=nonstopmode -halt-on-error
-file-line-error -outdir=<directory> main.tex` and retains the complete
console stream in that directory's `compile.log`.

| Command | Exit | Actual result and subsequent action |
| --- | --- | --- |
| `bash build.sh build_initial_01` | 12 | pdfLaTeX exited 1: missing `\end{equation}` after the displayed bounds in `sections/01_introduction.tex`; no PDF. Added the missing delimiter. The failed log and exact inputs remain in `build_initial_01/` and its `input_source/`. |
| `bash build.sh build_initial_02` | 0 | 12-page PDF, 377,783 bytes. One final underfull box in Table 1's first column. Exact inputs saved in `build_initial_02/input_source/`; changed that column to ragged-right. |
| `bash build.sh build_initial_03` | 0 | 12-page PDF, 377,779 bytes. No final warnings. All 12 pages visually inspected. Actual bibliography inspection then identified the omitted printed miscellaneous-entry DOI and duplicated C421 year; exact pre-correction inputs saved in `build_initial_03/input_source/`. |
| `bash build.sh build_initial_04` | 0 | Stable 12-page PDF, 378,216 bytes, after the two bibliography-format corrections. This is a changed-input citation-quality build, not another error-retry loop. |

Thus there was one failed build and three successful changed-input
builds. The initial error-repair sequence succeeded on its second
attempt; no failed attempt or warning was erased. Initial-pass undefined
cross-references in `compile.log` are normal multi-pass records, not
remaining defects: the final `main.log` is checked separately.

## Deterministic settings and environment

Every build used:

```text
SOURCE_DATE_EPOCH=1788912000
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
```

`main.tex` additionally sets `\pdfinfoomitdate=1`, `\pdftrailerid{}`
and `\pdfsuppressptexinfo=15`. The actual engine is pdfTeX
3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian), LaTeX2e
2021-11-15 patch level 1; latexmk 4.76. Poppler utilities report 22.02.0.
The build read `/etc/LatexMk`. The full TeX dependency record, including
system classes, packages and fonts, is preserved in
`build_initial_04/main.fls`; the bibliography run is recorded in
`main.blg`, and `.fdb_latexmk` records the build dependencies.

No two identical-input fresh builds were performed as a final release
test at this stage. The coordinator explicitly reserves that gate until
after the two manuscript review/revision passes.

## Actual quality checks

- `pdfinfo`: 12 pages, PDF 1.5, unencrypted, no JavaScript, author
  `Anonymous`, correct title, no creation/modification date fields.
- `pdffonts`: all 23 listed font resources embedded and subset, with
  Unicode mappings; zero unembedded fonts.
- Final `build_initial_04/main.log` and `.blg`: zero LaTeX/BibTeX
  warnings, undefined references/citations, overfull boxes or underfull
  boxes. The complete console and final engine logs are retained.
- `pdftotext -layout`: actual extraction stored as
  `build_initial_04/main.txt`; no `??`, `[?]`, TODO/FIXME/XXX or
  unresolved verification markers found.
- All nine section files and the shared macro file are included from
  `main.tex`; no orphan active section file. All six bibliography keys
  are cited, and all citations resolve.
- Visual inspection: all 12 pages of build 03 were rendered at 70 dpi
  and viewed individually. After the bibliography-only correction,
  build 04 pages 1–11 were independently rendered at the same scale
  and matched the inspected images byte-for-byte by 11 `cmp` checks.
  Build 04 page 12 was freshly viewed at 100 dpi. Text, displays,
  three tables, headers, page numbers and bibliography are readable
  with no observed clipping or overlap. Rendered pages are preserved.
- The front-matter and paragraph flow were reread in the rendered
  article. Every theorem item maps to the included proof locations in
  `DRAFT_HANDOFF.md`; no external Markdown file substitutes for a
  central argument.

The visual check is a baseline check, not a claim that unbuilt future
review revisions have been inspected. No mathematical program,
symbolic/numerical diagnostic, old certificate rerun, Git mutation,
external upload or formal evaluation occurred in this writing phase.

## Remaining gates

The writer stops after this handoff. Two actual nonauthor manuscript
review/revision passes, their coordinator adjudication, final identical-
input fresh builds and byte comparison, final-page inspection, evaluation,
release sealing and integration remain coordinator-owned.
