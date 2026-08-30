# P124 build record

Status: **ROUND2 GO_INTERNAL / EXTERNAL HOLD**.

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_alg_cross_colon.py
PYTHONDONTWRITEBYTECODE=1 python3 code/verify_alg_cross_colon_basins.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Settled result

- core verifier: **PASS, 1,469,669 assertions**, byte-identical to canonical;
- basin verifier: **PASS, 265,987 assertions**, byte-identical to canonical;
- combined exact controls: **1,735,656 assertions**;
- four-stage LaTeX/BibTeX build: **PASS**;
- PDF: **5 A4 pages, 293,617 bytes**;
- bibliography: **9/9 cited entries resolved**;
- settled LaTeX errors: zero;
- undefined citations and references: zero;
- overfull/underfull box warnings: zero;
- rerun requests: zero;
- all fonts embedded, subsetted, and Unicode-mapped;
- PDF metadata Author empty; no forms, JavaScript, or encryption;
- all five rendered pages visually inspected;
- `main_round0_original.pdf` is the frozen initial snapshot;
- Review A required support-document corrections only, so
  `main_round1.pdf` intentionally retains the same manuscript bytes;
- Review B returned `0 CRITICAL / 0 MAJOR / 0 MINOR` and `GO_INTERNAL`;
- round 2 is support-only, and `main_round2.pdf` is a direct copy of current
  `main.pdf`.

All four PDF snapshots—round 0, round 1, current, and round 2—are
byte-identical, each 293,617 bytes, with SHA-256
`3dd3316a0abbc504a65c6214bc52d4a439a4e16f8290ca655b7fcece2b501f81`.
The source suppresses build dates and variable trailer identifiers.

The round-2 isolated build copied only `main.tex` and `references.bib` into a
fresh temporary directory and ran the four commands above.  Its PDF is
byte-identical to current `main.pdf`.  The package manifest is
`SHA256SUMS`; `sha256sum -c SHA256SUMS` passes for every listed artifact.

Public posting, submission, novelty or priority language, and external
release remain **HOLD**.
