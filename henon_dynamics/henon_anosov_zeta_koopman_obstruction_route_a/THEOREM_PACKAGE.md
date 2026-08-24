# Exact theorem package — C125

Let \(T_A:\mathbb T^2\to\mathbb T^2\) be induced by

\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix}\in SL(2,\mathbb Z).
\]

## Proposition 1 — complete all-period orbit census

The eigenvalues are

\[
\lambda_\pm=\frac{3\pm\sqrt5}{2},\qquad
\lambda_+>1,\quad 0<\lambda_-<1,
\]

so \(A^n-I\) is nonsingular for every \(n\geq1\).  Its torus kernel has
cardinality \(|\det(A^n-I)|\); hence

\[
N_n:=\#\operatorname{Fix}(T_A^n)
=|\det(A^n-I)|=S_n-2,
\]

where \(S_n=\operatorname{tr}(A^n)\) satisfies

\[
S_0=2,\qquad S_1=3,\qquad S_n=3S_{n-1}-S_{n-2}.
\]

If \(P_n\) is the number of points of exact least period \(n\), then

\[
P_n=\sum_{d\mid n}\mu(n/d)N_d,
\qquad O_n=P_n/n
\]

is the number of primitive orbits.  This is an all-order theorem, not an
orbit-search extrapolation.

## Proposition 2 — exact Artin--Mazur zeta

With the unweighted convention,

\[
\zeta_T(z)=\exp\!\left(\sum_{n\geq1}\frac{N_nz^n}{n}\right)
=\prod_{\gamma\ \mathrm{primitive}}(1-z^{|\gamma|})^{-1}.
\]

Because \(N_n=\lambda_+^n+\lambda_-^n-2\) and
\(\lambda_+\lambda_-=1\),

\[
\boxed{\displaystyle
\zeta_T(z)=\frac{(1-z)^2}{(1-\lambda_+z)(1-\lambda_-z)}
=\frac{(1-z)^2}{1-3z+z^2}.}
\]

The identity holds as a formal series at zero and as the displayed rational
meromorphic function.  It is not a target-divisor theorem.

## Proposition 3 — natural Koopman obstruction

Let \(U:L^2(\mathbb T^2)\to L^2(\mathbb T^2)\) be
\((Uf)(x)=f(T_Ax)\).  Haar invariance makes \(U\) unitary.  For
\(e_k(x)=e^{2\pi i k\cdot x}\),

\[
Ue_k=e_{A^{\mathsf T}k}.
\]

Since \(A^{\mathsf T}\) bijects \(\mathbb Z^2\), this is an infinite
permutation of an orthonormal basis.  More directly, \(e_{(j,0)}\) is a
bounded orthonormal sequence and its image \(e_{(2j,j)}\) is again
orthonormal, hence has no norm-convergent subsequence.  Thus \(U\) is not
compact, belongs to no finite Schatten class, is not trace class, and has no
ordinary trace-class Fredholm determinant \(\det(I-zU)\).  In particular,
the rational orbit zeta above is not identified with such a determinant.

## Proposition 4 — exact negative controls

For the parabolic shear
\(B=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\),
\(B^n-I\) is singular and \(\operatorname{Fix}(T_B^n)\) is a union of
\(n\) circles, so the finite fixed-point convention fails.  For the frozen
hyperbolic matrix, \(\det(A^n-I)=-N_n\); deleting the absolute value yields
signed Lefschetz data, not cardinalities.  Finally, replacing Fourier indices
by \((\mathbb Z/m\mathbb Z)^2\) gives modulus-dependent pseudo-traces, for
example at \(n=3\) the values for \(m=2,3,4,5\) are \(4,1,16,1\).

The canonical Route-A result is

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)
overall = ROUTE_A_EXPLORATORY
route_b_invocation_allowed = false
```
