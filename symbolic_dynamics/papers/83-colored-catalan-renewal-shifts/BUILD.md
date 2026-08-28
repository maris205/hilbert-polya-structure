# Build

From this directory run:

```bash
python3 code/verify_catalan_renewal.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The build is deterministic apart from standard PDF metadata suppressed in
`main.tex`.
