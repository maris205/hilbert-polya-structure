# HCS-C25 source audit: the AGY induced transfer model

## Material Passport

- Origin Skill: `research-lit / primary-source lock`
- Origin Mode: `source_audit`
- Origin Date: `2026-08-10T02:21:35Z`
- Verification Status: `SOURCE_VERIFIED_WITH_DERIVED_LEMMAS_LABELLED`
- Version Label: `hcs_c25_source_audit_v1`
- Primary object: the Avila--Gouëzel--Yoccoz precompact first-return model
  for a fixed Rauzy class, not an averaged Markov approximation
- Primary source: A. Avila, S. Gouëzel, J.-C. Yoccoz, *Exponential mixing
  for the Teichmüller flow*, Publ. Math. IHÉS **104** (2006), 143--211,
  <https://www.numdam.org/item/10.1007/s10240-006-0001-5.pdf>
- Official preprint: arXiv:math/0511614,
  <https://arxiv.org/abs/math/0511614>
- Boundary-space source: R. Aimino, M. Nicol, M. Todd, *Recurrence
  statistics for the space of Interval Exchange maps and the Teichmüller
  flow on the space of translation surfaces*, arXiv:1310.8422v2,
  <https://arxiv.org/abs/1310.8422>

The published AGY article is the formula authority.  The arXiv v1 and journal
numbering differ, and the arXiv v1 display in the proof of its Lemma 4.6 omits
both the projective normalization in the displayed inverse branch and the
minus sign in the relation between the roof and inverse Jacobian.  The
published formulas on pp. 164--165 have the normalization and the correct
relation

\[
r_\Xi\circ h=-\frac1d\log(J\circ h).
\]

This audit therefore never infers a sign convention from the defective v1
display.

## Rauzy matrix chronology

AGY Section 3.1.3, p. 154, fixes the literal cocycle convention.  If an arrow
has winner \(\alpha\) and loser \(\beta\), then

\[
B_\gamma e_\xi=e_\xi\quad(\xi\ne\alpha),
\qquad
B_\gamma e_\alpha=e_\alpha+e_\beta.
\]

For chronological concatenation \(\gamma_1\gamma_2\),

\[
\boxed{B_{\gamma_1\gamma_2}=B_{\gamma_2}B_{\gamma_1}.}
\]

Thus later arrows multiply on the left.  This is the same fixed-label
chronology used in HCS-C24.  A return branch retains its full Rauzy path
\(\gamma_h\), its chronological product \(B_{\gamma_h}\), and eventually a
pathwise metaplectic lift.  Neither a transition-frequency matrix nor an
average of branch cocycles is the AGY object.

The fixed-fibre lift is a project construction, not an AGY claim.  With
\(J_\pi=\Omega_\pi^{-1}\) and reference form \(J_0=J_{\pi_*}\), the
released certificate chooses seven integral frames \(S_\pi\) satisfying
\(S_\pi^TJ_\pi S_\pi=J_0\).  Every edge is then represented by

\[
g_e=S_{\mathrm{dst}}^{-1}B_eS_{\mathrm{src}}
\in\operatorname{Sp}(J_0,\mathbb Z).
\]

The fourteen exact edge matrices pass independent symplectic checks.  One
lift above each labeled edge can therefore be chosen and composed
chronologically; no central sign and no global group-theoretic splitting is
asserted.

## Acceleration and exact state space

The AGY acceleration is more than the ordinary same-winner Zorich
acceleration.  It is a first return of the Veech flow to a small precompact
section selected by a Rauzy word.

In Definition 4.1 and Lemma 4.2, pp. 160--161, a path \(\gamma\), from
\(\pi_s\) to \(\pi_e\), is **strongly positive** when it is positive and

\[
(B_\gamma^*)^{-1}(\Theta_{\pi_s}\setminus\{0\})\subset\Theta_{\pi_e}.
\]

Every \(k\)-complete path with \(k\ge 3|\mathcal A|-4\) is strongly
positive.  AGY Section 4.1.3, pp. 162--163, then chooses a strongly positive
loop \(\gamma_*\) based at one \(\pi\in\mathcal R\), subject to the no-proper
overlap condition

