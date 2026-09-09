# E6 — Nonauthor review of the good-model / periodic-jet boundaries

2026-09-09 UTC. Scope: B3, B4 and X2, with X1's fixed-point-diameter
criterion as a positive control. This reviewer did not author the submitted
constructions. This is an independent invocation and algebraic/source check,
not independent model-family evidence, human peer review, a formal Route-A
evaluation, or an admission decision. Calibration: `NOT_CALIBRATED`.
No venue-specific criteria binding was supplied or inferred.

## 1. Outcome and exact claims accepted

**No open mathematical must-fix was found in the claims as actually stated.**
The proofs support the following distinct conclusions. Their quantifiers are
essential; combining the conclusions does not produce a universal theorem
that periodic jets cannot detect good reduction.

| Package | Verified output | Boundary that must remain attached |
| --- | --- | --- |
| B3, [REPORT.md](../../lanes/b3_good_model_periods/REPORT.md), Theorem 2 | For every finite $J\ge0$, an explicit same-field, same-degree pair has the same specified marked native-cycle observables and opposite global affine-good-model answers. The field is $\mathbb Q(\sqrt{-23})$, degree $3J+4$, and marked least period three. | One marked cycle, not all periodic data; degree grows with $J$; obstruction is over the original number field, after every original local field passes. |
| B3, Lemmas 1 and 3 | Periodic points lie in the canonical affine projective-module lattice. A triangle's normalized determinant ideal has class $[I]^{-2}$ and detects its local collinearity defects. | The determinant identity is static exterior-power algebra; it does not supply periodic triangles or make primitivity equivalent to a frame. |
| B4, [PROOF_SUPPLEMENT.md](../../lanes/b4_wild_jet_detection/PROOF_SUPPLEMENT.md), Lemmas 1–2 | Scale-free forward/inverse finite-jet coefficient norm has an attained minimum equal to $T(M)=\max_i(1,\lvert\lambda_i\rvert,\lvert\lambda_i\rvert^{-1})$. A finite native cycle admits compatible integral polynomial transition charts, in every order simultaneously, exactly when its return eigenvalues are units. | Arbitrary scalar shrinking is allowed. One cycle gets one finite extension and finitely many charts; different cycles need not share any chart, radius, or extension. Degrees need not survive reduction. |
| B4, Theorem 3 | For the WM6 family, the complete false-positive locus of that specified test is $\lvert a\rvert=1$, $1<\lvert c\rvert\le \lvert p\rvert^{-r(d-k)/(d-1)}$. | The parameter classification and spectral envelope are imported WM6 results. This is a classification of one test, not of all intrinsic jet observables. |
| B4, Lemma 4 and Theorem 5 | Ambient jet-action spectra are monomials in derivative eigenvalues. Continuous Hausdorff-valued linear-conjugacy invariants on the full invertible jet space factor through the derivative; globally regular plane class functions lie in $K[\operatorname{tr}M,\det M,(\det M)^{-1}]$. | Full jet space, extension to the linear locus, and the stated continuity/regularity are indispensable. Exact derivative data are not multiplier norms. |
| X2, [PERIODIC_JET_COUNTEREXAMPLE.md](../../lanes/x2_obstruction_transfer/PERIODIC_JET_COUNTEREXAMPLE.md) | Every prescribed finite order $N$ is blind to potential affine-good reduction under raw centered forward/inverse jet integrality, even at every geometric periodic point and every repetition. The explicit map works for every prime. | Fixed displayed tangent coordinates, but growing degree; integrality and reduced jets, not equality of exact jets, return spectra, cycle counts, or cross-point positions. |
| X1, [INTERFACE_ATLAS.md](../../lanes/x1_interface_atlas/INTERFACE_ATLAS.md), §3 | For $\lvert a\rvert=1$, potential local affine-good reduction is equivalent to all roots of $f(Y)-(a+1)Y$ lying in one disk of radius $\lvert\operatorname{lc}f\rvert^{-1/(d-1)}$. | Geometric roots and a finite extension are allowed. This does not assert a chart over the original local field. |

Recommendation on substance: **retain this as a complete auxiliary boundary
package; do not count B3, B4, X2 or X1's positive control as separate new
substantial papers on the evidence reviewed.** The explicit constructions
are useful, and their stated negative tests are fully settled. After GR5,
WM6, interpolation, lattice theory and the primary-source subtraction below,
they do not settle the broader all-observable reconstruction question or
supply a new class-sensitive dynamical existence theorem.

