# COPRIME-0001 countable trace stage

Stage ID: `COPRIME-0001-COUNTABLE-TRACE`.

This self-contained paper subproject freezes a countable coprime renewal
suspension and proves its first Route-A theorem edge. The state labels are
integers `n>=2`, adjacent labels must be coprime, the roof is `log(n)`, and
the symmetrized transfer kernel is

```text
K_s(m,n)=1_{gcd(m,n)=1}(mn)^(-s/2).
```

On counting-measure `ell^2`, the kernel is a holomorphic trace-class family
for `Re(s)>1`. The half-plane is exact for this operator realization: its
`e_2` column is not square summable for `Re(s)<=1`. Trace powers equal the
exact cyclic coprime ledger, and the project certifies primitive/repetition
identities through power six using exact rational arithmetic.

The result does not provide a prime-to-orbit correspondence, von-Mangoldt
weights, analytic continuation, a completed-xi divisor, quantization, Route B,
Hilbert--Pólya, or RH.

## Contents

- `PAPER_PLAN.md`: claim--evidence map and manuscript outline.
- `NARRATIVE_REPORT.md`: compact theorem narrative and strict boundary.
- `source_lock.yaml` and `route_a_evaluation.yaml`: top-level shareable copies.
- `configs/`, `evaluations/`, `formal/`: repository-compatible provenance.
- `experiments/` and `tests/`: self-contained exact certificate and regression.
- `artifacts/`: canonical and convenience certificate copies.
- `paper/`: modular LaTeX manuscript and compiled PDF.
- `results/ARTIFACT_HASHES.sha256`: frozen hashes.

## Reproduction

From this project directory:

```bash
python3 -m unittest -v tests/test_coprime_0001_countable_trace.py
python3 experiments/coprime_0001_countable_trace.py --quiet \
  --output artifacts/coprime_0001/countable_trace_certificate.json
sha256sum -c results/ARTIFACT_HASHES.sha256
```

Build the paper with:

```bash
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

Validated environment: Python `3.12.3`; the certificate uses only the Python
standard library plus PyYAML in the regression test.

HP-Dynamics source commit: `a1d4550`.

