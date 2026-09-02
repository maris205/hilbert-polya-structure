# P160 — binary-projective Steiner triangle collapse

**Status: ROUND-0 INTERNAL DRAFT / HOLD_EXTERNAL.**

This anonymous short note determines the complete functional graph and every
target fibre of `(a,b,c)->(b star c,c star a,a star b)` on the classical
binary-projective Steiner quasigroup.  Its residual result is the conjunction
of a fixed/three-cycle/depth-one four-stratum graph and the explicit
`1/(N-2)/0` fibre law.  The Steiner system, quasigroup operation, projective
carrier, and generic CA/zeta machinery are explicitly zero credit.

## Exact control

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p160.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p160.py > /tmp/p160_replay.txt
cmp -s /tmp/p160_replay.txt verification_output.txt
```

The Round-0 transcript contains 4,836,144 exact assertions and ends in PASS.

## Build

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Round 0 is not an acceptance or external-release state.  Formal hostile
Reviews A and B and final cold QA remain required.
