# P141: Weighted Threshold-Graph Random Greedy MIS

Status: **ROUND-B OWNER-SUMMARY REPAIR COMPLETE / GO_INTERNAL
(OWNER-THIN) / HOLD_EXTERNAL**.

This directory contains an anonymous, specialized exact-law note for positive-
rate random-greedy maximal independent sets on labelled threshold graphs. The
threshold-graph support, the RSA/random-greedy process, and the
Plackett/exponential weighted order are fully owned inputs and receive zero
contribution credit here. This is not a new greedy-MIS process.

## Core residual

After those owned inputs are subtracted, the note derives:

- the weighted reverse-stick endpoint distribution;
- reverse-hazard recovery and an open-simplex parametrization;
- precise nonidentifiability of the original vertex-rate vector;
- the accepted-update size PGF and first two moments;
- all vertex marginals and nested inclusion laws for zero vertices;
- a clock firewall separating full scans, accepted updates, priority-label
  span, and continuous completion time.

Only `K=|I|` has the displayed size PGF. Continuous time obeys a separate
active-set Laplace recursion.

Theorem 3.1's weighted reverse-stick endpoint law is **owner-thin and
folklore-risky**: it is a short conditioning consequence of the fully owned
support/process/order machinery. Its inverse/simplex, PGF, and marginal
consequences inherit that owner-thin status. No direct printed owner was found
in the bounded audit, but that non-hit is not novelty, priority, or owner
clearance. External status therefore remains `HOLD_EXTERNAL`.

## Files

- `main.tex`, `references.bib`: anonymous source and verified bibliography.
- `main.pdf`: current four-page A4 manuscript, unchanged by Round A.
- `main_round0_original.pdf`: preserved Round-0 freeze.
- `main_round1.pdf`: Round-A theorem/artifact PASS freeze, byte-identical to
  Round 0 and current.
- `main_round2.pdf`: Round-B owner-summary-repair freeze, also byte-identical.
- `HOSTILE_REVIEW_A.md`: independent Round-A PASS review.
- `HOSTILE_REVIEW_B.md`: independent Round-B theorem PASS and documentary
  owner-framing repair request.
- `IMPROVEMENT_LOG.md`, `OWNER_REPAIR_LOG.md`: round history, documentary
  repair, and artifact identity records.
- `PAPER_PLAN.md`, `NARRATIVE_REPORT.md`, `CLAIMS_EVIDENCE.md`: claim,
  ownership, proof, and evidence records.
- `code/verify.py`: self-contained exact rational verifier.
- `code/verification_output.txt`: canonical verifier stdout.
- `BUILD.md`, `FINAL_QA.md`: reproducible build and Round-B closure audit.

## Reproduce the exact control

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

The frozen replay contains 750,181 exact assertions and no sampling or
floating point.

## Compile

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

No external posting, contact, authorship, or submission action is authorized.
