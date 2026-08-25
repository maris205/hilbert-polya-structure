# C157 compilation report

- Engine: LuaLaTeX (LuaHBTeX 1.14.0).
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`, `FORCE_SOURCE_DATE=1`.
- Final PDF: `main.pdf`, 2 pages.
- Final PDF SHA-256:
  `3b9c8f688532e933782b7d8227e5ee86e58fa6f74c1149196eaf22a2eaa33ed8`.
- Round artifacts: round 0 (1 page), round 1 (2 pages), round 2/final (2 pages).
- Undefined references/citations: 0.
- Overfull/underfull boxes, missing glyphs, package warnings: 0.
- Fonts: all embedded, including Droid Sans Fallback.
- Determinism: two fresh-directory fixed-epoch builds are byte-identical to
  one another, `main.pdf`, and `main_round2.pdf`.
- Visual inspection: both pages are legible, with no clipping, overlap,
  missing glyph, or blank-region failure.
- Release correction: the second sentinel is displayed as `3.92e-12`, its two
  evaluation points are explicit, and the dual-tail statement includes
  `M>=|s|` without presenting the numerical centers as interval arithmetic.
