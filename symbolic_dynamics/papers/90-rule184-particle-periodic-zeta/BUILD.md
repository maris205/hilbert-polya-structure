# Build record — P90

## Commands

Run from this directory:

```bash
python3 code/verify_rule184.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Dependencies are Python 3, BibTeX, and pdfLaTeX with the standard packages
named in `main.tex`. The exact control has no third-party Python dependency.

## Final artifact

- file: `main.pdf`
- format: PDF 1.5, A4
- pages: 5
- size: 329,610 bytes
- SHA-256: `7db799503da50d23f747c1a6f7e1483e7a0316b36e52dd4d91cb9615ca55b964`
- pdfTeX: 1.40.22 (TeX Live 2022/Debian environment)

The final log has no undefined citation/reference, rerun request, overfull or
underfull box, or LaTeX/package warning. All PDF fonts reported by `pdffonts`
are embedded and subsetted. Text extraction and all five rendered pages were
inspected. External release remains **HOLD**.
