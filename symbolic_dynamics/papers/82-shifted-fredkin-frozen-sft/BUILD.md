# Build

Run all commands from `papers/82-shifted-fredkin-frozen-sft/`.

## Requirements

- Python 3.8 or newer; the control uses only the standard library.
- `pdflatex` and `bibtex` from a standard TeX Live installation.
- `pdfinfo`, `pdffonts`, and `pdftotext` for the release checks.

## Exact finite control

```bash
python3 code/verify_fredkin.py
```

Expected terminal lines:

```text
TOTAL_STATES=299592
ASSERTIONS=1878811
```

## Four-stage LaTeX build

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final pass should produce `main.pdf` with zero LaTeX warnings,
undefined references/citations, and overfull or underfull boxes.

## Release checks

```bash
pdfinfo main.pdf
pdffonts main.pdf
pdftotext main.pdf -
```

Search both source and extracted PDF text for unresolved markers and for any
use of `temporal zeta` that could be confused with the explicitly spatial
frozen-set zeta.
