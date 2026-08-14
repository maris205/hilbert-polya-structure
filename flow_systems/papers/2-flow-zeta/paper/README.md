# Paper

The final manuscript is [paper.pdf](paper.pdf).  It was independently reviewed,
revised, rebuilt with XeLaTeX, and visually inspected.  The final log contains
no undefined citations/references, missing characters, or overfull boxes.

Build with:

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
```

`manuscript.pdf` is the build target; `paper.pdf` is the release copy.
