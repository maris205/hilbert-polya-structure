# SF2: global fold identification, no escape, and the remaining finite-point gap

2026-09-09. Author-side proof package, restricted to the new R3 C4 lane.
Accepted first-pass FG2 and R2 NI are inputs, not re-proved here. All
arguments below are by hand; no mathematical program was executed.

## 0. Status and exact claim

Let $B=\mathbb A^4_{\overline{\mathbb Q}}$ with coordinates $(A,B,C,D)$,
and put
$$
K_{A,B,C}(x,y,z)=x^2+y^2+z^2-xyz-Ax-By-Cz.
$$
On $\mathcal S=\{K=D\}\to B$ use
$$
s_x(x,y,z)=(A+yz-x,y,z),\qquad
T=s_zs_ys_x,
$$
with $s_y,s_z$ obtained in the same manner. Composition is rightmost
first. Write $B^{\rm sm}=B\setminus\Delta$ for the smooth-fibre locus,
$\mathcal X_n=\operatorname{Fix}(T^n)|_{B^{\rm sm}}$ for the full fixed
scheme, and $P_n$ for the ordinary geometric generic exact
least-native-period-$n$ set. Let $L_n$ be its geometric splitting field.
The arithmetic formulation has the same horizontal ramification test.

The fold divisor $\mathscr F$ is specified globally in §1. SF2 asks that
the normalization of $B$ in **every** $L_n$, $n\ge3$, be unramified at
$\eta_{\mathscr F}$. The quantifier is all native periods; no finite
truncation is substituted.

**SF2 status: NOT CURRENTLY JUSTIFIED.** This package proves three
strictly weaker but uniform facts:

1. The critical hypersurface in the accepted rational two-cycle model
   is geometrically irreducible. Its image is the actual irreducible
   global fold divisor, including all four fold branches at the
   accepted base point.
2. Every $\mathcal X_n\to B^{\rm sm}$ is finite flat of the classical
   fixed-intersection rank. Thus no fixed sheet of any period can
   escape to infinity over this smooth base.
3. At $\eta_{\mathscr F}$, higher native layers cannot specialize to
   **any** period-two point, including the noncolliding two-cycles.

What remains is ramification at finite points of least native period
at least three. Section 5 states that missing input as an exact
normalization criterion. No shared higher-period branch component is
exhibited, so the absence of a proof is not a counterexample to SF2.

### Proof dependencies and scope

Accepted FG2 supplies the rational cycle model, generic degree $11$,
the complete period-two fibre inventory at $b_f$, and its simple-fold
local models. Classical fixed-intersection theory supplies fibre
**lengths**, not reducedness. Regular-local algebra then proves the
no-escape statement. Finally, an invariant two-form and the accepted
iterate-ideal lemma isolate the whole period-two part. None of these
inputs controls the normalized different of the residual higher-period
part. The full Fricke Galois-tower assertion FGT remains unchanged.

## 1. The global fold really is one irreducible divisor

Use the accepted degree-eleven cycle model
$$
\Phi(q,X,Y,Z)=\bigl(X-qYZ,\ Y-qXZ,\ Z-qXY,\
q(XYZ-X^2-Y^2-Z^2)\bigr).
\tag{1}
$$
At
$$
c_f=(q,X,Y,Z)=(2/3,3/2,3/2,3/2),\qquad
b_f=(0,0,0,-9/4),
\tag{2}
$$
accepted FG2 §3.6 gives a simple fold. It also gives the other three
sign-conjugate folds above $b_f$, with four distinct local branch
tangents in the base. Distinct local branches do not imply distinct
global divisors.

