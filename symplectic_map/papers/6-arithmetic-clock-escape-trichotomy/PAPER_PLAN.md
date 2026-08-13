# Paper Plan

**Title:** *Finite Arithmetic Capacity under Additive Locally Constant,
Good-Reduction Multiplier, and Algebraic-Action Readouts*  
**One-sentence contribution:** A fixed readout of the form
`log p = v + log q + alpha`, with `v` in one finite-dimensional rational
space, `q^2` supported on one finite set of rational primes, and `alpha`
real algebraic, realizes at most `dim_Q(V)+|S_Q|` distinct rational-prime
logarithms.  
**Format:** anonymous 11 pt specialist theory article with author--year
citations  
**Type:** theorem, source-class certificates, and source-locked exact/static
implementation audit  
**Date:** 2026-08-14  
**Target:** compiled pre-review manuscript; independent manuscript review is a
separate downstream stage  
**Section count:** eight main sections and three appendices

The paper has one technical spine.  Hermite--Lindemann removes the algebraic
additive term from a hypothetical dependence; finite-place valuations then
remove the fixed-support multiplier term one outside prime at a time.  What
remains forces the locally constant terms for distinct outside primes to be
rationally independent.  The three dynamical source classes explain when the
normal form is available; they are not three separate no-go theorems.

## Claims--Evidence Matrix

| Claim | Primary evidence | Supporting audit evidence | Status | Location |
|---|---|---|---|---|
| C1. The additive normal form is closed under the declared finite rational operations, including negative and rational multiplier powers. | `notes/PROOF_PACKAGE.md`, Lemmas 1--2 | `exact_controls` K005; exact scope ledger | Proved | Sec. 3 |
| C2. Distinct outside-support primes force rationally independent `v_p` terms. | Full Hermite--Lindemann, squaring, and one-place-per-prime proof in `notes/PROOF_PACKAGE.md` | proof IDs T005--T009; K006 | Proved | Sec. 4 |
| C3. The hit-set capacity is at most `dim_Q(V)+|S_Q|`, without assuming the hit set finite. | Theorem A, proof Step 7 | proof ID T010 | Proved | Sec. 4 |
| C4. Fixed finite-memory locally constant readouts occupy one finite-rank rational space after higher-block recoding. | Class-L proof certificate | proof ID L001; scope S001--S002 | Proved within source class | Sec. 5.1 |
| C5. For the declared good-reduction Hénon class, periodic coordinates are algebraic/integral away from fixed bad places and squared multiplier moduli have fixed support. | Class-M projective, non-Archimedean, monodromy, and normal-extension proof | proof IDs M001--M005; upstream Paper 3 | Proved within source class | Sec. 5.2; App. B |
| C6. Regular algebraic action evaluation and allowed real algebraic transforms yield a real algebraic additive term; algebraicity and gauge invariance are distinct. | Class-A proof certificate | proof IDs A001--A002; upstream Paper 4 | Proved within source class | Sec. 5.3 |
| C7. Selector L/M/A architectures are a corollary, not the proof of the additive theorem. | Corollary B | proof ID C001 | Proved | Sec. 5.4 |
| C8. Escape conditions are only necessary failures of this certificate and are neither exclusive, exhaustive, nor sufficient. | Corollary C | proof ID E001; escape/output gates | Proved as scoped contraposition | Sec. 6 |
| C9. The registered exact/static audit closes source, proof, scope, control, isolation, review, upstream, escape, and output gates without target data or numerical execution. | `results/EXPERIMENT_RESULTS.json`, registry, and manifest | 51-test JUnit and independent tree-bound review | Verified implementation/provenance | Sec. 7; App. C |

## Evidence Boundaries

- The capacity theorem is deductive; the registered audit checks its explicit
  dependency and scope contract rather than proving Hermite--Lindemann or the
  valuation theorem by computation.
- No prime table, generated prime-target array, Riemann-zero file, numerical
  logarithm, target fit, or numerical candidate run enters the paper package.
