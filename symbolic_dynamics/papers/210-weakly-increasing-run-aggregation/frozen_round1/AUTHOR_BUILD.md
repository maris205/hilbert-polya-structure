# Actual P210 author source-only build and view

2026-09-07 UTC. Two source-only author draft builds of successive expositions; neither is a terminal root build. No latexmk binary was available. Root authorized the explicit existing pdflatex→bibtex→pdflatex×2 fallback. No installation or external upload occurred.

## Build execution

[execution/build01](execution/build01/RESULT.json) captures the real parent command and exit0. [draft_build_01](draft_build_01/REPORT.json) starts from ten TeX/bibliography source files only: main.tex, math_commands.tex, references.bib and seven sections. It contains no copied auxiliary/PDF from another build. The actual commands are:

1. `/usr/bin/pdflatex -recorder -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex`
2. `/usr/bin/bibtex main`
3. The same pdflatex command.
4. The same pdflatex command.

All four native exits are0. Every pass retains full raw stdout/stderr, its log and recorder/auxiliary/bibliography products, and before/after source-product pins. Initial unresolved references/citations during multipass construction remain in their original logs; the final log has **zero undefined references/citations, no rerun/multiply-defined warnings, and zero overfull/underfull warnings**. No source revision or failed TeX run was needed.

Engine: pdfTeX1.40.22 (TeX Live2021/Debian), as recorded by the full initial output. Child settings include `LANG=C`, `LC_ALL=C`, `TZ=UTC`, `SOURCE_DATE_EPOCH=1704067200`, `FORCE_SOURCE_DATE=1`, no shell escape, private empty HOME and TMPDIR. Exact environment and engine/config lookup commands appear in CONTEXT.json and commands/*/ATTEMPT.json. The parent interpreter is isolated/no-site Python3.10 with an absent cache prefix.

Complete conservative external/source input inventories have **117,808 paths**, before and after identical, stored losslessly as INPUTS_BEFORE.json.gz and INPUTS_AFTER.json.gz. Installed TeX/font/configuration trees are hash inventories, not wholesale copies. FLS_CLOSURE.json records every actual .fls INPUT, classified against pre-pinned external/source files, prior-pass products or prior recorder OUTPUT events in the same pass; there are **zero unresolved input roles**. Native dependency/configuration returns and full raw streams remain covered. This is an explicit bounded dependency inventory, not an OS/startup trace; not all conservative pinned paths were consumed.

The PDF is **301,075 bytes**, **6 pages** (main text ends on page5; references span pages5–6), A4, blank author metadata. All17 listed fonts are embedded. PDF SHA-256:
`e08c44ad4caa897bf4e1656d2ca9e119f1b4cf463a87b9ffff4663ac7bee0155`.
This initial PDF remains immutable in draft_build_01. The selected live PDF is the revised draft02 below.

## Actual six-page visual inspection

`pdftoppm -png -r 110` rendered all six pages, native exit0. I, /root/p210_author, then actually opened and viewed each page image with the image-view tool, in three two-page calls. File existence/hash checks did not substitute for visual inspection. [AUTHOR_VIEW.actual.json](AUTHOR_VIEW.actual.json) binds the exact PDF and all six image hashes.

| Page | Actual visual observations |
|---|---|
| 1 | Anonymous title/abstract and literal rule readable; exact orbit and three-rule table fit within margins; no clipping or missing symbols. |
| 2 | Background paragraph, two mass lemmas and sharp-clock statement/proof readable; witness equation fits; continuing proof at page break is legible. |
| 3 | Witness closes; unique refinement and attained-minimum image proof are complete and readable; three-branch display fits; coding section begins normally. |
| 4 | Both coding directions, terminal-one boundary and mass identity readable; formal series corollary and partition endpoint formula fit with no overlap. |
| 5 | Fibre proposition/suffix DP and limitations readable; source caveat and external hold visible; references begin with one intact entry. |
| 6 | Remaining six bibliography entries readable; URLs wrap within margins; no cut-off content; unused lower space is natural bibliography ending, not venue padding. |

Outcome: author visual PASS for this exact six-page draft. No decorative figures, illegible tables or visible formula/reference errors were found. This is not independent review and does not confer physical Round0, manuscript acceptance or terminal page-view credit. Root's own actual all-page viewing and later terminal source-only builds/views remain required.

## Selected revised author draft02

The integer-domain wording clarification in AUTHOR_REVISION_LOG.md changed three section sources, not the theorem/verifier/canonical. A wholly fresh `execution/build02/` → `draft_build_02/` repeated the source-only four-pass process with all native exits 0, the same 117,808 unchanged broad input pins, complete .fls closure, zero final warnings/unresolved markers, six rendered pages and all 20 fonts embedded. The selected live main.pdf is its exact 323,806-byte output, SHA-256 `46afb4e470090087d3d57097849219f24d2e415495d4454e301a99c9847d9306`. Its blackboard-bold integer-domain font accounts for the font change.

I actually viewed all six draft02 page images in three new two-page tool calls, including fresh views of pages 5–6 whose raster bytes happen to equal draft01. The new receipt AUTHOR_VIEW_DRAFT02.actual.json binds all page hashes. The integer-domain abstract/clock are legible; the coding section begins cleanly on page 4; no clipping or layout defect was seen. Main text still ends page 5, references pages 5–6. Initial build/view originals remain; the three old live-source pins resolve through exact draft01 source-copy roles. This is author visual PASS for the selected revised draft, not root viewing or terminal acceptance.
