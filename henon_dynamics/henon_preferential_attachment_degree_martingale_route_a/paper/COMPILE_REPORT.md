# Compile report

The three revision archives and final alias are produced from `main.tex` with fixed `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, using two LuaLaTeX passes per clean build.

The release gate requires two byte-identical clean builds for each round, no settled LaTeX/package/layout/reference warning, no control character or missing glyph, embedded subset fonts, successful page rasterization, three distinct round hashes, and an exact round-2 final alias.  Final page, font, byte, and SHA-256 receipts are recorded in `C321_RELEASE_MANIFEST.json`.
