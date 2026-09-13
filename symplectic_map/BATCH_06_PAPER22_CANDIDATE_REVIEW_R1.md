# Batch 06 Paper 22 — Independent Candidate Novelty and Portfolio Review R1

**Review date:** 2026-08-24 (UTC)  
**Reviewer role:** fresh independent bounded candidate reviewer  
**Candidate stage:** theorem-design gate only; no manuscript, build, release, or
external action is authorized by this review  
**Independence statement:** the reviewer authored neither the candidate
mathematics nor the Batch 06 charter and did not read, request, or wait for any
sibling R2 candidate-review artifact.  The algebra below was recomputed from
the candidate definition.  Public-source access was read-only and restricted
to primary or authoritative records; no manuscript or project file was
uploaded, and no cross-model API was called.

## 1. Executive disposition

**Verdict: bounded candidate GO, with mandatory claim and portfolio locks.**

The candidate clears the three numerical gates, narrowly on portfolio-adjusted
novelty:

| Gate | Required | R1 score | Disposition |
|---|---:|---:|---|
| Novelty | at least 7.5 | **7.6/10** | PASS, bounded and portfolio-adjusted |
| Standalone value | at least 7.5 | **7.8/10** | PASS if the spectral-collapse theorem is the headline |
| Proof plausibility | at least 9.0 | **9.4/10** | PASS after direct algebraic recomputation |

The defensible new object is not merely “the Paper 21 construction with more
coordinates.”  It is the stable-rank phenomenon that, for every public rank
`r >= 4`, the growing `r x r` exact degree matrix has an `(r-3)`-dimensional
semisimple unit eigenspace and a three-dimensional symmetric quotient carrying
the Perron root.  Thus the nontrivial characteristic factor and the exact
degree-sequence annihilator remain cubic while the ambient symplectic dimension
grows.  The sharp ordinary-degree seed threshold `g = 2r` and the uniform
selector/carry proof complete a credible standalone package.

The novelty margin is intentionally small.  Papers 20 and 21 are direct owned
predecessors of the same product-plus-pure-power template in ranks two and
three.  Paper 21 is exactly the `m=1` specialization of the quotient formulas
below on its declared domain.  Paper 22 may proceed only with an explicit
no-parallel-claim rule and with a public headline beginning at `r >= 4`.

This is not publication readiness and not a global priority finding.

## 2. Candidate identity and frozen public theorem range

Let `K` be a field of characteristic zero, let `r >= 4`, and let
`g >= 2r+1`.  Put

\[
 V_{r,g}(q)=\prod_{i=1}^r q_i^2+q_1^g,
 \qquad
 W_{r,g}(p)=\prod_{i=1}^r p_i^2+p_r^g,
\]

\[
 S(q,p)=(q,p+\nabla V_{r,g}(q)),\qquad
 T(q,p)=(q+\nabla W_{r,g}(p),p),\qquad F=T\circ S.
\]

Write

\[
 M_r=2\mathbf 1\mathbf 1^{\mathsf T}-I_r,
\]

replace row one of `M_r` by `(g-1)e_1^T` to obtain `A`, replace
row `r` by `(g-1)e_r^T` to obtain `B`, and set `C=BA`.

The admissible public theorem is bounded to this displayed family and to
`r >= 4`.  The title should expose that boundary, for example:

> **Cubic Spectral Collapse for Product-Coupled Hamiltonian Shears in
> \(\mathbb A^{2r}\), \(r\ge4\)**

“All-dimensional” is acceptable only if the title or first sentence gives
`r >= 4`; “first,” “new Perron realization,” and “arbitrary Hamiltonian
shears” are not acceptable.

## 3. Independent proof-plausibility recomputation

### 3.1 Symplecticity and support rows

Both maps are polynomial automorphisms, with subtraction inverses.  Their
Jacobian matrices have the triangular blocks

\[
 J_S=\begin{pmatrix}I&0\\ \nabla^2V&I\end{pmatrix},\qquad
 J_T=\begin{pmatrix}I&\nabla^2W\\0&I\end{pmatrix}.
\]

Hessian symmetry proves preservation of the standard symplectic form.  This
argument works over every characteristic-zero field; algebraic closedness is
not needed for the degree theorem.

