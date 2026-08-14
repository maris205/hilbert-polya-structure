# HCS-C56 derivation package

Status: **DOCS_FINAL_NO_MORE_EDITS; exact derivation in the project
RELEASE_CANDIDATE.**  Every numerical statement below that is not inherited from
the frozen HCS-C55 surface is supplied by the current exact payload and
independently recomputed by the checker.

## 1. From a cubic form to its line scheme

Let $V=\mathbf Q^4$ and let
$\operatorname{Gr}(2,V)$ carry the tautological rank-two bundle $\mathcal S$.
A cubic form $F\in\operatorname{Sym}^3(V^\vee)$ restricts to every
two-plane $S\subset V$, giving a section

$$
\sigma_F:\operatorname{Gr}(2,V)\longrightarrow
\operatorname{Sym}^3(\mathcal S^\vee).
\tag{1.1}
$$

The scheme-theoretic zero locus of $\sigma_F$ is precisely $F_1(Y)$: a
two-plane is a zero exactly when its projective line lies on $Y=V(F)$.
Both the Grassmannian and the vector bundle have dimension/rank four.

For a smooth cubic surface over an algebraically closed field of
characteristic zero, Cayley--Salmon gives exactly 27 geometric lines.
Kass--Wickelgren Corollary 53 says that every corresponding zero of
$\sigma_F$ is simple.  Therefore the zero scheme is geometrically reduced,
zero-dimensional, and of length 27.  It is closed in the projective
Grassmannian, hence proper and quasi-finite, therefore finite.  Over
$\mathbf Q$ a finite geometrically reduced scheme is finite étale.  Thus

$$
F_1(Y)/\mathbf Q\text{ is finite étale of rank }27.
\tag{1.2}
$$

This step proves neither connectedness nor the Galois group.

## 2. Exact chart equations

On $U_{01}=\{p_{01}\ne0\}$ choose the row-reduced matrix

$$
\begin{pmatrix}1&0&a&b\\0&1&c&d\end{pmatrix}.
\tag{2.1}
$$

Using homogeneous coordinates $(s:t)$ on the line gives

$$
(u_0,u_1,u_2,u_3)=(s,t,as+ct,bs+dt).
\tag{2.2}
$$

Because $F$ is cubic, its restriction has a unique expansion

$$
F(s,t,as+ct,bs+dt)
=f_0s^3+f_1s^2t+f_2st^2+f_3t^3,
\tag{2.3}
$$

with $f_i\in\mathbf Q[a,b,c,d]$.  The chart of the line scheme is

$$
F_1(Y)\cap U_{01}
=\operatorname{Spec}\mathbf Q[a,b,c,d]/(f_0,f_1,f_2,f_3).
\tag{2.4}
$$

The intended exact lexicographic output has shape

$$
g(d),\quad
\lambda_c c+h_c(d),\quad
\lambda_b b+h_b(d),\quad
\lambda_a a+h_a(d),
\tag{2.5}
$$

where $\lambda_a\lambda_b\lambda_c\ne0$ and $\deg g=27$.
The release proof does not trust the shape label.  It defines

$$
A_g=\mathbf Q[d]/(g)
\tag{2.6}
$$

and sends

$$
d\mapsto\bar d,\qquad
a\mapsto-h_a(\bar d)/\lambda_a,\quad
b\mapsto-h_b(\bar d)/\lambda_b,\quad
c\mapsto-h_c(\bar d)/\lambda_c.
\tag{2.7}
$$

Direct substitution, denominator clearing, and four zero-remainder checks
show that (2.7) kills all $f_i$.  It therefore induces a surjective algebra map

$$
\mathbf Q[a,b,c,d]/(f_0,f_1,f_2,f_3)\twoheadrightarrow A_g,
\tag{2.8}
$$

where surjectivity holds because $\bar d$ generates $A_g$.  Reversing arrows,
this is a closed immersion

$$
\operatorname{Spec}(A_g)\hookrightarrow F_1(Y)\cap U_{01}.
\tag{2.9}
$$

This arrow direction is part of the certificate contract.

## 3. Four-prime irreducibility sieve

Let $g\in\mathbf Z[d]$ be primitive.  At a prime $p$ not dividing its
leading coefficient, reduction preserves its degree.  Suppose that
$g=uv$ is a nontrivial factorization in $\mathbf Q[d]$.  By Gauss's lemma it
may be chosen as a primitive factorization in $\mathbf Z[d]$.  Since
$p\nmid\operatorname{lc}(g)$, neither factor loses degree modulo $p$.

If $\bar g$ is squarefree and has irreducible factor degrees
$D_p=(d_{p,1},\ldots,d_{p,r_p})$, then $\bar u$ is a product of a subset of
those distinct irreducible factors.  Therefore

$$
\deg u\in S_p
:=\left\{\sum_{j\in J}d_{p,j}:J\subseteq\{1,\ldots,r_p\}\right\}.
\tag{3.1}
$$