\[
\gamma_*=\gamma_s\gamma=\gamma\gamma_e
\quad\Longrightarrow\quad
\gamma\text{ is trivial or }\gamma=\gamma_*.
\]

AGY calls such a word **neat**.  With this frozen word, the state spaces are

\[
\widehat\Xi
=\widehat\Upsilon_{\mathcal R}^{(1)}
  \cap(\Delta_{\gamma_*}\times\Theta_{\gamma_*}),
\qquad
\Xi=\Upsilon_{\mathcal R}^{0}\cap\Delta_{\gamma_*}.
\]

The map \(T_{\widehat\Xi}\) is the first return of the Veech flow to
\(\widehat\Xi\), and it is a skew product over the noninvertible base map
\(T_\Xi\).  Its branch paths form the countable set \(\Gamma\) consisting of
\(\gamma_*\) and the minimal paths of the form
\(\gamma_*\gamma_0\gamma_*\) that do not begin with
\(\gamma_*\gamma_*\); see Section 4.1.3 and Lemma 4.4, pp. 162 and 165.

This construction is source-standard after \(\gamma_*\) is frozen, but it is
not intrinsically unique.  AGY explicitly says that it chooses a particular
precompact section, and the proof of Lemma 4.3 also notes freedom in the
Finsler metric.  Therefore HCS-C25 must record the concrete base state and
the complete edge-token word \(\gamma_*\); the phrase "the canonical AGY
space" without this data is too strong.

## Full branches, inverse branches, Jacobian, and roof

On the forward branch labelled by \(\gamma\in\Gamma\), equations (4.8)--(4.9),
p. 163, give

\[
T_{\widehat\Xi}(\lambda,\pi,\tau)
=\left(
  \frac{(B_\gamma^*)^{-1}\lambda}
       {\|(B_\gamma^*)^{-1}\lambda\|},
  \pi,
  \|(B_\gamma^*)^{-1}\lambda\|(B_\gamma^*)^{-1}\tau
 \right),
\]

and

\[
r_\Xi(\lambda,\pi)
=-\log\|(B_\gamma^*)^{-1}\lambda\|.
\]

In the proof of Lemma 4.3, pp. 164--165, the base \(\Xi\), with the Hilbert
Finsler metric and induced Lebesgue measure, is a John domain and
\(T_\Xi\) is a countable full-branch uniformly expanding Markov map.  The
inverse branch is

\[
h_\gamma(\lambda,\pi)
=\left(\frac{B_\gamma^*\lambda}{\|B_\gamma^*\lambda\|},\pi\right).
\]

If \(d=|\mathcal A|\), and \(J\) denotes the inverse Jacobian of \(T_\Xi\)
with respect to the induced Lebesgue measure as in Definition 2.2, then

\[
J(h_\gamma(\lambda,\pi))
=\|B_\gamma^*\lambda\|^{-d}.
\]

Lemma 4.5, pp. 165--166, identifies inverse branches with \(\Gamma\) and
gives

\[
r_\gamma(x):=r_\Xi(h_\gamma x)
=\log\|B_\gamma^*\lambda\|\ge\log 2,
\qquad
J_\gamma(x):=J(h_\gamma x)=e^{-d r_\gamma(x)}.
\]

It proves that \(r_\Xi\) is a good roof in the sense of Definition 2.3.
Theorem 4.6, stated on p. 166 and proved in Section 6 on p. 181, gives an
unspecified \(\sigma_0>0\) such that

\[
\int_\Xi e^{\sigma_0 r_\Xi}\,d\mathrm{Leb}<\infty.
\]

The full branch word and its chronological matrix are therefore preserved in
both \(r_\gamma\) and the proposed fiber operator.  This is genuine induced
dynamics, not a chronological average.

## AGY analytic space and weighted transfer operator

Definitions 2.1--2.4, pp. 145--147, supply the abstract John domain,
uniform expansion, distortion, good-roof, and exponential-tail hypotheses.
Equation (2.1), p. 147, defines

\[
C_b^1(\Xi)
=\{u:\Xi\to\mathbb C:
u\text{ and }Du\text{ are bounded and continuous}\},
\qquad
\|u\|_{C^1}=\|u\|_\infty+\|Du\|_\infty.
\]

AGY Section 7.3, equation (7.13), p. 187, defines, for
\(\Re s>-\sigma_0\),

