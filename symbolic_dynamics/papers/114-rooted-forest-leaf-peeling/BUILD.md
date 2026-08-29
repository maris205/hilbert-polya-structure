# Build record — P114

`latexmk` is not installed in the workspace.  The portable build is:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

After both hostile-review repairs, the four documented stages exit `0` and
produce a 3-page A4 `main.pdf`.  The settled log and BibTeX transcript contain
no actionable warning, undefined citation/reference, or over/underfull box;
all 24 font records are embedded, subsetted, and Unicode-mapped.  The fresh
verifier remains byte-identical to `code/verification_output.txt` at 400,105
assertions.  Final deterministic rebuild, all-page visual inspection, and
hash sealing are recorded in `FINAL_QA.md` rather than claimed here.
