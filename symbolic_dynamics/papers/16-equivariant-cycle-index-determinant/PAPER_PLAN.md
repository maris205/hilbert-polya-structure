# PAPER PLAN

**Title:** Character-Resolved Cycle-Index Determinants of the Tensor-Atom
Shift: A Formal Burnside Lift and an Arithmetic Fredholm No-Go

**Candidate:** SD-C18

**Type:** theoretical symbolic-dynamics paper

**Date:** 2026-08-14

**Target format:** anonymous general A4 research manuscript

**Target length:** approximately 7,000 words plus references and proof appendix

## One-sentence contribution

We retain the nonzero \(S_3\) primitive-cycle class erased by the scalar
tensor-subset determinant and prove that, for its canonical rank-one and
diagonal lifts, no character readout both preserves the pure Euler trace-log
and survives as a nontrivial fixed arithmetic Fredholm fiber.

## Claims–evidence matrix

| Claim | Evidence | Status | Manuscript location |
|---|---|---|---|
| The primitive squarefree ledger has a canonical Burnside/species lift | cyclic ordered set partitions; \(C_2\) sign carrier; zero-specialization | proved | Sections 3–4 |
| The first scalar-zero coefficient hides a nonzero equivariant class | \(\mathcal R_3=[S_3/S_3]+[S_3/C_3]-[S_3/C_2]\); marks \((0,0,3,1)\); character \((0,0,3)\) | proved | Section 4 |
| Higher Adams powers cannot remove the \(pqr\) residual | multidegree map \(\alpha\mapsto r\alpha\) | proved | Section 4 |
| Distinct arithmetic weights destroy fixed-fiber \(S_n\) symmetry | direct commutator/stabilizer theorem | proved | Section 5 |
| Equal weights restore symmetry but kill all nontrivial rank-one isotypes | image is the trivial line | proved | Section 5 |
| The diagonal resolved lift has the wrong power ghosts and determinant | coefficient witness \(r\) versus 0; mixed superdeterminant factors | proved | Section 6 |
| No linear readout both detects \(R_3\) and preserves the pure Euler trace-log | isolated mixed squarefree coefficient | proved for frozen model | Section 6 |
| A formal projective limit exists, but no canonical bounded raw-transfer inductive limit does | zero-specialization; nonintertwining and norm growth | proved | Section 7 |
| The diagonal prime-subset operator is in \(\mathcal S_q\) iff \(q\operatorname{Re}s>1\) | exact singular-value Euler product | proved | Section 7 |
| The mechanism is not arithmetically selective | composite, shuffled, random, and free-commutative inventories obey the same finite algebra | proved structurally | Section 8 |

## Argument blueprint

### Central thesis

The Burnside/cycle-index lift is a legitimate formal refinement of the
scalar subset determinant, but its resolved motion cannot be interpreted as
a character Fredholm factor of the arithmetically specialized canonical
operator without changing either symmetry, temporal powers, or the Euler
ledger.

### Subargument 1 — positive formal result

- **Claim:** scalar cancellation loses nontrivial primitive symmetry data.
- **Evidence:** exact \(pqr\) Burnside marks and representation character.
- **Counterargument:** equal cardinalities suggest an equivariant pairing.
- **Response:** the three-cycle mark differs by three, excluding such a
  pairing.

### Subargument 2 — fixed-fiber obstruction

- **Claim:** prime specialization turns \(S_n\) relabeling into covariance
  between operators, not commutation with one operator.
- **Evidence:** explicit conjugation formula and stabilizer theorem.
- **Counterargument:** equalize weights.
- **Response:** equalization leaves only the trivial rank-one image.

### Subargument 3 — analytic lift obstruction

- **Claim:** keeping subset representation lines through a diagonal operator
  changes the power ledger and determinant.
- **Evidence:** \(b(x)^r\) versus \(b(x^r)\), coefficient witness, and
  mixed-factor product.
- **Counterargument:** regularize the determinant.
- **Response:** the mismatch is already a finite formal trace mismatch;
  regularization cannot preserve both sequences.

### Subargument 4 — scoped conclusion

- **Claim:** the formal ledger is useful, but the canonical arithmetic
  character-Fredholm program stops.
- **Evidence:** character-readout incompatibility, Schatten theorem, raw
  transfer noninductivity, and controls.
- **Counterargument:** a different equivariant model might evade the result.
- **Response:** acknowledged; a genuine fiber cocycle would be a new
  Symbolic Dynamics candidate.

## Detailed structure

### Abstract — 220–250 words

- State the formal positive result and analytic no-go in the first two
  sentences.
- Include the exact memorable certificate: character \((0,0,3)\), marks
  \((0,0,3,1)\), and \(\mathcal S_q\) threshold.
- State the fixed route tuple and no-RH boundary.

### 1. Introduction — 850 words

