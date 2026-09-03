# Paper build

`main.tex` contains three conditional revision states.  Build round `r` with

```text
lualatex -interaction=nonstopmode -halt-on-error -jobname=main "\def\CRevisionRound{r}\input{main.tex}"
```

The release script performs two fresh fixed-epoch builds per revision and requires byte identity with the checked PDFs.  `main.pdf` is byte-identical to `main_round2.pdf`.
