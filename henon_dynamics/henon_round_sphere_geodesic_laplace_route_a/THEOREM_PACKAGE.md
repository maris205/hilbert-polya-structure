# Round-sphere geodesic and Laplace theorem

On `T^1 S_R^d`, `d>=2`, write `|x|=R`, `|v|=1`, `x dot v=0`.  Then

\[
\Phi_t(x,v)=\left(\cos(t/R)x+R\sin(t/R)v,
-R^{-1}\sin(t/R)x+\cos(t/R)v\right).
\]

Every orbit has least period `2pi R`.  The fixed set of `Phi_t` is the whole
unit tangent bundle when `t` is an integer multiple of that period and is
empty otherwise.  The return derivative is the identity, so the family is
maximally clean.  Quotienting by the flow gives the oriented Grassmannian of
two-planes in `R^(d+1)`; its dimension is `2d-2`.

For the nonnegative Laplacian,

\[
\lambda_\ell=\frac{\ell(\ell+d-1)}{R^2},\qquad
m_{d,\ell}=\frac{(2\ell+d-1)(\ell+d-2)!}{\ell!(d-1)!}.
\]

The heat operator is trace class for every positive time with trace
`sum m exp(-t lambda)`.  Completing the square gives the natural
functional-calculus operator

\[
Q_d=\sqrt{-\Delta+(d-1)^2/(4R^2)},\qquad
Q_d|_{\mathcal H_\ell}=\frac{\ell+(d-1)/2}{R}.
\]

Therefore `exp(-i 2pi R Q_d)=(-1)^(d-1) I` and
`exp(-i 4pi R Q_d)=I`.

The strict Route-A tuple is
`(A0_FAIL,A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`.  Exact source
revival does not create a target spectral correspondence.
