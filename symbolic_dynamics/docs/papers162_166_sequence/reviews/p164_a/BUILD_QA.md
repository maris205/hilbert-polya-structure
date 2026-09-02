# P164 source-only build and PDF QA

## Inputs

Each cold build received only the pinned `main.tex` and `references.bib`.
No paper-local auxiliary file, generated bibliography, or PDF was copied into
the build directory.

The build sequence in each fresh temporary directory was:

```bash
SOURCE_DATE_EPOCH=0 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
SOURCE_DATE_EPOCH=0 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=0 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Reproducibility receipts

| item | cold build 1 | cold build 2 |
|---|---|---|
| source-only pipeline | PASS | PASS |
| final PDF bytes | 300,597 | 300,597 |
| final PDF SHA-256 | `db26e57e610577cdff03c348fa3ce794165e3268393350d7d2f55b14e98070ae` | `db26e57e610577cdff03c348fa3ce794165e3268393350d7d2f55b14e98070ae` |
| final `main.log` SHA-256 | `b5e664a2f5bd40e3fa4ec81f02d73acbd95813c9a795cfcb6eeb0c894ad4e59c` | `b5e664a2f5bd40e3fa4ec81f02d73acbd95813c9a795cfcb6eeb0c894ad4e59c` |
| final-pass warnings/errors | 0 | 0 |
| BibTeX warnings | 0 | 0 |

Both cold PDFs are byte-identical to the pinned paper PDF.

## Structural PDF QA

- 4 pages, A4, PDF 1.5.
- 23 font rows; all 23 fonts are embedded, subsetted, and Unicode mapped.
- No raster images, forms, JavaScript, encryption, suspect objects, or page
  rotation.
- Title, Author, Subject, and Keywords metadata fields are empty.  The visible
  byline is `Anonymous`; no affiliation, email, ORCID, acknowledgement, or
  identifying institution appears in the extracted text or source.
- Text extraction covers all displayed equations and all four references.
- The final log has no undefined citation/reference, multiply-defined label,
  overfull/underfull box, or package error warning.

## Full-page visual inspection

All four pages were rendered at 150 dpi and inspected individually.

| page | result |
|---:|---|
| 1 | Title, abstract, theorem opening, equations (1)--(8), margins and footer are clean. |
| 2 | Theorem continuation, equations (9)--(13), proof blocks and page break are clean. |
| 3 | Equations (14), evaluated spectra, limitations, and references (1)--(3) are clean; URLs remain inside the text block. |
| 4 | Reference (4) renders cleanly.  The large remaining white area is the natural end of a four-page manuscript, not lost content. |

No clipping, overlap, missing glyph, orphaned heading, broken link text, or
illegible formula was observed.

## QA verdict

**PASS.**  The two proof-level minor findings in Hostile Review A do not arise
from compilation or PDF production.  The frozen artifact remains
`HOLD_EXTERNAL` pending review closure.
