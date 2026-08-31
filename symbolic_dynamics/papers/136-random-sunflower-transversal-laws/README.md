# P136: Recorded-Transversal Laws on Rate-Weighted Sunflower Forests

Status: **GO_INTERNAL / ROUND 2 FROZEN / HOLD_EXTERNAL**.

This directory contains a short exact-probability manuscript for the surviving
SF1 theorem package. It is deliberately positioned as an exact law for a
restricted, already-owned random covering process. It does not claim a new
algorithm, exponential-race method, or general forest-independence principle.

## Core result

For vertex-disjoint heterogeneous sunflowers with fixed positive edge rates,
the paper derives:

- every weighted selected-petal endpoint mass;
- every actual recorded vertex-set mass;
- at unit rates, the full choice-count PGF, mean, second moment, and variance;
- the marked stopped endpoint tensor product, additive discrete choice count,
  and product choice-count PGF for a disjoint forest.

The endpoint is the full recorded set and need not be minimal.
The choice count is not continuous elapsed time. The paper makes no wall-clock
convolution claim; under its exponential embedding, forest completion occurs
at the maximum of the component stopping times.

## Files

- `main.tex`, `references.bib`: anonymous manuscript source.
- `main.pdf`: current compiled manuscript.
- `main_round0_original.pdf`: immutable copy of the first compiled draft.
- `main_round1.pdf`: Review-A-repaired compiled draft.
- `main_round2.pdf`: Review-B sign-off copy, byte-identical to the current PDF.
- `PAPER_PLAN.md`: claim and proof plan.
- `NARRATIVE_REPORT.md`: research narrative and boundary statement.
- `CLAIMS_EVIDENCE.md`: claim-level proof/control ledger.
- `CONTROL_RESULTS.md`: frozen exact-arithmetic replay record.
- `BUILD.md`: stable five-stage clean build and PDF QA record.
- `HOSTILE_REVIEW_A.md`, `HOSTILE_REVIEW_B.md`, `HOSTILE_REVIEW.md`: two
  independent review rounds and their consolidated verdict.
- `FINAL_QA.md`, `SHA256SUMS`: terminal artifact audit and frozen manifest.
- `code/verify.py`: self-contained rational verifier.
- `code/verification_output.txt`: canonical verifier stdout.

## Reproduce the control

From this directory:

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

A zero exit code is the byte-replay contract. See `CONTROL_RESULTS.md` for the
frozen input and assertion counts.

## Compile

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

No external submission action is authorized by this package.