- The formal labels in K001/K004/K006 are not numerical targets.  The rational
  constant `2` in K002 and symbolic token `LOG_2` in K003 are source-locked
  assumption-boundary controls.
- The bound concerns exact equality and distinct rational primes.  It gives no
  Diophantine approximation or stability estimate.
- Deninger and Connes--Consani are positive arithmetic architectures outside
  the finite L/M/A certificate.  They rule out any universal no-go framing.
- The manuscript claims neither historical priority nor a Riemann-zero,
  trace-formula, determinant, quantization, or Route-B result.

## Structure and Page Budget

### Abstract (180--230 words)

- State the additive theorem and exact numerical bound immediately.
- Name the two proof mechanisms: Hermite--Lindemann and finite-place
  valuation isolation.
- Explain the L/M/A source certificates and selector corollary.
- Report the static audit facts: nine registered gates, 51 tests, one formal
  run, zero numerical runs/targets.
- End with the strongest nonclaim.

### 1. Introduction (1.2--1.5 pages)

- Motivate prime-logarithm periodic lengths using Berry--Keating, Deninger,
  and Connes--Consani without implying that this paper advances a spectral
  construction.
- Identify the design question: how much exact arithmetic capacity can a
  fixed additive finite certificate carry?
- State the theorem informally and list four falsifiable contributions.
- Place Figure 1 after the contributions.
- State the universal-no-go and complete-trichotomy nonclaims on page 1.

### 2. Arithmetic and dynamical context (1.1--1.4 pages)

- Symbolic suspensions and finite-memory roof functions.
- Arithmetic Hénon maps, good reduction, heights, and multiplier spectra.
- Exact symplectic generating actions and algebraic evaluation.
- Infinite-dimensional/adelic positive prime-orbit architectures.
- Position the contribution as a mixed source certificate with moderate
  synthesis novelty.

### 3. Additive certificate and closure (1.4--1.8 pages)

- Define `S_Q`-units uniformly across number fields.
- Define the canonical real-log normal form and target independence.
- Prove extension invariance and rational multiplier-log closure.
- State admitted and excluded operations in a compact table.

### 4. Finite arithmetic-capacity theorem (1.8--2.2 pages)

- State the theorem with set semantics and no prior finiteness assumption.
- Give the complete proof in the main text: choose certificates, clear
  denominators, derive `log R=beta`, apply Hermite--Lindemann, square, pass to
  one field, isolate every outside prime, count.
- Use Figure 2 to make the proof flow and failure conditions legible.
- Record the zero-dimensional and `q=1` edge cases.

### 5. Three source certificates (2.0--2.5 pages)

- Class L: higher-block recoding and finite rational rank.
- Class M: cyclic multiplicity, separate-degree homogenization,
  projective-affine dimension, good-reduction maximum argument, integral
  determinant-one monodromy, normal saturation, `q^2=lambda*bar(lambda)`.
- Class A: regular algebraic evaluation, real-valued algebraic transforms,
  full gauge endpoint term, and normalization boundary.
- State the selector theorem as a corollary after the additive theorem.
- Place Figure 3 after the three embeddings.

### 6. Capacity boundary and positive outside examples (1.0--1.3 pages)

- Give the four necessary certificate escapes.
- Explain target injection controls and why they do not contradict the
  theorem.
- Present Deninger's and Connes--Consani's prime-length architectures as
  positive, structurally outside cases.
- State every nonclaim: not exclusive/exhaustive/sufficient; no universal
  finite-dimensional or smooth obstruction.

### 7. Registered exact/static audit (0.9--1.2 pages)

- Explain pre-execution source lock, independent code authority, and actual
  Paper-3/Paper-4 terminal bindings.
- Report all nine gates, six exact controls, 20 proof IDs, 10 admitted and 9
  excluded operations, 12 scanned files, 51 tests, and strict manifest
  closure.
