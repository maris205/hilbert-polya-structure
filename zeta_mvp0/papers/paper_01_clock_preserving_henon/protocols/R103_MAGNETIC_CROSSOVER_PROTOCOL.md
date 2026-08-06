# R103 — Magnetic Symmetry-Crossover Scan

## Frozen question

Is the R102 shift from an orthogonal-like to a unitary-like adjacent-spacing
ratio a persistent response to time-reversal breaking, or an isolated
finite-sample value at \(B=1\)?

## Design

- Fixed centered warp \((a,n)=(1.02,1)\).
- Fields \(B\in\{0,0.25,0.5,1,2,4\}\), fixed before execution.
- Reuse R101 \(h=0.0225\) spectra at \(B=0,1\); compute the other four on the
  same grid, wall, and 180-level window.
- Report mean adjacent ratio and unfolded variance after the same 25/15 edge
  discards.
- Treat the scan as a trajectory in symmetry space, not as an optimization:
  no field is selected by closeness to GUE and no zero data are loaded.

## Interpretation gate

Retain the magnetic extension if at least three nonzero fields have mean
spacing ratio above the converged \(B=0\) value and the response does not
collapse immediately back to the radial/Poisson control.  This is a
descriptive crossover gate, not an RMT goodness-of-fit test.
