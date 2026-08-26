# C172 compilation report

- Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).
- Fixed build epoch: `SOURCE_DATE_EPOCH=1787702400` with
  `FORCE_SOURCE_DATE=1`.
- Final artifact: A4, PDF 1.5, 2 pages.
- Round 0 SHA-256:
  `85512426e9c9d281f115540df049ae8152aa1b26e780d9e8a9fa0fe6d459bfa5`.
- Round 1 SHA-256:
  `9fd6fac3435c6104fe8276e2a652e12151b2d47a387391c96f892aba8ac3d7a1`.
- Round 2/final SHA-256:
  `e33678ba00be91542797fd3c8625c33159b6f9dfcef65e1ad92f9674e7895a37`.
- The three round hashes are pairwise distinct; `main.pdf` is byte-identical
  to `main_round2.pdf`.
- Two fresh empty-directory, two-pass builds produced the same final SHA-256
  as each other and as the released PDF.
- Embedded-font audit: 25 font records, 25 embedded, 0 non-embedded.
- Final log audit: 0 warning, overfull, underfull, missing-character,
  undefined-reference or missing-glyph matches.
- Text extraction found the English abstract, Chinese abstract, qualified A0
  tuple and declarations.
- Visual inspection of both pages found no clipping, collision, spill, blank
  page or unreadable text.

Auxiliary build files are excluded from the package and release manifest.
