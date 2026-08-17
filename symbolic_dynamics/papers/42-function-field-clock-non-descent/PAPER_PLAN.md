# Paper 42 writer plan

**Working title:** Finite-Field Clocks Do Not Become Rational Primes: Exact
Factor Non-Descent for the Full Shift

**Candidate:** proposed `SD-C44`, historical parent `SD-C01`

**Paper type:** exact theory/closure paper with source-ownership audit

**Date:** 2026-08-17 UTC

**Current checkpoint:** post-output publication-source synchronization;
out-of-tree PDF candidate complete; HOLD for independent writer Round 1.

**Target length:** 12--13 A4 pages, with an allowed total range of 10--14
pages including references and appendices. The manuscript uses a single-column
11-point article layout and at most three pure-TikZ figures.

**One-sentence contribution:** For the frozen full-
`q`-shift with `q` in `{2,3,5}`, we prove that its valid function-field
primitive factors cannot be retyped as the rational-prime Euler ledger while
simultaneously preserving the exact degree clock, source-symbol marker,
multiplicity, and determinant ownership.

## Claim and evidence matrix

| ID | Claim | Exact evidence | Status and novelty | Main location |
|---|---|---|---|---|
| C0 | The full-`q` shift owns the primitive-necklace ledger, Möbius count, and determinant `D_q(s,z)=1-zq^(1-s)`. | Frozen Lemma 0; periodic-point count `#Fix(sigma^r)=q^r`; Artin--Mazur/Bowen--Lanford context. | Proved prior art; 0 novelty credit. | Sections 2--3 |
| C1 | No total map from all source primitive necklaces to rational primes preserves `log p=n log q`. | The primitive class `[01]` has length two and would have image `q^2`, which is composite. | Proved exact closure; bounded novelty only. | Section 4.1 |
| C2 | No factorwise identification preserves marker, weight, and multiplicity. | Formal monomial equality forces `n=1,p=q`; `N_q(1)=q` then collides with one target factor at `p=q`. | Proved exact closure; bounded novelty only. | Section 4.2 |
| C3 | The source and rational-prime marked determinants differ in their first logarithmic `z` coefficient. | Source coefficient `q^(1-s)` versus prime-zeta coefficient `P(s)`; exact large-real-`s` separation. | Proved exact analytic mismatch; no zero data. | Section 4.3 |
| C4 | Every declared repair gives up at least one frozen coordinate. | Six-row repair matrix over support, clock, marker, multiplicity, and owner. | Exhaustive only for declared repairs. | Section 5 |
| C5 | The source function-field ledger remains valid and A1/A2 remain positive. | Necklace/irreducible-polynomial count equality, ordinary powers, and scalar weighted-adjacency determinant. | Positive control; source/function prior art. | Sections 3 and 5 |
| C6 | The strict disposition is Route rejected and Route B false. | Frozen tuple `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)`. | Internal governance; 0 novelty credit. | Section 6 |
| C7 | The selector is unique but retrospective. | Six-card Boolean rule was written after all card outcomes and exact witnesses were known. | No prospective, outcome-independent, priority, or novelty credit. | Sections 2 and 6 |

## Narrative spine

1. A function-field ledger can be exact without being a rational-prime
   ledger.
2. The source object, marker, clock, and determinant are frozen before the
   comparison.
3. Three independent exact tests fail: a length-two support witness, a
   degree-one multiplicity collision, and a first marked coefficient mismatch.
4. Positive controls show that the source ledger itself is not damaged.
5. Repair succeeds only after changing a declared coordinate, so it cannot
   earn same-object credit.
6. The strict Route tuple preserves source A1/A2 while rejecting the broader
   rational-prime program.

## Structure and page budget

### Abstract (180--220 words; about 0.35 page)

- State the exact source object and the rational-prime factor question.
- Give all three witnesses without numerical experiment language.
- Preserve the positive function-field ledger.
- State the narrow Route outcome and retrospective/novelty boundary.
- No citations or undefined abbreviations.

### 1. Introduction (0.9--1.1 pages)

- Open with the distinction between equality of zeta-shaped functions and
  identity of primitive-factor semantics.
- Attribute periodic-point and finite-shift determinant machinery.
- State the frozen comparison and three theorem channels.
- Give four falsifiable contribution bullets.
- Place Figure 1 as the hero ownership/type diagram.
- Make the 3/10 typed-closure novelty boundary visible before Section 2.

