# P196 — Cyclic Gödel-implication dynamics

**Round:** `ROUND0_COMPLETE / AWAITING_DUAL_REVIEW`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

On cyclic words over the finite chain `{0,...,q-1}`, the paper studies the
synchronous coordinate rule `T(x)_i = x_i ⇒ x_(i+1)` for Gödel implication.
It proves that one update lands exactly in a constrained cyclic language and
that subsequent updates are rotations. It then gives the complete period
census from a transfer matrix and an every-target product of binomial
differences for the highly nonuniform fibres.

## Exact replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
```

The canonical run checks 123,032 transitions and 492,356 assertions and ends
with `status=PASS`.

## Deterministic build

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The anonymous A4 manuscript is three pages. Classical finite-chain logic,
SFT transfer matrices, and cyclic Möbius inversion receive zero contribution
credit. Posting or submission is not authorized.
