# Derivation package

## 1. From the H\'enon boundary orbit to a Mellin matrix

C35 showed that dilation conjugates the cubic chirp through the family

\[
P_a(x)=2a^3x^3-ax=P_6(ax).
\]

The Poisson boundary coefficients are therefore functions of the dilation
parameter \(a>0\). Splitting a test function into its positive and negative
real half-lines and Mellin transforming in \(a\) gives the two kernels

\[
\kappa_\pm(z)=\int_0^\infty
 e^{\pm2\pi i(2u^3-u)}u^{z-1}\,du.
\]

The signs mix the two half-lines, so the natural matrix is

\[
K(z)=\begin{pmatrix}\kappa_+&\kappa_-\\\kappa_-&\kappa_+\end{pmatrix}.
\]

The fixed parity vectors \((1,1)\) and \((1,-1)\) diagonalize it. This is
why the even and odd symbols are forced rather than selected after seeing
their zeros.

## 2. Rotated-contour continuation

Write \(a=4\pi\), \(b=2\pi\). On rotating
\(u=e^{\sigma i\pi/6}r\), the cubic term becomes decaying:

\[
\kappa_\sigma(z)=e^{\sigma i\pi z/6}
\int_0^\infty
e^{-ar^3+b e^{-\sigma i\pi/3}r}r^{z-1}\,dr.
\]

Expanding the linear exponential yields an absolutely convergent series on
compact subsets away from the gamma poles,

\[
\kappa_\sigma(z)=
\frac{a^{-z/3}e^{\sigma i\pi z/6}}3
\sum_{m\ge0}
\frac{\left(b a^{-1/3}e^{-\sigma i\pi/3}\right)^m}{m!}
\Gamma\!\left(\frac{z+m}{3}\right).
\]

Grouping \(m\) modulo three gives the \({}_1F_2\) formula in the theorem
package. It is this grouped form that is evaluated with complex balls.

Integration by parts of
\(d(e^{\sigma i(au^3-bu)})/du\) gives

\[
3a\kappa_\sigma(z+3)-b\kappa_\sigma(z+1)
=\sigma iz\kappa_\sigma(z).
\]

Complex conjugation gives the second identity in T1.

## 3. Parity and formal scattering

Because the phase is odd,

\[
A(z)=2\int_0^\infty
\cos(2\pi P_6(u))u^{z-1}\,du,
\]

and

\[
B(z)=2\int_0^\infty
\sin(2\pi P_6(u))u^{z-1}\,du.
\]

The Taylor series of the cosine has only even powers of \(u\), while the
sine has only odd powers. This explains the even/odd pole split. In the
parity basis,

\[
K(z)=\operatorname{diag}(A(z),iB(z)),
\]

up to the fixed unnormalized parity basis convention, and hence

\[
K(1-z)K(z)^{-1}
=\operatorname{diag}\left(\frac{A(1-z)}{A(z)},
\frac{B(1-z)}{B(z)}\right).
\]

Reciprocity is algebraic. Critical-line unitarity follows from real-type
symmetry, not from a numerical zero pattern.

## 4. Exact local zero argument

Let

\[
c=\frac{7286922241147175}{10^{16}}
+i\frac{16054479123346985}{10^{16}},
\qquad r=10^{-12}.
\]

The producer evaluates the analytic continuation and its first derivative
at the exact rational center using Arb complex balls. It also evaluates the
three companion functions on the full input balls \(D\) and \(1-D\).

For the only global analytic estimate required by Rouch\'e, the rotated
contour gives

\[
\kappa_\sigma''(z)=
e^{\sigma i\pi z/6}
\int_0^\infty e^{-4\pi t^3+2\pi e^{-\sigma i\pi/3}t}
t^{z-1}\left(\log t+\frac{\sigma i\pi}{6}\right)^2dt.
\]

On \(D\), use

\[
\operatorname{Re}z>18/25,
\qquad |\operatorname{Im}z|<161/100,
\]

and the elementary inequalities

\[
\pi<22/7,
\quad e^\pi<24,
\quad e^{\pi(161/100)/6}<3.
\]

On \((0,1)\), discard the decaying cubic factor and bound the resulting
log-moment by 8. On \((1,\infty)\),
\(-4\pi t^3+\pi t\le-9t\) and the remaining weighted log-moment is below 1.
The prefactors then give less than 579 for each sign and hence

\[
\sup_D|A''|<1158<1200.
\]

Taylor's theorem with integral remainder now gives, on \(\partial D\),

\[
|A(z)-A'(c)(z-c)|
\le |A(c)|+\frac12\sup_D|A''|r^2.
\]

The certified rational inequality

\[
10^{-16}+600r^2<\frac25r
\]

lets Rouch\'e compare \(A\) with the linear function
\(A'(c)(z-c)\). The latter has one simple zero, so the former has one zero
counting multiplicity. It must therefore be simple.

## 5. Divisor consequence

The full-ball lower bounds for \(A(1-z)\), \(B(z)\), and \(B(1-z)\)
exclude every possible local numerator or odd-channel cancellation. Thus

\[
\operatorname{ord}_{D}\det S_H=-1,
\qquad
\operatorname{ord}_{1-D}\det S_H=+1.
\]

The discs are disjoint, lie inside the open strip, and avoid the critical
line. Conjugation produces a four-disc orbit. No information about a
Riemann zero is imported: direct Arb evaluation proves

\[
\inf_D\left|
\frac12z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z)
\right|>\frac9{20}.
\]

The functional equation transfers nonvanishing to \(1-D\). Thus the H\'enon
pole and mirror zero are certified additional divisor points relative to the
completed Riemann target.

## 6. Why the ordinary determinant inference fails independently

Let \(M_F\) be multiplication by a measurable matrix function \(F(t)\) on
\(L^2(\mathbb R,dt;\mathbb C^2)\). If \(F\ne0\) on a set of positive
measure, there are disjoint measurable subsets on which \(\|F\|\) is
uniformly positive. After restricting further, one fixed entry
\(|F_{ij}|\) is uniformly positive. Normalized indicator vectors on those
subsets, tensored with the fixed basis vector \(e_j\), form an orthonormal
sequence whose images under \(M_F\) do not converge to zero. Hence \(M_F\)
is not compact. Applying this to \(F=S_H-I\) rules out an
ordinary Fredholm determinant even before the divisor obstruction is used.

## 7. The large pivot

For the homogeneous phase \(P_0(u)=2u^3\), the Mellin integral is a single
gamma factor:

\[
\kappa_\sigma^{(0)}(z)=
\frac13(4\pi)^{-z/3}\Gamma(z/3)e^{\sigma i\pi z/6}.
\]

The unwanted strip divisor disappears because the linear term, which broke
exact scaling homogeneity, has disappeared. At the same time the phase
family is now an ambient scaling coboundary. Therefore the next question is
not another zero scan. It is whether passage through the Poisson boundary
quotient carries a genuine index that prevents the coboundary from being
removed. This is a single theorem-level fork: anomaly or closure.
