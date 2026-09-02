# Narrative report

The chosen system takes a genuinely different dynamical step: it moves from
closed or nonlinear state-space models to a dissipative completely positive
semigroup on the full Bloch ball.  With ground/excited basis fixed, population
relaxation and excitation determine `Gamma1`; half of that rate plus pure
dephasing determines `Gamma2`.  The flow is affine in Bloch coordinates, yet
its entanglement-breaking transition is nonlinear in the physical rates.

For positive `Gamma1`, writing `p=gamma_up/Gamma1`,
`eta=exp(-Gamma1 t)`, and `q=2Gamma2/Gamma1`, the normalized Choi state's only
possibly negative partial-transpose eigenvalue lies in a two-by-two block.
The channel is entanglement breaking exactly when

`p(1-p)(1-eta)^2 >= eta^q`.

For `0<p<1` the left-minus-right side is strictly decreasing as a function of
`eta` from positive to negative; since `eta` decreases with time, there is one
finite threshold.  For `p=0` or `p=1`, the product vanishes and no finite time
works, although the infinite-time pure-state preparation channel is
entanglement breaking.  Pure dephasing behaves similarly: no finite-time EB,
but complete dephasing is the EB limit.

The exact trace-distance contraction coefficient is the largest singular
value of the affine map's linear part.  This gives a short recurrence
obstruction throughout `Gamma1>0`, while the dissipation-free boundary is
classified directly as periodic phase rotation or the identity.

This is a complete source-local theorem and a useful Route-A negative control.
Its finite Choi matrix is not a global arithmetic determinant; continuous time
is not a prime-log clock; and a dissipative GKSL generator is not a same-clock
self-adjoint spectral realization.
