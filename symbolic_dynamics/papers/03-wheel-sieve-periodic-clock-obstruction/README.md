# Paper 03 — Wheel-Sieve Periodic-Clock Obstruction

Status: **COMPLETE / THEOREM STOP — ROUTE B LOCKED**

Research index: [Ra-1: Arithmetic Symbolic Dynamics](../../README.md)

Shared rules: [proposal](../../propose-symbolic-dynamics.md),
[Route A](../../skills/route-a-evaluator.md), and
[Route B](../../skills/route-b-evaluator.md)

This paper project studies the only live wheel-sieve branch left by Paper 02:
an infinite factor or observational recoding that is shift compatible, retains
the endogenous exact multiplier clock, and might create primitive periodic
orbits.  Symbolic Dynamics is the only primary system family.

The theorem package says that exact clock fidelity and inherited periodicity
are incompatible.  A shift-compatible direct image with a single-valued
exact decoder inherits strict grading and has no periodic points; no topology,
finite alphabet, or locality is required.  The same conclusion holds on an
orbit closure when the target map and total decoder are continuous and each
lagged clock-pair closure misses the diagonal.  This covers exact $q$ and
$\log q$ in their ordinary topologies.  Separately, a compact target cannot
continuously carry the full unbounded clock.

Clock erasure, a discontinuous boundary decoder, or clock compactification
can manufacture target cycles, but those cycles do not inherit a finite exact
wheel clock under the frozen same-object rules.  The elementary periodic
contradiction is classical in mechanism; this paper contributes the
wheel-source-specific obstruction and control package.

No candidate ID is assigned.  No determinant is defined.  Route B remains
locked.

## Shareable paper and artifacts

- [`main.pdf`](main.pdf) — current compiled theorem note, 10 pages.
- `main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` —
  preserved review history; Round 2 is byte-identical to `main.pdf`.
- `main.tex`, `sections/`, `figures/`, `math_commands.tex`, and
  `references.bib` — modular source and pure-TikZ figure.
- [`NARRATIVE_REPORT.md`](NARRATIVE_REPORT.md), [`PAPER_PLAN.md`](PAPER_PLAN.md),
  and [`LITERATURE_AUDIT.md`](LITERATURE_AUDIT.md) — claims, structure, and
  prior-art boundary.
- [`PAPER_IMPROVEMENT_LOG.md`](PAPER_IMPROVEMENT_LOG.md) and `reviews/` —
  independent two-round review record.

- [`SOURCE_LOCK.md`](SOURCE_LOCK.md) — frozen theorem class and claim boundary.
- [`PROOF_PACKAGE.md`](PROOF_PACKAGE.md) — normalized statements, proofs, and
  counterexamples.
- [`ADVERSARIAL_CONTROLS.md`](ADVERSARIAL_CONTROLS.md) — assumption-deletion
  controls and Route-A interpretation.

- [`COMPILATION_REPORT.md`](COMPILATION_REPORT.md) — final build and PDF
  validation.
- [`PAPER_MANIFEST.sha256`](PAPER_MANIFEST.sha256) — complete paper-project
  checksums.

## Build

From this paper-project root:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