Put $S=X^2+Y^2+Z^2$, $P=XYZ$, and
$Q=X^2Y^2+Y^2Z^2+Z^2X^2$. With columns ordered $(X,Y,Z,q)$, the
Jacobian determinant is
$$
r=(1-6q)P-S+qQ+q^2(S^2+PS-4Q)+q^3P^2.
\tag{3}
$$
Here is a hand-checkable determinant derivation. For
$v=(X,Y,Z)^t$, $g=(YZ,XZ,XY)^t$ and the symmetric matrix $H$ with
diagonal zero and off-diagonal entries $H_{12}=Z$, $H_{13}=Y$,
$H_{23}=X$, the Jacobian is
$$
\begin{pmatrix}J&-g\\q(g-2v)^t&P-S\end{pmatrix},
\qquad J=I-qH.
$$
Direct $3\times3$ minor expansions give
$$
\begin{aligned}
\det J&=1-q^2S-2q^3P,\\
g^t\operatorname{adj}(J)g&=Q+2qPS+3q^2P^2,\\
v^t\operatorname{adj}(J)g&=3P+2qQ+q^2PS.
\end{aligned}
$$
Substitute them in
$(P-S)\det J+q(g-2v)^t\operatorname{adj}(J)g$ to obtain (3).
This identity is polynomial, so it does not require $J$ invertible.

On $q\ne0$ set $a=qX$, $b=qY$, $c=qZ$, and now write
$S_a=a^2+b^2+c^2$, $P_a=abc$, $Q_a=a^2b^2+b^2c^2+c^2a^2$.
Then (3) becomes
$$
q^3r=U+qV,
\tag{4}
$$
where
$$
\begin{aligned}
U&=P_a^2+P_aS_a+P_a+Q_a
   =(ab+c)(ac+b)(bc+a),\\
V&=S_a^2-4Q_a-S_a-6P_a.
\end{aligned}
\tag{5}
$$
Each displayed factor of $U$ is irreducible over
$\overline{\mathbb Q}$: it is monic linear in one of the variables.
They are pairwise nonassociate. None divides $V$. For instance, on
$ab+c=0$, further setting $a=c=0$ gives
$V=b^2(b^2-1)$, which is not the zero polynomial; the other two tests
follow by cyclic permutation. Hence $\gcd(U,V)=1$.

Consequently $U+qV$ is a primitive degree-one polynomial in $q$ over
$\overline{\mathbb Q}[a,b,c]$, irreducible by Gauss's lemma. It is
still irreducible after inverting $q$, since its constant coefficient
is nonzero. The substitution above is an isomorphism of the rings
with $q$ inverted. Finally $r|_{q=0}=P-S\ne0$, so $q$ is not a factor
of $r$. A factorization of $r$ before localization would thus induce
one after localization. This proves:

**Proposition 1.1.** The entire critical hypersurface
$\mathscr R=V(r)\subset\mathbb A^4_{q,X,Y,Z}$ is geometrically
irreducible. Its dense open part in (4) is rational, with
$q=-U/V$.

Define $\mathscr F=\overline{\Phi(\mathscr R)}_{\rm red}$.
Its image is irreducible. It has dimension at most three, and the
accepted fold at (2) gives image dimension three. Thus $\mathscr F$
is an irreducible hypersurface in $B$ meeting $B^{\rm sm}$.
All four critical points over $b_f$ belong to $\mathscr R$, so all
four accepted local branch graphs belong to this same global divisor.

The accepted local degree exhaustion ($4\cdot2+3=11$ cycle sheets)
allows a meridian about just one of these local branch graphs. It is
a single transposition on cycle labels; the phase discriminant is
$1-4q_f=-5/3\ne0$. Therefore the generic inertia along $\mathscr F$
has odd cycle sign in the accepted FG2 extension. This uses the
accepted local calculation, rather than assuming that a restricted
one-parameter discriminant records generic inertia faithfully.

The assertion concerns the specified divisor from the finite-$q$
critical chart. It makes no assertion that every possible branch
divisor in every compactified chart has been classified.

## 2. Every fixed incidence is finite flat over the smooth base

