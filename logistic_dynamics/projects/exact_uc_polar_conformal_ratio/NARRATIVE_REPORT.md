# Narrative report — LOG-0001 conformal-ratio stage

## Result

Let `U_L,U_R` be the radius-`1/1000` operator stadiums and `V_L,V_R` the
radius-`3/5000` proof-only stadiums.  Normalize the two Riemann maps from the
unit disk at the branch midpoints with positive derivative.  For a point in
the closed inner stadium, travel from the midpoint to its projection on the
branch interval and then radially to the point.  Hyperbolic density
monotonicity bounds the two path pieces by `500*pi` and `log(4)`.  Therefore

\[
r_L=r_R\le r_*:=\tanh\!\left(\frac{500\pi+\log4}{2}\right)<1.
\]

The stable quantities

\[
\delta_*=1-r_*,\qquad \beta_*=-\log r_*
\]

both begin `3.2418512480136249798...e-683`.  A 4096-bit Arb computation
certifies positive lower bounds for both.

## Determinant consequence

The preceding LOG-0001 theorem organizes the same matching-space operator
into two geometric Taylor streams.  Bounding each finite geometric
denominator by `delta_*`, keeping `||ell||<103/125`, and summing a shifted
Gaussian in the coefficient rank gives

\[
|D_{\rm pol}(s)|\le
\exp\!\left(3.45\times10^{689}
+4.20\times10^{682}(1+|s|)^2\right).
\]

This numerical envelope concerns the same canonical Fredholm determinant; no
finite matrix or reciprocal zeta is substituted.

## Interpretation

The result closes a proof-constant gap, not an arithmetic one.  The enormous
constants reflect the aspect ratio of the frozen stadium and the elementary
path estimate.  They do not estimate the true determinant type.  Exact order,
lower growth, a sharp divisor law, completed-xi structure, quantization, and
Route B remain open or unauthorized.

