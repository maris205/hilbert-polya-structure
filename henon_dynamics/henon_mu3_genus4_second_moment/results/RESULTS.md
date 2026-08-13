# HCS-C48 exact results

## All-prime theorem

For every prime \(p>3\) with \(p\equiv1\pmod3\), the second chronological
moment is controlled by the smooth bidegree-\((3,3)\) curve

\[
X_p:\quad
\rho r^3(t^3+u^3)+s^3tu(\rho^2t-u)=0
\quad\subset\quad\mathbf P^1\times\mathbf P^1.
\]

The direct three-case Jacobian argument proves geometric smoothness outside
characteristics two and three; adjunction gives genus four.  If
\(a_p=p+1-\#X_p(\mathbf F_p)\), projective direction counting gives

\[
Z_p=p^3-p^2-8p+p\#X_p(\mathbf F_p),
\qquad
C_{p,2}=-14-2a_p.
\]

Thus the residual arithmetic term is an actual genus-four Frobenius trace,
not a fitted numerical pattern.  The integer form of the Weil check is
\(a_p^2\le64p\).

## Exact finite controls

All split primes through 199 pass independent chronological, projective,
moment, Weil, and four-chart Jacobian gates.  The first seven also pass a
third computation by direct enumeration of \(S\cap R\) in \(\mathbf P^3\).

| \(p\) | \(\rho\) | \(\#X_p\) | \(a_p\) | \(C_{p,2}\) | \(Z_p\) |
|---:|---:|---:|---:|---:|---:|
| 7 | 2 | 12 | -4 | -6 | 322 |
| 13 | 3 | 18 | -4 | -6 | 2158 |
| 19 | 7 | 24 | -4 | -6 | 6802 |
| 31 | 25 | 24 | 8 | -30 | 29326 |
| 37 | 26 | 54 | -16 | 18 | 50986 |
| 43 | 36 | 24 | 20 | -54 | 78346 |
| 61 | 47 | 78 | -16 | 18 | 227530 |
| 67 | 37 | 96 | -28 | 42 | 302170 |
| 73 | 8 | 66 | 8 | -30 | 387922 |
| 79 | 23 | 108 | -28 | 42 | 494698 |
| 97 | 35 | 90 | 8 | -30 | 911218 |
| 103 | 56 | 96 | 8 | -30 | 1091182 |
| 109 | 63 | 66 | 44 | -102 | 1289470 |
| 127 | 107 | 156 | -28 | 42 | 2051050 |
| 139 | 96 | 84 | 56 | -126 | 2676862 |
| 151 | 32 | 96 | 56 | -126 | 3433438 |
| 157 | 12 | 150 | 8 | -30 | 3867538 |
| 163 | 104 | 180 | -16 | 18 | 4332214 |
| 181 | 48 | 198 | -16 | 18 | 5931370 |
| 193 | 84 | 222 | -28 | 42 | 7193110 |
| 199 | 106 | 168 | 32 | -78 | 7872838 |

## Analytic and operator gain

The exact first moment has abscissa zero, the genus-four second moment has
abscissa \(1/4\), and the first unresolved generic wall is the third moment at
\(1/3\).  Consequently the normalized Euler germ is holomorphic and nonzero
on \(\Re s>1/3\).  Combining this with the exact C47 criterion
\(X_s\in L^q(M,\tau)\iff q\Re s>2\) gives

\[
\mathcal G(s)=
\exp\!\left(-\sum_{n=1}^{5}\frac{\ell_n(s)}n\right)
\det_{6,\tau,\mathrm{gr}}(I-X_s),
\qquad \Re s>\frac13.
\]

Order six is minimal in the normalized semifinite \(L^q(M,\tau)\) category on
the full open half-plane because order five requires \(\Re s>2/5\).  This is
not a classical Fredholm determinant: on the underlying Hilbert direct sum,
\(X_s\in S^q(\mathcal H)\) iff \(q\Re s>3\), so classical trace class begins
only at \(\Re s>3\), and its trace does not encode the normalized root.  No
continuation through \(1/3\), functional equation, Gamma factor, Riemann
divisor, or self-adjoint Hilbert--Pólya operator is claimed.
