# Build record — P103

Status: **final internal mechanical PASS / external HOLD**.

```bash
python code/verify_double_adjugate.py > code/verification_output.txt
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final control output begins with
`double-adjugate exact controls: PASS`.  External release remains **HOLD**.

## Final production result

- exact control: PASS, **141,190 assertions** after adding multi-step
  scalar-line image staircases;
- four stages: PASS;
- artifact: 4 A4 pages, 296,320 bytes, PDF 1.5;
- SHA-256:
  `c2f31e00a677cffed632f381717ded6a7628d2ba84e1b375acab2b87340c619a`;
- final log warnings, undefined citations/references, and over/underfull
  boxes: 0;
- fonts: 23/23 embedded, subsetted, and Unicode-mapped;
- all 4 pages visually inspected: PASS;
- `sha256sum -c SHA256SUMS`: PASS.

The full evidence list is frozen in `SHA256SUMS`; see `FINAL_QA.md` for the
mechanical audit and `HOSTILE_REVIEW.md` for the consolidated mathematical
gate.
