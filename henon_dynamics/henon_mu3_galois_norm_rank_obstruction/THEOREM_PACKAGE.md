# HCS-C45 theorem package

## 1. Paired determinant and rational norm

For a split prime \(p\equiv1\pmod3\), let

\[
K_p=\mathbf Q(\zeta_p),\qquad
L_p=K_p^+,\qquad d_p=[L_p:\mathbf Q]=(p-1)/2.
\]

For the additive character \(\psi_a(x)=\zeta_p^{ax}\), let
\(D_{p,a}^{\rm aug}(z)\) be the C43 augmentation factor.  It is rational,
regular and nonzero on \(|z|<1\), has value one at the origin, has all finite
divisor support on \(|z|=1\), and has virtual degree two.

Define the conjugate-paired local factor

\[
E_p(z)=D_{p,1}^{\rm aug}(z)D_{p,-1}^{\rm aug}(z)\in L_p(z). \tag{1}
\]

Its logarithm is

\[
\Log_0E_p(z)=-\sum_{n\ge1}\frac{B_{p,n}}n z^n, \tag{2}
\]

where \(B_{p,n}=A_{p,n}(\psi)+A_{p,n}(\psi^{-1})\in L_p\).  A Galois
embedding changes only the additive character; it does not change the ordered
Hénon phase.

Set

\[
N_p(z)=\operatorname{Norm}_{L_p/\mathbf Q}E_p(z). \tag{3}
\]

Then \(N_p\in\mathbf Q(z)\), \(N_p(0)=1\), and

\[
\Log_0N_p(z)
=-\sum_{n\ge1}\frac{C_{p,n}}n z^n,
\qquad
C_{p,n}=\operatorname{Tr}_{L_p/\mathbf Q}B_{p,n}. \tag{4}
\]

## 2. Ordinary norm obstruction

Each conjugate of \(E_p\) has virtual degree four.  Therefore

\[
\boxed{\deg_{\rm virt}N_p=4d_p=2(p-1)}. \tag{5}
\]

This is the order at infinity and is invariant under cancellation between a
displayed numerator and denominator.  If a rational prefactor \(Q_p\) has
\(|\deg_{\rm virt}Q_p|\le M\) independently of \(p\), then

\[
|\deg_{\rm virt}(Q_pN_p)|\ge2(p-1)-M. \tag{6}
\]

Consequently the ordinary rational norm cannot be realized by graded
finite-dimensional determinant ratios of uniformly bounded rank difference.

## 3. The first rational trace

C44 proves

\[
\boxed{C_{p,1}=-6}. \tag{7}
\]

This follows from the zero-fiber identity
\(\#\{2x^3+2y^3+(1+\rho)xy=0\}=p-3\).

Multiplication by \((1-z)^6\) cancels only the first Taylor coefficient of
the norm.  It is not an established Tate factor because \(C_{p,n}\) is not
identically \(-6\) for higher \(n\).  For example, the exact second moment is
\(-30\) at \(p=31\).

## 4. Canonical normalized norm germ

On the simply connected disk \(|z|<1\), define

\[
G_p(z)=\exp\!\left(d_p^{-1}\Log_0N_p(z)\right),
\qquad G_p(0)=1. \tag{8}
\]

Then

\[
\Log G_p(z)=-\sum_{n\ge1}\frac{c_{p,n}}n z^n,
\qquad
c_{p,n}=C_{p,n}/d_p. \tag{9}
\]

Equation (7) gives the improved first coefficient

\[
\boxed{c_{p,1}=-\frac{12}{p-1}}. \tag{10}
\]

For every embedding \(\sigma:L_p\hookrightarrow\mathbf C\), C43's smooth
cubic bound gives

\[
|B_{p,n}^{\sigma}|\le4\cdot4^n.
\]

Averaging over embeddings yields

\[
|c_{p,n}|\le4\cdot4^n. \tag{11}
\]

### Theorem 4.1

The product

\[
\boxed{\mathcal G(s)=\prod_{p\equiv1\ (3)}G_p(p^{-s})} \tag{12}
\]

converges locally uniformly and defines a holomorphic nonzero function on

\[
\boxed{\operatorname{Re}s>1/2}. \tag{13}
\]

Proof.  On a compact subset with \(\operatorname{Re}s\ge\sigma_0>1/2\),
finitely many small-prime factors are analytic because \(|p^{-s}|<1\).  In
the prime tail, choose \(p\) so that \(4p^{-\sigma_0}\le1/2\).  The
\(n=1\) logarithmic series is bounded by

\[
\sum_p\frac{12p^{-\sigma_0}}{p-1}<\infty,
\]

while (11) makes the \(n\ge2\) part

\[
O\!\left(\sum_pp^{-2\sigma_0}\right)<\infty.
\]

Normal convergence of the canonical logarithm proves the result.

## 5. Boundary and determinant status

All zero and pole support of \(N_p\) lies on \(|z|=1\).  The germ in (8)
extends meromorphically across such a point only when the corresponding
divisor valuation of \(N_p\) is divisible by \(d_p\).  Equivalently, a global
ordinary rational root requires \(N_p\) to be a \(d_p\)-th power up to its
fixed normalization.

Thus (12) is a canonical normalized trace-determinant germ.  It is not yet:

- a rational finite-dimensional determinant;
- an ordinary Fredholm determinant;
- a function continued across \(\operatorname{Re}s=1/2\);
- a function satisfying the Riemann functional equation.

Under the optional display \(z=p^{1/2-s}\), unit-circle local divisors lie on
the critical line, but no natural-boundary theorem follows without controlling
cross-prime coincidences and cancellation.

## 6. Exact second-moment control

Let

\[
\Phi_{p,2}=2\sum_{i=0}^3x_i^3+x_0x_1+x_1x_2+x_2x_3+\rho x_3x_0,
\]

and let \(Z_{p,2}=\#\Phi_{p,2}^{-1}(0)\).  Chronological cyclotomic trace
gives

\[
C_{p,2}=\frac{2Z_{p,2}}p-2p^2,
\qquad
c_{p,2}=\frac{2C_{p,2}}{p-1}. \tag{14}
\]

Exact controls show \(C_{p,2}=-6,-6,-6,-30,18,-54,18,42,-30\) at
\(p=7,13,19,31,37,43,61,67,73\), respectively.  Hence there is no complete
Tate collapse.  This finite ledger is a control, not a boundary theorem.

## 7. Route-A scope

The normalized norm provides the strongest analytic half-plane yet obtained
from this Hénon arithmetic kernel.  It retains chronology, improves the Euler
domain to the open critical boundary, and uses no fitted data.  A1 remains
weak because the primes are arithmetic fibers.  A3 remains partial because
ordinary determinant structure, continuation, Gamma factors, and a functional
equation are open.  The correct tuple is

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

