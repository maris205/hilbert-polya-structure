# C219 paper build

Set `SOURCE_DATE_EPOCH=1787875200` and compile `main.tex` with LuaLaTeX.  The
revision switch `CRevisionRound` is `0`, `1`, or `2`; all three PDFs are
distinct and `main.pdf` is byte-identical to round 2.  The final manifest
excludes auxiliary LaTeX sidecars and Python bytecode.
