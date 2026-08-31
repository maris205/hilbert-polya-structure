# Paper build

`main.tex` is the final round-2 source.  Every revision is compiled twice in
fresh temporary trees with two LuaLaTeX passes, fixed
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
The fixed trailer ID makes same-source PDFs byte-identical.
