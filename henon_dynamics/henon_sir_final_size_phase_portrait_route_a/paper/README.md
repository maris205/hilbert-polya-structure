# Build C198 paper

Compile `main.tex` twice with LuaLaTeX and a fixed `SOURCE_DATE_EPOCH`.  Select
rounds 0 and 1 by defining `\CRevisionRound`; the default is final round 2.
The three round PDFs preserve substantive theorem revisions and `main.pdf`
equals round 2.

Release checks fixed-epoch fresh reproducibility, font embedding, logs, text,
metadata and every rendered page.  Build sidecars are excluded from the
content-addressed manifest.
