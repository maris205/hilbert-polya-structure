# C104 paper

`main.tex` is a short Route-A pilot paper. Build it with

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The PDF reports the exact symbolic result and its limitations: the candidate
polynomial Hénon map has not yet been given a certified three-branch coding,
and the finite determinant is not called Fredholm.
