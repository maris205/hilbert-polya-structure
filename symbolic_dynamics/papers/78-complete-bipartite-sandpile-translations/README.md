# P78 — complete-bipartite sandpile translations

Status: internal Stage-2 short paper; external release **HOLD**.

For recurrent Abelian sandpiles on `K_{m,n}` with a sink in the `n`-part,
the paper computes the exact order of an arbitrary integral loading profile
from explicit inverse-Laplacian coordinates.  A two-site loading reduces to
up to four denominator classes, with three when `n=2`.  The paper then gives the uniform orbit
decomposition, every iterate fixed-point count, the Artin–Mazur zeta function,
invariant measures, and the full finite Koopman spectrum.  Single-site
periods are `mn` opposite the sink and `m` beside the sink.

Build and control:

```bash
python3 code/verify_sandpile_translation.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Source cutoff: 2026-08-27 UTC.  No public posting, submission, or absolute
priority claim is authorized.
