# Narrative report

The harmonic drift confines the telegraph-driven particle to `[-v/mu,v/mu]`.  In the scaled coordinate, zero stationary flux forces the component imbalance to equal `y` times the marginal, reducing the coupled forward equations to a beta density.  Its recurrence gives all position and mixed orientation moments.

Time correlations close because the generator maps `(x,sigma)` through a two-by-two upper-triangular matrix.  The semigroup formula is stated for nonnegative lag; stationarity supplies negative lag by transpose.  At `mu=2lambda`, its two decay rates coalesce and the removable quotient becomes `t exp(-mu t)`; keeping this face explicit prevents a division-by-zero convention bug.

For polynomial observables the deeper effect is parity.  The involution `(x,sigma)->(-x,-sigma)` splits the generator into two bidiagonal chains.  At integer `k=2lambda/mu`, repeated values lie in the same chain precisely when `k` is odd, forcing one Jordan vector because every connecting coefficient is nonzero for `v>0`.  When `k` is even they lie in different simple-diagonal chains and remain semisimple.
