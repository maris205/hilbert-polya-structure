# Theorem package

## Frozen model

Let `B` be standard Brownian motion and let `L^0(X)` be **symmetric**
semimartingale local time.  For `p in [0,1]`, put `theta=2p-1` and freeze

`X_t=x+B_t+theta L_t^0(X)`.

For `0<p<1`, define the scale and speed densities (up to a common reciprocal
normalization) by

`s'(x)=1/(1-p)` for `x<0`, `s'(x)=1/p` for `x>0`,

`m'(x)=2(1-p)` for `x<0`, `m'(x)=2p` for `x>0`.

The endpoint conventions are obtained by monotone limits and excursion
construction, not by dividing by zero.

## Central theorem

For every `|theta|<=1` the SDE has a unique strong solution and defines a
conservative Feller semigroup.  For `t>0` its Lebesgue density is

`q_p(t;x,y)=phi_t(y-x)+(2p-1)sgn(y)phi_t(|x|+|y|)`.

On a standard generator core, `A f=f''/2` off zero and

`p f'(0+)=(1-p)f'(0-)`.

The density `k_p(t;x,y)=q_p(t;x,y)/m'(y)` is symmetric in `x,y`, so the
semigroup is self-adjoint on `L^2(m)`.  For `lambda>0`, with
`k=sqrt(2lambda)`, the Lebesgue resolvent density is

`r_lambda(x,y)=[e^{-k|x-y|}+(2p-1)sgn(y)e^{-k(|x|+|y|)}]/k`.

Let `tau` be first exit from `(-a,b)`, `a,b>0`.  Then

`P_x(X_tau=b)=(s(x)-s(-a))/(s(b)-s(-a))`.

In explicit form, with `D=pa+(1-p)b`, this is

- `p(x+a)/D` for `-a<=x<=0`;
- `[pa+(1-p)x]/D` for `0<=x<=b`.

For `lambda>0`, set `rho=(1-p)/p`, `k=sqrt(2lambda)`, and

`Q=cosh(kb)sinh(ka)+rho sinh(kb)cosh(ka)`.

The discounted right-exit transform is

- `sinh(k(x+a))/Q` on the negative side;
- `[cosh(kx)sinh(ka)+rho sinh(kx)cosh(ka)]/Q` on the positive side.

The left-exit transform follows by `(p,x,a,b)->(1-p,-x,b,a)`.  Their sum is
`E_x exp(-lambda tau)`.  The mean exit time is `-x^2+C x+B` on the negative
side and `-x^2+A x+B` on the positive side, where

`D_m=(1-p)b+pa`,

`A=(1-p)(b^2-a^2)/D_m`, `C=p(b^2-a^2)/D_m`,

`B=ab[pb+(1-p)a]/D_m`.

Finally, when `X_0=0`, the positive occupation fraction
`U_t=t^{-1} integral_0^t 1_{X_s>0} ds` is independent of `t` in law and has

`f_p(u)=p(1-p)/{pi sqrt[u(1-u)] [p^2(1-u)+(1-p)^2u]}`

for `0<u<1` and `0<p<1`.  Its mean is `p`; at `p=0` and `p=1` it becomes an
atom at zero and one respectively.

## Proof

Harrison and Shepp prove strong existence and pathwise uniqueness exactly for
`|theta|<=1`; equivalently, give every reflected Brownian excursion an
independent positive sign with probability `p`.  The image formula for `q_p`
is nonnegative, integrates to one, solves the heat equation away from zero,
and, as a function of the starting point, is continuous with
`p partial_x q(0+)=(1-p) partial_x q(0-)`.  Direct split-Gaussian convolution
gives Chapman--Kolmogorov, hence identifies the Feller semigroup.

For cross-interface points,

`q_p(t;x,y)=2(1-p)phi_t(|x|+|y|)` for `x>0>y`,

while the reversed density is `2p phi_t(|x|+|y|)`.  Division by `m'` makes
them equal; same-side symmetry is immediate.  Integrating each Gaussian
image against `e^{-lambda t}` and using
`integral_0^infty e^{-lambda t}phi_t(z)dt=e^{-sqrt(2lambda)|z|}/sqrt(2lambda)`
proves the resolvent formula.

Hitting probabilities solve `h''=0` on both subintervals, with two boundary
values, continuity, and the skew derivative condition.  The displayed scale
formula is the unique solution.  The right discounted transform solves
`u''/2=lambda u`, `u(-a)=0`, `u(b)=1`; propagating `(u,u'/k)` by hyperbolic
matrices on each side and multiplying the derivative by `rho` at zero gives
the displayed denominator `Q`.  Reflection gives the other side.  Solving
`m''/2=-1` with the same four matching conditions gives `A,B,C`.

At inverse local time, positive and negative excursion durations are
independent stable-`1/2` subordinators whose Laplace scale coefficients are
`p` and `1-p`.  Their ratio has the stated Lamperti density.  The substitution
`u=sin^2(v)` verifies normalization; reflection gives
`f_p(u)=f_{1-p}(1-u)`, and Fubini plus `P_0(X_s>0)=p` gives `E U_t=p`.

At `p=1/2` every image correction vanishes and ordinary Brownian motion is
recovered.  At `p=1` (`p=0`), after the first hit of zero all excursions are
positive (negative), giving the corresponding one-sided reflection.  If
`|theta|>1`, no solution exists; it is outside the frozen parameter space.

## Route-A stopping theorem

The process is recurrent on a noncompact continuum and has no isolated
finite primitive-orbit ledger.  Its heat/resolvent kernels carry neither
rational-prime labels nor a logarithmic prime clock.  Speed symmetrization is
a natural source Hilbert-space representation, but it supplies no target
divisor, Fredholm Euler product, target continuation, or Hilbert--Pólya
operator.  Under `NO_BAD_EULER_OR_ROOT_NUMBER`, the strict tuple is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`,

the verdict is `ROUTE_A_REJECTED`, and Route B is disabled.
