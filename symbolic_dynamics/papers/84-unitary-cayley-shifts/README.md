# P84 — unitary Cayley shifts

Status: internal freeze after hostile audit; external release **HOLD**.

The paper turns the known Ramanujan spectrum of the unitary Cayley graph into
an exact symbolic-dynamics package: all periodic counts, rational zeta,
entropy, odd/even mixing-period dichotomy, sharp odd-modulus correlation
rate, and conjugacy rigidity inside the family.

Reproduce:

```bash
python3 code/verify_unitary_cayley.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Evidence cutoff: 2026-08-28 UTC.  No public posting, submission, or absolute
priority claim is authorized.