- Separate implementation evidence from mathematical proof.

### 8. Conclusion and limitations (0.5--0.7 pages)

- Rephrase the result as a capacity certificate.
- Emphasize exact-only scope and moderate synthesis novelty.
- Identify two concrete next questions: quantitative approximate analogues
  and separately locked nonalgebraic/multivalued/infinite-place readouts.

### Appendix A. Expanded theorem and edge-case ledger

- Rational roots and negative powers.
- Set selection and arbitrary certificate choice.
- Full output-scope table.

### Appendix B. Source-class proof details

- Class-M no-infinity, integrality, monodromy, and conjugation details.
- Class-A gauge formula and Class-L higher-block construction.

### Appendix C. Reproducibility and artifact hashes

- Official commands, versions, hashes, JUnit, figure regeneration, and
  forbidden-data declaration.

## Figure and Table Plan

| ID | Type | Description | Frozen source | Priority |
|---|---|---|---|---|
| Figure 1 | Hero implication/boundary diagram | Canonical L/M/A sum, theorem bound, and the four assumption exits; distinguish a scoped certificate from positive outside architectures | source lock, scope ledger, official result | HIGH |
| Figure 2 | Proof-flow diagram | Rational dependence to `log R=beta`, Hermite--Lindemann, squaring, valuation isolation, independence, and capacity count | proof ledger and official proof gate | HIGH |
| Figure 3 | Source/audit matrix | L finite rank, M fixed support, A algebraicity, selector embeddings, upstream Paper-3/Paper-4 closure, and nine registered gates | proof ledger, upstream gate, official result | HIGH |
| Table 1 | Assumption boundary | Admitted operation, certificate mechanism, and nearest excluded operation | scope ledger | HIGH |
| Table 2 | Related-work boundary | Symbolic, arithmetic Hénon, exact action, and arithmetic positive architectures | verified citations | MEDIUM |
| Table 3 | Official gate summary | Nine gates and zero-execution counters | official JSON/registry/manifest | MEDIUM |

All figures must be generated from strict JSON/ledger loaders, exported as PDF
and SVG vector masters plus PNG review copies, and reproduce byte-for-byte
under two consecutive full regenerations.

## Citation Plan

- Prime-logarithm motivation: Berry--Keating (1999), explicitly heuristic.
- Symbolic dynamics: Parry--Pollicott (1990) and Lind--Marcus (1995), only for
  standard shifts, suspensions, and higher-block context.
- Arithmetic Hénon background: Friedland--Milnor (1989), Silverman (1994),
  Ingram (2014), Hsia--Kawaguchi (2018), Cantat--Dujardin (2026), and
  Bianchi--He (2026).
- Exact action background: Delshams--Ramírez-Ros (1997),
  Bialy--Tsodikovich (2023), and standard symplectic-map references already
  verified in the preceding paper.
- Transcendence and valuations: Baker (2022) and Neukirch (1999).
- Positive outside-boundary architectures: Deninger (1998, 2026), Connes
  (1999), Connes--Consani (2016, 2024).
- Every bibliographic record must have primary DOI/arXiv/publisher verification
  and a claim-level safe-use note.  Citations provide context only; none
  substitutes for the paper-specific proof.

## Author-Side Pre-Review Checklist

- [ ] Three or more deterministic vector figures with strict frozen-data
  provenance.
- [ ] At least 13 cited-only, individually verified bibliography records.
- [ ] Complete theorem proof in the main text and expanded source proofs in
  appendices.
- [ ] No `[VERIFY]`, TODO, placeholder, overclaim, or stale section.
- [ ] Clean deterministic build; no undefined reference/citation or material
  box warning; embedded/subset fonts.
- [ ] Claim manifest, experiment passport, figure package, paper
  configuration, pipeline state, and pre-review integrity report.
- [ ] Immutable `paper_pre_review.pdf` snapshot.
- [ ] No independent manuscript review or author self-check labeled as
  independent review.
