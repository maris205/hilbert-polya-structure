# Compilation Report — SD-C23

**Artifact:** main.pdf
**Build date:** 2026-08-14
**Format:** anonymous 11pt A4 article
**Status:** PASS

## Clean build

The final build began with no retained LaTeX auxiliary state and used:

1. pdflatex with nonstop interaction and halt-on-error
2. BibTeX
3. pdflatex with nonstop interaction and halt-on-error
4. pdflatex with nonstop interaction and halt-on-error
5. pdflatex with nonstop interaction and halt-on-error

This is four successful PDFLaTeX passes with BibTeX inserted after pass one.
The fourth pass is stable.

## Final PDF

- Pages: **22**
- Page size: **595.276 × 841.89 pt (A4)**
- File size: **457,150 bytes**
- PDF version: **1.5**
- SHA-256:

      6ff4bd948b55a9e3cbdf590646e5dbf029b9d163d20f761664c3a746762ab5d0

## Audit

- LaTeX errors: **0**
- LaTeX/package warnings: **0**
- Overfull boxes: **0**
- Underfull boxes: **0**
- Undefined references: **0**
- Undefined citations: **0**
- Multiply defined labels: **0**
- Unresolved placeholder text: **0**
- Bibliography entries cited and resolved: **9**
- PDF fonts: **25/25 embedded**, all subsetted
- PDF encryption: **none**
- Text extraction: **PASS**
- Visual inspection: title/status box, both TikZ figures, theorem displays,
  count/control tables, route ledger, references, and final scope page
  inspected without clipping or overlap
- Target-zero data: **absent**

## Exact-suite linkage

The manuscript snapshot is synchronized to the final exact suite:

- 19/19 tests pass;
- \(T_{32}=14{,}532{,}674\), \(P_{32}=454{,}021\);
- 667 explicit primitive classes through length 16;
- 48 weighted traces and 51 determinant coefficients with zero mismatch;
- 30,626 audited source edges;
- byte-identical double-run results ledger SHA-256:

      9467c520837374b34d4fd019a7f11b944808cf038e202cbaba07db76b5f61e8f

## Cleanup

The authority directory retains the manuscript sources, figures,
references.bib, main.tex, main.pdf, and this report.  LaTeX auxiliary files
are removed after the final audit.
