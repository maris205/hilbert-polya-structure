# C176 compile report

- Engine: LuaHBTeX 1.14.0.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Command: two passes of `lualatex --interaction=nonstopmode --halt-on-error main.tex` in each fresh isolated directory.
- Final PDF: three A4 pages.
- Two fresh final builds were byte-identical to each other and to released `main.pdf`.
- Round-0 SHA-256: `e66b00e7b51b3b2723ca13d64337350979e857f5d50b77b82c1a2a3be2b65552`.
- Round-1 SHA-256: `df9cadc1f5b94209424468dc0bbe7a761a5abba84b197b1682b8ffbcc2e17e09`.
- Final/main-round2 SHA-256: `e17ed450d618f5a17c151207d3fddccb667cd24496ec329fb4a209a2cc1bdcf6`.
- The three round hashes are pairwise distinct; `main.pdf` and `main_round2.pdf` are byte-identical.
- `pdffonts` reports every listed font embedded and subset.
- Fresh final logs contain no warning, overfull/underfull box, missing glyph, undefined reference/citation, rerun request, or multiply defined label.
- Visual audit of all three rendered page snapshots found legible English and Chinese text, intact formulas/table/declarations, normal margins and page numbers, and no clipping, collision, truncation, malformed glyph, or unintended blank page.

All build auxiliaries are excluded and absent from release.
