# Batch 07 — Paper 27 candidate v5: fresh R1 review

Review role: independent novelty/standalone/proof reviewer (R1)  
Review date: 2026-08-28 UTC  
Candidate: `positive_newton_translation_reciprocity_v5`  
Review boundary: authoritative `BATCH_07_STATUS.md` through E0051, the
charter, the permitted P22/P25/P26 note files, README/registry predecessor
rows, and a bounded public primary-source search.  I did not read any R2 or
earlier candidate-review artifact, manuscript, PDF, build root, temporary or
future root.  No computation, build, network upload, or external effect was
used.  The novelty-check and research-lit workflows were used only for the
bounded literature screen.

## Decision

**PASS.**  The finding census is zero and all numerical gates pass.  Paper 27
is not yet opened or numbered; this file is only the candidate R1 gate record.

| Gate | R1 result | Notes |
|---|---:|---|
| Blocker | 0 | No fatal scope, algebra, authority, or evidence issue. |
| Major | 0 | No unresolved theorem or collision defect. |
| Minor | 0 | E0051 removes the former multi-edge-core obligation. |
| Ambiguity | 0 | Latest append-only repairs control terminology and scope. |
| Novelty | 8.0 / 10 | Above 7.5; bounded search found no exact conjunction. |
| Standalone value | 8.0 / 10 | Above 7.5 after P22/P25/P26 absorption. |
| Proof readiness | 9.1 / 10 | Above 9.0 with the E0051 local lemma scope. |
| Anonymous content mass | 26–30 pages | Credible proof-first range; governance text excluded. |
| Gate 9 portfolio noncollision | PASS | P28–P31 axes are disjoint and unconsumed. |

## Exact theorem audited

The headline family is the separated Hamiltonian product shear

\[
H(q,p)=V(q)+W(p),\qquad
S_V(q,p)=(q,p+\nabla V(q)),\qquad
T_W(q,p)=(q+\nabla W(p),p),\qquad
F=T_W\circ S_V,
\]

over a characteristic-zero coefficient field.  The collected finite supports
are nonempty sets
\(E_V,E_W\subset\mathbb Z_{\ge 2}^{,r}\), with \(r\ge3\).  Degree vectors
live in an ordered real space and are not confused with the coefficient
field.  The headline quantifies strict exposed vertices and strict positive
carries; wall-face statements are auxiliary and require the stated
positive-support Hessian certificate.  Empty cells, exposed ties, nonpositive
carries, zero/unit support coordinates, positive characteristic, and
uncollected zero coefficients are outside the headline.

For an exposed pair \(e=(\alpha,\beta)\),

\[
A_\alpha={\bf1}\alpha^{\mathsf T}-I,\qquad
B_\beta={\bf1}\beta^{\mathsf T}-I,
\]

and the forward phase order is \(A_\alpha\) then \(B_\beta\).  The inverse is

\[
F^{-1}=S_V^{-1}\circ T_W^{-1},\quad
T_W^{-1}(q,p)=(q-\nabla W(p),p),\quad
S_V^{-1}(q,p)=(q,p-\nabla V(q)).
\]

The subtraction signs do not change a strict fresh leading degree.

### Weighted seeds and cells

For each edge, \(K_e\) is the positive orthant cut out by the displayed
strict rational score, carry, target, and reflected-score inequalities, and

\[
C_e^+=\{(u,w):u\in K_e,;w>0,;A_\alpha u-w>0\}.
\]

The theorem requires a nonempty positive-integer pair in each invoked cell.
Every such pair is realizable by disjoint monomial blocks with algebraically
independent leading forms, so weighted degree vectors are actual polynomial
degrees rather than formal labels.  The ordinary seed is the special case
\(u=w={\bf1}\).  The spans

\[
U_e=\operatorname{span}_{\mathbb R}\{u:(u,w)\in C_e^+\cap
(\mathbb Z_{>0}^r)^2\},\qquad
V_e=\operatorname{span}_{\mathbb R}\{A_\alpha u:(u,w)\text{ as above}\}
\]

