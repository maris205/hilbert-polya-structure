# Build record — P96

Status: **internal mechanical PASS / external HOLD**.

From this directory, the final production replay used:

```bash
python3 code/verify_finite_subset_circle.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Expected evidence-bearing source files are:

```text
main.tex
references.bib
code/verify_finite_subset_circle.py
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

- QA date: 2026-08-28 UTC
- exact control: PASS, 7,000 assertions and 189,245 literal subsets
- four stages: PASS (`pdflatex`, `bibtex`, `pdflatex`, `pdflatex`)
- artifact: `main.pdf`, 8 A4 pages, 350,561 bytes, PDF 1.5
- PDF SHA-256:
  `99e8dc79d7a2882afad5de08f8ab633e8bddb30b60d1d40848cbcefcec45f8a3`
- undefined citations/references: 0/0
- LaTeX/package warnings: 0
- multiply defined labels: 0
- overfull/underfull boxes: 0/0
- fonts: 23/23 embedded, subsetted, and Unicode-mapped
- extracted-text sentinel findings (`??`, `[?]`, `[VERIFY]`, `TODO`,
  `FIXME`): 0
- all 8 rendered pages visually inspected: PASS
- `sha256sum -c SHA256SUMS`: PASS

Derived LaTeX files and `main.pdf` are retained for the internal package
audit.  Public release, submission, contact, and absolute priority language
remain unauthorized.
