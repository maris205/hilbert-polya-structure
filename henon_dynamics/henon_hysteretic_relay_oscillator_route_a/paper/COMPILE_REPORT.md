# Compilation report

- Engine: LuaLaTeX 1.14; two passes per revision in fresh temporary trees.
- Fixed environment: SOURCE_DATE_EPOCH=1788048000, FORCE_SOURCE_DATE=1, TZ=UTC.
- The LuaTeX trailer ID is fixed in `main.tex`, so independent temporary
  trees produce byte-identical PDFs.
- All three PDFs have two pages, pairwise distinct hashes, and main.pdf equals
  main_round2.pdf byte-for-byte.
- SHA-256 hashes (round 0, round 1, round 2/main) are
  `01f63ca1884707b9e60a0fa5bdf7bfc3b979635e2b2225dd8e7b6fe97aa1309a`,
  `be625772877bcadbea17e95986cdfeb441268bbf52dade614a235a11a6e13d5a`, and
  `624451ea83a7623cfae7c880a13703a54aecbafe9a9be8a96a8caf6137794ff4`.
- Text extraction and embedded/subset font checks pass; no undefined references
  or missing assets. The previous forced-float note is eliminated by the
  `[htbp]` placement; no layout warning remains in the settled pass.
