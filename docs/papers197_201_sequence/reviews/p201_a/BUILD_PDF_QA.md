# P201 Review A — source-only build and all-page QA

One genuinely source-only build was performed in the previously empty
`qa/cold_build/` directory, copying only frozen `main.tex` and
`references.bib`. Commands were pdflatex, bibtex, pdflatex, pdflatex, with
each stdout retained. No author aux, bbl, log or PDF was used as build input.
This build had already run when the historical collision was reported;
closing its record does not rehabilitate paper admission.

The resulting PDF is exactly byte-identical to both
`round0_frozen/main.pdf` and `main_round0_original.pdf`:

`7711af8b9cf8b31f0c8a0514ad4b31d7709626a9faf77c1e2c633064c77d15a4`.

PDF facts: 5 A4 pages, 364,568 bytes, PDF 1.5, unencrypted. Title, subject,
keywords, author, creator and producer metadata are blank. All 27 font
entries report embedded, subsetted fonts. The final log has no Warning,
Overfull, Underfull, undefined or Error match. The earlier shell check
returned status 1 solely because rg had zero matches, not because a build
failed. The PDF metadata/fonts and command receipts are retained in QA.

Each rendered page was opened with the image viewer, not just extracted as
text. The actual inspected raster files are `qa/visual/page-1.png` through
`page-5.png`.

| Page | Actual visual inspection |
|---|---|
| 1 | Anonymous title, abstract and labelled definition legible; ownership paragraph and rank-packing display fit; no clipped glyph or margin overflow |
| 2 | Core-extension positive-time boundary and threshold hierarchy legible; the critical theorem continues normally onto page 3 |
| 3 | Factorial-count continuation, forest code, static sum and fibre statement fit; no equation collision or missing symbol |
| 4 | Image and unique-maximum proofs legible; numerical table aligned and all seven rows present |
| 5 | Claim ceilings and disclosure continue normally; all three bibliography entries and long URLs readable; remainder is ordinary end-of-paper whitespace |

This is visual/build acceptance of the preserved mathematical record only.
It is not scientific admission acceptance: C1 remains validated and open
for that purpose. No author source or frozen artifact was modified.
