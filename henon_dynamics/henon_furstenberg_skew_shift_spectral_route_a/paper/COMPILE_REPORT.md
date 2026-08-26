# C169 compile report

- Engine: LuaHBTeX 1.14.0.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Command: `lualatex --interaction=nonstopmode --halt-on-error main.tex` in a fresh isolated directory.
- Final PDF: two A4 pages.
- Two fresh final builds were byte-identical to each other and to released `main.pdf`.
- Round-0 SHA-256: `393c75bf2dadfc21d6c307b15f1e03696106b5db29f546f63cd0092f8dcd4197`.
- Round-1 SHA-256: `79d1ccace7808a61c1d785e8ffcf3019de3d3264b8d455e9e4392b201c003f27`.
- Final/main-round2 SHA-256: `447af4e9468fa8001f0a0bbe42230532f3a6f2254a4f4f8f2513a04a14b5113d`.
- The three round hashes are pairwise distinct; `main.pdf` and `main_round2.pdf` are byte-identical.
- `pdffonts` reports every listed font embedded and subset.
- Fresh final logs contain no warning, overfull/underfull box, missing glyph, undefined reference/citation, or multiply defined label.
- Visual audit of both rendered pages found legible English and Chinese text, intact formulas/table/declarations, normal margins and page numbers, and no clipping, collision, truncation, malformed glyph, or unintended blank page.

All build auxiliaries are excluded and absent from release.