Set
$$
u_n=(2+\sqrt5)^n+(2-\sqrt5)^n,\qquad
a_n=u_n+4(-1)^n.
\tag{6}
$$
The required classical input is valid on **every smooth cubic fibre**:
the affine fixed scheme of the native Coxeter iterate $T^n$ is
zero-dimensional with total length $a_n$. In
[Iwasaki–Uehara, §§5 and 8](https://arxiv.org/pdf/math/0512583v3),
Lemma 5.1 identifies the smoothness hypothesis, Lemma 8.1 excludes
periodic curves, Lemma 8.2 computes the projective intersection
$a_n+2$, and Lemma 8.3 gives two boundary contributions of one. The
coordinate conversion is
$(x_1,x_2,x_3)=(-x,y,z)$,
$(\theta_1,\theta_2,\theta_3,\theta_4)=(-A,B,C,-D)$;
reversing the Coxeter word transposes its graph. Only intersection
length is used. Their Painlevé clock is twice the present native clock.

The universal smooth surface $\mathcal S^{\rm sm}\to B^{\rm sm}$ is
smooth of relative dimension two. The graph of $T^n$ meets its relative
diagonal in $\mathcal X_n$. Locally the diagonal ideal has two
generators, so $\mathcal X_n$ is cut out by two equations in the
regular six-dimensional total space. Each geometric fibre has finite
support by the preceding input, hence $\mathcal X_n\to B^{\rm sm}$
is quasi-finite and separated.

At a closed point of $\mathcal X_n$, the two equations give local
dimension at least four. Quasi-finiteness gives dimension at most
four. Their height is therefore two and they form a regular sequence
in the ambient regular local ring. The local ring of $\mathcal X_n$
is Cohen–Macaulay of dimension four. The base local ring is regular
of dimension four and the fibre dimension is zero. The
[miracle-flatness criterion, Stacks 00R4](https://stacks.math.columbia.edu/tag/00R4)
therefore gives flatness at every closed point. The flat locus is
open and the schemes here are of finite type over an algebraically
closed field, so it gives flatness everywhere.

For completeness, constant fibre length upgrades this quasi-finite
flat map to a finite map; it is not valid to infer finiteness from
quasi-finiteness alone. The following argument supplies the upgrade.

**Lemma 2.1.** Let $Y\to S$ be a separated, quasi-finite, flat
finite-presentation morphism over a connected normal locally
Noetherian base. If every geometric fibre has the same finite length
$d$, then the morphism is finite locally free of rank $d$.

**Proof in the present setting.** It suffices to check after strict
henselization at each base point. Write $R$ for this local normal
domain and $K_R=\operatorname{Frac}(R)$. By
[Zariski's main theorem, Stacks 05K0](https://stacks.math.columbia.edu/tag/05K0),
embed $Y_R$ as an open subscheme of a finite $R$-scheme $Z$. Replace
$Z$ by the schematic closure of $(Y_R)_{K_R}$ inside $Z$. This does
not change its intersection with $Y_R$: flatness makes $Y_R$
schematically generically dense. The resulting finite $R$-algebra is
torsion-free, with generic rank $d$.

Since $R$ is henselian, the finite algebra is a product of local finite
algebras $Z_i$. Any such component whose closed point belongs to the
open $Y_R$ lies wholly in $Y_R$: an open subset of the spectrum of a
local ring containing its closed point is the entire spectrum. These
retained components are finite and flat, being open-and-closed parts
of $Y_R$. The sum of their ranks is the length of the closed fibre of
$Y_R$, namely $d$. Every nonzero omitted component of $Z$ would have
positive generic rank, because $Z$ is torsion-free over the domain
$R$. That contradicts the total generic rank $d$. There are no
omitted components, so $Y_R=Z$ is finite. Finiteness descends, and a
finite flat finite-presentation map is finite locally free. $\square$

This is the usual constant-degree form of a Deligne–Rapoport
finiteness lemma; it is also stated as Exercise 2(iv) in
[Conrad's Math 248B handout](https://virtualmath1.stanford.edu/~conrad/248BPage/homework/hmwk8.pdf).
The degree-stratification theorem
[Stacks 07RY–07RZ](https://stacks.math.columbia.edu/tag/07RZ) also gives
this implication directly, without the normal-base restriction. The
proof above records the precise upgrade used here.

**Proposition 2.2 (all-period no escape).** For each $n\ge1$,
$$
\mathcal X_n\longrightarrow B^{\rm sm}
\quad\text{is finite flat of rank }a_n.
\tag{7}
$$
In particular $\mathcal X_1$ is empty, since $a_1=0$, and
$\mathcal X_2$ has rank $22$. The fixed scheme is generically reduced
by accepted R2; no reducedness on every special smooth fibre is
claimed. Indeed the accepted fibre at $b_f$ already has length $22$
but only $14$ ordinary points.

Every generic fixed sheet consequently has a finite specialization
along every valuation centered on $B^{\rm sm}$. This handles all
remote sheets at infinity, not just those near the colliding cycles.
It says nothing yet about ramification at their finite specializations.

## 3. The whole period-two fibre excludes nontrivial root-of-unity returns

On a smooth cubic fibre the Poincaré-residue two-form is nowhere zero.
Each $s_i$ preserves $K$ and has ambient Jacobian determinant $-1$;
therefore it negates this two-form. Thus $T^2$ preserves it and
$$
\det\bigl(DT^2|_{T_p\mathcal S_b}\bigr)=1
\quad\text{at every }p\in\mathcal X_2.
\tag{8}
$$

At $b_f$, accepted FG2 gives exactly eight doubled nonzero fixed
points of $T^2$ and six simple axis points. At a doubled point the
accepted simple-fold local algebra is
$\overline{\mathbb Q}[\epsilon]/(\epsilon^2)$ and has tangent
dimension one. Hence $DT^2-I$ has a nonzero kernel on the surface
tangent space. By (8), both eigenvalues of $DT^2$ there equal one.

For an axis point $p=(x,0,0)$, $x^2=D\ne0$, tangent coordinates on
the surface are $(y,z)$ and $T(p)=(-x,0,0)$. Differentiating the three
explicit involutions, without iterating a program, gives
$$
DT_p=\begin{pmatrix}-1&-x\\x&x^2-1\end{pmatrix},\qquad
DT_{T(p)}=\begin{pmatrix}-1&x\\-x&x^2-1\end{pmatrix},
$$
and therefore
$$
DT^2_p=
\begin{pmatrix}
1+x^2&x^3\\x^3&x^4-x^2+1
\end{pmatrix},\qquad
\det DT^2_p=1,\qquad \operatorname{tr}DT^2_p=D^2+2.
\tag{9}
$$
At $D=-9/4$ the trace is $113/16>2$, so the eigenvalues are positive
real reciprocals, one larger than one, and neither is a root of unity.
The other axes have the same trace for the actual ordered map, as
follows from an explicit commuting symmetry. On $A=B=C=0$, let
$r_0(x,y,z)=(y,z,x)$; then
$r_0Tr_0^{-1}=s_zTs_z$, so $g=s_zr_0$ commutes with $T$ and cycles
the three axis pairs. Return derivatives at corresponding points are
conjugate. This does not assume a permutation symmetry of arbitrary
ordered forcing.

Now fix any root of unity $\zeta\ne1$. On $\mathcal X_2$ the vertical
derivative of $T^2$ is an endomorphism of the pulled-back rank-two
tangent bundle, since $T^2$ is the identity on that fixed scheme.
Its $\zeta$-eigenvalue locus
$$
\Sigma_\zeta=
V\!\left(\det(DT^2|_{T_{\mathcal S/B}}-\zeta I)\right)
\subset\mathcal X_2
\tag{10}
$$
is closed. By Proposition 2.2 its image in $B^{\rm sm}$ is closed.
The preceding complete $b_f$ inventory shows that this image misses
$b_f$. Since $\mathscr F$ is irreducible and contains $b_f$, the
image cannot contain $\eta_{\mathscr F}$.

**Proposition 3.1.** At every geometric period-two point over
$\eta_{\mathscr F}$, an eigenvalue of the vertical return derivative
$DT^2$ is either one or is not a root of unity.

This argument applies separately to every $\zeta\ne1$. It asserts
the property at the generic point. It does not assert a single open
neighborhood of $b_f$ on which all root-of-unity orders are excluded.

## 4. No higher native layer can enter any period-two germ

We use the accepted R2 iterate-ideal identity, whose elementary
content is recalled to specify the hypotheses. For a parameter-family
map $f$ fixing the parameters and a point $p$ with $f(p)=p$,
$$
f^m(z)-z=Q_m(z)(f(z)-z),\qquad
Q_m(p)=I+Df_p+\cdots+(Df_p)^{m-1}.
\tag{11}
$$
Telescoping $f^j(f(z))-f^j(z)$ and taking divided differences gives
the identity including the parameter variables. If the last matrix
is invertible, the two fixed ideals coincide in the local ring.

Apply this with $f=T^2$ and any geometric point of $\mathcal X_2$
over $\eta_{\mathscr F}$. Proposition 3.1 makes every eigenvalue of
$I+Df+\cdots+Df^{m-1}$ nonzero: at eigenvalue one its value is $m$,
and at an eigenvalue which is not a root of unity its value is
$(\lambda^m-1)/(\lambda-1)\ne0$. Jordan blocks do not alter this
invertibility criterion.

One may use the three ambient state coordinates in (11). The normal
direction to the smooth level $K=D$ contributes one additional
eigenvalue one, because $K\circ T^2=K$ and $dK\ne0$. Thus the same
invertibility holds in these ambient coordinates, and remains valid
after imposing $K=D$. Consequently, for every $m\ge1$,
$$
\operatorname{Fix}(T^{2m})_p=
\operatorname{Fix}(T^2)_p
\quad\text{as parameter-family local schemes.}
\tag{12}
$$
For odd $n$, a point of least native period two does not satisfy
$T^n(p)=p$ at all. Smooth fibres have no period-one points by (7).

**Proposition 4.1.** No generic ordinary point of least native period
$n\ge3$ can specialize to a point of least native period at most two
over $\eta_{\mathscr F}$.

The result is stronger than isolation of the single colliding pair:
it covers all eleven generic two-cycle labels and every point in
their special fibre. It uses the complete period-two inventory only
as a nonresonance witness, not as a proposed enumeration of higher
periodic points.

## 5. Exact residual criterion and why SF2 is still open

Let $R=\mathcal O_{B,\eta_{\mathscr F}}^{\rm sh}$, a strictly
henselian discrete valuation ring, and let $K_R$ be its fraction
field. All finite algebras below are obtained after this base change.
For even $n$, the natural closed inclusion
$\mathcal X_{2,R}\subset\mathcal X_{n,R}$ is an equality locally
at every point of the special fibre of $\mathcal X_{2,R}$, by (12).
Finite schemes over a henselian local ring decompose into the
components of their special fibres. Hence that inclusion identifies
$\mathcal X_{2,R}$ with an open-and-closed part and gives
$$
\mathcal X_{n,R}=\mathcal X_{2,R}\ \sqcup\ \mathcal Z_n
\quad(n\text{ even}).
\tag{13}
$$
For odd $n$ put $\mathcal Z_n=\mathcal X_{n,R}$. These are finite
flat schemes with
$$
\operatorname{rank}_R\mathcal Z_n=
\begin{cases}a_n-22,&n\text{ even},\\a_n,&n\text{ odd}.
\end{cases}
\tag{14}
$$
Every special point of $\mathcal Z_n$ has least native period at
least three. By accepted generic reducedness, its generic point
algebra is the disjoint union of the ordinary $P_d$ algebras for
$d\mid n$, $d\ge3$.

Let $\widetilde{\mathcal Z}_n$ be the normalization of $R$ in that
generic finite étale algebra (component by component). It is finite,
since $R$ is excellent. The following is an exact reformulation,
not a new proof of the right-hand condition:
$$
\boxed{\quad
\mathrm{SF2}\quad\Longleftrightarrow\quad
\widetilde{\mathcal Z}_n\to\operatorname{Spec}R
\text{ is finite étale for every }n\ge3.
\quad}
\tag{15}
$$
Indeed finite unramified extensions of the henselian discretely
valued field are closed under subextensions, conjugates and finite
composita. Thus the normalization of an ordinary point algebra is
unramified exactly when its Galois splitting extension is unramified.
Taking every divisor $d\mid n$ proves the forward implication of
(15), and retaining the $P_n$ factor proves the reverse implication.
Equivalently, each **normalized** different in (15) must be a unit.

A stronger sufficient statement would be
$$
\det\bigl(DT^n_p-I\bigr)\ne0
\quad\text{for every geometric special point }p\in\mathcal Z_n
\quad\text{and every }n\ge3.
\tag{16}
$$
The implicit-function criterion would then make $\mathcal Z_n$
itself finite étale. Neither (16) nor the weaker exact condition (15)
has been established here. In particular, closed resonance loci for
higher-period points have not been shown to omit $\mathscr F$.

Any actual ramification failure of SF2 must now be supported at a
finite point $p$ of native least period $d\ge3$, with $d\mid n$,
where $DT^n_p-I$ is singular. Therefore $DT^d_p$ has an eigenvalue
whose $(n/d)$-th power is one. For a degeneration from exact period
$n>d$, the iterate-ideal identity further requires a **nontrivial**
root of unity of order dividing $n/d$; eigenvalue one alone does not
create extra higher-period branches. For $n=d$, eigenvalue one can
give a same-period collision.

Failure of (16) is not by itself failure of (15). For example, over a
characteristic-zero strictly henselian DVR with uniformizer $t$, the
raw algebra $R[z]/(z^2-t^2)$ has a doubled special point but its
normalization is $R\times R$, unramified. In contrast
$R[z]/(z^2-t)$ is ramified. These are algebraic illustrations of the
logical distinction, not claimed realizations inside the Fricke
family. Constant length and finite flatness alone distinguish neither
case.

## 6. Source subtraction and handoff

| Input | Precise role and boundary |
| --- | --- |
| [Accepted FG2](../../lanes/c4_fricke_galois/REPORT.md), §§3.3–3.6 | The cycle model, degree, complete $b_f$ fibre and local odd cycle-sign inertia. Not claimed again as an R3 discovery. |
| [Accepted R2](../../continuation_round2/c4_uniform_fricke/PROOF_SUPPLEMENT.md), §§4–6 | Iterate-ideal identity and ordinary generic reducedness/count. NI separates the singular divisor, not the present smooth fold. |
| [Iwasaki–Uehara](https://arxiv.org/pdf/math/0512583v3), §§5, 8 | Classical absence of periodic curves and smooth-fibre intersection lengths. No assertion of ordinary reducedness at every smooth parameter is imported. |
| [Stacks 00R4](https://stacks.math.columbia.edu/tag/00R4), [Stacks 05K0](https://stacks.math.columbia.edu/tag/05K0), [Stacks 07RZ](https://stacks.math.columbia.edu/tag/07RZ), [Conrad handout](https://virtualmath1.stanford.edu/~conrad/248BPage/homework/hmwk8.pdf) | Classical local algebra and quasi-finite-to-finite upgrade; the argument used is included in §2. |
| [Cantat, *Bers and Hénon, Painlevé and Schrödinger*](https://arxiv.org/pdf/0711.1727v2), Theorem 1.2 and §§3, 5 | Boundary dynamics and real hyperbolic regimes were checked as possible inputs. They do not establish a uniform complex higher-period nonresonance theorem on $\mathscr F$. In particular the $D\ge4$ real maximal-entropy regime does not contain $b_f$, where $D=-9/4$. |

The research-lit local-first check found no relevant locally named
Fricke/Markoff/Iwasaki/Cantat PDF, and no callable Zotero/Obsidian
metadata tool. The documented arXiv-fetch script was absent, so
primary web/arXiv retrieval was used. Searches for parabolic periodic
monodromy and resonance in the Fricke/Markoff family did not locate a
source proving (15). This bounded search is not a novelty certificate
or evidence of a no-go theorem.

The increment beyond these inputs is the explicit global critical
irreducibility calculation and their assembly into all-smooth-base
finiteness plus complete period-two isolation at the generic fold.
The imported lengths, fixed-point hyperbolicity tools, elementary
divided differences and commutative algebra are source-owned.

**Next exact input needed:** prove that the normalizations
$\widetilde{\mathcal Z}_n$ in (15) have unit different for all
$n\ge3$, or exhibit an actual $n\ge3$ whose normalized point algebra
ramifies at $\eta_{\mathscr F}$. A valid no-resonance witness for every
period somewhere on the same irreducible divisor would suffice for
the stronger route (16). A finite period census, the fold's own
unipotent return, or a statement about infinity is no longer enough.

No all-period Galois maximality, cycle-character independence,
rational-specialization theorem, Euler product, root identity, or
closure of FGT follows from the present partial package.
