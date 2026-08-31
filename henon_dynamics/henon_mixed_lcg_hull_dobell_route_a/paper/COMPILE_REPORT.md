# Compilation report

- Engine: LuaLaTeX / LuaHBTeX 1.14.0, two passes per revision in two fresh
  temporary trees.
- Fixed environment: SOURCE_DATE_EPOCH=1788048000, FORCE_SOURCE_DATE=1,
  TZ=UTC.
- The LuaTeX trailer ID is fixed in main.tex.  Both fresh builds in every
  round were byte-identical.
- All three retained PDFs have two pages and pairwise distinct hashes;
  main.pdf equals main_round2.pdf byte-for-byte.
- SHA-256 values for round 0, round 1, and round 2/main are
  2f4e608dd5b94a70db0d07a7e05f5b5205ab4e34d7c8337640369a0bd48fc1a0,
  df9c0f557627f8c62b6dcd5633f397874bad5b7647e01c61473924a90ceddf3c,
  and 533ae5616e925f9025a8db853da9dfd9ef84541245d61a811d4f996a1b9b9fc2.
- The settled build has no layout, citation, reference, or rerun warning.
  Text extraction, both-page visual inspection, and embedded/subset font
  checks pass.
