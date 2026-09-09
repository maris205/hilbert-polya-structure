# E5 internal nonauthor review: R4 cusp and fold transversality

2026-09-09. Reviewer: `c429_e5_fricke_galois_review`.
This is a current-team internal mathematical/source review.

## 1. Verdict and reviewed claim

**Local mathematical results: PROVABLE AS STATED.** The cycle-map
cusp, its explicit unfolding and slice monodromy, marked-fold
conormal, remote-fold covector and finite-orbit variation formula
survive independent checking.

**The final conditional implications are valid under their explicit
hypotheses.** Two scope clarifications were required: retain every
specialization of generic higher-period sheets at a proposed special
witness, and match branches on the global smooth locus when deriving
global noncontainment from local conormal independence. These do not
change the local formulas. Their disposition is recorded in §8.
The witness's smooth-base domain was also made explicit. All three
clarifications were independently read back; **unresolved mathematical
or source-applicability must-fixes: zero.**

**SF2: NOT CURRENTLY JUSTIFIED.** The all-period component coverage,
relative covector independence and all-residual-sheet witness remain
unproved. No counterexample to SF2 is produced. FGT, layer independence
and cycle-character separation remain open. Accepted FG2, NI and R3
proof/review files were kept read-only.

The reviewer read both new author files completely, then the changed
conditional passages after revision:

- [REPORT.md](../../c4_remote_parabolic_divisors/REPORT.md), initially
  165 lines, including the exact frozen SF2 question and source table.
- [PROOF_PACKAGE.md](../../c4_remote_parabolic_divisors/PROOF_PACKAGE.md),
  initially 390 lines, §§0–5.
