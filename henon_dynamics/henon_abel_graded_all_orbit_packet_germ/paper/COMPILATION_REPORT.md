# Compilation report

- master source: paper.tex;
- engine: pdfTeX 1.40.22;
- bibliography: BibTeX with plain style;
- output: paper.pdf;
- pages: 8;
- PDF metadata author: Liang Wang;
- PDF metadata title: *Abel-Graded All-Orbit Prime-Ideal Packet Germs for a
  Henon Survivor*;
- unresolved citations: 0;
- unresolved references: 0;
- overfull boxes: 0;
- underfull boxes: 0;
- final SHA256:
  3e9257380037469285e6f04cb1de552905ea9ab1dec5e68445b4352567f25b3c.

Compilation sequence:

    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    bibtex paper
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex
    pdflatex -interaction=nonstopmode -halt-on-error paper.tex

The final PDF was visually checked on the title/abstract page, theorem and
figure page, and conclusion/reference page.
