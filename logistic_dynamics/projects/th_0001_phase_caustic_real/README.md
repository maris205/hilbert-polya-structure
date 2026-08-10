# TH-0001 on-shell real caustic audit

This self-contained stage records the exact on-shell follow-up to the frozen
TH-0001 three-kick Fourier-integral audit.  The object is the ordered product
of the three factors with parameters (1/2,3/2,5/2), not a newly fitted map.

The audit establishes a narrow geometric result:

1. the internal caustic (15q_1q_2=1) is attained by every real stationary
   branch with (q_1\ne0);
2. the endpoint projection Jacobian is exactly minus the internal Hessian;
3. (t=q_1=1) gives an exact rational canonical trajectory whose Hessian has
   rank one and whose null-direction cubic derivative is (132\ne0).

This strengthens obstruction `OBR-011`: a global single nondegenerate phase
chart is not available on the real stationary relation.  It does not build a
multi-chart Maslov ledger and does not define a determinant, spectrum, trace
formula, Route-B operator, or Riemann-Hypothesis result.

## Contents

- `source_lock.yaml` and `route_a_evaluation.yaml`: convenient top-level copies;
- `configs/`, `evaluations/`, `formal/`: repository-compatible provenance;
- `experiments/` and `src/`: the exact SymPy rational certificate generator;
- `tests/`: deterministic regression and source-hash checks;
- `artifacts/`: canonical and convenience certificate copies;
- `paper/`: modular LaTeX manuscript and compiled PDF;
- `results/ARTIFACT_HASHES.sha256`: frozen reproducibility hashes.

The historical parent Route-A evaluation referenced by the generator is kept
under `evaluations/route_a/TH-0001/20260806T053410Z.yaml` so a fresh clone can
reproduce the provenance without access to the main research repository.

## Reproduction

Run from this project directory:

```bash
PYTHONPATH=. python3 experiments/th_0001_phase_caustic_real.py --quiet \
  --output artifacts/th_0001/phase_caustic_real_audit.json
PYTHONPATH=. python3 -m unittest -v tests/test_th_0001_phase_caustic_real.py
sha256sum -c results/ARTIFACT_HASHES.sha256
```

Build the manuscript with two deterministic passes:

```bash
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Source freeze: HP-Dynamics commit `1b8cc8e` (`research: certify TH-0001
on-shell caustic`).

## Route-A checkpoint

```text
analytic tuple:       (A1_WEAK, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)
Riemann-target tuple:  (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
scoped verdict:        GO_WITH_LIMITATIONS
Route B:               not authorized
```

The smallest next task is to stop this incidence audit.  Reopening requires a
new source lock for explicit phase/Maslov charts and transition rules, or a
structurally different candidate; spectrum and zero calculations remain out of
scope.
