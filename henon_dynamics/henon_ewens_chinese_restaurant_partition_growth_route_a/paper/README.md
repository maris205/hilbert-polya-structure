# Paper build

`main.tex` has three conditional revisions.  Build round `r` with LuaLaTeX and

```text
\def\CRevisionRound{r}\input{main.tex}
```

The release gate performs two clean fixed-epoch builds for each revision and requires byte identity.  The final `main.pdf` is byte-identical to `main_round2.pdf`.
