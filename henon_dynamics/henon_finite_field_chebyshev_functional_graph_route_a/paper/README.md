# Paper build

The source uses `\CRevisionRound` to produce three substantively different manuscripts:

```bash
SOURCE_DATE_EPOCH=1788134400 lualatex -interaction=nonstopmode -halt-on-error -jobname=main_round0_original '\def\CRevisionRound{0}\input{main.tex}'
SOURCE_DATE_EPOCH=1788134400 lualatex -interaction=nonstopmode -halt-on-error -jobname=main_round1 '\def\CRevisionRound{1}\input{main.tex}'
SOURCE_DATE_EPOCH=1788134400 lualatex -interaction=nonstopmode -halt-on-error -jobname=main_round2 '\def\CRevisionRound{2}\input{main.tex}'
```

Each command is run twice from a fresh build directory.  `main.pdf` must equal `main_round2.pdf` byte for byte.  The final release gate independently performs two more fresh round-2 builds, rejects any LaTeX/package/layout/reference warning, verifies embedded subset fonts, and compares exact bytes.
