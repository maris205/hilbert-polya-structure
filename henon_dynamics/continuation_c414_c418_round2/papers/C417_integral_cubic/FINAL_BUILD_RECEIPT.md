# C417 final build and every-page visual receipt

Status: **PASS — two fresh final builds are byte-identical; all 17 final
pages actually viewed.** One explicitly recorded pass-a stabilization
invocation was needed to close a retained label-rerun warning; it changed
no source or PDF byte. Execution date: 2026-09-07 UTC.

The root coordinator explicitly delegated these builds and page checks
to the nonlinear-geometry worker, who had completed the separate C417
[nonauthor manuscript review](REVIEW_MANUSCRIPT.md). The execution and
visual inspection below are that worker's work, not a claim that root
personally viewed the pages. The closed review's mathematical contract
is unchanged. The entire original `build_author/` directory and historical
author/review receipts are preserved.

## Final artifact and input identities

The delivered [main.pdf](main.pdf), stabilized pass-a PDF and untouched
pass-b PDF are all **17 pages, 392,206 bytes**, with SHA256:

```text
b0f62d97bea170e9b03cc42a7da1c7f5503ba09cadef906a5201993bafa39e5b
```

The initial pass-a PDF already had exactly this hash. The
[source identity list](final_build/SOURCE_SHA256SUMS) records all thirteen
inputs: `main.tex`, `math_commands.tex`, `references.bib` and the ten
section files. Its SHA256 is:

```text
58ba8cd4ab192a2793795527149d154f28c9d07dabd117943ce3f23e2f63d34c
```

After compilation, `sha256sum -c final_build/SOURCE_SHA256SUMS` passed
all thirteen inputs. All **26 source-copy `cmp` operations** between
current inputs and their two clean copies exited 0. The two final PDFs
passed `cmp`; after copying pass a to the delivered `main.pdf`, a
separate delivered/pass-a `cmp` also exited 0. Complete returned results
are retained in [comparisons.log](final_build/comparisons.log).

## Two genuinely fresh builds and one recorded stabilization

The actual `mktemp -d /tmp/c416-c417-final.XXXXXX` command created
`/tmp/c416-c417-final.56a6rZ`. C417's two previously absent directories
were:

```text
/tmp/c416-c417-final.56a6rZ/C417_integral_cubic/a
/tmp/c416-c417-final.56a6rZ/C417_integral_cubic/b
```

Only the three named top-level source files and `sections/` were copied
with `cp` / `cp -R`. No author PDF, auxiliary, generated bibliography,
cache or author build directory was copied in. The temporary paths
record this execution; reproduction should create new fresh paths.

In each directory the actual initial invocation was:

```bash
set -o pipefail
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex \
  2>&1 | tee full_console.log
```

Both invocations exited **0**. Their PDFs were already byte-identical,
and their resulting `.aux` files also matched. Nevertheless, pass a's
last TeX log still contained exactly one diagnostic:
`Label(s) may have changed. Rerun to get cross-references right.`
Latexmk had ended with all targets up-to-date. Pass b's last TeX log
was clean. The cause of Latexmk's different stopping behavior is not
claimed to have been established merely from those observations.

The worker notified root before changing any build output. Root then
explicitly authorized exactly one affected pass-a stabilization, with
the initial log and console preserved. In that same pass-a directory,
the actual additional invocation was:

```bash
set -o pipefail
env SOURCE_DATE_EPOCH=1788652800 FORCE_SOURCE_DATE=1 \
  pdflatex -interaction=nonstopmode -halt-on-error main.tex \
  2>&1 | tee stabilization_console.log
```

It exited **0**. The final TeX log is warning-free and the PDF retained
the exact pre-stabilization SHA256 shown above. `cmp` with the unchanged
pass-b PDF exited 0. This was an additional reference-stabilization
invocation on pass a, **not** a source repair, a third fresh build, or
a replacement of either original fresh-build history.

The initial recipe matches the preceding C409–C413 final-build report.
The `paper-compile` skill was reread in full. Its old-directory cleanup
and automatic-source-fix examples were not used because the delegation
required new directories and unchanged sources. No venue page cap was
introduced.

Actually checked environment: pdfTeX 3.141592653-2.6-1.40.22, TeX Live
2022/dev/Debian; LaTeX2e 2021-11-15 patch level 1; Latexmk 4.76;
BibTeX 0.99d; Poppler `pdftoppm` 22.02.0. The epoch is 2026-09-06
00:00:00 UTC, independent of the 7 September wall-clock execution.
`pdfinfo` locally displays creation and modification as 6 September
2026 08:00:00 CST. No timezone override was added to these invocations.

## Retained diagnostics and final checks

The new `final_build/` retains both full initial console transcripts,
both bibliography logs, both final TeX logs, and specifically:

