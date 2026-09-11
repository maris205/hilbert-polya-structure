# Deterministic build — P187

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Exact control:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_p187.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_p187.py | cmp - code/CANONICAL.txt
```
