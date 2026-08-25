# C165 compile report

- Engine: LuaHBTeX 1.14.0.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`, with
  `FORCE_SOURCE_DATE=1` and `TZ=UTC`.
- Command: `lualatex --interaction=nonstopmode --halt-on-error main.tex` in
  a fresh isolated build directory.
- Final PDF: two A4 pages.
- Two fresh isolated builds: byte-identical to each other and to the released
  `main.pdf`.
- Final/main-round2 SHA-256:
  `8902e83f58d04aee5f754e97c8c142db113f8c591ab5a23c868b9396648f3be3`.
- Round-0 SHA-256:
  `72ae89e5c70bfa57c9190781f59879445c91966c4eb8bf00a52feec217a1eea5`.
- Round-1 SHA-256:
  `4c89c0c1a00239169292892b1d561f2f2dec4a7478196fbe35628a9c0dd98c3a`.
- `pdffonts`: every listed font is embedded and subset.
- Fresh final logs contain no warning, overfull/underfull box, missing glyph,
  undefined reference/citation, or multiply defined label.
- Visual audit: both rendered pages show readable English and Chinese text,
  intact formulae, declarations, margins, and page numbers with no clipping,
  collision, truncation, blank region defect, or malformed glyph.
- A post-round hostile audit corrected the `m=1,2` self-adjoint boundaries;
  the two fresh builds above are of that corrected final source.

Build auxiliaries are excluded from release and removed after this report.
