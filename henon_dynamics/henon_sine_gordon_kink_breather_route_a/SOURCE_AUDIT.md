# Source and scope audit

* Frozen source commit: `0ebc633706bc34b8b915a44749423486fd4cd243`.
* Evaluator authority: `flow_systems/skills/route-a-evaluator.md` v0.2.0,
  SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`.
* Equation: $u_{tt}-u_{xx}+\sin u=0$ on the real line, with
  $V(u)=1-\cos u$ and vacua $2\pi k$.  Kink rows use canonical $k=0$;
  the theorem retains every integer vacuum layer.
* Momentum convention (fixed throughout):
  $P=-\int_{\mathbb R}u_tu_x\,dx$.
* Allowed data: the displayed PDE, exact profile identities, rational
  regression probes, and independent symbolic/numeric checks.
* Forbidden data: target primes or zeros, arithmetic local data, Euler factors,
  root numbers, automorphy, target divisors, and Hilbert--Pólya operators.

The sole contextual citation is McLaughlin--Scott (1978), *Perturbation
analysis of fluxon dynamics*, Physical Review A **18(4)**, 1652--1680,
DOI `10.1103/PhysRevA.18.1652`.  It is a source pointer, not a priority or
completeness claim.  The package is distinct from C231 Allen--Cahn/Fisher
fronts: this is a Lorentz-invariant second-order wave equation with a kink
mass shell, breathers, and a rest-kink Hamiltonian Hessian.
