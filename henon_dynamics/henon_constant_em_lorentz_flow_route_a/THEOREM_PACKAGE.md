# Theorem package

Let `eta=diag(1,-1,-1,-1)` and

```text
A/kappa = [[0, Ex, Ey, Ez],
           [Ex, 0, Bz,-By],
           [Ey,-Bz, 0, Bx],
           [Ez, By,-Bx, 0]],       kappa=q/m.
```

Then `A^T eta+eta A=0` and the spatial equation is
`du/dtau=kappa*u0*(E+v cross B)`.  Thus all signs are frozen.

## Main theorem

There are unique `a,b>=0` such that
`chi_A(z)=(z^2-a^2)(z^2+b^2)`, with
`a^2-b^2=kappa^2(E^2-B^2)` and `a^2b^2=kappa^4(E dot B)^2`.
If `D=a^2+b^2>0`,

`Ph=(A^2+b^2I)/D`, `Pr=(-A^2+a^2I)/D`

are complementary projectors and

`exp(tau A)=Ph[cosh(a tau)I+sinh(a tau)A/a]+Pr[cos(b tau)I+sin(b tau)A/b]`,

with analytic limiting quotients.  Integrating gives

`Phi=Ph[sinh(a tau)I/a+(cosh(a tau)-1)A/a^2]
    +Pr[sin(b tau)I/b+(1-cos(b tau))A/b^2]`,

and `x(tau)=x0+Phi(tau)u0`.  The flow preserves `eta(u,u)`, has determinant one, and is proper orthochronous.

Nonconstant velocity is periodic exactly when `b>0`, `Pr u0 != 0`, and either `a=0` or `Ph u0=0`; its least
period is `2pi/b`.  For `a>0`, the hyperbolic component prevents periodicity.  For `a=0<b`, the `Ph` component
is constant and the `Pr` component rotates.  A future-timelike physical worldline never closes because `u^0`
stays positive, so `x^0` is strictly increasing.

Electric-like (`a>0,b=0`) motion is hyperbolic plus a secular kernel; magnetic-like (`a=0,b>0`) motion is a
constant kernel plus rotation; generic motion has hyperbolic and rotational planes.  At `A=0`, velocity is
constant and position is affine.  A nonzero null field has `a=b=0`, `A^3=0 != A^2`,
`exp(tau A)=I+tau A+tau^2A^2/2`, and
`Phi=tau I+tau^2A/2+tau^3A^2/6`; it has no nonconstant periodic velocity.
