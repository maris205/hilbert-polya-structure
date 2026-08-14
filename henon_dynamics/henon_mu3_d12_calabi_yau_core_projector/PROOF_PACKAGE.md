# HCS-C52 proof package

Status: **release proof; exact producer/checker replay passed**

## 1. Statement under proof

Let

\[
K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0,
\]

and let \(X\subset\mathbf P^7_K\) be the smooth complete intersection

\[
C=\sum_{i=0}^{7}x_i^3=0,\qquad
Q=\sum_{i=0}^{6}x_ix_{i+1}+\rho x_7x_0=0.          \tag{P1}
\]

The claims proved here are:

1. the projective monomial source stabilizer of the ordered pair
   \((C,Q)\) is the order-\(24\) group
   \(G=\operatorname{Dih}(C_{12})\);
2. the graph average of \(G\), composed with the explicit middle
   Chow--Künneth projector, cuts out a \(K\)-rational rank-\(10\)
   summand of \(H^5(X)\);
3. its Hodge ledger is \((1,4,4,1)\), while the complementary ledger is
   \((0,79,79,0)\); and
4. rank \(10\) is minimal among idempotents in the graph algebra
   \(\mathbf Q[G]\) that retain the \(H^{4,1}\) line.

All claims about smoothness and the dimensions
\(h^{4,1}=1,\ h^{3,2}=83\) are inherited from C50--C51.  The proof below
does not promote the graph projector to a multiplicative
Chow--Künneth decomposition and does not infer coniveau, automorphy, or a
functional equation.

## 2. Complete projective monomial stabilizer

### Lemma 2.1: reduction to a finite phase system

Every projective monomial transformation preserving the two source
equations has a representative

\[
x_i\longmapsto \rho^{e_i}x_{\sigma(i)},\qquad
e_i\in\mathbf F_3,\qquad e_0=0,                    \tag{P2}
\]

where \(\sigma\) is an automorphism of the eight-cycle supporting \(Q\).

### Proof

If \(x_i\mapsto a_ix_{\sigma(i)}\) sends \(C\) to a scalar multiple
\(\alpha C\), coefficient comparison gives \(a_i^3=\alpha\) for every
\(i\).  Dividing all \(a_i\) by \(a_0\) changes only the projective lift,
and the resulting ratios lie in \(\mu_3(K)\).  This proves the phase
normalization in (P2).

The squarefree monomials in \(Q\) are exactly the edges of an
eight-cycle.  A monomial transformation preserving \(Q\) up to scalar
must permute this support, so \(\sigma\) is a rotation or reflection of
that cycle.  This leaves \(16\) permutations and \(3^7\) normalized
phase vectors before the edge equations are imposed.  \(\square\)

### Lemma 2.2: exact enumeration

Let \(c(E)\) be zero on the seven ordinary edges and one on
\(\{7,0\}\).  A normalized pair \((\sigma,e)\) is a source symmetry if
and only if there is \(q_g\in\mathbf F_3\) such that

\[
c(\{i,i+1\})+e_i+e_{i+1}
=q_g+c(\{\sigma(i),\sigma(i+1)\})                  \tag{P3}
\]

for all cyclic indices \(i\).  The solution set consists of exactly the
\(24\) rows displayed in the derivation package.

### Proof

Equation (P3) is direct coefficient comparison in
\(Q(gx)=\rho^{q_g}Q(x)\).  For each of the \(16\) support permutations
it is an affine linear system over \(\mathbf F_3\).  Row reduction gives
solutions only for

\[
r_0,r_2,r_4,r_6,s_1,s_3,s_5,s_7,                  \tag{P4}
\]

three solutions for each, and no solutions for the remaining eight
permutations.  Substitution of every listed word into (P3) verifies
existence; the exhausted \(16\)-permutation list verifies completeness.
Thus the projective monomial source stabilizer has order \(24\).
\(\square\)

### Lemma 2.3: group presentation

For

\[
\begin{aligned}
r&:\ \sigma=(6,7,0,1,2,3,4,5),&
e&=(0,1,1,0,1,0,1,0),\\
s&:\ \sigma=(7,6,5,4,3,2,1,0),&
e&=(0,1,0,1,0,1,0,1),
\end{aligned}                                      \tag{P5}
\]

one has

\[
r^{12}=s^2=1,\qquad srs=r^{-1},                    \tag{P6}
\]

and \(\langle r,s\rangle\) has \(24\) projective elements.

### Proof

Exact phase-permutation multiplication proves (P6).  The powers
\(1,r,\ldots,r^{11}\) are distinct, and none of the elements \(sr^k\)
is a power of \(r\); hence the presented subgroup has \(24\) elements.
By Lemma 2.2 it is the complete projective monomial source stabilizer.
We write it as \(\operatorname{Dih}(C_{12})\), explicitly meaning the
order-\(24\) semidirect product \(C_{12}\rtimes C_2\).  This notation
does not assert that \(G\) is the full automorphism group of \(X\).
\(\square\)

## 3. Chow projectors without an MCK hypothesis

