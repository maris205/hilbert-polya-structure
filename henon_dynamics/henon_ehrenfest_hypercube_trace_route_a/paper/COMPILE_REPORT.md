# C171 compilation report

- Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).
- Fixed build epoch: `SOURCE_DATE_EPOCH=1787702400` with
  `FORCE_SOURCE_DATE=1`.
- Final artifact: A4, PDF 1.5, 2 pages.
- Round 0 SHA-256:
  `029ae5982a6a45ba9766e27e03d433e8d09ca050696f6ce42a5478fb76b0ac1f`.
- Round 1 SHA-256:
  `9984476f2bc690d88194149e3eafbea4da1e72c30e9704b9896ca2616e447852`.
- Round 2/final SHA-256:
  `592c9a57b5592bdc9e07e4e3554c884e8ca1daaf4154c8bafed02e5dd3cc4c26`.
- The three round hashes are pairwise distinct; `main.pdf` is byte-identical
  to `main_round2.pdf`.
- Two fresh empty-directory, two-pass builds produced the same final SHA-256
  as each other and as the released PDF.
- Embedded-font audit: 23 font records, 23 embedded, 0 non-embedded.
- Final log audit: 0 warning, overfull, underfull, missing-character,
  undefined-reference or missing-glyph matches.
- Text extraction found the English abstract, Chinese abstract, Route-A
  rejected boundary and declarations.
- Visual inspection of both pages found no clipping, collision, spill, blank
  page or unreadable text.

Auxiliary build files are excluded from the package and release manifest.
