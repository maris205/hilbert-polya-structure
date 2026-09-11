# P195 — Odd-side least-neighbour tree walks

**Round:** `ROUND0_COMPLETE / AWAITING_DUAL_REVIEW`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

The carrier is a labelled tree with a distinguished root. The root moves to
the least-labelled neighbour whose side of the cut edge has odd cardinality.
The paper proves the complete recurrent classification, the sharp
`floor((n-1)/2)` tail, parity-separated recurrent EGFs, an every-target local
fibre formula, and sharp fibre maxima.

## Exact replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
```

The exhaustive run covers every Prüfer tree and root through `n=8`, checking
2,223,278 transitions and 4,328,312 assertions.

## Deterministic build

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The anonymous A4 manuscript is three pages. Posting and submission are not
authorized.
