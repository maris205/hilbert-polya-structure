# Build record — P110

Status: **final mechanical QA passed for internal use / external HOLD**.

From this directory, run:

```bash
python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Required source/evidence files are:

```text
main.tex
references.bib
code/verify.py
CONTROL_OUTPUT.txt
README.md
CLAIMS_EVIDENCE.md
CONTROL_RESULTS.md
BUILD.md
```

## Final frozen replay

- final replay date: 2026-08-29 UTC;
- exact control: **PASS**, 1,916,206 assertions, with fresh stdout
  byte-identical to `CONTROL_OUTPUT.txt` and SHA-256
  `8b88fb8202b063ee843eb5941ed57a373b8941f1759c5d334447105913d01ab3`;
- literal phase states: 142,417 partitions through `n=10`;
- independent binary-cut lane: every nonconstant cut through `n=12`;
- four-stage LaTeX build: **PASS** (`pdflatex`, `bibtex`, `pdflatex`,
  `pdflatex`);
- `main.pdf`: 5 A4 pages, 321,838 bytes, PDF 1.5, SHA-256
  `313c9f3584ebb4e38d8c88450b060ec9429f31fe33eb7db2ee1b948936682f3b`;
- a second complete four-stage build reproduced that PDF hash exactly;
- final `main.log`/`main.blg`: zero actual warnings, undefined citations or
  references, multiply defined labels, overfull or underfull boxes, fatal
  errors, or rerun requests;
- `pdfinfo`: empty author field, no encryption, forms, JavaScript, or
  rotation;
- fonts: 25 of 25 embedded, subsetted, and Unicode-mapped;
- plain extracted text: 16,448 bytes in 370 lines;
- layout-preserving extracted text: 19,535 bytes in 271 lines, with no exact
  unresolved sentinel;
- bibliography closure: 4/4 keys cited, zero uncited or undefined key;
- Python syntax check: **PASS**;
- deterministic rebuild: final PDFs byte-identical;
- rendered visual inspection at 150 dpi: all 5 pages **PASS**, with no clipping,
  overlap, orphan reference page, or illegible material;
- consolidated Review A/B record: **PASS**, zero unresolved mathematical
  issue;
- `SHA256SUMS`: frozen evidence manifest validated by `sha256sum -c`;
- external release: **HOLD**.

See `HOSTILE_REVIEW.md`, `FINAL_QA.md`, and `SHA256SUMS` for the consolidated
review, complete mechanical gate, and frozen evidence package.
