# COMPILATION REPORT

**Paper:** Character-Resolved Cycle-Index Determinants of the Tensor-Atom
Shift: A Formal Burnside Lift and an Arithmetic Fredholm No-Go

**Candidate:** SD-C18

**Date:** 2026-08-14

**Status:** SUCCESS

## Build

- Engine: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/Debian)
- Bibliography: BibTeX with `plainnat`
- Final sequence: BibTeX followed by four consecutive clean `pdflatex`
  passes using `-interaction=nonstopmode -halt-on-error`
- Output: `main.pdf`
- Pages: 19
- Page geometry: A4, 595.276 by 841.89 pt
- PDF version: 1.5
- File size: 520345 bytes
- SHA-256:
  `f11aef29764971a6ad0c021dd9f6cf57b6ef7f5b9fdccd7721ca9b7dd6dd44b4`

## Mechanical audit

| Check | Result |
|---|---:|
| LaTeX errors | 0 |
| LaTeX warnings in each final pass | 0 |
| Undefined references | 0 |
| Undefined citations | 0 |
| Overfull boxes | 0 |
| Underfull boxes | 0 |
| Bibliography entries | 14 |
| Distinct cited keys | 14 |
| Uncited bibliography entries | 0 |
| Missing bibliography keys | 0 |
| PDF text markers (`TODO`, `FIXME`, `XXX`, `VERIFY`, `??`, `[?]`) | 0 |
| Unembedded PDF fonts | 0 |
| Unsubset PDF fonts | 0 |

`pdfinfo` confirms A4 geometry, 19 pages, an unencrypted PDF, and anonymous
author metadata.  `pdffonts` reports every font as embedded and subset.
`pdftotext` followed by marker search reports no unresolved placeholders.
The first two pages were also rasterized and visually inspected: the title,
abstract, research-status box, equations, citations, contribution list, and
Figure 1 fit within the page and are legible.

## Scope audit

- The manuscript remains wholly within Symbolic Dynamics.
- The fixed resolved tuple is
  `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`.
- The manuscript states `ROUTE_A_REJECTED` and `ROUTE_B_LOCKED`.
- The scalar Paper 14 A2 shadow is explicitly not patched into SD-C18.
- The no-go is scoped to the canonical rank-one and diagonal models; no
  universal impossibility claim is made.
- No Riemann-zero data, fitting, Route-B carrier, or cross-system-family
  derivation appears.
- External review was intentionally omitted by project instruction.

## Deliverable integrity

The PDF was generated from the modular `main.tex`, `math_commands.tex`,
`sections/`, `figures/incompatibility_triangle.tex`, and `references.bib`
sources.  Compilation auxiliaries were removed after verification; the
source tree, bibliography, final PDF, and this report remain sufficient for
a clean rebuild.
