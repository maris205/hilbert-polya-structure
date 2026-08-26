# C178 compile report

- Engine: LuaHBTeX 1.14.0.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`.
- Command: `lualatex --interaction=nonstopmode --halt-on-error main.tex`,
  twice in each fresh isolated directory.
- Final PDF: two A4 pages.
- Two fresh final builds were byte-identical to each other and to released
  `main.pdf`.
- Round-0 SHA-256:
  `1134e2ae678cb2ba5f16cba2a8e09383975249726b74d725810377532d1be962`.
- Round-1 SHA-256:
  `e784823ef6029b27cf4dc1942aaeb071e4c8201a18a32d24773084be717fc62d`.
- Final/main-round2 SHA-256:
  `936b9aa851d26114e4131a649460ad84e7522e7e6dbfa21907558810113d3fb3`.
- The three round hashes are pairwise distinct; `main.pdf` and
  `main_round2.pdf` are byte-identical.
- `pdffonts` reports every listed font embedded and subset.
- Both fresh final logs contain no warning, overfull or underfull box,
  missing character or glyph, undefined reference or citation, multiply
  defined label, or error.
- Visual audit of both rendered pages found legible English and Simplified
  Chinese text, intact formulas including the metaplectic \(2\pi\) sign and
  \(4\pi\) return, an intact decision table, normal margins and page
  numbers, and no clipping, collision, truncation, malformed glyph, or
  unintended blank page.

All build auxiliaries are excluded and absent from release.
