# COMPILATION REPORT — SD-C22

## Release artifact

| Field | Value |
|---|---|
| PDF | main.pdf |
| Pages | 18 |
| Paper size | A4, 595.276 × 841.890 pt |
| PDF version | 1.5 |
| File size | 515,522 bytes |
| SHA-256 | 60be9e7c60adfd1407746fde66d32b3d6a5898aea5ab670b165f3b648e7bbeb9 |
| Compiler | pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/Debian) |
| Bibliography | BibTeX 0.99d, plainnat |

## Clean release build

A fresh middleware directory was used and all previous auxiliary,
bibliography-output, log, and outline files were moved out before the release
sequence:

    pdflatex main.tex        # pass 1
    bibtex main
    pdflatex main.tex        # pass 2
    pdflatex main.tex        # pass 3
    pdflatex main.tex        # pass 4

Final pass status:

- LaTeX errors: 0
- BibTeX errors: 0
- LaTeX warnings: 0
- BibTeX warnings: 0
- undefined citations: 0
- undefined references: 0
- overfull boxes: 0
- underfull boxes: 0
- rerun/label warnings: 0

## Content and source audit

- Contracted convention is used throughout:
  \[
  \ell(p)=2+\sum_{d=2}^{\lfloor\sqrt p\rfloor}\lceil p/d\rceil.
  \]
- Sanity endpoints are consistent: \(\ell(5)=5\) and
  \(\ell(4093)=15293\).
- Test count is consistently reported as 12/12.
- Route tuple is consistently
  (A0_STRUCTURAL_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL,
  A4_FAIL).
- \(L_s\) is consistently called a source-weighted vertex adjacency, not a
  Ruelle transfer operator.
- The raw graph-step product and induced return determinant are kept distinct.
- All cited bibliography keys resolve; the final bibliography contains 13
  cited primary sources.
- No control characters, unresolved question marks, stale 15294 endpoint,
  stale 10/10 count, or unexpanded citation/reference command appears in the
  release.
- All modular section and figure inputs referenced by main.tex exist.
- All local links in README.md exist after this report was created.

## PDF audit

- pdfinfo confirms 18 A4 pages and the expected title, author, subject, and
  keywords.
- pdftotext succeeds and the extracted text has no unresolved citations,
  references, or stale endpoint conventions.
- pdffonts reports 31 font resources; every font is embedded, subset, and
  Unicode-mapped.
- Visual inspection covered the title/abstract, overview figure and
  bibliography citations, clock-dilution theorems, route tuple, and final
  theorem/evidence ledger.
- The overview figure is pure TikZ vector artwork; no raster manuscript asset
  is required.

## Release cleanup

Compilation middleware (main.aux, main.bbl, main.blg, main.log, and main.out)
is removed from the authority directory after this audit. The source,
bibliography, modular sections, TikZ figure, and final PDF remain.