- `pass_a_initial.log`: the actual initial last TeX log with its warning;
- `pass_a_console.log`: the full original fresh-build console;
- `pass_a_stabilization_console.log`: the complete additional invocation;
- `pass_a.log`: the final clean post-stabilization TeX log;
- `pass_b_console.log` and `pass_b.log`: untouched pass-b evidence.

Also retained are `pass_a.blg`, `pass_b.blg`, `pdfinfo.txt`, `fonts.txt`,
`main.txt`, `SOURCE_SHA256SUMS`, `comparisons.log` and `diagnostics.log`.
The initial pass-a log has SHA256
`402d585c7ef9513afc1573bd1d0c3db7478c1a26e0a949b47849051b93fad1a1`.
Both final TeX logs have SHA256
`f89555b48ec3438a18f9c73d03425c843cc70503073307b1d35affc713324c61`.

Both final TeX logs and bibliography logs have zero matches for
`Warning`, `Overfull`, `Underfull`, `undefined`, `Missing character`,
`multiply defined`, `LaTeX Error` and `Fatal error`. The normal `rg`
no-match exit is one. Historical intermediate warnings remain visible
in the unfiltered console and initial log; they are not misreported as
having never occurred.

The final text has no `??`, `[?]`, `[VERIFY]`, TODO, TBD or FIXME match.
Its layout extraction has SHA256
`291983798334a7dc6a6073ad585235f6af3e0b214fea33aaf73c04dc4a776890`.
A direct layout-text extraction from the preserved author PDF was
byte-identical to the final extraction. The author/review PDF hash
remains an honest historical identity, not this final-output identity.

The final PDF is unencrypted, letter size, PDF 1.5, with blank author
metadata and a visible anonymous author block. All **20 font-object
rows** are embedded subset Type 1 fonts with Unicode maps; there is
no Type 3 or unembedded font.

## Every one of the seventeen final pages actually viewed

The pass-a PDF was rendered in its temporary directory with:

```bash
pdftoppm -r 100 -png main.pdf page
```

Rendering exited 0. The render was made from the same exact PDF bytes
as the final stabilized/delivered file; the unchanged SHA256 and final
pass-a/pass-b `cmp` were checked before these pages were displayed.
No claim depends on reusing a different author's PNG. The worker
individually displayed `page-01.png` through `page-17.png`, in complete
groups 1–5, 6–10, 11–15 and 16–17.

| Page | Actual visual result |
|---:|---|
| 1 | Anonymous title, abstract, family recurrence and first theorem items fit; theorem continuation is normal. |
| 2 | Equality item and all seven template rows are complete, including the wrapped six-cycle parameter range. |
| 3 | Source distinctions and the four-row comparison Table 2 are legible with resolved citations. |
| 4 | Global-extrema normalization, prime-adic proof and endpoint/secant equations fit without clipping. |
| 5 | Affine/parabolic cases, endpoint alphabet argument and reflection formulas are readable. |
| 6 | No-cancellation formulas and symbolic enumeration proposition are complete and properly spaced. |
| 7 | All five rows of Table 3 and all endpoint patterns in Table 4 fit; large float spacing is not missing text. |
| 8 | Four-global-symbol warning, finite input ranges and unique maximizing tuple are legible. |
| 9 | All fourteen finite-complement rows, full caption and certificate argument fit; no table clipping. |
| 10 | Two-symbol derivations, reciprocal lemma and interpolation fractions are readable. |
| 11 | Complete six-cycle exhaustion and all converse ordered pairs fit, including long displayed formulas. |
| 12 | Equality coefficients, all five disjoint cycles and ordinary zeta product are complete. |
| 13 | Return proof and explicit source/target limitations are present; appendix page-break whitespace is intentional. |
| 14 | Complete cycle-extractor listing, extraction lemma and start of its proof are readable and unclipped. |
| 15 | Extraction proof continues normally; the entire small-diameter enumeration listing fits. |
| 16 | The full symbolic enumeration listing and its closing bounds/table references fit without overflow. |
| 17 | All five bibliography entries, DOIs and wrapped URLs are readable within the margins. |

No wholly blank page, overlapping text, missing glyph, unreadable table,
clipped equation/listing or unresolved reference was found. The main
argument/limitations end on page 13; Appendix A occupies pages 14–16;
references are page 17. Temporary PNGs remain outside the package and
are not a new scientific figure collection or reproduction dependency.

## Scope of this completion

This closes the specifically delegated C417 final-build and all-page
visual execution. Root still integrates and independently checks this
receipt and the final delivered bytes. Formal evaluation, global release
reports, ledger/manifest and Git actions were not performed here.
No frozen mathematical code, finite certificate or old batch build was
rerun. Clean typography and byte identity do not certify mathematics,
human peer review, global priority, target Euler factors, root numbers
or Hilbert–Pólya progress. `NO_BAD_EULER_OR_ROOT_NUMBER` remains in force.
