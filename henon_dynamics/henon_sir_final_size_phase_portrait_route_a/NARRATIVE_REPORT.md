# Narrative report

The closed SIR equations form a genuinely nonlinear but completely organized
two-dimensional flow.  After the correct physical scaling, every parameter
choice shares one phase portrait.  The conserved curve controls the peak and
the final state, while the removed population supplies a strict Lyapunov-like
coordinate that excludes recurrence.

The main subtlety is not computing a Lambert W value; it is choosing the right
branch and stating its hypothesis.  Positive infection drives susceptible mass
down to the lower intersection, so `W_0` owns the forward final state.
`W_{-1}` is the upper intersection.  When infection starts at exactly zero,
the trajectory is already fixed, and a supercritical susceptible value stays
on that upper branch.  Treating this boundary as a limit without qualification
would give a false final state.

C198 closes all these pieces in one theorem: scaling, invariant, global
positivity, peak, branch, quadrature, sensitivity, equilibria, stability and
no recurrence.  Its executable certificate is intentionally branch-adversarial:
one path evaluates Lambert W and another solves the two monotone equations
without it.

This mathematical completeness does not help Route A.  Strict monotonicity
removes a primitive-periodic-orbit ledger, and neither the biological rates nor
Lambert function provide prime arithmetic or a target determinant.  The
correct output is a strong dynamical classification and an equally strong
candidate rejection.  Nothing in the package is a real-world epidemic
prediction or recommendation.
