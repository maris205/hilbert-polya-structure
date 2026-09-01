# Results

The deterministic receipt stores 438 regression cells:

- 96 conductor-shell spectrum cells;
- 36 finite-quotient DFT/filtration comparisons;
- 72 heat-trace cells;
- 36 convergent-half-plane zeta cells;
- 84 pole-location/residue cells;
- 72 exact counting-staircase cells;
- 27 Schatten threshold cells;
- 15 composite-branching control cells.

The largest quotient order is 4096.  Every DFT/filtration discrepancy is below
\(2\times10^{-14}\) after normalization by the top eigenvalue.  The independent
checker performs 1507 semantic assertions.  SymPy performs 102 exact checks.
Fresh-path replay is byte exact, and all 17 hostile mutations are rejected.

These results confirm the convention and endpoints encoded in the theorem.
They are not used as a substitute for the quantified proofs.  The release
gate separately locks the exact Example 5.1 owner attribution and the
zero-originality boundary for the positive spectral/zeta core.
