# Paper Plan: Diagonal-Translation Rigidity and Phase Reciprocity

## Frozen article identity

- **Type:** anonymous, proof-first mathematical theory article.
- **Working title:** *Diagonal-Translation Rigidity and Phase Reciprocity in Positive Newton-Fan Hamiltonian Shears*.
- **One-sentence contribution:** For separated Hamiltonian shears with finite nonempty collected supports E_V,E_W contained in Z_{>=2}^r (r >= 3), every certified strict branch has an exact all-ones translation, at most d_V+d_W-2 selector changes, and a stationary affine (lambda,mu) tail; reflected inverse reciprocity is characterized edgewise on observable spans, while the lower-ideal result is only a local one-edge statement.
- **Content budget:** 25.7 pages through the end of the conclusion; references and any appendix are excluded.  The target is deliberately proof-sized (22--30 pages), not a conference page-limit claim.
- **Body structure:** eight numbered sections plus an unnumbered abstract.  The future source trio will use the section names listed below, but no section file is authorized at this gate.
- **Source boundary:** the source-design input subset has eleven files; SOURCE_LOCK.md is the twelfth project file, and the locked post-plan universe is distinguished from the 24-row pre-lock aggregate.  The status ledger is excluded from every self-excluding aggregate.

## Claims--evidence and kill conditions

| ID | Claim to state | Internal evidence | Planned section | Kill condition |
|---|---|---|---|---|
| C1 | K is characteristic zero; r >= 3; E_V,E_W are finite, nonempty, collected, and every exponent is in Z_{>=2}^r. | RESEARCH_QUESTION, PROOF_PACKAGE §§1 and 14 | 3 | Empty/uncollected support, zero coefficient, coordinate below 2, positive characteristic, or r < 3 |
| C2 | Positive integer pair seeds with disjoint algebraically independent leading blocks realize each declared edge and define U_e,V_e. | PROOF_PACKAGE §§1, 2, 9, 14; exact fixture seeds | 3 | No integer seed, failed carry, empty lattice cell, or unsupported span assertion |
| C3 | A positive exposed face has a nonzero grouped Hessian determinant for every nonzero coefficient choice in the class. | PROOF_PACKAGE §4 and determinant witness | 4 | Zero/unit exponent, characteristic cancellation, or invalid secondary minimizer argument |
| C4 | Face-gradient components are algebraically independent and remain visible after injective substitution. | PROOF_PACKAGE §5 and Jacobian criterion | 4 | Hidden coefficient cancellation, noninjective substitution, or missing fresh block |
| C5 | Forward and reflected-inverse leading forms survive in the stated phase order. | PROOF_PACKAGE §§2--5 and strict carries | 4 | Wrong phase order/sign, uncollected term, or non-strict carry |
| C6 | The exposed degree maps are A_alpha = 1 alpha^T - I and B_beta = 1 beta^T - I. | Componentwise gradient calculation in §3 of PROOF_PACKAGE | 3--4 | Tie or failed selector/target certificate |
| C7 | Each certified two-phase step is u' = u + delta 1 with delta > 0 and integral on integer seeds. | PROOF_PACKAGE §6 | 5 | Positive class leaves the certified cell or delta <= 0 |
| C8 | An infinite certified branch changes selectors at most d_V+d_W-2 times. | Strictly increasing g(t), invariant equal-total walls, single-crossing unequal-total walls | 5 | Nonmonotone envelope, tie counted as strict, or omitted total-degree class |
| C9 | A stationary pair has t_(n+1) = lambda t_n + mu with global-origin intercept. | PROOF_PACKAGE §8 | 5 | Selector is not stationary or origin is silently reset |
| C10 | Coordinate reversal gives B_(R alpha) R = R A_alpha and A_(R beta) R = R B_beta. | PROOF_PACKAGE §9 | 6 | Wrong permutation, phase order, or sign |
| C11 | Phase-resolved reciprocity is necessary and sufficient edgewise on U_e,V_e with reflected certificates. | n=1 restriction plus edge induction | 6 | Scalar-only equality, non-fixed same seed, or proper span promoted to full rank |
| C12 | The lower-ideal result is a one-edge, one-step four-projection margin lemma. | PROOF_PACKAGE §10 and typed pair margins | 7 | Target-core inclusion, C1-to-C2 stability, multi-edge, or all-iterate claim |
| C13 | The asymmetric r=3 fixture realizes a strict C1-to-C2-to-C2 path and its reflected path. | PROOF_PACKAGE §11 exact matrices, gaps, carries, and seeds | 7 | Arithmetic, gap, determinant, or span mismatch |
| C14 | Cancellation and missing-reflection fixtures delimit the hypotheses. | PROOF_PACKAGE §12 | 6 and 8 | Example lies inside the headline class or does not cancel/mismatch |
| C15 | The bounded public screen found no exact conjunction collision with Papers 12--26 or reserved axes 28--31. | CITATION_VERIFICATION and NOVELTY_ASSESSMENT | 2 and 8 | A primary source has the exact conjunction or a reserved axis is imported |
| C16 | The article is proof-only, anonymous, and has no external effect. | EXPERIMENT_TRACKER, SOURCE_LOCK, later publication lock | 8 | Empirical/CAS support, identity/path/provenance leak, upload, or submission |

