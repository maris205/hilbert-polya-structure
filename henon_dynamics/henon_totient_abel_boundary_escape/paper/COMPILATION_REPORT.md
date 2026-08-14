# Compilation report

- **Status:** SUCCESS
- **PDF:** `paper/paper.pdf`
- **Pages:** 7 total
- **Author metadata:** Liang Wang
- **Title metadata:** Totient Abel Laws and Tagged-Mass Escape at a Henon
  Packet Boundary
- **Engine:** pdfTeX 1.40.22 / LaTeX2e
- **Bibliography:** BibTeX with `plainnat`
- **Undefined references:** 0
- **Undefined citations:** 0
- **Overfull boxes:** 0
- **Underfull boxes:** 0
- **Fonts embedded:** YES
- **Visual inspection:** first and theorem/table/conclusion pages PASS
- **Final equals round two:** YES

Build command:

```bash
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```