\[
L_su(x)
=\sum_{T_\Xi y=x}e^{-s r_\Xi(y)}J(y)u(y)
=\sum_{h\in\mathcal H}
  e^{-s r_h(x)}J_h(x)u(hx).
\]

The space used for the scalar spectral argument is \(C_b^1(\Xi)\), with the
frequency-dependent equivalent norm

\[
\|u\|_{1,t}
=\|u\|_\infty+\frac{1}{\max(1,|t|)}\|Du\|_\infty
\tag{7.14}
\]

for \(s=\sigma+it\).  Proposition 7.7 gives the high-frequency Dolgopyat
estimate, equation (7.15), and equation (7.16) defines the normalized
operator

\[
\widetilde L_su=\frac{L_s(f_\sigma u)}{\lambda_\sigma f_\sigma}.
\]

Lemma 7.8 gives the derivative/Lasota--Yorke bound for its iterates.  Lemma
7.18, pp. 199--200, explicitly uses the uniform finiteness of weighted branch
sums such as

\[
\sum_{h\in\mathcal H}e^{(3\sigma_0/4)r_h(x)}J_h(x).
\]

The suspension-observable spaces \(B_0\) and \(B_1\) in Definitions
7.1--7.2, pp. 182--183, are not the base transfer space and should not be
silently substituted for \(C_b^1(\Xi)\).  Likewise, Proposition 7.7 estimates
an \(L^2\) norm of \(L_s^ku\) for \(C^1\) input; it does not declare a
trace-class or nuclear Hilbert-space realization.

### Derived lemma: absolute branch-norm summability on `C_b^1`

This paragraph is an audit derivation from the cited AGY hypotheses, not a
verbatim theorem in the paper.  Put

\[
A_{h,s}u(x)=e^{-s r_h(x)}J_h(x)u(hx).
\]

Definitions 2.2--2.3 give constants independent of \(h\) with

\[
\|Dh\|\le\kappa^{-1},\qquad
\|Dr_h\|_\infty\le C_r,\qquad
\|D\log J_h\|_\infty\le C_J.
\]

Consequently, for fixed \(s\),

\[
\|A_{h,s}\|_{C^1\to C^1}
\le C_s\sup_{x\in\Xi}e^{-\Re(s)r_h(x)}J_h(x).
\tag{A}
\]

The logarithm of the positive weight on the right has uniformly bounded
derivative.  Since the John-domain distance on \(\Xi\) is bounded, bounded
distortion compares its supremum to its integral with a constant independent
of \(h\).  A branchwise change of variables then gives

\[
\begin{aligned}
\sum_h\sup_\Xi e^{-\Re(s)r_h}J_h
&\le C_s'\sum_h\int_\Xi e^{-\Re(s)r_h(x)}J_h(x)\,dx\\
&=C_s'\int_\Xi e^{-\Re(s)r_\Xi(y)}\,dy<\infty
\end{aligned}
\]

whenever \(\Re s>-\sigma_0\).  Combining this with (A) yields

\[
\boxed{
\sum_{h\in\mathcal H}\|A_{h,s}\|_{C^1\to C^1}<\infty,
\qquad \Re s>-\sigma_0.
}
\tag{B}
\]

Thus the literal vector-valued extension

\[
\mathcal L_s^{\mathrm{Mp}}F(x)
=\sum_{h\in\mathcal H}
e^{-s r_h(x)}J_h(x)
\mu(\widetilde B_{\gamma_h})F(hx)
\tag{C}
\]

converges in operator norm on \(C_b^1(\Xi;L^2(\mathbb R^2))\), provided a
pathwise metaplectic lift is frozen and the fiber factors are unitary.  This
extension and conclusion (B) are project deductions; AGY proves the scalar
estimates but does not discuss metaplectic fibers.  Here
\(\widetilde B_{\gamma_h}\) also presupposes the fixed symplectic
trivialization already audited in HCS-C24.

## Branch isolation and bounded projections

### The AGY `C^1` space

Multiplication by a raw branch indicator
\(1_{h(\Xi)}\) is generally **not** a bounded endomorphism of the global
space \(C_b^1(\Xi)\): the indicator jumps at the branch boundary.  No AGY
result supplies such a cylinder projection on this space.