## 2. B3: independent proof checks

### 2.1 Ideal arithmetic and the all-affine obstruction

Let $\omega=(1+\sqrt{-23})/2$, $R=\mathbb Z[\omega]$,
$I=(2,\omega-1)$ and $A=\omega+1$. The relation
$\omega^2-\omega+6=0$ gives
$N(m+n\omega)=m^2+mn+6n^2$. The two roots modulo two are distinct.
$A$ has norm eight and is zero at $I$, but not at the other prime
$(2,\omega)$. Consequently $(A)=I^3$. No element has norm two:
if $n\ne0$, the completed-square expression is at least $23/4$, and
if $n=0$ it is a square. Hence $I$ is not principal, and neither is
$I^2$, because $I=I^3/I^2$. No assertion about the entire class group
is needed. The class of $I$ has exact order three.

For $h=J+1$, the submitted map has degree $3h+1$ and leading
coefficient $A^{-h}$. If $sO_v=IO_v$, its scalar-conjugate nonlinear
term is

$$
\frac{s^{3h}}{A^h}\,y
 \prod_{\delta\in\{\alpha,\beta,\gamma\}}(y-\delta/s)^h,
\qquad
(\alpha,\beta,\gamma)=(-1-\omega,1-\omega,2\omega).
$$

All roots are integral in these coordinates and the prefactor is a unit.
The inverse is integral as well, both degrees survive, and the two
indeterminacy directions remain the coordinate directions. This passes
the regular-good definition at every finite place, including the primes
above two and three. It is not merely a Jacobian or lattice-invariance test.

The canonical scale ideal is exactly $I$, since
$(A^{-h})I^{3h}=R$. GR5's actual all-affine theorem then excludes every
global $K$-affine good coordinate map, not just common scalar changes.
This is a fixed-field nonexistence statement. It must not be relabeled
as nonexistence after every number-field extension.

Evidence anchors: B3 §§2.1–2.2; C426
[classification](../../../research_c424_c428/papers/C426_affine_good_models/sections/02_classification.tex),
[local rigidity](../../../research_c424_c428/papers/C426_affine_good_models/sections/03_local_rigidity.tex),
and [global obstruction](../../../research_c424_c428/papers/C426_affine_good_models/sections/05_global.tex).

### 2.2 Native period, all-prime primitivity and jets

The coordinates $\alpha,\beta,\gamma$ sum to zero and annihilate
$H(Y)=(Y-\alpha)(Y-\beta)(Y-\gamma)$. Thus the three stated points
are an actual orbit for one application of the submitted Hénon map.
With $u=2$, $v=3\omega-1$,

$$
(u,v)=I,\qquad
(u,v),\ (v,-u-v),\ (-u-v,u)
$$

are its oriented pair-difference vectors. The three vectors are related
by unimodular integral matrices. Dividing by any local generator of
$I$ makes each vector primitive. This proves pairwise distinctness in
every residue field, and exact least period three modulo every positive
prime power. An arbitrary good chart differs by an integral affine map,
so it preserves this conclusion. No characteristic-three exception is
hidden in the order-three linear map.

The determinant is
$-(u^2+uv+v^2)=51-9\omega=-3(3\omega-17)\ne0$.
Thus the original orbit is noncollinear. Pairwise distinctness modulo
every prime does not assert reduced noncollinearity.

The linear map $M(x,y)=(y,-x-y)$ has $M^3=1$. At each orbit point
the perturbation vanishes to order at least $h$. Centered substitutions
have zero constant term, so composition preserves the ideal of terms
of degree at least $h$. The return is therefore identity modulo
$\mathfrak m^{J+1}$. This argument is algebraic and uses no factorials.
For $J=0$ it only proves the required fixed-point equality; the
multiplier assertion is correctly restricted to $J\ge1$.

The comparison map
$F_\mathrm{good}=(y,-x-y+y(y^3-y)^h)$ is monic and integral in both
directions. Its cycle $(-1,0),(0,1),(1,-1)$ has pair-difference vectors
with a unit coordinate and determinant $-3$. The same order-of-vanishing
argument gives identical specified return jets. Fields, degrees,
Jacobians and marked reduction-period towers match exactly. Entire
periodic spectra and reduced maps away from that orbit do not match by
anything proved here.

Evidence anchors: B3 §§2.3–2.5, equations (3)–(8).

