# Compile report

- Engine: LuaLaTeX, two passes in a fresh temporary directory.
- Deterministic environment: `SOURCE_DATE_EPOCH=1788393600`,
  `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Round 0: 2 pages, SHA-256
  `4da9f036410ec30fd3080ca0907479f540c35e11c60b9721401dbeb334f36867`.
- Round 1: 3 pages, SHA-256
  `144202417e9c69fbe6d3f80e16c42190aa4aab0357a3d3a8d74cbb29aabc3e13`.
- Round 2/final: 3 pages, SHA-256
  `a13711c9f3ccfe29b9e65ae5d4807c805328bdd177c098b839ba633d5946ea69`.
- `main.pdf` is byte-identical to `main_round2.pdf`.
- Each round has 8 font rows; every row is embedded, subset, and Unicode-mapped.
- LaTeX/package warnings: 0.
- Overfull/underfull boxes: 0.
- Undefined references/citations: 0.
- Missing characters/glyphs: 0.
- Forbidden extracted control bytes, `qquad`, `??`, `[VERIFY]`, TODO/FIXME: 0.
- Raster check: every page in all three rounds is nonempty.
- Visual inspection: all 3 final pages inspected; equations, headings,
  footers, theorem text, and source line are visible with no clipping or overlap.

Round 0 contains the complete abelian/Wilson/weighted-law proof.  Round 1 adds
all transfer-current minors and every boundary.  Round 2 adds the exact
evidence receipt, source ownership/collision boundary, and Route-A firewall.
