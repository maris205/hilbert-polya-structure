# P207 B — actual source-only build and all-page inspection

2026-09-06 UTC. **BUILD_PASS / ALL_SEVEN_PAGES_ACTUALLY_VIEWED**.
This is the B-stage build/view evidence, not either terminal Round2
build and not a mathematical replay or novelty clearance.

## Physical source-only build

The reviewer read the complete existing source-only build helper and
ran this command from `/root/autodl-tmp/symbolic_dynamics`:

```text
bash docs/papers204_208_sequence/qa/cold_build.sh /root/autodl-tmp/symbolic_dynamics/papers/207-upper-neighbor-rank-dynamics/frozen_round1 /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p207_b/cold_build_01 /root/autodl-tmp/symbolic_dynamics/papers/207-upper-neighbor-rank-dynamics/frozen_round1/main.pdf
```

The actual exit code was zero. The helper starts a fresh destination
and copies only nine source inputs: `main.tex`, `math_commands.tex`,
`references.bib` and six section TeX files. No PDF, aux, bbl or previous
compile products are input. The source list and hashes are retained in
`cold_build_01/SOURCE_INPUTS.sha256`, and match the reviewed frozen
source bytes. The helper itself is included in `CONTEXT_PINS.sha256`.

`latexmk` was unavailable. The documented fallback was the actual
`pdflatex`, `bibtex`, `pdflatex`, `pdflatex` source-only sequence in
the inspected helper. Its `set -e` successful completion entails each
stage and the final frozen-PDF raw comparison succeeding; separate
stage exit-code receipts were not invented. Full stage stdout, TeX
log/fls, BibTeX log, engine versions and diagnostics remain in the
build directory. `BUILD_EXECUTION.json` records the actual command,
complete tool stdout and exit. Its historical pending-view field was
true at build completion and is superseded by the actual later page
inspection recorded here, not silently overwritten.

Reproducibility settings are recorded in `BUILD_ENVIRONMENT.txt`:
SOURCE_DATE_EPOCH=1704067200, FORCE_SOURCE_DATE=1, TZ=UTC, LC_ALL=C.
The build output is 407,557 bytes, A4, seven pages, PDF 1.5,
unencrypted, no forms or JavaScript. Its SHA-256 is

`5e74fa6a334f1cbc23837632b364729d97111b231e1ef8c3fd6a40a8dbc78759`.

The successful helper actually ran a raw `cmp` against the frozen
Round1 PDF; byte identity was not inferred merely from a hash. The
same PDF hash appears in the preserved author/A outputs, but those
earlier builds were not counted as this physical B build.

## Diagnostics and actual page views

`DIAGNOSTICS.txt` is empty after the final pass for the helper's exact
`undefined|Overfull|Warning` scan. That scan does not include `Underfull`.
The actual final `main.log`, line 638, contains one
`Underfull \vbox (badness 1038) has occurred while \output is active []`,
immediately before the page-4 marker; `pass3.stdout`, line 88, records
the same diagnostic. A direct final-log search finds no `Overfull`,
`undefined` or `Warning` matches. The seven actual page views below
found no clipping or missing content, including on page 4; those views
do not erase the recorded underfull spacing warning.

This corrects the later-discovered Minor artifact finding P207-B-ART1.
The exact initial overstatement is preserved in
[BUILD_REPORT.initial.md](BUILD_REPORT.initial.md), along with all
unchanged original logs, PDF and page images. Root's actual
[response supplement](../../P207_B_RESPONSE_SUPPLEMENT.md) authorizes
this evidence-only correction, not a manuscript or PDF change.
No new build or new page viewing is claimed by this correction.

All 31 listed font objects are embedded
Type 1; no Type 3 or unembedded font appears. The extracted PDF text,
all four bibliography items and their manuscript use were inspected.
These technical checks accompany, and do not replace, viewing pages.

The actual render command, after creating only the owned destination,
was:

```text
pdftoppm -r 105 -png docs/papers204_208_sequence/reviews/p207_b/cold_build_01/main.pdf docs/papers204_208_sequence/reviews/p207_b/page_views/page
```

It exited zero. All seven resulting PNGs were then opened through the
image viewer and actually inspected by this reviewer during B.
Their byte pins are in `PAGE_VIEW_PINS.sha256` and the final manifest.

| Actual page | Content inspected | Visual result |
|---:|---|---|
| 1 | Title/abstract, literal map, complement/source limits, start of permanent-extrema lemma | Readable; no clipping or missing symbols |
| 2 | Extrema proof, finite certificate, repeated-cycle/global-bound proof and core statement | Equations and quantified witness bounds visible; margins intact |
| 3 | Core proof continuation, role table, determinant and seed statement | Table aligned; determinant/recurrence/seed display readable |
| 4 | Seed proof, sharp fibre theorem, full local source table | Odd/even targets and table boundary conditions legible |
| 5 | Eight kernels, inverse trace, Schatten setup and k=0/1 cases | Matrix entries and equation numbers intact; no overlap |
| 6 | k>=2 comparison, length budget/equality analysis, limits | All inequalities and scope text readable; no overflow |
| 7 | Four references and source URL | Bibliography visible and complete; remaining white space is benign |

There is no visual defect requiring a manuscript change. This means
these seven exact B-build pages were viewed; it does not claim a
fresh view of other historical PDFs, specialist typographic review,
or final submission/public-release readiness. `OWNER_AMBER /
HOLD_EXTERNAL` remains.
