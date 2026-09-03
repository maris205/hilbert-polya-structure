# C320 results

The deterministic evidence has SHA-256
`d80d64c1a0d1ce9dcc9ca9148b0cf140bef5288c09b35202e704d3385a976098`
and internal payload SHA-256
`a20ea9c547a905c103cfafc9526e16ecd2d18799fe748de65f8939343234c8b0`.
It contains 129 exact formal rows through `Q^128`, six high-precision
theta/ODE/`S,T` rows, 18 rational reciprocal-collision rows, and 15
coordinate-axis equilibrium rows: 1,705 audited scalar leaves.

The exact rows close both the three cyclic ODE residuals and
`X1+X2+X3=-E2/2`, whose even-power coefficients are `12*sigma1(n)`.
The independent checker reconstructs the theta coefficients from Jacobi
products instead of the producer's series division and recomputes all
100-digit analytic samples.
