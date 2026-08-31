# Paper build

`main.tex` is the final round-2 source.  Each revision is compiled twice in a
fresh temporary directory with LuaLaTeX, two passes per build, under
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

The fixed trailer ID makes independent builds byte-identical.  The three
revision PDFs are retained; `main.pdf` equals `main_round2.pdf`.
