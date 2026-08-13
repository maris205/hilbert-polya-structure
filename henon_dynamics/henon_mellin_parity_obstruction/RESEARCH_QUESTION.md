# Research question

## Bold hypothesis

Can the infinite scaling orbit of the adelic H6 Poisson boundary be
diagonalized by Mellin transform into a genuine two-sign scattering symbol
whose determinant is reciprocal, unitary on the critical line, and harmless
to the Riemann divisor?

For

\[
P_6(u)=2u^3-u,
\qquad
\kappa_\pm(z)=\int_0^\infty e^{\pm2\pi iP_6(u)}u^{z-1}\,du,
\]

define

\[
K(z)=
\begin{pmatrix}
\kappa_+(z)&\kappa_-(z)\\
\kappa_-(z)&\kappa_+(z)
\end{pmatrix}.
\]

In the parity basis its eigen-symbols are

\[
A(z)=\kappa_+(z)+\kappa_-(z),
\qquad
B(z)=\frac{\kappa_+(z)-\kappa_-(z)}{i}.
\]

The natural formal scattering matrix is

\[
S_H(z)=K(1-z)K(z)^{-1}
=\operatorname{diag}\!\left(
\frac{A(1-z)}{A(z)},
\frac{B(1-z)}{B(z)}
\right).
\]

It automatically satisfies reciprocity and critical-line unitarity. The
decisive question is whether its divisor is compatible with the completed
Riemann zeta function.

## Decisive theorem

The even, zeta-relevant symbol has exactly one simple zero in the certified
disc of radius \(10^{-12}\) centered at

\[
z_0\approx
0.7286922241147174961
+1.6054479123346984864i,
\]

while \(A(1-z_0)B(z_0)B(1-z_0)\ne0\). Thus the unrenormalized parity
scattering candidate has an off-critical pole at \(z_0\) and an off-critical
zero at \(1-z_0\), together with their conjugates.

The mirror and odd factors, as well as the natural linear parent, are
certified nonzero on the required discs. Hence the unrenormalized candidate
is stopped. The next admissible escape is not fitted cancellation but a
different Hénon form: the homogeneous cubic, where the open question is a
Poisson-boundary anomaly or exact coboundary trivialization.
