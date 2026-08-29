# P106 — Synchronous MIS polarity dynamics

Status: **FINAL QA PASS / INTERNAL FREEZE / EXTERNAL HOLD**.

Internal Route-A short paper on the parallel Boolean update

\[
F(A)=\{v:N(v)\cap A=\varnothing\}.
\]

The paper proves the universal cubic collapse `F^3=F`, identifies all
one- and two-cycles, derives the Artin–Mazur zeta function, and proves that
for every bipartite graph the number of periodic configurations is the
square of the number of maximal independent sets.  Paths give an explicit
Padovan-type zeta family.

Known MIS-network fixed-point results and formal-concept polarity are
owner-subtracted; the classical path recurrence has a direct citation.  Two
nonauthor reviews repaired the source boundary and independently confirmed
the synchronous temporal package.  The canonical control has **6,462,317
exact assertions**; the 4-page PDF, consolidated review, final QA, and
verified SHA-256 seal are retained locally.  Direct-system owner risk is high,
so external circulation and priority language remain **HOLD**.

## Reproduce

```bash
python code/verify_mis_polarity.py > code/verification_output.txt
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
