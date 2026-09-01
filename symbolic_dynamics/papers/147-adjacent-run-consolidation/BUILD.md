# Build and review-closure record — P147

**Status:** **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**

## Toolchain

- Engine: `pdfTeX` through `pdflatex`.
- Bibliography: `bibtex` with `plainnat`.
- Sequence: LaTeX → BibTeX → LaTeX → LaTeX.
- Determinism controls: `SOURCE_DATE_EPOCH=1704067200`,
  `FORCE_SOURCE_DATE=1`, `\pdfinfoomitdate`, empty trailer ID, and suppressed
  PTEX metadata.

## Round-0 artifact

- `main.pdf`: 3 A4 pages, 330,830 bytes.
- `main_round0_original.pdf`: byte-identical preserved snapshot.
- SHA-256: `c21bc9029f7dd697a623f489d446fcfa9329bd96f1bb6ea34e9c363a545a6aa3`.
- Final LaTeX/BibTeX logs: no unresolved citations/references, bad boxes, or
  warnings matched by the QA scan.

## Round-1 repair artifact

- `main.pdf` and `main_round1.pdf`: 4 A4 pages, 338,052 bytes.
- SHA-256: `1d9c5ceb72891e1c509ebeb8adfdb23d110958f129ea7ae32d3c9d427253ce20`.
- The distinct Round-0 PDF remains preserved unchanged at SHA-256
  `c21bc9029f7dd697a623f489d446fcfa9329bd96f1bb6ea34e9c363a545a6aa3`.
- The settled Round-1 log has no unresolved citation/reference, bad box, or
  rerun request.  First-pass warnings caused by the two new citations are
  absent from the settled log.
- Repairs formalize the ancestry selector and all-size witness orbits, type
  the fibre target in `Comp(n)`, and add the 2025/2026 owner-neighbour
  subtraction.

## Independent Review-B build and visual gate

All three Round-0 pages were rasterized at 120 dpi and inspected.  The title,
abstract, theorem, display equations, page breaks, declarations, URLs, and
references are visible; no clipping, collision, blank page, or corrupted
glyph was observed.

Review B cold-replayed the frozen transcript byte for byte: all 2,690,869
integer assertions passed.  Its isolated deterministic
`pdflatex -> bibtex -> pdflatex -> pdflatex` build reproduced the current
Round-1 PDF byte for byte at
`1d9c5ceb72891e1c509ebeb8adfdb23d110958f129ea7ae32d3c9d427253ce20`.
All four current pages were rasterized and inspected; the repaired ancestry
proof and witness displays, theorem, links, declarations, and bibliography
are inside the page bounds, with no clipping, collision, blank page, corrupt
glyph, unresolved marker, or identifying metadata.

Hostile Review A (0 Critical / 1 Major / 3 Minor) is fully closed; Hostile
Review B returned ACCEPT (0 / 0 / 0).

## Final archival freeze

Root preserved the historical artifacts and froze `main_round2.pdf` as a
read-only, byte-identical copy of the accepted current `main.pdf`: 4 A4 pages,
338,052 bytes, SHA-256
`1d9c5ceb72891e1c509ebeb8adfdb23d110958f129ea7ae32d3c9d427253ce20`.
The final paper-local `SHA256SUMS` manifest was regenerated after closure and
passes in full.  This archival step does not change the accepted review
status.
