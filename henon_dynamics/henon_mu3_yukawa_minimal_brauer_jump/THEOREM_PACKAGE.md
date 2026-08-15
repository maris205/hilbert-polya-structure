# HCS-C57 theorem package

Status: **PAPER_COMPILED; PAPER_HOSTILE_PASS; THEOREM_TARGET_LOCKED; machine
PREFREEZE_CODE_RESULTS_PASS; NOT_RELEASED.**

This file states the exact theorem target and the finite premises that a C57
release must certify. The mathematical implication from those premises is
proved in PROOF_PACKAGE.md. The project-local exact producer and independent
checker now certify C57-EXACT-0 through C57-EXACT-7 at
`PREFREEZE_CODE_RESULTS_PASS`, with a strict schema and scoped manifest. These
remain machine-prefreeze theorem inputs. The separately bound paper is now
compiled and hostile-audited, but neither layer is yet a project release.

## 1. Frozen object

Let \(Y/\mathbf Q\) be the smooth, geometrically irreducible cubic surface
fixed by HCS-C55. Let \(E/\mathbf Q\) and \(K/\mathbf Q\) be the fields proved
in HCS-C56:

\[
[E:\mathbf Q]=27,\qquad E\ne K,\qquad
\operatorname{Gal}(K/\mathbf Q)=W(E_6),\qquad |W(E_6)|=51840.
\tag{1.1}
\]

The field \(E\) is non-Galois and parameterizes one line; \(K\) is its normal
closure and the common normal field of all 27 lines.

Write

\[
\Lambda=\operatorname{Pic}(Y_{\overline{\mathbf Q}})
\tag{1.2}
\]

for the rank-seven geometric Picard lattice with its faithful \(W(E_6)\)
action.

## 2. Double-six fields

Let \(D=\{\mathcal E,\mathcal G\}\) be an unordered double-six. Here
\(\mathcal E\) and \(\mathcal G\) also denote the effective sums of the six
lines in its two sixers. Define

\[
U_1=\operatorname{Stab}_{W(E_6)}(D)
\cong S_6\times C_2,
\qquad |U_1|=1440,
\qquad [W(E_6):U_1]=36.
\tag{2.1}
\]

Let \(U_1^+\cong S_6\) be the index-two subgroup preserving the two sixers
separately, and put

\[
F_D=K^{U_1},\qquad F_D'=K^{U_1^+}.
\tag{2.2}
\]

The second subgroup needed only for the **complete classification argument**
is the classical \(U_3\) of index

\[
[W(E_6):U_3]=720.
\tag{2.3}
\]

No natural-stabilizer enumeration may replace the source theorem that
produces the \(U_1/U_3\) dichotomy for arbitrary finite base change.

## 3. Exact premises certified at machine PREFREEZE

The live certificate/checker tuple satisfies the following contract. The
imperative wording is retained to record exactly what every replay must
continue to enforce.

### C57-EXACT-0: frozen import

The importer must verify the frozen C56 theorem, certificate, Route, and
scoped identity; reconstruct the exact cubic and line shape; and preserve the
C56 layered contract:

\[
\text{project RELEASE_FROZEN},\quad
\text{documentation DOCS_FINAL_NO_MORE_EDITS},\quad
\text{machine PREFREEZE_CODE_RESULTS_PASS}.
\tag{3.1}
\]

### C57-EXACT-1: incidence carrier

For the degree-27 eliminant \(g\), the exact divided-difference incidence
polynomial \(J(x,y)\) must give, over \(\mathbf Q[x]/(g)\),

\[
H_x(y)=\gcd_y(g(y),J(x,y)),\qquad
\deg_y H_x=10,\qquad g=H_xQ_x,
\tag{3.2}
\]

with \(\deg_yQ_x=17\) and
\(\gcd(H_x,y-x)=1\). Exact all-and-only replays must give

\[
135\text{ meeting pairs},\qquad
72\text{ sixers},\qquad
36\text{ double-sixes}.
\tag{3.3}
\]

### C57-EXACT-2: subgroup and cohomology data

