# P114 — Rooted-forest leaf peeling

Anonymous internal short paper on the finite dynamical system obtained by
deleting every non-root leaf of a labelled rooted forest in parallel.

The paper determines, for every ambient label size `n`:

- the endpoint and exact pointwise clock;
- every root-set basin and every bounded-depth shell;
- every one-step fibre from only the target's vertex and non-root-leaf counts;
- the phase size, fixed/periodic census, zeta function, and, for `n>=2`, the
  sharp maximum depth and all deepest states (with `n=0,1` stated separately).

Classical Cayley/all-minors and labelled-height formulas, parallel `RAKE`,
height-driven dynamical pruning, parallel leaf stripping,
inclusion–exclusion, absorption/zeta conversion, and Hamilton-path extremality
are explicitly subtracted.  The residual internal result is only the
endpoint-indexed finite-map assembly and `(m,s)` fibre calculation; a bounded
search is not evidence of priority for either.
External posting, submission, novelty, and priority remain `HOLD_EXTERNAL`.

## Reproduce

```bash
python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The canonical verifier reports `400,105 exact assertions; PASS` through
`n=6`.  The compiled manuscript is `main.pdf`.
