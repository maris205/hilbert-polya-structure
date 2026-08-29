# Build Record — P115

Status: anonymous compact author draft; external release/novelty/priority
**HOLD**.

Run from this directory:

~~~text
python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

## Toolchain

~~~text
Python 3.12.3
pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
BibTeX 0.99d (TeX Live 2022/dev/Debian)
~~~

## Revised author build result

- Verifier: **PASS — 2,259,162 exact assertion executions**
- Fresh verifier stdout: **14 lines, 1,449 bytes**, byte-for-byte identical to
  `code/verification_output.txt`
- New structural lanes: forward/inverse index-chain coordinates, statewise
  product conjugacy, weak-component sizes, and per-root attached-tree layers
- LaTeX/BibTeX stages: all exited zero
- PDF: **7 A4 pages**, PDF 1.5, 397,625 bytes
- Bibliography: 9 cited entries, all resolved
- Log diagnostics: **0 warnings**, **0 overfull boxes**, **0 underfull
  boxes**, **0 undefined citations/references**, **0 errors**
- Settled rerun scan: **0 rerun requests**
- Text extraction: 22,920 bytes, 662 lines
- Fonts: **27/27 embedded, 27/27 subsetted, 27/27 Unicode-mapped**
- Visual audit: all 7 pages rendered at 150 dpi and individually inspected;
  no clipping, collision, blank page, missing glyph, broken display, or
  unreadable reference was found

The document is anonymous (Anonymous) and contains no affiliation or
acknowledgment. Deterministic PDF metadata settings suppress creation dates
and trailer identifiers. The assertion total is a raw count of executed
checks, not a count of independent theorems. This record documents only the
author-stage build; it does not certify owner completeness or authorize
external circulation.
