# Build and review-artifact record — P161

**Date:** 2026-09-02 UTC.  
**Status:** `ROUND-2 / REVIEW B ACCEPTED / HOLD_EXTERNAL`.

## Toolchain and command

- Engine: pdfTeX 1.40.22 / TeX Live 2022/dev/Debian.
- Bibliography: BibTeX 0.99d.
- Class: anonymous `amsart`, 10 pt, A4, 27 mm margins.
- Settled sequence:

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

The retained logs are `build_pdflatex_1.log`, `build_bibtex.log`,
`build_pdflatex_2.log`, and `build_pdflatex_3.log`.  A further settling pass
left the PDF byte-identical.

## Round-0 artifact

| Check | Value |
|---|---|
| Immutable pre-review freeze | `main_round0_original.pdf` |
| Pages / format | 4 / A4 |
| Size | 305,817 bytes |
| SHA-256 | `b0e241883509857362f59688b6ea18422959b07862681cabe13bedfe0d1f79c0` |
| Freeze integrity | preserved unchanged after Review A |
| References | 3/3 cited and resolved |
| Encryption | none |
| Identifying metadata | title, author, subject, and keywords blank |

The final retained pass has no build error, undefined citation/reference,
rerun request, overfull box, or underfull box.  All 21 reported font rows are
embedded, subsetted, and Unicode mapped.  `qpdf` is not installed, so no qpdf
structural check is claimed; `pdfinfo`, `pdffonts`, `pdftotext`, and four-page
raster inspection completed successfully.

## Exact-control freeze

- A fresh paper-local replay matched `verification_output.txt` byte for byte.
- Assertions: 1,317,843, all exact finite-field integer operations.
- Transcript SHA-256:
  `26846bfd5cb94d397605f7f4dbf19b22bb29081fe43156e8e45c5ea2839f045c`.
- Full carriers: 433 states at `p=3` and 98,785 states at `p=7`.
- Checked interfaces include anisotropy, solved altitudes, all literal edges,
  four-cycles, oriented depths, reverse candidates, every target indegree,
  image stabilization, fibre mass, and the empty-core boundary.
- No `__pycache__` or `.pyc` artifact was created.

## Visual and source gates

All four pages were rasterized and inspected.  The zero-credit opening,
theorem, source-subtraction table, oriented depth displays, `0/1/(1+2R)`
fibre law, stable image, reverse-window proof, `p=3` boundary, declarations,
and three references are legible and remain within page bounds.

Kocik–Solecki's legacy DOI was verified and its current DOI redirect recorded;
the orthocentric statement was inspected in the author manuscript.  The
Wildberger chapter DOI/arXiv record and Guy arXiv record were cross-checked,
including the distinction between Guy's Steiner/reflection trisequence and
the literal orthocenter window.  Source verification supports subtraction
only and does not authorize external release.

## Review-A repair and Round-1 artifact

Review A found zero Critical, zero Major, and one Minor build-provenance item:
the Round-0 console emitted a font-expansion ordering warning.  Microtype now
retains protrusion with expansion disabled.  No mathematical or executable
claim changed.

| Check | Value |
|---|---|
| Current / Round-1 PDFs | `main.pdf` / `main_round1.pdf` |
| Pages / format | 4 / A4 |
| Size | 304,462 bytes |
| SHA-256 | `1fcf260e266257c04d0f47aa90a6d47821eefa22834bd32d60fc4a1451d7f214` |
| Current versus Round 1 | byte-identical |
| Current versus Round 0 | intentionally different; Round 0 preserved |

The retained Round-1 logs are `build_round1_pdflatex_1.log`,
`build_round1_bibtex.log`, `build_round1_pdflatex_2.log`, and
`build_round1_pdflatex_3.log`.  The settled log contains zero selected
warning, bad-box, undefined-reference, or rerun lines.  All 21 reported font
rows remain embedded, subsetted, and Unicode mapped; all four repaired pages
passed raster inspection.

## Review-B acceptance and Round-2 artifact

Fresh Review B returned `ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`.
Its independent verifier contains 6,262,521 assertions over `p=3,7,11,19`
and an isotropic `p=5` scope control.  Both its canonical replay and two
source-only cold manuscript builds were byte reproducible.  The two cold PDFs
equal the retained Round-1 PDF, their settled logs contain zero selected
warning or bad-box lines, and all four pages passed fresh visual inspection.

No Round-2 source change was needed.  `main.pdf`, `main_round1.pdf`, and
`main_round2.pdf` are byte-identical: 4 A4 pages, 304,462 bytes, SHA-256
`1fcf260e266257c04d0f47aa90a6d47821eefa22834bd32d60fc4a1451d7f214`.
The immutable Round-0 artifact remains distinct and unchanged.
