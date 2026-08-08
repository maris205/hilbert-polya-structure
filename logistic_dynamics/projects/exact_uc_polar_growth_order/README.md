# Exact-\(U_c\) polar Fredholm growth-order stage

Stage ID: `LOG-0001-GROWTH-ORDER`.

HP-Dynamics source commit:
`ec00bcb` (`research: prove LOG-0001 quadratic growth bound`).

This standalone stage studies the same canonical determinant

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_{s,B})
\]

constructed for the frozen exact-\(U_c\) polar Logistic transfer family. It
proves three target-free upper statements:

1. `D_pol` is an entire function of classical order at most two;
2. its zeros satisfy an `O(R^2)` disk-count upper bound and therefore an
   `O(T^2)` upper bound in every fixed real strip;
3. it has no zeros in the explicit half-plane
   `Re(s) > log(2)/log(4/U_c^2)`.

The theorem does not identify the exact order, give a sharp or lower divisor
asymptotic, compute determinant roots, or compare the divisor with any
external target. The transfer operator, roof, matching space, complex
domains, and determinant convention are unchanged from the parent
nuclear-Fredholm stage.

## Contents

- `PAPER_PLAN.md`: claim--evidence map and fixed manuscript outline.
- `NARRATIVE_REPORT.md`: compact mathematical narrative and claim boundary.
- `source_lock.yaml` and `route_a_evaluation.yaml`: compact phase decision
  record.
- `results/`: formal theorem note and source hashes.
- `src/`, `tests/`, and `artifacts/`: compact reproduction mirror.
- `experiments/`, `configs/`, `evaluations/`, and `formal/`: compatibility
  layout used to execute the copied regression without path changes.
- `paper/`: modular generic-article manuscript and compiled PDF.

The target-free certificate checks the exact roof lower bound, the zero-free
threshold, the safe line `Re(s)=2`, the inherited `||ell||<0.824` envelope,
and every two-stream allocation through `q=24`. It does not evaluate the
Fredholm determinant or search for roots.

## Manuscript build

```bash
PYTHONPATH=. python3 tests/test_log_0001_growth_order.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
