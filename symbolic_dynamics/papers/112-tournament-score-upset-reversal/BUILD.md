# Build record — P112

Status: **POST-REVIEW REPAIR MECHANICAL PASS / NOT FINAL QA / EXTERNAL HOLD**.

The environment does not provide `latexmk`, so the repository-standard
four-stage build is:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run the exact control separately with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
```

## Current post-review repair result

- exact verifier: **PASS**;
- exact assertions: **1,677,508** over all **33,868** labelled tournament
  states for `0<=n<=6`;
- fresh verifier stdout: byte-identical to the stored **781-byte**
  `code/verification_output.txt`;
- LaTeX/BibTeX build: **PASS** under the four commands above;
- artifact: `main.pdf`, **8 A4 pages**, **332,780 bytes**, PDF 1.5;
- main body through Conclusion: page **7**;
- References begin: page **7** and end on page **8**;
- actual final LaTeX warnings: **0**;
- actual final BibTeX warnings: **0**;
- undefined citations/references: **0**;
- overfull/underfull boxes: **0**;
- bibliography closure: **13/13** cited keys, with no uncited entry;
- PDF author metadata: empty;
- deterministic PDF date/trailer controls: active, with no creation or
  modification date reported by `pdfinfo`;
- fonts: **23/23 embedded, subsetted, and Unicode-mapped**;
- unresolved sentinels (`??`, `[?]`, `[VERIFY]`, `TODO`, `FIXME`): **0**.
- visual inspection: all **8/8** rendered pages checked; the corrected
  iterate display has `t-1` with no comma, and the mechanics table and
  references are legible with no clipping or overlap.

This is a repair-stage compilation record only.  It is not a final QA or
owner clearance.  No artifact hash, Git operation, external posting, or
submission action was performed.  External release remains **HOLD**.
