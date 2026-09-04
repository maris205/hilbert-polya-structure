# P189 — transpose--row-compression dynamics

**Round:** `ROUND1_FROZEN / REVIEW_A_PASS`  
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
pages.  `main_round1.pdf` is a deliberate byte-identical Review-A receipt of
the frozen Round-0 artifact.  Review A passed with zero findings in
`reviews/round1/reviewer_a/`; Review B and final-release packaging remain
pending.

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

The live PDF, immutable Round-0 copy, and immutable Round-1 copy all have
SHA-256 `6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81`.
This is an internal mathematical artifact, not an external novelty or
circulation clearance.
