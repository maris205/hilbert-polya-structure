# P140: Random Majority Triple Contraction

Status: **ROUND-A REPAIRED / GO_INTERNAL / HOLD_EXTERNAL**.

This directory contains an anonymous short exact-probability manuscript for
uniform adjacent majority-of-three contraction on odd binary words. The paper
is deliberately restricted to the closed two-run family for its strongest
endpoint and marked-history laws.

## Core result

For `0^a1^b`, with `a,b>=1` and odd `a+b`, the paper proves:

- exact two-run transition closure;
- terminal probabilities and terminal history counts;
- the complete cross-boundary history-count PGF recurrence, its support, and
  the closed exactly-one-cross probability;
- independence of the entire continuous holding-time vector from the entire
  embedded window history;
- the boundary `tau_1=0` almost surely; for `n=2m+1>=3`, an odd-rate
  exponential-sum completion time and exact `Beta(1/2,m)` representation; and
  a rate-one Gamma scaling limit along `m -> infinity`.

The discrete contraction count is always `(n-1)/2`; it is not the continuous
elapsed completion time.

## Files

- `main.tex`, `references.bib`: anonymous manuscript source and verified
  bibliography.
- `main.pdf`: current repaired four-page A4 manuscript.
- `main_round0_original.pdf`: preserved pre-review PDF.
- `main_round1.pdf`: Round-A repaired freeze, byte-identical to `main.pdf`.
- `HOSTILE_REVIEW_A.md`: independent Round-A review.
- `IMPROVEMENT_LOG.md`: finding disposition and artifact delta.
- `PAPER_PLAN.md`: claim and proof plan.
- `NARRATIVE_REPORT.md`: research narrative and ownership boundary.
- `CLAIMS_EVIDENCE.md`: claim-level proof/control ledger.
- `code/verify.py`: self-contained exact rational verifier.
- `code/verification_output.txt`: canonical verifier stdout.
- `BUILD.md`: reproducible four-stage build record.
- `FINAL_QA.md`: Round-A closure, artifact, bibliography, and visual audit.

## Reproduce the exact control

From this directory:

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

A zero exit code is the byte-replay contract. The frozen run contains 190,740
exact assertions and no sampling or floating point.

## Compile

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

No external posting, contact, authorship, or submission action is authorized.
