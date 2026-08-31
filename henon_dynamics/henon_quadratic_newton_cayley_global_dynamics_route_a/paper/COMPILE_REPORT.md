# C257 deterministic paper compile report

- Engine: LuaHBTeX/LuaLaTeX (TeX Live 2022), PDF 1.5.
- Frozen environment: `SOURCE_DATE_EPOCH=1788048000`,
  `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Each of rounds 0, 1, and 2 was built twice from fresh temporary directories,
  with two LuaLaTeX passes per fresh build.  Both builds of every round were
  byte-identical.
- Round hashes:
  - round 0: `dfd224f58699fb28acbe829c73385aed928755a265b169d2af23dd9c1d017096`
  - round 1: `e9a2c9ee0aa4297d54f71f8b190f4933a2f9ee06f79747f119d9f2adac7f52c5`
  - round 2: `10ee0b0fd7a4e2e8b8bda30e181ce6b667666d52601cd6e041d6b0b14938281f`
- `main.pdf` equals round 2 byte for byte; SHA-256 is
  `10ee0b0fd7a4e2e8b8bda30e181ce6b667666d52601cd6e041d6b0b14938281f`.
- Final dimensions: 2 A4 pages, 327578 bytes.
- Font gate: 24 font records; every font is embedded and subset.
- Log gate: no overfull/underfull boxes, undefined references/citations,
  unresolved rerun request, or package/LaTeX warning after the second pass.
- Text gate: title, Cayley/preperiodic/Cauchy theorems, scope literal,
  evaluator tuple, overall rejection, and Route-B false statement are
  extractable with `pdftotext`.
- Visual gate: both final pages were rasterized at 120 dpi and inspected;
  equations, headings, margins, references, and page breaks are intact.
- The three revision PDFs have distinct hashes, and the final artifact is
  release-ready.
