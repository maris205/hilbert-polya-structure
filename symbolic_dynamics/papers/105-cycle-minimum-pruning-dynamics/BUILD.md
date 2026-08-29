# Build record — P105

Status: **final internal mechanical PASS / external HOLD**.

From this directory, run:

```bash
python3 code/verify_cycle_minimum_pruning.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Evidence-bearing final-package files are:

```text
main.tex
references.bib
code/verify_cycle_minimum_pruning.py
CONTROL_OUTPUT.txt
README.md
CLAIMS_EVIDENCE.md
CONTROL_RESULTS.md
BUILD.md
HOSTILE_REVIEW_A.md
HOSTILE_REVIEW_B.md
HOSTILE_REVIEW.md
FINAL_QA.md
main.pdf
SHA256SUMS
```

## Final production result

- build date: 2026-08-29 UTC;
- exact control: **PASS**, 17,219,241 assertions;
- four stages: **PASS** (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`);
- artifact: `main.pdf`, 5 A4 pages, 331,334 bytes, PDF 1.5;
- SHA-256:
  `f4a6f777cda71f702edb979e0d9ddb33ba9f77646d1cbbdbe02e50c3905bd85f`;
- undefined citations/references: 0/0;
- LaTeX/package warnings: 0;
- overfull/underfull boxes: 0/0;
- fonts: 24/24 embedded, subsetted, and Unicode-mapped;
- extracted text: 17,919 bytes, with no `??`, `[?]`, TODO, FIXME, XXX, or
  `[VERIFY]` sentinel;
- Python bytecode syntax check: **PASS**.
- all five rendered pages visually inspected: **PASS**;
- `sha256sum -c SHA256SUMS`: **PASS**.

Independent cross-hostile ledgers A and B, the consolidated review, and final
QA are frozen.  External release remains **HOLD**.