For the target data,

$$
\begin{aligned}
S_7&=\{0,3,6,9,12,15,18,21,24,27\},\\
S_7\cap S_{19}&=\{0,6,9,12,15,18,21,27\},\\
S_7\cap S_{19}\cap S_{29}&=\{0,9,18,27\},\\
S_7\cap S_{19}\cap S_{29}\cap S_{37}&=\{0,27\}.
\end{aligned}
\tag{3.2}
$$

Thus no factor can have degree $1\le\deg u\le26$, and $g$ is irreducible
over $\mathbf Q$.  Since $\operatorname{char}\mathbf Q=0$, it is also
separable.  Consequently

$$
E:=\mathbf Q[d]/(g)
\tag{3.3}
$$

is a degree-$27$ number field and $\operatorname{Spec}(E)$ is finite étale and
connected.

The independent checker multiplies the stored modular factors back and checks
derivative gcds.  A list of factor degrees without the factors themselves
would be insufficient certificate data.

## 4. Why the main chart covers the global scheme

By (1.2), $F_1(Y)$ is finite étale of total rank 27.  By (2.9) and (3.3), it
contains $\operatorname{Spec}(E)$ as a closed subscheme of the chart
$F_1(Y)\cap U_{01}$.  A finite étale scheme over a field is a finite disjoint
union of spectra of finite separable fields, so every open subscheme is also
closed (equivalently, it is cut out by an idempotent).  Therefore
$F_1(Y)\cap U_{01}\hookrightarrow F_1(Y)$ is open-and-closed, and the
composition of (2.9) with this inclusion is a global closed immersion.

On global finite coordinate rings it gives a surjection between
finite-dimensional $\mathbf Q$-vector spaces of the same dimension.  It is
therefore an isomorphism.  Hence

$$
F_1(Y)=F_1(Y)\cap U_{01}\cong\operatorname{Spec}(E).
\tag{4.1}
$$

This degree comparison is the logical reason that no line lies outside the
chart.  It avoids the circular argument “we found 27 chart solutions, so all
lines were in the chart” unless simplicity, scheme length, and closed
immersion have first been established.

The five complementary-chart unit-ideal computations remain valuable: they
independently detect a wrong row-reduction convention, a wrong expression for
$p_{01}$, or a mismatched cubic.  They are a replay guard, not a substitute
for the scheme-theoretic argument.

## 5. Identifying the two fields

Let $\alpha$ be the class of $d$ in $E$.  Its 27 embeddings into
$\overline{\mathbf Q}$ give the 27 roots of $g$.  Formula (2.7) reconstructs
the remaining coordinates of the corresponding line from each root.

Let $K$ be the splitting field of $g$.  All line coordinates lie in $K$, so
all 27 lines are defined over $K$.  Conversely, any field over which all lines
are defined contains every $d$-coordinate and hence every root of $g$; if it
is normal, it contains $K$.  Thus $K$ is the least normal field of definition
of all lines and is the Galois closure of $E$.

The notation must never be collapsed:

$$
[E:\mathbf Q]=27,\qquad
K=E^{\mathrm{normal\ closure}},\qquad
[K:\mathbf Q]\text{ is determined by the Galois group.}
\tag{5.1}
$$

## 6. From finite-field factors to full $W(E_6)$

Let $G=\operatorname{Gal}(K/\mathbf Q)$.  Its faithful permutation action on
the roots is the action on the 27 lines.  Preservation of line incidence embeds
$G$ in $W(E_6)$ (Elsenhans--Jahnel Fact 3).  Irreducibility of $g$ makes this
action transitive.

The squarefree factorization at $p=37$ has cycle type

$$
(2,5,5,5,10).
\tag{6.1}
$$

Because the leading coefficient and discriminant of $g$ are nonzero modulo
$37$, the prime is unramified for this permutation algebra, and the
factorization supplies a Frobenius element $\varphi_{37}\in G$ with (6.1).
Its order is ten, so $\varphi_{37}^2$ has order five.

Elsenhans--Jahnel Lemma 8 now gives the dichotomy

$$
G=U\quad\text{or}\quad G=W(E_6),
\tag{6.2}
$$

where $U$ is the simple subgroup of index two and order 25920.  Their
Algorithm 10, Remark 11(c), Remark 12, and Remark 13 identify (6.1) as a
single $W(E_6)$ conjugacy class outside $U$.  Thus
$\varphi_{37}\notin U$, excluding the first case in (6.2).  Therefore

$$
G=W(E_6),\qquad |G|=2\cdot25920=51840.
\tag{6.3}
$$

The independent checker also enumerates all 51840 lattice transformations,
finds exactly 5184 elements with type (6.1), and verifies that every one lies
outside $U$ (zero such elements inside $U$).  This independent finite
verification hardens the source-based class identification.

### Parity firewall

