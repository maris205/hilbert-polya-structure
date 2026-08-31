# P135 — Derived-centralizer orbit partitions

Status: **GO_INTERNAL / ROUND 2 FROZEN / HOLD_EXTERNAL**.

Internal mathematical short-note package for the self-map on integer
partitions obtained from the natural-point orbits of the derived subgroup of
a permutation centralizer.

The manuscript proves the wreath-product orbit rule, a tagged all-weight
period/tail theorem, the complete recurrent classification and generating
functions, and an exact coefficient formula for every target fibre.

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

See `CONTROL_RESULTS.md` for the frozen exact controls, `BUILD.md` for the
isolated builds, `HOSTILE_REVIEW.md` for the consolidated two-round verdict,
and `FINAL_QA.md` for the terminal artifact audit.

Internal development only.  External release remains `HOLD_EXTERNAL`.