- [X1's direct-family source report](../../x1_fricke_parabolic_sources/REPORT.md),
  as a source locator; the material primary passages were independently
  accessed rather than accepted solely from its summary.

### Assumptions, notation and dependency map

The family is $x^2+y^2+z^2-xyz-Ax-By-Cz=D$ over characteristic
zero, with native return $T=s_zs_ys_x$, rightmost first. Analytic
normal forms are over $\mathbb C$. Ordinary exact native periods
retain their original meaning; no replacement of the clock by $T^2$
is made. The irreducible divisor $\mathscr F$ is the accepted global
image of the critical hypersurface of the degree-eleven cycle map
$\Phi$, not a newly defined slice discriminant.

The new local arguments have the following dependencies:

1. An invertible transverse Jacobian reduces the cycle map near
   $\xi_c=(1/c,0,0,c)$ to one scalar function. Its cubic coefficient
   and mixed derivative give a versal cusp by preparation.
2. Smoothness exclusions and the unramified quadratic phase cover
   make this a statement about genuine native two-cycles.
3. A Schur complement gives the marked-fold conormal. A separate
   rank-one displacement reduction gives the remote-fold conormal.
4. Independence of those conormals proves local transversality.
   A global inference additionally requires the final all-component
   coverage and branch-matching hypotheses.
5. R3 supplies finite fixed incidences and the generic-fold residual
   reduction. It does not make an arbitrary special witness's
   lower-period limits disappear.

## 2. Explicit cusp calculation

The source/target substitutions in package (3) are correct:
$X=s+h$, $Y=s-h$, $a=(A+B)/2$, $b=(A-B)/2$.
At $\xi_c$, the derivative of $(b,C,D)$ in $(h,Z,q)$ has determinant
$-2c^2\ne0$. Replacing $D$ by $t=D+C$ is an invertible target
coordinate change. Thus the asserted analytic elimination of
$h,Z,q$ is valid near every stated $c$.

For $b=0$, the unit $1+qZ$ forces $h=0$, and uniqueness makes
$q,Z$ even functions of $s$. With $C=c,t=0$, the relation
$Z=c+qs^2$ reduces the remaining equation to
$$
D=q\bigl[-c^2+(c-2-2cq)s^2+(q-q^2)s^4\bigr].
$$
Its coefficient of $s^2$ gives
$q_2=(c-4)/c^3$. Therefore
$qZ=1+(c-3)s^2/c^2+O(s^4)$ and
$F(s,0,c,0)=-(c-3)s^3/c^2+O(s^5)$.

At $s=b=0$ and variable $t$, one has exactly
$Z=c$ and $q=(c-t)/c^2$. This verifies the coefficient $t/c$
of $s$, not merely its first-order approximation. Analyticity and
evenness then justify
$$
F(s,0,c,t)=\frac tc s-\frac{c-3}{c^2}s^3+O(ts^3,s^5).
$$
In particular $F_{sss}=-6(c-3)/c^2$ and $F_{st}=1/c$ have the
claimed nonzero values.

### Preparation, units and versality

The germ $F-a$ has order exactly three in $s$ at the central
parameter. Weierstrass preparation applies with a nonvanishing
analytic unit. Its central monic polynomial is $s^3$; therefore
the shift removing the quadratic coefficient is an invertible
source-coordinate change near that point.

For precision about the unit, put $\kappa=-(c-3)/c^2\ne0$ and
write the prepared polynomial as $s^3+p_2s^2+p_1s+p_0$.
At the central parameter its unit has value $\kappa$. Comparing
constant terms after parameter differentiation gives
$\partial_a p_0=-1/\kappa\ne0$ and $\partial_t p_0=0$.
Comparing the coefficient of $s$ in the $t$ derivative gives
$\partial_t p_1=1/(c\kappa)\ne0$. Thus possible derivatives
of the preparation unit cannot destroy the two needed independent
directions. Since all $p_i$ vanish centrally, depressing the cubic
does not change these first-order constant/linear-coefficient tests.

The depressed coefficients are consequently independent target
coordinates, with $b,C$ passive. This proves the cubic family
$w^3+uw+v=0$, not just a cubic Taylor jet. Elimination of its
double-root equations gives $4u^3+27v^2=0$. The conclusion concerns
the branch image contributed by this source germ. It does not claim
that the whole global divisor has no other local branches at every
point of the curve.

## 3. Smoothness, phases and the actual slice permutation

The singularity equations exhaust the cases correctly. If $x=y=0$,
then $z=C/2$ and the level condition gives $C=0$ or $4$. If both
$x,y$ are nonzero, then either $z=2,y=x$ or $z=-2,y=-x$.
The first forces $C=4$ on this level and introduces no additional
parameter; the second forces $C=-4/3$ and $x^2=8/3$. Exactly one
zero among $x,y$ is impossible. Thus the smooth-fibre exclusions are
precisely $0,4,-4/3$, while $c=3$ is excluded solely because the
cubic coefficient vanishes. No conclusion for that higher-degenerate
case is asserted.

The phase discriminant is $1-4/c$, nonzero under these hypotheses.
The two ordered phases over $\xi_c$ have $x=y=0$ and distinct
$z$ coordinates with sum $c$ and product $c$. The native map sends
$z$ to $c-z$, so these are genuine least-period-two points.
The accepted phase model is regular on this chart, and its étale
quadratic cover preserves the local cusp calculation. The central
fixed fibre has one tangent direction; the determinant-one return
therefore has both eigenvalues one. The family iterate-ideal lemma
isolates these particular germs from higher periods, as asserted.

On $a=b=0$, factor the odd scalar equation by $s$. The remaining
factor has nonzero derivative in $s^2$ at the center, so the implicit
function theorem gives
$s^2=c\,t/(c-3)+O(t^2)$. Its linear coefficient is nonzero.
After a local unit change, this is a quadratic branch over $t$,
alongside the analytic axis sheet $s=0$. The slice loop therefore
transposes a pair and fixes the third label.

This does not deny that other loops in the full two-parameter cubic
unfolding may realize a three-cycle. The reviewed statement is the
specific slice permutation, not a classification of every cusp loop.
Nor is its marked local factor the full degree-eleven cycle-sign
squareclass, which may contain contributions from other blocks.

The even sign change $(X,Y,Z)\mapsto(X,\varepsilon Y,\varepsilon Z)$
really sends $(A,B,C,D)$ to $(A,\varepsilon B,\varepsilon C,D)$
and fixes $q$. The transformed $D=-\varepsilon C$ statement and
$a=(A+\varepsilon B)/2$ convention are therefore correct.

## 4. Marked fold conormal

On the stated nonempty chart $\det J\ne0$, differentiating $\Phi$
gives $d\mathbf A=J\,dv_0-g\,dq$. Substitution into $dD$ yields
a coefficient of $dq$ equal to the Schur complement of the full
Jacobian. On the critical hypersurface it vanishes. Hence at an
ordinary fold the image tangent is annihilated by
$$
\nu_f=dD-q(g-2v_0)^tJ^{-1}d\mathbf A.
$$
Its $dD$ coefficient is one, so it is not the zero covector.
At the positive accepted fold, $J$ has diagonal one and off-diagonal
minus one; the expression reduces to
$dD-(dA+dB+dC)/2$ with the stated sign.

The formula describes the marked image branch. The author explicitly
does not apply it at $\xi_c$, where $J$ is singular. It is also not
an implicit assertion that a smooth source fold maps to a smooth
point of the entire global branch divisor.

## 5. Remote fold and orbit variation

Let $G(a,z)=f_a^n(z)-z$ in compatible local fibre coordinates, with
$L=D_zG$ of rank one. Choose a kernel vector $v$ and cokernel row
$\ell$. Solving one transverse state coordinate and equation is
legitimate by the nonzero rank-one minor. The remaining scalar
equation $\varphi(a,s)$ has $\varphi_s=0$ centrally.

Terms caused by the eliminated coordinate lie in the image of $L$
and are killed by $\ell$. Consequently its second kernel derivative
and parameter differential are the displayed $\beta_n$ and
$\alpha_n$, up to harmless nonzero normalization factors.
With both nonzero, the critical state $s_c(a)$ is analytic and the
critical-value function has differential $\alpha_n\ne0$.
Taylor expansion there has a nonzero quadratic coefficient; an
analytic square root of that unit gives the fold normal form.
Thus Lemma 3.1's hypotheses really suffice.

A parameter-dependent state-coordinate change adds an image-of-$L$
term to the parameter displacement, along with an invertible equation
change. This verifies the claimed intrinsic conormal line. Kernel
rescaling changes the nonzero second-derivative test by a square and
cokernel rescaling by a nonzero factor; none changes the criterion.

For the parameter derivative of the return, the product rule inserts
the parameter variation once at each native step and transports it
through precisely the remaining steps. Thus
$$
\alpha_n(\dot a)=\ell\sum_{j=0}^{n-1}
Df^{n-1-j}|_{p_{j+1}}\,V_j(\dot a)
$$
has the correct indices and ordering, with identity transport for
$j=n-1$. Compatible orbit charts include the parameter dependence
of the chosen fibre trivializations. The formula does not compute or
assume a nonzero value for any actual remote orbit.

For two smooth local image hypersurfaces, nonzero
$\alpha_n\wedge\nu_f$ is exactly conormal independence. The
two-equation implicit-function theorem proves Corollary 3.2's local
transversality. It alone proves no global image-divisor separation.

## 6. Satellite test and final conditional bridge

If a least-period-$d$ return has $M_d-I$ invertible, that point
continues analytically. The anti-invariance of the two-form under
$T$ gives $\det M_d=(-1)^d$. Its characteristic polynomial shows
that an eigenvalue $\zeta$ is equivalent to
$\tau_d=\zeta+(-1)^d/\zeta$. Excluding both possible eigenvalues
equal to one is precisely what keeps this test in the analytic
lower-period-continuation case. Nonzero $d\tau_d\wedge\nu_f$
then makes that resonance hypersurface smooth and transverse.
Repeated eigenvalues or a zero trace differential are not silently
covered by this test.

The final all-component hypothesis now requires the tests on the
smooth loci of the global image divisors, with the marked branch
equal to the unique local germ of $\mathscr F$. If a candidate
global image equalled $\mathscr F$, its conormal at such a point
would be the same line, contradicting independence. Untested
higher-degeneracy images are excluded only by an additional explicit
hypothesis. This makes the conditional implication valid; neither
its coverage nor its independent-conormal hypothesis is proved.

For the alternative witness route, use the finite closure
$Y_n\subset\mathcal X_n$ of all generic $P_d$ with $d\mid n$
and $d\ge3$, over the smooth base. Every point of $(Y_n)_b$
must be tested, even if its special least period has dropped. If
the ambient fixed incidence is étale at all those points, its
critical locus intersected with $Y_n$ has closed image missing $b$.
For $b\in\mathscr F\cap B^{\rm sm}$, that image cannot contain
the generic point of irreducible $\mathscr F$. There the accepted
R3 period-two isolation identifies the relevant residual part.
Étale local fixed-point sections over the normal base imply the
normalization of their generic point algebra is also unramified.

Thus the clarified witness condition is sufficient. It does not
permit dropping special lower-period limits, or taking the critical
image of all $\mathcal X_n$ and forgetting the forced two-cycle
degeneracy. The current cusp calculation supplies no all-residual-sheet
witness of this kind. Raw nonreducedness also remains distinct from
ramification of the normalization.

## 7. Primary-source verification and ownership subtraction

The four material external-source checks were performed directly.
This was a targeted applicability review, not a full audit of every
proof in all four papers or a universal novelty search.

**Direct Fricke source.** In
[Rebelo–Roeder, v4](https://arxiv.org/pdf/2104.09256v4), I read
Lemma 10.8 and its proof, Proposition 9.6 and its proof, and the
Corollary 6.8 Picard eigenvalue input. Lemma 10.8 supplies all-saddle
genericity for hyperbolic even words outside countably many
real-algebraic hypersurfaces of the ambient parameter space.
Proposition 9.6 excludes all periodic points from a uniform nearby
neighborhood of infinity for a fixed hyperbolic word. These are
classical ownership inputs, including no escape, not new SF2 evidence.
The displayed coordinate change $(-x,y,z)$ with parameter change
$(-A,B,C,D)$ matches the source's plus-$xyz$ convention and preserves
the word. Its even subgroup can be applied to $T^{2n}$ without
redefining native periods.

Our separate inference is that the marked two-cycle fold already
forces multiplier one for these even powers. An ambient open set
obtained by discarding the full non-simple locus therefore discards
the divisor of interest. Properness of ambient bad sets does not
show that a residual bad component avoids this prescribed divisor.
This source update is recorded here; it does not rewrite the frozen
R3 review or change its accepted mathematical scope.

**Unconstrained polynomial-automorphism family.**
[Buzzard–Hruska–Ilyashenko](https://www.math.purdue.edu/~buzzard/papers/ks29sep03.pdf),
§1.1, Theorems 1.1 and 1.4, has the stated full-$P_d$ genericity
and generic rank-two stable/unstable multiplier variation. Its
parameter space consists of normalized polynomial automorphisms of
$\mathbb C^2$ of fixed dynamical degree. The rank theorem concerns
continued saddle points; it does not assert the required conormal
independence on a prescribed Fricke parabolic divisor. No applicable
family identification or rank-preserving restriction is supplied.

**Substantial-family stability.**
[Dujardin–Lyubich, v2](https://arxiv.org/pdf/1305.2898v2), §3.1 and
Theorem 3.2, explicitly requires substantial families of polynomial
automorphisms of $\mathbb C^2$. The definition excludes persistent
unit-modulus multiplier relations outside the dissipative alternative,
and explicitly excludes conservative families. The persistent
relation $\lambda_1\lambda_2=1$ for $T^2$ fails this hypothesis,
independently of the ambient-surface mismatch. The author does not
claim that conservative dynamics can never have stability theorems;
only this cited theorem is unavailable.

**One-dimensional lifting mechanism.**
[Levin–Shen–van Strien, v2](https://arxiv.org/pdf/1901.09941v2),
§§2.1–2.4 and the Main Theorem, uses a one-dimensional marked
holomorphic deformation with its specified uniformly bounded lifting
property and attracting/nondegenerate parabolic orbit hypotheses.
The conclusion allows persistence as an alternative to transversality.
Neither a compatible one-dimensional Fricke reduction nor its
lifting property is established here. Even an applicable version
would require excluding the persistence alternative rather than
silently discarding it.

The inspected arXiv metadata matches the reported versions and the
limited publication-status statements for Rebelo–Roeder and
Levin–Shen–van Strien. The BHI journal/year/page entry also matches
[Buzzard's institutional publication list](https://www.math.purdue.edu/~buzzard/BuzzardCV.pdf),
item 19. No claim about an unchecked final publisher status is added.
These source conclusions support subtraction and limits, not an
assertion that no missing relative theorem exists anywhere in the literature.

## 8. Review changes, final binding and handoff

Three scope clarifications have been independently read back:

1. **Special-witness closure — closed.** The test now includes the
   finite closure of the generic higher-period point sets, retaining
   limits of special least period one or two. The critical locus
   is intersected with that closure. This is necessary because R3
   isolates period-two germs only over generic $\mathscr F$.
2. **Global branch matching — closed.** The conditional tests now
   occur on common global smooth loci, with the marked branch equal
   to the unique local germ of $\mathscr F$. The author includes
   the accepted four-branch $b_f$ example explaining why different
   local germs alone do not prove different global divisors.
3. **Smooth-base witness domain — closed.** Both files now explicitly
   place a proposed special witness in $\mathscr F\cap B^{\rm sm}$,
   the domain where the finite-flat incidence argument is being used.

The author confirmed the final files stable; their final changed
passages and hashes were independently checked. The initial complete
165/390-line files were read in full, followed by every reported
revision, not only the final status sentences.

| Final artifact | Lines | SHA256 |
| --- | ---: | --- |
| REPORT.md | 174 | `691937bb8cf086aa69e88725aefb4505147ec025e95c1fca9f3ea03553ba9f73` |
| PROOF_PACKAGE.md | 410 | `e320660178d4cab76c8af1c0269177324a1f59c5bbe9dae113c62fa2e6c5ca1c` |

Hashes bind the reviewed bytes; they do not prove the mathematics.
Final status: **zero unresolved mathematical/source-applicability
must-fixes in the local results and final conditional implications.**

The exact local formulas and original SF2 question survived unchanged.
The conditional bridge is approved only with the clarified
specialization and branch-matching hypotheses, not in an unrestricted
genericity formulation. This remains an auxiliary local proof/source
package, not completion of a new independent paper contract.

Only this exclusive review file was written. No mathematical program,
finite-period census, old checker, PDF build, extra child agent,
external model/API upload, Git action, or author/shared/frozen-file
write was performed by this reviewer. Proof-writer enforced exact
local versus conditional versus unproved statuses; research-review
was used as a current-team internal check, and research-lit supplied
the primary-source applicability and ownership audit.

**Handoff:** retain the proved local cusp and conormal interfaces;
subtract the direct-family classical no-escape and ambient-genericity
inputs; keep the all-period relative coverage/independence or witness
problem open. Do not infer SF2, higher-layer inertia, cycle-character
separation, FGT, target arithmetic or an admitted paper from this review.
