# Paper 22 — Final Proof-First Proposal

## Title

**Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian Product Shears:
Sharp Selector Thresholds in Arbitrary Mode Number**

## Lifecycle status

Source-design authoring only. The author-level derivation has been written,
but every artifact and formula remains pending independent
source-design review. No downstream authority follows from this proposal.

## Headline theorem

Let $K$ be a field of characteristic zero, let $r\ge4$, and let
$g\ge2r+1$. Define

$$
V_{r,g}(q)=\prod_{i=1}^r q_i^2+q_1^g,\qquad
W_{r,g}(p)=\prod_{i=1}^r p_i^2+p_r^g,
$$

and let $F_{r,g}=T\circ S$ be the corresponding pair of exact-gradient
shears. Put $h=g-1$, $m=r-2$, form the literal phase matrices $A$ and $B$
from the gradient supports, and put $C=BA$.

The proposed theorem proves:

1. polynomial invertibility and preservation of the standard symplectic form;
2. strict selection and invariance on

   $$
   \mathcal K_{r,g}
   =\left\{u>0:
   \frac{u_i}{u_1}\ge1,
   \sum_{i=2}^r\frac{u_i}{u_1}<\frac{g-2}{2}\right\};
   $$

3. exact phase recurrence and leading-form survival;
4. strict last-coordinate visibility for $n\ge1$ and

   $$
   \deg(F_{r,g}^n)=e_r^{\mathsf T}C^n\mathbf1;
   $$

5. $\lambda_1(F_{r,g})=\rho(C)$;
6. an $(r-3)$-dimensional identity eigenspace and a three-dimensional
   complementary matrix

   $$
   Q_{m,h}=
   \begin{pmatrix}
   h+4m+4 & 2m(2m+1) & 2(2m+1)\\
   2h+4m+2 & 4m^2+1 & 4m\\
   2h & 2mh & h
   \end{pmatrix};
   $$

7. the exact factorization

   $$
   \chi_C(t)=(t-1)^{r-3}P_{m,h}(t),
   $$

   with

   $$
   \begin{aligned}
   P_{m,h}(t)
   ={}&t^3-(2h+4m^2+4m+5)t^2\\
   &+(h^2-8hm(m+1)+2h+4)t
   -h^2(2m+1)^2;
   \end{aligned}
   $$

8. $P_{m,h}(1)=-4m(m+1)(h+1)^2\ne0$, so the unit eigenvalue has exact
   multiplicity $r-3$;
9. a cubic annihilating recurrence for the exact degree sequence;
10. sharpness of $g\ge2r+1$ for the stated seed and strict selected face; and
11. the same degree theorem for four arbitrary nonzero coefficients on the
    fixed supports.

The proposal does not assert universal irreducibility or algebraic degree
exactly three.

## Proof architecture

1. **Geometry before degree.** Expand gradients, inverses, and symplectic
   block identities.
2. **Supports before matrices.** Bind every row of $A$ and $B$ to a literal
   derivative monomial and multiply $C=BA$.
3. **Selectors before recurrence.** Prove the first and second competitive
   margins on the full cone.
4. **Every cone wall.** Prove middle lower walls, last lower wall, and the
   height wall, including the least parameters.
5. **Carries before exactness.** Use $C-I>0$ and the phase-labelled induction
   to dominate old coordinates.
6. **Leading forms before equality.** Use the polynomial-domain argument,
   including the four-coefficient corollary.
7. **Visibility before Perron.** Prove $q_r$ exceeds every $q$ and $p$
   coordinate for $n\ge1$.
8. **Invariant decomposition before determinant.** Split $K^r=U\oplus E$,
   fix the quotient coordinate convention, and then compute the cubic.
9. **Boundaries after the theorem.** Record $g=2r$, $n=0$, coefficient
   failure, positive characteristic, and the $r=3$ predecessor check.

This order prevents a formal matrix or a sampled determinant from being
mistaken for an exact degree theorem.

## Planned 24–28 content pages

| Section | Planned pages | Non-negotiable content |
|---|---:|---|
| 1. Introduction and stable-rank question | 2.5–3 | exact delta, Papers 20–21, bounded literature |
| 2. Family and symplectic geometry | 3–3.5 | coordinates, gradients, inverses, Hessian blocks |
| 3. Support rows and two selectors | 3–3.5 | exact $A,B$, both margins, seed threshold |
| 4. Strict cone invariance | 4–4.5 | every lower wall and height form |
| 5. Carry and leading-form induction | 3.5–4 | both phases and coefficient corollary |
| 6. Exact degree and Perron visibility | 2.5–3 | $e_r$, $n=0$ boundary, PF |
| 7. Unit space and cubic collapse | 4–4.5 | $U\oplus E$, $Q$, $P$, $P(1)$, recurrence |
| 8. Boundaries, lineage, limitations | 1.5–2 | $g=2r$, $r=3$, anti-claims |

The content range is credible without experiments, figures, governance text,
or duplicated Paper 21 exposition.

## Citation and novelty boundary

External citations support only contextual statements about affine-triangular
degree growth, broader higher-dimensional examples, spectral language, and
neighboring symplectic constructions. All theorem-critical claims are proved
internally. The bounded search supports only a no-direct-collision statement,
not priority.

Paper 20 is the rank-two predecessor and Paper 21 the rank-three predecessor.
Paper 22 begins at $r\ge4$. The source must foreground the stable quotient,
not present the family construction or cubic base case as new.

## Hard exclusions

No maximal cone, arbitrary-support theorem, classification, genericity,
entropy, periodic-point theory, integrability, arithmetic dynamics,
non-conjugacy, positive characteristic, universal cubic irreducibility,
rank-three novelty, global threshold, or literature-priority claim is in
scope.

## Permission boundary

Authorized at this stage:

- exactly the ten UTF-8/LF source-design Markdown files;
- read-only validation of their inventory, bytes, line endings, and hashes;
- a later fresh independent review commissioned by the parent.

Not authorized:

- source lock, paper plan, publication governance, manuscript, bibliography,
  code, scientific experiment, CAS certificate, build, PDF, release object,
  upload, submission, repository push, external message, identity disclosure,
  Paper 23, or any other external effect.

The proposal stops after the source-design author inventory is frozen.
