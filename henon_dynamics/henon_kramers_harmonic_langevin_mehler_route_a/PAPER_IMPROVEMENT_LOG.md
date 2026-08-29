# Paper improvement log — HCS-C237

## Round 0

Initial theorem draft: all three matrix regimes, Gaussian covariance, Gibbs
law, Kalman determinant and Route-A boundary.

## Round 1

Added explicit \(\gamma=0\) and \(\omega=0\) faces, stationary covariance
entry formulas, and a finite-time Lyapunov derivation.  Added fixed-control
counts and citation roles.

## Round 2

Reworded the critical optimum as a drift spectral-abscissa/asymptotic
exponent.  Added the \(t e^{-\omega t}\) Jordan prefactor warning and removed
any implication of a sharp uniform pure-exponential norm bound.  Added the
independent checker (411 assertions), SymPy (26 identities), replay and
32/32 mutation results.  The checker now independently locks every boundary
row's parameter and semantic labels, including the under/critical/over and
zero-damping rows.  These are internal reproducibility checks, not external
peer review.
