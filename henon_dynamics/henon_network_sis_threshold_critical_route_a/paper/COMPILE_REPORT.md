# Compile report

- Engine: LuaLaTeX, two settled passes per build.
- Reproducibility epoch: `SOURCE_DATE_EPOCH=1788134400`.
- Each revision round was built twice from fresh state; the two builds were
  byte-identical within that round.
- Round 0 SHA-256:
  `dc5784b015d69721c60033708b5bd03fcd8d1a631bf4e18506d8ccc67d86a0fa`.
- Round 1 SHA-256:
  `58faff18875db3e3b916dff5bf2275654985d6e4c7c5b4244f866e3f97252928`.
- Round 2/final SHA-256:
  `666b0e3e62cef878a88caf0305d9cdc6e6331e1ddab42c76369f1e9973c0c03e`.
- `main.pdf` is byte-identical to `main_round2.pdf`.
- The three hashes are distinct, matching the two substantive theorem
  revisions recorded in `PAPER_IMPROVEMENT_LOG.md`.
- Final length: 2 pages; final size: 160,906 bytes.
- Fonts: 22 listed fonts, all embedded and subset.
- Settled logs for all three rounds are warning-free, with no overfull or
  underfull boxes, undefined references, or undefined citations.
- PDF text inspection exposes the unique-endemic theorem, the critical `1/t`
  law, the Route-A verdict, the scope literal, and the source DOI.
- Both pages were rendered at 130 dpi and visually inspected; equations,
  theorem blocks, page breaks, links, and margins are intact.
