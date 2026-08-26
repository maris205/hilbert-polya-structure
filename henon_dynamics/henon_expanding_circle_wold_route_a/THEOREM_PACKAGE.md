# C177 theorem package

## Assumptions

Let \(b\ge2\) be an integer, let \(\mathbb T=\mathbb R/\mathbb Z\), and set
\[
T_b(x)=bx\pmod1,
\qquad U_bf=f\circ T_b
\]
on normalized Haar \(L^2(\mathbb T)\). Write \(e_m(x)=e^{2\pi imx}\).

## All-parameter theorem

For every integer \(b\ge2\) and \(n\ge1\):

1. The fixed points of \(T_b^n\) are exactly \(j/(b^n-1)\), \(0\le j<b^n-1\). Hence
   \[
   F_b(n)=b^n-1,
   \quad P_b(n)=\sum_{d\mid n}\mu(n/d)(b^d-1),
   \quad C_b(n)=P_b(n)/n.
   \]
   Here \(P_b(n)\) counts exact-period points and \(C_b(n)\) primitive cycles.
2. The Artin--Mazur zeta and its primitive-cycle product are
   \[
   \zeta_{AM,b}(z)=\exp\!\left(\sum_{n\ge1}\frac{(b^n-1)z^n}{n}\right)
   =\frac{1-z}{1-bz}
   =\prod_{n\ge1}(1-z^n)^{-C_b(n)}.
   \]
3. The exact Fourier action is \(U_be_m=e_{bm}\), and
   \[
   L^2(\mathbb T)=\mathbb C1\oplus
   \bigoplus_{\substack{r\in\mathbb Z\setminus\{0\}\\b\nmid r}}
   \overline{\operatorname{span}}\{e_{rb^j}:j\ge0\}.
   \]
   Each nonconstant summand is a unilateral shift. Thus \(U_b\simeq1\oplus S^{(\aleph_0)}\), its spectrum is the closed unit disk, and its only eigenvalue is \(1\) on constants.
4. The Perron adjoint satisfies
   \[
   U_b^*e_m=\begin{cases}e_{m/b},&b\mid m,\\0,&b\nmid m.\end{cases}
   \]
   The Koopman operator is a proper isometry, noncompact, in no finite Schatten class, and \(\det(I-zU_b)\) is not an ordinary Fredholm determinant for \(z\ne0\).
5. For \(s\ge0\), mean-zero \(f\in\dot H^s\), and \(g\in L^2\),
   \[
   |\langle f,U_b^ng\rangle|
   \le b^{-ns}\|f\|_{\dot H^s}\|g\|_2.
   \]
   For \(s>0\) the factor is sharp: \(f=e_{b^n}\), \(g=e_1\) gives equality after normalization.

## Proof

The equation \(T_b^n(x)=x\) is \((b^n-1)x=0\) in \(\mathbb T\), whose kernel is the displayed cyclic grid. Exact-period counts follow from \(F_b(n)=\sum_{d\mid n}P_b(d)\) and Möbius inversion; periodic points split into cycles, proving \(n\mid P_b(n)\). Expanding the two logarithms gives the rational zeta. The standard coefficientwise orbit decomposition gives the product.

Substitution gives \(U_be_m=e_{bm}\). Every nonzero integer has a unique representation \(m=rb^j\) with \(b\nmid r\), so the displayed subspaces are mutually orthogonal, exhaustive, and shifted forward by \(U_b\). Constants are fixed. This proves the Wold decomposition and also that the range omits, for example, \(e_1\). The basis inner products give the adjoint formula.

An isometry carrying an infinite orthonormal sequence to another cannot be compact. Its nonzero singular values are all one, so no finite Schatten membership and no trace-class perturbation \(zU_b\) exist for \(z\ne0\).

Finally, with \(\widehat f(0)=0\),
\[
\langle f,U_b^ng\rangle
=\sum_{m\ne0}\overline{\widehat f(b^nm)}\widehat g(m).
\]
Insert \(|b^nm|^s\), use \(|m|^{-s}\le1\), and apply Cauchy--Schwarz. This gives the stated \(b^{-ns}\) factor. The one-mode pair proves sharpness.

## Boundaries and Route-A decision

The case \(b=1\) is excluded: the identity has infinite fixed sets and no ordinary Artin--Mazur zeta. Negative or noninteger slopes are outside the frozen family. Prime and composite \(b\) obey identical degree-only formulas. The inverse-limit extension is a unitary dilation on a different phase space, not a quantization of this endomorphism.

The v0.2 tuple is `(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)`, overall `ROUTE_A_REJECTED`, Route B false. A1 is weak because the primitive ledger is complete; A0 fails because it carries no intrinsic arithmetic or prime correspondence.