Let \(h=c_1(\mathcal O_X(1))\).  Since \(X\) is a \((2,3)\) complete
intersection,

\[
\deg X=\int_Xh^5=6.                                \tag{P7}
\]

Define

\[
\pi_{2i}=\frac1{6}h^{5-i}\times h^i
\quad(0\le i\le5),\qquad
\pi_5=\Delta_X-\sum_{i=0}^{5}\pi_{2i}.             \tag{P8}
\]

### Lemma 3.1: orthogonal idempotence

The six \(\pi_{2i}\) are mutually orthogonal idempotents in
\(\operatorname{CH}^5(X\times_KX)_{\mathbf Q}\), and \(\pi_5\) is an
idempotent orthogonal to all of them.

### Proof

For decomposable codimension-five correspondences on a fivefold,

\[
(a\times b)\circ(c\times d)
=\left(\int_Xda\right)c\times b.                   \tag{P9}
\]

Taking \(a=h^{5-i}, b=h^i, c=h^{5-j}, d=h^j\), the integral in (P9)
vanishes unless \(i=j\), and equals \(6\) when \(i=j\).  Including the
two factors \(1/6\) proves

\[
\pi_{2i}\circ\pi_{2j}=\delta_{ij}\pi_{2i}.         \tag{P10}
\]

The identities for the complementary projector \(\pi_5\) follow by
expansion against \(\Delta_X\).  Weak Lefschetz shows that the
nonmiddle cohomology is generated by the powers of \(h\), so the
realization of \(\pi_5\) is precisely \(H^5(X)\).  No multiplicativity
claim is used.  Moreover,
\(\pi_{2i}^t=\pi_{10-2i}\), so the sum of the ambient projectors and
\(\pi_5\) are self-transpose.  \(\square\)

### Lemma 3.2: the Reynolds correspondence

Let

\[
e_G=\frac1{24}\sum_{g\in G}[\Gamma_g].             \tag{P11}
\]

Then \(e_G\) and \(\pi_5\) commute, \(e_G^2=e_G\), and \(e_G^t=e_G\).
Consequently

\[
\pi_{\mathrm{core}}=\pi_5e_G,\qquad
\pi_{\mathrm{lev}}=\pi_5-\pi_5e_G                 \tag{P12}
\]

are mutually orthogonal self-transpose Chow idempotents.

### Proof

Every element of \(G\) is induced by a projective linear transformation,
so \(g^*h=h\).  Its graph therefore commutes with every correspondence
in (P8), and hence with \(\pi_5\).  Graph composition and transposition
give

\[
[\Gamma_g][\Gamma_h]=[\Gamma_{gh}],\qquad
[\Gamma_g]^t=[\Gamma_{g^{-1}}].                    \tag{P13}
\]

The first identity and the fact that each group element occurs exactly
\(24\) times in the double sum prove \(e_G^2=e_G\); inversion permutes
the group, proving \(e_G^t=e_G\).  Commutation with \(\pi_5\), followed
by direct expansion, proves every assertion in (P12) inside the Chow
ring modulo rational equivalence.  \(\square\)

## 4. Residue-twisted Cayley action

Let

\[
\mathscr F=yC+zQ,\qquad
R=K[x_0,\ldots,x_7,y,z]/J(\mathscr F),             \tag{P14}
\]

with

\[
\deg x_i=(0,1),\qquad
\deg y=(1,-3),\qquad
\deg z=(1,-2).                                     \tag{P15}
\]

The Cayley-ring identification gives

\[
H^{4,1}_{\mathrm{prim}}(X)\cong R_{1,-3},\qquad
H^{3,2}_{\mathrm{prim}}(X)\cong R_{2,-3}.          \tag{P16}
\]

### Lemma 4.1: correct projective action

Choose a lift \(M_g\in\operatorname{GL}_8(K)\), and define \(A_g\) by

\[
\binom C Q(M_gx)=A_g\binom C Q(x).                 \tag{P17}
\]

The residue action on the Jacobian ring is the polynomial pullback of

\[
(x,(y,z)^t)\longmapsto
(M_gx,A_g^{-t}(y,z)^t),                            \tag{P18}
\]

multiplied by

\[
\omega(g)=\frac{\det M_g}{\det A_g}.               \tag{P19}
\]

It is independent of the scalar lift \(M_g\).

### Proof

The transformation in (P18) fixes \(yC+zQ\).  Its Jacobian on the
ambient Cayley variables is

\[
\det(M_g)\det(A_g^{-t})
=\frac{\det M_g}{\det A_g},                        \tag{P20}
\]

which is the orientation multiplier in the residue map.  If
\(M_g\) is replaced by \(\lambda M_g\), then

\[
A_g\longmapsto
\operatorname{diag}(\lambda^3,\lambda^2)A_g.       \tag{P21}
\]

