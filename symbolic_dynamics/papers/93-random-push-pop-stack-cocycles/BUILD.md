# Build

From this directory, compile with:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run the deterministic control with:

```text
python3 code/verify_push_pop.py
```

The manuscript is an anonymous `amsart` internal preprint and names no
target journal.  The exact control uses only the Python standard library.

## Current artifact

- Build date: 2026-08-28 UTC
- Four-stage LaTeX/BibTeX build: successful
- PDF: `main.pdf`
- Pages: 7 A4 pages; references begin on page 7
- Size: 350,677 bytes
- PDF version: 1.5
- Undefined references/citations on the final pass: 0/0
- LaTeX/package warnings on the final pass: 0
- Overfull/underfull boxes: 0/0
- Fonts: 25/25 embedded, subsetted, and Unicode-mapped
- Exact control: 265,861 integer/rational assertions passed
- Floating diagnostics: 5 passed and explicitly excluded from the exact
  assertion count

External release remains **HOLD**.  The hostile-review ledger, final QA
record, and checksums are included in the frozen internal package.
