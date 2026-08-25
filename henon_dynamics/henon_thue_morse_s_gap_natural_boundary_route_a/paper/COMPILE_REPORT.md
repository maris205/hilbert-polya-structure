# C159 compile report

- Engine: LuaHBTeX 1.14.0.
- Command: `SOURCE_DATE_EPOCH=1700000000 FORCE_SOURCE_DATE=1 lualatex --interaction=nonstopmode --halt-on-error main.tex`.
- Final PDF: two A4 pages.
- Fresh fixed-epoch double build: byte-identical.
- Final/main-round2 SHA-256:
  `1eb08405e11870017c9ef448fa2c14cb5b93a53916b09421d5e46c0741c6ab5c`.
- Round-0 SHA-256:
  `455a3d02845c3479d9552612490e7a3e6f10a08187d7b6401edc910c2f4ba1b4`.
- Round-1 SHA-256:
  `9ddbc3eddf93bb1de6161677f6aa43ad0e6e38c16779aca5b6bcf3a1271f2d61`.
- `pdffonts`: every listed font is embedded and subset.
- Final log: no warning, overfull/underfull box, missing glyph, undefined
  reference/citation, or multiply defined label.
- Visual audit: both pages contain readable content; equations, Chinese text,
  declarations, and page margins show no clipping, collision, or truncation.

Build auxiliaries are excluded from release and removed after this report.
