# Quantum Window Correction Record

## Scope

The raw R100--R104 NPZ spectra are unchanged.  During the final manuscript
audit, the stored level-change aggregates in the historical summary JSON
files were found to use an edge aggregation inconsistent with the declared
25/15 discard.  Spacing statistics already used the intended 140-level
window.

`scripts/audit_quantum_windows.py` version 2 recomputes every level, gap,
and ratio comparison directly from the archived spectra through the shared
`spectral_window()` function.  Its machine-readable output is
`results/QUANTUM_WINDOW_AUDIT.json`.  The historical summaries are retained
as provenance and are not silently rewritten.

## Corrected median level changes

| Run | Cells in fixed order | Unified-window medians |
|---|---|---|
| R100, \(0.04\to0.03\) | radial; \(a=1.02,B=0,1\); \(a=6,B=0,1\) | 1.195%, 1.233%, 1.215%, 1.667%, 1.655% |
| R101, \(0.03\to0.0225\) | same order | 0.661%, 0.681%, 0.677%, 0.930%, 0.926% |
| R102, \(0.0225\to0.0175\) | \(a=1.02,B=0,1\) | 0.347%, 0.346% |
| R104, \(0.03\to0.0225\) | \(B=0.25,0.5,2,4\) | 0.679%, 0.679%, 0.677%, 0.685% |

## Decision impact

There is no gate reversal:

- every R100 cell remains above the 1% median gate;
- every R101, R102, and R104 cell remains below it;
- adjacent-ratio, CDF, unfolding, residual, and cross-stencil conclusions
  are unchanged.

The manuscript and generated figures use the version-2 audit values.