### 2.3 What the triangle ideal really contributes

If $P_i\in(r+I)^2$, then
$\Delta=\det(P_1-P_0,P_2-P_0)\in I^2$. Hence
$\mathfrak a_C=(\Delta)I^{-2}$ is integral and has class $[I]^{-2}$.
At a local scalar chart its valuation is that of $\Delta/s_v^2$;
this is positive exactly when the reduced triangle is collinear.
Integral affine changes multiply its determinant by a unit.

Thus an everywhere noncollinear reduced triangle forces $I^2$ principal.
Periodicity does not enter the calculation. The converse dynamical
supply assertion is false: the already globally good map
$(y,y^2+10-x)$ has no real periodic orbit, since the summed recurrence
would give $0=\sum_i((z_i-1)^2+9)$. Goodness cannot supply the frame
without a separate existence theorem.

The periodic-containment lemma also checks out: in a local good scalar
model, a periodic coordinate maximum $M>1$ would force a unit-leading
term of size $M^d$ to equal a recurrence sum of size at most $M$.
Intersecting the local disk squares gives the canonical affine module.
This justifies reduction on its residue modules without assuming global
freeness. It does not make those modules new arithmetic dynamical invariants.

Evidence anchors: B3 Lemmas 1 and 3 and the recurrence following (9).

## 3. B4: attained norm and simultaneous-cycle quantifiers

### 3.1 Attainment really includes inverse Jordan blocks

Every coefficient norm dominates the corresponding linear matrix norm;
an eigenvector over a finite extension proves the lower bound $T(M)$.
After splitting the characteristic polynomial, scale a Jordan block to
$B=\lambda I+\epsilon U$, with
$|\epsilon|\le\min(1,\min_i|\lambda_i|)$. Then

$$
B^{-1}=\lambda^{-1}\sum_{q=0}^{h-1}(-\epsilon U/\lambda)^q
$$

has norm at most $|\lambda|^{-1}$. The forward block has norm at most
$\max(1,|\lambda|)$. Thus a finite-extension basis attains the joint
linear bound even for repeated eigenvalues and nonsemisimple matrices.

A further common scalar $t$ multiplies a degree-$q$ nonlinear coefficient
of either germ by $t^{q-1}$. Finitely many coefficients can all be made
at most $T(M)$, so the infimum is an actual minimum. If both maps are
polynomial, one scalar handles every coefficient and therefore every
truncation at once. This is an elementary polynomial-germ assertion,
not an assertion about arbitrary infinite formal germs.

For example the one-dimensional formal germ
$z+\sum_{q\ge2}p^{-q^2}z^q$ has unit derivative, but no nonzero scalar
$t$ makes every forward coefficient integral: its degree-$q$ valuation
is $-q^2+(q-1)v_p(t)$. Every finite truncation can be treated separately.
This confirms why the submitted polynomiality restriction must stay.

Evidence anchor: B4 supplement §1, particularly (P4)–(P6).

### 3.2 The common shrink around a cycle is legitimate

For a unit-spectrum return $M$, its characteristic polynomial has
integral coefficients and unit constant coefficient. Starting with any
lattice $\Lambda'$, the finite sum
$\Lambda_0=\sum_{i=0}^{s-1}M^i\Lambda'$ is a full lattice. Both $M$
and $M^{-1}$ preserve it by Cayley–Hamilton. This does not require the
eigenvalues to lie in the cycle's field.

Transport $\Lambda_0$ using each one-step derivative. The last lattice
is again $\Lambda_0$, so bases with $A_n=A_0$ yield integral invertible
linear parts on every transition. There are only $2n$ forward/inverse
transition polynomials. Multiplying every $A_j$ by the same sufficiently
small $t$ places all their nonlinear coefficients in the maximal ideal
without disturbing the cyclic closure. Further shrinking separates the
finitely many distinct centers. Conversely, integral transition maps
and inverses give unit return eigenvalues by taking derivatives.

This proves a single common shrink within a given finite cycle. It does
not prove one affine map of the ambient plane, one common scale for all
cycles, or simultaneous containment of every periodic point in one
degree-preserving good lattice. The reduction of every transition may
be linear precisely because degree preservation is not required.

Evidence anchor: B4 supplement §2, equations (P8)–(P12).

### 3.3 The WM6 phase formula is correctly imported