For the product term, the gradient support row in coordinate `i` has weight

\[
 2\sum_{j=1}^r u_j-u_i=(M_ru)_i.
\]

The only competing rows are the pure row `(g-1)u_1` in the first shear and
the pure row `(g-1)v_r` in the second.  Consequently `A` and `B` are the
correct candidate phase matrices once the two strict selectors are proved.

### 3.2 Exact selector algebra

Put

\[
 m=r-2\ge2,\qquad h=g-1\ge2m+4,
\]

normalize `u_1=1`, and write

\[
 x_i=u_i/u_1,\quad
 X=\sum_{i=2}^r x_i,\quad
 y=x_r,\quad
 Z=\sum_{i=2}^{r-1}x_i=X-y.
\]

The proposed invariant region is

\[
 \mathcal K_{m,h}=
 \left\{x_i\ge1\ (2\le i\le r),\quad
 X<\frac{h-1}{2}\right\}.
\]

The first exact face margin is

\[
 \Delta_S=h-(1+2X)=h-1-2X>0.
\]

After the first phase,

\[
 v_1=h,\qquad v_i=2+2X-x_i\quad(2\le i\le r),
\]

and

\[
 \sum_i v_i=h+2(m+1)+(2m+1)X.
\]

The second exact face margin is therefore

\[
\begin{aligned}
 \Delta_T
 &=h v_r-\left(2\sum_i v_i-v_r\right)\\
 &=(2h-4m)X-(h+1)y-4m-2\\
 &=(2h-4m)Z+(h-4m-1)y-4m-2.
\end{aligned}
\]

At the least allowed value `h=2m+4`, write `Z=m+delta`.
The cone gives `y<3/2-delta`, so

\[
 \Delta_T>m+\frac52+(2m+5)\delta>0.
\]

Increasing `h` increases the margin by `(2Z+y)` per unit.  Hence the two
selectors are strict on the whole stated parameter range.

**Required terminology repair.**  The displayed `x_i >= 1` walls are useful
invariant lower walls; they are not necessary conditions for either selector.
Thus `\mathcal K_{m,h}` is an **explicit invariant selector cone**, not “the
exact selector cone” in the maximal or necessary-and-sufficient sense.  The
two displayed face margins are exact.  The manuscript must use this
distinction consistently.

### 3.3 Cone invariance

For `u'=Cu`, direct substitution gives

\[
\begin{aligned}
 u'_1&=h+4m+4+(4m+2)X,\\
 u'_i&=2h+4m+2+4mX+x_i \quad(2\le i\le r-1),\\
 u'_r&=h(2+2X-y).
\end{aligned}
\]

The middle lower walls follow from

\[
 u'_i-u'_1=h-2+x_i-2X>0.
\]

For the last lower wall,

\[
 u'_r-u'_1
 =h-4m-4+(2h-4m-2)Z+(h-4m-2)y.
\]

At `h=2m+4` this is strictly larger than
`m+3+(2m+4)delta`; it increases with `h`.

For the height wall, define

\[
 H=(h-1)u'_1-2\sum_{i=2}^r u'_i.
\]

Exact collection yields

\[
\begin{aligned}
 H={}&h^2-h-8m^2-8m-4\\
 &+\bigl((4m-2)h-8m^2-4m-4\bigr)X
 +2(h+1)y.
\end{aligned}
\]

At the least `h`, the minimum over the lower walls is

\[
 H\ge4m^2+6m+6>0,
\]

and every increment of `h` adds positive terms.  Therefore `C` maps the
cone strictly into itself.  These identities supply a short uniform proof;
no numerical fitting is needed.

### 3.4 Sharp seed threshold

The ordinary total-degree seed is `u_0=1`.  It lies in the strict cone exactly
when

\[
 m+1<\frac{h-1}{2},
\]

which, for integral parameters, is equivalent to

\[
 h\ge2m+4\quad\Longleftrightarrow\quad g\ge2r+1.
\]

At `g=2r`, the pure and mixed first-shear rows both have seed weight
`2r-1`, so `Delta_S=0`.  This proves sharpness for the seed and for the
strict pure-face selection mechanism.

