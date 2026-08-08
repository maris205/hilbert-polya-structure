# Exact-\(U_c\) polar nuclear Fredholm stage

Stage ID: `LOG-0001-NUCLEAR-FREDHOLM`.

This shareable stage records the analytic determinant result for the frozen
exact-\(U_c\) polar Logistic transfer family. The same-object matching-space
family is proved order-zero nuclear, its canonical Fredholm determinant is
entire, and its based-word trace formula retains signed inverse derivatives.

The result is not a Riemann-spectrum claim. In particular it contains no
prime/zero data, Fredholm-zero calculation, completed-\(\xi\) identity,
functional equation, divisor-count theorem, quantization, Route-B result, or
RH claim. The analytic Route-A tuple is
`(A1_WEAK, A2_ANALYTIC_DETERMINANT, A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FAIL)`;
the Riemann-target tuple remains `(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)`.

## Contents

- `source_lock.yaml` and `route_a_evaluation.yaml`: phase decision record.
- `results/`: formal theorem note.
- `src/`, `tests/`, and `artifacts/`: requested compact mirror.
- `experiments/`, `configs/`, `evaluations/`, `formal/`: compatibility mirror
  used to run the copied regression exactly in this standalone project.
- `paper/`: complete modular generic-article manuscript.

## Reproduction

```bash
PYTHONPATH=. python3 tests/test_log_0001_nuclear_fredholm.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The regression enumerates all 510 based words with lengths one through eight;
it is an implementation check, not a numerical spectral experiment.
