# Paper 06 Compilation Report

- Source: `main.tex` with nine modular section files and one pure-TikZ hero
  figure.
- Engine: pdfLaTeX + BibTeX.
- Output: `main.pdf`, A4, 12 pages.
- Frozen PDF: 436700 bytes; SHA-256
  `8fc39f7eba1ad16555f4f727faac27bfe5d9129af82774208701fabb504e6ddd`.
- Final build: four-stage `pdflatex -> bibtex -> pdflatex -> pdflatex` completed
  successfully on 2026-08-13.
- Final log audit: no undefined citations/references, LaTeX warnings,
  overfull boxes, underfull boxes, or fatal errors.
- Visual audit: the hero figure was rasterized from page 2 and inspected;
  boxes, arrows, formulas, caption, and STOP/GO branches are readable. Color
  is redundant with line style and labels.
- PDF metadata: title, author, subject, and keywords are present; the PDF is
  unencrypted and contains no JavaScript.

Intermediate `.aux`, `.bbl`, `.blg`, `.log`, and `.out` files are deliberately
removed after the verified build. `references.bib` remains the authoritative
bibliography source.
