# Exact theorem package — C121

Let

\[
H(x,y)=(x^2-4-y,x).
\]

## Proposition 1 — birational projective geometry

The affine inverse is

\[
H^{-1}(x,y)=(y,y^2-4-x).
\]

The forward and inverse projective extensions are

\[
\bar H[X:Y:Z]=[X^2-4Z^2-YZ:XZ:Z^2],
\]

\[
\bar H^{-1}[X:Y:Z]=[YZ:Y^2-4Z^2-XZ:Z^2].
\]

Their indeterminacy points are respectively
\(I_+=[0:1:0]\) and \(I_-=[1:0:0]\).  The line \(Z=0\), away from
\(I_+\), is contracted to \(I_-\), while \(\bar H(I_-)=I_-\).  Since the
affine map is an automorphism and has no affine exceptional curve, the line
at infinity is the only exceptional curve and its orbit never reaches the
forward indeterminacy point.

## Proposition 2 — all-order algebraic stability

Set \(p_{-1}=y\), \(p_0=x\), and

\[
p_n=p_{n-1}^2-4-p_{n-2}.
\]

Then \(H^n=(p_n,p_{n-1})\).  For every \(n\geq1\), \(p_n\) has degree
\(2^n\) and unique leading homogeneous term \(x^{2^n}\), whereas
\(p_{n-1}\) has degree \(2^{n-1}\).  Indeed, squaring the monic leading term
of \(p_{n-1}\) produces degree \(2^n\), and both subtracted terms have
strictly lower degree.

After homogenization to degree \(d=2^n\), the first coordinate contains
\(X^d\) and is not divisible by \(Z\); the third coordinate is \(Z^d\), and
the second contains the factor \(Z^{d/2}\).  The three coordinates therefore
have gcd one.  Hence

\[
\deg(\bar H^n)=2^n=(\deg\bar H)^n
\]

for every \(n\geq1\): the projective map is algebraically stable.  Its first
algebraic dynamical degree is

\[
\lambda_1(\bar H)=\lim_{n\to\infty}\deg(\bar H^n)^{1/n}=2.
\]

This is an algebraic degree-growth statement only, not an entropy theorem.

## Proposition 3 — exact low-period witnesses

At a fixed point, \(x=y=q\) and \(q^2-2q-4=0\), so the two fixed points are

\[
(1+\sqrt5,1+\sqrt5),\qquad(1-\sqrt5,1-\sqrt5).
\]

Moreover,

\[
(0,-2)\longmapsto(-2,0)\longmapsto(0,-2)
\]

is primitive because its points are distinct.  With
\(B(x)=\begin{psmallmatrix}2x&-1\\1&0\end{psmallmatrix}\), the monodromy
based at \((0,-2)\) is

\[
B(-2)B(0)=\begin{pmatrix}-1&4\\0&-1\end{pmatrix}.
\]

It has trace \(-2\), determinant \(1\), and

\[
\det(I-zB(-2)B(0))=(1+z)^2.
\]

For the family \(H_c(x,y)=(x^2+c-y,x)\), each transition of this same
candidate cycle has first-coordinate residual \(c+4\).  Thus controls
\(c=-3\) and \(c=-5\) have residuals \(+1\) and \(-1\), respectively, and
do not preserve the frozen witness.

These results do not constitute a complete orbit atlas or a prime-like target
correspondence.  They construct neither a weighted dynamical zeta/target
divisor nor an analytic bridge.  Under the repository Route-A evaluator, the
canonical outcome is therefore

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_EXPLORATORY
```
