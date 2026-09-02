# C311 hostile audit

The suite flips the Hopf side, changes equilibrium coordinates, Jacobian
entries, defective-node boundaries, real or imaginary `G21`, `l1`, the radial
coefficient, and individual eigenvalue probes.  It also attempts `A1_PASS`,
Route-B activation, and a root-number claim.  Every semantic attack receives
a new correct payload hash before submission.

Duplicate/nonfinite/top-level JSON failures and duplicate/anchored/scope-
escalated YAML are also rejected.  The suite is designed specifically to
catch a numerically correct Hopf sign paired with the wrong normalization or
parameter side.