The checker must reconstruct \(W(E_6)\), \(U_1\), \(U_1^+\), and their actions
on the 27 lines and on \(\Lambda\). It must verify

\[
\begin{gathered}
|U_1|=1440,\qquad [W(E_6):U_1]=36,\qquad
\operatorname{orb}_{U_1}(27)=[12,15],\\
\operatorname{core}_{W(E_6)}(U_1)=1,\qquad
N_{W(E_6)}(U_1)=U_1,\\
H^1(W(E_6),\Lambda)=0,\qquad
H^1(U_1,\Lambda)\cong\mathbf Z/2\mathbf Z.
\end{gathered}
\tag{3.4}
\]

The last computation must use exact integral cocycles and Smith normal form.
It verifies the selected field; it does not prove the universal
\(U_1/U_3\) classification.

### C57-EXACT-3: degree-36 resolvers

There must be exact orbit polynomials

\[
R_\theta(T)=\prod_D(T-\theta_D),\qquad
R_\delta(T)=\prod_D(T-\delta_D)
\in\mathbf Q[T]
\tag{3.5}
\]

of degree 36, with exact coefficient reconstruction, separability,
irreducibility witnesses, and all-and-only double-six binding.

### C57-EXACT-4: orientation and fixed fields

For an oriented sixer invariant \(\beta_D\), the checker must verify

\[
\delta_D=\beta_D^2,\qquad
\operatorname{Stab}(\theta_D)=
\operatorname{Stab}(\delta_D)=U_1,\qquad
\operatorname{Stab}(\beta_D)=U_1^+.
\tag{3.6}
\]

Consequently

\[
\mathbf Q(\theta_D)=F_D=\mathbf Q(\delta_D),\qquad
F_D'=F_D(\beta_D)=F_D(\sqrt{\delta_D}).
\tag{3.7}
\]

Equation (3.7) is a stabilizer/fixed-field result. It does not include an
expanded identity \(\delta=P(\theta)\).

### C57-EXACT-5: twelve-line carrier

Over \(F_D=\mathbf Q(\theta_D)\), an exact monic degree-12 carrier
\(A_{12}(d)\) and degree-15 complement \(B_{15}(d)\) must satisfy

\[
g(d)=A_{12}(d)B_{15}(d)
\tag{3.8}
\]

with zero division remainder and independent forward multiply-back. Its
twelve roots must be exactly the lines in \(D\).

### C57-EXACT-6: determinant-defined quartic

Let

\[
c=[u_0^3]F=75081586157.
\tag{3.9}
\]

The map from \(F\cdot H^0(\mathbf P^3,\mathcal O(1))\) to the four
coefficients of

\[
u_0^4,\quad u_0^3u_1,\quad u_0^3u_2,\quad u_0^3u_3
\tag{3.10}
\]

has a triangular \(4\times4\) matrix with diagonal
\((c,c,c,c)\). Its determinant is

\[
c^4=
31778526453059635681033276764499400992765201\ne0.
\tag{3.11}
\]

Therefore every quartic class modulo
\(F\cdot H^0(\mathbf P^3,\mathcal O(1))\) has a unique representative in
which the four coefficients in (3.10) vanish. Let
\(\mathcal M=(m_0,\ldots,m_{30})\) be the resulting ordered basis,
with \(m_0=u_0^2u_1^2\). Restriction to the twelve carrier lines gives

\[
M_D\in\operatorname{Mat}_{60\times31}(F_D).
\tag{3.12}
\]

After deleting column zero, the rows

\[
0,\ldots,10,\quad12,\ldots,20,\quad24,\ldots,29,\quad
36,37,38,48
\tag{3.13}
\]

must define a nonzero \(30\times30\) minor \(N_D\). The coefficient vector

\[
q_D=(1,q_1,\ldots,q_{30})
\tag{3.14}
\]

is defined by Cramer's rule for that minor, and

\[
Q_D=\sum_{i=0}^{30}q_i m_i.
\tag{3.15}
\]

