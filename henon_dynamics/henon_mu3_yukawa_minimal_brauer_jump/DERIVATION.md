# HCS-C57 derivation

Status: **RELEASE_FROZEN; DOCS_FINAL_NO_MORE_EDITS; PAPER_COMPILED;
PAPER_HOSTILE_PASS; exact derivation fixed; project-local machine premises
PREFREEZE_CODE_RESULTS_PASS.**

This file derives the formulas used in the theorem package. It distinguishes
formal consequences of the frozen C56 theorem, classical classification
results, and finite exact calculations now certified by the C57 machine
handoff at `PREFREEZE_CODE_RESULTS_PASS`. The labeled written bridges remain
mathematical arguments rather than machine claims.

The official 24-page paper build, independent hostile paper audit, final hostile
root audit, external 13-root binding, implementation identity, self-excluding
64-entry release manifest, and byte-identical archived Route now pass. P57
therefore freezes the project without changing this derivation or the protected
machine tuple.

## 1. Galois-theoretic setup

HCS-C56 gives the tower

\[
\mathbf Q\subset E\subset K\subset\overline{\mathbf Q},
\qquad [E:\mathbf Q]=27,
\qquad \operatorname{Gal}(K/\mathbf Q)=W(E_6).
\tag{1.1}
\]

The field \(E\) is not Galois. The 27 embeddings of \(E\) correspond to the
27 lines, while \(K\) contains all line coordinates.

Let \(D=\{\mathcal E,\mathcal G\}\) be a double-six and let

\[
U_1=\operatorname{Stab}(D),\qquad
U_1^+=\operatorname{Stab}(\mathcal E)
\cap\operatorname{Stab}(\mathcal G).
\tag{1.2}
\]

The standard Schläfli action gives

\[
U_1\cong S_6\times C_2,\qquad
U_1^+\cong S_6,\qquad
[W(E_6):U_1]=36,\qquad [U_1:U_1^+]=2.
\tag{1.3}
\]

Therefore

\[
F_D=K^{U_1},\qquad [F_D:\mathbf Q]=36,
\tag{1.4}
\]

and

\[
F_D'=K^{U_1^+},\qquad [F_D':F_D]=2.
\tag{1.5}
\]

The core of \(U_1\) in \(W(E_6)\) is trivial because the faithful action on
the 36 double-sixes is the coset action on \(W(E_6)/U_1\). Hence the normal
closure of \(F_D\) is \(K\).

## 2. Complete 2-primary classification and degree divisibility

Let \(L/\mathbf Q\) be finite, put
\(G_L=\operatorname{Gal}(\overline{\mathbf Q}/L)\), and define

\[
H_L=\operatorname{im}\!\left(
G_L\longrightarrow W(E_6)
\right).
\tag{2.1}
\]

Set

\[
N_L=\ker\!\left(G_L\longrightarrow H_L\right).
\tag{2.1a}
\]

The \(G_L\)-action on the discrete torsion-free lattice \(\Lambda\) factors
through \(H_L\), so \(N_L\) acts trivially. A continuous homomorphism from
the profinite group \(N_L\) to \(\Lambda\) has finite image, which must be
zero. Consequently

\[
H^1(N_L,\Lambda)
=\operatorname{Hom}_{\mathrm{cont}}(N_L,\Lambda)=0,
\tag{2.1b}
\]

and inflation--restriction for
\(1\to N_L\to G_L\to H_L\to1\) yields

\[
H^1(G_L,\Lambda)\cong H^1(H_L,\Lambda).
\tag{2.1c}
\]

The cubic surface is geometrically rational, hence
\(\operatorname{Br}(Y_{\overline{\mathbf Q}})=0\), and the number field
\(L\) satisfies \(H^3(L,\mathbf G_m)=0\). The low-degree
Hochschild--Serre sequence therefore gives the exact identification

\[
\operatorname{Br}(Y_L)/\operatorname{im}\operatorname{Br}(L)
\cong H^1(G_L,\Lambda)
\cong H^1(H_L,\Lambda).
\tag{2.1d}
\]

Since \(K/\mathbf Q\) is Galois,

\[
K^{H_L}=K\cap L
\tag{2.2}
\]

