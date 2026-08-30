# P125 build record

Status: **PASS / ANONYMOUS ROUND-TWO FREEZE / GO_INTERNAL / EXTERNAL HOLD**.

Reproduce from this directory with:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Round-two settled result

- repaired verifier: **PASS, 27,405,887 exact assertions**;
- fresh stdout: byte-identical to `code/verification_output.txt`;
- isolated four-stage LaTeX/BibTeX build: **PASS (0/0/0/0)**;
- final-stage LaTeX errors: zero;
- undefined citations and references: zero;
- overfull and underfull box warnings: zero;
- rerun requests: zero;
- bibliography: **6/6 cited entries resolved**;
- PDF: **5 A4 pages, 367,999 bytes**;
- PDF metadata Author empty; no forms, JavaScript, or encryption;
- all fonts embedded, subsetted, and Unicode-mapped;
- all five rendered pages visually inspected with no clipping, overlap,
  missing glyph, broken link text, or unresolved marker;
- `main_round0_original.pdf` remains the untouched initial snapshot;
- `main_round1.pdf` is the frozen Review-A repair snapshot;
- `main_round2.pdf` is the phrase-only Review-B repair snapshot and is
  byte-identical to current `main.pdf`.

The round-two four-stage build settled with zero warnings.  The live PDF and
round-two copy have SHA-256

```text
58c48b37ef1da5ff62b4d584c2f3303e6e622cd08f0bb45a6c79068e32c058db
```

The preserved round-zero PDF retains SHA-256

```text
e9f190aed3d2ac1ec337c7d9133f77d2e17c64f8b18070e74587c6c8397d4368
```

Round-two evidence hashes:

```text
main.tex                     d85fb6a2aef1b03d9d203fe8c92d94834ba8c098a4b908f1514cdb9041bcdb7c
references.bib               138ccfc9deec2c31fc8fad76c7046b2f3ce6c3b34e2dba3f60f8cd64a39c3017
code/verify.py               57d9770d3054d28e06ab54bf6faab57140b61dd24f3d6e7f4c7c5d70d55ba96c
code/verification_output.txt 484d8734adfd36a5e562a206fc833fa13eb5240f3ebc36c67ad3c02e2b54ceb0
```

The source suppresses build dates and variable trailer identifiers.  The two
Review-A repairs and the phrase-only Review-B notation repair are recorded in
`IMPROVEMENT_LOG.md`.  Public posting, submission, novelty or priority
language, and external release remain **HOLD**.