It does **not** prove that the degree sequence is undefined, non-exponential,
or governed by no recurrence at `g=2r`; multiple top monomials may coexist.
The sharpness statement must retain the words “seed/selected face” or an
equivalent limitation.

### 3.5 Carry induction, no cancellation, and exact degree

At the seed, `A 1>1`.  If the full-step `q` vector is `u_n=C^n1`, the
carried `p` vector from the preceding step is strictly smaller than
`Au_n`, and the carried `q` vector is strictly smaller than `Cu_n`.
The strict selectors thus give phase by phase

\[
 v_{n+1}=Au_n,\qquad u_{n+1}=Cu_n.
\]

All coefficients in the gradients are positive integers.  Composition in
the positive support semiring expresses every selected coefficient as a sum
of products of positive integers.  Its image in a characteristic-zero field
is nonzero, so the selected leading support cannot cancel.  This argument
must not be transferred to positive characteristic or sign-changing
specializations.

The last `q` coordinate is visible and maximal.  In addition to
`u'_r>u'_1`, for a middle index one obtains

\[
 u'_r-u'_i=(2h-4m)Z+(h-4m)y-4m-2-x_i>0.
\]

At the least `h` the lower bound is `m+3` after using
`x_i<=1+delta` and `y<3/2-delta`; it increases with `h`.
Moreover `u'_r=h v_r` dominates `v_r`, `v_1`, and every other `v_i`.
Therefore the candidate exact formula is plausible and correctly indexed:

\[
 \deg(F^n)=e_r^{\mathsf T}C^n\mathbf1\qquad(n\ge0),
\]

and positivity of `C` gives

\[
 \lambda_1(F)=\rho(C).
\]

### 3.6 Three-dimensional quotient and exact characteristic factor

Let

\[
 U=\{x_1=x_r=0,\ \sum_{i=2}^{r-1}x_i=0\}.
\]

Then `dim U=r-3=m-1`.  Since a vector in `U` has total coordinate sum zero,

\[
 A|_U=-I,qquad B|_U=-I,qquad C|_U=I.
\]

The complementary symmetric subspace consists of vectors

\[
 (a,b,\ldots,b,c),
\]

with `m` equal middle entries.  In the coordinates `(a,b,c)`, the quotient
matrix is

\[
 Q_{m,h}=
 \begin{pmatrix}
 h+4m+4 & 4m^2+2m & 4m+2\\
 2h+4m+2 & 4m^2+1 & 4m\\
 2h & 2hm & h
 \end{pmatrix}.
\]

If the second quotient coordinate is instead the sum of the middle entries,
the similar matrix is

\[
 \widetilde Q_{m,h}=
 \begin{pmatrix}
 h+4m+4 & 4m+2 & 4m+2\\
 m(2h+4m+2) & 4m^2+1 & 4m^2\\
 2h & 2h & h
 \end{pmatrix}.
\]

Direct determinant expansion gives

\[
\begin{aligned}
 P_{m,h}(t)={}&t^3-(2h+4m^2+4m+5)t^2\\
 &+(h^2-8hm^2-8hm+2h+4)t\\
 &-h^2(2m+1)^2.
\end{aligned}
\]

Hence

\[
 \chi_C(t)=(t-1)^{r-3}P_{m,h}(t),
\]

and

\[
 P_{m,h}(1)=-4m(m+1)(h+1)^2\ne0.
\]

The unit eigenvalue therefore has algebraic and geometric multiplicity
exactly `r-3`; there is no hidden unit Jordan block.  Since `C` commutes with
all permutations of the middle coordinates, uniqueness of the positive
Perron vector places it in the symmetric quotient.  Thus `rho(C)` is the
largest positive root of `P_{m,h}`.

The seed also lies in the symmetric quotient.  Consequently the exact degree
sequence has a cubic constant-coefficient annihilator for every `r>=4`, even
though the full matrix size grows with `r`.  This is the strongest standalone
headline.

The word “cubic” describes the quotient characteristic equation or
annihilating recurrence.  It must **not** be upgraded to “algebraic degree
exactly three for every `(r,g)`”: `P_{m,h}` may factor or the minimal
annihilator may drop at special parameters unless a separate irreducibility
theorem is proved.

