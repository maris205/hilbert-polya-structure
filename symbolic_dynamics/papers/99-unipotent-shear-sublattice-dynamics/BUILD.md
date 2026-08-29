# Build record — P99

Status: **internal mechanical PASS / external HOLD**.

From this directory, the production replay is:

```bash
python3 code/verify_shear_sublattices.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Expected evidence-bearing package files are:

```text
main.tex
references.bib
code/verify_shear_sublattices.py
code/verification_output.txt
README.md
CLAIMS_EVIDENCE.md
CONTROL_RESULTS.md
BUILD.md
HOSTILE_REVIEW.md
FINAL_QA.md
main.pdf
SHA256SUMS
```

## Final production result

- QA date: 2026-08-29 UTC
- exact control: PASS, 93,912 registered assertions
- four stages: PASS (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`)
- artifact: `main.pdf`, 4 A4 pages, 284,865 bytes, PDF 1.5
- PDF SHA-256:
  `311d64d0d6b8d8236e6b6b8e193a10869e66cad705ad8cc1ed14d29c77424c01`
- undefined citations/references: 0/0
- LaTeX/package warnings: 0
- multiply defined labels: 0
- overfull/underfull boxes: 0/0
- fonts: 22/22 embedded, subsetted, and Unicode-mapped
- extracted-text sentinel findings (`??`, `[?]`, `[VERIFY]`, `TODO`,
  `FIXME`): 0
- all 4 rendered pages visually inspected: PASS
- `sha256sum -c SHA256SUMS`: PASS for every entry

Derived LaTeX files and `main.pdf` are retained for the internal package
audit.  Public release, submission, contact, and priority language remain
**HOLD**.
