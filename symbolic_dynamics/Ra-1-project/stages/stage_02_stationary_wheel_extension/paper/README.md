# Stage-02 Shareable Paper

This directory contains the anonymous, theorem-only preprint
**Scoped Obstructions to Stationarizing a Graded Wheel-Sieve Symbolic
System**.

## Deliverables

- NARRATIVE_REPORT.md — claims, evidence, non-claims, and provenance.
- PAPER_PLAN.md — claims--evidence matrix and section/figure plan.
- main.tex and sections/ — modular anonymous LaTeX source.
- figures/obstruction_map.tex — reproducible pure-TikZ theorem relationship
  figure; it contains no empirical data.
- main.pdf — compiled shareable preprint.
- main_round0_original.pdf — byte-identical Phase-4 baseline preserved before
  any independent review or improvement.
- main_round1.pdf — manuscript after the first independent review and fix
  pass.
- main_round2.pdf — manuscript after the independent second-round
  verification and final scope-clarity fixes; byte-identical to main.pdf.
- PAPER_IMPROVEMENT_LOG.md and PAPER_IMPROVEMENT_STATE.json — complete
  review text, response ledger, and two-round workflow state.
- COMPILATION_REPORT.md — build and validation record.

## Scientific status

The paper proves three scoped obstruction families:

1. strict equivariant extensions cannot add periodic points, while the
   graded source itself has an empty full-backward-orbit inverse limit;
2. strong forward-bisimulation quotients of forward-well-founded graphs are
   acyclic (finite DAGs are a corollary), with a separate grading obstruction
   for representative-exact next-prime state decoders; and
3. finite-alphabet fixed-window decoders have finite image and cannot recover
   the infinite exact clock range.

The bisimulation theorem does **not** cover an infinite DAG with an infinite
forward path.  The finite-local-decoder theorem does **not** cover countable
alphabets or infinite memory.  The remaining observational-recoding branch
is NOT_TESTABLE because its infinite mathematical specification is
incomplete.

No Stage-02 numerical experiment has been run and no determinant convention
has been defined.  In project terminology, Route B is the later analytic
determinant-comparison route; it remains locked.

## Build

From this directory, run:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

The manuscript has no external citations; references.bib is intentionally
empty.  The current environment did not provide latexmk, so the verified
build used repeated pdflatex passes.

Both independent reviewer/improvement rounds are complete.  The final
assessment is 8/10: accepted as a precise, externally shareable scoped
project preprint.  Ignored LaTeX intermediates were removed after validation;
either build command regenerates them.
