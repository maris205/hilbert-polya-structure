# B3 — Native periodic data versus the global good-model obstruction

2026-09-09 UTC. Author scouting report; no admission or independent-review
claim. Owned path: this lane only. Mathematical program executions: **zero**.

## Frozen full question and stopping boundary

The original B3 investigation is whether C426/GR5's complete all-affine
good-model classification yields genuinely new native periodic-orbit
arithmetic after subtracting classical good-reduction period lifting. The
following is the single precise proposed bridge tested here.

**B3-PJ.** Fix a nonnegative integer $J$. Suppose $K$ is a number field,
$R=\mathcal O_K$, and
$$
F(x,y)=(y,f(y)-ax),\qquad a\in K^\times,\quad \deg f=d\ge2,
$$
has a regular affine-good model over $K_v$ at every finite place $v$, with
no field extension allowed. Suppose it has a marked $K$-rational orbit
$C=(P_0,\ldots,P_{n-1})$, $n\ge3$, such that:

1. $n$ is the actual least period for the single native map $F$;
2. $C$ affinely spans $\mathbb A^2_K$;
3. in every local good chart its reduced orbit still has least period $n$;
4. at every $P_i$, the $J$-jet of the ordinary return $F^n$ is the $J$-jet
   of the identity (the condition is vacuous beyond fixed-point equality
   when $J=0$).

Does it follow that one $K$-affine coordinate change is good at every
finite place? More generally, can the vanishing of GR5's ideal-square
obstruction be decided from these marked-cycle observables, for any fixed
finite jet depth?

The decisive negative criterion is an exact same-field, same-degree pair
for every $J$: one map globally good, the other locally good everywhere
but with no global affine good model, both carrying noncollinear,
everywhere-residually-primitive native $3$-cycles whose return jets through
order $J$ are identity. This is a falsifier for the stated observable
bridge, not a no-go for all periodic arithmetic or all periods of a map.

**Pre-proof feasibility discriminator.** Start from the order-three linear
Hénon map $L(x,y)=(y,-x-y)$ on the canonical scale lattice $I\oplus I$.
Try adding a degree-preserving nonlinear term divisible by high powers of
the three orbit-coordinate factors. Check, on paper, simultaneously:
weighted coefficient integrality, exact primitive reduction at every
prime, noncollinearity, preservation of the finite jet, and the class of
$I^2$. A failure of any one condition invalidates the proposed
counterexample. No finite census or mathematical program is authorized
or needed for this test.

## Outcome and proof status

**B3-PJ is false for every finite $J$, with an explicit same-field,
same-degree pair.** The counterexample and the lattice/triangle interfaces
below are proved as stated. They are useful auxiliary boundaries, not a
claim of a substantial new paper after source subtraction. No class-sensitive
uniform period theorem or complete local-global existence criterion for
native periodic orbits has been obtained. The original broad B3
investigation is not declared universally impossible by this one falsifier.

The method used the repository batch workflow for claim freezing and
scope, `research-lit` for local-first source subtraction, `idea-creator`
for pruning duplicate directions, and `proof-writer` for the exact
counterexample contract. No external model review or GPU pilot was used.

## 1. Imported theorem and its exact periodic compatibility interface

The actual C426 manuscript was read, especially
`../../../research_c424_c428/papers/C426_affine_good_models/sections/02_classification.tex`
through `06_examples.tex`, with its proof predecessor
`../../../research_c424_c428/continuation_round5/arithmetic/PROOF_PACKAGE.md`,
§§1–4. Paths in this paragraph are relative to this lane.

For $q(Y)=f(Y)-aY$ and leading coefficient $b$, C426 says that all local
good tests passing gives a unique fractional scale ideal and patched centre
$$
(b)I^{d-1}=R,\qquad r\in K,\qquad D_v=r+I\mathcal O_{K_v}.
$$
All local good charts have image $D_v^2$, while a single global affine
good chart exists exactly when $I^2$ is principal. A global common scalar
chart requires the stronger condition that $I$ be principal. We import
these statements as proved, including all affine changes, wild centres,
and nonprincipal two-torsion repair; none is a new B3 theorem.

**Lemma 1 (native periodic containment; elementary compatibility).** Every
$K$-rational periodic point of $F$ belongs to $(r+I)^2$. Moreover $F$ and
$F^{-1}$ preserve that affine $R$-lattice, whether or not $I^2$ is principal.