are explicit hypotheses.  A full-matrix iff statement is made only when
\(U_e=V_e=\mathbb R^r\); on a proper span the claim is only about the
induced selector action.  The fixture supplies three independent integer
\(u\)-seeds in each cell, so no single-seed span overclaim remains.

### Translation and recurrence

With \(h_V(u)=\max_{\alpha\in E_V}\alpha\cdot u\) and
\(h_W(v)=\max_{\beta\in E_W}\beta\cdot v\), a strict step gives

\[
v_n=h_V(u_n){\bf1}-u_n,
\quad
\delta_n=((|\beta|-1)\alpha-\beta)\cdot u_n,
\quad
u_{n+1}=u_n+\delta_n{\bf1}.
\]

Thus \(u_n=u_0+t_n{\bf1}\), \(t_0=0\), and on a fixed phase

\[
t_{n+1}=\lambda_{\alpha,\beta}t_n+\mu_{\alpha,\beta},\qquad
\lambda_{\alpha,\beta}=(|\alpha|-1)(|\beta|-1),\qquad
\mu_{\alpha,\beta}=((|\beta|-1)\alpha-\beta)\cdot u_0.
\]

The formula uses one global origin (a phase-local origin is equivalent), and
\(\lambda>1\) under the positive-support assumption.  This is a weighted
degree law for certified orbits, not a claim about entropy, all dynamical
degrees, or a global map classification.

### E0050 global wall bound

Let
\(d_V=|\{|\alpha|:\alpha\in E_V\}|\) and
\(d_W=|\{|\beta|:\beta\in E_W\}|\).  Along
\(u(t)=u_0+t{\bf1}\), set
\(g(t)=h_V(u(t))-t\).  It is a strictly increasing upper envelope because
all slopes \(|\alpha|-1\) are positive.  Since

\[
v(t)=g(t){\bf1}-u_0,
\qquad
\beta\cdot v(t)-\eta\cdot v(t)
=(|\beta|-|\eta|)g(t)-(\beta-\eta)\cdot u_0,
\]

every unequal-total V wall and every unequal-total W wall is crossed at most
once globally; equal-total walls are invariant.  Therefore a strict exposed
orbit has at most

\[
\#\{​\text{selector changes}\}\le d_V+d_W-2.
\]

This is the controlling E0050 statement.  The earlier \(d_Vd_W-1\) and
\((M_V+1)(M_W+1)-1\) expressions are conservative historical bounds only.
The same argument with V/W interchanged applies to the inverse.  A strict
orbit consequently reaches a stationary phase after finitely many changes;
no nontrivial infinite or periodic strict selector word is asserted.

### Leading-form survival

For every positive exposed face \(F\), a generic secondary weight has a
unique minimizer \(\alpha_0\).  In the grouped Hessian expansion, the
all-\(\alpha_0\) tuple is the unique lowest group and has coefficient

\[
c_{\alpha_0}^{,r}(-1)^r(1-|\alpha_0|)\prod_i\alpha_{0i}\ne0.
\]

Characteristic zero and coordinates at least two make this coefficient
nonzero.  The Jacobian criterion gives algebraic independence of the face
gradient tuple, and injective substitution into independent input leading
forms prevents top cancellation.  Strict carries separate fresh and carried
blocks; inverse subtraction only changes signs.  The stated boundary fixture
\(V=(q_1+q_2+q_3)^3, W=(p_1-p_2)^3\) loses the predicted W half-step leading
form precisely outside this hypothesis, so the failure boundary is real and
correctly scoped.

### Reflected phase reciprocity

Let \(R\) reverse coordinates and
\(Rstate(u,w)=(Rw,Ru)\).  The reflected inverse starts from this swapped
state, uses \(R\alpha\) in its W phase and \(R\beta\) in its V phase, and
has the correct order/signs.  On the observable spans,

\[
B_{R\alpha}R=RA_\alpha,\qquad A_{R\beta}R=RB_\beta.
\]

Equality of both phase-resolved vectors for all integer seeds in a cell forces
these restrictions at \(n=1\); identities on every edge of the finite
seed-indexed word plus reflected carry checks imply all-iterate reciprocity by
induction.  Literal full matrices are claimed only at full spans.  Scalar
total-degree equality and same-seed reciprocity for a non-\(Rstate\)-fixed
pair are not substituted for the vector statement.