All 60 restrictions must vanish for every one of the 36 conjugate
double-sixes. For the upper half of the rank sandwich, choose an
\(F_D\)-rational hyperplane section \(H_0\); both
\(\mathcal E+\mathcal G\) and \(4H_0\) are \(F_D\)-rational. If

\[
\mathcal E+\mathcal G-4H_0=\operatorname{div}(r)
\]

over \(\overline{F_D}\), then \(c_\sigma=\sigma(r)/r\) is a scalar
cocycle. Hilbert theorem 90 writes \(c_\sigma=\sigma(a)/a\), so
\(r/a\in F_D(Y)^*\). Thus the corresponding
section of \(\mathcal O_Y(4)\) descends to \(F_D\), and the surjection

\[
H^0(\mathbf P^3_{F_D},\mathcal O(4))
\longrightarrow H^0(Y_{F_D},\mathcal O_Y(4))
\]

lifts it to an ambient quartic. Together with the certified nonzero minor,
this rank sandwich must prove

\[
\operatorname{rank}_{F_D}M_D=30.
\tag{3.16}
\]

### C57-EXACT-7: divisor and quaternion bridge

The twelve lines must be distinct, \(Q_D\) must not be a multiple of \(F\),
and exact intersection accounting must prove

\[
\operatorname{div}_{Y_{F_D}}(Q_D)=\mathcal E+\mathcal G.
\tag{3.17}
\]

For \(\ell=u_0\), no carrier line is contained in \(\ell=0\). Put

\[
\mathcal L_0=\operatorname{div}_Y(\ell),\qquad
f_D=Q_D/\ell^4,\qquad
\mathcal D=\mathcal E-2\mathcal L_0.
\tag{3.18}
\]

Then the checker and written proof must agree on

