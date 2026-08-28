# P85 — periodic-alphabet full shifts

Status: internal freeze after hostile audit; external release **HOLD**.

The paper gives an explicit block conjugacy from every unconstrained periodic
alphabet schedule to a height-`p` suspension of the full `Q`-shift, where
`Q` is the product of the phase alphabet sizes.  It proves complete
classification by `(p,Q)`, exact periodic counts, zeta, entropy, and the
unique maximal law.

Reproduce:

```bash
python3 code/verify_periodic_alphabet.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Evidence cutoff: 2026-08-28 UTC.  No public posting, submission, or absolute
priority claim is authorized.
