# SD-C14 derivation package

## 1. Positive all-moment classification

Let \(\mu\) be a finite positive measure on \(\mathbb T\) such that
\(\int u^r\,d\mu(u)=1\) for every \(r\geq1\). Positivity implies that the
negative Fourier coefficients are the conjugates of the positive ones, hence
they also equal one. Therefore \(\nu=\mu-\delta_1\) has every nonzero Fourier
coefficient equal to zero. Uniqueness of Fourier coefficients for finite
measures gives

\[
  \mu=\delta_1+c\,m_{\rm Haar},\qquad c\geq0.
\]

The sign follows from positivity (equivalently, integrate a nonnegative
continuous function supported away from \(1\)). Thus a normalized state or a
finite-support solution has \(c=0\). The only nontrivial escape is the
nonnormalized, infinite Haar component.

For \(\Phi_c(a\oplus x)=a+c\tau(x)\) and \(W=1\oplus u\),

\[
 \Phi_c(W^r)=1\quad(r\ne0),\qquad \Phi_c(1)=1+c.
\]

After state normalization the nonzero moments are \(1/(1+c)\), not one.

## 2. Analytic and Fuglede--Kadison determinants

For \(|q|<1\), the analytic trace-log is

\[
 D_c(q)=\exp\!\left(-\sum_{r\geq1}\frac{q^r\Phi_c(W^r)}r\right)
       =\exp\!\left(-\sum_{r\geq1}\frac{q^r}r\right)=1-q.
\]

Consequently the Haar sector is exactly invisible to the same analytic
determinant. This identity persists atomwise for every positive inventory.
The distinct magnitude object is

\[
 \Delta_c(1-qW)=|1-q|\max(1,|q|)^c,
\]

by Jensen's formula; the normalized-trace version is its
\(1/(1+c)\)-th power. These two determinant conventions are not combined.

## 3. Finite cyclic approximants and perturbations

For
\(\mu_N=\delta_1+(c/N)\sum_{j=0}^{N-1}\delta_{e^{2\pi i j/N}}\),

\[
 \int u^r d\mu_N=1+c\,\mathbf1_{N\mid r},
 \qquad
 D_{c,N}(q)=(1-q)(1-q^N)^{c/N}.
\]

The first ledger leak is exactly \(r=N\), for every tested
\(N=2,\ldots,64\). For Haar density
\(1+2\varepsilon\cos(k\theta)\), \(|\varepsilon|\leq1/2\), the first leak is
at \(r=k\), and

\[
 D_{c,k,\varepsilon}(q)
 =(1-q)\exp(-c\varepsilon q^k/k).
\]

## 4. Adjoint and recurrent controls

The self-adjoint block
\(H=\begin{psmallmatrix}0&W\\W^*&0\end{psmallmatrix}\) satisfies \(H^2=I\).
Hence odd traces vanish but
\((\operatorname{Tr}_2\otimes\Phi_c)(H^{2r})=2(1+c)\): the hidden Haar mass
leaks already at power two.

For a two-edge recurrent word with independent formal coefficients \(x,y\),
the return word contains \(uu^{-1}=1\). Its full matrix trace coefficient is
\(2(1+c)xy\) (or \((1+c)xy\) per normalized vertex), so Fourier-nullity does
not erase balanced inverse words.

## Claim boundary

SD-C14 proves a unique infinite, nonnormalized positive moment escape. It also
proves that this escape is analytically determinant-invisible, fails under
state normalization, finite approximation, self-adjointization, and recurrent
inverse-word coupling, and is inventory-independent. It proves no target
divisor, completion, zero statement, RH implication, or Route-B operator.