The matrix is a writing map, not evidence by itself.  Every universal claim is
proved symbolically in the main body or a clearly referenced appendix; the
fixture is never used to establish a universal theorem.

## Proof dependency spine and acceptance tests

The article follows the dependency order D0 typed assumptions and seed
realization; D1 symplectic Jacobians and inverse order; D2 grouped positive-face
determinant; D3 Jacobian independence and injective substitution; D4 strict
carries and phase maps; D5 all-ones translation and integer monotonicity; D6
envelope monotonicity and wall count; D7 stationary affine tail; D8 reflected
identities and observable-span necessity/sufficiency; D9 local four-projection
lemma; and D10 fixture, counterexamples, and boundaries.

Before source review, the author must check:

1. Every displayed matrix multiplication uses the phase order W after V in the forward map and W before V in the inverse.
2. The determinant coefficient is exactly c_(alpha0)^r (-1)^r (1-|alpha0|) product_i alpha0_i and is nonzero for the locked field and support class.
3. The same global origin u_0 is used in the translation, wall count, and affine intercept.
4. Reflection labels are described as appropriate support/action certificates, not as global support closure.
5. The lower-ideal lemma carries selected-minus-new signs on all four normalized projections and stops after one step.
6. Every anti-claim and failure boundary in SOURCE_LOCK is visible in the final limitations section.

## Section-by-section outline

### Abstract (0.4 page; `00_abstract.tex`)

State the exact field, dimension, collected positive supports, certified strict
edge, and the four results: survival, diagonal translation and d_V+d_W-2
bound, affine tail, and edgewise reflected reciprocity.  Mention the local
four-projection lemma only with its one-step scope.  Use no citations, priority
language, computation, or undefined empirical terminology.  The abstract must
stand alone and say that all conclusions are certified-branch statements.

### 1. Introduction (1.8 pages; `01_introduction.tex`)

Open with the apparent high-dimensional selector automaton produced by two
nonlinear shears.  Explain why positive mixed supports do more than make each
individual gradient easy: they force a common diagonal direction while leaving
transient selector changes and reflected phase order to analyze.  State the
gap, the one-sentence contribution, and four falsifiable contributions aligned
with C3--C12.  Preview the exact wall bound and observable-span distinction.
End with the scope map and a reading guide.  Figure 1 is a symbolic phase
pipeline showing V selector -> first carry -> W selector -> diagonal update,
alongside the W-then-V reflected inverse path; it contains no data.

### 2. Related work and collision positioning (1.5 pages; `02_related_work_and_collision_positioning.tex`)

Organize synthesis by methodological family rather than paper-by-paper:
(i) polynomial automorphisms and reversors (S01, S02, S08, S19, S20), (ii)
monomial/Newton/tropical degree mechanisms (S03--S05, S11, S14, S16, S17), and
(iii) Hamiltonian, symplectic, triangular, and dynamical-degree contexts
(S06, S07, S09, S10, S12, S13, S15, S18).  For each family state what is
borrowed as context and what must not be inferred.  Include a compact table
with columns source role, closest mechanism, and missing Paper-27 property.
Disclose that the public screen is bounded through 2026-08-29 UTC and is not
an exhaustive or priority claim.  Explicitly absorb Paper 22's forward
endpoint-spike mechanism and distinguish Paper 26's planar bridge.

### 3. Setup, typed cells, and main theorem (2.8 pages; `03_setup_typed_cells_and_main_theorem.tex`)

Define K, r, supports, coefficient field, monomial weighted degree, incoming
leading blocks, shears, Hessians, inverses, support functions h_V and h_W,
matrices A and B, and the coordinate reversal R.  State the corrected typing:
the u-only cone K_e^u is separate from the pair cell C_e^+, which contains w,
pair carries, reflected predicates, and target certificates.  Define integer
seed cells and U_e,V_e.  State one omnibus theorem with four explicitly scoped
clauses: (A) symplecticity and leading-form survival/phase maps, (B) diagonal
translation, wall bound, and affine tail, (C) edgewise observable-span
reciprocity, and (D) the local one-edge lower-ideal lemma.  Every quantifier
must say certified strict branch or finite seed-indexed edge word.

