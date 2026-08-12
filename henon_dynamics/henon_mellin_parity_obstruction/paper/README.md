# Paper

`main.tex` is the theorem-level obstruction note. Build it with

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The paper distinguishes the certified local divisor theorem from a global
strip census and from an operator-scattering construction. Generated LaTeX
auxiliary files are not release artifacts.
