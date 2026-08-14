# HCS-C52 theorem package

Status: **release theorem; exact B0--B2 replay passed**

## 1. Frozen source

Let

\[
 K=\mathbf Q(\rho),\qquad \rho^2+\rho+1=0,
\]

and let \(X\subset\mathbf P^7_K\) be the smooth fivefold

\[
 C(x)=\sum_{i=0}^{7}x_i^3=0,
 \qquad
 Q(x)=\sum_{i=0}^{6}x_ix_{i+1}+\rho x_7x_0=0.       \tag{1}
\]

Smoothness in characteristic zero and the Hodge numbers

\[
 h^{4,1}(X)=h^{1,4}(X)=1,
 \qquad
 h^{3,2}(X)=h^{2,3}(X)=83                         \tag{2}
\]

are inherited from C50--C51.  This package neither changes the closing edge
in \(Q\) nor re-proves smoothness from finite-prime data.

The C51 odd packet is

\[
 O_4=H^5(X)(2),                                    \tag{3}
\]

with Hodge types

\[
 (2,-1)^1+(1,0)^{83}+(0,1)^{83}+(-1,2)^1.          \tag{4}
\]

## 2. Projective monomial source group

A projective monomial source symmetry is represented by

\[
 g:x_i\longmapsto \rho^{e_i}x_{\sigma(i)},
 \qquad e_i\in\mathbf F_3,                          \tag{5}
\]

modulo a common phase, and is required to preserve the two equations in
(1) up to their individual nonzero scalars.  Let \(G_{\mathrm{mon}}\) be
the group of all such maps.

Define permutations of \(\mathbf Z/8\mathbf Z\) by

\[
 r_k(i)=i+k,
 \qquad
 s_k(i)=k-i.                                       \tag{6}
\]

Solving the phase equations gives precisely the eight permutations

\[
 r_0,r_2,r_4,r_6,s_1,s_3,s_5,s_7,                 \tag{7}
\]

with three normalized phase solutions for each.  Hence

\[
 |G_{\mathrm{mon}}|=24.                            \tag{8}
\]

One choice of generators is

\[
\begin{aligned}
 r:&\quad
 \sigma=(6,7,0,1,2,3,4,5),
 &e&=(0,1,1,0,1,0,1,0),\\
 s:&\quad
 \sigma=(7,6,5,4,3,2,1,0),
 &e&=(0,1,0,1,0,1,0,1).
\end{aligned}                                      \tag{9}
\]

Both send \(C\) to \(C\) and \(Q\) to \(\rho Q\), and exact projective
composition gives

\[
 r^{12}=s^2=1,
 \qquad
 srs=r^{-1}.                                       \tag{10}
\]

Thus

\[
 G_{\mathrm{mon}}\cong
 \operatorname{Dih}(C_{12}),                       \tag{11}
\]

where \(\operatorname{Dih}(C_{12})\) has order \(24\).  Equation (11)
classifies only the projective monomial source stabilizer.  It is not a
claim about the full automorphism group of \(X\).

## 3. Algebraic middle projector

Let \(h=c_1(\mathcal O_X(1))\).  Since \(X\) has degree \(6\),

\[
 \int_Xh^5=6.                                      \tag{12}
\]

For \(0\le i\le5\), define

\[
 \pi_{2i}=\frac1{6}h^{5-i}\times h^i
 \in\operatorname{CH}^5(X\times_KX)_{\mathbf Q},   \tag{13}
\]

and put

\[
 \pi_5=\Delta_X-\sum_{i=0}^{5}\pi_{2i}.            \tag{14}
\]

The correspondences in (13) are mutually orthogonal idempotents.  Hence
\(\pi_5\) is an idempotent cutting out the middle cohomology.  Every
\(g\in G_{\mathrm{mon}}\) is induced by a projective linear map and fixes
\(h\), so \(\pi_5\) commutes with every graph correspondence
\([\Gamma_g]\).

Define the Reynolds graph projector

\[
 e_G=\frac1{24}\sum_{g\in G_{\mathrm{mon}}}[\Gamma_g]              \tag{15}
\]

and the two middle projectors

\[
 \pi_{\mathrm{core}}=\pi_5e_G,
 \qquad
 \pi_{\mathrm{lev}}=\pi_5-\pi_5e_G.                \tag{16}
\]

Then, in \(\operatorname{CH}^5(X\times_KX)_{\mathbf Q}\),

\[
 \pi_{\mathrm{core}}^2=\pi_{\mathrm{core}},
 \qquad
 \pi_{\mathrm{lev}}^2=\pi_{\mathrm{lev}},
 \qquad
 \pi_{\mathrm{core}}\pi_{\mathrm{lev}}=0,          \tag{17}
\]

and both projectors are self-transpose.  These are Chow identities modulo
rational equivalence, not merely cohomological identities.

## 4. Residue-twisted Cayley representation

Set

\[
 \mathscr F=yC+zQ,                                  \tag{18}
\]

with bidegrees

\[
 \deg x_i=(0,1),
 \qquad
 \deg y=(1,-3),
 \qquad
 \deg z=(1,-2),                                     \tag{19}
\]

and let

\[
 R=K[x_0,\ldots,x_7,y,z]/J(\mathscr F).             \tag{20}
\]

The primitive Hodge pieces are

