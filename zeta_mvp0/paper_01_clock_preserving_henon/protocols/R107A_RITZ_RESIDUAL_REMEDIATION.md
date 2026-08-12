# R107A — Ritz-Residual Remediation

## Trigger

R107 passed every cross-stencil level and spacing gate, but failed its formal
maximum residual gate.  The fourth-order fine grids had median relative Ritz
residuals near \(5\times10^{-12}\), while one or more edge Ritz pairs reached
\(1.9\times10^{-6}\) at \(B=0\) and \(5.0\times10^{-6}\) at \(B=1\).

This remediation is frozen after observing that failure and before recomputing
any spectrum.

## Single allowed change

For every requested block of 180 modes:

- request 200 shift-invert Ritz pairs;
- tighten the ARPACK tolerance from \(2\times10^{-10}\) to
  \(10^{-12}\);
- sort the returned spectrum and retain only the lowest 180 pairs;
- compute residuals only after this fixed truncation.

The extra twenty edge pairs are numerical guard modes.  No physical parameter,
domain, grid spacing, analysis window, magnetic field, reference spectrum, or
acceptance threshold changes.

## Decision

R107A passes only if all original R107 gates pass and the retained 180 modes
have maximum relative residual below \(10^{-8}\) on both fine cells.

The original R107 failure remains recorded.  If R107A fails, the current
fourth-order cross-discretization result is not promoted.
