# P175 paper plan — diagonal-feedback commutator

**Working title:** *Diagonal-Feedback Commutators and Support-Colouring
Fibres*  
**Type:** finite algebraic dynamics / enumerative short note  
**Format:** anonymous `amsart`, A4, 10pt  
**Round:** final Round 2; dual hostile reviews closed  
**Target length:** 3--5 pages including references  
**External state:** `HOLD_EXTERNAL`

## One-sentence contribution

The self-map (A\mapsto[\operatorname{diag}(A),A]) has a completely
explicit height-two functional graph, while every target fibre is an
occupation-weighted proper-colouring sum determined only by the target's
undirected support.

## Claims--evidence matrix

| claim | proof evidence | exact evidence | location |
|---|---|---|---|
| (\Phi^2=0), unique recurrent zero | output diagonal vanishes entrywise | every literal arrow in eleven boxes | Theorem 2 |
| image iff zero diagonal plus (q)-colourable support | solve each off-diagonal scalar equation after fixing the input diagonal | every target, including (\mathbb F_4) | Theorem 1 |
| complete occupation-marked fibre sum | equal-colour ordered entries are free, unequal-colour entries unique | every target grouped by labelled diagonal occupations | Theorem 1 |
| zero is the unique largest fibre | every nonzero support excludes a positive summand from the empty-support sum | fibre maxima in every box | Corollary 1 |
| exact image and kernel formulas | group targets by support; group colourings by occupation | independent support census and composition sum | Corollary 1 |
| complete rooted functional graph and all-time fibres | (\operatorname{im}\Phi\subseteq\ker\Phi), plus target indegrees | all depth layers and second images | Theorem 2 |

## Structure

### Abstract

- State the literal map in the first sentence.
- Give the two-step clock, image criterion, and fibre sum.
- Name the image/kernel/tree consequences.
- Close with owner subtraction and external hold.
- Target: 150--190 words.

### 1. Diagonal feedback and scope

- Define the finite field, carrier, diagonal extraction, and commutator.
- Explain why image classification is not automatic from the shallow clock.
- Position against additive commutator varieties, fixed-element/Engel maps,
  P119, and Potts/chromatic theory.
- State the narrow residual without novelty language.

### 2. Support colourings and every-target fibres

- Define (G_B), labelled occupations, (m(c)), and
  (\mathcal P_{G,q}(X;\mathbf z)).
- Theorem 1: diagonal obstruction, exact fibre polynomial, image criterion,
  support-only dependence.
- Prove the scalar equations and count free ordered entries.
- Corollary: unique maximum, kernel composition sum, image graph sum.

### 3. Complete functional graph

- Prove (\Phi^2=0), sharp boundary heights, and the all-time fibre formula.
- Describe the unique rooted component: root loop, depth-one leaves/branch
  vertices, and support-indexed depth-two leaf counts.
- Give image tower, depth layers, fixed counts, and zeta.

### 4. Exact controls and limitations

- Report the independent standard-library verifier.
- Include representative table with (\mathbb F_4) to test prime-power scope.
- Separate exhaustive computation from the uniform proof.
- Reiterate the shallow-clock and owner-density limitations.

## Figure plan

**Figure N/A.**  No figure is planned for Round 0.  The functional graph is a
height-two rooted tree whose complete branching data fit in one displayed
formula, and a decorative tree would communicate less than the theorem.
One compact exact-control table is planned.

## Citation plan

- Section 1: Young; Kadyrsizova--Yerlanov; Baddeley; Larsen--Lu; Bier.
- Section 2: Sokal for the Potts/Tutte/chromatic owner region.
- Section 2: Stanley for the chromatic symmetric occupation enumerator;
  display and subtract the exact Potts specialization and deterministic
  occupation-weight transform.
- Section 3: Artin--Mazur for zeta bookkeeping.
- Section 4: no new citations.

All entries must be DOI- or primary-page verified and only cited entries may
remain in `references.bib`.

## Review boundary

Review A returned no finding.  Review B left the mathematics intact but
forced the exact Potts/Stanley owner reframe; it is implemented in the
Round-2 source and passed read-only delta acceptance.  No release action is
authorized.

## Completion checklist

- [x] narrative and claim spine
- [x] figure documented as N/A
- [x] complete anonymous LaTeX source
- [x] independent canonical verifier
- [x] settled PDF and byte-identical Round-0 copy
- [x] build and self-QA ledgers
