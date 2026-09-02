# Theorem package — PROVABLE AS STATED

In normalized synodic units let the primaries of masses `1-mu` and `mu` lie at `(-mu,0)` and `(1-mu,0)`, with `0<mu<=1/2`, and remove both collision points.  Set

`Omega=(x^2+y^2)/2+(1-mu)/r1+mu/r2`

and use `xddot-2 ydot=Omega_x`, `yddot+2 xdot=Omega_y`.

## Main theorem

There are exactly five equilibria.  Three are collinear, one in each interval `(-infinity,-mu)`, `(-mu,1-mu)`, `(1-mu,infinity)`.  At each, with `S=(1-mu)/r1^3+mu/r2^3>1`, the characteristic polynomial is

`lambda^4+(2-S)lambda^2+(1+S-2S^2)`,

and its negative constant term gives one real and one imaginary pair: saddle-times-center, hence unstable.

The other two are `L4,L5=(1/2-mu, plus_or_minus sqrt(3)/2)` and have

`lambda^4+lambda^2+(27/4)mu(1-mu)`.

Let `mu_R=(1-sqrt(23/27))/2`.  For `0<mu<mu_R` there are two distinct imaginary pairs and the linearized flow is bounded, including when their frequencies are resonant.  At `mu=mu_R`, each eigenvalue `plus_or_minus i/sqrt(2)` has algebraic multiplicity two but geometric multiplicity one at each of `L4` and `L5`.  The matrix is defective, its exponential has linearly growing solutions, and the equilibrium is **not linearly stable**.  For `mu_R<mu<=1/2` the spectrum is a Hamiltonian quartet with nonzero real parts.

`mu=0` is excluded: the rotating Kepler limit has a whole unit circle of equilibria.  Collision points are singular, not equilibria.  The theorem is linear only; it makes no claim about nonlinear resonance consequences, bifurcations, or KAM stability.

Finite evidence is regression only.  Route tuple `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`, Route B false.