*Proof.* At a finite place choose a passing scalar chart
$S(x,y)=(sx+r_v,sy+r_v)$. Its map is
$$
G(x,y)=(y,g(y)-ax),\qquad g\in O[Y],\quad a\in O^\times,
$$
with unit leading coefficient and $O=\mathcal O_{K_v}$. Write a native
periodic coordinate sequence as $G^i(P)=(z_i,z_{i+1})$, cyclically indexed.
If $M=\max_i|z_i|>1$, choose $|z_{i+1}|=M$. The recurrence gives
$$
g(z_{i+1})=z_{i+2}+az_i.
$$
Its left side has absolute value $M^d>M$, while the right side has
absolute value at most $M$, a contradiction. Thus the periodic point is
in $S(O^2)=D_v^2$. Intersecting inside $K^2$ over all finite places gives
$(r+I)^2$. The forward and inverse local models preserve $O^2$, so the
same intersection proves lattice invariance. This uses native Hénon
iteration, not iteration of the auxiliary polynomial $q$. $\square$

One may therefore reduce the dynamics on
$$
((r+I)/(\mathfrak p I))^2
$$
as an affine rank-two residue space; its notation means the translate
of $I/\mathfrak p I$, not division of subsets of $K$. It has
$(\mathrm N\mathfrak p)^2$ elements. Locally choosing a generator of
$I_v$ identifies it with $\kappa_v^2$. Changing a good chart gives an
integral affine conjugacy and does not change least periods. Freeness of
$I\oplus I$ is unnecessary for this reduction.

Consequently, at any selected finite place $v$, a rational native period
is bounded by the classical finite quantity
$B(\mathcal O_{K_v},2)$ for two-variable integral polynomial cycles.
This applies equally when $I^2$ is nonprincipal: its hypotheses only need
the *local* chart and Lemma 1. Applying a standard period bound after GR5
therefore does not exploit the nonscalar global repair.

## 2. Exact same-field counterexample at every finite jet depth

**Theorem 2 (marked periodic-jet blindness to the global obstruction).**
For every $J\ge0$, put $h=J+1$ and $d=3h+1$. Over the fixed number field
$$
K=\mathbb Q(\sqrt{-23}),\quad
\omega=(1+\sqrt{-23})/2,\quad R=\mathbb Z[\omega],
$$
there are two degree-$d$, Jacobian-one, single-factor Hénon maps
$F_{\mathrm{good},h}$ and $F_{\mathrm{obs},h}$ with the following properties.

- The first is already regular-good over $R$.
- The second is affine-good over every $K_v$ but has no $K$-affine
  coordinate change good at all finite places.
- Each has an affinely noncollinear native rational $3$-cycle that stays
  primitive modulo every prime, and hence modulo every positive prime
  power in its canonical good lattice.
- At every point of both marked cycles the $J$-jet of the native return
  $F^3$ is exactly the identity. In particular, for $J\ge1$ both return
  multiplier multisets on the marked cycles are exactly $\{1,1\}$.

### 2.1 The obstructed ideal (imported arithmetic, explicitly checked)

Let
$$
I=(2,\omega-1),\qquad A=\omega+1.
$$
The C426 three-torsion example proves $I^3=(A)$ and $I^2$ nonprincipal.
For completeness, $\omega^2-\omega+6=0$ splits into distinct linear factors
modulo $2$, with primes $I=(2,\omega-1)$ and $I'=(2,\omega)$. The element
$A$ has norm $8$, lies in $I$ and not $I'$, so $(A)=I^3$. A generator of
$I$, were one to exist, would have norm $2$. But
$$
N(m+n\omega)=m^2+mn+6n^2=(m+n/2)^2+23n^2/4
$$
never equals $2$ for integers $m,n$. Thus $I$ is nonprincipal; $I^2$
cannot be principal either, because $I=I^3/I^2$ would then be principal.

Set
$$
\alpha=-1-\omega,\qquad \beta=1-\omega,\qquad \gamma=2\omega.
$$
All three lie in $I$ and sum to zero. Put
$$
H(Y)=(Y-\alpha)(Y-\beta)(Y-\gamma),
$$
and define
$$
F_{\mathrm{obs},h}(x,y)
=\left(y,-x-y+\frac{yH(y)^h}{A^h}\right). \tag{1}
$$
This is a single-factor Hénon polynomial automorphism with Jacobian $1$,
degree $3h+1$, and leading coefficient $b=A^{-h}$. Its inverse is
$F^{-1}(x,y)=(-y-x+xH(x)^h/A^h,x)$.

