# P83 — colored Catalan renewal shifts

Status: internal freeze after hostile audit; external release **HOLD**.

For the countable loop shift with `c*C_(n-1)` first-return loops of length
`n`, the paper proves the exact transition

```text
c=1 transient  ->  c=2 null recurrent  ->  c>=3 positive recurrent,
```

together with closed Gurevich entropy, maximal-measure return law, algebraic
zeta, and exact fixed-point laws at both boundary parameters.

Reproduce:

```bash
python3 code/verify_catalan_renewal.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Evidence cutoff: 2026-08-28 UTC.  No public posting, submission, or absolute
priority claim is authorized.
