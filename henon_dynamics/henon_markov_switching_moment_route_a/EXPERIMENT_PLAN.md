# Experiment plan — C117

1. Freeze both Hénon maps, the row-stochastic transition matrix, and the
   transition/application chronology.
2. Derive `B_0,B_1`, their determinants, and the stationary distribution.
3. Build the 4-by-4 conditional first-moment operator.
4. Derive the symmetric-square action on `(x^2,xy,y^2)` and build the 6-by-6
   conditional second-moment operator.
5. Compute exact traces through power six and both full determinant
   polynomials.
6. Compare stationary-average second moments with the symmetric square of the
   stationary-average Jacobian.
7. Run an independent checker, Newton/SymPy cross-check, canonical replay, and
   hostile mutation audit before compiling the paper.
