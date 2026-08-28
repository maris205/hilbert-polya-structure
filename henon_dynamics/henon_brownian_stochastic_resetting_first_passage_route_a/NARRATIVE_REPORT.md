# Narrative report

HCS-C214 freezes a nonlocal continuous stochastic subtype: Brownian motion
whose Poisson clock returns it to its starting point.  The package deliberately
separates two questions that are often conflated.  The free process on the
line has a normalized Laplace stationary density.  The search process is
killed at a positive target and therefore has only a survival mass, not that
stationary law.

The main theorem is a complete renewal closure.  Conditioning on the last
reset gives the propagator and an erfc form; conditioning on the first reset
gives the first-passage and survival transforms.  The `s=0` transform limit
recovers the MFPT, and exact Laplace identities state both moment conventions
for every `n>=0`: `(-1)^n F^(n)(0)=E[T^n]` and
`(-1)^n S^(n)(0)=E[T^(n+1)]/(n+1)`; all moments are finite for positive
parameters.  Dimensionless calculus reduces the reset
optimization to one universal positive root.

The checker independently integrates the singular-looking renewal integral,
normalizes the free density, tests every transform row, and audits all
boundaries.  SymPy verifies the structural identities.  Replay, hostile
mutations, and deterministic PDF builds close reproducibility.  The model is
source-attributed, not claimed novel, and has no arithmetic Route-A payload.
