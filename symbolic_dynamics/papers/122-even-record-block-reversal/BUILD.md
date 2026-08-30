# P122 build record

Status: **PASS / ANONYMOUS ROUND-TWO FREEZE / GO_INTERNAL / EXTERNAL HOLD**.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Round-one settled result after hostile repair:

- exact verifier: **PASS, 1,637,027 assertions**;
- four-stage LaTeX/BibTeX build: **PASS**;
- `main_round0_original.pdf`: frozen initial review snapshot;
- `main_round2.pdf` and current `main.pdf`: byte-identical final snapshot;
- current PDF: **4 A4 pages, 293,934 bytes**, deterministic date-free trailer;
- bibliography: **6/6 cited entries resolved**;
- settled errors, undefined citations/references, box warnings, and rerun
  requests: zero;
- all PDF fonts embedded, subsetted, and Unicode-mapped;
- metadata Author empty; no form, JavaScript, or encryption.

Round one corrects the live Huang identity, uses the published bubblesort and
queuesort records, pins the exact Foata transform, makes the five-bit
invariant inductive, adds a complete fibre/bit example, and subtracts
P105/P117/P120 explicitly.  Independent re-entry returned GO_INTERNAL with
no critical or major findings.  Round two only unifies the abstract's
external-HOLD wording; the initial and round-one PDFs remain frozen.
External release remains **HOLD**.
