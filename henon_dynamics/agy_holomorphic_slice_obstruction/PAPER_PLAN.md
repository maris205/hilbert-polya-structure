# Paper plan

**Working title:** Scalar AGY Determinants Survive Infinite Oscillator Twists

**One-sentence contribution:** A fixed positive Rauzy prefix gives one
complex domain on which the countable scalar AGY transfer operator is trace
class with algebraic Perron trace atoms, whereas the unsmoothed metaplectic
twist is noncompact on the same domain.

**Type:** mathematical theory plus exact reproducibility note.

**Format:** self-contained research article; approximately 10--12 pages of
main text plus proof/reproducibility appendix.

**Date:** 2026-08-10.

## Claims--evidence matrix

| Claim | Evidence | Status | Paper location |
|---|---|---|---|
| All countable AGY inverse branches share a complex compact-containment domain | Fixed-positive-prefix factorization and self-contained complex-cone proof | Proved; two independent theorem audits | Section 2 |
| Scalar weights are holomorphic and summable on that domain | Right-half-plane principal log, uniform fixed-point comparison, C25 real branch sum | Proved | Section 3 |
| The scalar Bergman transfer is trace class | Verified Bandtlow--Jenkinson map-weight hypotheses; complex dimension three | Proved | Section 3 |
| Every chronological word trace is `lambda^(-(s+1))/chi'(lambda)` | Exact normalizer telescoping and projective quotient derivative | Proved; exact examples replayed | Section 4 |
| The same-domain oscillator twist is bounded but noncompact | Uniform Bergman evaluation, C26 evaluation slice, C24 atom theorem, C25 injectivity | Proved | Section 5 |
| A concrete branch gives a rational positive essential-norm bound | Independent reconstruction of the length-128 matrix, point, roof, and Jacobian | Verified computationally before release | Section 6 |
| No Hilbert--Pólya construction follows | Route-A criteria: no self-adjoint bridge or zero match | Negative assessment | Section 7 |

## Known weaknesses to state early

- The common domain is constructible but nonunique; the theorem does not
  optimize its Bergman constants.
- The algebraic trace atom is arithmetic structure, not an automorphic or
  prime-orbit identification.
- The metaplectic conclusion is about ordinary compact/nuclear determinant
  theory, not every possible flat or distributional trace.
- C24 and C25 are substantial inputs; the paper must distinguish inherited
  results from the new C26 application.

## Structure

### Abstract (180--220 words)

- Open with the same-domain dichotomy, not general RH motivation.
- State the fixed-positive-prefix complex-domain mechanism.
- Give the exact Perron trace atom.
- State the essential-norm lower bound and the full half-plane.
- End with the finite-Weil pivot and the Route-A limitation.

### 1. Introduction (1.25 pages)

- **Hook:** scalar analytic compactness does not automatically compactify an
  infinite unitary fibre.
- **Gap:** C25's branch localizer cannot exist in a holomorphic space.
- **Approach:** complexify through the fixed positive prefix, then slice the
  whole operator by constants and evaluation.
- **Contributions:** common complex domain; scalar trace/Perron formula;
  same-domain infinite-fibre obstruction; exact certificate.
- **Result preview:** display the two boxed formulas side by side.
- **Front-matter artifact:** Table 1 comparing scalar versus oscillator
  spaces, trace status, periodic atom, and failure mechanism.

### 2. Positive-prefix complexification (1.75 pages)

- Define `H_C` and projective maps, then derive the fixed-prefix
  factorization from the published AGY branch grammar and Rauzy chronology.
- Prove boundedness and connectedness of the canonical complex cone.
- Prove nonnegative preservation and strict-positive interior mapping.
- Construct `Omega` and state why the natural domain itself is too small.
- Keep the real-Hilbert-contraction counterexample/scope note concise.

### 3. Scalar holomorphic transfer operator (1.5 pages)

- Establish the common principal logarithm.
- Prove complex `ell^1` weight summability and local holomorphy in `s`.
- Invoke the verified Bergman exponential-class theorem.
- Define the ordinary Fredholm determinant.
- State explicitly that invariant-density normalization is excluded.

### 4. Perron arithmetic of chronological trace atoms (1.5 pages)

