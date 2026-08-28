# Theorem package

Let `a,b,c,d>0` and consider

`x' = x(a-b y),   y' = y(-c+d x)`

on the open positive quadrant. Set `x_* = c/d`, `y_* = a/b`,
`u=log(x/x_*)`, and `v=log(y/y_*)`. Then

`u' = a(1-exp(v)),   v' = c(exp(u)-1)`.

Define `F(s)=exp(s)-s-1` and

`H(u,v)=c F(u)+a F(v)`.

## Main theorem

1. `H` is a strict convex proper first integral. Its only critical point is
   `(0,0)`, and `H(0,0)=0`.
2. For every `h>0`, the level `H=h` is a smooth compact oval and the vector
   field is nonzero on it. Consequently it is one periodic orbit with a finite
   physical period `T(h)`.
3. For `r>=0`, the two inverse branches of `F` are
   `ell(r)=-W_0(-exp(-1-r))-1-r` and
   `upp(r)=-W_{-1}(-exp(-1-r))-1-r`. Writing
   `u_- = ell(h/c)`, `u_+ = upp(h/c)`, and
   `r(u)=(h-cF(u))/a`, the exact quadratures are:

   `Area(h)=integral_{u_-}^{u_+}[upp(r(u))-ell(r(u))] du`,

   `T(h)=(1/a) integral_{u_-}^{u_+}[1/(1-exp(ell(r(u))))
       +1/(exp(upp(r(u)))-1)] du`.

   Endpoint singularities are integrable.
4. With geometric action `J(h)=Area(h)/(2 pi)`, coarea gives
   `J'(h)=T(h)/(2 pi)` for `h>0`.
5. The linearized center has frequency `sqrt(a c)`, hence
   `lim_{h downarrow 0} T(h)=2 pi/sqrt(a c)`.
6. Every periodic orbit satisfies exact averages
   `<x>=c/d` and `<y>=a/b` (equivalently `<exp(u)>=<exp(v)>=1`).

The axes are invariant but have no positive-quadrant periodic oval. If a rate
vanishes, the strict-positive theorem is not applied; the resulting triangular
or one-dimensional equations are boundary models. No period monotonicity or
large-energy asymptotic is asserted.

## Proof ledger

The Hessian of `H` is `diag(c exp(u),a exp(v))`, while `F(s)` tends to infinity
at both ends, proving strict convexity and properness. A positive level is
therefore a compact regular one-manifold. The Hamilton equations make it
invariant, and the sole zero of the vector field is the origin, which is not on
`H=h`; each connected level is consequently a periodic orbit. Solving
`F(s)=r` by `W_0` and `W_{-1}` gives the two branches. Splitting the orbit into
the lower and upper branches yields the two quadratures. The area formula and
the coarea identity for a regular nested level family give `d Area/dh=T`.
Linearization at the center is the matrix `[[0,-a],[c,0]]`. Finally, integrate
`u'` and `v'` over one period to obtain the two exponential averages, then
return to `x,y` coordinates.

The theorem is global in the positive parameter family, but the numerical
ledger below is only a reproducible finite control; it is not a substitute for
the proof.
