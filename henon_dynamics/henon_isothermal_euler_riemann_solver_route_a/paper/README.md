# Manuscript build

`main.tex` is parameterized by `\CRevisionRound` and retains three substantive revisions.

```bash
SOURCE_DATE_EPOCH=1788307200 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error \
  -jobname=main '\def\CRevisionRound{2}\input{/absolute/path/to/paper/main.tex}'
```

Run twice in an otherwise empty directory.  The release closer repeats two fresh isolated builds per round and enforces byte equality, settled logs, embedded subset fonts, required extracted text, and rasterizability.  `main.pdf` equals `main_round2.pdf` byte for byte.