\[
 H^{4,1}_{\mathrm{prim}}(X)\cong R_{1,-3},
 \qquad
 H^{3,2}_{\mathrm{prim}}(X)\cong R_{2,-3}.          \tag{21}
\]

For a lift \(M_g\in\operatorname{GL}_8(K)\), write

\[
 \binom{C}{Q}(M_gx)=A_g\binom{C}{Q}(x).             \tag{22}
\]

The induced Cayley transformation is

\[
 (x,(y,z)^t)\longmapsto
 (M_gx,A_g^{-t}(y,z)^t).                             \tag{23}
\]

On residue classes its polynomial pullback is multiplied by

\[
 \omega(g)=\frac{\det M_g}{\det A_g}.               \tag{24}
\]

The factor (24) is mandatory.  Together with the bidegree in (19), it
makes the action independent of the scalar lift of the projective map.

With the generators in (9), the exact character on \(R_{2,-3}\) is

\[
 \operatorname{tr}(r^k)=
 (83,-1,-3,-1,-7,-1,3,-1,-7,-1,-3,-1)              \tag{25}
\]

for \(0\le k\le11\), and

\[
 \operatorname{tr}(sr^k)=3                          \tag{26}
\]

for every \(k\).  The four one-dimensional character multiplicities,
ordered by

\[
 (r,s)\longmapsto(1,1),(1,-1),(-1,1),(-1,-1),       \tag{27}
\]

are

\[
 (4,1,3,3).                                         \tag{28}
\]

For the two-dimensional characters

\[
 \vartheta_j(r^k)=2\cos\!\left(\frac{\pi jk}{6}\right),
 \qquad
 \vartheta_j(sr^k)=0,
 \qquad 1\le j\le5,                                \tag{29}
\]

the multiplicities are

\[
 (7,8,6,8,7).                                       \tag{30}
\]

The dimension check is

\[
 4+1+3+3+2(7+8+6+8+7)=83.                          \tag{31}
\]

The one-dimensional space \(R_{1,-3}=Ky\) is the trivial representation.

## 5. Dihedral middle-motive decomposition theorem

### Theorem A

The projectors in (16) are \(K\)-rational Chow projectors with rational
coefficients.  The same Chow projectors split every Weil realization; in
particular, their \(\ell\)-adic realizations are \(G_K\)-equivariant
idempotents.  This realization-compatibility is not a claim that common
Frobenius polynomials have already been computed or that a strict compatible
system has been certified.  The invariant core has rank \(10\) and Hodge
ledger

\[
 \pi_{\mathrm{core}}H^5(X):
 \quad
 (4,1)^1+(3,2)^4+(2,3)^4+(1,4)^1.                  \tag{32}
\]

The complement has rank \(158\) and ledger

\[
 \pi_{\mathrm{lev}}H^5(X):
 \quad
 (3,2)^{79}+(2,3)^{79}.                             \tag{33}
\]

After one Tate twist, (32) has Calabi--Yau-threefold Hodge type

\[
 (3,0)^1+(2,1)^4+(1,2)^4+(0,3)^1.                  \tag{34}
\]

After the C51 twist by two, (33) becomes

\[
 (1,0)^{79}+(0,1)^{79}.                             \tag{35}
\]

Equations (34)--(35) are statements about Hodge realizations.  They do not
construct a Calabi--Yau threefold or an abelian variety of dimension \(79\)
over \(K\).

## 6. Graph-algebra optimum

Let

\[
 \varepsilon:\mathbf Q[G_{\mathrm{mon}}]\longrightarrow\mathbf Q,
 \qquad
 \varepsilon\!\left(\sum_ga_gg\right)=\sum_ga_g    \tag{36}
\]

be the augmentation.  Every element of the group algebra acts on every
trivial copy by the same scalar \(\varepsilon(a)\).

### Theorem B

Let \(q\in\mathbf Q[G_{\mathrm{mon}}]\) be an idempotent whose graph
correspondence acts as the identity on \(H^{4,1}(X)\).  Then it acts as the
identity on all four trivial copies in \(H^{3,2}(X)\), and by complex
conjugation on the corresponding pieces in \(H^{2,3}(X)\) and
\(H^{1,4}(X)\).  Consequently

\[
 \operatorname{rank}(qH^5(X))\ge10.                 \tag{37}
\]

The bound is sharp, because \(e_G\) attains rank \(10\).  Therefore no
idempotent in \(\mathbf Q[G_{\mathrm{mon}}]\) cuts out the desired
rank-two extreme Hodge pair.

Theorem B is confined to the graph algebra.  It does not exclude a
\(K\)-rational algebraic correspondence outside \(\mathbf Q[G]\), a
correspondence after extending coefficients, or a rank-two summand in a
different category.

## 7. Route-A and successor scope

The new C52 delta is:

1. an exact source monomial group of order \(24\);
2. a \(K\)-rational algebraic middle projector with compatible
   realizations;
3. a rank-10/rank-158 Hodge decomposition; and
4. an optimality theorem for the natural graph algebra.

C52 inherits the C50--C51 analytic germ and normalized-semifinite
determinant.  It proves no new half-plane, automorphy, Hasse--Weil
functional equation, full H\'enon functional equation, Riemann divisor, or
self-adjoint Hilbert--P\'olya generator.

Full rank-10 Frobenius polynomials, local irreducibility, and additional
incidence correspondences are the C53 gate and are not claimed here.
