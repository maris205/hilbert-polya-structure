# HCS-C27 theorem package: fixed-prime finite-Weil AGY determinants

## Material passport

- **Candidate:** HCS-C27, the source-locked AGY return system with the full
  finite Weil fibre over an odd prime.
- **Date:** 2026-08-10.
- **Analytic input:** the common Bergman domain, scalar trace-class operator,
  and Perron trace formula proved in HCS-C26.
- **Exact source input:** the frozen C24, C25, and C26 certificates listed in
  results/c27_certificate.json.
- **New theorem-level output:** for every fixed odd prime \(p\), the
  chronology-preserving finite-Weil twist is an ordinary trace-class
  holomorphic family with a Fredholm determinant and exact periodic atoms.
- **New arithmetic theorem:** away from
  \(D_g=\det(I-g)\), its fibre trace is
  \(\left(\frac{D_g}{p}\right)\).
- **New exact obstructions:** a complete \(p=43\) finite-Weil
  fibre-polynomial collision, and an integral symplectic conjugacy collapsing
  an all-prime, all-repetition symbolic pair.
- **Finite evidence:** 150 source-locked AGY branches have 150 distinct
  discriminants, characteristic polynomials, and 24-prime Legendre
  signatures. This is not an all-length theorem.

The labels **proved**, **exact finite certificate**, and **finite evidence**
are kept separate below. This document contains no Route-A score.

## 1. Source lock and the two chronological orders

The C25 fixed-fibre source frame, inherited by C26 at its base state, has
the unimodular alternating form

\[
J_0=
\begin{pmatrix}
0&-1&0&0\\
1&0&-1&1\\
0&1&0&-1\\
0&-1&1&0
\end{pmatrix}.
\tag{1.1}
\]

The released fixed-fibre homology matrices satisfy

\[
g_e^T J_0 g_e=J_0,
\qquad
g_e\in\operatorname{SL}(4,\mathbb Z).
\tag{1.2}
\]

An integral Darboux change of basis is

\[
T=
\begin{pmatrix}
1&1&0&1\\
0&0&-1&0\\
0&1&0&0\\
0&0&0&-1
\end{pmatrix},
\quad
\det T=-1,
\quad
T^T J_0T=
\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix}.
\tag{1.3}
\]

Thus reduction modulo every odd prime gives a genuine element of
\(\operatorname{Sp}(4,\mathbb F_p)\).

If

\[
\boldsymbol\beta=(\beta_1,\ldots,\beta_n)
\]

is the **forward Rauzy order**, the C25 convention is

\[
g_{\mathrm{fwd}}(\boldsymbol\beta)
=g_{\beta_n}\cdots g_{\beta_1};
\tag{1.4}
\]

later edges multiply on the left. The corresponding transfer-operator
factor order is contravariant:

\[
(\gamma_1,\ldots,\gamma_n)
=(\beta_n,\ldots,\beta_1).
\tag{1.5}
\]

Both orders will always be displayed when a periodic atom is formed. No
averaged transition matrix or commutative surrogate is used. In particular,
the scalar inverse-branch matrix \(A_\beta=B_\beta^T\) is not substituted
for the forward homology cocycle \(g_\beta\).

## 2. Finite Heisenberg and Weil conventions

Fix an odd prime \(p\), put \(X=\mathbb F_p^2\), and write

\[
V=X\oplus X^\vee,
\qquad
J=\begin{pmatrix}0&I_2\\-I_2&0\end{pmatrix}.
\]

For \(v=(x,\xi)\) and \(w=(y,\eta)\), freeze

\[
\omega(v,w)=v^TJw=x^T\eta-\xi^Ty,
\qquad
\psi_p(a)=\exp(2\pi i\widetilde a/p).
\tag{2.1}
\]

The Heisenberg multiplication and Schrödinger Weyl operators are

