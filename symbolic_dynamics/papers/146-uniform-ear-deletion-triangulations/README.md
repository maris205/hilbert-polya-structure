# P146 — uniform ear deletion of a convex polygon

Status: **ROUND-2 INTERNAL REVIEW ACCEPTED / OWNER-THIN / HOLD_EXTERNAL**.

Anonymous internal short paper.  The literal random process repeatedly deletes
a uniformly chosen current vertex of a labelled convex polygon.  The paper
derives every triangulation endpoint mass from rooted weak-dual hook counts and
proves the sharp minimum, attained exactly by path-dual triangulations.

## Reproduce

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p146.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p146.py > /tmp/p146_replay.txt
cmp -s /tmp/p146_replay.txt verification_output.txt
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` freezes the visibly defective pre-review build;
`main_round1.pdf` records the theorem/artifact repair; and
`main_round2.pdf` records the accepted build after closing both nonblocking
review-B source/plan minors.  Exhaustive enumeration is a falsifier, not a
proof.  External status remains `HOLD_EXTERNAL`.