inside the fixed algebraic closure, and therefore

\[
[K\cap L:\mathbf Q]=[W(E_6):H_L].
\tag{2.3}
\]

The complete Swinnerton-Dyer--Elsenhans--Jahnel classification must now be
used in two branches:

\[
\begin{array}{c|c|c}
\text{nonzero 2-primary quotient}
&\text{containment}&\text{ambient index}\\ \hline
\mathbf Z/2
&H_L\subseteq gU_1g^{-1}&36\\
(\mathbf Z/2)^2
&H_L\subseteq gU_3g^{-1}&720.
\end{array}
\tag{2.4}
\]

Thus

\[
\begin{aligned}
H_L\subseteq gU_1g^{-1}
&\Longrightarrow
[W(E_6):H_L]
=36[U_1:g^{-1}H_Lg],\\
H_L\subseteq gU_3g^{-1}
&\Longrightarrow
[W(E_6):H_L]
=720[U_3:g^{-1}H_Lg].
\end{aligned}
\tag{2.5}
\]

Both rows imply

\[
36\mid[W(E_6):H_L].
\tag{2.6}
\]

Combining (2.3), (2.6), and the tower law yields the stronger divisibility
statement

\[
36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q].
\tag{2.7}
\]

In particular \([L:\mathbf Q]\ge36\). If equality holds, the index-720
branch is impossible; all factors in (2.7) are equal, so

\[
L=K\cap L,\qquad H_L=gU_1g^{-1}.
\tag{2.8}
\]

This is the equality classification. It is not obtained from enumerating only
the stabilizers of lines, double-sixes, and Steiner configurations.

## 3. Exact incidence carrier

On the HCS-C56 main chart, every line is reconstructed from a root \(x\) of
the irreducible degree-27 eliminant \(g\). Let the four line coordinates be
rational polynomial functions of \(x\).

For two roots \(x,y\), meeting of the corresponding lines is equivalent to
the vanishing of an exact divided-difference expression \(J(x,y)\). The
diagonal divisions are performed polynomially, so \(J\) is defined in

\[
\left(\mathbf Q[x]/(g(x))\right)[y].
\tag{3.1}
\]

Set

\[
H_x(y)=\gcd_y(g(y),J(x,y)).
\tag{3.2}
\]

The required characteristic-zero identities are

\[
\deg H_x=10,\qquad
\gcd(H_x,y-x)=1,\qquad
g=H_xQ_x,\qquad \deg Q_x=17.
\tag{3.3}
\]

Thus each line meets exactly ten distinct other lines, and the number of
unordered incident pairs is

\[
\frac{27\cdot10}{2}=135.
\tag{3.4}
\]

A sixer is a six-element independent set in this graph. Exact enumeration
gives 72 sixers. Pairing each sixer with its unique opposite sixer gives 36
unordered double-sixes.

The characteristic-zero gcd proves the incidence relation. Modular counts at
good primes are independent all-and-only checks; a timed-out direct replay is
a non-result, not a conflicting computation.

## 4. Double-six and orientation resolvers

Let \(\alpha_i\) denote the scaled \(d\)-coordinate of the \(i\)-th line. For
a double-six \(D\), define a symmetric separating invariant

\[
\theta_D=\sum_{\ell_i\in D}\alpha_i.
\tag{4.1}
\]

Its orbit product is

\[
R_\theta(T)=\prod_{D}(T-\theta_D).
\tag{4.2}
\]

The exact configuration action proves that the 36 values are distinct and
that

\[
\operatorname{Stab}_{W(E_6)}(\theta_D)=U_1.
\tag{4.3}
\]

Consequently

\[
\mathbf Q(\theta_D)=K^{U_1}=F_D.
\tag{4.4}
\]

Choose an orientation \(D=(\mathcal E,\mathcal G)\) and define

\[
\beta_D=
\sum_{\ell_i\in\mathcal E}\alpha_i
-
\sum_{\ell_i\in\mathcal G}\alpha_i,
\qquad
\delta_D=\beta_D^2.
\tag{4.5}
\]

The swap in the \(C_2\) factor sends \(\beta_D\) to \(-\beta_D\), while
\(\delta_D\) is fixed. Exact stabilizers give

