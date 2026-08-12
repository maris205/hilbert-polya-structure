# Theorem package

## Frozen object and conventions

Let

\[
P_6(u)=2u^3-u
\]

be the generating-function phase of the area-preserving H\'enon map

\[
H_6(q,p)=(1-6q^2-p,q).
\]

For \(\sigma\in\{+1,-1\}\), define initially as an oscillatory Mellin
integral

\[
\kappa_\sigma(z)
=\int_0^\infty
 \exp\!\bigl(\sigma 2\pi iP_6(u)\bigr)u^{z-1}\,du.
\]

Put

\[
K(z)=
\begin{pmatrix}
\kappa_+(z)&\kappa_-(z)\\
\kappa_-(z)&\kappa_+(z)
\end{pmatrix},
\qquad
A(z)=\kappa_+(z)+\kappa_-(z),
\qquad
B(z)=\frac{\kappa_+(z)-\kappa_-(z)}{i}.
\]

No Riemann-zero table, fitted affine spectral map, or post hoc divisor is
allowed.

## T1. Meromorphic continuation of the cubic Mellin symbols

Let

\[
\lambda=\frac{2\pi}{(4\pi)^{1/3}},
\qquad X=-\frac{2\pi^2}{27}.
\]

Rotating the ray by \(u=e^{\sigma i\pi/6}r\) gives the meromorphic
continuation

\[
\begin{aligned}
\kappa_\sigma(z)
=\frac{(4\pi)^{-z/3}e^{\sigma i\pi z/6}}{3}
\Bigg[&
\Gamma\!\left(\frac z3\right)
{}_1F_2\!\left(\frac z3;\frac13,\frac23;X\right)\\
&+\lambda e^{-\sigma i\pi/3}
\Gamma\!\left(\frac{z+1}{3}\right)
{}_1F_2\!\left(\frac{z+1}{3};\frac23,\frac43;X\right)\\
&+\frac{\lambda^2e^{-2\sigma i\pi/3}}2
\Gamma\!\left(\frac{z+2}{3}\right)
{}_1F_2\!\left(\frac{z+2}{3};\frac43,\frac53;X\right)
\Bigg].
\end{aligned}
\]

It obeys

\[
12\pi\kappa_\sigma(z+3)-2\pi\kappa_\sigma(z+1)
=\sigma iz\kappa_\sigma(z)
\]

and

\[
\kappa_-(z)=\overline{\kappa_+(\overline z)}.
\]

Consequently \(A\) and \(B\) are real-type meromorphic functions. Their
polar sets split by parity: \(A\) can have poles only at
\(0,-2,-4,\ldots\), while \(B\) can have poles only at
\(-1,-3,-5,\ldots\).

## T2. Natural parity scattering symmetry

Where \(K(z)\) is invertible, define the formal two-channel symbol

\[
S_H(z)=K(1-z)K(z)^{-1}.
\]

In the parity basis,

\[
S_H(z)=\operatorname{diag}\!\left(
\frac{A(1-z)}{A(z)},
\frac{B(1-z)}{B(z)}
\right).
\]

It follows identically that

\[
S_H(z)S_H(1-z)=I.
\]

Because \(A\) and \(B\) are real-type, \(1-z=\overline z\) on
\(\operatorname{Re}z=1/2\). Hence, away from its divisor,

\[
S_H(1/2+it)^*S_H(1/2+it)=I.
\]

This is an exact functional-equation and critical-line-unitarity theorem for
the symbol. It is not yet an operator-scattering construction.

## T3. Certified off-critical zero

Let

\[
c=
0.7286922241147175
+1.6054479123346985i,
\qquad r=10^{-12},
\qquad D=\{z:|z-c|\le r\}.
\]

Complex-ball evaluation of the hypergeometric continuation proves

\[
|A(c)|<10^{-16},
\qquad
|A'(c)|>\frac25.
\]

The rotated-contour majorant proves

\[
\sup_{z\in D}|A''(z)|<1200.
\]

Thus on \(\partial D\),

\[
|A(c)|+\frac12\sup_D|A''|r^2
<10^{-16}+600\cdot10^{-24}
<\frac25\,10^{-12}
\le |A'(c)(z-c)|.
\]

