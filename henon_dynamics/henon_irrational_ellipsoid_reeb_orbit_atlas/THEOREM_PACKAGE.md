# C242 theorem package

## Frozen model

Let
\[
 E(a,b)=\{(z_1,z_2)\in\mathbb C^2:
 \pi|z_1|^2/a+\pi|z_2|^2/b\le1\},\qquad a,b>0,
\]
and restrict \(\lambda_0=\frac12\sum_j(x_j\,dy_j-y_j\,dx_j)\) to its
boundary.  Its Reeb flow is
\[
 \varphi_t(z_1,z_2)=(e^{2\pi it/a}z_1,e^{2\pi it/b}z_2).
\]
The coordinate circles are \(\gamma_1=\{z_2=0\}\) and
\(\gamma_2=\{z_1=0\}\), with action and period \(a\) and \(b\), respectively.

## Theorem (irrational slope)

If \(a/b\notin\mathbb Q\), a point with both coordinates nonzero cannot
return: closure would require \(t/a\in\mathbb Z\) and \(t/b\in\mathbb Z\),
which forces \(a/b\in\mathbb Q\). Hence the two coordinate circles are the
only simple closed Reeb orbits. Their iterates satisfy
\[
 A(\gamma_1^k)=T(\gamma_1^k)=ka,\qquad
 A(\gamma_2^k)=T(\gamma_2^k)=kb.
\]
In the transverse complex line and the coordinate complex-line trivialization
used by Hutchings, the return
eigenvalues are
\[
 \rho(\gamma_1^k)=e^{\pm2\pi i k a/b},\qquad
 \rho(\gamma_2^k)=e^{\pm2\pi i k b/a},
\]
and Hutchings' convention gives
\[
 \mu_{\rm CZ}(\gamma_1^k)=2\lfloor ka/b\rfloor+1,qquad
 \mu_{\rm CZ}(\gamma_2^k)=2\lfloor kb/a\rfloor+1.
\]
The irrationality also makes both transverse returns nondegenerate.

## Rational boundary

If \(a/b=p/q\) in lowest terms, the common period is
\(L=qa=pb\). Every boundary point is periodic at time \(L\), so the
Morse--Bott critical manifold is the full three-dimensional boundary (the
orbit-space family has dimension two). The coordinate circles are degenerate
members with transverse multiplier one. A nondegenerate CZ index is not
assigned until a perturbation is chosen; the receipt records this as `null`,
not as an irrational floor formula.

## Exact floor certificate

For the parameter witnesses \(a/b=\sqrt2\) and \(1/\sqrt2\), the producer
uses no floating-point comparison. It records an integer \(m\) and verifies
\[
 m^2\le2k^2<(m+1)^2
 \quad\text{or}\quad
 2m^2\le k^2<2(m+1)^2,
\]
which are equivalent to the two required floor statements. The independent
checker recomputes all 48 rows for \(1\le k\le12\), while the six rational
rows certify \(qa=pb\).

## Route-A disposition

The result is a convention-complete analytic A1 orbit theorem. The geometric
parameters carry no intrinsic prime or prime-power labels, so A0 fails; no
target weighted zeta or determinant is defined, so A2 and A3 fail. The formal
quantization hint is not a Hilbert--Pólya operator. The locked tuple is
`(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` with Route B
disabled.

## Reproducibility and nonclaims

The JSON receipt, independent checker, SymPy crosscheck, byte replay and
29-case hostile suite are part of this package. No literature-priority claim,
arithmetic matching claim, target-zero claim, Euler-factor/root-number claim,
or external peer-review claim is made.
