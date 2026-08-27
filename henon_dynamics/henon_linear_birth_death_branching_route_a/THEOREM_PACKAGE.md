# Theorem package

Let `Z_t` be the linear birth--death branching chain with rates
`lambda,mu>=0`, initial population `z in N_0`, and `r=lambda-mu`.

## Finite-time theorem

For one ancestor, the PGF solves

\[
\partial_tF=(F-1)(\lambda F-\mu),\qquad F_0(s)=s.
\]

If `r!=0`, set `delta=exp(-rt)` and obtain

\[
F_t(s)=\frac{\mu(1-s)-\delta(\mu-\lambda s)}
{\lambda(1-s)-\delta(\mu-\lambda s)}.
\]

If `r=0`, set `tau=lambda*t` and obtain

\[
F_t(s)=\frac{\tau+(1-\tau)s}{1+\tau-\tau s}.
\]

These M\"obius maps satisfy `F_t o F_u=F_(t+u)`: `delta` multiplies and
`tau` adds.

Define

\[
p_0=\frac{\mu(1-\delta)}{\lambda-\mu\delta},\qquad
\beta=\frac{\lambda(1-\delta)}{\lambda-\mu\delta}
\]

off criticality, and `p_0=beta=tau/(1+tau)` at criticality. Then

\[
P_1(Z_t=0)=p_0,\qquad
P_1(Z_t=n)=(1-p_0)(1-\beta)\beta^{n-1},\quad n\ge1.
\]

For arbitrary `z`, the number `K` of ancestral lines alive at time `t` is
`Binomial(z,1-p_0)`. Given `K=k`, the total is a sum of `k` positive geometric
variables, hence

\[
P_z(Z_t=n)=\sum_{k=1}^{\min(z,n)}\binom zk p_0^{z-k}(1-p_0)^k
\binom{n-1}{k-1}(1-\beta)^k\beta^{n-k},\quad n\ge1,
\]

and `P_z(Z_t=0)=p_0^z`. The all-parameter answer is therefore a
survivor-binomial mixture, not uniformly one negative-binomial law. Special
parameters can collapse the mixture; the paper states this exception rather
than making an overstrong pointwise prohibition.

The moments are

\[
E_zZ_t=ze^{rt},\qquad
\operatorname{Var}_zZ_t=
z\frac{\lambda+\mu}{r}e^{rt}(e^{rt}-1)
\]

for `r!=0`, and `Var_z Z_t=2*z*lambda*t` at criticality.

## Long-time theorem

For every fixed `z>=1`:

1. If `lambda<mu`, put `rho=lambda/mu`. The positive geometric law with PGF
   `g(s)=(1-rho)*s/(1-rho*s)` is quasi-stationary because, for every `t>=0`,
   `[g(F_t(s))-g(F_t(0))]/[1-g(F_t(0))]=g(s)`. Conditional survival from
   every fixed `z>=1` converges to this law. The pure-death edge has `g(s)=s`
   and is the point mass at one.
2. If `lambda=mu=c>0`, then `Z_t/(ct)` conditional on survival converges to
   `Exp(rate 1)`.
3. If `lambda>mu`, then `W_t=e^{-(lambda-mu)t}Z_t` converges almost surely and
   in `L2`. Put `q=(lambda-mu)/lambda`. For `z` ancestors,
   `K~Binomial(z,q)`, `P(W=0)=(mu/lambda)^z`, and given `K=k>=1`,
   `W~Gamma(shape k, rate q)`. Thus the positive limit is a conditional
   binomial mixture of gamma components, not a single component in general.

The theorem separately closes `z=0`, `t=0`, `lambda=mu=0`, pure birth, pure
death, the critical coordinate, and every condition under which survival
conditioning is undefined. The finite regression checks conventions; the
proof, not its parameter grid, establishes the continuum claims.
