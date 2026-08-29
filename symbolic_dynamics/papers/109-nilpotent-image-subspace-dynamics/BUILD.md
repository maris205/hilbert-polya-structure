# Build record — P109

Status: **final mechanical QA PASS / internal freeze / external HOLD**.

From this directory, run:

```bash
python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Final mechanical freeze

- build date: 2026-08-29 UTC
- exact control: PASS, 515,379 registered assertions; fresh stdout is
  byte-identical to `code/verification_output.txt`
- stored verifier output: 1,388 bytes, SHA-256
  `21f744fbeb1f952de370d8dd0604727ff196d1d8798f679f038a9baa079ce99c`
- two consecutive four-stage LaTeX builds: PASS with identical PDF hash
- artifact: `main.pdf`, 5 A4 pages, 302,089 bytes, PDF 1.5, SHA-256
  `d71468be5407a28719fe755074a63d3006377572866bf9aa3a160367fc652d34`
- actionable LaTeX/package/pdfTeX/BibTeX warnings: 0
- undefined citations/references: 0/0; all 7 bibliography keys cited and
  resolved
- multiply defined labels: 0
- overfull/underfull boxes: 0/0
- fatal/emergency/rerun requests: 0/0/0
- PDF metadata: A4; empty Author; no encryption, forms, JavaScript, or
  rotation; PDF version 1.5
- fonts: all 22 entries embedded, subsetted, and Unicode-mapped
- searchable layout text: 17,773 bytes, 267 lines
- extracted-text sentinels (`??`, `[?]`, `TODO`, `FIXME`, `VERIFY`, bare
  `qquad`): 0
- all five pages rendered at both 120 dpi and 150 dpi and visually inspected:
  PASS
- `SHA256SUMS`: 14 tracked files, self-excluded; `sha256sum -c` PASS 14/14

The source is anonymous.  Full commands and checks are recorded in
`FINAL_QA.md`.  External circulation remains **HOLD**.