### 2.2 Every local good model exists, but no global one exists

At any finite place choose $s\in K_v^\times$ with $sO=IO$. Then
$$
S_s^{-1}F_{\mathrm{obs},h}S_s(x,y)
=\left(y,-x-y+
\frac{s^{3h}}{A^h}y
\prod_{\delta\in\{\alpha,\beta,\gamma\}}
(y-\delta/s)^h\right). \tag{2}
$$
Here $\delta/s\in O$ and $s^{3h}/A^h\in O^\times$, since
$I^{3h}=(A^h)$. Both directions have integral coefficients; their top
coefficients are units; the reduced indeterminacy points are the two
distinct coordinate points at infinity. Thus (2) verifies all parts of
regular good reduction, including at primes above $2$ or $3$.

By GR5 the scale ideal is precisely $I$, since
$(b)I^{d-1}=(A^{-h})I^{3h}=R$. Its square is nonprincipal, so *every*
global affine coordinate change fails somewhere. This includes mixed
matrices and unrelated coordinate translations; the failure is not merely
that no common scalar has been found.

### 2.3 Native least period and primitive reduction at all finite places

Let
$$
P_0=(\alpha,\beta),\quad P_1=(\beta,\gamma),\quad
P_2=(\gamma,\alpha).
$$
Since $H$ vanishes at each coordinate and their sum is zero, (1) gives
exactly $P_0\mapsto P_1\mapsto P_2\mapsto P_0$. Write
$$
u=\beta-\alpha=2,\qquad v=\gamma-\beta=3\omega-1.
$$
Then
$$
(u,v)=(2,3\omega-1)=(2,\omega-1)=I. \tag{3}
$$
For the nontrivial inclusion in (3),
$v-2=3(\omega-1)$ and $2(\omega-1)\in(2)$, so their difference gives
$\omega-1\in(u,v)$. The three pair differences, with orientations chosen
cyclically, are
$$
(u,v),\qquad(v,-u-v),\qquad(-u-v,u). \tag{4}
$$
Each pair of coordinates generates $I$, because these vectors differ by
matrices in $\mathrm{GL}_2(R)$. After division by a local generator $s$,
at least one coordinate of each difference is a unit. Hence the three
reduced points are pairwise distinct at every finite place. The reduced
native orbit has least period three, and so does its reduction modulo
every higher prime power. This is stronger than just existence of a
nontrivial rational cycle.

The determinant of two independent differences is
$$
\det(P_1-P_0,P_2-P_0)=-(u^2+uv+v^2)
=-3(3\omega-17)\ne0. \tag{5}
$$
Thus the original three points are not collinear over $K$. Their
reductions need not be noncollinear; that stronger condition is precisely
where a determinant-class obstruction can remain, as §3 explains.

### 2.4 All prescribed finite return jets are identity

Let $L(x,y)=(y,-x-y)$. Its matrix is
$$
M=\begin{pmatrix}0&1\\-1&-1\end{pmatrix},\qquad M^3=\mathrm{Id}.
$$
At a point whose second coordinate is any $\delta\in\{\alpha,\beta,\gamma\}$,
the perturbation $yH(y)^h/A^h$ belongs to $(y-\delta)^h$. Consequently
$$
F_{\mathrm{obs},h}(P_i+Z)=P_{i+1}+MZ+O((Z)^h), \tag{6}
$$
where the last notation means membership in the $h$th power of the
two-variable maximal ideal, not an analytic estimate. Composition of
three such expressions gives
$$
F_{\mathrm{obs},h}^3(P_i+Z)=P_i+Z+O((Z)^h). \tag{7}
$$
Indeed, substitution of polynomials with zero constant term into
$(Z)^h$ preserves that ideal, so the induction behind (7) loses no
terms of degree below $h$. Since $h=J+1$, (7) proves identity through
order $J$. This argument works also for $J=0$. It is an exact identity
of algebraic jets over $K$, hence remains true in any finite-place good
chart. It uses no division by factorials and has no tame-prime exception.

### 2.5 A globally good comparison map over the same field and degree

Define
$$
F_{\mathrm{good},h}(x,y)
=\bigl(y,-x-y+y(y^3-y)^h\bigr). \tag{8}
$$
It is integral over $\mathbb Z$, has unit leading coefficient and
Jacobian $1$, and its inverse is integral. Its two reduced indeterminacy
points are distinct at every finite place; it is therefore globally
regular-good over $R$ without changing coordinates.

