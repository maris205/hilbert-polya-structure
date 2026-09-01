# Compile report

- Engine: LuaLaTeX, two settled passes per build.
- Reproducibility epoch: `SOURCE_DATE_EPOCH=1788134400`.
- Each revision round was built twice from fresh state; the two builds were
  byte-identical within that round.
- Round 0 SHA-256:
  `34695190fa613ff2f163c03c150892adf513fb884e5993addfb12b0f70d75df8`.
- Round 1 SHA-256:
  `df472f2578a0dbf724cbd31a274122dc168af6742e4df2ba4a5f381262e21a18`.
- Round 2/final SHA-256:
  `06bb70f11ddb1e3dbcdf72a89896b88feb843c354c29a4eac5640dfc9bc350de`.
- `main.pdf` is byte-identical to `main_round2.pdf`.
- The three hashes are distinct, matching the two substantive spectral
  revisions recorded in `PAPER_IMPROVEMENT_LOG.md`.
- Final length: 2 pages; final size: 180,463 bytes.
- Fonts: 25 listed fonts, all embedded and subset.
- Settled logs for all three rounds are warning-free, with no overfull or
  underfull boxes, undefined references, or undefined citations.
- PDF text inspection exposes the algebraic roots, essential edge,
  eigenvalue gate, asynchronous regime, Route-A verdict, scope, and DOI.
- Both pages were rendered at 130 dpi and visually inspected; equations,
  theorem blocks, page breaks, links, and margins are intact.
