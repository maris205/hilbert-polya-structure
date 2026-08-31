# Narrative report

HCS-C266 resolves the main convention trap in skew Brownian motion: there is
not one interchangeable “interface density.”  The transition density with
respect to Lebesgue measure has a terminal-coordinate jump at zero whenever
`p!=1/2`.  The same semigroup, expressed against the speed measure, has a
symmetric kernel and hence a self-adjoint Markov realization.  The paper
derives both instead of silently switching reference measures.

The step beyond a kernel formula is a complete interface atlas.  Time
Laplace transformation gives the full resolvent.  A piecewise linear scale
function gives every two-sided hitting probability.  A two-by-two hyperbolic
transfer calculation retains the right and left discounted exit transforms,
and a piecewise quadratic Poisson problem gives the mean exit time.  The
excursion decomposition then closes the generalized arcsine occupation law,
including the ordinary Brownian and one-sided reflected limits.

The evidence independently checks 275 stored rows, 963 assertions, 133
symbolic identities, exact fresh byte replay, and 16/16 hostile mutations.
These finite rows detect implementation and convention errors; the
all-parameter result is established by the proof in `THEOREM_PACKAGE.md` and
the paper.

Route A stops cleanly.  Recurrence and speed-space self-adjointness do not
manufacture rational-prime primitive orbits or a target determinant.  The
source theorem remains complete while the target spectral claims remain
explicitly absent.