\[
\operatorname{Stab}(\beta_D)=U_1^+,\qquad
\operatorname{Stab}(\delta_D)=U_1.
\tag{4.6}
\]

Therefore

\[
\mathbf Q(\delta_D)=F_D,\qquad
F_D'=F_D(\beta_D)=F_D(\sqrt{\delta_D}).
\tag{4.7}
\]

The exact orbit product

\[
R_\delta(T)=\prod_D(T-\delta_D)
\tag{4.8}
\]

is another degree-36 defining polynomial. Equations (4.4) and (4.7) prove the
same-field statement without constructing an expanded polynomial
\(\delta=P(\theta)\).

## 5. Twelve-line carrier over the double-six field

Let \(d_1,\ldots,d_{12}\) be the roots of \(g\) belonging to \(D\). Define

\[
A_{12}(d)=\prod_{i=1}^{12}(d-d_i)\in F_D[d].
\tag{5.1}
\]

Since the complementary 15 lines form the second \(U_1\)-orbit,

\[
B_{15}(d)=\prod_{i=13}^{27}(d-d_i)\in F_D[d].
\tag{5.2}
\]

After monic normalization of \(g\),

\[
g=A_{12}B_{15}.
\tag{5.3}
\]

The carrier coefficients are functions of \(\theta_D\). The exact gate must
check monicity, the prescribed subtop coefficient, long-division remainder
zero, and an independent forward multiplication. A reconstructed table alone
does not establish (5.3).

## 6. Quartics modulo the cubic equation

There are 35 monomials of degree four in four variables. Multiplication by
the cubic equation gives an injective four-dimensional subspace

\[
F\cdot H^0(\mathbf P^3,\mathcal O(1))
\subset H^0(\mathbf P^3,\mathcal O(4)).
\tag{6.1}
\]

The quotient therefore has dimension 31. Put

\[
c=[u_0^3]F=75081586157.
\tag{6.2}
\]

With source basis \((Fu_0,Fu_1,Fu_2,Fu_3)\) and target coordinates given by
the coefficients of

\[
u_0^4,\quad u_0^3u_1,\quad u_0^3u_2,\quad u_0^3u_3.
\tag{6.3}
\]

the resulting \(4\times4\) coefficient block is triangular with diagonal
\((c,c,c,c)\). Hence

\[
\det(\text{gauge block})
=c^4
=31778526453059635681033276764499400992765201\ne0.
\tag{6.4}
\]

The four coefficient functionals therefore restrict isomorphically to
\(F\cdot H^0(\mathbf P^3,\mathcal O(1))\). Every quartic class has a unique
representative in which the four coefficients in (6.3) vanish. This proves
the gauge rather than merely declaring it.

Let

\[
\mathcal M=(m_0,\ldots,m_{30}),\qquad m_0=u_0^2u_1^2,
\tag{6.5}
\]

be the locked ordered basis.

Restricting a quartic

\[
Q=\sum_{j=0}^{30}q_jm_j
\tag{6.6}
\]

to one line yields a binary quartic and hence five scalar equations. The 12
carrier lines yield the \(60\times31\) matrix

\[
M_Dq=0.
\tag{6.7}
\]

## 7. Rank sandwich and canonical determinant

The divisor classes of the two sixers satisfy

\[
\mathcal E+\mathcal G\sim4H_Y,
\tag{7.1}
\]

where \(H_Y\) is the hyperplane class.

There is a descent step before this class equality can be used to bound the
matrix rank. Put \(k=F_D\), and choose a \(k\)-rational hyperplane section
\(H_0=\operatorname{div}_Y(\ell)\). The unordered divisor
\(\mathcal E+\mathcal G\) and the divisor \(4H_0\) are both
\(k\)-rational. Over \(\bar k\), choose \(r\in\bar k(Y)^*\) with

\[
\operatorname{div}(r)=\mathcal E+\mathcal G-4H_0.
\]

For every \(\sigma\in\operatorname{Gal}(\bar k/k)\), the quotient
\(c_\sigma=\sigma(r)/r\) has trivial divisor and hence lies in
\(\bar k^*\). The scalars \(c_\sigma\) form a multiplicative
1-cocycle. Hilbert theorem 90 gives \(a\in\bar k^*\) such that
\(c_\sigma=\sigma(a)/a\); consequently \(r_0=r/a\) lies in \(k(Y)^*\).
The section

