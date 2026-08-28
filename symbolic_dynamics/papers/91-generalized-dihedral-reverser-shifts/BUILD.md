# Build record — P91

## Commands

Run from this directory:

```bash
python3 code/verify_reverser_shift.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Dependencies are Python 3, SymPy, BibTeX, and pdfLaTeX with the standard
packages named in `main.tex`. All Python comparisons are exact.

## Final artifact

- file: `main.pdf`
- format: PDF 1.5, A4
- pages: 4
- size: 296,997 bytes
- SHA-256: `196160eff81a974c496e0259ca15f73e9b8fcf6a7838cf5afef193ef0c5c6df6`
- pdfTeX: 1.40.22 (TeX Live 2022/Debian environment)

The final log has no undefined citation/reference, rerun request, overfull or
underfull box, or LaTeX/package warning. All PDF fonts reported by `pdffonts`
are embedded and subsetted. Text extraction and all four rendered pages were
inspected. External release remains **HOLD**.
