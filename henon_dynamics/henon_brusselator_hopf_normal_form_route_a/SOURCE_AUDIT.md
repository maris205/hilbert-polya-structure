# C311 source and claim audit

The frozen system is the dimensionless Brusselator

`xdot=A-(B+1)x+x^2y`, `ydot=Bx-x^2y`, with `A>0`, `B>=0`.

Prigogine and Lefever's 1968 paper
[`10.1063/1.1668896`](https://doi.org/10.1063/1.1668896) is the historical
model owner.  Kuznetsov's bifurcation text
[`10.1007/978-1-4757-3978-7`](https://doi.org/10.1007/978-1-4757-3978-7)
fixes the multilinear Hopf convention.  Neither citation is used to claim
literature novelty.

The package independently derives the equilibrium, complete linear chamber,
normalized eigenvectors, multilinear tensors, complex `G21`, Kuznetsov
`l1`, physical radial coefficient, and leading amplitude/frequency.  It
proves only the local Hopf cycle branch; no global uniqueness or global
attractor theorem for periodic orbits is asserted.

The source cycle earns `A1_WEAK`, not a prime-indexed ledger.  No target
arithmetic datum, Euler factor, root number, automorphy, divisor law,
functional equation, zero match, or Hilbert--Pólya operator is asserted.