### E0051 lower-ideal scope

The authoritative perturbation result is local and one-step only.  On one
declared strict typed pair core, require positive \(\epsilon\)-interior,
selected-minus-new margins at least \(\eta>0\) on all four projected
sections \(V^+,W^+,W^-,V^-\), and the corresponding typed pair margins on the
source core.  The retained rows are respectively
\((\alpha,\beta,R\alpha,R\beta)\), with the selected-minus-lower sign
convention.  All lower exponents are integer support vectors with nonzero
coefficients.  These hypotheses preserve the one-step forward and reflected
inverse leading forms.  E0051 explicitly removes any v5 claim of transition
to a second core, C1→C2→C2 perturbation stability, or all-iterate lower-ideal
stability.  Earlier optional multi-edge wording is outside the headline and
must not be advertised as a theorem.

## Exact asymmetric fixture

\[
E_V=\{(8,2,2),(2,5,6),(2,8,2)\},\qquad
E_W=\{(2,2,8),(6,5,2)\},\qquad R(x_1,x_2,x_3)=(x_3,x_2,x_1).
\]

The matrices are \(A_1,A_2,B_1,B_2={\bf1}e^{\mathsf T}-I\) for the listed
rows.  The strict full pair cells \(C_1^+,C_2^+\) have the displayed K1/K2
score and carry inequalities.  Exact products are

\[
C_{21}=B_2A_1=I+{\bf1}(90,19,22),\qquad
C_{22}=B_2A_2=I+{\bf1}(18,55,70).
\]

The listed positive target, carry, reflected, and gamma-gap forms prove
\(C_1^+\to C_2^+\to C_2^+\), and the reflected identities prove the paired
minus-cell path.  The weighted seed
\(((2,1,1),(1,1,1))\) witnesses the transient C1 edge; the ordinary equal
seed is a separate stationary baseline with \(A_2{\bf1}=12{\bf1}\) and
\(C_{22}{\bf1}=144{\bf1}\).  The off-component point \((1,10,1)\) exposes
\(\gamma=(2,8,2)\), while \(R\gamma\notin E_W\), so the local reflection
component is not being recast as a global map reversor.  E0043's three seed
vectors give full U/V spans for both cells.

## Collision and portfolio census

The complete P12–P26 matrix is claim-level, not citation-by-inheritance:

| Predecessor | Closest owned result | R1 disposition |
|---:|---|---|
| P12 | Hénon period-three trace residue | No Newton/shear degree collision. |
| P13 | Primitive-cycle cover/monodromy | No separated shear selector automaton. |
| P14 | Monomial Hénon torus escape | No gradient-Hessian/reflected phase result. |
| P15 | Quartic Hénon trace fibres | No weighted selector graph. |
| P16 | Support-size torus escape | No selector matrices. |
| P17 | Sparse shift-like torus-coset decay | No Hamiltonian Newton reciprocity. |
| P18 | Marked trace/Fitting ramification | No leading-degree transport. |
| P19 | Maximal translates/support-one obstruction | No reflected cell graph. |
| P20 | Stationary two-mode matrix/visibility/quadratic Perron | Adjacent only; v5 is r≥3, multi-cell, bidirectional, and makes no bare quadratic claim. |
| P21 | Stationary three-mode cubic recurrence/visibility | Adjacent only; v5 makes no cubic or minimal-recurrence claim. |
| P22 | Endpoint-spiked cone, cubic quotient, box stability | Adjacent predecessor; endpoint family and cubic quotient are excluded, while v5 adds positive mixed-support translation/reciprocity. |
| P23 | Fixed staggered quartic spectral escape | Different support/mechanism; no collision. |
| P24 | Planar two-term period-two wall monodromy | Closest boundary, but v5 excludes planar exposed ties and wall exchange. |
| P25 | Support-rank factorization, Perron degree, minimal scalar order | Strong adjacent collision; all rank/Perron/minimality claims are anti-claims in v5. |
| P26 | Planar arbitrary-positive-support Newton envelope, contraction, forward/inverse rate bridge | Strongest thematic adjacent source; v5 is r≥3, uses all-ones translation and global wall monotonicity, and does not claim planar contraction or a rate bridge. |

