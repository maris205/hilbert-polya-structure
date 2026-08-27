# P80 — cocktail-party majority dynamics

Status: internal Stage-2 short paper; external release **HOLD**.

The paper proves a complete functional-graph description for synchronous
strict majority with inertial ties on `CP_n = K_{2n} \ M`: exact fixed and
two-cycle counts, both consensus basins, all iterate fixed-point counts, the
Artin–Mazur zeta function, the symbolic natural extension, exact Bernoulli
outcome probabilities, and the `n^{-1/2}` critical window.

Build and control:

```bash
python3 code/verify_cocktail_majority.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The script is an exhaustive finite regression check and is not used as a
proof.  Source cutoff: 2026-08-27 UTC.  No public posting, submission, or
absolute priority claim is authorized.
