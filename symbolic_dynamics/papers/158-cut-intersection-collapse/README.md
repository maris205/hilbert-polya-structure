# P158 — cut-intersection collapse

Status: **ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL**.

Starting from labelled `K_n`, intersect the current graph with an independent
fair vertex cut at every epoch.  P158 freezes three exact axes:

1. `P(T<=t)=A_(2^(t-1))(n)/2^(tn)`, first-hit probabilities, and the exact
   mean tail series;
2. every labelled target fibre `(R)_r 2^r A_(R-r)(z)`; and
3. the exact image condition and labelled image EGF, including the
   isolate-free `r=R` boundary.

The mandatory sentinel is `n=5,t=2`: two disjoint edges plus one isolate have
zero fibre.  Cuts, bicluster graphs, random-intersection terminology,
labelled EGFs, and inclusion–exclusion receive zero contribution credit.

## Reproduce the exact control

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p158.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p158.py > /tmp/p158_replay.txt
cmp -s /tmp/p158_replay.txt verification_output.txt
```

The frozen run executes 77,530 exact integer assertions, including a literal
successive-intersection/complement-word comparison for every enumerated
history.  Enumeration is counterexample pressure, not proof, source
ownership, novelty, priority, or release clearance.

## Rebuild

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` preserves the original author freeze;
`main_round1.pdf` freezes the Review-A repair, and `main_round2.pdf` is the
byte-identical zero-finding Review-B acceptance freeze.  The hostile reviews
and `IMPROVEMENT_LOG.md` retain the findings and dispositions.
Nothing in this directory authorizes external posting, circulation, author
contact, or submission.
