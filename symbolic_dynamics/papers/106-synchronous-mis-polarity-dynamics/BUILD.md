# Build record — P106

Status: **final internal mechanical PASS / external HOLD**.

From this directory run:

```bash
python code/verify_mis_polarity.py > code/verification_output.txt
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final control output begins with
`synchronous MIS polarity exact controls: PASS`.

## Final production result

- exact control: PASS, **6,462,317 assertions**;
- four stages: PASS;
- artifact: 4 A4 pages, 299,003 bytes, PDF 1.5;
- SHA-256:
  `b20aa2b9cbc33a15c3ce1f99aeab17b077e09c5f4660f617c4ed8a5fbe7687c1`;
- final warnings, undefined citations/references, and over/underfull boxes: 0;
- fonts: 23/23 embedded, subsetted, and Unicode-mapped;
- all four rendered pages visually inspected: PASS;
- `sha256sum -c SHA256SUMS`: PASS.

Build timestamps and external-release metadata are intentionally excluded
from the deterministic manuscript.  See `HOSTILE_REVIEW.md` and
`FINAL_QA.md`; external release remains **HOLD**.