This does not block exact branch isolation.  Lemma 7.5, pp. 186--187, proves
the existence of bounded \(C^1\) bump functions supported in any ball
compactly contained in \(\Xi\).  For a fixed branch \(h_0\), choose such a
bump \(\rho\) with

\[
\operatorname{supp}\rho\Subset h_0(\Xi)
\]

and choose \(x_0\) with \(\rho(h_0x_0)=1\).  The branch images form a
partition, so for every fiber vector \(v\),

\[
\operatorname{ev}_{x_0}\,
\mathcal L_s^{\mathrm{Mp}}(\rho\,v)
=e^{-s r_{h_0}(x_0)}J_{h_0}(x_0)
 \mu(\widetilde B_{\gamma_{h_0}})v.
\tag{D}
\]

The injection \(v\mapsto\rho v\) and evaluation at \(x_0\) are bounded.
The scalar coefficient in (D) is nonzero.  Hence (D) is an exact nonzero
single-branch compression, without any characteristic-function projection
and without mixing branch chronologies.  Together with (B), this is the
recommended HCS-C25 large gate for the C24 tensor-compression obstruction.

### Canonical Hilbert companion, with a scope warning

Definition 2.2 gives the unique invariant probability
\(d\mu=f_0\,d\mathrm{Leb}\), where \(f_0\in C^1\) is bounded above and below.
It therefore also gives a canonical Hilbert realization after the inducing
word is frozen.  Define

\[
p_h(x)=\frac{J_h(x)f_0(hx)}{f_0(x)},
\qquad \sum_hp_h(x)=1,
\]

and the normalized vector operator

\[
\mathcal P_s^{\mathrm{Mp}}F(x)
=\sum_h p_h(x)e^{-s r_h(x)}
  \mu(\widetilde B_{\gamma_h})F(hx).
\]

A direct Jensen inequality and invariance of \(\mu\) show

\[
\|\mathcal P_s^{\mathrm{Mp}}\|_{L^2(\mu;\mathcal F)\to
L^2(\mu;\mathcal F)}\le1,
\qquad \Re s\ge0.
\tag{E}
\]

Before Jensen is applied, Cauchy--Schwarz and branch disintegration show
that the countable Bochner series is absolutely convergent almost everywhere
and unconditionally convergent in \(L^2(\mu;\mathcal F)\): its tail over a
set \(A\) of branches has squared norm at most

\[
\int_{\bigcup_{h\in A}h(\Xi)}\|F(y)\|_{\mathcal F}^2\,d\mu(y).
\]

On this Hilbert space, multiplication by \(1_{h(\Xi)}\) is an orthogonal
projection of norm one and exactly isolates the branch \(h\).  Thus the
same branch-compression obstruction has an especially transparent Hilbert
form on \(\Re s\ge0\).  Equation (E) is a project derivation from AGY's
invariant density, not AGY's claimed spectral-gap space.  AGY's quasicompact
analysis remains the \(C^1\) analysis above.

This normalized \(L^2\) obstruction is not caused by the metaplectic fibre.
With every fibre multiplier equal to one, nonatomicity makes every nonzero
branch weighted composition noncompact throughout \(\Re s\ge0\); on the
imaginary axis the scalar Perron--Frobenius operator is also the adjoint of
an isometric Koopman operator and hence a coisometry.  The Hilbert companion
is kept as a space-level robustness test; the oscillator-specific
source-space gate is the \(C_b^1\) bump/evaluation compression.

For completeness, the unnormalized scalar branch operator on
\(L^2(\mathrm{Leb})\) satisfies

\[
\|A_{h,s}\|_2^2
=\operatorname*{ess\,sup}_{y\in h(\Xi)}
J(y)e^{-2\Re(s)r_\Xi(y)}.
\]

Using \(J=e^{-dr}\) on a branch and exponential tails gives the derived
sufficient condition

\[
\sum_h\|A_{h,s}\|_2<\infty
\quad\text{if}\quad
\Re s\ge \frac d2-\sigma_0.
\]

