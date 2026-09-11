# Deterministic build — P188

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Exact replay:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p188.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p188.py | cmp - CANONICAL.txt
```