For $d=p^m$, $k=p^r$, $m>r\ge1$, the reviewed WM6 proof gives
unit multipliers at every actual periodic point exactly on
$|a|=1$, $|c|\le C_*$, and potential regular-good reduction exactly on
$|a|=1$, $|c|\le1$. B4's lemmas convert the former into its jet/chart
test without adding parameter assumptions. The unit-Jacobian envelope
formula follows because the two eigenvalue norms have product one.

At $|a|\ne1$, the fixed point zero has eigenvalue norms
$|a|^{1/2}\ne1$. This prevents a vacuous all-periodic assertion.
The proofs include $p=2$, $a=-1$, $c=0$, the threshold equality,
ramified extensions, and repeated roots. A threshold not in the base
field's value group merely supplies no parameter at that boundary.
Finite extensions preserve the normalized absolute values; they do not
destroy the WM6 obstruction.

Evidence anchors: B4 supplement §3 and the imported
[WM6 proof](../../../research_c424_c428/continuation_round6/arithmetic_spectral/PROOF_PACKAGE.md), §§1–5.

## 4. B4's jet-spectrum and invariant no-go limits

The degree filtration on $W_N=\mathfrak m/\mathfrak m^{N+1}$ gives
diagonal blocks $\operatorname{Sym}^q(M^*)$. Triangularizing $M^*$
over an algebraic closure produces eigenvalues
$\lambda_1^{\alpha_1}\cdots\lambda_s^{\alpha_s}$ for
$1\le|\alpha|\le N$, one for each monomial index. Neither
diagonalizability nor characteristic zero is needed. The resulting
degree-normalized forward/inverse spectral radius is $T(M)$.

This concerns the fixed ambient truncated ideal/algebra. It is not the
local algebra obtained by imposing $F^n(z)-z=0$, so it does not recover
wild local intersection length or rule out retaining those equations.

For the topological statement, scalar conjugates
$t^{-1}g(tz)$ converge coefficientwise to $Dg_0$ as $t\to0$ through
nonzero elements of the local field. Continuity on the full jet space
and uniqueness of limits in the Hausdorff target then give
$\Phi(g)=\Phi(Dg_0)$. Continuity at the linear limit would suffice;
having no such limit point in the stated domain would not.

For regular algebraic functions, scalar conjugation gives positive
weights to all nonlinear coefficients and weight zero to the linear
coefficients and $\det(M)^{-1}$. Weight-zero regular functions cannot
contain nonlinear coefficients. The plane matrix invariant ring follows
by restriction to diagonal matrices, symmetric Laurent polynomials,
and the density of matrices with distinct eigenvalues. Invariance under
full jet conjugacy gives the same ring because the derivative transforms
by similarity. The submitted characteristic-zero hypotheses suffice.

The following counterchecks prevent stronger wording:

- The identity jet and $(x,y+x^2)$ have identical derivatives but are
  not conjugate as $N$-jets for $N\ge2$. An abstract nonlinear conjugacy
  class is not determined by the derivative.
- Ratios such as $v/u^2$ on $z+uz^2+vz^3$, $u\ne0$, survive scalar
  conjugacy and have no unrestricted extension to the linear jet.
  The report correctly does not call this a full universal jet invariant.
- Fixed volume or a scale calibrated from leading homogeneous terms
  removes scalar contraction from the allowed changes.
- Exact trace and eigenvalue values can vary while all their norms are
  one. The invariant theorem adds no nonlinear information beyond the
  derivative; it does not make the derivative constant on WM6's plateau.
- A function defined only on a restricted set of Hénon return jets,
  without extension to their linear limits, is not covered merely by
  being continuous on that smaller set.

Evidence anchors: B4 supplement §§4–6. These exclusions are already
present in the submitted theorem and are not newly required weakenings.

## 5. X2: fixed-coordinate finite-cutoff falsifier

Fix any prime $p$ and $N\ge1$. With
$L=\lfloor\log_pN\rfloor$, $r=L+3$, $k=p^r$, $d=p^{r+1}$,
$\Delta=d-k$ and $R=p^{1/\Delta}$, the submitted map is

$$
F(x,y)=(y,y^d+p^{-1}y^k-x).
$$

The cyclic recurrence bounds every periodic coordinate by $R$: above
$R$ the degree-$d$ term uniquely dominates, contradicting the maximal
coordinate bound on the other side. This applies to all least periods,
including one and two, with no periodic-orbit search.

