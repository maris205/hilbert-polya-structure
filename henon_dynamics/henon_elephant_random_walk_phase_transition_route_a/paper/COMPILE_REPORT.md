# Compile report

The three revision archives and final alias are produced from `main.tex` under fixed `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC` using two LuaLaTeX passes per clean build. The release gate requires two byte-identical clean builds per round, no settled LaTeX/package/layout/reference warnings, embedded subset fonts, successful page rasterization, three distinct round hashes, and a round-2 final alias.

Final page, font, byte, and SHA-256 receipts are recorded in `C316_RELEASE_MANIFEST.json`.
