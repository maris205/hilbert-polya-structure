# Compile report

The release gate performs two clean two-pass LuaLaTeX builds per round with `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  It requires byte identity, distinct revision hashes, no warning or layout fault, no control character or missing glyph, embedded subset fonts, successful page rasterization, exact revision sentinels, and `main.pdf == main_round2.pdf`.
