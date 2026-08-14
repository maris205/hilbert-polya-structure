# COMPILATION REPORT — SD-C24

## Deliverable

- Title: *Cofactor Holonomy on the Successor–Divisor Shift: Exact Class
  Resolution and a Fredholm Trilemma*
- Candidate: **SD-C24**
- Primary system family: **Symbolic Dynamics**
- Canonical artifact: `main.pdf`
- Page count: **23**
- Page geometry: **A4**, 595.276 × 841.89 pt
- PDF version: **1.5**
- File size: **531747 bytes**
- PDF SHA-256:
  **a923c06108d86a3e0ccd7e63415e7c86db9d25b03ec53511bd2e2ad32fb322ba**
- Encryption: **none**

## Toolchain and clean build

- pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
- BibTeX 0.99d
- Bibliography style: `plainnat`

The project was rebuilt from a source-only state with
`-interaction=nonstopmode -halt-on-error`: one initial `pdflatex` pass,
`bibtex main`, and three further `pdflatex` passes.  Thus the clean protocol
used BibTeX and four complete LaTeX passes.  Every command exited
successfully, and the final pass produced the stabilized 23-page artifact.

## Mechanical audit

| Check | Result |
|---|---:|
| LaTeX/package warnings | 0 |
| Fatal or nonfatal LaTeX errors | 0 |
| Undefined references | 0 |
| Undefined citations | 0 |
| Overfull boxes | 0 |
| Underfull boxes | 0 |
| Distinct cited keys | 10 |
| Bibliography entries | 10 |
| Cited-but-missing keys | 0 |
| Uncited bibliography entries | 0 |
| PDF draft markers (`TODO`, `FIXME`, `??`, `[?]`) | 0 |
| Font objects | 31 |
| Unembedded font objects | 0 |
| Unsubset font objects | 0 |
| Pure TikZ figure sources | 2 |

The full LaTeX source was additionally checked for control characters,
unbalanced inline/display math delimiters, missing `\input` targets, and the
previously reported naked-math and lost-backslash patterns.  No unresolved
instance remains.  `pdftotext` contains no placeholder or unresolved-reference
marker.  `pdfinfo` confirms anonymous-author metadata and an unencrypted A4
artifact.

## Visual and scope audit

Pages 1, 8, 10, 18, 19, and 23 were rasterized and inspected.  This covers
the title and research-status box, both TikZ figures, the exact holonomy
coefficient formulas, the strict Route-A table and tuple, the bibliography,
and the final scope ledger.  No clipping, collision, overflow, or illegible
label was observed.

The artifact consistently records the sharp trace-class domain
`Re(s) > 1/2` and `Re(s+u) > 1/2`, distinguishes the ordinary regular lift
from its semifinite group-trace formulation, and separates the formal pure-
cofactor series from honest endpoint-regularized Fredholm determinants.  Its
frozen Route-A tuple is

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`,

with overall verdict `ROUTE_A_REJECTED`; Route B remains locked.  No review
loop, target-zero data, RH claim, Hilbert–Pólya carrier, or cross-family
construction was introduced.

## Source hashes

- `main.tex`:
  `b9a40af45cb5151e3d60d5b54f4ee6c345d9096e752e82c669371d06ce8cb502`
- `math_commands.tex`:
  `5b8559cccfb3d77e78274ecf1825ae6317f2994b672cec2475b38d60367fd674`
- `references.bib`:
  `3d1db6d7d7fe51b9e7691984543bdccc51066d0562dda33af140bd569f72b079`

## Cleanup

LaTeX and BibTeX intermediates are excluded from the final shareable paper
artifact.  The modular manuscript sources, bibliography, TikZ sources,
authority Markdown packages, and `main.pdf` are sufficient for a clean
rebuild.
