# HCS-C47 exact results

## Exact local normalized-trace model

For every split prime, the direct sum over \(d_p=(p-1)/2\) real Galois
classes has positive field-degree-normalized identity trace

\[
\tau_p(1)=\frac{8p+4}{3}.
\]

The grading supertrace gives exactly

\[
\operatorname{str}_p(W_p^n)=c_{p,n}=\frac{C_{p,n}}{d_p}.
\]

The positive trace supplies size and integrability; the supertrace supplies
the analytic phase.  A positive Fuglede--Kadison determinant alone cannot
replace the latter.

## Semifinite and classical thresholds

\[
\tau(|X_s|^q)=
\sum_{p\equiv1\pmod3}\frac{8p+4}{3}p^{-q\Re s},
\qquad
X_s\in L^q(M,\tau)\Longleftrightarrow q\Re s>2.
\]

| normalized semifinite class | exact domain |
|---|---|
| \(L^1\) | \(\Re s>2\) |
| \(L^2\) | \(\Re s>1\) |
| \(L^3\) | \(\Re s>2/3\) |
| \(L^4\) | \(\Re s>1/2\) |

Since \(|\Gamma X_s|=|X_s|\), grading cancellation cannot improve the
positive \(\tau\)-trace-class threshold.  It does, however, enter the
normalized semifinite regularization.

These \(L^q\) classes use the field-degree-normalized semifinite trace.
For the canonical Hilbert trace, \(X_s\in S^q(\mathcal H)\) instead requires
\(q\Re s>3\), so classical trace class starts only at \(\Re s>3\).  The
classical trace does not encode the field-degree-normalized root.

## Exact fourth-order realization

On \(\Re s>1/2\),

\[
\mathcal G(s)=
\exp\!\left(-\ell_1(s)-\frac{\ell_2(s)}2-\frac{\ell_3(s)}3\right)
\det_{4,\tau,\mathrm{gr}}(I-X_s).
\]

The three counterterms are convergent series of exact local chronological
Galois supertraces, not fitted prefactors.  They are not global semifinite
traces of non-\(L^1\) powers.  This is a genuine operator-category upgrade of
the C45 germ in the semifinite \(\tau\)-category, not a classical Fredholm
determinant.  It proves neither continuation nor a Riemann divisor.

The frozen unnormalized third Galois-traced moments \(C_{p,3}\) are exact
rationals:

\[
\frac{12}{7},\frac{132}{13},\frac{54}{19},\frac{960}{31},
-\frac{612}{37},\frac{3054}{43},\frac{3414}{61}.
\]
