# Theorem package

## Frozen convention

Let `r=(x,y)` be the knife contact point, `theta` the blade angle, `u` the
signed velocity along the blade, `omega=theta_dot`, and `I_c=J+m a^2`.

```text
r_dot=u(cos theta,sin theta),  theta_dot=omega,
u_dot=a omega^2,               omega_dot=-(m a/I_c)u omega.
```

The conserved energy is `H=m u^2/2+I_c omega^2/2`.

## Complete signed-offset theorem

For `a!=0`, `H>0` and `omega_0!=0`, put

```text
R=sqrt(2H/m), A=m|a|R/I_c, eta=sqrt(I_c/m)/|a|,
sigma=sign(omega_0), s=A(t-t0).
```

Then, for a unique `t0` and `theta0`,

```text
u=sign(a) R tanh(s),
omega=sigma R sqrt(m/I_c) sech(s),
theta=theta0+sigma eta asin(tanh(s)).
```

It is a heteroclinic connection from `(-sign(a)R,0)` to
`(sign(a)R,0)`.  Its blade-angle deflection is `sigma*pi*eta`, independent of
energy.  With `q=tanh(s)`, contact position is the exact one-dimensional
quadrature

```text
r(q)-r(0)=(sign(a)R/A) integral_0^q
  y e(theta0+sigma eta asin y)/(1-y^2) dy.
```

The velocity converges exponentially at both ends, so unique intercepts
`b_plus,b_minus` exist with `r(t)=b_plus+v_plus t+o(1)` as `t->+infinity`
and the analogous formula at `-infinity`.  These are two asymptotic lines.
The blade deflection is not automatically the velocity-heading deflection:
negative `u` adds `pi` to the physical heading.

On the equilibrium line `omega=0`, the transverse eigenvalue is
`-(m a/I_c)u_*`; precisely `a u_*>0` is stable.  Each open half-plane carries
the Poisson bracket `{u,omega}=(a/I_c)omega`, which generates the reduced flow
from `H`.  The reduced density `du domega/|omega|` is invariant there, and its
product with configuration Haar volume is an off-line full-flow invariant
measure.  No positive `C^1` reduced density, hence no smooth density of
configuration-Haar-factor form, extends across a nonzero reduced equilibrium.
Because that state still translates in the full reconstruction when `u_*!=0`,
this pointwise argument does not exclude every configuration-dependent
full-flow density.

The involution `(r,theta,u,omega)->(r,theta,-u,-omega)` reverses time.  If
`a=0`, `u,omega` are constant: `omega!=0` gives a periodic `SE(2)` circle of
period `2pi/|omega|`, whereas `omega=0` gives a straight line (or a fixed
configuration when `u=0`).  If `a!=0` but `omega_0=0`, the reduced state is an
equilibrium and reconstruction is straight; `H=0` is fixed.  Hence all
recurrence boundaries are explicit.

## Proof/evidence separation

Substitution, energy reduction, exponential endpoint estimates, linearization,
the invariant-density equation and the reversor identity prove the theorem for
continuous parameters.  The 12-orbit/36-state ledger only checks signs,
normalizations and limiting formulas.

## Route-A verdict

```text
(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
ROUTE_A_REJECTED; Route B false.
```

The Poisson form is a formal operator hint, not a target Hilbert–Pólya lift.
