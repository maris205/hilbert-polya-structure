# Research question

**Can one close the complete all-parameter renewal and first-passage theorem
for Brownian motion reset to its start, while separating the stationary free
process from the killed search and preserving the Route-A arithmetic
firewall?**

The answer is yes at the source-theorem level.  The renewal decomposition gives
an explicit propagator and Laplace laws; differentiation gives every finite
moment; and a dimensionless calculus argument gives a unique nonzero optimum.
The answer is deliberately negative for arithmetic promotion: the model has
no prime carrier or periodic-orbit clock.

## Frozen assumptions

* `D>0`, `r>0`, and target distance `a>0` are fixed; `X_0=0` and every reset
  returns to `0`.
* The free process is considered on all of `R` before killing.  Its invariant
  density is stated only in that realization.
* The search process is killed on first hitting `a`; its survival mass is
  sub-probability and no stationary density is asserted.
* Laplace variable `s>=0` and physical elapsed time are used; no fitted or
  logarithmic clock is introduced.
* No target zero/prime tables or arithmetic weights enter any calculation.

## Falsifiers

Release stops if the erfc propagator disagrees with independent quadrature,
the stationary density fails normalization, the renewal identity or
first-passage transform fails, the `s=0` survival limit disagrees with the
MFPT, the optimality root is not the unique positive root, any boundary row is
misclassified, or a repaired-hash/stale-hash/unknown-key mutation is accepted.