\[
s_D=r_0\ell^4\in H^0(Y_k,\mathcal O_Y(4))
\]

is therefore defined over \(k\) and has divisor
\(\mathcal E+\mathcal G\). Thus both the line-bundle equality and its
required section descend; geometric linear equivalence alone is not being
used as an \(F_D\)-rational section.

Now use the restriction sequence

\[
0\longrightarrow\mathcal O_{\mathbf P^3}(1)
\xrightarrow{\cdot F}\mathcal O_{\mathbf P^3}(4)
\longrightarrow\mathcal O_Y(4)\longrightarrow0
\tag{7.2}
\]

and \(H^1(\mathbf P^3_k,\mathcal O(1))=0\) to lift \(s_D\) over \(k\)
to an ambient quartic. Hence there exists a nonzero class over \(F_D\)
vanishing on \(\mathcal E+\mathcal G\), so

\[
\operatorname{rank}M_D\le30.
\tag{7.3}
\]

Delete the \(m_0\)-column and take rows

\[
\mathcal R=
\{0,\ldots,10,12,\ldots,20,24,\ldots,29,36,37,38,48\}.
\tag{7.4}
\]

Let \(N_D\) be the corresponding \(30\times30\) matrix. A good-specialization
certificate gives

\[
\det N_D\ne0
\tag{7.5}
\]

in \(F_D\), so \(\operatorname{rank}M_D\ge30\). Combining with (7.3),

\[
\operatorname{rank}M_D=30,\qquad \dim\ker M_D=1.
\tag{7.6}
\]

Normalize \(q_0=1\). Writing \(b_D\) for the selected entries of the first
column, define

\[
(q_1,\ldots,q_{30})^t=-N_D^{-1}b_D.
\tag{7.7}
\]

Equivalently, every \(q_i\) is a ratio of explicit determinants by Cramer's
rule. This definition, together with the gauge, order, rows, and
normalization, is a complete exact specification of \(Q_D\). An expanded
31-by-36 table is optional and is not a theorem dependency.

## 8. Divisor exhaustion

All \(60\) entries of \(M_Dq_D\) vanish, so \(Q_D\) vanishes on all 12
distinct lines in \(D\). It is not a multiple of \(F\), because it is a
nonzero class in the quotient gauge.

As a divisor on the cubic surface,

\[
\operatorname{div}_Y(Q_D)\sim4H_Y.
\tag{8.1}
\]

Its degree is

\[
(4H_Y)\cdot H_Y=4H_Y^2=12,
\tag{8.2}
\]

because \(H_Y^2=\deg Y=3\). The 12 distinct line components already
contribute degree 12. Positivity of degree for any nonzero effective residual
divisor rules out residual components, while the same total count rules out
multiplicity greater than one. Therefore

\[
\operatorname{div}_Y(Q_D)=\mathcal E+\mathcal G.
\tag{8.3}
\]

## 9. Norm divisor and quaternion

Let

\[
\ell=u_0,\qquad
\mathcal L_0=\operatorname{div}_Y(\ell).
\tag{9.1}
\]

The exact line replay verifies that no carrier line is contained in
\(\ell=0\). Set

\[
f_D=Q_D/\ell^4.
\tag{9.2}
\]

