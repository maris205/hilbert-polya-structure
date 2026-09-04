# P186 — rank-compression support dynamics

**Round:** `ROUND2_DUAL_REVIEW_FREEZE`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

For a sorted subset `A={a_0<...<a_{k-1}}` of `[0,n-1]`, the paper studies

```text
T(A) = support{a_j-j}.
```

It proves the all-time ordered-gap formula, exact pointwise maximum-gap
clock, all basins, a unique deepest state, all-time image condition and
image size, every-time every-target fibre generating function, Fibonacci
first images, and every depth population.

The paper-local replay is byte-stable and ends with **12,104,596 exact
assertions** over every subset through `n=18`.  Two process-separated hostile
reviews add 28,872,986 assertions, close two Round-0 Minor abstract-scope
findings, and leave zero open findings.  The final PDF has three A4 pages.

## Exact replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p186.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p186.py | cmp - CANONICAL.txt
```

## Deterministic build

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` preserves the author artifact;
`main_round1.pdf` preserves the accepted abstract repairs;
`main_round2.pdf` is a byte-identical Review-B receipt.  Two source-only cold
builds reproduce the final PDF.  No external action is authorized.
