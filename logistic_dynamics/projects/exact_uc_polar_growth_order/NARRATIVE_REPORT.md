# Narrative report — LOG-0001 growth-order stage

## Result

Keep the exact-\(U_c\) polar matching-space determinant

\[
D_{\rm pol}(s)=\det_{\rm Fr}(I-\mathcal L_{s,B})
\]

without changing the map, roof, domains, or determinant convention. The
compactly nested stadiums provide two geometric rank-one streams, indexed by
the input branch and a Taylor degree. Their norms are bounded by

\[
\|u_{\sigma,m}\|\,\|x_{\sigma,m}(s)\|
\le e^{L_\ell |s|}r_\sigma^m,
\qquad r_\sigma<1.
\]

Hadamard's inequality and the geometric elementary-symmetric identity then
give a Fredholm coefficient majorant with a negative quadratic exponent in
the rank. Summing that Gaussian-type majorant yields

\[
|D_{\rm pol}(s)|
\le \exp\!\left(C_0+C_1(1+|s|)^2\right).
\]

Thus the classical order is at most two. A nonzero anchor in the right
half-plane lets Jensen's formula convert the same envelope into `O(R^2)`
zeros in disks and `O(T^2)` zeros in every fixed real strip through height
`T`.

## Zero-free half-plane

Let

\[
\alpha_0=\frac{U_c^2}{4},\qquad
\tau_*=-\log\alpha_0=\log\frac4{U_c^2}.
\]

Every length-\(n\) word has roof time at least \(n\tau_*\). Applying this
lower bound to the unchanged signed trace ledger proves absolute convergence
of the trace logarithm at the actual Fredholm value whenever

\[
\Re s>\sigma_*:=\frac{\log2}{\log(4/U_c^2)}
=1.3382657903899534\ldots.
\]

In that half-plane the determinant is the exponential of its convergent
trace logarithm and is therefore nonzero.

## Interpretation

These conclusions are upper and target-free. They do not determine the
exact order or a sharp divisor asymptotic, and they do not evaluate or fit
any determinant root. The reusable mechanism is narrower: finitely many
geometric nuclear streams with parameter weights of size \(e^{O(|s|)}\)
produce a quadratic entire-function envelope, while a positive roof lower
bound supplies a zero-free right half-plane through the exact trace ledger.
