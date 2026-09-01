# HCS-C277 — Caputo fractional Dirichlet heat flow

This package closes the solution family of the Caputo subdiffusion equation on
`(0,pi)` in its exact sine basis.  For `0<beta<1`, it proves inverse-stable
subordination, positivity and contraction, but also the decisive category and
regularity boundaries: the family is not a semigroup, and within the declared
nonnegative smoothing domain it gains exactly two spatial derivatives at each
fixed positive time and belongs to `S_p` exactly
for `p>1/2`.  Its scaled long-time limit is the Dirichlet resolvent.  The
classical `beta=1` heat face instead has all-order smoothing and exponential
decay.

Run the six commands in [`code/README.md`](code/README.md).  The final paper is
[`paper/main.pdf`](paper/main.pdf).  Route A is rejected, Route B is disabled,
and scope is `NO_BAD_EULER_OR_ROOT_NUMBER`.