For \(\mathcal H(2)\), \(d=4\), so this is
\(\Re s\ge2-\sigma_0\).  AGY does not give a numerical \(\sigma_0\), and it
does not prove absolute \(L^2\) branch-norm summability on the imaginary
axis.  The bounded cylinder projection in (E), not this far-right sufficient
sum, is therefore the robust Hilbert gate.

## Prior-art boundary for the two derived mechanisms

This targeted audit does not treat absence of a located paper as novelty
evidence.

For the decoder, the closest classical source is S. P. Kerckhoff,
*Simplicial systems for interval exchange maps and measured foliations*,
Ergodic Theory Dynam. Systems **5** (1985), 257--271,
<https://doi.org/10.1017/S0143385700002881>.  Its first-stage projective
cones and refinement cylinders supply the standard coding geometry behind
first-edge separation.  The audit did not locate there an explicit theorem
stated as “one cumulative fixed-start matrix is inverted by winner-row
subtraction,” so C25 proves that algorithm directly and describes it as an
explicit algorithmic restatement, not as a broadly novel coding principle.
The Veech/Fickenscher “decoding Rauzy induction” results concern recovery of
an unknown initial permutation from infinite or sufficiently complete
matrix sequences and are not used as either this theorem or a counterexample
to it.

For the fibre obstruction, J. M. Bonet, M. C. Gómez-Collado, D. Jornet, and
E. Wolf, *Operator-weighted composition operators between weighted spaces
of vector-valued analytic functions*, Ann. Acad. Sci. Fenn. Math. **37**
(2012), 319--338, <https://doi.org/10.5186/aasfm.2012.3723>, already give
evaluation factorizations showing that compactness of a single
operator-weighted composition map forces compact point weights.  Thus the
bare “infinite-dimensional unitary weight is noncompact” mechanism is prior
art.  The additional C25 statement is the exact localization of such a
weight inside an absolutely convergent **multi-branch** AGY transfer sum,
with its full source half-plane and normalized \(L^2\) companion.

The nearest transfer-operator benchmark located in this audit is M. Magee
and F. Naud, *Explicit spectral gaps for random covers of Riemann surfaces*,
Publ. Math. IHÉS **132** (2020), 137--179,
<https://doi.org/10.1007/s10240-020-00118-w>.  It permits arbitrary Hilbert
unitary twists for norm estimates, while its trace-class/Fredholm
determinant construction is made for finite-dimensional twists.  This
supports the scope distinction used here; it is not cited as proving the
specific AGY multi-branch theorem or the exact essential-norm formula.

## Quasi-Hölder boundary: Aimino--Nicol--Todd

Aimino--Nicol--Todd Section 1.5, pp. 8--9 of arXiv:1310.8422v2, starts from
the Zorich map \(T_1\), chooses a finite dynamical cylinder
\(B\Subset\mathcal R\times\Delta\), and defines the first return
\(T_2:B\to B\).  It has a countable partition
\(\mathcal Q=\{B_i\}_{i\in I}\), and each
\(T_2:B_i\to B\) is a diffeomorphism.  Proposition 1.4 records full-branch
expansion, distortion, Jacobian control, and the Markov property.

Section 1.6, pp. 9--12, defines

\[
|f|_\alpha
=\sup_{0<\varepsilon\le\varepsilon_0}
\varepsilon^{-\alpha}
\int_B\operatorname{osc}(f,B_\varepsilon(x))\,dm(x),
\qquad
V_\alpha(B)=\{f\in L^1(m):|f|_\alpha<\infty\}.
\]

With \(\|f\|_\alpha=|f|_\alpha+\|f\|_1\), this is a Banach algebra that
contains characteristic functions of **some** measurable sets.  Lemma 1.6
controls the individual inverse-branch operators, Lemma 1.7 gives a
Lasota--Yorke estimate, and Proposition 1.8 proves quasicompactness and a
spectral gap for the full transfer operator.

The paper does **not** state that

\[
1_{B_i}\in V_\alpha(B)
\quad\text{for every return branch }B_i.
\]

Remark 2.3, p. 14, gives the sufficient boundary-neighborhood condition

\[
\sup_{0<\varepsilon\le\varepsilon_0}
\frac{m(B_\varepsilon(\partial A))}{\varepsilon^\alpha}<\infty
\quad\Longrightarrow\quad 1_A\in V_\alpha.
\]