The marked orbit is
$$
(-1,0)\longmapsto(0,1)\longmapsto(1,-1)\longmapsto(-1,0).
$$
Its pair differences generate $R$, including in residue characteristic
$2$ or $3$, so its least period remains three everywhere. Its triangle
determinant is $-3\ne0$. The perturbation in (8) vanishes to order at
least $h$ at $-1,0,1$, so the argument (6)–(7) gives the same identity
$J$-jets of the ordinary return. The fields, degrees, Jacobians, marked
least periods, all marked reduction-period towers, and specified finite
return jets now match, while global good-model existence differs.
This proves Theorem 2 and refutes B3-PJ for every $J$. $\square$

**Scope of matching.** No equality of the full periodic spectra or of the
reduced maps outside the marked orbit is asserted. Coordinates and
coefficients differ. There is no claim that
jets of *all* periodic points fail to detect local potential good
reduction. Increasing $J$ increases the degree; this theorem is not a
fixed-degree, all-orders rigidity counterexample. For $J\ge1$ the marked
returns are degenerate; no nondegeneracy or simple-periodic-scheme hypothesis was
silently assumed. Prime ideals label arithmetic reductions, not
prime-owned primitive trajectories.

## 3. What does detect the square: arithmetic area, not just periods

**Lemma 3 (triangle defect ideal).** Assume GR5's everywhere-local-good
hypotheses and let $P_0,P_1,P_2\in(r+I)^2$ be affinely independent
$K$-points, periodic or not. Put
$$
\Delta=\det(P_1-P_0,P_2-P_0),\qquad
\mathfrak a_C=(\Delta)I^{-2}.
$$
Then $\mathfrak a_C$ is an integral nonzero ideal and
$$
[\mathfrak a_C]=[I]^{-2}. \tag{9}
$$
Its support is exactly the set of finite places where the three points
become collinear in a local good chart. In particular, a periodic triangle
that remains noncollinear at *every* finite place forces $I^2$ principal.

*Proof.* Every difference coordinate is in $I$, so $\Delta\in I^2$,
proving integrality. Taking classes gives (9). In a local scalar chart
the determinant is $\Delta/s_v^2$; its positive valuation is exactly
collinearity after reduction. Right composition with
$\mathrm{Aff}_2(O_v)$ multiplies that determinant by a unit and preserves
the criterion. $\square$

Equation (9) is a genuine compatibility interface, but its mechanism is
the already-owned determinant/Steinitz obstruction. Periodicity was not
used. Pairwise distinct reductions do *not* imply noncollinearity in a
two-dimensional residue space; Theorem 2 exploits exactly this missing
datum. For a nonprincipal two-torsion $I$, (9) is a principal class, in
agreement with nonscalar repair, even though $I$ itself is not principal.

The converse assertion that every globally good map supplies such a
periodic affine frame is false. For example,
$$
F(x,y)=(y,y^2+10-x)
$$
is already globally regular-good over $\mathbb Q$, but has no real
periodic orbit: summing the native recurrence around a putative orbit
gives
$$
0=\sum_i(z_i^2-2z_i+10)=\sum_i((z_i-1)^2+9)>0.
$$
Thus a frame-detection theorem would need a new theorem supplying
appropriate arithmetic periodic points; goodness alone supplies none.

## 4. Closest-primary-source subtraction

These are targeted verified primary sources, not an exhaustive priority
search. The searches included “Hutz good reduction periodic points
varieties period”, “Pezda polynomial mappings several variables local
fields”, “periodic cycles ideal class good reduction”, and “polynomial
cycles projective modules”. The local C426 proof was read before the
searches; WM6 was read before concluding its comparison. No manuscript
text was uploaded and no paper was downloaded
to the repository.

