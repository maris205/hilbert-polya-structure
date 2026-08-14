# DERIVATION PACKAGE — SD-C19

## 1. Inclusion–exclusion transfer

For \(P=\{p_1,\ldots,p_n\}\), write \(e_k(x)\) for the elementary symmetric
polynomial.  The signed subset transfer in the trivial character is

\[
B_+(x)=\sum_{k=1}^n(-1)^{k+1}e_k(x)
=1-\prod_{i=1}^n(1-x_i),
\]

so \(D_+=1-B_+=\prod_i(1-x_i)\).

For the parity character, multiplication by \((-1)^k\) gives

\[
B_-(x)=\sum_{k=1}^n(-1)^{k+1}(-1)^k e_k(x)
=-\sum_{k=1}^n e_k(x)
=1-\prod_{i=1}^n(1+x_i).
\]

Hence \(D_-=\prod_i(1+x_i)\).

## 2. Direct \(2\times2\) regular calculation

Separate even and odd subset degrees:

\[
b_{\rm even}=\sum_{|S|\ {\rm even}}\varepsilon(S)x_S,
\qquad
b_{\rm odd}=\sum_{|S|\ {\rm odd}}\varepsilon(S)x_S.
\]

With \(L_a=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\),

\[
I-B_{\rm reg}=
\begin{pmatrix}
1-b_{\rm even}&-b_{\rm odd}\\
-b_{\rm odd}&1-b_{\rm even}
\end{pmatrix}.
\]

The eigenvectors of \(L_a\) are the trivial and sign characters, so

\[
\det(I-B_{\rm reg})
=(1-b_{\rm even}-b_{\rm odd})
 (1-b_{\rm even}+b_{\rm odd})=D_+D_-.
\]

For two atoms \(x,y\),

\[
B_{\rm reg}=(x+y)L_a-xyI,
\]

and direct evaluation gives

\[
\det(I-B_{\rm reg})=(1-x^2)(1-y^2).
\]

This is the minimal same-object certificate: the moving fiber and both
character factors occur inside one regular matrix.

## 3. Trace and repetition signs

Set every atom variable equal to a diagnostic variable \(t\).  Then

\[
B_+(t)=1-(1-t)^n,qquad B_-(t)=1-(1+t)^n.
\]

The determinant convention implies

\[
-\log D_\chi(t)=\sum_{r\ge1}\frac{B_\chi(t)^r}{r}.
\]

Closed coefficients are

\[
[t^k](-\log D_+)=\frac nk,qquad
[t^k](-\log D_-)=\frac{n(-1)^k}{k},
\]

and, after adding the two character traces,

\[
[t^k](-\log D_{\rm reg})=
\begin{cases}
0,&k\text{ odd},\\
2n/k,&k\text{ even}.
\end{cases}
\]

The prototype checked all three ledgers through degree ten for ten atom
cutoffs, giving 300 exact rows.  This collapse tests repetition signs; the
multivariate sparse-polynomial calculation supplies the noncollision proof.

## 4. Cyclic character phase ledger

For \(C_m=\langle a\rangle\) and \(\chi_j(a)=\omega^j\), the coefficient of
a squarefree degree-\(k\) monomial in \(D_j\) is the exact cyclotomic pair

\[
\bigl((-1)^k,jk\bmod m\bigr).
\]

Thus

\[
D_j=\prod_i(1-\omega^jx_i),qquad
D_{\rm reg}=\prod_jD_j=\prod_i(1-x_i^m).
\]

The prototype stores phase exponents modulo \(m\), avoiding floating
approximations to roots of unity.  It checked 350 character rows and the exact
regular permutation determinant for \(m=2,\ldots,8\).

## 5. First one-letter leakage coefficient

Naturality reduces a one-letter rule to labels \(g_k\) by subset size.  For a
one-dimensional character put \(\lambda_k=\chi(g_k)\).  Then

\[
D_\chi(x)=1-\lambda_1e_1(x)+\lambda_2e_2(x)
-\lambda_3e_3(x)+\cdots.
\]

The desired atom product is

\[
\prod_i(1-\lambda_1x_i)
=1-\lambda_1e_1(x)+\lambda_1^2e_2(x)
-\lambda_1^3e_3(x)+\cdots.
\]

At the first \(k\) for which \(\lambda_k\ne\lambda_1^k\), the discrepancy is

\[
(-1)^k(\lambda_k-\lambda_1^k)e_k(x).
\]

For a matrix representation the transfer-level two-atom discrepancy is

\[
xy\,[\rho(g_2)-\rho(g_1)^2].
\]

The 72,079-table enumeration tests this coefficient condition in the full
regular family, not a weaker determinant-only assertion.

## 6. Exact primitive-necklace recurrence

Let

\[
A_n(y)=\sum_{k=1}^n\binom nk y^k=(1+y)^n-1.
\]

The coefficient \([y^c]A_n(y)^r\) counts all length-\(r\) base words with
total subset degree \(c\).  If \(Q_r(c)\) counts words of minimal period \(r\),
unique minimal period gives

\[
Q_r(c)=[y^c]A_n(y)^r-
\sum_{\substack{d\mid r,\ d<r\\(r/d)\mid c}}
Q_d\!\left(\frac{c}{r/d}\right).
\]

Each primitive necklace has exactly \(r\) rotations, so its count at degree
\(c\) is \(Q_r(c)/r\).  For the \(C_m\) lift, the Frobenius is \(a^c\), its
order is \(m/\gcd(m,c)\), and the lift multiplicity is \(\gcd(m,c)\).

At \(n=5,r=10,m=2\), the exact census contains

\[
81{,}962{,}825{,}835{,}072
\]

primitive base necklaces,
\(40{,}981{,}411{,}486{,}080\) mixed immediate closures, and
\(122{,}944{,}237{,}321{,}152\) primitive lifted cycles.  The three quantities
have different meanings and are never combined.

## 7. Off-shell firewall

Because \(B_j=1-\prod_i(1-\omega^jx_i)\),

\[
\det(I-zB_j)=1-z+z\prod_i(1-\omega^jx_i).
\]

At \(z=1\) the constant terms cancel and the atom product remains.  For a
generic \(z\ne1\), the affine combination is not a product of independent
atom factors.  The clean character factorization is therefore a fixed
normalization identity, not an off-shell family.

## 8. Finite versus infinite regular fiber

Replacing \(C_m\) by \(\mathbb Z\) sends the generator to the bilateral shift
\(U\) on \(\ell^2(\mathbb Z)\).  Formally,

\[
I-B=\prod_p(I-x_pU).
\]

For a nonzero finite inventory, the difference from the identity is a nonzero
translation-invariant operator and is not compact, hence not trace class.  The
ordinary Fredholm determinant of the full regular object is unavailable.
Bloch characters retain \(\prod_p(1-wx_p)\), but this does not reconstruct an
ordinary full-fiber determinant.  Finite fiber dimension is therefore a
load-bearing assumption of the same-object Artin certificate.
