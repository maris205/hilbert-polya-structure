# Exact-\(U_c\) polar conformal-ratio stage

Stage ID: `LOG-0001-CONFORMAL-RATIO`.

HP-Dynamics research commit:
`80107bc8ec2bcb4b5d0dd7a30447c5bc2d075320`.

This standalone stage keeps the exact-\(U_c\) polar map, intrinsic roof,
matching space, frozen stadiums, two-stream nuclear expansion, and canonical
Fredholm determinant unchanged.  It replaces the previously implicit
Riemann-map restriction constants by the exact common upper bound

\[
r_L=r_R\le
\tanh\!\left(\frac{500\pi+\log4}{2}\right)=:r_*<1.
\]

A 4096-bit outward Arb certificate resolves

\[
1-r_*=3.2418512480136249798\ldots\times10^{-683}
\]

without rounding \(r_*\) to one.  Inserting the bound into the inherited
two-stream coefficient theorem gives the fully numerical same-determinant
envelope

\[
|D_{\rm pol}(s)|\le
\exp\!\left(3.45\times10^{689}
+4.20\times10^{682}(1+|s|)^2\right).
\]

The constants are deliberately coarse proof constants for a long, thin
stadium.  The stage does not compute a conformal map or determinant root,
prove exact order or lower growth, compare against an external divisor, or
open Route B.

## Contents

- `PAPER_PLAN.md`: fixed claim--evidence map and manuscript outline.
- `NARRATIVE_REPORT.md`: compact theorem narrative and boundary.
- `source_lock.yaml` and `route_a_evaluation.yaml`: stage decision records.
- `results/`: formal theorem note and source hashes.
- `src/`, `tests/`, and `artifacts/`: compact reproduction mirror.
- `experiments/`, `configs/`, `evaluations/`, and `formal/`: compatibility
  layout for byte-identical reproduction.
- `paper/`: modular standalone manuscript and compiled PDF.

## Reproduction

```bash
PYTHONPATH=. python3 tests/test_log_0001_conformal_ratio.py
python3 experiments/log_0001_conformal_ratio.py \
  --quiet \
  --output artifacts/log_0001_conformal_ratio/conformal_ratio_certificate.json
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