## 4. Portfolio collision audit: Papers 12–21

| Paper | Occupied object | Collision with Paper 22 | R1 disposition |
|---|---|---|---|
| 12 | period-three trace residues on an exceptional quartic Hénon fiber | no shared degree matrix, gradient-shear family, or spectral quotient | NONE |
| 13 | normalized primitive-cycle covers and monodromy in a degenerating Hénon family | periodic schemes rather than iterated coordinate degrees | NONE |
| 14 | four-step finite-rank torus escape for monomial Hénon maps | arithmetic survivor windows, not canonical gradient shears | NONE |
| 15 | low-period trace fibers of quartic generalized Hénon maps | trace/Jacobian quasi-finiteness, not degree growth | NONE |
| 16 | support-size finite-rank torus escape | sparse unit equations and transition bounds, not Perron matrices | NONE |
| 17 | torus-coset decay for shift-like recurrences | character geometry and survivor dimension, not this shear word | NONE |
| 18 | marked trace coordinates and scalar-boundary ramification | marked-cycle deformation theory, not support-degree propagation | NONE |
| 19 | maximal torus translates and a support-one GCD obstruction | translate moduli/arithmetic obstruction, not canonical shear dynamics | NONE |
| 20 | two-mode product-plus-pure-power Hamiltonian shears on `A^4` | same structural template at rank two; quadratic Perron factor | **DIRECT OWNED PREDECESSOR** |
| 21 | three-mode product-plus-pure-power Hamiltonian shears on `A^6` | same template at rank three; `m=1` gives exactly its matrix and cubic | **DIRECT OWNED PREDECESSOR / BASE CASE** |

The portfolio novelty is therefore the stable quotient and the new unit-mode
decomposition for variable `r>=4`, not the use of gradient shears, positive
supports, a two-phase matrix, a Perron root, or the first cubic example.

### Low-rank specialization check

- At `m=1`, `Q_{m,h}` is exactly Paper 21's `3 x 3` matrix and
  `P_{m,h}` is its displayed cubic on the common parameter domain.
- Formally at `m=0`,
  \[
  P_{0,h}(t)=(t-1)\bigl(t^2-(2h+4)t+h^2\bigr),
  \]
  and cancelling the spurious unit factor recovers Paper 20's quadratic
  Perron equation and `(sqrt(g)+1)^2` root.

These checks strengthen the algebra but increase the overlap penalty.

## 5. Paper 21 absorption and overlap rule

Mathematical absorption is safe: the quotient theorem specializes cleanly to
Paper 21 at `m=1`.  Portfolio handling is safe only under one of the following
exclusive policies:

1. **Preferred consolidation:** Paper 22 absorbs Paper 21 as a disclosed
   low-rank predecessor/base case, and Paper 21 is not advanced in parallel
   as an independent public manuscript.  Reuse is tracked and the new public
   theorem begins at `r>=4`.
2. **Separated successor:** Paper 21 remains an independently citable
   predecessor; Paper 22 cites/discloses it, proves only `r>=4` as new, avoids
   duplicated prose and proof presentation, and makes the `(r-3)` unit modes
   plus stable cubic quotient the unmistakable delta.  Concurrent submission
   would require full editorial disclosure and a stronger overlap review.

What is not safe is presenting Papers 21 and 22 as unrelated discoveries or
claiming Paper 22 as the first three-mode/cubic realization.  Paper 20 must
also appear in the lineage paragraph.

Paper 21 states `g>=8` and treats `g=7` as outside its chosen strict cone.
The present natural cone suggests a potentially sharper low-rank analysis,
but Paper 22 must not silently announce a Paper 21 `g=7` extension or
correction.  Such a claim requires its own authorized cross-paper proof and
integrity review.  Keeping the Paper 22 public range at `r>=4` avoids that
conflict.

## 6. Bounded public-primary-source collision screen

### 6.1 Search protocol and boundary

On 2026-08-24 UTC, the reviewer used read-only public search and opened
primary/authoritative records.  Query families were adversarially varied for
each core claim, including:

- `symplectic polynomial automorphism gradient shears degree growth spectral radius`,
  `canonical polynomial automorphism exact dynamical degree Hamiltonian shear`,
  and `symplectic shear dynamical degree`;
