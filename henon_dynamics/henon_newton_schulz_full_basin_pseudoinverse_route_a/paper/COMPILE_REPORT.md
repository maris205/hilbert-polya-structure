# Compile report

All archives are built from `main.tex` with fixed `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`, using two LuaLaTeX passes in each fresh directory. The release gate requires two byte-identical builds for every round, no settled LaTeX/package/layout/reference warnings, three distinct revision hashes, embedded subset fonts, successful page rasterization, and a round-2 final alias.

Page, font, byte, and SHA-256 receipts are stored in `C317_RELEASE_MANIFEST.json`.
