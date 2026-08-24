# Compile report — C120

- Engine: `pdfTeX 1.40.22` through `latexmk 4.76`.
- Deterministic environment: `SOURCE_DATE_EPOCH=0`, `TZ=UTC`, with
  `\pdfinfoomitdate=1` and an empty trailer ID.
- Source SHA-256:
  `c219462025aac0a6ffd4661b8535d28129b18a9fc3c1ff9aaece29dc8d34fe3f`.
- Final PDF SHA-256:
  `6ecb9ba1d6f2d5129949e16d029b0162e7495be5f041b581ddd2aa0f8817fdc4`.
- Page count: `2` A4 pages.
- Two isolated fixed-date builds and the checked-in PDF are byte-identical.
- All fonts reported by `pdffonts` are embedded.
- Final logs contain no LaTeX/package warnings, overfull or underfull boxes,
  undefined or multiply-defined references, or citation warnings.
- Both pages were rendered and visually inspected for clipping, collisions,
  malformed mathematics, and unreadable tables; none was found.
- The final scope paragraph displays the evaluator-native tuple
  `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` and its missing
  prime/A2/divisor obligations without layout overflow.

The round-0, round-1, and round-2 PDFs are byte-identical release snapshots.
The two evidence-led prose passes documented in `PAPER_IMPROVEMENT_LOG.md`
were completed before the fixed-date release build; no external reviewer or
score trajectory is claimed.
