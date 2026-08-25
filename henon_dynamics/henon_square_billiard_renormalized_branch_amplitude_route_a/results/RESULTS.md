# C162 results

- Full-trace normalized boundary limit: **PROVED** for every `N>=1`.
- Positive-time phase: `exp(i*pi/4)`; negative time is its conjugate.
- Coincident simple subtraction poles: **PROVED** to vanish after normalization.
- Exact replay through `N=800`: 270 occupied shells and 2,520 nonzero lattice
  vectors, including 28 shell times with coincident simple poles.
- Independent validation: 1,988 checker assertions, nine exact SymPy checks,
  23 repaired-hash mutation rejections, and one stale-hash rejection.
- Local 60-decimal convergence rows at `N=1,2,5,13,65` are regression
  sentinels only.
