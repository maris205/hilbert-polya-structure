# C170 compile report

- Engine: LuaHBTeX 1.14.0.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Command: `lualatex --interaction=nonstopmode --halt-on-error main.tex` in a fresh isolated directory.
- Final PDF: two A4 pages.
- Two fresh final builds were byte-identical to each other and to released `main.pdf`.
- Round-0 SHA-256: `c5630751db8af61d9c9483c27aadf9735f7d25f9862416bb02959b8c563657eb`.
- Round-1 SHA-256: `aa7ea24c8a92486f6f7d42839ee3597243831828d38c852aca0480321b14b8ef`.
- Final/main-round2 SHA-256: `fdd0782265a5049bbb30211655e8cf8e79ad8e3c52896644e9563ca0a3743db7`.
- The three round hashes are pairwise distinct; `main.pdf` and `main_round2.pdf` are byte-identical.
- `pdffonts` reports every listed font embedded and subset.
- Fresh final logs contain no warning, overfull/underfull box, missing glyph, undefined reference/citation, or multiply defined label.
- Visual audit of both rendered pages found legible English and Chinese text, intact formulas/table/declarations, normal margins and page numbers, and no clipping, collision, truncation, malformed glyph, or unintended blank page.

All build auxiliaries are excluded and absent from release.
