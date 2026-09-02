# Theorem package — PROVABLE AS STATED

Let `H^2_kappa` be the complete simply connected oriented surface of Gaussian curvature `-kappa^2`, with `kappa>0`.  Let `gamma` solve `D_t dot(gamma)=b J dot(gamma)` and have constant speed `v>0`.

## Main theorem

Every maximal solution is complete and, up to orientation-preserving isometry and time translation, is exactly one of:

1. `|b|>kappa v`: a hyperbolic circle.  It has primitive period `T=2 pi/sqrt(b^2-kappa^2 v^2)`.
2. `|b|=kappa v`: a horocycle.  It is nonclosed; the ambient Lorentz generator is nonzero nilpotent with `A^3=0` and `A^2!=0`.
3. `0<|b|<kappa v`: an unbounded hypercycle.
4. `b=0`: a geodesic.

The sign of `b` reverses orientation and changes no unoriented shape or period.  For `v=0` the solutions are stationary and the unit-frame proof is not invoked.  At `kappa=0`, treated as a limit rather than part of the hyperbolic theorem, nonzero field gives a Euclidean circle of period `2 pi/|b|`, while zero field gives a line.

## Proof spine

Constant speed gives geodesic curvature `b/v`.  In the hyperboloid model, let `F=(e0,T,N)=(kappa X,T,JT)` mean the matrix with these vectors as columns.  It obeys the right-action ODE `F'=F A` with

```text
A = [[0,kappa*v,0],[kappa*v,0,-b],[0,b,0]],
A^T eta+eta A=0,
A^3=(kappa^2*v^2-b^2)A.
```

The three Lorentz conjugacy types yield the complete geometric classification.  In the circle chamber, `kappa coth(kappa rho)=|b|/v`; hyperbolic circumference divided by speed gives the period.  The exponential frame solution proves global completeness and exhausts all initial data.

For circle cells, the basepoint exponential has independent sine and `1-cosine` components, so it returns exactly when `sqrt(b^2-kappa^2 v^2)t` is in `2 pi Z`; this locks primitivity at the position level.  At equality, `exp(tA)e0=e0+tAe0+t^2 A^2e0/2` has tangent component `kappa v t`, so the base point cannot return at nonzero time.

Finite evidence is regression evidence only.  Route-A tuple: `A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT`; overall `ROUTE_A_REJECTED`.  A magnetic quantum Hamiltonian is only a formal hint here; no self-adjoint domain or quantum spectrum is constructed.
