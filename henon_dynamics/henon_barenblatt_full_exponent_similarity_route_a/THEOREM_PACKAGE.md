# Theorem package

Let `m>0`, `M>0`, `alpha=1/(m+1)`, and

\[
u(x,t)=t^{-\alpha}F(\xi),\qquad \xi=x t^{-\alpha}.
\]

Assume `F` is centered, nonnegative, integrable, has mass `M`, that `F^m` is
locally absolutely continuous, and that

\[
(F^m)' + \alpha\xi F=0
\]

holds almost everywhere.  Uniqueness below is up to almost-everywhere
equality (equivalently, for the continuous representative determined by
`F^m`).  Then `F` has exactly one of the following forms.

## Complete profile classification

For `m>1`, put

\[
p=\frac1{m-1},\qquad k=\frac{m-1}{2m(m+1)}.
\]

Then

\[
F(\xi)=(C-k\xi^2)_+^p,
\quad
M=C^{p+1/2}k^{-1/2}B(1/2,p+1).
\]

For `m=1`,

\[
F(\xi)=\frac{M}{2\sqrt\pi}e^{-\xi^2/4}.
\]

For `0<m<1`, put

\[
q=\frac1{1-m},\qquad b=\frac{1-m}{2m(m+1)}.
\]

Then

\[
F(\xi)=(C+b\xi^2)^{-q},
\quad
M=C^{1/2-q}b^{-1/2}B(1/2,q-1/2).
\]

Each displayed mass is a strictly monotone function of `C>0`, so prescribed
`M` fixes `C` uniquely.  This is only a centered zero-flux first-kind profile
classification; it is not a classification of arbitrary Cauchy solutions.
Indeed, on each positivity component the integrated law gives the displayed
quadratic or logarithmic primitive.  In the porous branch, continuity at the
component endpoints forces equal endpoint modulus and hence the single
interval `(-sqrt(C/k),sqrt(C/k))`.  In the heat and fast branches the finite
primitive cannot meet zero at a finite endpoint, so the positivity set is all
of the real line.  Thus extra components or zero intervals cannot occur.

## Absolute moments

For every real `r>-1`, the porous-medium coefficient is

\[
\int_{\mathbb R}|\xi|^rF(\xi)\,d\xi
=C^{p+(r+1)/2}k^{-(r+1)/2}B((r+1)/2,p+1).
\]

All such moments are finite.  The Gaussian coefficient is

\[
M\,2^r\frac{\Gamma((r+1)/2)}{\sqrt\pi}.
\]

In fast diffusion,

\[
\int_{\mathbb R}|\xi|^rF(\xi)\,d\xi
=C^{-q+(r+1)/2}b^{-(r+1)/2}
B((r+1)/2,q-(r+1)/2)
\]

is finite exactly when

\[
r<2q-1=\frac{1+m}{1-m}.
\]

At equality the divergence is logarithmic; above it the divergence is a
power.  Consequently the fast-diffusion second moment is finite exactly for
`m>1/3`, logarithmically divergent at `m=1/3`, and power divergent below.

## Pressure, rescaling, and dissipation

For `m>1`, the pressure

\[
P=\frac{m}{m-1}u^{m-1}
\]

is quadratic on the positivity set.  Writing \(R_M=\sqrt{C/k}\), the
interfaces are \(X_\pm(t)=\pm R_Mt^\alpha\), and the one-sided pressure law is

\[
X_\pm'(t)=\frac{\alpha X_\pm(t)}t
=-\lim_{x\to X_\pm(t),\,u(x,t)>0}P_x(x,t).
\]

With `tau=log t`, `xi=x t^{-alpha}`, and `v=t^alpha u`,

\[
v_\tau=(v^m)_{\xi\xi}+\alpha(\xi v)_\xi
=\partial_\xi(v\partial_\xi\mu),
\]

where

\[
\mu=\frac{m}{m-1}v^{m-1}+\frac\alpha2\xi^2\quad(m\ne1),
\qquad
\mu=\log v+\frac\alpha2\xi^2\quad(m=1).
\]

The mass-`M` profile is stationary.  Define the branched free energy by

\[
\mathcal F_m[v]
=\int_{\mathbb R}\left(\frac{v^m}{m-1}
+\frac{\alpha}{2}\xi^2v\right)d\xi,
\qquad m\ne1,
\]

and by its heat branch

\[
\mathcal F_1[v]
=\int_{\mathbb R}\left(v\log v-v
+\frac14\xi^2v\right)d\xi.
\]

Their first variations are precisely the two displayed formulas for `mu`.
For sufficiently regular positive rescaled solutions for which every
displayed energy term is finite (so no infinity-minus-infinity is used) and
whose boundary decay justifies integration by parts,

\[
\frac{d\mathcal F_m}{d\tau}
=\int_{\mathbb R}\mu\,\partial_\xi(v\partial_\xi\mu)\,d\xi
=-\int_{\mathbb R}v|\partial_\xi\mu|^2\,d\xi.
\]

No dissipation claim is made outside that class.  In the fast Barenblatt
family the finite-second-moment/free-energy setting used here applies for
`m>1/3`, not at or below the boundary.