| Primary source actually accessed | What is already owned / exact applicability boundary |
| --- | --- |
| T. Pezda, *Cycles of polynomial mappings in several variables over rings of integers in finite extensions of the rationals*, Acta Arith. **108** (2003), 127–146, [publisher full text](https://www.impan.pl/shop/publication/transaction/download/product/83956), Theorems 3.1–3.2, Corollary 3.1, Lemma 4.1. | Local period bounds and orbit-distance identities are classical. Theorem 3.2 identifies possible lengths across all polynomial maps in $N\ge2$ variables with the intersection of local possibilities. It is not a fixed-map Hasse principle or a Hénon/nonfree-module theorem. Its local upper bounds still apply in GR5 charts. |
| B. Hutz, *Good reduction of periodic points on projective varieties*, [author manuscript](https://arxiv.org/pdf/0801.3645), Theorems 1–2 and §3. | The relation between primitive period, reduced period, tangent/cotangent action and residue-characteristic powers is already standard. Hutz's displayed main theorem assumes a smooth projective model and a morphism; the Hénon homogenization is not such a morphism. We do not cite that theorem directly as though the hypotheses held. Pezda supplies the applicable affine-polynomial comparison. No new exponent bound is claimed here. |
| P. Ingram, §11 in *Hénon maps: a list of open problems*, [published text](https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html), the cycle interpolation preceding Question 46 and the divisibility sequence preceding Question 47. | Prescribing Hénon cycles by polynomial interpolation and using coordinate-difference ideals are already explicit. Our vanishing-factor perturbation is elementary interpolation/Hermite interpolation, not a new general mechanism. The residual here is its compatibility with an obstructed GR5 scale ideal and a marked cycle that stays primitive everywhere. This does not by itself establish paper-level substance. |
| C426/GR5, exact local manuscript/proof inputs listed in §1. | All affine local rigidity, canonical disc square, finite wild-centre test, ideal-square global obstruction, and class-three arithmetic example are imported. Theorem 2 does not rebrand them as a second good-model classification. |
| WM6, `../../../research_c424_c428/continuation_round6/arithmetic_spectral/{FROZEN_CONTRACT.md,PROOF_PACKAGE.md}`, especially proof §§1–4. | WM6 already separates all-periodic multiplier *norms* from local potential good reduction in a wild family. B3's counterexample concerns a different obstruction: global freeness over a fixed number field after every local test passes, and only a specified marked orbit's finite jets. Neither theorem implies the other, and the stronger all-periodic observable is not replaced by one chosen cycle. |

The publisher's 2003 PDF was read at printed pp. 127–131 for the cited
results. Hutz's author manuscript was checked for the projective
hypotheses and primitive-period statement. The initial alternate IMPAN
URL with an `/en/` component, an EuDML open, and a Project Euclid 2015
article open failed; no conclusion relies on their unavailable full
text. Search snippets for the 1994 and 2015 Pezda papers are not used as
verified theorem text. Access dates: 2026-09-09 UTC.

## 5. Disposition, missing datum, and reusable handoff

**Recommended disposition: auxiliary boundary; no B3 paper admission
recommended at this checkpoint.**

The single frozen B3-PJ implication has an all-$J$ exact falsifier. The
broader desired class-sensitive native arithmetic remains unmet:

1. A degree-independent local period bound is already classical and
   available without global freeness, so simply combining it with C426
   is not a new repair-sensitive theorem.
2. Even an everywhere-primitive, noncollinear rational cycle with
   arbitrarily high prescribed finite identity return jet does not force
   a global affine good model. The exact counterexample is (1).
3. A normalized determinant ideal of a periodic triangle does retain the
   inverse square class, by (9), but this is the static determinant
   obstruction evaluated on three points. A substantial periodic
   theorem would need a new dynamical supply or rigidity statement about
   such triangles, not merely their definition.
4. No conclusion was reached about nondegenerate marked orbits with
   additional arithmetic frame data, the complete exact periodic
   multiplier/jet collection, or a fixed-map local-global existence
   principle. Those are not refuted by the construction.

Useful interfaces for the coordinator are Lemma 1 (periodic points and
reduction on a nonfree canonical lattice), Theorem 2 (all finite marked
jet-depth falsifiers over one fixed field), and Lemma 3 (exact triangle
defect class). A receiver must respect the distinction between finite
marked data and all periodic data, and between local potential good
reduction and global affine trivialization.

## Verification and limitations

The source statements, ideal products, three coordinate transitions,
all-prime primitivity, determinant, inverse formula, degree, and jet
composition were checked algebraically in this report. No executable
symbolic test, finite orbit search, old run, build, PDF, external model
call, evaluator update, shared-index edit, or Git mutation was performed.
This is AI-assisted author work, not independent internal review or human
peer review. No global novelty/priority certification is claimed.

`NO_BAD_EULER_OR_ROOT_NUMBER`: the ideals above are reduction and module
ideals, not target Euler factors. Native cycles are not owned by prime
ideals. There is no target zero/divisor correspondence, automorphy,
root-number, or Hilbert–Pólya conclusion.