\[
(v,z)(w,z')
=\left(v+w,z+z'+\frac12\omega(v,w)\right),
\tag{2.2}
\]

\[
[\pi_p(x,\xi)f](t)
=\psi_p\!\left(\xi^T(t+x/2)\right)f(t+x).
\tag{2.3}
\]

Consequently,

\[
\pi_p(v)\pi_p(w)
=\psi_p\!\left(\frac12\omega(v,w)\right)\pi_p(v+w).
\tag{2.4}
\]

Let

\[
\rho_p^{\mathrm{std}}:\operatorname{Sp}(J,\mathbb F_p)
\longrightarrow U(\mathbb C^{p^2})
\tag{2.5}
\]

be the full finite Weil representation with central character \(\psi_p\),
normalized by

\[
[\rho_p^{\mathrm{std}}(g)]\pi_p(v)
[\rho_p^{\mathrm{std}}(g)]^{-1}=\pi_p(gv).
\tag{2.6}
\]

This is an honest representation of
\(\operatorname{Sp}(4,\mathbb F_p)\), not a projective representation and
not a representation of a metaplectic double cover. The exceptional
nonuniqueness over \(\mathbb F_3\) occurs in symplectic dimension two, not
in the present symplectic dimension four. The full \(p^2\)-dimensional
representation is used; it is not replaced by one parity constituent.

The source matrices are not written in the standard \(J\)-frame.  For any
displayed nondegenerate alternating form \(J_\star\), choose a Darboux
matrix \(T_\star\) over \(\mathbb F_p\) satisfying

\[
T_\star^T J_\star T_\star=J.
\]

For \(g\in\operatorname{Sp}(J_\star,\mathbb F_p)\), define the pulled-back
representation

\[
\boxed{
\rho_{p,J_\star}(g)
=\rho_p^{\mathrm{std}}(T_\star^{-1}gT_\star).
}
\tag{2.6a}
\]

A different Darboux matrix conjugates (2.6a) by one fixed Weil operator.
Consequently its character and characteristic polynomial are independent
of that choice.  For the C25/C26 frame we take the integral matrix \(T\) in
(1.3), reduced modulo \(p\); C24 matrices below use their displayed
\(J_{24}\)-frame.  When the source frame is clear, write

\[
\Theta_p(g)=\operatorname{Tr}\rho_{p,J_\star}(g).
\tag{2.6b}
\]

Thus every source-frame matrix is Darboux-conjugated before the standard
Weil representation is applied; no matrix preserving \(J_0\) is silently
treated as if it preserved \(J\).

Define

\[
G_p=\sum_{x\in\mathbb F_p}\psi_p(x^2/2).
\tag{2.7}
\]

With (2.1),

\[
G_p^2=\left(\frac{-1}{p}\right)p,
\qquad
\overline{G_p}=\left(\frac{-1}{p}\right)G_p.
\tag{2.8}
\]

Every character below is represented exactly in the basis
\((1,G_p)\); no floating square root of \(p\) is used.

## 3. Thomas's character formula in symplectic dimension four

Let \(g\in\operatorname{Sp}(J_0,\mathbb F_p)\), and set

\[
H_g=g-I,
\qquad
k_g=\dim_{\mathbb F_p}\ker H_g,
\qquad
r_g=4-k_g.
\tag{3.1}
\]

Choose a \(4\times r_g\) matrix \(C\) whose columns give a basis of
\(V/\ker H_g\). In the \(J_0\)-frame define

\[
Q_g=C^T H_g^T J_0 C,
\qquad
d_g=\det Q_g\in\mathbb F_p^\times.
\tag{3.2}
\]

For \(r_g=0\), set \(d_g=1\). The matrix \(Q_g\) is nondegenerate.
Changing the quotient basis sends \(Q_g\) to \(R^TQ_gR\), so its
determinant changes by a square. Hence

\[
\eta_p(d_g)=\left(\frac{d_g}{p}\right)
\]

is intrinsic. No additional signed-discriminant factor is inserted.

### Theorem 3.1 -- exact full finite-Weil character

**Status: proved, classical finite-Weil input.** Put

\[
\gamma_p(1)=p^{-1/2}G_p.
\]

Then Thomas's formula specializes to

\[
\boxed{
\Theta_p(g):=\operatorname{Tr}\rho_{p,J_0}(g)
=p^{k_g/2}\gamma_p(1)^{4-k_g}\eta_p(d_g).
}
\tag{3.3}
\]

Equivalently, without radicals,

\[
\boxed{
\Theta_p(g)=
\begin{cases}
\eta_p(d_g),&k_g=0,\\[1mm]
\eta_p(d_g)\eta_p(-1)G_p,&k_g=1,\\[1mm]
\eta_p(d_g)\eta_p(-1)p,&k_g=2,\\[1mm]
\eta_p(d_g)pG_p,&k_g=3,\\[1mm]
p^2,&k_g=4.
\end{cases}}
\tag{3.4}
\]

#### Proof

Thomas associates to \(g-I\) the induced isomorphism

\[
\sigma_g:V/\ker(g-I)\longrightarrow(g-I)V.
\]

The bilinear form induced by the symplectic pairing has discriminant
\(d_g\) modulo squares. His finite-field character formula is

\[
p^{k_g/2}\gamma_p(1)^{4-k_g-1}\gamma_p(d_g).
\]

For the additive character (2.1),

\[
\gamma_p(d_g)=\eta_p(d_g)\gamma_p(1).
\]

This gives (3.3). Substitution of
\(G_p=p^{1/2}\gamma_p(1)\), followed by (2.8), gives (3.4).
\(\square\)

### Corollary 3.2 -- normalization and exact checks

For every \(g\),

\[
\Theta_p(I)=p^2,
\qquad
|\Theta_p(g)|^2=p^{k_g}=|\ker(g-I)|,
\tag{3.5}
\]

and

\[
\Theta_p(hgh^{-1})=\Theta_p(g),
\qquad
\Theta_p(g^{-1})=\overline{\Theta_p(g)}.
\tag{3.6}
\]

Thus the finite Weil character never vanishes. It is a class function, but
it is not multiplicative:

\[
\Theta_p(g_2g_1)
\ne \Theta_p(g_2)\Theta_p(g_1)
\]

in general. A chronological product must be formed before its character is
evaluated.

## 4. Fixed-prime trace-class Fredholm theorem

Let \(\Omega\subset\mathbb C^3\), \(h_\gamma\), and
\(w_{s,\gamma}\) be the common domain, inverse branches, and weights of
HCS-C26. On \(A^2(\Omega)\), write

\[
K_{s,\gamma}f=w_{s,\gamma}(f\circ h_\gamma).
\]

C26 proves, locally uniformly for
\(\operatorname{Re}s>-\sigma_0\), that

\[
\sum_\gamma\|K_{s,\gamma}\|_1<\infty.
\tag{4.1}
\]

For a fixed odd prime \(p\), let

\[
\mathcal H_p=A^2(\Omega)\widehat\otimes\mathbb C^{p^2}.
\tag{4.2}
\]

Use the C25 left-column convention

\[
[\mathcal T_{s,p,\gamma}F](z)
=w_{s,\gamma}(z)\,
 \rho_{p,J_0}(g_\gamma\bmod p)F(h_\gamma z)
\tag{4.3}
\]

and define

\[
\mathcal L_{s,p}=\sum_{\gamma\in\Gamma}
\mathcal T_{s,p,\gamma}.
\tag{4.4}
\]

### Theorem 4.1 -- fixed-\(p\) finite-Weil Fredholm family

**Status: proved from C26 Theorem 3.2 by finite tensor extension.**
For every fixed odd prime \(p\) and every
\(\operatorname{Re}s>-\sigma_0\):

1. the series (4.4) converges absolutely in trace norm;
2. \(\mathcal L_{s,p}\) is trace class and lies in an exponential
   singular-value class with exponent \(1/3\), with constants allowed to
   depend on \(p\);
3. \(s\mapsto\mathcal L_{s,p}\) is trace-norm holomorphic; and
4. the ordinary Fredholm determinant

   \[
   \boxed{
   \mathcal D_p(s,u)
   =\det_{\mathcal H_p}(I-u\mathcal L_{s,p})
   }
   \tag{4.5}
   \]

   is jointly holomorphic on
   \[
   \{\operatorname{Re}s>-\sigma_0\}\times\mathbb C.
   \]

#### Proof

The finite Weil matrix is unitary on a \(p^2\)-dimensional space, hence

\[
\|K_{s,\gamma}\otimes\rho_{p,J_0}(g_\gamma)\|_1
=\|K_{s,\gamma}\|_1\,\|\rho_{p,J_0}(g_\gamma)\|_1
=p^2\|K_{s,\gamma}\|_1.
\tag{4.6}
\]

Equation (4.1) gives locally uniform trace-norm summability for every fixed
\(p\). The common compact branch image used in C26 factors the vector-valued
operator through the same Bergman restriction tensored with the
\(p^2\)-dimensional identity. Its singular values are the scalar restriction
singular values with finite multiplicity \(p^2\), so the exponential
exponent \(1/3\) persists. The branch majorant gives trace-norm holomorphy,
and the standard trace-class determinant theorem gives (4.5).
\(\square\)

No constant in this proof is asserted to be uniform as \(p\to\infty\).

### Theorem 4.2 -- chronological periodic atom

Let

\[
\boldsymbol\beta=(\beta_1,\ldots,\beta_n)
\]

be a forward Rauzy word. Its transfer-operator factor word is
\((\beta_n,\ldots,\beta_1)\). Therefore

\[
\rho_{p,J_0}(g_{\beta_n})\cdots\rho_{p,J_0}(g_{\beta_1})
=\rho_{p,J_0}(g_{\mathrm{fwd}}),
\qquad
g_{\mathrm{fwd}}=g_{\beta_n}\cdots g_{\beta_1}.
\tag{4.7}
\]

Let \(A_{\mathrm{fwd}}\) be the corresponding positive scalar projective
matrix, let \(\lambda_{\boldsymbol\beta}\) be its Perron root, and put

\[
\chi_{\boldsymbol\beta}(t)
=\det(tI-A_{\mathrm{fwd}}).
\]

Then

\[
\boxed{
\operatorname{Tr}
\bigl(
\mathcal T_{s,p,\beta_n}\cdots
\mathcal T_{s,p,\beta_1}
\bigr)
=\Theta_p(g_{\mathrm{fwd}})
 \frac{\lambda_{\boldsymbol\beta}^{-(s+1)}}
 {\chi_{\boldsymbol\beta}'(\lambda_{\boldsymbol\beta})}.
}
\tag{4.8}
\]

Consequently, with absolute wordwise convergence,

\[
\operatorname{Tr}\mathcal L_{s,p}^n
=\sum_{\boldsymbol\beta\in\Gamma^n}
\Theta_p(g_{\mathrm{fwd}})
\frac{\lambda_{\boldsymbol\beta}^{-(s+1)}}
{\chi_{\boldsymbol\beta}'(\lambda_{\boldsymbol\beta})},
\tag{4.9}
\]

where the indexing uses the frozen conversion between forward words and
operator-factor words. For sufficiently small \(|u|\),

\[
-\log\mathcal D_p(s,u)
=\sum_{n\ge1}\frac{u^n}{n}
 \operatorname{Tr}\mathcal L_{s,p}^n.
\tag{4.10}
\]

The determinant (4.5), not the logarithmic series, supplies the entire
continuation in \(u\).

#### Proof

The scalar factor is C26 Theorem 4.1. The trace of a tensor product is the
product of traces, while (4.7) preserves the forward homology chronology.
Absolute trace-norm word summability justifies (4.9); the standard Fredholm
logarithm gives (4.10) near \(u=0\).
\(\square\)

## 5. Power characters and the finite-Weil fibre polynomial

For \(g\in\operatorname{Sp}(4,\mathbb F_p)\), define

\[
P_{p,g}(T)=\det(I-T\rho_{p,J_\star}(g)),
\tag{5.1}
\]

It has degree \(p^2\), and

\[
\boxed{
-\log P_{p,g}(T)
=\sum_{r\ge1}\frac{\Theta_p(g^r)}rT^r
}
\tag{5.2}
\]

as a formal identity, or analytically for \(|T|<1\). Thus repetitions use
\(\Theta_p(g^r)\), not the generally incorrect value
\(\Theta_p(g)^r\).

If

\[
P_{p,g}(T)=\sum_{m=0}^{p^2}c_mT^m,
\]

then its coefficients follow from exact Newton recursion:

\[
c_0=1,
\qquad
c_m=-\frac1m\sum_{r=1}^m
c_{m-r}\Theta_p(g^r).
\tag{5.3}
\]

The arithmetic takes place in \(\mathbb Q(G_p)\). Since
\(\operatorname{Sp}(4,\mathbb F_p)\) is perfect for odd \(p\),
\(\det\rho_{p,J_\star}(g)=1\). Because \(p^2\) is odd,

\[
c_{p^2}=-1,
\qquad
c_m=-\overline{c_{p^2-m}}.
\tag{5.4}
\]

The released certificate reconstructs and verifies (5.3)--(5.4) for both
C26 three-return products at \(p=3,5,7\).

The polynomial (5.1) packages only the finite fibre. It becomes a complete
primitive dynamical local factor only if the scalar orbit bookkeeping
supplies a compatible multiplicative local variable. That extra statement
is not built into the notation.

## 6. Good-prime quadratic theorem

### Theorem 6.1 -- generic traces are Kronecker signs

**Status: proved.** Let
\(g\in\operatorname{Sp}(4,\mathbb Z)\) preserve a unimodular integral
alternating form, and assume

\[
D_g=\det(I-g)\ne0.
\tag{6.1}
\]

For every odd prime \(p\nmid D_g\),

\[
\boxed{
\Theta_p(g\bmod p)
=\left(\frac{D_g}{p}\right).
}
\tag{6.2}
\]

#### Proof

The condition \(p\nmid D_g\) makes \(g-I\) invertible modulo \(p\), so
\(k_g=0\). Thomas's discriminant is then the square class of
\(\det(g-I)\). Since the dimension is four,
\(\gamma_p(1)^4=1\), and (3.3) reduces to (6.2).
\(\square\)

Away from the finitely many prime divisors of \(D_g\), one orbit therefore
sees the quadratic character of the squarefree kernel of \(D_g\). The
primes dividing \(D_g\) are exactly where singular \(G_p\)-terms may appear.
This is genuine arithmetic structure, but it is orbit-dependent: nothing
here proves that different AGY orbits share one quadratic field or one
conductor.

For powers,

\[
\Theta_p(g^r)
=\left(\frac{\det(I-g^r)}p\right)
\quad\text{when }p\nmid\det(I-g^r).
\tag{6.3}
\]

## 7. Exact finite chronology gates

Let \(G\), \(H\), and \(K\) denote the frozen C26 forward return matrices
gamma_star, second_branch, and third_branch. Define

\[
F=KHG,
\qquad
R=GHK.
\tag{7.1}
\]

These are the forward and noncyclically reversed three-return products of
total elementary length 650. Their integer characteristic polynomials are
different. The gcd of their nonzero coefficient differences is \(64\), so
they remain different modulo every odd prime.

The two-return control \(HG\) versus \(GH\) is intentionally null:

\[
\operatorname{Tr}\rho_{p,J_0}(HG)
=\operatorname{Tr}\rho_{p,J_0}(GH)
\]

by trace cyclicity. It is not a spectral chronology sentinel.

The finite scan over the 24 odd primes \(3\le p\le97\) and powers
\(1\le r\le24\) contains 576 exact comparisons between
\(\Theta_p(F^r)\) and \(\Theta_p(R^r)\):

\[
328\text{ differ},
\qquad
248\text{ agree}.
\tag{7.2}
\]

This proves sensitivity in many cases, but not separation.

### Proposition 7.1 -- complete \(p=43\) finite-Weil fibre-polynomial collision

**Status: exact finite certificate.** Modulo \(43\), both \(F\) and \(R\)
have order \(925\), although their characteristic polynomials differ:

\[
\chi_F(t)\equiv
t^4+33t^3+9t^2+33t+1\pmod{43},
\tag{7.3}
\]

\[
\chi_R(t)\equiv
t^4+11t^3+13t^2+11t+1\pmod{43}.
\tag{7.4}
\]

The complete common period was exhaustively checked:

\[
\boxed{
\Theta_{43}(F^r)=\Theta_{43}(R^r)
\quad(1\le r\le925).
}
\tag{7.5}
\]

Both sequences are \(925\)-periodic, so equality holds for every integer
\(r\). Equation (5.2) gives

\[
\boxed{
P_{43,F}(T)=P_{43,R}(T).
}
\tag{7.6}
\]

Thus the full \(43^2=1849\)-dimensional finite Weil **fibre polynomial**
fails to distinguish this chronology pair.

This is not a collision of the full C26 AGY periodic atom. The scalar
Perron factors in (4.8) depend on the two different integer characteristic
polynomials and remain different. Proposition 7.1 isolates a failure of the
finite fibre, not a collapse of the scalar dynamics.

## 8. Integral symplectic conjugacy collapses a symbolic tower

The C24 control is displayed in the state-2-rooted,
base-trivialized symplectic source frame frozen by C24,

\[
J_{24}=
\begin{pmatrix}
0&-1&1&-1\\
1&0&-1&1\\
-1&1&0&-1\\
1&-1&1&0
\end{pmatrix}.
\tag{8.1}
\]

The distinct eventually-positive cycles C24-P076 and C24-P082 have the
following C24 `base_trivialized_symplectic_matrix` entries:

\[
M_{76}=
\begin{pmatrix}
2&1&0&3\\
2&3&0&4\\
3&5&2&6\\
2&3&1&4
\end{pmatrix},
\qquad
M_{82}=
\begin{pmatrix}
1&1&0&2\\
1&4&0&4\\
1&6&2&5\\
1&4&1&4
\end{pmatrix}.
\tag{8.2}
\]

Their central first-return orders are

\[
(\mathtt{bbb},\mathtt{ttbt},\mathtt{tbbtt})
\quad\text{and}\quad
(\mathtt{bbb},\mathtt{tbbtt},\mathtt{ttbt}).
\tag{8.3}
\]

They use the same branch multiset but are not cyclic rotations. Put

\[
X=
\begin{pmatrix}
0&0&-1&1\\
-1&0&0&-1\\
0&-2&0&-1\\
0&-1&0&-1
\end{pmatrix}.
\tag{8.4}
\]

### Theorem 8.1 -- all-prime, all-repetition class-function collapse

**Status: proved by exact integral identities.** One has

\[
\det X=1,
\qquad
X^TJ_{24}X=J_{24},
\qquad
M_{82}X=XM_{76}.
\tag{8.5}
\]

Therefore

\[
M_{82}=XM_{76}X^{-1}
\]

inside the integral symplectic group. Reduction modulo every odd prime
preserves this conjugacy. For every odd \(p\) and every integer \(r\),

\[
\boxed{
\Theta_p(M_{76}^r)=\Theta_p(M_{82}^r),
\qquad
P_{p,M_{76}}(T)=P_{p,M_{82}}(T).
}
\tag{8.6}
\]

More generally, every class-function fibre collapses this symbolic pair and
its complete repetition tower. This is a limitation of endpoint conjugacy
data, not a failure of the Thomas formula.

Unlike the \(p=43\) C26 control, the displayed base-trivialized homological
matrices for P076 and P082 also have the same characteristic polynomial,

\[
t^4-11t^3+18t^2-11t+1.
\tag{8.7}
\]

Thus their displayed homological characteristic/Perron data and every
class-function finite fibre both collapse for this C24 census pair.  The
matrices in (8.2) are not the raw C24 `chronological_matrix` entries, and no
C26 scalar transfer-operator atom is defined or compared here.  These C24
cycles are a control on symbolic separation; they are not presented as C26
AGY return branches.

The collapse is not universal. As a singular-prime positive control, the
C24 pair P014/P016 has the same integer characteristic polynomial and
\(\det(I-g)=3\), but its exact \(p=3\) characters are

\[
-G_3
\quad\text{and}\quad
+G_3.
\tag{8.8}
\]

The singular quotient discriminant can therefore refine
characteristic-polynomial data, although it cannot overcome genuine
symplectic conjugacy.

## 9. Finite arithmetic fragmentation evidence

Let

\[
\gamma_*=\mathtt{t}^{64}(\mathtt{tbttbtbb})^8.
\]

At base state \(4\), enumerate every first-return bridge \(v\) of length at
most \(12\), and form the source-locked branch

\[
\gamma_*\,v\,\gamma_*.
\tag{9.1}
\]

There are exactly 150 such bridges. Their length census is

\[
\begin{array}{c|rrrrrrrrrr}
|v|&1&3&5&6&7&8&9&10&11&12\\ \hline
\#v&1&1&1&2&3&6&11&20&37&68.
\end{array}
\tag{9.2}
\]

For the chronological branch matrix \(g_v\), put

\[
D_v=\det(I-g_v)
\]

and define the 24-prime signature

\[
\mathfrak s(v)=
\left(
\begin{cases}
0,&p\mid D_v,\\
\left(\frac{D_v}{p}\right),&p\nmid D_v
\end{cases}
\right)_{
\substack{p\text{ odd prime}\\3\le p\le97}}.
\tag{9.3}
\]

### Proposition 9.1 -- exact bounded scan

**Status: finite evidence, not an all-length theorem.** In this scan,

\[
\boxed{
\begin{aligned}
\#\{\chi_{g_v}\}&=150,\\
\#\{D_v\}&=150,\\
\#\{\mathfrak s(v)\}&=150.
\end{aligned}}
\tag{9.4}
\]

No two scanned branches share the tested finite arithmetic signature. The
evidence favours orbit-dependent quadratic data over one small common
conductor.

The four previously published orbit discriminants give a smaller exact
factorization control. Their squarefree kernels are

\[
5{,}680{,}213,
\]

\[
8{,}442{,}687{,}618{,}099{,}208{,}317{,}639{,}430,
\]

\[
193788302599683387167116428697122910571377207,
\]

and

\[
193788302599828820682721458615724385190853431.
\tag{9.5}
\]

They are pairwise distinct. Neither (9.4) nor (9.5) proves that all future
branches have distinct squarefree kernels, that conductor fragmentation
persists at every length, or that no different arithmetic assembly exists.

## 10. Scope firewall

The proved positive result is deliberately fixed-prime:

> For every fixed odd \(p\), the literal chronology-preserving finite-Weil
> twist has a genuine trace-class Fredholm determinant with exact arithmetic
> periodic traces.

The following statements are not consequences of this package.

1. **No \(p\to\infty\) limit.** The trace-norm estimate contains a factor
   \(p^2\); no uniform prime limit is proved.
2. **No automatic prime product.** The family
   \(\{\mathcal D_p\}_p\) is not one intrinsic operator, an adelic Hilbert
   space, or a regularized product over primes.
3. **The modulus is external.** A fixed \(p\) is selected by hand; the AGY
   dynamics has not produced an intrinsic distribution over primes.
4. **Odd primes only.** The convention uses
   \(1/2\in\mathbb F_p\). No \(p=2\) statement is made.
5. **Full \(\operatorname{Sp}\), not \(\operatorname{PSp}\).** The central
   element \(-I\) acts by parity \(f(x)\mapsto f(-x)\), not by a disposable
   scalar. Quotienting by the centre loses data.
6. **No finite-field metaplectic signs.** The representation is already
   honest over \(\operatorname{Sp}(4,\mathbb F_p)\); importing the real
   metaplectic edge signs would create spurious choices.
7. **No branchwise character product.** Repetitions use
   \(\Theta_p(g^r)\), and a word value is evaluated only after its
   chronological product is formed.
8. **No averaged chronology.** Forward and operator-factor orders are both
   retained through (1.4)--(1.5).
9. **The fibre polynomial is not the scalar orbit factor.** Proposition 7.1
   leaves the distinct C26 scalar Perron atoms intact.
10. **A class function is not a complete symbolic decoder.** Theorem 8.1
    proves an all-prime conjugacy collapse, while Proposition 7.1 gives a
    nonconjugate fixed-prime fibre collision.
11. **Finite scans remain finite.** Equations (7.2) and (9.4) are not
    promoted to all-power or all-length theorems.
12. **No Hilbert--Pólya conclusion.** No functional equation, Riemann-zero
    divisor, self-adjoint operator, prime-orbit law, or Route-B bridge is
    obtained.

## 11. Exact provenance and primary sources

The exact producer and released output are

~~~text
code/c27_producer.py
results/c27_certificate.json
~~~

The source lock is

~~~text
C24 c24_certificate.json  4b4fe5943262137eeeb3eda4de887725a0663402a1f39f8cc43e089bcc91e778
C25 c25_certificate.json  a35cee22714abbb9dc9aadcc165720d1ff77aff3b7f29071f53a1b451760bd12
C26 c26_certificate.json  1c0289b9b47e65e0603ea001be7cce263aea13d58c66e4609eac88edf8f7ce4a
~~~

The independent checker does not import the producer. It reconstructs the
source matrices, modular quotient forms, Thomas characters, Newton
polynomials, power periods, conjugacy identities, and branch signatures
through a separate exact-arithmetic implementation. Its 8/8 checks pass,
including all six \(p=3,5,7\) local-polynomial hashes, the complete
\(p=43\) period, the certified late separations at \((p,r)=(83,41)\) and
\((89,30)\), the P076/P082 integral conjugacy, and all 150 branch signatures.
The checker and result are

~~~text
code/c27_independent_check.py
results/c27_independent_check.json
~~~

The integral identities in Theorem 8.1 were also checked directly over
\(\mathbb Z\). The \(p=43\) claim is recorded under
**p43_complete_weil_fibre_polynomial_collision**, and the bounded branch
evidence under **agy_branch_arithmetic_scan**.

Primary finite-Weil sources:

- Teruji Thomas, *The Character of the Weil Representation*, Theorem 1A and
  Remark 1.3: <https://arxiv.org/abs/math/0610644>.
- Shamgar Gurevich and Ronny Hadani, *Quantization of Symplectic Vector
  Spaces over Finite Fields*, especially Theorem 1.3.1, Proposition 2.3.1,
  and Remark 2.7.2: <https://arxiv.org/abs/0705.4556>.
- Shamgar Gurevich and Ronny Hadani, *On the Diagonalization of the Discrete
  Fourier Transform*, for the Schrödinger normalization and Fourier phase:
  <https://arxiv.org/abs/0808.3281>.

The fixed-prime Fredholm proof depends on the common-domain and scalar
trace-class theorems in
../agy_holomorphic_slice_obstruction/THEOREM_PACKAGE.md; it does not reprove
those source-locked analytic inputs.
