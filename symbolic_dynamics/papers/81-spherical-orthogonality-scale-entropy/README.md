# P81 — spherical orthogonality shift

Status: internal Stage-2 short paper; external release **HOLD**.

For the compact-alphabet shift of consecutive orthogonal unit vectors, the
paper proves all-length endpoint bridges, topological mixing, one-symbol
periodic closure, exact finite-block manifold dimension, and

```text
h_epsilon = (d-2) log(1/epsilon) + O_d(1).
```

Thus both metric mean dimensions are `d-2` and topological entropy is
infinite.  The normalized Funk spectrum is cited as prior input, not claimed.

Build and control:

```bash
python3 code/verify_orthogonality_shift.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Source cutoff: 2026-08-27 UTC.  No public posting, submission, or absolute
priority claim is authorized.
