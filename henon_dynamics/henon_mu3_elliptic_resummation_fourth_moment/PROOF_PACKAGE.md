# HCS-C50 proof package

## 1. Automorphisms of the C48 curve

Work over \(K=\mathbf Q(\rho)\), \(\rho^2+\rho+1=0\), with

\[
f(x)=-\frac{x(\rho^2x-1)}{\rho(x^3+1)}.
\]

Direct reduction modulo \(\rho^2+\rho+1\) gives

\[
f(\rho^2/x)=-f(x).                                      \tag{1}
\]

For

\[
T(x)=-\frac{\rho^2(x+1)}{x+\rho^2},\qquad
h=\frac{\rho-1}{3},
\]

the same exact calculation gives

\[
T(T(x))=x,\qquad f(T(x))f(x)=h^3,                       \tag{2}
\]

and

\[
T(\rho^2/x)=\frac{\rho^2}{T(x)}.                        \tag{3}
\]

Equations (1)--(3) show that the maps \(\delta,\iota,\jmath\) in the
theorem package extend to automorphisms of the smooth projective curve.
They prove

\[
\delta^3=\iota^2=\jmath^2=1,\qquad
[\iota,\delta]=[\iota,\jmath]=1,\qquad
\jmath\delta\jmath=\delta^{-1}.
\]

The subgroup \(\langle\delta,\jmath\rangle\) is \(S_3\). Its base
transformations are only the identity and \(T\), whereas the central
involution \(\iota\) induces \(x\mapsto\rho^2/x\), which is distinct from
both. Thus the generated group has order twelve and is \(C_2\times S_3\).

## 2. Quotient genera and rational idempotents

The quotient by \(\delta\) is the \(x\)-line, so

\[
H^0(C,\Omega_C^1)^{\langle\delta\rangle}=0.              \tag{4}
\]

The fixed points of \(x\mapsto\rho^2/x\) are \(x=\rho\) and
\(x=-\rho\). The former is a zero branch of \(f\), and the latter is a
pole branch. Each has a unique point above it on the completed cubic
cover, giving exactly two fixed points of \(\iota\). Riemann--Hurwitz gives

\[
2g(C)-2=2\bigl(2g(C/\iota)-2\bigr)+2,\qquad
g(C/\iota)=2.                                           \tag{5}
\]

Among the rational irreducible representations of \(S_3\), only the
standard representation has no \(C_3\)-invariant vector. Equation (4) and
\(\dim H^0(C,\Omega_C^1)=4\) therefore force two standard copies. By (5),
the \(\iota\)-invariant subspace has dimension two, so the central
involution has one positive and one negative standard block:

\[
H^0(C,\Omega_C^1)=
\operatorname{Std}_{+}\oplus\operatorname{Std}_{-}.     \tag{6}
\]

The central factor
\[
e_{\mathrm{std}}=1-\frac{1+\delta+\delta^2}{3}
\]
selects the standard \(S_3\)-block. Multiplication by
\((1+\jmath)/2\) is a primitive rank-one idempotent in that
\(M_2(\mathbf Q)\)-block, and \((1\pm\iota)/2\) selects its central sign.
Thus each \(q_\pm\) from the theorem package acts with rank one on
differentials, and its connected Jacobian image \(E_\pm\) is elliptic.
The complementary primitive idempotent in each standard block has an
isogenous image: primitive idempotents in \(M_2(\mathbf Q)\) are equivalent,
and the off-diagonal matrix units, after clearing denominators, give
mutually inverse \(K\)-quasi-isogenies between their connected images.
Therefore

\[
\operatorname{Jac}(C)\sim_K E_+^2\times E_-^2.          \tag{7}
\]

All correspondences are \(K\)-rational because the three generating
automorphisms are \(K\)-rational.

## 3. Residual logarithm in the second-moment factor

Set \(u=2s+1\). From the exact second moment,

\[
\begin{aligned}
\log F_2(s)
&=\sum_{p\ {\rm split}}\frac{14+2a_p}{p-1}p^{-2s}\\
&=\sum_{p\ {\rm split}}(14+2a_p)p^{-u}
 +R_{\mathrm{den}}(s),                                 \tag{8}
\end{aligned}
\]

where

\[
R_{\mathrm{den}}(s)=
\sum_{p\ {\rm split}}(14+2a_p)p^{-u}
\sum_{j\ge1}p^{-j}.                                     \tag{9}
\]

At a split rational prime there are two primes of \(K\) of norm \(p\).
The two reductions of \(C\) are isomorphic, so the degree-one term in

\[
\log\!\left(\zeta_K(u)^7L(H^1(C/K),u)\right)
\]

is exactly \((14+2a_p)p^{-u}\). Define \(\log H_2\) on the original
absolute-convergence domain by subtracting this logarithm from (8).

The residual pieces are controlled as follows.

1. Since \(|a_p|\le8\sqrt p\), (9) is locally absolutely convergent for
   \(\Re u>1\).
2. At split primes, the \(m\ge2\) terms of the curve \(L\)-function have
   size \(O(p^{m/2}p^{-m\Re u})\); the first is summable for \(\Re u>1\).
3. At inert rational primes, \(N\mathfrak p=p^2\), so the first curve term
   is \(O(p^{1-2\Re u})\), again summable for \(\Re u>1\).
4. Ramified and bad primes form a finite set and contribute harmless
   nonvanishing local factors in this half-plane.

Thus \(\log H_2\) converges locally absolutely for \(\Re u>1\), and
\(H_2=\exp(\log H_2)\) is holomorphic and nonzero for \(\Re s>0\).
Equality first holds where all Euler products converge absolutely and then
continues by uniqueness.

