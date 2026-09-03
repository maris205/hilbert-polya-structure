# P167 paper plan

**Working title:** Minimum Inverse-Position Feedback on Finite Endofunctions  
**Format:** anonymous short theory note, `amsart` 10pt  
**Lifecycle:** internal Round 0; `HOLD_EXTERNAL`  
**Date:** 2026-09-03 UTC  
**Target length:** 4--5 A4 pages including the minimal bibliography

## Theorem ceiling

The paper is allowed to claim only the theorem package for the literal map

```text
M(f)(i) = min {j : f(j)=i} if i is present,
          i                  if i is absent.
```

The residual package consists of the path/cycle update, the sharp full and
first-image clocks, the recurrent component census and its consequences,
and the target-resolved inverse product with its Bell ceiling.  Least kernel
transversals, first-occurrence/set-partition encodings, generic functional
graphs, labelled `SET` calculus, involution and Bell numbers, and the
Artin--Mazur conversion are background.  The bounded owner non-hit is not a
novelty or priority result.

## Claims--evidence matrix

| ID | Claim | Analytic evidence | Executable control | Section |
|---|---|---|---|---|
| C1 | First images have cycle/path components; cycles invert and paths reverse or split | first-position injection and direct occurrence calculation | every literal image parsed through `n=7`; all path orders/cycles through size 9 | Sections 1--2 |
| C2 | Sharp heights are `2n-2` globally and `2n-3` on the first image | endpoint-deletion induction, mandatory zero exclusion, explicit witness | all states/targets through `n=7` and symbolic witnesses | Section 2 |
| C3 | Connected recurrent census, EGF, fixed counts, all positive-iterate counts, and zeta | endpoint inequalities plus labelled component assembly | coefficient agreement through order 14 and state powers through `n=7` | Section 3 |
| C4 | Exact fibre formula for every target, including unsupported targets | forced first positions plus optional fixed symbols | every target through `n=7`, with adversarial collisions | Section 4 |
| C5 | Maximum fibre is `B_n`, attained at the identity | injection by kernel partition and block-minimum construction | all restricted-growth partitions and all target maxima through `n=7` | Section 4 |
| C6 | Boundary rows `n=1,2,3` are exact | direct small dynamics, the uniform formulas, and finite fibre substitution | complete edge/tail/period/fibre graphs | Theorem 1 and Section 4 |

## Section plan

### Abstract

- State the literal identity-on-missing convention.
- Report both sharp clocks, recurrent/fixed census, and every-target inverse.
- Include the Bell maximum and the external hold.
- No citations and no ownership claim.

### 1. Literal feedback map and theorem ceiling

- Define the carrier, feedback iteration, tail, period, first image, and
  inverse-product notation.
- Separate the one-sided inner-inverse/KRR relation from mutual inverses.
- Subtract the five primary background lanes.
- State one complete main theorem containing all required formulas and the
  `n=1,2,3` table.

### 2. Component action and clocks

- Prove off-diagonal injection and the exact path/cycle action.
- Prove the recurrent endpoint criterion and irreversibility of splitting.
- Prove the path bound `2s-2` with its unique decreasing maximizer.
- Exclude that maximizer from the first image using the mandatory zero and
  realize both sharp bounds with the displayed source.

### 3. Recurrent species and zeta

- Count recurrent paths separately at sizes 1, 2, 3 and by a free
  two-pair action for size at least 4.
- Assemble connected components by the labelled-set formula.
- Classify fixed states as involutions and derive odd/even iterate counts.
- Convert those counts to the formal finite-map zeta function.

### 4. Inverse atlas and Bell ceiling

- Identify forced present symbols, forbidden fixed/present collisions, and
  optional fixed symbols.
- Multiply the legal already-open letters at every unforced position.
- Prove the converse construction, so zero fibres are covered as well.
- Inject each fibre into kernel partitions and realize all partitions over
  the identity.
- Close the `n=1,2,3` boundary proof, including the `n=3` fibre histogram.

### 5. Controls and scope

- Describe the standalone standard-library verifier as falsification, not
  proof.
- State the exact assertion count and two byte-identical replays.
- Repeat the non-claims and `HOLD_EXTERNAL` lifecycle.

## Figure and table plan

No figure is necessary: the component rule is shorter and less ambiguous in
symbols.  One compact table in Theorem 1 records all boundary invariants for
`n=1,2,3`.  No prior-bound comparison table is appropriate because the
owner search produced background neighbours, not a directly comparable
theorem for the literal iterate.

## Citation plan

- Transformation semigroups and kernel transversals:
  `FernandesEtAl2009`, `Higgins2019`.
- Restricted-growth/first-occurrence encoding: `BeanEtAl2026`.
- Functional-digraph background: `FlajoletOdlyzko1989`.
- Periodic-point zeta definition: `ArtinMazur1965`.

All five entries are DOI- or publisher-verified and are cited only for
background subtraction.

## Review boundary

No paper review is part of Round 0, as required by the batch assignment.
The inputs include a completed independent hostile candidate gate; it is
used as a frozen theorem contract, not relabelled as a manuscript review.

## Completion checklist

- [x] frozen theorem and ownership ceiling
- [x] complete anonymous LaTeX draft
- [x] standalone verifier and two exact replays
- [x] minimal verified bibliography
- [x] settled Round-0 PDF and source-only cold-build match
- [x] author-side PDF, anonymity, log, and metadata QA