- Open with scalar dimension versus equivariant recurrent motion.
- Connect directly to the Paper 15 \(pqr\) survivor.
- State the incompatibility triangle before technical detail.
- Give four falsifiable contributions.
- Place Figure 1 here.

### 2. Classical boundary — 850 words

- Organize prior work by formalism: symbolic zeta; Burnside/species;
  necklace/Witt/Adams; equivariant/twisted zeta; stable/infinite limits.
- State what is classical and the exact model-specific novelty boundary.

### 3. Frozen tensor-subset shift — 800 words

- Define tensor source, edge alphabet, rank-one transfer, and scalar shadow.
- Define semilinear label action and \(C_2\)-colored sign line.
- Establish notation for primitive squarefree cycles.

### 4. Formal Burnside lift and the \(pqr\) certificate — 1,000 words

- Derive cyclic ordered set partitions and counts.
- State and prove the Burnside orbit decomposition.
- Give marks and character decomposition.
- Prove Adams isolation and formal projective zero-specialization.

### 5. Fixed arithmetic symmetry obstruction — 800 words

- Prove semilinear covariance and the commutator criterion.
- Specialize to distinct prime weights.
- Analyze equal weights and nontrivial isotypes.

### 6. Ghost, determinant, and readout incompatibility — 1,000 words

- Separate rank-one and diagonal power traces.
- Prove the coefficient witness and diagonal mixed-factor theorem.
- Prove the character-readout incompatibility.

### 7. Infinite-label analytic boundary — 650 words

- Distinguish projective formal completion from raw operator induction.
- Prove nonintertwining/norm growth.
- Prove the \(\mathcal S_q\) criterion and explain why trace class does not
  repair the determinant.

### 8. Controls and Route-A decision — 650 words

- Report inventory-blind controls and `PROVES_TOO_MUCH`.
- Give the frozen route table.
- Explain why the scalar A2 shadow cannot be patched into SD-C18.

### 9. Conclusion — 350 words

- Retain the formal ledger; stop character Fredholm fibers.
- Name the next in-family obligation: a genuine finite-group fiber cocycle.
- Keep cross-family ideas in `ROUND2_CLUE` only.

### Appendix — full proofs and scope ledger

- Primitive-root/cycle-index details.
- Full \(S_3\) mark and character tables.
- Two-variable determinant certificate.
- Schatten proof details.
- Explicit nonclaims and mandatory statements.

## Figure plan

| ID | Type | Description | Source | Priority |
|---|---|---|---|---|
| Figure 1 | conceptual incompatibility diagram | Formal Burnside ledger at top; three outgoing branches show augmentation killing motion, arithmetic specialization breaking commutation, and diagonal lifting adding mixed factors | exact theorems in `PROOF_PACKAGE.md`; manually drawn TikZ | high |
| Table 1 | exact \(S_3\) certificate | orbit classes, subgroup marks, and irreducible linearization | direct finite derivation | high |
| Table 2 | route decision | A0–A4 verdicts with one-object reasons | Route-A evaluator | high |

### Figure 1 caption target

“The formal \(C_2\)-colored Burnside ledger retains the \(pqr\) residual,
but each canonical analytic readout loses a required property: augmentation
kills the residual, prime specialization breaks fixed-fiber \(S_n\)
commutation, and the diagonal lift changes \(b(x)^r\) into \(b(x^r)\) and
adds mixed determinant factors.”

The figure is monochrome/colorblind-safe vector TikZ and remains readable in
grayscale.  It contains no decorative title; all interpretation is in the
caption.

## Citation plan

- **Introduction:** Bowen--Lanford; Gusein-Zade--Luengo--Melle-Hernández;
  Labelle--Yeh.
- **Classical boundary:** Joyal; Labelle--Yeh; Dress--Siebeneicher (1988,
  1989); Metropolis--Rota; Siebeneicher; Brun; Knutson; Pollicott.
- **Infinite-label boundary:** Church--Ellenberg--Farb; Thoma; Simon.
- **All DOI metadata:** frozen in `LITERATURE_AUDIT.md` and
  `references.bib`.

## Front-matter checks

- The title names both the positive formal lift and negative analytic result.
- The abstract contains the exact \(S_3\) and Schatten certificates.
- The introduction states the route decision before Section 2.
- Figure 1 summarizes the full argument for a skim reader.

## Review status

External or cross-model review is intentionally skipped.  The project lead
explicitly requested no review round.  The manuscript receives only internal
proof, citation, compilation, and scope checks.

## Completion checklist

- [x] Source lock frozen
- [x] Preregistration frozen
- [x] Proof dependency map complete
- [x] Primary-source novelty boundary complete
- [x] Modular LaTeX sections drafted
- [x] TikZ Figure 1 integrated
- [x] Citation audit: zero orphans
- [x] Four clean `pdflatex` passes after BibTeX
- [x] A4, embedded fonts, no undefined references/citations, no markers
