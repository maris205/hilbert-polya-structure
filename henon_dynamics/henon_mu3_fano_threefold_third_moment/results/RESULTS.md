# HCS-C49 exact results

## Outcome

The six-step chronological third moment admits an exact projective
interpretation through the complete intersection

\[
X_\rho=V\!\left(\sum_{i=0}^5x_i^3,
x_0x_1+x_1x_2+x_2x_3+x_3x_4+x_4x_5+\rho x_5x_0\right)
\subset\mathbf P^5.
\]

For every split prime \(p>3\), radial counting gives

\[
Z_{p,3}=1+\#\mathbf P^5-\#S-\#Q+p\#X,
\qquad
C_{p,3}=-2-\frac{2\alpha_p}{p^2}-\frac{2\beta_p}{p},
\]

where \(\alpha_p=\#S-\#\mathbf P^4\) and
\(\beta_p=\#\mathbf P^3-\#X\). The quadratic form is split because its
hyperbolic discriminant is \(\rho\), a square at split primes, hence

\[
\#Q=(p^2+1)(p^2+p+1).
\]

The generic characteristic-zero fibre is a smooth \((2,3)\) Fano
threefold. Adjunction and the Chern-class computation give

\[
K_X=\mathcal O_X(-1),\qquad e(X)=-36,\qquad b_3(X)=40,
\qquad h^{1,2}(X)=20.
\]

The Fermat--Jacobi formula
\(\alpha_p=20p^2+pa_p\) is an all-split-prime theorem. At good split
primes, Chevalley--Warning gives \(p\mid\beta_p\); writing
\(\beta_p=pb_p\) yields

\[
C_{p,3}=-42-2b_p-\frac{2a_p}{p}.
\]

The actual quotient values in the finite ledger are controls, not a claimed
new distribution theorem. Likewise, HCS-C49 does not promote its finite
smoothness controls to an all-split-prime smoothness theorem.

## Exact finite ledger

All 21 split primes through 199 were counted exactly by projective charts.
The first seven were independently matched by a literal six-step chronology
dynamic program. Fractions are reduced.

| \(p\) | \(C_{p,3}\) | \(c_{p,3}=2C_{p,3}/(p-1)\) |
|---:|---:|---:|
| 7 | 12/7 | 4/7 |
| 13 | 132/13 | 22/13 |
| 19 | 54/19 | 6/19 |
| 31 | 960/31 | 64/31 |
| 37 | -612/37 | -34/37 |
| 43 | 3054/43 | 1018/301 |
| 61 | 3414/61 | 569/305 |
| 67 | 3300/67 | 100/67 |
| 73 | -828/73 | -23/73 |
| 79 | -3264/79 | -1088/1027 |
| 97 | 1218/97 | 203/776 |
| 103 | 1104/103 | 368/1751 |
| 109 | 864/109 | 16/109 |
| 127 | -8928/127 | -992/889 |
| 139 | 888/139 | 296/3197 |
| 151 | -3138/151 | -1046/3775 |
| 157 | 7458/157 | 1243/2041 |
| 163 | 11790/163 | 1310/1467 |
| 181 | -1908/181 | -106/905 |
| 193 | 1644/193 | 137/1544 |
| 199 | -16560/199 | -1840/2189 |

The certificate also stores \(Z,S,Q,X,\alpha,\beta\), the disjoint chart
counts, the exact quotient ledgers, and integer Weil inequalities for every
row.

## Smoothness firewall

For \(x_0\ne0\), the normalized singular recurrence reduces to two boundary
equations in \(t=x_0^3,u=x_1/x_0^2\). The stored elimination polynomials have
degrees 21 and 20. The checker independently constructs their 41-by-41
Sylvester matrix and obtains

\[
\operatorname{Res}(R,H)=2^{21}3^{12}23^3\ne0.
\]

It also verifies the full projection-denominator factorization and the
split/inert classification. The derivation of the triangular Gröbner
remainder and the recorded modular Gröbner computations at the denominator
primes remain explicit external exact-elimination proof artifacts; they are
not silently represented as computations performed by the checker.

## Analytic and operator gain

At good split primes, the rank-22 Fermat bound and \(b_3=40\) give

\[
|C_{p,3}|\le46+80\sqrt p,
\qquad
|c_{p,3}|\le\frac{92+160\sqrt p}{p-1}=O(p^{-1/2}).
\]

Thus the third-moment wall drops to \(\Re s>1/6\). Together with the second
moment and the uniform \(n\ge4\) estimate, the normalized Euler germ is
holomorphic and nonzero on

\[
\boxed{\Re s>1/4}.
\]

In the field-degree-normalized semifinite category,
\(X_s\in L^q(\mathcal M,\tau)\) exactly when \(q\Re s>2\). Therefore order
eight is the minimal fixed regularization covering this half-plane:

\[
\mathcal G(s)=\exp\!\left(-\sum_{n=1}^{7}\frac{\ell_n(s)}n\right)
\operatorname{Det}_{8,\tau,\mathrm{gr}}(I-X_s).
\]

This is not a classical Fredholm determinant. On the underlying Hilbert
space, \(X_s\in S^q\) only when \(q\Re s>3\), and the classical trace does
not implement the normalized root.

## Route-A status and limits

The scoped verdict is
`ROUTE_A_EXPLORATORY_FANO_THREEFOLD_QUARTER_ABSCISSA`:

- A1: `A1_WEAK`;
- A2: `A2_ANALYTIC_DETERMINANT`;
- A3: `A3_PARTIAL_ANALYTIC_STRUCTURE`;
- A4: `A4_NATURAL_QUANTIZATION`.

No continuation through \(\Re s=1/4\), functional equation, Gamma factor,
Riemann divisor, self-adjoint Hilbert--Pólya operator, or RH result is
claimed. The next large gate is the fourth chronological moment or an
independent global functional-equation mechanism.
