# C422 final release build report

2026-09-08 UTC. **PASS: two genuinely fresh final builds are byte-identical; all 14 final pages were actually inspected.**

The final entry is [main.pdf](main.pdf): **14 pages, 352289 bytes**, SHA-256:

```text
83691c4b0f36d28373642ed8a6a1c290db29333986de601aaf914b08120c3079
```

This is the authorized production gate after the coordinator read and accepted the complete [round-two review](../../manuscript_reviews/round2/C422_REVIEW.md). It is not a new mathematical experiment, external peer review, or batch-level release adjudication. No production source was changed.

## 1. Reviewed inputs and preservation

The 17 actual TeX/Bib inputs are exactly those in [the reviewed input manifest](build_round1/source_snapshot/source_inputs.sha256), SHA-256:

```text
19a5a9e3dca4adce3731c181d4429833f8cf3fbef549f1127ad32d2fc406dc7f
```

From the paper directory, `sha256sum -c build_round1/source_snapshot/source_inputs.sha256` passed **17/17** before creating the fresh build directories, after both builds, and after creating the final PDF alias. The manuscript has nine section inputs and five actual proof tables. The additional `figures/latex_includes.tex` remains an unchanged commented index, not an 18th production input.

The approved review PDF [build_round1/main.pdf](build_round1/main.pdf) remains **14 pages, 352364 bytes**, SHA-256:

```text
ecdb73cf225c34164a9f27d4ef2b56dc67485fb805307dfc56cd48e6420ffdae
```

The baseline [main_round0_original.pdf](main_round0_original.pdf) remains SHA-256:

```text
25f78d8224a3582200ceec838c6df6ed15da22fc79bb6917f49fcf05b51f0888
```

The failed original `build_round0/`, successful baseline `build_round0_attempt2/`, original source snapshot, revised source snapshot, and `build_round1/` were not cleaned, overwritten, or relabeled. Before release placement, the paper root had **no `main.pdf` alias**, so creating it did not overwrite any old alias. Existing baseline and reviewed PDFs were verified and preserved.

The accepted round-two raw report has 300 lines and SHA-256 `41b58e4a6587bfaf1da8490f7e62d7ffb03746a7190bf55c405edb0b9dcbd850`; its verdict is PASS, zero mandatory fixes, both approved optional edits closed. The author response remains [REVISION_ROUND1.md](REVISION_ROUND1.md), SHA-256 `747847112d2dcd509bfd7fadf42069e6d660b517497dfc0fd4c244a915b110b9`.

## 2. Actual environment

The installed environment was checked directly: Linux 5.15.0-78-generic, x86_64 GNU/Linux; latexmk 4.76; pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian), kpathsea 6.3.4/dev; LaTeX2e 2021-11-15 patch 1; BibTeX 0.99d; Poppler 22.02.0. No package installation or upgrade was performed.

Both commands set `SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C`. Both final PDFs store `/CreationDate (D:20260908000000Z)` and `/ModDate (D:20260908000000Z)`. The local `pdfinfo` output displays that same instant as 08:00 CST; the actual stored UTC dates were additionally inspected directly.

Tool/configuration SHA-256 values:

```text
/etc/LatexMk
  276b04cd6052a7574fecfc7acad3295d67c4bcf99b2f544b82a6157abe8340aa
/usr/bin/latexmk
  22e2164fea826ee19ff234503ef807d2728541e10eb3563912169977a650c951
/usr/bin/pdftex
  01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9
/usr/bin/bibtex
  c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f
/usr/share/texlive/texmf-dist/tex/latex/needspace/needspace.sty
  5ae673ce2a80fb868c954373252294d9e6469feeb78b445182772fd043eb0914
```

The existing anonymous 11-point letter-size article layout with one-inch margins is retained. The conclusion and references both reach page 14; there is no appendix and no imposed named-venue page quota. Compliance with a particular journal or conference template is not asserted.

## 3. Exact fresh-build commands and exits

Both `build_final1` and `build_final2` were checked absent, including absence of symlinks, then created with `mkdir build_final1 build_final2`. Neither contained inherited auxiliary files. The coordinator explicitly approved omission of the volatile automatic PDF trailer ID as a **build-only** setting from the start. The proven compiler-command override was used; `-usepretex` was permitted but not used. The production TeX was not edited.

