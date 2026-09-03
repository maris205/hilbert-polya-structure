# Paper build

`main.tex` contains three substantive revisions selected by
`\CRevisionRound=0,1,2`.  The final `main.pdf` must be byte-identical to
`main_round2.pdf`.

Every round is compiled twice in a fresh temporary directory with LuaLaTeX,
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  The
release gate checks settled logs, text sentinels, control characters, embedded
subset fonts, per-page rasterization, and byte determinism.
