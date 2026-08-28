# Build

`latexmk` was checked first and is unavailable in this environment.  From
this directory, use the reproducible four-stage fallback:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run the deterministic exact control with:

```text
python3 code/verify_socle_shift.py
```

This is an internal anonymous `amsart` preprint and names no venue.  Public
release is on hold.

## Release artifact

- Build date: 2026-08-28 UTC
- PDF: `main.pdf`
- Pages: 5
- Size: 313,957 bytes
- Format: A4, PDF 1.5
- Final TeX pass: successful with zero LaTeX/package warnings
- PDF SHA-256: `c642f7ac4f95d5181b01b852a4550e2c88cbc9193fd38497a97fa05c82aebfd0`
