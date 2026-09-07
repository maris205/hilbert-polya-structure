# C416 final build and every-page visual receipt

Status: **PASS — two fresh final builds are byte-identical; all 15 final
pages actually viewed.** Execution date: 2026-09-07 UTC. This work was
explicitly delegated by the root coordinator to the nonlinear-geometry
worker. The builds and visual inspection reported here were performed by
that worker, not personally by the root coordinator.

The [nonauthor manuscript review](REVIEW_MANUSCRIPT.md) was already
PASS/CLOSED before this release execution. No mathematical source or
claim was changed. The original `build_author/` directory and historical
author/review receipts are preserved.

## Final artifact and input identities

The delivered [main.pdf](main.pdf), pass-a PDF and pass-b PDF are all
**15 pages, 338,853 bytes**, with SHA256:

```text
31259d5c108bcf05b3fa1313a919d7559a9bdfbcd0f5deec56f5ba67e1167a55
```

The [source identity list](final_build/SOURCE_SHA256SUMS) contains all
12 actual inputs: `main.tex`, `math_commands.tex`, `references.bib` and
the nine section files. Its SHA256 is:

```text
aa4843e4acf40b166c8413fb8352133224b834154292230dcefb360f816d17af
```

After compilation, `sha256sum -c final_build/SOURCE_SHA256SUMS` passed
all twelve inputs. Each current source was then compared with its copy
in both clean directories: **24 source-copy `cmp` operations exited 0**.
The two PDFs also passed `cmp`; after copying pass a to the delivered
`main.pdf`, a separate delivered/pass-a `cmp` exited 0. The complete
returned results are in [comparisons.log](final_build/comparisons.log).

## Genuinely fresh inputs and exact build recipe

The actual command `mktemp -d /tmp/c416-c417-final.XXXXXX` created
`/tmp/c416-c417-final.56a6rZ`. C416's two previously absent directories
were:

```text
/tmp/c416-c417-final.56a6rZ/C416_discrete_sine/a
/tmp/c416-c417-final.56a6rZ/C416_discrete_sine/b
```

Only the three named top-level source files and `sections/` were copied
into each directory with `cp` / `cp -R`. No prior PDF, `.aux`, `.bbl`,
author build directory, cache or generated bibliography was an input.
The temporary paths are execution provenance, not package dependencies;
a reproduction should create its own fresh directories.

In each directory the actual shell invocation was:

```bash
set -o pipefail
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex \
  2>&1 | tee full_console.log
```

Both invocations exited **0**, including their required LaTeX/BibTeX
reference-resolution passes. There was no third C416 invocation and
no typography repair. The recipe is the one actually documented in
the preceding C409–C413 final-build report. The `paper-compile` skill
was reread in full; its old-directory cleanup and automatic-source-fix
examples were not used because this delegation required fresh inputs
and no source edits. No venue or page cap has been selected.

Actually checked environment: pdfTeX 3.141592653-2.6-1.40.22, TeX Live
2022/dev/Debian; LaTeX2e 2021-11-15 patch level 1; Latexmk 4.76;
BibTeX 0.99d; Poppler `pdftoppm` 22.02.0. The command pins the epoch
to 2026-09-06 00:00:00 UTC, not the wall-clock build date. The local
`pdfinfo` display is 6 September 2026 08:00:00 CST for creation and
modification. No additional timezone override was used in these builds.

## Retained logs, PDF checks and provenance

The new `final_build/` retains:

- `pass_a.log` and `pass_b.log`: each build's actual final TeX log;
- `pass_a_console.log` and `pass_b_console.log`: both full, unfiltered
  console transcripts, including ordinary intermediate unresolved refs;
- `pass_a.blg` and `pass_b.blg`: both actual bibliography logs;
- `pdfinfo.txt`, `fonts.txt`, `main.txt`, `SOURCE_SHA256SUMS`,
  `comparisons.log` and `diagnostics.log`.

The final logs, not the intermediate console messages, determine the
clean result. Both final TeX logs and both bibliography logs have zero
matches for `Warning`, `Overfull`, `Underfull`, `undefined`,
`Missing character`, `multiply defined`, `LaTeX Error` and `Fatal error`.
The normal `rg` no-match exit is one. The extracted text has no `??`,
`[?]`, `[VERIFY]`, TODO, TBD or FIXME match.

Both final TeX logs have SHA256
`95c4841ca8ddf1385f621eebff91a59736b190fd2c999906d130e0b3cb30b72b`.
The retained `pdftotext -layout` extraction has SHA256
`6a74d14a9a78fd3f833a96b2803f8196aedc5fa7b1be0122b1163bd0a15e3ff3`.
A direct read-only layout-text extraction from the preserved author PDF
was compared with this final extraction and was byte-identical. The
historical author PDF hash is not rewritten as a final-build hash.

The final PDF is unencrypted, letter size, PDF 1.5, with a blank author
metadata field. All **20 font-object rows** are embedded subset Type 1
fonts with Unicode maps; no Type 3 or unembedded font is present.

## All fifteen final pages actually viewed

The exact pass-a PDF above was rendered in its temporary directory with

```bash
pdftoppm -r 100 -png main.pdf page
```

Rendering exited 0. The worker individually displayed `page-01.png`
through `page-15.png`, in groups 1–5, 6–10 and 11–15, and inspected
every page. No old author PNG was substituted for a final render.

| Page | Actual visual result |
|---:|---|
| 1 | Title, abstract, family definition, theorem and central Table 1 fit; no clipped glyph or equation. |
| 2 | Generic/boundary Tables 2–3, piecewise total and return product are complete and separated. |
| 3 | Source-version qualification and binomial/generating-function proof are legible; references resolve. |
| 4 | Escape induction and prime-adic inequalities fit without equation-number collision. |
| 5 | Core-cell verification steps and both explicit central cycle strings are readable. |
| 6 | Floor/ceiling formula, six-row clipping Table 4 and phase identities fit. |
| 7 | Negative-phase proof and signed-lift section are complete; no overlap or missing glyph. |
| 8 | All twelve generic-strip Table 5 rows and the exact endpoint-complement formula fit. |
| 9 | The full endpoint Table 6, including the paired start row and escape entries, is readable and unclipped. |
| 10 | Long endpoint itinerary, no-alias proof and first boundary circuit are properly spaced. |
| 11 | Growing-cycle proposition, its two-line string and sign/time formulas are legible. |
| 12 | Final routing case and exhaustion argument continue normally; no missing paragraph. |
| 13 | Least-radius Table 7, zeta derivation and explicit claim boundaries are complete. |
| 14 | Appendix A and all 36 rows of Table 8 fit on the page; no bottom-row clipping. |
| 15 | Both bibliography entries resolve and wrap within the margins; remaining whitespace is intentional. |

No wholly blank page, missing figure placeholder, overlapping text,
unreadable table, clipped equation or unresolved reference was found.
The main argument and limitations end on page 13, Appendix A is page
14, and references are page 15. These are descriptive page counts, not
a claim of compliance with an unspecified conference limit.

The final PNGs remain temporary inspection artifacts outside the package;
they are not new scientific figures and are not needed to reproduce the
document. All fifteen inspected pages come from the final delivered bytes.

## Scope of this completion

This receipt closes the delegated C416 final-build/visual execution only.
It does not turn typesetting or hashes into mathematical correctness,
human peer review, global priority or target arithmetic progress. No old
mathematical script, finite certificate, old batch build, formal evaluator
or release/sealing program was rerun here. Global reports, evaluation,
manifest/ledger and Git integration remain with the coordinator.
`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional.
