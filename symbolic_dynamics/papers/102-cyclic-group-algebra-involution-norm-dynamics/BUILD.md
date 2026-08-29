# Build record — P102

Status: **final internal mechanical PASS / external HOLD**.

From this directory, the production replay is:

```bash
python3 code/verify_involution_norm.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The expected final evidence files are:

```text
main.tex
references.bib
code/verify_involution_norm.py
code/verification_output.txt
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

- build date: 2026-08-29 UTC
- exact control: PASS, 116,278 registered assertions
- four LaTeX stages: PASS (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`)
- artifact: `main.pdf`, 6 A4 pages, 328,565 bytes, PDF 1.5
- undefined citations/references: 0/0
- LaTeX/package warnings: 0
- multiply defined labels: 0
- overfull/underfull boxes: 0/0
- PDF font entries: 24/24 embedded, subsetted, and Unicode-mapped
- extracted-text sentinels (`??`, `[?]`, `TODO`, `FIXME`, `VERIFY`): 0
- PDF SHA-256: `94d699e7e2609c8039a200cbaa14a92a34190a9b221cad3b88961d967cc657aa`
- all six final page renders visually inspected: PASS
- `sha256sum -c SHA256SUMS`: PASS

The exact script uses only Python's standard library and integer/polynomial
finite-field arithmetic.  The two hostile reviews and final QA are frozen;
external circulation stays **HOLD**.
