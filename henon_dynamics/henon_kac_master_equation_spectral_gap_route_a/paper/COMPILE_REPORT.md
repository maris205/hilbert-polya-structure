# Compile report

The three manuscript archives and final alias are built from `main.tex` with `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, using two LuaLaTeX passes per clean build.

The release gate requires two byte-identical clean builds per round, no settled LaTeX/package/layout/reference warning, no source control character or missing glyph, embedded subset fonts, successful page rasterization, three distinct round hashes, and exact equality between `main.pdf` and round 2.  Final page, byte, font, raster, and SHA-256 receipts are stored in `C322_RELEASE_MANIFEST.json`.