Rouch\'e's theorem therefore gives exactly one zero of \(A\), counted with
multiplicity, in \(D\). It is simple. Moreover,

\[
D\subset\{0<\operatorname{Re}z<1\},
\qquad
D\cap\{\operatorname{Re}z=1/2\}=\varnothing.
\]

This is a certified local statement, not a global census of strip zeros.

## T4. Certified no-cancellation gate

On the full complex balls \(D\) and \(1-D\), interval evaluation proves

\[
\inf_{z\in D}|B(z)|>\frac45,
\qquad
\inf_{z\in D}|A(1-z)|>\frac3{10},
\qquad
\inf_{z\in D}|B(1-z)|>\frac{13}{10}.
\]

For the completed Riemann function

\[
\xi(z)=\frac12z(z-1)\pi^{-z/2}\Gamma(z/2)\zeta(z),
\]

the same complex-ball calculation proves

\[
\inf_{z\in D}|\xi(z)|>\frac9{20}.
\]

Therefore the unique zero of \(A\) in \(D\) is not cancelled in

\[
\det S_H(z)=
\frac{A(1-z)B(1-z)}{A(z)B(z)}.
\]

The determinant has one pole in \(D\) and one zero in \(1-D\), counted with
multiplicity. Real-type symmetry supplies the conjugate pole and zero.
All four points lie in the open critical strip and off the critical line.
Since \(\xi\) is nonzero on \(D\), and \(\xi(z)=\xi(1-z)\), these are
certified additional divisor points rather than untested collisions with the
target Riemann divisor. No Riemann-zero table is used.

## T5. The natural linear parent does not cancel the divisor

For the linear phase \(P_{\mathrm{lin}}(u)=-u\), the even symbol is

\[
A_{\mathrm{lin}}(z)
=2(2\pi)^{-z}\Gamma(z)\cos\!\left(\frac{\pi z}{2}\right).
\]

Its complex-ball image on \(D\) is bounded away from zero by \(7/10\).
Its divisor is also explicit and contains no nonreal point of \(D\). Thus
the natural linear scaling parent supplies no structural cancellation of the
H\'enon zero. Dividing by a fitted factor having that zero is excluded by the
frozen protocol.

## T6. Ordinary Fredholm realization is unavailable

After Mellin diagonalization, \(S_H(1/2+it)-I\) is a matrix-valued
multiplication operator on a non-atomic \(L^2\) space. A multiplication
operator on such a space is compact only when its matrix symbol vanishes
almost everywhere. Consequently a nontrivial \(S_H-I\) is not trace class,
and the pointwise \(2\times2\) determinant above is not an ordinary global
Fredholm determinant.

A Birman--Krein determinant would require a separately constructed pair
with trace-class resolvent difference. A crossed-product or semifinite
determinant would require a specified algebra and trace. Neither is supplied
by the formal multiplier alone.

## Main obstruction theorem

The unrenormalized H6 Mellin--parity symbol simultaneously possesses exact
reciprocity and critical-line unitarity, yet its zeta-relevant even channel
creates a certified off-critical divisor in the open critical strip.
Therefore

\[
\boxed{
\text{reciprocity + critical-line unitarity does not imply an
RH-compatible divisor.}
}
\]

The concrete candidate is rejected at Route-A gates A2 and A3. The result is
a no-go theorem for this candidate, not for every H\'enon deformation.

## Homogeneous pivot theorem and open anomaly gate

Remove the inhomogeneous term and consider

\[
H_0(q,p)=(-6q^2-p,q),
\qquad P_0(q)=2q^3.
\]

Then

\[
\kappa_\pm^{(0)}(z)
=\frac13(4\pi)^{-z/3}
\Gamma\!\left(\frac z3\right)e^{\pm i\pi z/6},
\]

so its parity symbols are gamma times
\(\cos(\pi z/6)\) and \(\sin(\pi z/6)\). They have no zero or pole in
\(0<\operatorname{Re}z<1\).

This is not yet a positive Route-A construction. The homogeneous scaling
cocycle is an ambient coboundary. The next large gate is therefore exact:
does the Poisson boundary quotient turn this removable ambient cocycle into
a nontrivial index or anomaly? A positive answer must construct the quotient
operator and its determinant intrinsically; a negative answer closes the
polynomial-chirp adelic branch at its most symmetric point.
