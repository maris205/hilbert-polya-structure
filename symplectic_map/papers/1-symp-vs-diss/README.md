# 1-symp-vs-diss

This project tested a deliberately narrow question: can the symbolic information
attributed to the critical logistic map survive a smooth passage to an
area-preserving Hénon map, without using prime tables or Riemann zeros to define
or tune the dynamics?

The frozen family is

\[
H_{a,\rho}(x,y)=(1-a x^2-\rho y,x),\qquad 0\leq\rho\leq1.
\]

At \(\rho=0\), the first coordinate follows the quadratic map. At
\(\rho=1\), the map is area preserving. Intermediate values are matched,
conformally symplectic controls. The primary inherited parameter is
\(a=1.5436890126920763\); it is frozen from the earlier logistic work and is
not selected using primes, orbit multipliers, or zeros.

## Evidence boundary

- The critical-point obstruction for a smooth projection-preserving symplectic
  lift is an elementary theorem and a known phenomenon in weak-noise canonical
  extensions; it is not claimed as a new theorem by itself.
- Periodic-orbit ledgers, monodromy data, continuation results, and arithmetic
  controls are numerical until explicitly certified.
- Generic chaos, orbit abundance, or GUE/CUE-like statistics are not arithmetic
  evidence.
- Riemann-zero data are forbidden throughout this project.

## Result

The sealed test returned `A0_SHADOW_FAIL_CARRIER_UNAVAILABLE`. At \(\rho=1\),
finite exposure was 0.011724, no trajectory survived the full horizon, only 9,988
return gaps were available, and conditional pre-escape polarity was \(-0.70665\)
(95% cluster-bootstrap CI \([-0.71625,-0.69679]\)). All four neighbor controls
failed the specificity gate. The project therefore stops before any prime-
multiplier, Riemann-targeted zeta, or quantization experiment.

## Reproduction

From this directory:

```bash
cd code
PYTHONPATH=. pytest -q
python scripts/run_ledger.py --preset positive-control --max-period 10 \
  --output /tmp/ledger_positive_a6_rho1_n10_reproduction.json
python scripts/audit_ledger.py \
  /tmp/ledger_positive_a6_rho1_n10_reproduction.json \
  --output /tmp/ledger_positive_a6_rho1_n10_audit80_reproduction.json \
  --digits 80
cd ..
python code/scripts/analyze_transport.py --split test \
  --output-stem transport_test_analysis_reproduction_YYYYMMDD
```

The first command runs exact-identity and protocol tests. The ledger commands
reproduce the full-shift software control and its explicitly non-interval 80-digit
audit. The final command recomputes cluster-aware comparisons from already sealed
raw test artifacts. Re-running the test trajectory generator is excluded from the
standard reproduction path; its single-use access and hashes are recorded in
`experiments/test_access_log.md`.

## Paper

- Source: `paper/manuscript.tex`
- References: `paper/references.bib`
- Compiled article: `paper/paper.pdf` (13 pages)

The final build has embedded fonts, resolved references and citations, and no
remaining LaTeX overfull-box warnings.

## Layout

- `paper/`: manuscript and figures
- `code/`: reusable implementation, scripts, and tests
- `experiments/`: immutable source lock and run records
- `results/`: machine-readable outputs
- `notes/`: derivations, proof obligations, reviews, and literature audit
