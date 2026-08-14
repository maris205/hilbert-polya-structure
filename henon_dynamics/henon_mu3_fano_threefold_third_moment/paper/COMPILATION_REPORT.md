# HCS-C49 compilation report

**Build date:** 2026-08-14 UTC

**Engine:** pdfLaTeX through `latexmk`

**Command:** `latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`

## Frozen output

| property | value |
|---|---|
| PDF | `paper/main.pdf` |
| SHA-256 | `3968a846b236b3395dac2cb855b48a568793c16b8cc5c3c73011b6136196818a` |
| Pages | 6 |
| Page size | A4, 595.276 by 841.89 pt |
| File size | 198833 bytes |

## Verification

- The final `main.log` contains no LaTeX or package error, warning,
  undefined citation/reference, overfull box, or underfull box.
- `pdftotext` contains no verification marker, unresolved reference marker,
  placeholder, or release-commit sentinel.
- Every reported font is embedded, subsetted, and Unicode-mapped.
- No TeX or BibTeX input is newer than the PDF.
- The source bibliography has six entries; all six are cited and the build
  has no dangling or orphan citation.

The report describes the clean rebuild after the final bibliography metadata
and source-audit corrections.
