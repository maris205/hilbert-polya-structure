# Compilation report

- **Status:** SUCCESS
- **PDF:** `paper/main.pdf`
- **Size:** 260,866 bytes
- **Total pages:** 9
- **Main body:** conclusion ends on page 7
- **Appendix/references:** begin on page 8; final bibliography continuation on page 9
- **Undefined references:** 0
- **Undefined citations:** 0
- **Overfull boxes:** 0
- **Underfull boxes:** one noncritical bibliography paragraph (`badness 1360`)
- **Orphaned section files:** 0
- **Fonts:** embedded Type-1 fonts
- **Residual markers:** no `TODO`, `FIXME`, `XXX`, or `[VERIFY]`

The environment provides `pdflatex` and `bibtex` but not `latexmk`.  The
successful fallback sequence was:

```bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The first page was rasterized to a temporary directory and visually inspected.
The title, abstract, theorem formula, and opening text render correctly.  No
temporary inspection image was added to the repository.

This is a mathematical obstruction note rather than a venue-formatted
conference submission.  The seven-page main body and two-page
appendix/bibliography package are within the default nine-page main-body
budget used during the writing audit.
