# Build record

Build date: 2026-08-29 UTC.

The canonical PDF was produced with:

~~~bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
~~~

Final result: **main.pdf**, A4, 5 pages. The terminal log has no undefined
citation/reference, overfull box, or LaTeX warning. Exact equations and the
depth polynomial carry the relevant information; the figure phase therefore
records **NO_FIGURE_NEEDED**.
