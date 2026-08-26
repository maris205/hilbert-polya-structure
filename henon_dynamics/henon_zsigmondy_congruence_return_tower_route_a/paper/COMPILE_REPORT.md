# C179 compile report

- Engine: LuaHBTeX 1.14.0.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787788800`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`.
- Command: `lualatex --interaction=nonstopmode --halt-on-error main.tex`,
  twice in each fresh isolated directory.
- Final PDF: three A4 pages.
- Two fresh final builds were byte-identical to each other and to released
  `main.pdf`.
- Round-0 SHA-256:
  `b2ba74069d020f1c2c91102be7c66241c0a064c0cfa44d5a31b403a1b1bd95d6`.
- Round-1 SHA-256:
  `4fb4f610e974edb13af2d927c36ecf4f4e939a6116c0abc39bc695d5c7395c65`.
- Final/main-round2 SHA-256:
  `caba3bffcd0b1081f7fd93d1660cf3b317f994e96cb975f7d34ae6795f3d5374`.
- The three round hashes are pairwise distinct; `main.pdf` and
  `main_round2.pdf` are byte-identical.
- `pdffonts` reports every listed font embedded and subset.
- Round-0, round-1, and both fresh final logs contain no LaTeX warning,
  overfull or underfull box, missing character or glyph, undefined reference
  or citation, multiply defined label, or error.
- Visual audit of all three rendered final pages found legible English and
  Simplified Chinese, intact first-return and lift formulas, complete finite
  and global zeta formulas, an intact Route-A decision table, normal margins
  and page numbers, and no clipping, collision, truncation, malformed glyph,
  unintended blank page, or hidden content.

The validator amendment changed only the reported repaired-hash regression
count from 60 to 64.  Two new fresh isolated builds remained byte-identical;
the theorem, scope, reference population, and page count are unchanged.

All build auxiliaries are excluded and absent from release.
