# Paper build

`main.tex` contains three substantive revisions selected by
`\CRevisionRound=0,1,2`.  Round 0 is the original PGF/mean/cycle draft; round 1
adds the all-factorial hierarchy, second moment, singularity extraction,
support constructions, and boundary atlas; round 2 adds the executable audit,
Route-A closure, limitations, availability, and research declarations.

Each archived PDF is produced twice in unrelated temporary directories with
LuaLaTeX, two passes per build, `SOURCE_DATE_EPOCH=1788307200`,
`FORCE_SOURCE_DATE=1`, `TZ=UTC`, and a fixed trailer ID.  The release script
requires both builds to equal the archived bytes, all fonts to be embedded and
subset, settled logs to contain no warning/undefined/rerun/missing-character
event or overfull box above 10 pt, and text contracts to survive extraction.

The final `main.pdf` is byte-identical to `main_round2.pdf`.  Exact hashes,
pages, font rows, and log/visual audit results are frozen in
`COMPILE_REPORT.md` and `C291_RELEASE_MANIFEST.json`.
