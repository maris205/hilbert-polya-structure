# Build record — P97

Status: **internal mechanical PASS / external HOLD**.

From this directory, run:

```bash
python3 code/verify_sumset_squaring.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Expected evidence-bearing package files are:

```text
main.tex
references.bib
code/verify_sumset_squaring.py
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
- exact control: PASS, 91,509 assertions, 10,403 literal states, and 17,139
  literal ordered pairs
- four stages: PASS (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`)
- artifact: `main.pdf`, 5 A4 pages, 351,013 bytes, PDF 1.5
- PDF SHA-256:
  `4f1647b3f8e95b2ea7b60025bcbc40d0079f19c79391d2a1c8de27aa0b642952`
- undefined citations/references: 0/0
- LaTeX/package warnings: 0
- multiply defined labels: 0
- overfull/underfull boxes: 0/0
- fonts: 26/26 embedded, subsetted, and Unicode-mapped
- extracted-text sentinel findings: 0
- all 5 rendered pages visually inspected: PASS
- `sha256sum -c SHA256SUMS`: PASS

Derived LaTeX files and `main.pdf` are retained for the internal package
audit.  Public release, submission, contact, venue selection, and absolute
priority language remain unauthorized.
