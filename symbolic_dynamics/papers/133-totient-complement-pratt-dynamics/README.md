# P133 — Totient--complement Pratt dynamics

Status: **GO_INTERNAL / ROUND 2 FROZEN / HOLD_EXTERNAL**.

Internal mathematical short-note package for the squarefree divisor map

```text
d -> gcd(n,(n/d)phi(d)).
```

The manuscript proves a literal support conjugacy, the complete source-phase
recurrent decoder, a nonsharp `h+1` entry bound, and an every-target
inclusion--exclusion fibre formula.

## Reproduce

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)

pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

See `CONTROL_RESULTS.md` for the frozen verifier transcript, `BUILD.md` for
the isolated builds, `HOSTILE_REVIEW.md` for the consolidated two-round
verdict, and `FINAL_QA.md` for the terminal artifact audit.

Internal development only.  External release remains `HOLD_EXTERNAL`.
