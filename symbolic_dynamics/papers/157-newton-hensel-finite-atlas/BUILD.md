# Build and review-artifact record — P157

**Date:** 2026-09-02 UTC.  
**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

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
| Size | 331,521 bytes |
| SHA-256 | `4188a459ad233e8a6a55d5706648617e833ea0f7771d324a368352182a2f9c0d` |
| Freeze integrity | preserved unchanged after Review A |
| References | 1/1 cited and resolved |
| Encryption | none |
| Identifying metadata | title, author, subject, and keywords blank |

The final retained pass has no build error, undefined citation/reference,
rerun request, overfull box, or underfull box.  All 25 reported font rows are
embedded, subsetted, and Unicode mapped.  `qpdf` is not installed, so no qpdf
structural check is claimed; `pdfinfo`, `pdffonts`, `pdftotext`, and four-page
raster inspection completed successfully.

## Review A repair and Round-1 artifact

Review A reported zero Critical, zero Major, and two Minor wording issues.
The title is now neutral rather than eponymic; “complete” is restricted to
the proved temporal and one-step inverse interfaces.  No formula, proof, or
verifier changed.  The settled Round-1 sequence is retained as
`build_round1_pdflatex_1.log`, `build_round1_bibtex.log`,
`build_round1_pdflatex_2.log`, and `build_round1_pdflatex_3.log`.

| Check | Value |
|---|---|
| Round-1 PDF | `main_round1.pdf` |
| Pages / format | 4 / A4 |
| Size | 331,596 bytes |
| SHA-256 | `f054f639f4c9ba9d462c183f417597390223b18ca3f74ba5907c39637ba4743e` |
| Historical state | distinct from Round 0; both preserved |

Review B later found that the Round-1 settled log does contain a pdfTeX
font-expansion ordering warning; the original zero-warning sentence here was
therefore inaccurate.  The PDF remained deterministic and visually valid.

## Review-B repair and Round-2 artifact

Review B returned zero Critical, zero Major, and one Minor build-provenance
finding.  Microtype now retains protrusion with expansion disabled; the
transcript hash is placed on its own small line to keep the expansion-free
layout free of bad boxes.  No mathematical or executable claim changed.

| Check | Value |
|---|---|
| Current / Round-2 PDFs | `main.pdf` / `main_round2.pdf` |
| Pages / format | 4 / A4 |
| Size | 349,380 bytes |
| SHA-256 | `6b0c1fb81c065a9213df4cb4af7b731e25e02e3306e6220a154899166e9129dd` |
| Current versus Round 2 | byte-identical |
| Historical rounds | Round 0 and Round 1 preserved at recorded hashes |
| Isolated builds | 2/2 byte-identical to current |

The retained Round-2 logs are `build_round2_pdflatex_1.log`,
`build_round2_bibtex.log`, `build_round2_pdflatex_2.log`, and
`build_round2_pdflatex_3.log`.  Their settled pass has zero actual warning,
bad-box, undefined-reference, or rerun messages.  All 25 font rows remain
embedded, subsetted, and Unicode mapped; all four pages passed final raster
inspection.

## Exact-control freeze

- Fresh paper-local replay matched `verification_output.txt` byte for byte.
- Assertions: 2,563,880, all exact integer operations.
- Transcript SHA-256:
  `f5f1884f809110ca8ec3a954af1783c774896708495d626f694bbfb23f7876f1`.
- The normalized-unit lanes cover `v=1..6`, `N=1..11`; the full atlas covers
  every state and every target through `n=17`.
- No `__pycache__` or `.pyc` artifact was created.

## Visual and source gates

All four pages were rasterized and inspected.  The neutral title and
abstract, direct-prior paragraph, theorem, subtraction table, `N=1,2`
boundaries, exact lifting proof, every-target fibre proof, declarations, and
single reference are legible and remain within page bounds.

The BibTeX metadata was cross-checked against DOI content negotiation,
publisher metadata, arXiv, and the author manuscript.  Appendix Lemma A.4 of
the direct-prior manuscript explicitly prints `G_1(x)=3x^2-2x^3`.  This verification
supports subtraction only; it does not authorize external release.
