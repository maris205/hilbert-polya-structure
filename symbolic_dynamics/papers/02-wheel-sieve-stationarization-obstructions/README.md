# Paper 02 — Wheel-Sieve Stationarization Obstructions

Status: **THEOREM SCREENING COMPLETE; RECODING SOURCE LOCK PENDING**

Research index: [Ra-1: Arithmetic Symbolic Dynamics](../../README.md)

- Primary family: **Symbolic Dynamics only**
- Candidate ID: **not assigned**
- Route B: **locked**

This paper project contains the anonymous theorem-only preprint
**Scoped Obstructions to Stationarizing a Graded Wheel-Sieve Symbolic
System** and all supporting proof/source-lock material.

## Shareable paper

- [`main.pdf`](main.pdf) — final shareable paper, 11 pages.
- `main_round0_original.pdf`, `main_round1.pdf`, `main_round2.pdf` — preserved
  review history; Round 2 is byte-identical to `main.pdf`.
- `main.tex`, `sections/`, `figures/`, `math_commands.tex`, and
  `references.bib` — modular theorem source and pure-TikZ figure.
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `PAPER_IMPROVEMENT_LOG.md`, and
  `PAPER_IMPROVEMENT_STATE.json` — claims–evidence and two-round review record.
- `COMPILATION_REPORT.md` — final build and PDF validation.

## Exact theorem screen

1. If $\pi\circ S=\sigma\circ\pi$, an $S$-periodic point would project to a
   periodic point of the strictly graded wheel shift.  Independently, the
   frozen source's full-backward-orbit inverse limit is empty.
2. A strong forward-bisimulation quotient of a forward-well-founded graph is
   acyclic; every finite wheel DAG is a corollary.
3. A representative-exact state-class decoder for $q_{k+1}$ prevents
   cross-level merging and preserves strict grading.
4. A fixed finite-window decoder over a finite alphabet has finite image and
   cannot recover the unbounded exact prime clock.

These are scoped obstruction classes, not a universal no-go theorem.  Infinite
graphs with infinite forward paths, countable alphabets, and infinite-memory
rules remain outside the corresponding theorem hypotheses.

## Supporting package and live obligation

- [`G0_STRICT_EXTENSION_OBSTRUCTION.md`](G0_STRICT_EXTENSION_OBSTRUCTION.md)
- [`G0B_BISIMULATION_AND_CLOCK_OBSTRUCTIONS.md`](G0B_BISIMULATION_AND_CLOCK_OBSTRUCTIONS.md)
- [`STAGE2_PREREGISTRATION.md`](STAGE2_PREREGISTRATION.md)
- [`OBSERVATIONAL_RECODING_SOURCE_LOCK.md`](OBSERVATIONAL_RECODING_SOURCE_LOCK.md)
- [`refine-logs/EXPERIMENT_PLAN.md`](refine-logs/EXPERIMENT_PLAN.md)
- [Paper-01 dependency](../01-falsification-first-audit/wheel_sieve_level_shift/README.md)
- [Paper-01 ROUND2 ledger](../01-falsification-first-audit/ROUND2_CLUES.md)
- [`PAPER_MANIFEST.sha256`](PAPER_MANIFEST.sha256)

The observational-recoding source lock is incomplete.  Until it specifies one
infinite phase space, level-blind rule, alphabet/memory class, exact arithmetic
and clock decoders, path-lifting semantics, and cutoff consistency, no
implementation is authorized, no `SD-C07` is assigned, and no determinant is
defined.

## Build

From this paper-project root:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
