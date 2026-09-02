# Manuscript build

`main.tex` is a single deterministic source parameterized by `\CRevisionRound`.

```bash
SOURCE_DATE_EPOCH=1788307200 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error \
  -jobname=main '\def\CRevisionRound{2}\input{/absolute/path/to/paper/main.tex}'
```

Run twice in a clean temporary directory.  Rounds 0, 1, and 2 are archived separately; `main.pdf` equals `main_round2.pdf` byte for byte.  The release closer enforces settled logs, embedded subset fonts, required extracted text, rasterizability, and byte-identical rebuilds.