\[
\operatorname{div}(f_D)
=\mathcal E+\mathcal G-4\mathcal L_0
=\operatorname{Norm}_{F_D'/F_D}(\mathcal D).
\tag{3.19}
\]

The norm-divisor identity proves unramifiedness but not nontriviality. For
the required class matching, use the standard blow-up basis
\(h,e_1,\ldots,e_6\) of \(\Lambda\), and put

\[
e_\Sigma=\sum_{i=1}^6e_i,\qquad
H_Y=3h-e_\Sigma,\qquad
d_0=e_\Sigma-2h,\qquad
[\mathcal D]=e_\Sigma-2H_Y=3d_0.
\tag{3.20}
\]

For the central involution \(\iota\in U_1\) mapping to the nontrivial
element of \(U_1/U_1^+\), which exchanges the two sixers, the checker and
written proof must agree on

\[
\iota(h)=5h-2e_\Sigma,\qquad
\iota(e_\Sigma)=12h-5e_\Sigma,\qquad
\iota(d_0)=-d_0,
\tag{3.21}
\]

and

\[
\ker(1+\iota\mid\Lambda^{S_6})=\mathbf Z d_0,\qquad
(\iota-1)\Lambda^{S_6}=2\mathbf Z d_0.
\tag{3.22}
\]

With the cyclic-algebra convention in (3.19), its Hochschild--Serre
cocycle is zero on \(U_1^+\) and takes \(\iota\) to
\([\mathcal D]=3d_0\). This is nonzero modulo the coboundaries
\(2\mathbf Z d_0\), so (3.19)--(3.22), rather than the norm identity alone,
identify the unique nonzero class in \(H^1(U_1,\Lambda)\).

## 4. Locked theorem target

### Theorem A: divisibility and minimality

Let \(L/\mathbf Q\) be finite. If

\[
\left(
\operatorname{Br}(Y_L)/\operatorname{im}\operatorname{Br}(L)
\right)[2]\ne0,
\tag{4.1}
\]

then

\[
36\mid[K\cap L:\mathbf Q]\mid[L:\mathbf Q].
\tag{4.2}
\]

In particular \([L:\mathbf Q]\ge36\).

The bound is attained by \(F_D=K^{U_1}\). If equality
\([L:\mathbf Q]=36\) holds in (4.1), then, inside the fixed algebraic closure,

\[
L=K\cap L=K^{gU_1g^{-1}}
\tag{4.3}
\]

for a unique embedded double-six field. The 36 fields in (4.3) are conjugate
and form one Q-isomorphism type.

For

\[
G_L=\operatorname{Gal}(\overline{\mathbf Q}/L),\qquad
H_L=\operatorname{im}\!\left(G_L\longrightarrow W(E_6)\right),
\]

the universal implication uses the complete classical dichotomy:

\[
\begin{array}{rcl}
\mathbf Z/2\text{ branch}
&\Longrightarrow&H_L\subseteq gU_1g^{-1},
\quad [W(E_6):U_1]=36,\\
(\mathbf Z/2)^2\text{ branch}
&\Longrightarrow&H_L\subseteq gU_3g^{-1},
\quad [W(E_6):U_3]=720.
\end{array}
\tag{4.4}
\]

Thus both branches imply (4.2), while equality excludes the \(U_3\) branch.

### Theorem B: exact double-six and orientation fields

The resolvers in (3.5) are irreducible and have common normal closure \(K\).
For every double-six \(D\),

\[
[F_D:\mathbf Q]=36,\qquad
\mathbf Q(\theta_D)=F_D=\mathbf Q(\delta_D),
\tag{4.5}
\]

and

\[
F_D'=F_D(\sqrt{\delta_D})
\tag{4.6}
\]

is the quadratic field that separates the two sixers.

### Theorem C: Brauer jump

The base-field quotient is trivial, while the degree-36 field has exactly one
nonzero algebraic class:

\[
\operatorname{Br}(Y)/\operatorname{im}\operatorname{Br}(\mathbf Q)=0,
\tag{4.7}
\]

\[
\operatorname{Br}(Y_{F_D})/
\operatorname{im}\operatorname{Br}(F_D)
\cong\mathbf Z/2\mathbf Z.
\tag{4.8}
\]

The machine premise in (3.4) and the written Hochschild--Serre argument are
distinct dependencies of this conclusion.

### Theorem D: canonical explicit generator

The determinant construction (3.9)--(3.16) defines a unique normalized
quartic \(Q_D\) without an expanded coefficient table. Its divisor is
(3.17), and the quaternion algebra

\[
\mathcal A_D=(\delta_D,Q_D/u_0^4)
\tag{4.9}
\]

is unramified on \(Y_{F_D}\) and represents the unique nonzero element in
(4.8).

## 5. Exact proof boundary

Theorem A depends on the complete source classification in (4.4), not on an
exhaustive search through a few natural subgroups. Theorem B depends on exact
stabilizers, not on a numerical match of resolver roots. Theorem C depends on
the number-field Hochschild--Serre bridge, not on a machine label saying
“Brauer group”. Theorem D depends on the exact divisor identity, not merely
on solving a restriction matrix at one finite-field specialization.

## 6. Nonclaims

This theorem package does not assert:

- novelty of the general degree-36 resolver;
- an expanded \(\delta=P(\theta)\) identity;
- an expanded quartic coefficient table;
- a rational point, no rational point, a Hasse failure, weak-approximation
  failure, or a Brauer--Manin obstruction;
- a local evaluation of \(\mathcal A_D\);
- complete local inertia, conductors, Euler factors, or root numbers;
- stable-rationality novelty;
- a result for arbitrary cubic, Yukawa, or Hénon surfaces;
- any motive, automorphy, Calabi--Yau, or dynamical conclusion.

## 7. Current status

The implication from C57-EXACT-0 through C57-EXACT-7 to Theorems A--D is
written, and the exact project-local handoff and independent replay pass. The
machine tuple binds the finite premises while preserving every labeled
written bridge. The official paper source, 24-page PDF, compilation report,
and independent hostile paper audit pass. The post-compile formal-package
identity, commits, full-project manifest, archive, and project promotion remain
pending, so C57 is `PAPER_COMPILED`/`PAPER_HOSTILE_PASS` but `NOT_RELEASED`.
