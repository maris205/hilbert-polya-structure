# Stage 4 compile receipt

Date: 2026-08-26 UTC

The requested `latexmk` invocation could not run because `latexmk` is not
installed in the execution environment (`exit 127`).  The available TeX
toolchain was run instead in the isolated `stage4/latex_build/` directory:

```text
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=stage4/latex_build main.tex
bibtex stage4/latex_build/main
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=stage4/latex_build main.tex
pdflatex -interaction=nonstopmode -halt-on-error -output-directory=stage4/latex_build main.tex
```

All commands exited 0.  A final two-pass `pdflatex` refresh after the last
source edit also exited 0.  The final log contains no LaTeX/package warning,
undefined-reference, overfull/underfull-box, or error match.

```text
PDF: stage4/latex_build/main.pdf
pages: 11
bytes: 409160
SHA-256: cee9a255bbb805601531855c38512bcb011868825786f4dd56747055ce432454
```
