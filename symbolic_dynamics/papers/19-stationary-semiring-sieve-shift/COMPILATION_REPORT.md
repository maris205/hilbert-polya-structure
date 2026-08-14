# COMPILATION REPORT — SD-C21

**Build date:** 2026-08-14
**Engine:** pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022)
**Target:** `main.tex` to A4 PDF

## Clean build protocol

The previous diagnostic products were moved out of the project directory
before the final build.  The manuscript was then compiled with the following
deterministic sequence:

~~~text
pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass 1
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass 2
pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass 3
pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass 4
~~~

BibTeX and all four LaTeX passes exited successfully.  The first pass showed
the expected unresolved-reference bootstrap messages; after BibTeX and the
subsequent passes, the fourth-pass log was clean and stable.

## Final PDF

| item | value |
|---|---|
| pages | 16 |
| page geometry | 595.276 × 841.89 pt (A4) |
| file size | 474,720 bytes |
| SHA-256 | `b0b0dfd43250045a4f42bf021dffc63f602c3edd5659911ccda0f225f58a6fa0` |
| PDF version | 1.5 |
| encryption | none |
| suspect objects | none |

## Warning, citation, and reference audit

The fourth-pass log was searched for `Warning`, `undefined`, `Overfull`,
`Underfull`, multiply defined labels, and `Error`.  The search returned zero
matches.  The BibTeX log was also searched for warnings and errors, with zero
matches.  All 15 bibliography entries are cited and all cited keys resolve;
the extracted PDF contains no `??` or unresolved-reference marker.

The literature database uses primary papers or official publisher records.
The DOI and official-URL locks supporting the closest-collision and
claim-boundary audit are recorded in `SOURCE_LOCK.md` and
`LITERATURE_AUDIT.md`.

## Font audit

`pdffonts` reported 25 font rows.  Every row is a Type 1 font; every font is
embedded and subsetted, and every row reports a Unicode mapping.  No bitmap
or unembedded font is present.

## Source hashes

| file | SHA-256 |
|---|---|
| `main.tex` | `3974975af7c2e69295008cdd506de0e377b22a707745fab87f5565172005d0e4` |
| `references.bib` | `9fe8313718f737c7cffc4a5209f0a6747e4d237fa56c390dda19fde5f2738cb6` |
| `SOURCE_LOCK.md` | `322befdd0c3c43737b1f0d15b6b9e70582de95a5de1612529c1540d4b9042ef8` |

The modular source comprises 1,425 lines across `main.tex`,
`math_commands.tex`, `references.bib`, the section files, and the pure-TikZ
figure source.

## Structural and finite-certificate audit

The final manuscript uses explicit `Q_{n,d,q}` quotient-search states and
contains no existential factor-test transition.  It consistently describes
`L_s` as a source-weighted vertex adjacency, not as a Ruelle transfer
operator.  The prototype report records 13/13 passing tests; its sealed
source-oracle certificate found 1,651 quotient-search nodes/edges and zero
forbidden factor identifiers or calls.

## Visual inspection

Raster inspections were performed on pages 1, 3, 10, and 16: respectively
the title/status page, the pure-TikZ construction and exact-ledger page, the
universal-decider theorem, and the final claim/route ledger.  Text,
equations, tables, hyperlinks, page numbers, and the figure remain inside the
A4 text area.  No clipping, collision, or illegible annotation was found.

## Cleanup

After the audits above, generated auxiliary files were moved out of the
project directory.  The shareable directory retains `main.pdf`, the modular
LaTeX sources, bibliography, pure-TikZ figure, evidence packages, and this
report.
