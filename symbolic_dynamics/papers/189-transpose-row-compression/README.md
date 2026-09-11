# P189 — transpose--row-compression dynamics

**Round:** `ROUND2_DUAL_REVIEW_FREEZE / DUAL_REVIEW_PASS`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

For a labelled binary `n x n` matrix, the map replaces source row `j` by an
initial column of height equal to that row's sum.  The paper proves the exact
four-iterate collapse, recurrent/Fix/strict-two-cycle census, all three depth
layers, and complete time-one/time-two every-target fibre laws.  The case
`n=1` is included explicitly.

The independent author verifier exhausts every matrix through `n=4`, adds
partition and inverse-mass controls through `n=12`, and finishes with
**5,336,613 exact assertions**.  The anonymous deterministic PDF has four A4
pages.  `main_round0_original.pdf`, `main_round1.pdf`, `main_round2.pdf`, and
the live `main.pdf` are byte-identical at SHA-256
`6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81`.
Review A passed with zero findings in `reviews/round1/reviewer_a/`; fresh
Review B passed with zero findings in
`reviews/round2/reviewer_b/`. Terminal QA is closed.

## Exact replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_p189.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_p189.py | cmp - code/CANONICAL.txt
```

## Deterministic build

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
export FORCE_SOURCE_DATE=1
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The live PDF and immutable Round-0, Round-1, and Round-2 copies all have
SHA-256 `6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81`.
This is an internal mathematical artifact, not an external novelty or
circulation clearance.
