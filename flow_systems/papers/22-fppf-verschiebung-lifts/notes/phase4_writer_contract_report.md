# Paper 22 Phase-4b writer contract report

Date: **2026-08-24**  
Contract: **academic_paper/writer_full/v1**  
Decision round: **1**

## Draft Body

The complete seven-section draft is
[paper/manuscript.tex](../paper/manuscript.tex). It contains an English
abstract, an independently composed Chinese abstract, the main fppf theorem,
the separately checked finite-flat theorem, the explicit all-index proof, the
extension-class corollary, the source-sensitive correction, scope controls,
and all required declaration fields.

Body word counts were measured on de-TeXed section text. Mathematical
displays are normalized by the counter and declarations and references are
excluded:

| Section | Allocation | Measured | Allowed range | Result |
|---|---:|---:|---:|---|
| 1. Introduction and main results | 800 | 901 | 680--920 | pass |
| 2. Rational Witt sheaves and the extension | 650 | 561 | 553--748 | pass |
| 3. Three descent lemmas | 800 | 682 | 680--920 | pass |
| 4. The all-index descent obstruction | 1,250 | 1,063 | 1,063--1,438 | pass |
| 5. The extension-theoretic formulation | 550 | 469 | 468--633 | pass |
| 6. Finite-flat site and Dedekind-section assertion | 650 | 583 | 553--748 | pass |
| 7. Scope, controls, and conclusion | 300 | 327 | 255--345 | pass |
| **Body total** | **5,000** | **4,586** | **4,500--5,500** | **pass** |

## Dimension Scores

### D1 — section completeness: pass

All seven approved sections are present. There are no MATERIAL GAP, TODO, or
FIXME placeholders. Required data availability, ethics, author contributions,
funding, competing-interests, AI-use, and limitations statements are present.
Identity, funding, and competing-interest content remain openly marked
AUTHOR TO CONFIRM, rather than being invented.

### D2 — citation density: pass

External factual and source-attribution claims cite the verified Deninger v1
record, the nearest different-owner Deninger--Mellit result, or exact Stacks
tags. The bounded absence statement carries dated search provenance and is
expressly not promoted to a global novelty claim. The new mathematical
claims are supported by displayed proofs rather than external authority.

### D3 — argument-blueprint fidelity: pass

The manuscript follows all four frozen CER chains: sheaf epimorphy versus
objectwise surjectivity; uniqueness on the Dedekind root cover; nonzero
overlap specialization for every N>1; and the Ext/finite-flat consequences.
The precommitted counterarguments about alternate local choices, Cech
overreach, site transfer, and Route overclaiming are addressed explicitly.

### D4 — total word count: pass

The 4,586-word body is 8.3 percent below the 5,000-word target and therefore
inside the contract's plus-or-minus 10 percent band.

### D5 — per-section word count: pass

Every section lies within the approved plus-or-minus 15 percent allocation.
Section 4 sits at the lower integer boundary and was retained because its proof is complete and
replicable without padding.

### D6 — paragraph structure: pass

Body paragraphs consistently open with the relevant mathematical or
source-level claim, supply a proof step or citation, explain its role, and
link to the next step. Inter-section transitions are explicit. Short
theorem, proof-opening, introduction-opening, and conclusion-ending
paragraphs are treated under the contract's stated exemptions.

### D7 — register consistency: pass

The draft maintains a neutral pure-mathematics register. The source
correction uses restrained phrases such as “as stated,” “appears to use,”
and “requires correction.” It does not claim author agreement, submission
readiness, Route advancement, or a result about ring endomorphisms.

## Failure Condition Checks

| Condition | Triggered? | Basis |
|---|---|---|
| F1 mandatory dimension block | no | D1--D3 all pass |
| F4 mandatory dimension warn | no | D1--D3 all pass |
| F2 high-priority dimension block | no | D4--D5 pass |
| F3 high-priority dimension warn | no | D4--D5 pass |
| F0 every mandatory dimension pass | **yes** | D1--D3 pass and no block |

## Writer Decision

**writer_decision=accept**

The draft may proceed to citation/abstract checks and independent evaluator
review. This decision does not authorize Stage 2.5 integrity review,
submission, public release, Git operations, or external contact.
