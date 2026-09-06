# C409 paper plan

Working title: **Active fibres and natural boundaries in wild finite-adelic
dynamics**.

One-sentence contribution: an exact finite active-fibre test decides whether
periodic finite-adelic radial coefficients with arbitrary complex phases
produce a rational series or a meromorphic natural boundary, and proves the
nonhyperbolic wild FAD application through an actual product system.

Format: anonymous English mathematical article, 11pt, one-inch margins; no
chosen venue or fixed page budget. Complete proofs determine length. This
implements the parent BATCH_PLAN, frozen after independent outline review.
The R1 refinement is incorporated: the phase sum and prime set are finite,
all phases have modulus one, and the periodic exponents are nonnegative real
numbers. Body drafting is authorized by the parent's freeze notice.

## Fixed inputs and editorial scope

All source paths below refer to the frozen research tree
../../../research_c409_c413/ relative to this directory.

- arithmetic/PROOF_PACKAGE.md: Theorem 1 and its full seven-step proof,
  FAD corollary and all limiting/positivity arguments.
- arithmetic/REALIZED_EXAMPLE.md: the Salem companion matrix, actual additive
  system, product counts and embedding obstruction.
- arithmetic/POSTCLASSICAL_DELTA.md: the no-wild BHN deduction and failure
  of its sublinear-height hypothesis on the wild example.
- arithmetic/SOURCE_AUDIT.md and REVIEW_ARITHMETIC_ROOT.md:
  inspected-version boundaries and independent proof/substance checks.

These documents are writing inputs, not experiments to re-run or files to edit.
Workflow/admission language stays in this plan and provenance notes, not in the
mathematical exposition.

## Claims–evidence matrix

| Paper claim | Frozen proof evidence | Ownership deduction | Location |
| --- | --- | --- | --- |
| Exact rational versus natural-boundary criterion for all finite prime sets, periodic nonnegative real exponents and complex phase weights | PROOF_PACKAGE, Theorem 1, Steps 1–7 | Fourier ball expansion and atomic radial limits are classical; the retained step is the exact active fibre and its dense genuine conductor grids after aggregation | §§2–4 |
| Meromorphic continuation fails at every unit-circle point in the active branch | Steps 4–6, finite total variation and dense nonzero actual atoms | No generic “sum of natural-boundary functions” principle is asserted | §4 |
| Distorted positive-counting-entropy FAD systems have the entropy circle as a natural boundary, without unique dominance or integral wild exponents | Corollary 2, positivity, CRT and analytic error argument | The no-wild conclusion is already a deduction from BHN; classical FAD framework and root-rational branch are credited | §5 |
| The remaining wild conclusion applies to a genuinely nonhyperbolic self-map | REALIZED_EXAMPLE, E1–E3 and three dominant phases | Toral/additive formulas and a mixed set product are not new constructions; no mixed-characteristic algebraic-group realization is claimed | §6 |
| The example lies outside the inspected BHN and all-embeddings sufficient hypotheses | POSTCLASSICAL_DELTA §2; REALIZED_EXAMPLE §4 | A failed hypothesis is a scope comparison, not a priority certificate | §§5–6 |

## Section plan and proof placement

The manuscript will contain an abstract and seven numbered sections, each in
its own actual section file. No unnecessary appendix or figure is planned.

### Abstract

Start with the exact dichotomy and explain phase cancellation as the issue.
State that only finitely many primes and periodic data are allowed, but phase
weights may be complex and exponents real and nonnegative. Preview the dense
actual atomic measure, the masked rational control, and the wild nonhyperbolic
application. Do not call the algebraic no-wild result new. Approximately
170–220 words, without citations or unexplained FAD abbreviation.

### 1. Introduction and position among natural-boundary results

Open with the question of whether p-adic distortion survives cancellation
between dominant phases. Describe the finite test and its strongest conclusion.
Then distinguish algebraic dynamics, almost quasi-polynomial perturbations,
and Fourier/Cauchy mechanisms. Make the BHN no-wild deduction visible here,
not only in the final limitations.

