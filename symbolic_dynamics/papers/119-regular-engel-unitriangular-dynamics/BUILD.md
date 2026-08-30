# Round-two build record — P119

Status: **PASS / ANONYMOUS REVIEW-B REPAIR / EXTERNAL HOLD**.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Settled result

- exact verifier: **PASS, 1,491,877 assertions**;
- fresh stdout: **287 bytes**, byte-identical to
  `code/verification_output.txt`;
- exhaustive controls: 55,808 regular phase states, 39 restricted
  surjections, 112 iterated-fibre profiles, and 20,514 near-regular guard
  states;
- layer artifact: 43 data rows, rebuilt and byte-checked;
- four-stage LaTeX/BibTeX build: **PASS**;
- `main_round0_original.pdf`: 6 A4 pages, 410,459 bytes;
- `main_round1.pdf`: 6 A4 pages, 409,880 bytes;
- `main_round2.pdf` and current `main.pdf`: byte-identical, 6 A4 pages,
  **410,005 bytes**;
- bibliography: 7 cited entries, all resolved;
- settled warnings, errors, undefined citations/references, box warnings,
  and rerun requests: zero;
- fonts: 32/32 embedded, subsetted, and Unicode-mapped;
- PDF metadata: empty Author, date-free, no form, JavaScript, or encryption.

Round one added and subtracted Bier's direct fixed-`J` image theorem.  Round
two limits the abstract fibre quantifier to `gamma_(k+1)`, guards the
deepest-layer formula by `n>=2`, points explicitly to the proof of Bier's
Theorem 1, and fixes Table 1 after the theorem that defines it.  External
novelty, priority, specialist clearance, and circulation remain **HOLD**.

