# Paper 22 — Research Question and Scope Lock

## Working title

**Cubic Spectral Collapse for Endpoint-Spiked Hamiltonian Product Shears:
Sharp Selector Thresholds in Arbitrary Mode Number**

## Principal research question

Let $K$ be a characteristic-zero field, $r\ge4$, and $g\ge2r+1$. For

$$
V_{r,g}(q)=\prod_{i=1}^r q_i^2+q_1^g,\qquad
W_{r,g}(p)=\prod_{i=1}^r p_i^2+p_r^g,
$$

and

$$
F_{r,g}
=(q+\nabla W_{r,g}(p+\nabla V_{r,g}(q)),
\ p+\nabla V_{r,g}(q)),
$$

can the ordinary degree of every iterate be proved exactly from one explicit
selector cone, and can the apparent $r$-dimensional degree system be shown to
have only three nontrivial spectral dimensions?

The sought answer is family-specific:

$$
\deg(F_{r,g}^n)=e_r^{\mathsf T}C_{r,g}^n\mathbf1,
$$

with strict last-coordinate visibility for $n\ge1$, together with

$$
\chi_{C_{r,g}}(t)=(t-1)^{r-3}P_{r-2,g-1}(t).
$$

The word “cubic” refers to the complementary characteristic factor and an
annihilating recurrence. It does not assert algebraic degree exactly three
for every Perron root.

## Formal input/output contract

**Input**

- a field $K$ of characteristic zero;
- integers $r\ge4$ and $g\ge2r+1$;
- the exact two displayed potentials and the shear order $T\circ S$;
- the ordinary-degree seed $\mathbf1$.

**Output**

- explicit polynomial inverses and a symplecticity proof;
- literal gradient support rows and exact matrices $A$, $B$, and $C=BA$;
- an explicit sufficient invariant selector cone;
- phase-labelled support and leading-form induction;
- the exact degree of every iterate and the first dynamical degree;
- the invariant unit space, three-dimensional complement, cubic factor, and
  exact multiplicity of the unit eigenvalue;
- the seed/selected-face boundary at $g=2r$; and
- a sign-safe corollary for four nonzero coefficients on the fixed supports.

A finite computation, numerical spectral approximation, CAS transcript, or
sample of ranks is not an admissible substitute.

## Exact subquestions

1. Which derivative rows compete, and why are there exactly two selector
   comparisons?
2. Why does the cone use
   $\sigma=\sum_{i=2}^r u_i/u_1$, excluding the normalized first coordinate?
3. Do both selectors remain strict on all allowed lower faces and as the open
   height boundary is approached?
4. Does $C$ map every cone wall strictly inward at $r=4$ and
   $g=2r+1$, the least allowed values?
5. Are every old $p$- and $q$-coordinate and every possible leading-form
   cancellation handled phase by phase?
6. Why does $e_r$ see the total degree for $n\ge1$, and what changes at
   $n=0$?
7. Why is the eigenvalue $1$ present with exact multiplicity $r-3$?
8. Which three coordinates define the complementary matrix, and what is the
   precise coordinate convention?
9. Is the cubic an annihilator, a minimal polynomial, or merely a containing
   equation at special parameters?
10. Which conclusions survive arbitrary nonzero coefficients, and why do
    added supports or positive characteristic fall outside the proof?

## Falsification tests

The proposal fails as stated if:

- $\sigma$ contains $x_1$;
- either phase selector ties inside the open cone;
- an allowed lower face maps to or below its output lower face;
- the height form is nonpositive for an allowed parameter;
- a carried coordinate meets the fresh selected degree;
- an allowed nonzero coefficient specialization kills a unique leading form;
- $q_r$ fails to dominate one coordinate for $n\ge1$;
- the quotient matrix changes under its declared coordinate convention;
- $P(1)$ vanishes in the allowed range;
- the cubic claim is promoted to universal irreducibility; or
- the $r=3$ specialization is presented as new.

## In-scope boundaries

- Exact fixed family over every characteristic-zero field.
- Every integer $r\ge4$ and $g\ge2r+1$.
- Ordinary total degree, exact degree sequences, and first dynamical degree.
- Four arbitrary nonzero coefficients on the same two supports.
- Bounded primary-source context and explicit local predecessor disclosure.
- A credible later proof-first article of 22–30 substantive content pages.

## Out-of-scope boundaries

- Positive characteristic, added supports, arbitrary potentials, arbitrary
  shear words, or a Newton-fan classification.
- Claims about topological, metric, arithmetic, or measure-theoretic entropy.
- Genericity, integrability, invariant varieties, periodic points, traces,
  multipliers, torus translates, or arithmetic orbits.
- Non-conjugacy to every product or reduction.
- Global optimality at the parameter boundary.
- First realization or literature-priority claims.
- A new theorem or correction for Paper 20 or Paper 21.
- Manuscript, bibliography, source lock, build, PDF, release, submission,
  public hosting, external message, or identity disclosure at this stage.

## Predecessor and permission lock

Paper 20 is the rank-two direct predecessor and Paper 21 is the rank-three
direct predecessor. Paper 22 is a separated successor whose new range begins
at $r\ge4$. The project may not present these three local objects as unrelated
discoveries.

The only current artifact is the ten-file source-design package. A distinct
reviewer must assess it before any source lock or downstream lifecycle action.
