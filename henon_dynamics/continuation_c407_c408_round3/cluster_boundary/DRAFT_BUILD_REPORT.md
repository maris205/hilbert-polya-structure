# C408 author draft-build report

2026-09-06. Status: `DRAFT_COMPILE_PASSED`.
Scope: author-side draft compilation and bounded log/font/source checks,
not final dual-build verification, all-page visual QA, or release acceptance.

The source entry is [paper/main.tex](paper/main.tex), with one input file
per section, shared macros, and three inline bibliography entries. The
[paper plan](PAPER_PLAN.md) was read and accepted by the root coordinator.
The writing skills supplied the claim--evidence mapping, modular complete
proofs, and explicit citation/limitation discipline; the authorized local
mathematical-manuscript scope superseded their default ML venue, length,
figure, and external-review suggestions.

## Actual builds

Both output directories were newly created with `mktemp -d
/tmp/c408-draft-XXXXXX`. Commands ran from the `paper` source directory,
using the literal returned output path. The build command was:

```sh
SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir=OUTPUT_DIRECTORY main.tex
```

Shell `pipefail` preserved the exit status while `tee` retained the full
output in `OUTPUT_DIRECTORY/latexmk.stdout.log`. The final TeX engine log
is `OUTPUT_DIRECTORY/main.log`. Normal first-pass unresolved references
were resolved by latexmk's subsequent pass and remain visible in the
unmodified complete stdout logs.

| Draft | Actual directory | Exit | Result |
|---|---|---:|---|
| Initial | `/tmp/c408-draft-N5YW3x` | 0 | 12 A4 pages; two overfull filename boxes remained |
| Layout-corrected | `/tmp/c408-draft-te1OpG` | 0 | 12 A4 pages; clean final TeX log |

The initial final-pass warnings were two `Overfull \hbox` findings of
85.24197 pt and 72.30597 pt in the supplementary-file paragraph of
`sections/controls_limits.tex`. Long unbreakable `\texttt` file names
were replaced with breakable `\path` names using `apply_patch`. No
mathematics, citation, computational result, or scope statement changed
between these drafts. Both temporary directories and their raw logs are
preserved; the initial draft has not been overwritten or described as
warning-free.

## Layout-corrected draft receipt

- PDF: `/tmp/c408-draft-te1OpG/main.pdf`.
- Pages: 12; page size: 595.276 by 841.89 points, A4.
- File size: 374170 bytes.
- SHA256: `9d94e32bff36110a16822b7cc9c784ff1c200caa72f888ca71aa5c48b7620621`.
- Final `main.log` scan for `Warning`, `Overfull`, `Underfull`, `undefined`,
  and leading `!`: no matches (`rg` exit 1, its ordinary no-match status).
- `pdffonts`: all 21 listed font resources have `emb=yes`; no Type 3 font.
- All new TeX files were scanned as text for C0 control bytes other than
  tab, LF, and CR, plus DEL: no matches. An accidental NUL in the initial
  formal-reduction source had already been removed with `apply_patch`
  before either build.
- Tool versions reported during compilation: latexmk 4.76 and pdfTeX
  3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian.

The preamble uses explicit A4 geometry and guarded pdfTeX controls to omit
dates, omit the trailer identifier, and suppress path-sensitive pTeX
metadata. This records the settings used; it is not a claim that two
unchanged-source fresh builds have already been compared. The two drafts
above have a genuine intervening source layout change.

## Review handoff and remaining ownership

The root coordinator's full-source review requested two explicit hypotheses
in the general lemmas: product factors belong to the maximal ideal, and the
eliminated potential satisfies `dP(0)=0`. Both were implemented before
compilation; they hold in every application. The coordinator reported the
affected checks closed and no remaining mathematical or citation blocker
after reading the complete manuscript and actual primary citation contexts.
Its formal review record is separately coordinator-owned.

At the coordinator's request, paper source is now frozen pending any precise
correction request. No draft PDF has been copied into the release payload
by the author. Final two-fresh-directory compilation, PDF comparison,
text/all-page visual QA, final PDF placement, evaluation and sealing remain
coordinator-owned. No sealed round-2 file was changed or rerun, and no
unchanged mathematical control was rerun merely for manuscript production.
