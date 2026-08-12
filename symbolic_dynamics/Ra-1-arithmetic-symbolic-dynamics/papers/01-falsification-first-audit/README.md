# Paper 01 — Falsification-First Symbolic Audit

Status: **COMPLETE / FROZEN**

Parent index: [Ra-1-arithmetic-symbolic-dynamics](../../README.md)

Shared rules: [proposal](../../../propose-symbolic-dynamics.md),
[Route A](../../../skills/route-a-evaluator.md), and
[Route B](../../../skills/route-b-evaluator.md)

This paper project contains the anonymous preprint
**Falsification-First Symbolic Dynamics for Arithmetic Determinants: Six
Audits and Seven Scoped Obstructions**, together with its complete Session-4
research package.  Symbolic Dynamics is the only primary system family.

## Shareable paper

- [`main.pdf`](main.pdf) — final shareable paper, 19 pages.
- `main_round0_original.pdf`, `main_round1.pdf`, `main_round2.pdf` — preserved
  review history; Round 2 is byte-identical to `main.pdf`.
- `main.tex`, `sections/`, `figures/`, `math_commands.tex`, and
  `references.bib` — modular source and reproducible figures.
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `PAPER_IMPROVEMENT_LOG.md`, and
  `PAPER_IMPROVEMENT_STATE.json` — claims–evidence and two-round review record.
- `COMPILATION_REPORT.md` and `TEST_REPORT.md` — build and fresh 29-test audit.

## Frozen research lines

| ID | Symbolic object | Purpose |
|---|---|---|
| `SD-C01` | full $q$-shift over $\mathbb F_q$, plus the finite-memory weighted class | Exact function-field prime/repetition ledger and finite-state divisor-growth gate |
| `SD-C02` | squarefree $\mathscr B$-admissible subshift | Test whether direct rational-prime arithmetic in the grammar produces periodic prime orbits |
| `SD-C03` | weighted loop/renewal shift | Test countable-state flexibility, positivity, and inverse-design non-identifiability |
| `SD-C04` | Gauss continued-fraction shift with the Mayer transfer operator | Natural arithmetic/analytic symbolic benchmark and rational-prime ledger audit |
| `SD-C05` | recursive wheel-sieve level shift | Endogenous rational-prime generator and periodic-orbit test |
| `SD-C06` | Knauf number-theoretical spin-chain recursion | Exact zeta-quotient and signed-refinement collision audit |

No single row passes A0–A4, every Route-B flag remains locked, and coordinates
from different rows are not combined.

## Research package

- [`SESSION4_SUMMARY.md`](SESSION4_SUMMARY.md) — final synthesis and Route-A
  matrix.
- [`SESSION4_PREREGISTRATION.md`](SESSION4_PREREGISTRATION.md) — source locks,
  controls, and stop rules.
- [`EXPERIMENT_REPORT.md`](EXPERIMENT_REPORT.md) — numerical results,
  certificates, and reproduction commands.
- `finite_state_arithmetic_skeleton/`, `squarefree_admissible_shift/`,
  `renewal_inverse_design_obstruction/`, `farey_gauss_transfer/`,
  `wheel_sieve_level_shift/`, and `knauf_spin_chain_audit/` — six complete
  candidate packages.
- `evaluations/route_a/` — append-only Route-A records.
- `evaluations/route_b/` — lock notice only; Route B was never invoked.
- [`ROUND2_CLUES.md`](ROUND2_CLUES.md) — cross-family ideas recorded but not
  developed.
- [`PAPER_MANIFEST.sha256`](PAPER_MANIFEST.sha256) — paper-project checksums.

## Build and tests

From this paper-project root:

```bash
python figures/generate_all.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
python -m pytest -q
```
