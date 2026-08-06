# Compilation report

Date: 2026-08-06

## Result

- status: **SUCCESS**;
- output: main.pdf;
- engine: pdflatex with BibTeX and two final LaTeX passes;
- total pages: 9;
- main text through Conclusion: page 7 (references start on the same page);
- appendix: pages 8--9;
- PDF size: 286,173 bytes;
- SHA-256:
  e36ed99e10376af03548b489ff70eba222b5dcc5d7c64f9633b5d82c9de79f35.

The environment did not contain latexmk, so the equivalent manual sequence
was used:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

## Checks

- fatal LaTeX/BibTeX errors: 0;
- undefined citations: 0;
- undefined references: 0;
- overfull/underfull boxes in the final log: 0;
- leftover VERIFY, TODO, or FIXME markers in extracted PDF text: 0;
- orphaned section files: 0;
- fonts not embedded: 0;
- title page and appendix visually inspected.

The final compile.log and the individual pass logs are retained beside the
PDF.
