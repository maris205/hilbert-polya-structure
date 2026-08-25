# C160 compile report

- Engine: LuaHBTeX 1.14.0.
- Command: `SOURCE_DATE_EPOCH=1700000000 FORCE_SOURCE_DATE=1 lualatex --interaction=nonstopmode --halt-on-error main.tex`.
- Final PDF: two A4 pages.
- Fresh fixed-epoch double build: byte-identical.
- Final/main-round2 SHA-256:
  `cd4df138379fd4b689ac749337abebf785f1a42a32164842dbc84a9d2c29d7c5`.
- Round-0 SHA-256:
  `0750541d1eb81fbd9a1216aa50049a1c8653155d3dfee3d09f947e8a3d10c143`.
- Round-1 SHA-256:
  `9c3f1632c402be2304a81b1dafca2d293f14125412f6efa94032bea513d0c658`.
- `pdffonts`: every listed font is embedded and subset.
- Final log: no warning, overfull/underfull box, missing glyph, undefined
  reference/citation, or multiply defined label.
- Visual audit: formulas, bilingual abstracts, long integers, declarations,
  and page margins show no clipping, collision, or truncation.

Build auxiliaries are excluded from release and removed after this report.
