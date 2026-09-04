# Theorem package: planar Keller--Segel critical mass

Consider

\[
\rho_t=\Delta\rho-\nabla\cdot(\rho\nabla c),
\qquad -\Delta c=\rho,
\qquad
c(x)=-\frac1{2\pi}\int\rho(y)\log|x-y|\,dy.
\]

Assume throughout each asserted open time interval that `rho` is a
`C1`-in-time, `C2`-in-space nonnegative solution of finite mass, that the
logarithmic convolution defining `c` exists, and that the displayed fluxes,
derivatives, and cutoff limits are integrable.  Barycenter conservation is
asserted only with a finite first moment.  The virial identity is asserted only
with a finite second moment.  The free-energy identity additionally requires
finite entropy and interaction energy, strict positivity when `M>0`, and a
finite dissipation integral.  The zero solution is handled separately without
using `log rho`.

## Main theorem

1. Mass `M=integral rho` is constant; when the first moment is finite, the
   barycenter `integral x rho` is constant.
2. Under the free-energy hypotheses above, the free energy

   \[
   \mathcal F[\rho]=\int\rho\log\rho-\frac12\int\rho c
   \]

   satisfies

   \[
   \frac{d\mathcal F}{dt}
   =-\int\rho|\nabla(\log\rho-c)|^2.
   \]

   For `rho_lambda(x)=lambda^2 rho(lambda x)`,

   \[
   \mathcal F[\rho_\lambda]-\mathcal F[\rho]
   =2M\left(1-\frac{M}{8\pi}\right)\log\lambda.
   \]
3. If additionally `I=integral |x|^2 rho` is finite, then

   \[
   I'=4M\left(1-\frac{M}{8\pi}\right).
   \]

   Hence for `M>8 pi` the classical finite-moment solution cannot persist
   beyond

   \[
   T_* = \frac{2\pi I(0)}{M(M-8\pi)}.
   \]
4. At `M=8 pi`, for every `lambda>0` and `a` in the plane,

   \[
   \rho_{\lambda,a}(x)=
   \frac{8\lambda^2}{(\lambda^2+|x-a|^2)^2},\qquad
   c_{\lambda,a}(x)=-2\log(\lambda^2+|x-a|^2)+C
   \]

   is stationary and has mass `8 pi`.  Its second moment is infinite.
5. For a radial solution regular at the origin let

   \[
   m(r,t)=2\pi\int_0^r s\rho(s,t)\,ds,\qquad n=m/(2\pi).
   \]

   Then, for `r>0`,

   \[
   n_t=n_{rr}-\frac1r n_r+\frac1r n n_r.
   \]

   Here `m(0,t)=m_r(0,t)=0`; the equation at the origin is understood through
   its regular radial limit.

## Proof spine

For positive `rho`, the PDE is `div(rho grad(log rho-c))`; the stated
integrability and cutoff hypotheses justify integration by parts and prove the
first two items.  Dilation changes entropy by `2M log lambda` and logarithmic
interaction by `-M^2 log lambda/(4 pi)`.  For the virial law, symmetrize
`x dot (x-y)/|x-y|^2` with its reversed pair; the numerator becomes one.
One first excludes `|x-y|<=epsilon`; local integrability of the Newtonian
gradient and the stated moments permit the cutoff limit.
The resulting constant slope cannot drive a nonnegative second moment below
zero, yielding `T_*`.

For the critical profile, direct radial differentiation gives
`-Delta c=rho` and `grad log rho=grad c`.  Its enclosed mass is
`8 pi R^2/(lambda^2+R^2)`.  Its truncated second moment is

\[
8\pi\lambda^2\left[
 \log\frac{\lambda^2+R^2}{\lambda^2}
 +\frac{\lambda^2}{\lambda^2+R^2}-1\right],
\]

which diverges logarithmically.  Finally, integrating the radial PDE over a
disc and using `c_r=-m/(2 pi r)` yields the cumulative equation.

## Scope and Route A

The theorem does not construct post-concentration measure solutions, prove
general subcritical convergence, or classify nonradial critical dynamics.
The Route-A tuple is

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`.

Route A is rejected and Route B is locked.  No target arithmetic local data,
Euler factors, bad-prime data, root number, automorphy, target divisor or
counting law, target functional equation, target-zero match, or
Hilbert--Pólya operator is claimed.
