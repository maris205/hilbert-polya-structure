# Build record — P94

From this directory, run:

```bash
python3 code/verify_marked_s_adic.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Expected evidence-bearing source files are `main.tex`, `references.bib`, and
`code/verify_marked_s_adic.py`.  Derived LaTeX files and `main.pdf` are
retained for the internal package audit.

The final checks are:

```bash
pdfinfo main.pdf | grep '^Pages:'
pdffonts main.pdf
grep -E 'undefined|Citation.*undefined|Reference.*undefined|Overfull|Underfull' main.log
pdftotext main.pdf - | grep -E '\?\?|\[\?\]|TODO|FIXME|VERIFY'
```

The frozen package includes `HOSTILE_REVIEW.md`, `FINAL_QA.md`, and the
ten-file `SHA256SUMS` manifest produced after the review and mechanical-QA
stages.

## Recorded build

The four-stage build completed on 2026-08-28 UTC after the exact control
passed.  After the Round-2 wording clarification, the retained `main.pdf` has
7 pages and 352,417 bytes.  The final
`main.log` contains no undefined references or citations and no overfull or
underfull boxes.  All fonts reported by `pdffonts` are embedded subsets with
Unicode maps.
