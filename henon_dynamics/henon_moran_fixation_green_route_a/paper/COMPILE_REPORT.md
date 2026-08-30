# Compilation report

- Engine: LuaLaTeX 1.14, two passes per revision in fresh temporary trees.
- Fixed environment: SOURCE_DATE_EPOCH=1788048000, FORCE_SOURCE_DATE=1, TZ=UTC.
- The LuaTeX trailer ID is fixed in `main.tex`, so independent temporary
  trees produce byte-identical PDFs.  The Moran bibliography title uses
  balanced TeX quotation marks in the final proof package.
- All three PDFs have two pages, pairwise distinct hashes, and main.pdf equals
  main_round2.pdf byte-for-byte.
- SHA-256 hashes (round 0, round 1, round 2/main) are
  `78fe1f288e29c488d812fc4b500ae1efc01e9c7d32d8e7f2925510f79155323a`,
  `cbd4042a88fb026c980c2b7fb9f2606aacb298811ca484815a0ad2c14c83c4a7`, and
  `5fd7a31f51d35ad0f356df8ba87fd09671cf0b7d5889dbf5ed181e9df671fffe`.
- Text extraction and embedded/subset font checks pass; no undefined references
  or missing assets. The previous forced-float note is eliminated by the
  `[htbp]` placement; no layout warning remains in the settled pass.