Use one short assumptions/conclusions table comparing the inspected BCH
unique-dominance theorem, the BHN no-wild scope, and the present active-fibre
statement. Citations: BCH, BHN, BMW, BC, BGNS, Knill–Lesieutre and
Cornelissen–Park as their specific roles arise. No “first ever” claim.
State once that theorem locators refer to the inspected public versions;
unavailable final versions are not certified unchanged.

### 2. Radial data, phase classes and the main theorem

Define the continuous radial kernel at zero, finite S, periodic r/s/t data,
unit phases, torsion-ratio classes, common period W and grouped b_C.
State AF with all three conditions and the convention when p does not divide W.
State both rational/meromorphic-natural-boundary alternatives, the finite
atomic representation and the exact radial mass limit. Explain invariance
under increasing the common period. Include the phase-mask example
F(z)=2z/(1-z²) immediately after the theorem.

### 3. Fourier representation on the compatible adelic group

Prove the CRT description of the diagonal closure D and injectivity of
character evaluation. Prove the telescoping ball expansion at every point,
its absolute Fourier norm bound, restriction/collection, and identification
with Haar coefficients. Do not invoke a false absolute-Fourier theorem for
arbitrary continuous functions.

### 4. Active fibres, conductor grids and the dichotomy

Prove unbounded actual p-conductor from a nonconstant zero-residue fibre.
Prove unit invariance and the full equal-mass root grids. Aggregate the
actual phase measure and rule out both within- and between-class collisions.
Derive the radial mass limit by dominated convergence and exclude meromorphic
caps by discreteness of poles. Finish with the explicit rational expression
when AF fails. Every argument is in the body; no external proof package is
needed by a reader.

### 5. Application to finite-adelically distorted systems

Define confined system, ordinary fixed-count series, exponential dynamical
zeta, gcd sequences and the own-prime-coprime condition. State the FAD corollary.
Give the dominant determinant expansion with positive leading phase sum,
exclude root-of-unity eigenvalues by realizability, force AF by CRT,
control the subdominant analytic error, and transfer the boundary through
zeta's logarithmic derivative.

Explicitly present the no-wild BHN deduction with rational/height,
density-one local constancy and stability checks. Identify the wild
sublinear-height failure rather than treating all nonhyperbolic cases as new.
Keep the classical root-rational classification separate from the abstract
rationality theorem.

### 6. A realized nonhyperbolic wild example

Give the quartic companion matrix, irreducibility modulo two, reciprocal-root
geometry via Y=X+X^{-1}, and toral fixed-count formula. Derive the additive
fixed-count formula from the least Frobenius exponent. Form the actual set
product and display its three dominant phases and boundary radius
(p lambda)^{-1}. State the counting-entropy meaning, not an unproved
topological entropy identity on the noncompact/mixed set.

Show the BHN height obstruction and the failed all-embeddings unit-disc
condition. The example illustrates the theorem, not a second contribution.

### 7. Conclusions and scope

Restate precisely what the finite criterion detects. Retain finite S,
periodicity, nonnegative exponents, actual phase aggregation, public-version
limits and distinction between abstract coefficient series and realized zeta.
Do not add a prime-length/Euler-factor, target-zero, or Hilbert–Pólya claim.
No speculative new theorem or unrun experiment.

## Visual and citation plan

One comparison table in §1 is useful because three hypothesis classes have
different source ownership. No hero image, numerical plot, decorative
architecture diagram or new data-generation step is needed.
The complete mathematical example supplies the concrete comparison.

references.bib will contain only the seven intended cited works; metadata is
verified against the frozen audit and current primary metadata records.
Exact public versions and missing final-text comparisons are recorded in
CITATION_METADATA.md and reflected in relevant bibliography notes.

## Review, build and handoff

The current-team non-author outline review was coordinated by root and the
outline has been frozen. Each full manuscript then receives a
new non-author review; old proof review does not substitute for draft review.

Author checks may inspect LaTeX references, citations, notation and compile
the new manuscript. No frozen mathematical checks are re-run. Root owns formal
Route-A evaluation, final two-directory deterministic builds, all-page visual
inspection, global ledgers, registries and Git.