Over \(F_D'\), put

\[
\mathcal D=\mathcal E-2\mathcal L_0.
\tag{9.3}
\]

The nontrivial involution of \(F_D'/F_D\) exchanges
\(\mathcal E\) and \(\mathcal G\), and fixes \(\mathcal L_0\). Hence

\[
\begin{aligned}
\operatorname{Norm}_{F_D'/F_D}(\mathcal D)
&=\mathcal D+\overline{\mathcal D}\\
&=\mathcal E+\mathcal G-4\mathcal L_0\\
&=\operatorname{div}(f_D).
\end{aligned}
\tag{9.4}
\]

The cyclic-algebra divisor criterion then makes

\[
\mathcal A_D=(\delta_D,f_D)
=(\delta_D,Q_D/u_0^4)
\tag{9.5}
\]

unramified on \(Y_{F_D}\). Nontriviality requires a separate Picard-lattice
calculation. In the standard blow-up basis of \(\Lambda\), put

\[
e_\Sigma=e_1+\cdots+e_6,\qquad
H_Y=3h-e_\Sigma,\qquad
d_0=e_\Sigma-2h.
\tag{9.6}
\]

The divisor classes of the two sixers are

\[
[\mathcal E]=e_\Sigma,\qquad
[\mathcal G]=12h-5e_\Sigma,\qquad
[\mathcal D]=e_\Sigma-2H_Y=3d_0.
\tag{9.7}
\]

Let \(\iota\) be the central involution in
\(U_1=S_6\times\langle\iota\rangle\) that exchanges the two sixers. Its
action is

\[
\iota(h)=5h-2e_\Sigma,\qquad
\iota(e_\Sigma)=12h-5e_\Sigma,\qquad
\iota(d_0)=-d_0.
\tag{9.8}
\]

Since \(\Lambda^{S_6}=\mathbf Zh\oplus\mathbf Ze_\Sigma\), direct
substitution gives

\[
\ker(1+\iota\mid\Lambda^{S_6})=\mathbf Z d_0,\qquad
(\iota-1)\Lambda^{S_6}=2\mathbf Z d_0.
\tag{9.9}
\]

The Hochschild--Serre cocycle of the cyclic algebra (9.5) is zero on
\(S_6=U_1^+\) and, with the norm-divisor convention (9.4), takes \(\iota\)
to \([\mathcal D]=3d_0\). If this were a \(U_1\)-coboundary, a cobounding
class would be fixed by \(S_6\), but (9.9) shows that every such value at
\(\iota\) lies in \(2\mathbf Z d_0\). Because
\(3d_0\notin2\mathbf Z d_0\), the cocycle is nonzero and represents the
unique element of order two.

## 10. Cohomology and arithmetic Brauer quotient

The exact integral cochain calculation gives

\[
H^1(U_1,\Lambda)\cong\mathbf Z/2\mathbf Z.
\tag{10.1}
\]

The absolute Galois action over \(F_D\) factors through \(U_1\). The kernel
acts trivially on the torsion-free lattice \(\Lambda\), and has no nonzero
continuous homomorphism to it, so inflation gives

\[
H^1(F_D,\Lambda)\cong H^1(U_1,\Lambda).
\tag{10.2}
\]

A smooth cubic surface is geometrically rational, so

\[
\operatorname{Br}(Y_{\overline{\mathbf Q}})=0.
\tag{10.3}
\]

The low-degree Hochschild--Serre sequence, together with
\(H^3(F_D,\mathbf G_m)=0\) for a number field, yields

\[
\operatorname{Br}(Y_{F_D})/
\operatorname{im}\operatorname{Br}(F_D)
\cong H^1(F_D,\Lambda)
\cong\mathbf Z/2\mathbf Z.
\tag{10.4}
\]

The explicit calculation (9.6)--(9.9) maps (9.5) to the nonzero
double-six cocycle. Hence it is the generator in (10.4). The same integral
cohomology computation for the full \(W(E_6)\) action gives

\[
\operatorname{Br}(Y)/\operatorname{im}\operatorname{Br}(\mathbf Q)=0.
\tag{10.5}
\]

## 11. Derivation firewalls

1. Equation (2.4), not a natural-subgroup enumeration, controls arbitrary
   finite \(L/\mathbf Q\).
2. The stronger result is the divisibility (2.7), with minimum degree as a
   corollary.
3. Field equality in (4.7) comes from stabilizers; no
   \(\delta=P(\theta)\) identity is inferred.
4. A finite-field nonzero minor is a rank-lower-bound certificate; the
   geometric linear-equivalence argument supplies the separate upper bound.
5. Vanishing on 12 lines is upgraded to a divisor equality only through
   degree exhaustion.
6. Unramifiedness and nontriviality are separate: (9.4) proves the former,
   while the explicit lattice calculation (9.6)--(9.9) and
   (10.1)--(10.4) prove the latter.
7. No local evaluation or rational-point conclusion follows from (9.5).