The reserved unconsumed portfolio axes are disjoint: P28 primitive cycles of
length at least three/monodromy minimality; P29 toric cohomological degree
spectrum; P30 signed block-symplectic transfer characteristic reciprocity;
P31 zero-coordinate gradient cancellation.  None is silently imported into
P27.  There is no exact direct collision in the local P12–P26 corpus or the
bounded public screen.  The closest risks are P26 (thematic), P25 (support
and Perron vocabulary), and P24 (wall boundary), all explicitly separated.

## Public primary-source screen

Search date: 2026-08-28 UTC.  Query families were kept bounded and recorded
as follows:

1. `"Newton fan" automaton polynomial symplectic Hamiltonian shear degree
   growth`, `"Hessian" noncancellation Newton polytope polynomial
   automorphism degree`, and `"inverse degree" polynomial symplectic
   automorphism Hamiltonian shear`.
2. arXiv-restricted searches for `polynomial symplectic automorphism degree
   growth Hamiltonian shear`, `Newton polytope polynomial automorphism degree
   growth`, `tropical degree growth symplectic map`, and `dynamical degree
   polynomial symplectomorphism`.
3. `Hamiltonian product shears`, `Newton envelope degree polynomial map`,
   `projective contraction Newton polytope dynamics`, and `phase degree growth
   symplectic polynomial map`.
4. 2024–2026 searches for `tropical Newton support degree recurrence`,
   `Hamiltonian shear dynamical degree polynomial`, `all-ones translation
   degree vector`, `positive support gradient shear`, and `reflected inverse`.

The screen used only first-party arXiv records, DOI/journal pages, or author
records.  It did not claim global priority and could miss unindexed,
non-English, private, or inaccessible subscription material.  Representative
primary sources and exact relevant scope are:

1. Gómez–Meiss, *Reversors and Symmetries for Polynomial Automorphisms of the
   Plane*, arXiv (2003; revised 2003), Nonlinearity 17 (2004),
   https://arxiv.org/abs/nlin/0304035,
   https://doi.org/10.1088/0951-7715/17/3/012 — plane reversible polynomial
   automorphisms; adjacent, not a Newton-shear degree theorem.
2. Shafikov–Wolf, *Filtrations, hyperbolicity and dimension for polynomial
   automorphisms of C^n*, arXiv (2002),
   https://arxiv.org/abs/math/0207190 — higher-dimensional filtrations; no
   selector/reflection criterion.
3. Hasselblatt–Propp, *Degree-growth of monomial maps*, arXiv (2006; revised
   2007), https://arxiv.org/abs/math/0604521 — monomial degree/entropy
   sequences; no Hamiltonian support transport.
4. Bedford–Kim, *Linear Recurrences in the Degree Sequences of Monomial
   Mappings*, arXiv (2007), https://arxiv.org/abs/0710.1642 — monomial matrix
   recurrences; no separated shears.
5. Favre–Wulcan, *Degree growth of monomial maps and McMullen’s polytope
   algebra*, arXiv (2010; revised 2011),
   https://arxiv.org/abs/1011.2854 — polytope algebra/mixed volumes; no phase
   reciprocity.
6. Fordy–Hone, *Symplectic Maps from Cluster Algebras*, arXiv (2011), SIGMA
   7 (2011) 091, https://arxiv.org/abs/1105.2985,
   https://doi.org/10.3842/SIGMA.2011.091 — symplectic birational cluster
   maps and tropical recurrences; different map class.
7. Koch–Lomelí, *On Hamiltonian flows whose orbits are straight lines*,
   arXiv (2013), DCDS 34 (2014), https://arxiv.org/abs/1304.3377,
   https://doi.org/10.3934/dcds.2014.34.2091 — shear Hamiltonians/factorization;
   no iterate degree result.
8. Janeczko–Jelonek, *Polynomial symplectomorphisms*, BLMS 40 (2008),
   https://doi.org/10.1112/blms/bdm112 — group/transitivity structure; no
   reflected degree theorem.