For $1\le j<p^s$ the identity
$v_p\binom{p^s}{j}=s-v_p(j)$ follows from
$\binom{p^s}{j}=(p^s/j)\binom{p^s-1}{j-1}$, the latter factor being
a unit even at $p=2$. Since $N<k$, every required binomial is in this
range. The centered coefficient $b_j(z)$ satisfies

$$
|b_j(z)|\le
p^{-r+v_p(j)+(d-j)/(d-k)}<1\qquad(1\le j\le N).
$$

Indeed $v_p(j)\le L$ and
$-r+L+(d-j)/(d-k)<-3+p/(p-1)\le-1$.
The degree-$d$ summand has an extra factor $p^{-1}$ relative to this
bound; the degree-$k$ summand equals the displayed upper bound after
using $R^{d-k}=p$. There is no reversed inequality or missing wild case.

Every centered forward step therefore reduces to $J(u,v)=(v,-u)$
through order $N$. The inverse reduces to $J^{-1}$. Centered steps have
zero constant term, so truncation commutes with composition to the
required order. All return and inverse-return jets, including every
repetition, are integral and reduce to the corresponding powers of
$J$. Their linear determinants are one. Each finite orbit lies in a
finite extension, and every further extension preserves the inequalities.

The no-good-model step correctly uses GR5 after finite extension.
Monicity forces radius one. The polynomial
$Y^{d-1}+p^{-1}Y^{k-1}-2$ has a root $\xi$ of modulus $R$:
larger roots are excluded by domination; if all roots were smaller,
the Vieta coefficient $p^{-1}$ would have modulus less than $R^{d-k}=p$.
Repeated roots and $p=2$ do not alter this argument. Both zero and
$\xi$ are fixed points of $q=f-Y$, hence give native diagonal fixed
points. They cannot lie in one unit disk. Further extension to contain
$\xi$ preserves goodness, yielding the contradiction.

The estimate is genuinely stronger than a norm statement about first
derivatives: the entire prescribed raw coefficient truncation is small.
Nevertheless the centers themselves have been translated away. This
uses the same standard tangent basis at each center, not a single
integral ambient translation containing every center. Exact coefficients
are not identified with those of a good map, and the full cycle-count
ledger is not compared. This is no degree-independent finite-cutoff
integrality criterion, not a theorem about every finite-jet observable.

Evidence anchors: X2 proof Steps 1–4, especially (4)–(6).

## 6. X1 positive control and counterexamples to overextension

Let $E/\mathbb Q_p$ be finite, $F=(y,f(y)-ax)$, $d\ge2$,
$b=\operatorname{lc}f$ and $|a|=1$. Put
$H(Y)=f(Y)-(a+1)Y$ and $\rho=|b|^{-1/(d-1)}$.

Necessity follows from the GR5 disk containing every fixed point of
$q=f-aY$. For sufficiency choose one root $r$ as center and a finite
extension containing the roots and a scale $s$ with $|s|=\rho$.
Then $H(r+sY)/s$ has integral roots and unit leading coefficient, so
is integral. Adding $Y$ gives $(q(r+sY)-r)/s$, and GR5 applies.
Repeated roots are harmless. A finite set in an ultrametric field lies
in a radius-$\rho$ disk exactly when its pairwise diameter is at most
$\rho$. These are positions of actual native fixed points, not a change
of the native clock to $q$.

Two explicit controls show why the qualifications matter:

- Original-field descent fails: over $\mathbb Q_p$, take $a=1$ and
  $f(Y)=p^{-1}Y^3+2Y$. All diagonal fixed roots are zero, so the diameter
  condition holds. But the necessary scale valuation is $1/2$, not
  available in $\mathbb Q_p$. Over an extension with $s^2=p$, the
  scalar model is $(y,y^3+2y-x)$ and is good.
- The Jacobian hypothesis cannot be dropped: take $a=p$ and
  $f(Y)=Y^2+(p+1)Y$. Again all diagonal fixed roots are zero, now with
  $\rho=1$, but the nonunit determinant prevents both directions from
  being integral after any extension.

This positive control explains rather than contradicts the negative
results. B4 discards relative positions; X2 forgets centers; B3 concerns
global freeness after each local disk has already been found.

## 7. Primary-source ownership and residual substance

The following primary sources were actually accessed on 2026-09-09.
Only the indicated claims/passages were used; this is not an exhaustive
priority search or a rereview of their complete proofs.