- Freeze the later-on-left word convention.
- Prove weight telescoping.
- Identify the derivative with the quotient action.
- Derive `lambda^(-(s+1))/chi'(lambda)`.
- Explain precisely why `lambda` is an algebraic unit and why
  `chi'(lambda)` is not automatically a field discriminant.
- Include a small exact table for the source branch, the two-return
  contravariant-order sentinel, and the three-return spectral sentinel.

### 5. Infinite oscillator obstruction (1.75 pages)

- State the general evaluation-slice theorem and proof.
- Cite C24 atomic separation and C25 all-length injectivity as inputs.
- Prove absolute boundedness on vector Bergman space.
- State the same-domain scalar/twisted dichotomy.
- Discuss Hardy, Bergman, `H^infinity`, RKHS, and the anisotropic boundary
  through explicit assumptions rather than blanket claims.

### 6. Exact certificate and independent replay (0.75 pages)

- Present `gamma_*`, exact matrix/point/normalizer/Jacobian.
- Give the one-branch lower bound.
- Report positive-prefix margin and Birkhoff contraction sentinel.
- Report producer/checker, mutations, and hashes.
- Make clear which results are infinite theorems and which are finite
  implementation checks.

### 7. Hilbert--Pólya assessment and next door (0.75 pages)

- Route-A table with evidence for A1--A4.
- Explain why scalar success does not rescue the oscillator target.
- Separate ordinary trace from Weil distribution character.
- Specify the finite Weil `p^2` fibre experiment as the next large gate.

### 8. Conclusion (0.4 pages)

- Restate the sharp scalar/fibre separation.
- Highlight the algebraic trace atom as reusable positive infrastructure.
- Close the base-space lineage and name the finite-fibre pivot.

### Appendix

- Full evaluation-slice and tensor-slice proofs.
- Complex-cone details and the counterexample to automatic
  complexification of real contraction.
- Exact arithmetic tables and reproduction commands.
- AI-assistance and verification disclosure.

## Table and figure plan

| ID | Type | Content | Evidence source | Priority |
|---|---|---|---|---|
| Table 1 | Hero comparison | Scalar `A^2(Omega)` versus vector `A^2(Omega;L^2(R^2))`: boundedness, compactness, trace, periodic atom, determinant | Main theorems | High |
| Table 2 | Exact arithmetic | Source branch, cyclic two-return bookkeeping sentinel, and noncyclic three-return spectral sentinel | C26 certificate | High |
| Table 3 | Route-A | A1--A4 status, strongest evidence, decisive failure | Route-A YAML | High |

A decorative diagram is unnecessary.  Table 1 lets a skim reader see the
same-domain contrast without introducing a second visual vocabulary.

## Citation plan

- Introduction: AGY; Bandtlow--Jenkinson; Bonet et al.; HCS-C24/C25.
- Section 2: published AGY article as factorization authority.
- Section 3: both Bandtlow--Jenkinson papers.
- Section 5: Thomas for the character boundary; Hilgert for oscillator
  semigroup/Bargmann scope.
- Section 7: Gurevich--Hadani for the finite Weil pivot.

Every entry must be reused from a verified local bibliography or retrieved
from the DOI/article record.  Only cited entries belong in `references.bib`.

## Independent outline review

Two independent theorem audits challenged the complex-domain step.  Both
returned GO only after replacing the informal “real contraction
complexifies” argument by the fixed-positive-prefix complex-cone proof.
Their required fixes are incorporated:

- enlarge the natural complex domain;
- keep complex dimension three distinct from Jacobian exponent four;
- assert only local uniformity in `s` on compact subsets;
- exclude holomorphic invariant-density normalization;
- distinguish ordinary determinant failure from generalized traces;
- identify C24/C25 inputs rather than relabeling them as C26 results.

## Release checklist

- [x] Exact producer and independent checker pass.
- [x] All registered mutations are caught.
- [x] Claims and result JSON agree.
- [x] LaTeX paper compiles with zero undefined citations/references.
- [x] Reverse-outline test passes.
- [x] No unfinished marker or unsupported novelty claim remains.
- [x] Parent candidate and obstruction registries are updated.

Commit, annotated tag, and SSH push are recorded in the release handoff.
