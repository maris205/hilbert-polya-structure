# Paper

`main.pdf` is the compiled manuscript for HCS-C20.

Build from this directory with:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The paper proves the characteristic-zero \(D_7\), genus, quotient, Jacobian,
and real-multiplication theorems.  It also proves selected-prime good
reduction and simultaneous normalization at \(p=5,11,13\), so the displayed
\(B,C,E\) polynomials are genuine local Hasse--Weil factors there.