| Source | Verified ownership and relevance |
| --- | --- |
| [Kawaguchi, *Local and global canonical height functions for affine space regular automorphisms*](https://msp.org/ant/2013/7-5/ant-v7-n5-p08-s.pdf), introduction's good-reduction definition | Regular polynomial-automorphism good reduction retains both degrees and regularity, not only integral coefficients. This validates the distinction between B4's tiny local germs and the GR5 model problem; it does not supply GR5's new all-affine classification. |
| [Pezda, *Cycles of polynomial mappings in several variables over rings of integers in finite extensions of the rationals*](https://www.impan.pl/shop/publication/transaction/download/product/83956), §2, Theorems 3.1–3.2, Corollary 3.1, Lemma 4.1 | $B(O_v,2)<\infty$ for polynomial maps is classical. Theorem 3.2 identifies the set of realizable lengths across all maps over a Dedekind domain with the intersection of local possibilities. It does not fix a Hénon map or solve a nonfree-lattice local–global problem. B3's distinction is correct. |
| [Hutz, *Good reduction of periodic points on projective varieties*](https://arxiv.org/pdf/0801.3645), Theorems 1–2 | Period/reduced-period/cotangent-order/residue-characteristic-power lifting is already owned. The displayed theorem requires a smooth projective model and a morphism. Hénon homogenization has indeterminacy, so direct application would be invalid. B3 explicitly avoids it and uses Pezda for its applicable affine bound. |
| [Ingram, §11 of *Hénon maps: a list of open problems*](https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html), cycle-prescription discussion before Question 46 and ideal sequence before Question 47 | Prescribing Hénon cycles through polynomial interpolation and using coordinate-difference ideals are explicit existing mechanisms. B3's residue-primitive nonfree-lattice realization is an exact additional compatibility example, not a new general interpolation method. |
| [Benedetto, *Determining Potential Good Reduction in Arithmetic Dynamics*](https://math.colorado.edu/arithmetic2015/slides/Benedetto.pdf), “But Not Conversely” | The one-dimensional wild phenomenon of no repelling periodic points without potential good reduction is explicitly exhibited. This is an original lecture source, not a journal proof of B4 or X2. WM6 already imports and extends the relevant norm-blind mechanism. |
| [Cantat–Dujardin, *Multiplier rigidity for complex Hénon maps*, v1](https://arxiv.org/html/2603.09445v1), Theorem A, Theorem B, §1.3 | Exact complex trace spectra give finite-ambiguity rigidity; the introduction states bounded-period finite determination. These are exact-value and complex-field results, not unit-norm local criteria. B4's scope correctly neither contradicts them nor claims their rigidity as new. No $p$-adic theorem is inferred from the complex statements. |

The Pezda publisher PDF failed twice in browser opening. A direct read-only
GET of that same publisher URL followed by streamed text extraction succeeded;
the cited sections were read. No PDF file was saved. The other sources were
read through their primary HTML/PDF endpoints. Search results from aggregators
were not used as theorem evidence. No private manuscript text was submitted
to a search engine or external model.

Local source subtraction is decisive:

- C426/GR5 already owns all-affine disk-square rigidity, all original-field
  local tests, global ideal-square obstruction, the order-three ideal,
  and nonscalar two-torsion repair. B3 imports these honestly.
- WM6 already owns the wild family, all-periodic multiplier-norm plateau,
  fixed-point attainment, the complete parameter phase boundary, and
  the monic large-root obstruction to potential affine-good reduction.
  B4's phase formulas and X2's obstruction are not new classifications.
- B4's remaining linear-lattice and contraction lemmas are general and
  useful, but elementary. Spectral triangularity and regular-invariant
  contraction explain a specified observable failure, not a broad new
  inverse problem solution.
- X2's uniform Hasse-coefficient estimate is a real quantitative increment
  beyond the first-derivative plateau. Its degree increases with the
  cutoff, and it does not identify all exact periodic observables.
- X1's positive criterion is GR5 plus root/coefficient formulas. B3's
  triangle class is GR5 plus an exterior-power calculation. Neither
  closes a new independent dynamical supply theorem.

Thus there are complete exact auxiliary questions here, but not evidence
for multiple substantial independent full-question papers after subtraction.
The larger arbitrary-intrinsic-observable question remains unclosed; it must
not be replaced by the negative answer for the chosen norm or raw-integrality
test. Conversely, already proved auxiliary theorems need not be reopened as
missing proofs simply because they are not admitted as papers.

## 8. Must-fixes, minor comments and allowed handoff wording

### Must-fixes

**Open mathematical must-fixes: zero. Open source-applicability must-fixes:
zero for the scoped conclusions above.** This is a judgment on the inspected
versions, not a clean certificate for uninspected future summaries.

Coverage receipt for finding no blocking defect:

| Dimension checked | Basis |
| --- | --- |
| B3 ideal and global criterion | Direct ideal/norm computation and actual GR5 theorem/proof interface agree. |
| B3 orbit and jet observables | All-prime primitivity, determinant, exact return truncation and matching comparison map were checked algebraically. |
| B4 local norm and cyclic charts | Explicit inverse Jordan estimate, Cayley–Hamilton lattice, finite common shrink and converse derivative argument close every implication. |
| B4 full-jet invariant claims | Filtration and contraction proofs are valid under the stated ambient-domain and regularity assumptions; stronger formulations were tested by counterexamples. |
| X2 all-prime finite cutoff | Binomial valuation, strict exponent inequality, zero-constant-term composition and geometric fixed-root obstruction hold for every prime. |
| Extension and source ownership | Original/global/potential field quantifiers are separated; classical inputs and imported phase theorems are explicitly subtracted. |

One optional editorial comment, not a mathematical must-fix: B4's report
calls $\mathfrak m/\mathfrak m^{N+1}$ a finite local algebra. “Truncated
maximal ideal” or “nonunital truncated local algebra” is more precise;
the unital local algebra is $K[[z]]/\mathfrak m^{N+1}$. Its extra constant
eigenvalue is one, so no stated spectrum or norm conclusion changes.
Severity: Minor. Evidence anchor: text: B4 REPORT, “finite local algebra”.
Confidence: 5/5 for this terminology distinction.

Allowed handoff wording:

> B3, B4 and X2 have independently checked exact counterexamples/boundaries
> for their specified marked-cycle, scale-free and fixed-cutoff integrality
> observables. They remain auxiliary after source subtraction. They do not
> establish universal finite-jet blindness, fixed-degree all-orders blindness,
> equality of complete exact periodic data, or a new local–global theorem for
> existence of native periodic points.

Do not shorten that to “all higher jets cannot detect good reduction.”
Do not merge B3's fixed-number-field class obstruction with WM6/X2's
nonexistence after every finite local extension. Do not infer target Euler
factors, root numbers, automorphy, target zero/divisor data or a Hilbert–Pólya
realization. `NO_BAD_EULER_OR_ROOT_NUMBER` remains intact.

## 9. Inspection provenance

Read in full: the four assigned B3/B4/X2 files and X1's atlas. Read the
actual C426 classification, local-rigidity and local-test proofs, the
global necessity argument and class-three example, and WM6's full proof.
The imported GR5 theorem was checked for correct use, not reopened for a
new comprehensive historical admission review. Reviewed file SHA256 values:

| File, relative to this batch | SHA256 |
| --- | --- |
| `lanes/b3_good_model_periods/REPORT.md` | `d11e9e8077390df1e6ad8de7b43710be634ec34ca840f87d719859897a73972e` |
| `lanes/b4_wild_jet_detection/REPORT.md` | `aa33c4cf9dc036e2cbc096a35d0cdbef46bd57622e855ed4445900380604f9f5` |
| `lanes/b4_wild_jet_detection/PROOF_SUPPLEMENT.md` | `80f728c1de3b27f463853ba31734ca3e8995378c103eadf4726ed578c1e5e6e3` |
| `lanes/x2_obstruction_transfer/PERIODIC_JET_COUNTEREXAMPLE.md` | `9d4083f42e55abe7f96403165a99940667569c6ac34f9472973d9ee26ed8d307` |
| `lanes/x1_interface_atlas/INTERFACE_ATLAS.md` | `ff17a9f634f599c52206fc398902c16082258aeb9cacab87bad724bc8b921930` |

The research-review skill's external-model workflow was not run because
the task forbids uploads and additional agents. Its evidence-backed
claims/limitations discipline and the ARS router/domain-review guidance
informed this bounded report; no full ARS panel, score aggregation or
external certification is claimed. All mathematical checks were hand
derivations. No mathematical code, old run, build, Git operation, shared
index, evaluator or submitted-source write was performed. The only file
created is this report in the assigned review directory.