- `affine automorphism degree recurrence nonnegative matrix Perron Frobenius`,
  `spectral radius polynomial automorphism exact degree`, and
  `polynomial automorphism dynamical degree cubic Perron number`;
- `characteristic polynomial dynamical degree polynomial automorphism Perron`,
  `higher dimensional symplectic map algebraic degree growth`, and
  `polynomial automorphism higher dimension degree growth Perron matrix`;
- exact/support-oriented variants using `q_1^2 q_2^2`, `p_1^2 p_2^2`,
  `product potential pure power symplectic Hénon map`, and
  `coupled Hamiltonian shears polynomial potential degree growth`.

No searched primary record stated this exact product-plus-endpoint-pure-power
family, its threshold `g=2r+1`, or the factor
`(t-1)^(r-3) P_{m,h}`.  This is a bounded absence result, not an exhaustive
literature theorem or priority certificate.

### 6.2 Closest primary or authoritative records

| Source | Verified overlap | Why it is not a direct collision |
|---|---|---|
| J. Blanc and I. van Santen, *Dynamical degrees of affine-triangular automorphisms of affine spaces*, [arXiv:1912.01324](https://arxiv.org/abs/1912.01324) | arbitrary-dimensional affine-triangular degree calculations; weak Perron realization; nonnegative matrices | does not state this canonical gradient-shear family, its two exact face margins and invariant cone, the sharp `g/r` threshold, or the stable cubic quotient |
| E. Shao and X. Sun, *Dynamical degrees of affine-triangular automorphisms in dimension four*, [arXiv:2509.14584](https://arxiv.org/abs/2509.14584) | recent algebraic-degree bounds and explicit dimension-four context | dimension four and a larger affine-triangular class; no variable-r product potential or unit-mode collapse |
| J. Déserti, *Degree growth of polynomial automorphisms and birational maps: some examples*, [arXiv:1602.04642](https://arxiv.org/abs/1602.04642) | higher-dimensional degree-growth phenomena | polynomial-growth examples and broad landscape, not this exponential exact recurrence |
| N.-B. Dang and C. Favre, *Spectral interpretations of dynamical degrees and applications*, [Annals DOI](https://doi.org/10.4007/annals.2021.194.1.5) | general spectral language for dynamical degrees | no finite support selector or displayed Hamiltonian-shear formula |
| G. Rangarajan, *Polynomial map symplectic algorithm*, [arXiv:physics/0212098](https://arxiv.org/abs/physics/0212098) | polynomial symplectic-map factorization by elementary maps | computational integration architecture, not algebraic degree iteration or the candidate spectrum |
| N. Burby et al., *Approximation of nearly-periodic symplectic maps via structure-preserving neural networks*, [Scientific Reports 2023](https://www.nature.com/articles/s41598-023-34862-w) | arbitrary-dimensional Hénon-like maps generated by gradients of potentials | approximation/learning theory, not the exact polynomial family, threshold, degree sequence, or quotient factorization |
| K. Fujioka, R. Kogawa, J. Li, and A. Shudo, *Coupled Hénon Map, Part I*, [arXiv:2303.05769](https://arxiv.org/abs/2303.05769) | coupled four-dimensional symplectic Hénon dynamics | horseshoes and hyperbolicity rather than exact algebraic degree propagation |

Blanc–van Santen is the strongest novelty-risk citation because it already
establishes broad Perron realizability and arbitrary-dimensional matrix
methods.  Therefore Paper 22 may claim a new explicit family theorem only;
it may not claim the first realization of these Perron numbers or the first
use of a matrix spectral radius in polynomial-automorphism degree growth.

## 7. Standalone 22–30 page feasibility

A non-padded 24–28 page article is feasible:

| Section | Target pages | Required content |
|---|---:|---|
| Introduction and exact predecessor positioning | 2.5–3 | stable-rank question, Papers 20–21 disclosure, bounded public literature |
| Family, inverses, symplectic blocks, support ledger | 2.5–3 | all gradient rows, definitions of `A`, `B`, `C` |
| Two selectors and sharp threshold | 3–4 | exact margins, `g=2r` seed tie, terminology restraint |
| Cone invariance and carry induction | 4–5 | all lower/height walls, old-term domination, positive-support lemma |
| Visibility and exact degree sequence | 2.5–3 | `e_r` maximum, exact recurrence, Perron limit |
| Symmetry reduction and cubic collapse | 4–5 | `U`, quotient matrix, determinant, `P(1)`, semisimplicity |
| Low-rank lineage and limitations | 2–3 | `m=0,1` specializations, absorption policy, anti-claims |
| Optional algebra appendix | 1.5–2 | determinant expansion or scalar cubic recurrence audit |

No numerical experiment, plot, external dataset, or generic classification
claim is needed.  If the source spends most of its pages repeating Paper 21's
three-mode proof rather than proving the rank-stable quotient, standalone value
falls below the gate.

## 8. Allowed headline claims

Subject to a complete proof, the following are appropriately bounded:

1. For the displayed family with `r>=4` and `g>=2r+1`, a strict explicit
   invariant selector cone gives an exact two-phase degree recurrence.
2. The last coordinate realizes the exact total degree and
   `lambda_1(F)=rho(C)` in characteristic zero.
3. The seed/strict-pure-face threshold is sharp at `g=2r`.
4. The middle-difference space has dimension `r-3`, `C` acts there as the
   identity, and the Perron dynamics lie in a three-dimensional quotient.
5. The full characteristic polynomial factors as
   `(t-1)^(r-3) P_{m,h}(t)`, with
   `P_{m,h}(1)=-4m(m+1)(h+1)^2`.
6. The exact degree sequence has a cubic annihilating recurrence independent
   of the ambient rank, with coefficients depending explicitly on `(r,g)`.

## 9. Mandatory anti-claims and STOP conditions

The paper must not claim:

- that `mathcal K_{m,h}` is the maximal or necessary-and-sufficient selector
  region; call it an explicit invariant selector cone;
- that the theorem classifies arbitrary polynomial, symplectic, canonical,
  triangular, or Hamiltonian automorphisms;
- that the Perron root always has algebraic degree exactly three;
- that this is the first Perron realization, first matrix-degree method, first
  Hamiltonian shear construction, or first cubic example;
- that Paper 21 is unrelated, or that its theorem is newly reproved here;
- that failure of the strict seed selector at `g=2r` determines the actual
  degree dynamics at or below the boundary;
- validity in positive characteristic or under coefficient specializations
  that invalidate the positive-support argument;
- equality with topological, metric, arithmetic, or measure-theoretic entropy;
- genericity, integrability, non-conjugacy to products, periodic-point
  classification, or a universal Newton-fan theorem;
- a Paper 21 `g=7` correction or extension without a separate authorized
  cross-paper review;
- global literature priority from the bounded source search.

The candidate must STOP or return to repair if any of the following occurs:

1. a selector or carry term ties inside the stated open cone;
2. the source omits the second-phase margin `Delta_T` or treats `B` as acting
   directly on `u` instead of `Au`;
3. the cone height inequality is replaced by unverified numerical samples;
4. `e_r` is not proved to dominate every `q` and `p` coordinate;
5. the positive-support/no-cancellation argument is broadened beyond
   characteristic zero;
6. the quotient matrix does not match its stated coordinate convention;
7. the factor `(t-1)^(r-3)` is inferred only from sample determinants rather
   than from the invariant-space decomposition;
8. Papers 20–21 are omitted from the direct-collision and lineage sections;
9. Paper 21 and Paper 22 are advanced in parallel without explicit overlap
   governance.

## 10. Final gate decision

The independent algebraic audit supports the exact recurrence, threshold,
visibility, invariant unit space, quotient cubic, and `P(1)` identity.  The
bounded public-primary-source search found strong contextual neighbors but no
direct statement of the candidate conjunction.  Portfolio novelty survives
only because the new theorem is the rank-stable cubic collapse for `r>=4`,
not the underlying low-rank shear mechanism already occupied by Papers 20–21.

The authorized next stage is therefore **proof-first Paper 22 source design
under the locks in this review**.  This review authorizes no project build,
release candidate, publication claim, Paper 21 status mutation, or external
communication.

PAPER22_CANDIDATE_GATE_PASS_R1
