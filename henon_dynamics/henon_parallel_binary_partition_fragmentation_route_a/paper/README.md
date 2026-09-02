# Paper build

`main.tex` contains three substantive review states selected by the integer
macro `\CRevisionRound`.

Example fresh build of the final round:

```bash
mkdir -p /tmp/c301-paper
cd /tmp/c301-paper
SOURCE_DATE_EPOCH=1788307200 FORCE_SOURCE_DATE=1 \
  lualatex -interaction=nonstopmode -halt-on-error \
  -jobname=main '\def\CRevisionRound{2}\input{/absolute/path/to/paper/main.tex}'
SOURCE_DATE_EPOCH=1788307200 FORCE_SOURCE_DATE=1 \
  lualatex -interaction=nonstopmode -halt-on-error \
  -jobname=main '\def\CRevisionRound{2}\input{/absolute/path/to/paper/main.tex}'
```

The release script performs two isolated two-pass builds for every round and
requires byte identity with the archived PDFs.  `main.pdf` must equal
`main_round2.pdf`.  The Poppler audit checks page readability and embedded
fonts; the log audit rejects layout, reference, citation, rerun, and missing
character warnings.