### 4. Positive-face survival and degree transport (4.2 pages; `04_positive_face_survival_and_degree_transport.tex`)

First verify the symplectic Jacobians and inverse order.  Group the exposed
face Hessian determinant by row-labelled exponent tuples.  Choose a generic
secondary weight, isolate the repeated minimizer, and derive the matrix-lemma
witness.  Apply the characteristic-zero Jacobian criterion and injective
substitution to prove algebraic independence.  Then derive the componentwise
gradient degrees, strict fresh-block carries, forward phase map, and reflected
inverse subtraction signs.  Include a short proposition explaining why an
auxiliary tied-face Hessian certificate does not select a tied vertex.  This
section carries the complete proof of C3--C6, not a generic-coefficient
assertion.

### 5. Translation, wall bound, and affine tail (3.8 pages; `05_translation_wall_bound_and_affine_tail.tex`)

Derive v = h_V(u) 1 - u and u' = h_W(v) 1 - v = u + delta(u) 1.  Establish
integral delta >= 1 on a strict integer branch and write u_n = u_0 + t_n 1.
Group support exponents by total degree, define g(t) = h_V(u_0+t 1)-t, and
prove strict increase.  Show equal-total walls are invariant and unequal-total
walls cross at most once for both envelopes, yielding d_V+d_W-2.  Derive the
stationary affine tail with lambda=(|alpha|-1)(|beta|-1) and
mu=((|beta|-1) alpha-beta) dot u_0, emphasizing the global origin.  Figure 2
is a symbolic ray/envelope diagram with invariant and single-crossing walls.

### 6. Reflected inverse reciprocity (3.5 pages; `06_reflected_inverse_reciprocity.tex`)

Introduce R_state(u,w)=(Rw,Ru), derive the two permutation identities, and
track the W-then-V inverse phase.  Prove necessity from n=1 restrictions on
U_e and V_e; prove sufficiency by induction over a finite edge-indexed word
using reflected score, carry, and target certificates.  State the full-matrix
upgrade only for full spans and explain why scalar total-degree equality or a
non-R_state-fixed same seed is insufficient.  Figure 3 is a symbolic square
U_e -> V_e with the reflected action and the full-span upgrade.  Include the
missing-reflection n=1 counterexample at the end.

### 7. Local lower-ideal lemma and exact fixture (4.0 pages; `07_lower_ideal_lemma_and_exact_fixture.tex`)

Normalize one strict typed pair core by the l1 norm.  Define the four compact
projections pi_u(C_e^+), A_alpha u, R u, and R A_alpha u.  State selected-minus-
new row margins and typed pair margins, then use homogeneity to prove exactly
one forward and one reflected inverse leading step.  Explicitly deny target
inclusion and all-iterate stability.  Present the r=3 asymmetric supports,
matrices A_1,A_2,B_1,B_2, products C_21,C_22, all listed selector gaps,
carries, six seeds, determinant/full-span checks, and the reflected path.  A
table records the arithmetic; Figure 4 is a symbolic C1 -> C2 -> C2 graph.

### 8. Boundaries, limitations, reproducibility, and conclusion (3.7 pages; `08_boundaries_limitations_reproducibility_and_conclusion.tex`)

Give the cancellation fixture V=(q1+q2+q3)^3 and W=(p1-p2)^3, the zero/unit
support boundary, ties, empty cells, failed carries, missing reflected
certificates, proper spans, positive characteristic, and r=2 boundary.  List
all anti-claims: no arbitrary supports, global reversor, conjugacy,
classification, entropy, higher dynamical degrees, minimal scalar recurrence,
Perron algebraic degree, same-seed result away from an R_state-fixed pair,
multi-edge or all-iterate perturbation stability, or priority.  State that
reproducibility means literal symbolic derivations and exact fixture tables;
there is no code, data, CAS certificate, numerical scan, or GPU run.  Close
with a measured restatement and two concrete future directions (finite fan
extensions with new certificates; broader reversible support actions).

## Figure and table plan