Elsenhans--Jahnel Remark 5 explicitly says that the 27-line permutation
representation of $W(E_6)$ lands in $A_{27}$.  Hence the usual sign of
$\varphi_{37}$ as a permutation is $+1$.  In this argument “odd” means

$$
\varphi_{37}\notin U,
\tag{6.4}
$$

equivalently determinant $-1$ in the reflection representation.  Substituting
ordinary $S_{27}$ sign would make the exclusion step false.

## 7. Picard ranks

Over $\overline{\mathbf Q}$, a smooth cubic surface is the blow-up of
$\mathbf P^2$ in six points.  Therefore

$$
\operatorname{Pic}(Y_{\overline{\mathbf Q}})
=\mathbf ZH\oplus\bigoplus_{i=1}^6\mathbf ZE_i,
\qquad \rho(Y_{\overline{\mathbf Q}})=7,
\tag{7.1}
$$

with intersection form $\operatorname{diag}(1,-1,\ldots,-1)$ and canonical
class

$$
K_Y=-3H+E_1+\cdots+E_6.
\tag{7.2}
$$

The six roots in (2.8) span $K_Y^\perp$.  A vector fixed by every simple-root
reflection is orthogonal to all six roots, hence belongs to
$\mathbf QK_Y$.  Conversely $K_Y$ is fixed.  Thus

$$
\dim_{\mathbf Q}
\left(\operatorname{Pic}(Y_{\overline{\mathbf Q}})\otimes\mathbf Q\right)^{W(E_6)}
=1.
\tag{7.3}
$$

Since the Galois image is the full Weyl group, the geometric invariant lattice
has rank one.

The low-degree Hochschild--Serre sequence and Hilbert 90 give

$$
0\longrightarrow\operatorname{Pic}(Y)
\longrightarrow
\operatorname{Pic}(Y_{\overline{\mathbf Q}})^{G_{\mathbf Q}}
\longrightarrow\operatorname{Br}(\mathbf Q).
\tag{7.4}
$$

The Brauer group of a field is torsion.  Hence the cokernel of the first map in
(7.4) is torsion, so tensoring with $\mathbf Q$ gives equality of ranks, not
necessarily equality of integral groups.  Because a cubic surface has
$\operatorname{Pic}^0=0$,

$$
\rho(Y/\mathbf Q)=1.
\tag{7.5}
$$

## 8. Rational lines and extension degrees

From (4.1), an $L$-rational line for a finite extension $L/\mathbf Q$ is an
$L$-point of $\operatorname{Spec}(E)$, equivalently a $\mathbf Q$-algebra map

$$
E\longrightarrow L.
\tag{8.1}
$$

Since $E$ is a field, this map is injective.  Its image is a conjugate degree-27
subfield of $L$, and the tower law gives

$$
[L:\mathbf Q]=[L:E'][E':\mathbf Q]
=27[L:E'].
\tag{8.2}
$$

Taking $L=\mathbf Q$ is impossible, proving that $Y$ has no rational line.
This does not address $Y(\mathbf Q)$: a rational point need not lie on a
rational line.

## 9. Projective invariance

For $A\in\operatorname{GL}_4(\mathbf Q)$, the induced automorphism of
$\operatorname{Gr}(2,4)$ carries the zero scheme of $\sigma_F$ isomorphically
to the zero scheme for $F\circ A^{-1}$.  Multiplying $F$ by
$\lambda\in\mathbf Q^\times$ does not change its zero section.  Therefore all
scheme, field, Galois-action, and Picard-rank conclusions are invariant under
the projective ambiguity allowed in C55.

The displayed eliminant $g$ itself is not projectively intrinsic: it depends
on the chosen chart and separating coordinate.  What is intrinsic is the
finite étale algebra and its Galois action.

## 10. Certified exact payload

The machine lane supplies, and the independent checker derives:

1. the exact C55 stratified source lock and all 20 imported coefficient rows;
2. rational and selected-prime smoothness replays;
3. all four chart equations, the full coefficient arrays of $g,h_a,h_b,h_c$,
   and four direct zero remainders;
4. all five complementary-chart unit ideals;
5. complete modular factors, multiplication checks, gcd checks, subset-sum
   sets, and their intersection;
6. the Picard lattice, roots, line classes, group order, index-two kernel,
   target-class membership, and fixed rank;
7. independent semantic derivation of every theorem boolean and adversarial
   rebound rejection of every scalar leaf.

All 10 semantic gates, all 2684 adversarial rebound cases, and all 15 tests
pass at code/results prefreeze.  The canonical identifiers are recorded in
`README.md` and `INTEGRITY_REPORT.md`; temporary reconnaissance digests remain
outside theorem provenance.  The official paper-build identifiers are
recorded externally.  The scoped manifest remains the default code/results
identity, while a 46-entry self-excluding full-project successor is verified
separately as a release-wide ledger.  Commit provenance remains unset at this
no-commit release-candidate milestone.