For a bidegree-\((p,-3)\) Cayley representative, the polynomial
pullback under this lift change has total scalar \(\lambda^{-3}\):
each \(x\) contributes \(\lambda\), while each \(y\) and \(z\)
contributes respectively \(\lambda^{-3}\) and \(\lambda^{-2}\).
The determinant ratio in (P19) changes by \(\lambda^3\), so the two
factors cancel.  As an explicit control, \(\lambda=2\) gives
\(2^{-3}\) from the polynomial and \(2^3\) from the determinant ratio.
Thus the action descends to the projective transformation.  In
particular, the determinant ratio cannot be dropped merely because it
equals one for the chosen generator lifts.  \(\square\)

## 5. Exact character and Hodge ranks

The ambient bidegree-\((2,-3)\) space is

\[
y^2K[x]_3\oplus yzK[x]_2\oplus z^2K[x]_1,          \tag{P22}
\]

of dimension \(120+36+8=164\).  The relevant Jacobian relations have
rank \(81\), so \(\dim R_{2,-3}=83\), while \(R_{1,-3}=Ky\).

Using the action of Lemma 4.1 on the quotient produces

\[
\operatorname{tr}(r^k)=
(83,-1,-3,-1,-7,-1,3,-1,-7,-1,-3,-1)              \tag{P23}
\]

for \(0\le k\le11\), and

\[
\operatorname{tr}(sr^k)=3.                         \tag{P24}
\]

The exact character inner products give one-dimensional multiplicities

\[
(4,1,3,3)                                          \tag{P25}
\]

and two-dimensional multiplicities

\[
(7,8,6,8,7).                                       \tag{P26}
\]

Their weighted sum is \(83\).  The trivial representation therefore
occurs four times in \(H^{3,2}\), while \(R_{1,-3}=Ky\) is itself
trivial.  Since \(e_G\) projects onto invariants,

\[
\dim e_GH^5(X)=1+4+4+1=10.                         \tag{P27}
\]

The complementary dimension is \(168-10=158\).  This proves

\[
\begin{aligned}
e_GH^5(X)&:\ (4,1)^1+(3,2)^4+(2,3)^4+(1,4)^1,\\
(1-e_G)H^5(X)&:\ (3,2)^{79}+(2,3)^{79}.            \tag{P28}
\end{aligned}
\]

After one Tate twist, the first line has Hodge ledger
\((3,0)^1+(2,1)^4+(1,2)^4+(0,3)^1\).  This is a
Calabi--Yau-threefold Hodge **type**, not the cohomology of a constructed
Calabi--Yau threefold.  After the C51 twist by two, the second line has
types \((1,0)^{79}+(0,1)^{79}\); this does not construct an abelian
variety over \(K\).

The trace computation in (P23)--(P26) is finite exact linear algebra.
The release theorem requires a producer certificate and an independently
implemented checker that reconstructs the quotient action, includes the
factor (P19), and rejects mutations of the phase table, determinant
ratio, relation rank, and character decomposition.

## 6. Optimality inside the graph algebra

### Proposition 6.1

Let \(q\in\mathbf Q[G]\) be an idempotent whose graph action is the
identity on \(H^{4,1}(X)\).  Then

\[
\operatorname{rank}(qH^5(X))\ge10,                 \tag{P29}
\]

and equality is attained by \(e_G\).

### Proof

For \(a=\sum_ga_gg\in\mathbf Q[G]\), the action on every copy of the
trivial representation is multiplication by the same augmentation

\[
\varepsilon(a)=\sum_ga_g.                          \tag{P30}
\]

If \(a\) is idempotent, then \(\varepsilon(a)\in\{0,1\}\).
Because \(H^{4,1}\) is trivial, retaining it forces
\(\varepsilon(a)=1\).  The same scalar therefore retains all four
trivial copies in \(H^{3,2}\), and the rational graph action also retains
the conjugate pieces in \(H^{2,3}\) and \(H^{1,4}\).  The retained rank
is at least \(1+4+4+1=10\).  The group average \(e_G\) acts as identity
exactly on the full invariant subspace, so it attains the bound.
\(\square\)

Proposition 6.1 is a theorem only about the image of the rational group
algebra generated by graph correspondences.  It does not exclude
non-graph algebraic correspondences, coefficient extension, or a
rank-two summand in another category.

## 7. Realization and claim boundary

Because \(\pi_{\mathrm{core}}\) and \(\pi_{\mathrm{lev}}\) are
\(K\)-rational Chow correspondences with rational coefficients, every
Weil cohomology realizes them functorially.  In particular, they define
Betti, de Rham, and \(G_K\)-equivariant \(\ell\)-adic splittings induced
by the same Chow idempotents.  This realization-compatibility is not a
certified strict compatible system with computed common Frobenius
polynomials.

This conclusion does **not** prove:

- that the rank-\(158\) complement has coniveau one;
- that it is \(H^1(A)(-2)\) for an abelian variety \(A/K\);
- finite-dimensionality or abelian type of either motive;
- automorphy or a Hasse--Weil functional equation;
- a new convergence or continuation half-plane for the H\'enon Euler
  germ;
- a Riemann divisor or self-adjoint Hilbert--P\'olya generator; or
- that \(G\) is the full automorphism group of \(X\).

Those exclusions are part of the theorem statement, not merely
editorial caveats.
