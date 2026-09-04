# Theorem package: complete Berger Ricci-flow atlas

Let `sigma_i` satisfy `d sigma_1 = 2 sigma_2 wedge sigma_3` cyclically and
let

\[
g=A(\sigma_1^2+\sigma_2^2)+C\sigma_3^2,
\qquad A,C>0.
\]

## Main theorem

Under unnormalized Ricci flow the Berger cone is invariant and

\[
A'=-8+4r,\qquad C'=-4r^2,\qquad r'=\frac{8r(1-r)}A,
\qquad r=C/A.
\]

The sectional curvatures are

\[
K_{12}=\frac{4A-3C}{A^2},\qquad K_{13}=K_{23}=\frac C{A^2},
\]

and the orthonormal Ricci entries and scalar curvature are

\[
\operatorname{Ric}_{11}=\operatorname{Ric}_{22}=\frac4A-\frac{2C}{A^2},
\quad \operatorname{Ric}_{33}=\frac{2C}{A^2},
\quad R=\frac{8A-2C}{A^2}.
\]

Away from `r=1`,

\[
k=\frac C{\sqrt{|1-r|}}
\]

is positive and constant.  If `r<1`, put `u=sqrt(1-r)`; then

\[
A=\frac{ku}{1-u^2},\quad C=ku,\quad
u'=-\frac4k(1-u^2)^2.
\]

The solution is ancient and its remaining forward lifetime is

\[
T-t=\frac{k}{8}\left(\frac{u}{1-u^2}+\operatorname{atanh}u\right).
\]

If `r>1`, put `v=sqrt(r-1)`; then

\[
A=\frac{kv}{1+v^2},\quad C=kv,\quad
v'=-\frac4k(1+v^2)^2.
\]

Its remaining forward and backward lifetimes are respectively

\[
\frac{k}{8}\left(\frac{v}{1+v^2}+\arctan v\right),\qquad
\frac{k}{8}\left(\frac\pi2-\frac{v}{1+v^2}-\arctan v\right).
\]

The round solution is `A=C=A_0-4t` and is ancient.  Every positive solution
has finite forward extinction, `r -> 1` and
`A,C ~ 4(T-t)`.  More precisely,

\[
\lim_{t\uparrow T}(T-t)R(t)=\frac32,
\qquad
\lim_{t\uparrow T}(T-t)K_{13}(t)=\frac14.
\]

Thus curvature really blows up, while `|Rm|=O((T-t)^{-1})`; the extinction is
Type I.  Squashed and round branches are ancient.  A stretched branch instead
has a finite backward endpoint with `A -> 0`, `C -> infinity`.

Under volume-normalized Ricci flow,

\[
A'=\frac83(r-1),\qquad C'=\frac{16}{3}r(1-r),
\]

`A^2 C` is constant and every positive solution exists for all forward time
and converges exponentially to the unique round metric on its volume leaf.

## Proof spine

The curvature formula follows from the orthonormal Milnor frame.  Substitution
into `g'=-2 Ric` gives the reduced ODE.  Direct differentiation proves the
ratio equation and first integral.  The two chart equations are separable;
their endpoint integrals determine the maximal intervals.  Their Taylor
expansions at zero give the common Type-I asymptotic; substitution into the
explicit scalar and mixed sectional curvatures gives the two nonzero scaled
limits above, so the endpoint is a genuine curvature singularity rather than
only a metric-cone boundary.  In normalized flow, volume preservation gives
`A=K r^{-1/3}`, reducing convergence to a scalar monotone equation.

## Boundaries and limitations

`r=4/3` is the horizontal sectional-curvature wall, `r=2` the horizontal
Ricci wall, and `r=4` the scalar-curvature wall; all three now appear as
explicit evidence boundary rows.  The faces `A=0` and `C=0`
are not Riemannian metrics.  The local calculation descends to compatible
finite left quotients.  No claim concerns the full unequal-axis cone, weak
continuation through extinction, or Laplace-spectrum convergence.

## Route-A result

The tuple is

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`.

Therefore Route A is rejected and Route B is locked.  The package claims no
target arithmetic local data, Euler factors, bad-prime data, root number,
automorphy, target divisor/counting law, target functional equation,
target-zero match, or Hilbert--Pólya operator.
