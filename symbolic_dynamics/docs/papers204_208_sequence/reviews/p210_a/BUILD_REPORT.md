# Review A build and actual page inspection

Selected build: `build02/`, parent actual launch/return in
`execution/build02/`. This is a fresh source-only Review A build of physical
Round0, not an author build and not either root terminal build. The earlier
actual `build01/` and all its child evidence remain; its outer-launch metadata
has the explicitly retained sanitization caveat in SANITIZATION.md.

Exactly10 frozen final TeX/bibliography inputs were copied: main.tex,
math_commands.tex, references.bib and7 sections/*.tex. `commands/pass_1/
SOURCE_BEFORE.json` records only these source inputs and no PDF/aux/bbl/log
products. No host library tree was copied. Manual commands, with full native
logs and per-pass overwritten products physically preserved, were:

1. `/usr/bin/pdflatex -recorder -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex`
2. `/usr/bin/bibtex main`
3. The same pdflatex invocation.
4. The same pdflatex invocation.

All four native exits are0. The explicit child environment in CONTEXT.json
sets SOURCE_DATE_EPOCH=1704067200, FORCE_SOURCE_DATE=1, LC_ALL=C, LANG=C,
TZ=UTC, clean task-owned HOME/TMPDIR, `shell_escape=f`, and openin/out limits.
No auxiliary, cached PDF or old build output was an initial input. All117808
pre/post dependency keys agree. The gzip inventories cover source copies,
TeX/styles/formats/configuration, fonts, renderer assets, executables and
shared libraries; ldd/kpsewhich commands and FLS_CLOSURE.json establish their
actual roles. Every consumed recorder input has a pinned external/prior-product
or same-pass-generated role; no unresolved FLS input remains. The four passes'
source-before/source-after ledgers, logs, recorder, aux/bbl/blg/out products
are retained, not overwritten as a single final log.

The final PDF has6 pages and20 embedded fonts. Final log has no undefined
references/citations, rerun/multiply-defined warnings or over/underfull boxes;
text has no unresolved markers. PDF metadata, font table and full extracted
text are in commands/pdfinfo, pdffonts and pdftotext. The complete PDF SHA256 is
`46afb4e470090087d3d57097849219f24d2e415495d4454e301a99c9847d9306`.
The selected fresh raw comparison in `execution/build_pdf_cmp02/` exits0
against the frozen main.pdf; this is actual byte equality, not just matching
digest labels.

`pdftoppm -png -r 110` rendered all6 pages. I then actually opened/viewed
each rendered page of BOTH builds,12 image views in total. The selected
`VIEW_build02.actual.json` pins images and records these observations:

| Page | Actual visual observation |
|---|---|
| 1 | Anonymous title/abstract, literal orbit and three-operation table legible; no clipping or overlap. |
| 2 | Two clock lemmas, birth inequalities and theorem/witness display fit; proof continuation to page3 is coherent. |
| 3 | N=1 ending, refinement theorem and complete three-branch test visible; order-sensitive example readable. |
| 4 | Forward/inverse coding and terminal-one convention complete; series and endpoint formula fit margins. |
| 5 | Fibre product/transfer readable; original box, Robbins discrepancy and external hold visible; references begin cleanly. |
| 6 | Six remaining references and wrapped URLs readable; no missing citation marker or hidden author identity. |

The helper's REPORT deliberately still says `visual_inspection=NOT_PERFORMED`:
it only rendered images. The separate actual manual-view receipts are the
visual evidence and do not rewrite that machine record. No PDF/source repair
was needed. The paper-compile skill supplied source-only compilation, log/font/
metadata checks and actual page inspection; generic venue/page/GPU/external
submission defaults were inapplicable under the project contract.
