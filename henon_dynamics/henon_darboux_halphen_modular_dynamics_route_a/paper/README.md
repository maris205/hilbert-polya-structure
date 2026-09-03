# C320 paper artifacts

`main.tex` has three cumulative levels selected by `\CRevisionRound`.
The release gate rebuilds each level twice in isolated directories.
`main.pdf` is byte-identical to `main_round2.pdf`; exact pages, sizes, font
rows, and hashes are reported in `COMPILE_REPORT.md`.