| ID | Type | Content | Data source | Priority |
|---|---|---|---|---|
| Fig. 1 | Symbolic hero diagram | Forward V/W phases, carries, diagonal update, and reflected inverse order | Hand-drawn TikZ or native LaTeX; no external asset | HIGH |
| Fig. 2 | Symbolic envelope diagram | Translated ray, V/W upper envelopes, invariant equal-total walls, single-crossing walls | Exact formulas in §5 | HIGH |
| Fig. 3 | Symbolic span square | U_e and V_e restrictions, R_state action, full-span upgrade | Exact formulas in §6 | MEDIUM |
| Fig. 4 | Symbolic transition graph | Fixture C1 -> C2 -> C2 and reflected path with carries | PROOF_PACKAGE §11 | MEDIUM |
| Table 1 | Claim/evidence table | C1--C16 with section, proof anchor, and kill condition | This plan and source matrix | HIGH |
| Table 2 | Related-work matrix | Source role versus mechanism and explicit do-not-infer boundary | CITATION_VERIFICATION | MEDIUM |
| Table 3 | Fixture arithmetic | Matrices, products, gaps, seeds, determinants, spans | PROOF_PACKAGE §11 | HIGH |
| Table 4 | Boundary map | Failed assumption -> stopping consequence -> safe wording | PROOF_PACKAGE §12 and §13 | HIGH |

All visuals are symbolic.  No numerical plot, simulation, generated data, or
unverified diagram is allowed.

## Citation plan

Use only the twenty verified records S01--S20 from CITATION_VERIFICATION.md.
The introduction cites S01, S03, S06, S08, and S12 for context.  Section 2
uses all records in the three methodological groups above, with S09, S10,
S13, S15, and S18 reserved for dynamical-degree distinctions.  Sections 3--7
need no citation for theorem-critical algebra; they cite the source ledger only
where a contextual comparison is made.  Section 8 cites S19 and S20 when
stating that general inverse-degree bounds do not imply this exact equality.
The bibliography will contain only keys actually cited in the final source;
each entry must be copied from a verified arXiv/DOI/official record, never
generated from memory.  No citation is allowed to carry a priority claim.

## Source-writing and review gates

After this plan author stop, a fresh plan reviewer must check claim--evidence
alignment, proof dependency order, exact page arithmetic, citation roles,
figure/table safety, and the corrected scope wording.  A nonzero finding is
FAIL / WRITE NOTHING.  A PASS permits only the next publication-scope gate.
The future anonymous source trio is exactly main.tex, math_commands.tex, and
references.bib (with sections embedded or mechanically included as authorized
by a later source lock); it must contain none of the internal paths, hashes,
event IDs, reviewer names, identity, or provenance language in this plan.

## Next steps (not yet authorized)

- [ ] Independent PAPER_PLAN review and PASS consumption.
- [ ] Publication-stage scope review and lock.
- [ ] Draft the exact anonymous source trio from this plan.
- [ ] Run only the deterministic, time-indexed build gates authorized by the
      later ledger; no external release or submission.

BATCH07_PAPER27_PAPER_PLAN_FROZEN

## 10. Quantifier, page-range, and manifest correction addendum

This append-only addendum supersedes only the three administrative phrases
identified before plan review.  The one-step survival and diagonal-translation
clauses apply to each certified strict edge.  The selector-change bound and
the stationary affine tail apply to each **infinite certified strict branch**;
a finite branch may terminate at a tie, failed carry, empty cell, or missing
certificate before those conclusions are invoked.

The article target is 24--28 proof-content pages, with the planned 25.7-page
budget inside that interval.  The broader 22--30 range is retained only as the
candidate-gate credibility screen and is not a publication-stage page target.

The manifest vocabulary is now explicit: the source-design aggregate after
its independent review has 23 rows; adding SOURCE_LOCK gives the 24-row
post-lock aggregate; adding this plan gives the 26-row plan-stage aggregate
(the later plan-review row will make 27).  The controlled status ledger is
excluded from all aggregates, although it is included in review whitelists for
parent binding.  These corrections do not change the theorem, page arithmetic,
or claim matrix.

BATCH07_PAPER27_PAPER_PLAN_CORRECTION_ADDENDUM

## 11. Section-number crosswalk correction

This append-only note makes the plan's eight-body-section numbering
authoritative for downstream writing.  The source-design matrix and the final
proposal were drafted with a longer, ten-section skeleton; their section
labels are historical evidence anchors, not instructions for the new source.
Under this plan, C13 is proved and witnessed in Section 7, C14 is handled in
Sections 6 and 8, C15 is positioned in Sections 2 and 8, and C16 is governed
in Section 8.  All claim text, proof obligations, and kill conditions remain
unchanged.

BATCH07_PAPER27_PAPER_PLAN_SECTION_MAP_CORRECTED