From this paper directory, the actual Bash commands were:

```bash
set -o pipefail
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build_final1 \
  -pdflatex='pdflatex %O -jobname=main "\pdftrailerid{}\input{main.tex}"' \
  main.tex 2>&1 | tee build_final1/compile_console.log

set -o pipefail
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build_final2 \
  -pdflatex='pdflatex %O -jobname=main "\pdftrailerid{}\input{main.tex}"' \
  main.tex 2>&1 | tee build_final2/compile_console.log
```

Both commands exited **0**. Each fresh build performed three pdflatex passes and two BibTeX passes, as recorded by the complete console logs. These are convergence passes within two actual builds, not five independent builds. Intermediate undefined references/citations before convergence are retained in the console logs; none remain in either final engine log. No compilation failure, source correction, cleanup, or extra retry occurred in this final-build task.

## 4. Exact output comparisons

The following commands all exited **0**:

```bash
cmp build_final1/main.pdf build_final2/main.pdf
cmp build_final1/main.bbl build_final2/main.bbl
cmp build_final1/main.bbl build_round1/main.bbl
pdftotext -layout build_final1/main.pdf build_final1/main.txt
pdftotext -layout build_final2/main.pdf build_final2/main.txt
cmp build_final1/main.txt build_final2/main.txt
cmp build_final1/main.txt build_round1/main.txt
cmp build_final1/main.pdf \
  <(sed -E 's@^/ID \[<[^>]+> <[^>]+>\]$@@' build_round1/main.pdf)
```

Thus the two actual final PDFs are byte-identical, not merely visually similar. Their common hash is the release hash above. The final PDF is also byte-for-byte the approved reviewed PDF except for omission of the **75 characters** in its automatic `/ID` entry, with the line ending retained. This last command transforms only an in-memory comparison stream; no PDF post-processing or old-PDF modification occurred. Font objects, page content streams, visible content, links, layout and all other metadata are unchanged.

Both `.bbl` files have SHA-256 `f20079cee3ad53de57bf34d42b1cb4930c2a5bb0ffe74d7870a32db9dd0db818`. Both final 719-line extracted texts have SHA-256 `2f917993b2412c64c1c708f7bd4b9f9d8d3d0fac77365947831e95b30aac82f5`, identical to the complete text actually read during round two. No new mathematical text or bibliography change is concealed by the metadata adjustment.

## 5. Final logs, references, fonts and PDF checks

The final `main.log` and `main.blg` from **both** builds were scanned for `Warning`, `Overfull`, `Underfull`, `undefined`, `LaTeX Error`, and `Package Error`: **0 matches**. The final BibTeX log records all four bibliography entries and zero warnings. All labels and citations resolve. A final-text scan for `??`, `[?]`, `TODO`, `FIXME`, `XXX`, and `VERIFY` returned **0 matches**.

`pdfinfo build_final1/main.pdf` and `pdffonts build_final1/main.pdf` both exited 0, with outputs retained as `build_final1/pdfinfo.txt` and `build_final1/pdffonts.txt`. The PDF is unencrypted PDF 1.5, 14 letter pages (612 by 792 points), zero page rotation, no forms and no JavaScript. Visible authorship and metadata remain Anonymous Authors. The PDF is not tagged for accessibility; no tagged-PDF compliance claim is made.

All **19 font rows are embedded, subsetted Type 1 fonts with Unicode mappings**. There are no Type 3 fonts, missing-font placeholders, unresolved citation boxes, or missing images. The five figures are actual LaTeX proof tables; no external raster plot is a production input. The nine section files and five table inputs are all used, with the commented table index intentionally excluded.

## 6. Newly rendered final pages: actual inspection of every page

After exact comparisons, the first final PDF was newly rendered using:

```bash
mkdir build_final1/pages
pdftoppm -png -r 110 build_final1/main.pdf build_final1/pages/page
```

The command exited **0** and produced `page-01.png` through `page-14.png`. Every new image was actually opened and visually inspected in this final-build task, including the final reference page; the old review renders were not substituted for this check. Because the second PDF is byte-identical, these observations apply to both final builds and to the release alias.