### 2. Prior ownership, selection, and claim boundary (1.0--1.2 pages)

- Synthesize foundational periodic-point zeta, finite-shift determinant,
  necklace/irreducible counts, and rational Euler-product sources.
- Use a comparison table rather than paper-by-paper summaries.
- State that all positive source formulas are prior art.
- Explain the six-card selector and its retrospective chronology.
- Separate P39/P40/P41 collision boundaries from ranking/authorization.

### 3. Frozen source ledger and typed comparison (1.4--1.7 pages)

- Define the full shift, primitive necklaces, rotation/reversal convention,
  word powers, clock, marker, and source factor.
- Derive fixed-point exponential, determinant, primitive count, and product.
- Define the separate rational-prime diagonal comparator and its domain.
- Give the necessary equality matrix.
- Include Figure 1 if not already placed in the introduction.

### 4. Three exact non-descent theorems (2.0--2.4 pages)

- Theorem 1: total exact-clock support failure using `[01]`.
- Theorem 2: marker/weight/multiplicity failure at length one.
- Theorem 3: first marked coefficient mismatch using exact asymptotic limits.
- Give proof intuition and complete main-text proofs; no proof is deferred
  merely to create length.
- Include Figure 2, which keeps the three channels logically independent.

### 5. Positive controls, repairs, and ownership (1.2--1.5 pages)

- State the function-field prime-polynomial positive control.
- State the one-orbit and rational-prime diagonal-operator controls.
- Present the six-row repair matrix and bounded corollary.
- Include Figure 3 to show which coordinate each repair changes.

### 6. Strict Route audit and reproducibility boundary (0.8--1.0 pages)

- Explain A0--A4 coordinate by coordinate.
- Preserve A1/A2 positive for the source function-field species.
- State `ROUTE_A_REJECTED` and both Route-B booleans false.
- Record the independent DA acceptance qualitatively.
- Carry the unique blueprint Section-14 canonical integration block, sourced
  only from the final authority outputs and preserving its exact chronology.
- State that no prime-table fit, target-zero comparison, or scope enlargement
  follows from the reproducibility evidence.

### 7. Limitations and conclusion (0.55--0.7 page)

- Restate only the exact same-clock/same-marker closure.
- List changed-marker, induced, countable, and infinite-memory models as
  outside scope.
- State the 3/10 novelty assessment and literature-search limitation.
- Give one concrete reopening obligation: a new source lock declaring object,
  marker, clock, function space, and operator owner.

### Appendix A. Exact combinatorics and coefficient proof (1.0--1.3 pages)

- Derive Möbius inversion and `N_q(1),N_q(2)`.
- Tabulate `q=2,3,5` witnesses.
- Expand the dominated-convergence argument for the target coefficient.
- State falsifiers for each theorem.

### Appendix B. Type, literature, and provenance firewalls (0.8--1.0 pages)

- Give the full type table and source-to-claim matrix.
- Record retrospective chronology and non-authorization boundaries.
- Separate formal-in-`z`, local analytic, and `Re(s)>1` assertions.

### References (0.5--0.8 page)

- Four cited entries only: Artin--Mazur, Bowen--Lanford, the verified 2026
  necklace-polynomial preprint, and NIST DLMF 25.2.11.
- No bibliography padding.

## Figure plan

| ID | Type | Content and comparison | Location | Caption point |
|---|---|---|---|---|
| Figure 1 | Pure TikZ hero/type diagram | Source primitive necklace and owned determinant; exact function-field prime-polynomial control; blocked arrow to rational-prime atom. | Section 1 or 3 | Equal degree counts support the function-field ledger, but exact rational-prime retyping forces `p=q^n` and changes marker/multiplicity. |
| Figure 2 | Pure TikZ three-channel proof map | Clock/support, marker/multiplicity, and first coefficient shown as parallel independent channels. | Section 4 | Any one channel defeats the corresponding conjunction; the theorem does not infer one failure from another. |
| Figure 3 | Pure TikZ repair/ownership map | Six declared repairs grouped by the coordinate they abandon; function-field dictionary remains positive. | Section 5 | Repairs are legitimate changed models but do not receive same-object credit. |