9. Blanc–van Santen, *Dynamical degrees of affine-triangular automorphisms
   of affine spaces*, arXiv (2019; revised 2021),
   https://arxiv.org/abs/1912.01324,
   https://doi.org/10.1017/etds.2021.90 — affine-triangular dynamical degrees;
   different class.
10. Dang–Favre, *Spectral interpretations of dynamical degrees and
    applications*, arXiv (2020; revised 2021),
    https://arxiv.org/abs/2006.10262,
    https://doi.org/10.4007/annals.2021.194.1.5 — broad b-divisor/spectral
    framework; no support selector.
11. El Hilany, *The tropical non-properness set of a polynomial map*, arXiv
    (2022; revised 2024), https://arxiv.org/abs/2207.00989 — tropical
    Newton/polyhedral geometry; no iteration theorem.
12. Berger–Turaev, *Generators of groups of Hamiltonian maps*, arXiv (2022),
    Israel J. Math. 267 (2024), https://arxiv.org/abs/2210.14710,
    https://doi.org/10.1007/s11856-024-2709-7 — nonlinear position/momentum
    shear generators; no degree reciprocity.
13. Bianchi–Dinh–Rakhimov, *Monotonicity of dynamical degrees for Hénon-like
    and polynomial-like maps*, arXiv (2023), Trans. AMS 377 (2024),
    https://arxiv.org/abs/2307.10665 — general dynamical-degree monotonicity;
    no support-derived phase word.
14. Grigoriev, *A criterion of containment for tropical hypersurfaces*, arXiv
    (2024), https://arxiv.org/abs/2402.18384, and *Testing containment of
    tropical hypersurfaces*, JSC 132 (2026),
    https://doi.org/10.1016/j.jsc.2025.102472 — polyhedral containment, no
    Hamiltonian iteration.
15. Shao–Sun, *Dynamical degrees of affine-triangular automorphisms in
    dimension four*, arXiv (2025), https://arxiv.org/abs/2509.14584 —
    affine-triangular dimension-four bounds; different class.
16. Nisse, *Tropical Degrees and Stable Intersections*, arXiv (2026-05-24),
    https://arxiv.org/abs/2605.24966 — tropical degree/Newton polytope
    intersections; no iterate dynamics.
17. Takenawa, *Degree growth, orbit graphs, and functoriality for birational
    dynamical systems*, arXiv (2026-06-28),
    https://arxiv.org/abs/2606.29274 — finite-window orbit graphs and closed
    linear degree systems; no positive-support translation/reflection.
18. Abboud–Xie, *Dynamical degrees of twisted rational maps*, arXiv
    (2026-08-10), https://arxiv.org/abs/2608.09275 — relative/twisted
    dynamical degrees; no separated shear.
19. Déserti, *Degree growth of polynomial automorphisms and birational maps:
    some examples*, arXiv (2016; revised 2016), Eur. J. Math. 4 (2018),
    https://arxiv.org/abs/1602.04642,
    https://doi.org/10.1007/s40879-017-0175-z — higher-dimensional degree
    examples; no reflected support criterion.
20. Cheng–Wang–Yu, *Degree bounds for inverses of polynomial automorphisms*,
    Proc. AMS 120 (1994), https://doi.org/10.1090/S0002-9939-1994-1195715-1 —
    general inverse-degree bound; no phase reciprocity.

## Anti-claims and limitations retained

The candidate does not claim arbitrary supports, zero-coordinate extension,
an unconditional field algorithm, a global map-level reversor or
classification, entropy or higher dynamical degrees, a minimal scalar
recurrence/Perron algebraic degree, same-seed reciprocity for a non-fixed
pair, or priority.  The local lower-ideal lemma is not an all-iterate or
multi-edge perturbation theorem.  Exact fixture arithmetic is an example,
not evidence for a universal claim.  The public search is bounded and the
anonymous proof-page estimate assumes the four main proof objects and the
one-edge margin lemma are written explicitly.

All gates are therefore closed with a zero finding census at this candidate
stage.  No Paper 27 number or project is consumed by this review.

BATCH07_PAPER27_CANDIDATE_V5_REVIEW_R1_PASS
