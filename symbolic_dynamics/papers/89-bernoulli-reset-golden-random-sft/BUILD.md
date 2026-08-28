# Build

From this directory run the explicit four-stage build:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run the deterministic proof control with:

```text
python3 code/verify_reset_golden.py
```

The build is an anonymous `amsart` internal preprint and names no target
journal.  The control uses only the Python standard library.

## Final artifact

- Build date: 2026-08-28 UTC
- Four-stage LaTeX/BibTeX build: successful
- PDF: `main.pdf`
- Pages: 6 A4 pages
- Size: 320,648 bytes
- PDF version: 1.5
- SHA-256: `6782a62b934d40f7c1821cd161415a17e308cf4a78391886ecc6f2b639f04c0f`
- Undefined references/citations: 0/0
- LaTeX/package warnings on the final pass: 0
- Overfull/underfull boxes: 0/0
- Fonts: 24/24 embedded, subsetted, and Unicode-mapped
- Exact control: 66,787 integer/rational assertions passed
- Floating diagnostics: 10 passed and explicitly excluded from the exact
  assertion count

External release remains **HOLD** under `README.md` and `FINAL_QA.md`.
