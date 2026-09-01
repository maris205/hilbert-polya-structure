# Compile report

- Engine: LuaLaTeX, with two settled passes per fresh build.
- Reproducibility epoch: `SOURCE_DATE_EPOCH=1788134400` with
  `FORCE_SOURCE_DATE=1` and `TZ=UTC`.
- Each of rounds 0, 1, and 2 was compiled twice in independently created fresh
  directories; the two PDFs were byte-identical within every round.
- Round 0 SHA-256:
  `3345dd19e8302eda8557682dbaba555aa5091188e1baed69ea54482794dad9ca`.
- Round 1 SHA-256:
  `8032e0ac5ed5f68b366b254813fd28bb76c26c3aa94312a396a9e929a1209cfa`.
- Round 2/final SHA-256:
  `21134aa7aa51475bb686a9ceae9ebe83414aee6ebd38f2b8277f8f14db694cfa`.
- `main.pdf` is byte-identical to `main_round2.pdf`; the three round hashes are
  distinct and match the actual differences recorded in
  `PAPER_IMPROVEMENT_LOG.md`.
- Lengths: 3/3/3 pages for rounds 0/1/2.  Final size: 116,451 bytes.
- Fonts: 12/12/14 listed fonts for rounds 0/1/2; every font is embedded and
  subset.
- All six settled logs are warning-free, with no overfull or underfull boxes,
  undefined references/citations, rerun requests, or missing characters.
- Text extraction for every round confirms its intended revision content and
  the condition-independent, visibly wrapped Route-A tuple.  Final text also
  exposes the theorem status, exact numeric ledger, scope literal, source DOI,
  and arbitrary-Carnot nonclaim.
- Every page of all three rounds was rendered and visually inspected; no
  clipping, overlap, truncated tuple, or malformed glyph was found.
