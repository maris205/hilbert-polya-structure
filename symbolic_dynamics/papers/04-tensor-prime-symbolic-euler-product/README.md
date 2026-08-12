# Paper 04 — Tensor-Prime Symbolic Euler Product

Status: **ROUTE-A ANALYTIC CANDIDATE — A0–A2 EXACT / ROUTE B LOCKED**

Research index: [Ra-1: Arithmetic Symbolic Dynamics](../../README.md)

Shared rules: [proposal](../../propose-symbolic-dynamics.md),
[Route A](../../skills/route-a-evaluator.md), and
[Route B](../../skills/route-b-evaluator.md)

This paper freezes `SD-C07`, a single countable symbolic suspension derived
from the symmetric monoidal skeleton of finite full shifts.  Cartesian
product gives (F_m\otimes F_n\cong F_{mn}), while topological entropy gives
(h(F_n)=\log n).  The nonunit tensor atoms are therefore exactly the full
(p)-shifts, without reading a prime table, and their entropy supplies the
roof (\log p).

The canonical atom-loop shift has one primitive period-one orbit for every
tensor atom and no cross-atom transitions.  On
\(\ell^2(\operatorname{At})\), its weighted transfer operator is diagonal:

\[
  \mathcal L_s e_{F_p}=p^{-s}e_{F_p}.
\]

For \(\Re s>1\), it is trace class and

\[
  \det(I-\mathcal L_s)=\prod_p(1-p^{-s})=\zeta(s)^{-1},
  \qquad Z_{\otimes}(s)=\zeta(s).
\]

Repetitions give (p^r), and logarithmic differentiation gives the exact
von Mangoldt ledger.  A positive no-mixing theorem explains why the
recurrent core must split into atom loops: a cross-atom cycle creates a
strictly positive term at a composite with at least two prime factors, where
\(\Lambda\) vanishes.

The construction closes A0, A1, and A2 for one source-locked symbolic object.
It does **not** close A3: the transfer family is trace class only in the Euler
half-plane, its Fredholm determinant has the inverse orientation, and no
intrinsic Gamma factor, functional equation, Weil compression, or
critical-strip continuation has been derived.  A holomorphic trace-class
continuation through a nontrivial zeta zero is in fact impossible for this
ungraded operator.  The next same-family target is therefore an endogenous
graded symbolic transfer complex, not another fit of prime or zero data.

## Shareable paper and artifacts

- [`main.pdf`](main.pdf) — compiled shareable paper.
- `main.tex`, `sections/`, `figures/`, `math_commands.tex`, and
  `references.bib` — modular LaTeX source.
- [`SOURCE_LOCK.md`](SOURCE_LOCK.md) — the exact candidate tuple and forbidden
  moves.
- [`NARRATIVE_REPORT.md`](NARRATIVE_REPORT.md),
  [`PAPER_PLAN.md`](PAPER_PLAN.md), and
  [`LITERATURE_AUDIT.md`](LITERATURE_AUDIT.md) — claims, structure, and
  novelty boundary.
- [`EXPERIMENT_REPORT.md`](EXPERIMENT_REPORT.md), `code/`, `experiments/`, and
  `results/` — exact finite registry and adversarial controls.
- [`Route-A evaluation`](evaluations/route_a/SD-C07/20260812T220000Z.yaml) —
  frozen A0–A4 decision.
- [`PAPER_MANIFEST.sha256`](PAPER_MANIFEST.sha256) — paper-project checksums.

## Reproduce

From this paper-project root:

```bash
python code/exact_tensor_atom_experiment.py --output results
PYTHONDONTWRITEBYTECODE=1 \
  python -m unittest discover -s code -p 'test_*.py' -v
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

No Riemann zeros are read, fitted, or tested.  Route B remains locked.
