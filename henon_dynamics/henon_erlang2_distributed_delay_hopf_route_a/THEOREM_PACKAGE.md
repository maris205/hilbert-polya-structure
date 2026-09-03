# Proof Package

## Frozen claim

Let \(a,b\geq0\), \(r>0\), and

\[
K_r(s)=r^2s e^{-rs}\mathbf 1_{s\geq0}.
\]

For a compatible fading-memory history define

\[
z_1(t)=\int_0^\infty r e^{-rs}x(t-s)\,ds,\qquad
z_2(t)=\int_0^\infty K_r(s)x(t-s)\,ds .
\]

Then

\[
\dot x=-ax-bz_2,\qquad
\dot z_1=r(x-z_1),\qquad
\dot z_2=r(z_1-z_2)                                      \tag{1}
\]

is exactly equivalent to

\[
\dot x(t)=-ax(t)-b\int_0^\infty K_r(s)x(t-s)\,ds.         \tag{2}
\]

Writing

\[
M=\begin{pmatrix}-a&0&-b\\r&-r&0\\0&r&-r\end{pmatrix},
\qquad
p(\lambda)=\det(\lambda I-M)
          =(\lambda+a)(\lambda+r)^2+br^2,
\]

the following atlas is complete.

1. For \(b>0\), exponential stability holds exactly when
   \[
   0<b<b_H,\qquad b_H=\frac{2(a+r)^2}{r}.
   \]
   At \(b=b_H\),
   \[
   p(\lambda)=(\lambda+a+2r)(\lambda^2+r(r+2a)),
   \]
   so the conjugate pair is \(\lambda_\pm=\pm i\omega_H\), with
   \(\omega_H=\sqrt{r(r+2a)}\), and the remaining root is \(-a-2r\).
   The pair crosses from left to right as \(b\) increases:
   \[
   \operatorname{Re}\lambda_+'(b_H)
   =\frac{r^2}{2\{r(r+2a)+(a+2r)^2\}}>0.
   \]
   For \(b>b_H\) there are exactly two roots in the open right half-plane.
2. At \(b=0\), \(p=(\lambda+a)(\lambda+r)^2\).  If \(a\ne r\), the
   \(-r\) root has one Jordan block of size two and \(-a\) is simple.  If
   \(a=r\), there is one size-three block at \(-r\).  Thus \(b=0,a>0\)
   remains exponentially stable, whereas \(a=b=0\) has a constant mode
   and a size-two block at \(-r\).
3. The only other repeated-root face in the admissible parameter domain is
   \[
   0\leq a<r,\qquad
   b=b_D=\frac{4(r-a)^3}{27r^2}>0.
   \]
   There the double root and simple root are
   \[
   \mu=-\frac{r+2a}{3},\qquad
   \nu=-\frac{4r-a}{3},
   \]
   and the Jordan sizes are \(2+1\).  This defective face lies strictly
   inside the stable region.
4. For distinct roots \(\lambda_j\),
   \[
   e^{tM}=\sum_{j=1}^3 e^{t\lambda_j}
   \prod_{k\ne j}\frac{M-\lambda_kI}{\lambda_j-\lambda_k}.
   \]
   On a double face \(p=(\lambda-\mu)^2(\lambda-\nu)\),
   \[
   e^{tM}=e^{\mu t}(P_\mu+tN_\mu)+e^{\nu t}P_\nu,
   \]
   where \(P_\nu=(M-\mu I)^2/(\nu-\mu)^2\),
   \(P_\mu=I-P_\nu\), and \(N_\mu=(M-\mu I)P_\mu\).
   At \(a=r,b=0\), writing \(N=M+rI\), one has
   \(e^{tM}=e^{-rt}(I+tN+t^2N^2/2)\).

The imaginary crossing is a theorem about this linear family.  No nonlinear
equation has been specified, so no nonlinear periodic orbit or Hopf branch is
asserted.

## Proof

### Linear-chain equivalence

The kernel has unit mass and Laplace transform
\(\widehat K_r(\lambda)=r^2/(\lambda+r)^2\).  Differentiation under the
integral followed by integration by parts gives
\(\dot z_1=r(x-z_1)\) and \(\dot z_2=r(z_1-z_2)\).  Substitution gives
(1).  Conversely, uniqueness of the two stable first-order filters shows
that a solution of (1) whose initial \(z_1,z_2\) equal the displayed history
integrals retains those convolution identities and therefore solves (2).
This converse is deliberately limited to compatible initialization.

### Routh boundary and crossing

Expanding \(p\) gives

\[
p(\lambda)=\lambda^3+c_2\lambda^2+c_1\lambda+c_0,
\quad
c_2=a+2r,\quad c_1=r(r+2a),\quad c_0=r^2(a+b).
\]

For \(b>0\) all three coefficients are positive.  The remaining cubic
Routh--Hurwitz condition is

\[
c_2c_1-c_0=r\{2(a+r)^2-br\}>0,
\]

which is exactly \(b<b_H\).  At equality, direct multiplication gives the
factorization above.  Implicit differentiation of \(p(\lambda,b)=0\) at
\(\lambda=i\omega_H\) gives the stated positive real part.  For
\(b>b_H\), the first Routh column has signs \(+,+,-,+\), hence exactly two
right-half-plane roots.

### Exhaustion of repeated roots and Jordan type

\[
p'(\lambda)=(\lambda+r)(3\lambda+r+2a).
\]

The first critical root, \(-r\), is a root of \(p\) exactly when \(b=0\).
The second, \(-(r+2a)/3\), is a root exactly when
\(b=4(r-a)^3/(27r^2)\); positivity requires \(a<r\).  Equivalently,

\[
\operatorname{disc}p
=br^2\{4(r-a)^3-27br^2\},
\]

so no repeated face has been omitted.  Finally
\[
\det[e_1,Me_1,M^2e_1]=r^3\ne0.
\]
Thus \(M\) is cyclic and its minimal polynomial equals \(p\); every repeated
root has a single Jordan block of its algebraic multiplicity.  The
projector formulas are the Lagrange and Hermite interpolation formulas
modulo this minimal polynomial.

## Boundary atlas

- \(a=0,b>0\): stable for \(0<b<2r\), imaginary pair at \(b=2r\), and
  two right-half-plane roots for \(b>2r\).
- \(a=b=0\): the \(x\)-mode is constant; memory transients include
  \(t e^{-rt}\).
- \(b=0,a>0\): exponentially stable even though the \(-r\) block is
  defective.
- \(a=r,b=0\): the whole cubic is \((\lambda+r)^3\), with one block.
- \(r=0\): excluded because \(K_r\) is no longer the normalized Erlang
  density.
- \(r\to\infty\): for bounded spectral parameter,
  \(r^2/(\lambda+r)^2\to1\), so the slow limiting rate is \(-(a+b)\);
  this is a singular limiting observation, not an extra finite-\(r\)
  theorem.

## Status and risk

**PROVABLE AS STATED.**  The principal residual risk is terminological:
“Hopf boundary” means a simple transverse imaginary spectral crossing, not
a nonlinear Hopf-bifurcation theorem.  Exact finite evidence is a receipt;
the continuum parameter result follows from the analytic proof.
