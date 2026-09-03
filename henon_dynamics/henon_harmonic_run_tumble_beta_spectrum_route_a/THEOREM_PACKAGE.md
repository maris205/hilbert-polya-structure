# Theorem package

Let `alpha=lambda/mu`, `a=v/mu`, and `y=x/a`.  For `mu,v,lambda>0`, the unique stationary marginal density in `y` is

`p(y)=Gamma(alpha+1/2)/(sqrt(pi)Gamma(alpha)) (1-y^2)^(alpha-1)`,

with joint component densities `p_plus=(1+y)p/2`, `p_minus=(1-y)p/2`.

For every `n>=0`,

- `E[x^(2n)]=a^(2n)(1/2)_n/(alpha+1/2)_n`;
- odd position moments vanish;
- `E[sigma x^(2n)]=0`;
- `E[sigma x^(2n+1)]=a^(2n+1)(1/2)_(n+1)/(alpha+1/2)_(n+1)`.

For `t>=0`, writing `Z=(x,sigma)^T`, `R(t)=E[Z_t Z_0^T]=exp(A t)Sigma`, where
`A=[[-mu,v],[0,-2lambda]]` and
`Sigma=[[v^2/(mu(mu+2lambda)),v/(mu+2lambda)],[v/(mu+2lambda),1]]`.
In particular the `xx` entry has its exact removable limit
`v^2(1+mu t)e^(-mu t)/(2mu^2)` at `mu=2lambda`.
Stationarity fixes negative lag by `R(-t)=R(t)^T`.

Every `P_N=span{x^n,sigma x^n:0<=n<=N}` is invariant.  Its diagonal ladders are `-n mu` and `-n mu-2lambda`.  If `v>0` and `2lambda/mu=k` is integral, every in-filter repetition is a size-two Jordan block for odd `k`, but is semisimple for even `k`.  Otherwise the ladders are disjoint.  This is a theorem about all finite filters, not the full `L2` spectrum.

On the boundary `v=0, lambda>0`, the stationary law is `delta_0` tensored with uniform orientations and all repeated polynomial eigenvalues are semisimple because the couplings vanish.  At `v=lambda=0`, any orientation mixture over `delta_0` is stationary.
