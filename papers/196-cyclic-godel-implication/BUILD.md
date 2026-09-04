# Deterministic build — P196

Run from this directory:

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Replay the verifier with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
```

The source suppresses volatile PDF metadata. Final byte reproducibility is
checked by the batch cold-build script after both hostile reviews.
