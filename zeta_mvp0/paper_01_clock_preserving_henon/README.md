# Paper 01 — Clock-preserving Hénon operators

This self-contained package now lives directly at
`zeta_mvp0/paper_01_clock_preserving_henon/`; it was moved intact from the
former `zeta_mvp0/papers/` container on 2026-08-12.  Relative paths inside
the package are unchanged.

Legacy project identifier: **Paper 7**.  Repository stage identifier:
**paper_01**.

This directory freezes the analytic-v3 manuscript and the compact evidence
package for the Hénon-warped Schrödinger family

\[
 \mathcal H_{a,n}=-\frac12\Delta
 +2\pi\exp\!\left(\pi|H_a^n(q)|^2\right).
\]

The area-preserving polynomial warp leaves the classical two-term counting
clock unchanged.  The paper proves the corresponding operator realization,
bracketing estimates, strict ground-state ordering, and relative heat
asymptotics.  It reports controlled classical and spectral numerics, but does
not claim an endogenous rational-prime trace, a zeta-zero spectrum, the
Hilbert--Pólya conjecture, or RH.

The authoritative manuscript artifact is
`artifacts/paper_01_analytic_v3_round2_final.pdf`; historical pre-v3 PDFs are
not alternative final versions.

## Layout

- `manuscript/`: LaTeX source;
- `figures/`: figure sources and rendered paper figures;
- `src/` and `scripts/`: frozen Python package and experiment scripts;
- `tests/`: paper-specific regression tests;
- `protocols/`: experiment and theorem-development records;
- `data/`: accepted compact result archives;
- `reviews/`: manuscript reviews and improvement log;
- `artifacts/`: final PDF and hashes.

## Reproduction

From this directory, install the local package and run:

```bash
python -m pip install -e .
pytest -q tests
cd manuscript && ./compile_paper.sh
```

The exact dependency versions used historically are recorded in the
manuscript status and result manifests.  A fresh environment may require
version-compatible adjustments that must not be written back into the frozen
artifact without a new release record.