## 4. Exact characteristic-zero smoothness certificate

Write

\[
\mathcal C=\sum_{i=0}^7x_i^3,\qquad
\mathcal Q=\sum_{i=0}^6x_ix_{i+1}+\rho x_7x_0.
\]

The quadratic form \(\mathcal Q\) is nondegenerate because its even--odd
block has determinant \(1-\rho\ne0\). At a projective singular point of
\(X=V(\mathcal C,\mathcal Q)\), the gradients are dependent:
\(\nabla\mathcal C=\lambda\nabla\mathcal Q\). The scalar \(\lambda\) is
nonzero, because \(\lambda=0\) would force every coordinate to vanish.
After the common scaling \(y_i=3x_i/\lambda\), and then renaming \(y_i\)
as \(x_i\), the gradient equations become

\[
\begin{aligned}
x_0^2&=x_1+\rho x_7,\\
x_i^2&=x_{i-1}+x_{i+1}\quad(1\le i\le6),\\
x_7^2&=x_6+\rho x_0.                                   \tag{10}
\end{aligned}
\]

Multiplying the \(i\)-th equation by \(x_i\) and summing gives

\[
\mathcal C(x)=2\mathcal Q(x).                           \tag{11}
\]

It therefore suffices to adjoin \(\mathcal Q=0\), because (11) then forces
\(\mathcal C=0\). The frozen exact Singular calculation is:

~~~singular
ring R=0,(x0,x1,x2,x3,x4,x5,x6,x7,r),dp;
option(redSB);
poly Q=x0*x1+x1*x2+x2*x3+x3*x4+x4*x5+x5*x6+x6*x7+r*x7*x0;
ideal I=x0^2-x1-r*x7,
  x1^2-x0-x2,
  x2^2-x1-x3,
  x3^2-x2-x4,
  x4^2-x3-x5,
  x5^2-x4-x6,
  x6^2-x5-x7,
  x7^2-x6-r*x0,
  Q,
  r^2+r+1;
std(I);
~~~

With Singular's **dp** degree-reverse-lexicographic order and the reduced
standard-basis option, a local replay with Singular 4.2.1 returns exactly

~~~text
x7,
x6,
x5,
x4,
x3,
x2,
x1,
x0,
r^2+r+1
~~~

Hence the only affine recurrence solution above either root of
\(r^2+r+1\) is the origin. There is no projective singular point, so
\(X/K\) is smooth. This exact basis, rather than generic openness, proves
characteristic-zero smoothness. Openness is used only afterward to conclude
that the bad reductions form a finite set.

## 5. Exact bad-prime witness

At \(p=181\), \(\rho=48\), the vector

\[
v=(9,158,158,9,104,128,171,153)
\]

satisfies all eight equations in (10), together with

\[
\mathcal Q(v)=0,\qquad \mathcal C(v)=0
\quad\text{in }\mathbf F_{181}.
\]

It is nonzero, so it represents a projective singular point of the
reduction. The alternative recurrence
\(3y_i^2=\partial_i\mathcal Q(y)\) is related to (10) by a common scaling
in characteristic different from three; the project uses the
coefficient-one normalization throughout.

## 6. Betti numbers and the fourth moment

For the cubic sixfold,

\[
c(TS)=\frac{(1+H)^8}{1+3H}.
\]

The coefficient of \(H^6\) is \(31\), and \(\deg S=3\), so

\[
\chi(S)=93,\qquad b_6(S)=87,\qquad
b_6^{\mathrm{prim}}(S)=86.                             \tag{12}
\]

For a smooth \((2,3)\) fivefold,

\[
c(TX)=\frac{(1+H)^8}{(1+2H)(1+3H)}.
\]

The coefficient of \(H^5\) is \(-27\), and \(\deg X=6\), so

\[
\chi(X)=-162=6-b_5(X),\qquad b_5(X)=168.                \tag{13}
\]

Weak Lefschetz supplies the six nonmiddle even Tate classes in each
calculation. Deligne purity gives

\[
|A_p|\le86p^3,\qquad |B_p|\le168p^{5/2}.
\]

Substitution into the projective direction identity gives the exact
\(Z_{p,4}\), \(C_{p,4}\), and \(c_{p,4}\) formulas before any estimate is
applied.

## 7. Normal convergence and determinant identity

After replacing the \(n=2\) logarithm by its continued factor, the remaining
thresholds are

\[
n=1:0,\qquad n=3:1/6,\qquad n=4:1/8,\qquad n\ge5:1/n.
\]

Fix \(\sigma_0>1/5\). For all sufficiently large primes choose the cutoff
so that \(4p^{-\sigma_0}\le1/2\). The inherited estimate then bounds the
large-prime \(n\ge5\) tail by a constant multiple of

\[
\sum_p p^{-5\sigma_0}<\infty.
\]

For the finitely many remaining primes, the inherited unitary-block bound
\(|c_{p,n}|\le\tau_p(I)\), together with \(p^{-\sigma_0}<1\), makes each
local logarithmic tail converge geometrically. This proves local normal
convergence on \(\Re s>1/5\).

The criterion

\[
X_s\in L^q(\mathcal M,\tau)\Longleftrightarrow q\Re s>2
\]

puts \(X_s\) in \(L^{10}(\mathcal M,\tau)\) throughout this half-plane.
Regularization removes powers \(1,\ldots,9\); restoring the eight
counterterms other than \(n=2\), and replacing the latter by \(F_2^{\rm
cont}\), gives the exact determinant formula. The ordinary Hilbert direct
sum instead satisfies \(X_s\in S^q\Longleftrightarrow q\Re s>3\), which
forces order \(15\) and records the unnormalized Galois norm.
