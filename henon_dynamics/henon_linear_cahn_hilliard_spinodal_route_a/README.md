# HCS-C304: linear periodic Cahn--Hilliard spinodal atlas

This package proves one all-parameter theorem for
\(u_t=-\kappa\Delta^2u-\alpha\Delta u\) on the \(2\pi\)-periodic
\(d\)-torus, for every finite integer \(d\ge1\), every \(\kappa>0\), and
every real \(\alpha\). It classifies the analytic trace-class semigroup,
energy dissipation, unstable/neutral shell dimensions, fastest represented
shells and ties, actual-support asymptotics, recurrence, and the full
\(\kappa=0\) singular face.

The theorem is analytic. The 18 cases and 216 shell rows in the JSON archive
are deterministic regression receipts, not a finite-cutoff proof. In
particular, the fastest-shell proof uses an explicit global cutoff derived
from \(\alpha/\kappa\), never the receipt cutoff 12.

Primary entry points:

- `THEOREM_PACKAGE.md` — precise theorem and proof.
- `paper/main.pdf` — final short paper.
- `results/c304_ch_evidence.json` — self-hashed evidence.
- `code/c304_release_manifest.py` — complete release gate.
- `evaluations/route_a/HCS-C304/2026-09-03.yaml` — strict Route-A decision.

The frozen scope is `NO_BAD_EULER_OR_ROOT_NUMBER`. Route A is rejected with
tuple `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`; Route B is locked.