All figures use vector TikZ, no embedded raster, no decorative title, a
colorblind-safe blue/amber/purple palette, and line style in addition to
color. Captions must remain self-contained.

## Citation plan

| Section | Keys | Source-backed use |
|---|---|---|
| 1 | `artin1965periodic`, `bowen1970zeta` | Periodic-point zeta and finite-shift determinant context. |
| 2 | all four keys | Method-family synthesis and explicit prior ownership. |
| 3 | `artin1965periodic`, `bowen1970zeta`, `chebolu2026necklace`, `nistDLMF25211` | Full-shift ledger, necklace/irreducible count, and rational Euler product. |
| 4 | `nistDLMF25211` | Target prime Euler product/prime-zeta coefficient only. |
| 5 | `chebolu2026necklace`, `bowen1970zeta` | Positive function-field and finite-shift controls. |
| 6 | none | Internal Route/provenance statement. |
| 7 | none required | Scope and reopening obligations. |
| Appendix B | all four keys | Source-to-claim firewall. |

## Claim-language rules

- Say “the bounded audit did not locate the exact typed formulation,” never
  “no prior work exists.”
- Say “typed closure novelty assessed at 3/10,” never “new finite-field/Riemann
  connection.”
- Say “retrospective unique rule result,” never “prospectively selected.”
- Say “the source function-field ledger remains exact,” never “the full shift
  fails A1 or A2.”
- Say “the rational-prime diagonal comparator is separately owned,” never
  “the source operator realizes the rational Euler product.”
- Qualify totality, exact clock, marker, and listed-repair exhaustiveness every
  time a no-go is summarized.

## Internal writer review

The source draft received claim-to-proof, citation-key, and reverse-outline
checks before integration. After the post-output synchronization it received
two clean, fixed-epoch builds in independent scratch directories and a new
all-page visual inspection. A Round-1 text-layer finding was then repaired at
compile time, without changing a protected source: `cmap` supplies complete
math-font Unicode maps, while `accsupp` assigns U+2192 as the actual text of
the three visually unchanged long arrows. Two fresh 14-page builds are
byte-identical at SHA-256
`b64df6a2054f9ed4047feb679170211f29f44faf253abbe21d11763360708139`.
Default, layout, raw, and bounding-box extraction contain no illegal C0/DEL
character; the bounding-box XML parses; and all three arrows extract as a
single U+2192. No compiled artifact has been installed in the authority paper
directory.

## Post-output publication addendum -- 2026-08-17 UTC

- The authority integration reached `POST-OUTPUT AUTHORITY CLEAN` before this
  writer-owned synchronization. Final canonical bytes and results were known;
  this addendum is not prospective, outcome-independent, blind, preregistered,
  or eligible for novelty or priority credit.
- The designated Section-14 paragraph was replaced by exactly one canonical
  block. It records evaluator checks `11/11` and `11/11`, science SHA-256
  `078d98da2f3c89c0f5f4e7ef6be84066ee60a1c1d82c86788de675ad349b7848`,
  source resolution `29/29`, sole survivor `SD-C01`, zero theorem and positive-
  control failures, and six repair rows with zero failures.
- The same block records Route checks `21/21` and `13/13`, the frozen tuple,
  `ROUTE_A_REJECTED`, Route B false, all `2246` mutations with zero survivors,
  deterministic A/B/C and cold-copy results, paired-state equality, audit
  `56/56`, idempotence zero, the 95-entry ledger, and the exact 49-output set.
- The chronology remains
  `RETROSPECTIVE_STATIC_SEAL_FROZEN_BEFORE_AUTHORITY_MATERIALIZATION`.
  The Stage-A commit triple remains `PENDING_FIRST_ARTIFACT_COMMIT`, the paper
  manifest remains absent, and `STOP_DUPLICATE` remains an external collision
  boundary rather than an experiment result.
- Only `sections/6_route_reproducibility.tex`, this plan,
  `WRITER_HANDOFF.md`, and the self-excluding writer manifest are mutable in
  this lane. The other 15 writer sources and every integration/research byte
  remain locked to their pre-sync values.
- The PDF candidate remains outside the authority tree. Installing
  `main.pdf`, creating `COMPILATION_REPORT.md`, or advancing the paper manifest
  requires the independent writer review and a separate root release.