| Page | Final-page material inspected | Result |
| --- | --- | --- |
| 1 | Visible title, anonymous authors, entire abstract, introduction and equation (1.1) | PASS; intended white space before theorem retained |
| 2 | Complete Theorem 1.1, full state domain and bound, Theorem 1.2, source mechanism | PASS; the approved keep-together fix survives |
| 3 | Ownership table, organization, all seven native branches and proposition start | PASS; all rows including zero line coordinates visible |
| 4 | Proposition continuation, inverse table, bijectivity proof and compactification opening | PASS; normal continuation without omission |
| 5 | All eight blowups, Picard basis, eight boundary classes, anticanonical sum | PASS; long table entries and equations fit |
| 6 | Four accessible charts and all five local extension formulas | PASS; denominators and small-characteristic statements legible |
| 7 | Full integer lattice computation, adjunction, uniform-pole lemma | PASS; algebraic-closure marks and indices visible |
| 8 | Uniform-pole proof, valuations, exponent polygon and nonzero vertex coefficient | PASS; no clipped formulas or lost proof text |
| 9 | Local multiplicities, complete four-face table, divisibility, invariant opening | PASS; all face expressions, roots and equations intact |
| 10 | Three matrices, trace order, specialization, invariant extension | PASS; matrix entries and denominators readable |
| 11 | Special-point extension, exact polar divisor, finite-fibre decomposition | PASS; all equations and proof continuation visible |
| 12 | Component sum, full scheme-reducedness argument, genus and point-count lemma | PASS; proof endings and normalization sequence intact |
| 13 | Correct Stacks item types, singular bound, exact least-period proof, conclusion | PASS; corrected locator remains complete and within margins |
| 14 | Remaining limitations, AI/internal-review disclosure, all four references | PASS; no missing text, cut-off URL or bibliography overflow |

No new production defect requiring a source edit was found. Theorem 1.1 remains wholly on page 2 and the corrected Stacks locator is visible on page 13. Natural continuations of other paragraphs, proofs and the conclusion remain readable.

## 7. Final entry placement and freeze handoff

Only after the comparisons, final checks and all-page inspection passed, a Bash `set -e` sequence repeated the PDF/BibTeX/text comparisons, checked that neither a file nor symlink named `main.pdf` existed, then executed:

```bash
cp build_final1/main.pdf main.pdf
cmp main.pdf build_final1/main.pdf
cmp main.pdf build_final2/main.pdf
sha256sum main.pdf build_round1/main.pdf main_round0_original.pdf
sha256sum -c build_round1/source_snapshot/source_inputs.sha256
```

The sequence exited **0**, the final alias has the release hash and byte size above, both preserved PDF hashes remain unchanged, and all 17 sources still match the reviewed manifest. [README.md](README.md) now identifies the current final entry and distinguishes historical baseline/revision records from current production status.

Additional final artifact SHA-256 values:

```text
build_final1/main.log
  cf4d71173dc1895de60584d610b304865249a6316a9b0fc4dc19f7be9d91f4fa
build_final2/main.log
  d4f3a20f8cea86beb0790f3f6810b21516def9b279bfb73d86385e5a02aebfab
build_final1/main.blg and build_final2/main.blg
  bc68c41f6bda757f797410fb2011520c63078f7485b5198f5a55eab3d6313153
build_final1/compile_console.log
  8f1ca102d049670eb7a1a5c1227b2bfc474fb4759a027ed5c4bbc3127cca962e
build_final2/compile_console.log
  d441cac0881cf2ae06db36900389a2dff3b3b13e4b47a4800529ca0840072462
build_final1/pdfinfo.txt
  c9290e7f5aadbee145f0699f6edaa13751bbfb3906da4cb1aeb463096402b800
build_final1/pdffonts.txt
  0b8b518aaac7b0e02e63d6180e9099ace23888e567365c020b9aaa2eb8c8eb0f
```

The differing engine/console log hashes reflect path/process bookkeeping; log byte identity is not asserted. The required PDF, bibliography and text identities all pass.

The `paper-compile` workflow supplied the convergence, log/citation/font checks and all-page verification. Its example cleanup, source-edit and venue-specific steps were not used. The only newly written objects are in this C422 paper directory: two fresh final build trees, final PDF alias, this report and the current README. No historical mathematical program, finite-field enumeration, old diagnostic, formal evaluator, shared registry or Git operation was run. Writing stops at this handoff pending coordinating release adjudication; no file permissions were changed to simulate an immutable archive.