It applies this explicitly to balls, not to every \(B_i\).  Therefore a
bounded cylinder projection
\(f\mapsto1_{B_i}f\) on \(V_\alpha\) is recorded here as
**OPEN/CONDITIONAL**: it follows from the Banach-algebra property if the
displayed boundary estimate is proved uniformly for that branch, but that
verification is not supplied by arXiv:1310.8422.  The quasi-Hölder route is a
useful fallback, not the source-locked C25 gate.

## Numbering crosswalk

The source locations used above have the following preprint/journal
crosswalk.

| Object | Published article | arXiv:math/0511614v1 |
|---|---:|---:|
| hyperbolic skew product | Lemma 4.3 | Lemma 4.4 |
| good roof | Lemma 4.5 | Lemma 4.6 |
| exponential tails | Theorem 4.6 | Theorem 4.7 |
| bump functions | Lemma 7.5 | Lemma 7.6 |
| weighted transfer | (7.13) | (7.14) |
| \(\|\cdot\|_{1,t}\) | (7.14) | (7.15) |
| Dolgopyat estimate | Proposition 7.7 | Proposition 7.8 |
| normalized transfer | (7.16) | (7.17) |
| derivative estimate | Lemma 7.8 | Lemma 7.9 |
| explicit weighted branch sum | Lemma 7.18 | Lemma 7.19 |

## Claim / nonclaim ledger

### Source-locked claims

1. AGY supplies a countable full-branch, uniformly expanding first-return
   map on the precompact projective simplex \(\Xi\), once a neat strongly
   positive loop \(\gamma_*\) is frozen.
2. Every branch retains a complete chronological Rauzy word, its matrix
   product, a projective inverse branch, its exact roof, and its inverse
   Jacobian.
3. The source transfer operator is the weighted operator (7.13) on
   \(C_b^1(\Xi)\); the roof is good and has exponential tails.
4. AGY provides compactly supported \(C^1\) bumps, sufficient for exact
   localization inside one branch.
5. Aimino--Nicol--Todd provides a quasi-Hölder transfer space for a related
   compact-cylinder first return and proves quasicompactness there.

### Derived project claims

1. The AGY bounds imply the absolute \(C^1\) branch-norm sum (B) on
   \(\Re s>-\sigma_0\).
2. Branchwise unitary metaplectic factors preserve that norm estimate.
3. Bump injection followed by point evaluation gives the exact nonzero
   chronology-preserving branch compression (D).
4. The invariant-density normalization gives the bounded Hilbert companion
   (E), where ordinary cylinder indicators are orthogonal projections.

These deductions require proof in the C25 theorem package; they are not
attributed verbatim to AGY.

### Explicit nonclaims

- There is no unique AGY inducing word or unique intrinsic "canonical
  section" before \(\gamma_*\) is fixed.
- AGY does not choose a metaplectic lift or its central sign.
- AGY does not prove the metaplectic extension nuclear, compact, trace
  class, or determinant class.
- A scalar spectral gap does not make a discrete infinite-dimensional
  unitary fiber compact.
- The global \(C_b^1\) space has no raw characteristic-function cylinder
  projection; the audit uses source-provided bumps instead.
- arXiv:1310.8422 does not prove \(1_{B_i}\in V_\alpha\) for every branch;
  that statement remains conditional on a boundary-neighborhood estimate.
- No averaged transition matrix may replace the ordered Rauzy path or its
  ordered KZ/metaplectic product.
- No trace formula, zeta-zero match, self-adjoint Hilbert--Pólya operator, or
  arithmetic prime law is claimed by this source audit.

## Gate recommendation

The one-round large gate should use the **published AGY precompact
first-return model on vector-valued \(C_b^1(\Xi)\)**, with a concrete
strongly positive neat \(\gamma_*\) reconstructed from the literal HCS-C24
Rauzy graph.  Prove (B), define (C) with pathwise lift signs, and implement
the bump/evaluation compression (D).  If these steps pass, the C24
noncompactness theorem applies directly to this source-faithful analytic
realization; no quasi-Hölder boundary regularity and no same-matrix
cancellation computation is needed.  The \(L^2(\mu)\) cylinder-projection
argument should be retained as an independent robustness check, not
misreported as AGY's quasicompact spectral space.
