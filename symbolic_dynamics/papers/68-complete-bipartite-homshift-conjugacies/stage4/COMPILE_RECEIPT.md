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

All commands exited 0.  The final log contains no LaTeX/package warning,
undefined-reference, overfull/underfull-box, or error match.

```text
PDF: stage4/latex_build/main.pdf
pages: 7
bytes: 349071
SHA-256: a8e3491df2ce91ea43c5d1161c0300bb77209bd939f064c6dea20fdb2f8130e9
```
