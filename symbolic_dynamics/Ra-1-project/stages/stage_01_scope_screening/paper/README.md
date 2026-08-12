# Stage-01 Shareable Paper

This directory contains the anonymous preprint **Falsification-First Symbolic
Dynamics for Arithmetic Determinants: Six Audits and Seven Scoped
Obstructions**.

## Deliverables

- [`main.pdf`](main.pdf) — current shareable paper.
- `main_round0_original.pdf` — preserved Phase-4 baseline, before independent
  review.
- `main_round1.pdf` — preserved paper after the first improvement round.
- `main_round2.pdf` — final second-round paper, byte-identical to `main.pdf`.
- `main.tex`, `sections/`, `math_commands.tex`, and `references.bib` — modular
  LaTeX source.
- `figures/` — data-derived figures, their generators, and the generated
  candidate table.
- `NARRATIVE_REPORT.md` and `PAPER_PLAN.md` — claims–evidence narrative and
  manuscript plan.
- `PAPER_IMPROVEMENT_LOG.md` and `PAPER_IMPROVEMENT_STATE.json` — completed
  two-round independent-review record.
- `COMPILATION_REPORT.md` — build and validation record.
- `TEST_REPORT.md` — fresh frozen 29-test rerun and environment versions.

## Scientific status

Six source-locked symbolic objects are audited independently. No single row
passes A0–A4, and every Route-B flag remains locked. The conclusions are
candidate- and theorem-class scoped: they do not rule out symbolic dynamics
as a whole, and the strongest coordinates of different candidates are not
combined.

## Build

From this directory, run:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

Regenerate the figures and candidate table first with:

    python figures/generate_all.py

The current environment does not provide `latexmk`; the verified build uses
the explicit multipass sequence above.
