# P168 paper plan

**Working title:** Quartic Inverse-Span Dynamics: Binary Depth Jump and Exact Fibres  
**Format:** anonymous `amsart` 10pt short theory note  
**Lifecycle:** internal Round 0; `GREEN_OWNER_THIN / HOLD_EXTERNAL`  
**Date:** 2026-09-03 UTC  
**Target length:** 4--6 A4 pages including the minimal bibliography

## One-sentence contribution

After assigning the known inverse-subspace classification and inverse-line
geometry zero credit, the note determines the whole degree-four span-of-
inverses functional graph: its sharp binary/odd depth jump, image
stabilization, cycles and zeta function, and every target's fibre at every
positive time.

## Theorem ceiling

For a prime `p`, the carrier is the complete `F_p`-subspace lattice of
`K=F_{p^4}` and the literal update is

```text
J(A)=span_Fp{a^(-1): 0 != a in A},   J(0)=0.
```

Kolomeec--Bykov's classification of subspaces whose patched inverse image is
a subspace, and the normal-rational-curve geometry of inverse projective lines
from Faina--Kiss--Marcugini--Pambianco and Lavrauw--Zanella, are published
inputs.  They receive no contribution credit.  The note is allowed to retain
only the integrated finite-dynamical consequences listed below.  It contains
no novelty or priority assertion.

## Claims--evidence matrix

| ID | Claim | Analytic evidence | Executable control | Section |
|---|---|---|---|---|
| C1 | Rank never decreases; equality is equivalent to recurrence; recurrent states are `0`, `K`, lines, and scaled `F_{p^2}` planes | cardinality, published patched-inversion classification, direct scalar calculation | every subspace and edge for `p=2,3,5`; recurrent planes compared with an independently constructed quadratic subfield | Sections 1--3 |
| C2 | A non-subfield plane has image rank `min(p+1,4)`, so the sharp maximum tail is 2 only at `p=2` and 1 at odd primes | denominator-clearing independence for `1,(alpha-t)^(-1)`; equality classification rules out recurrent hyperplanes | complete rank-by-rank transition checks and depth histograms | Sections 2--3 |
| C3 | The recurrent count, fixed/two-cycle counts, depth enumerator, image stabilization, and zeta function have closed formulas | Gaussian coefficients and inversion on two cyclic scalar quotients | graph cycles, fixed points, recurrent count, and images checked exhaustively | Section 3 |
| C4 | Every target has an exact `t`-step fibre formula; at `p=2` each hyperplane has exactly two one-step plane predecessors | rank monotonicity, twisted scalar law, trace-pairing transitivity, mass count `30/15` | every target checked at times 1--4; full-field fibres are `16,46` for `p=2` and stable `161`, `937` for `p=3,5` | Section 4 |
| C5 | The full component graph is a bare recurrent core plus a single basin rooted at `K` | C1--C4 | complete edge digests for 67, 212, and 1,120 states | Sections 4--5 |

## Section plan

### Abstract

- Define the literal map and degree-four carrier in the first sentence.
- State the published-input boundary without citations.
- Give the sharp height dichotomy, recurrent description, and strongest fibre
  number (`30` binary planes over `15` hyperplanes, two each).
- Close with graph/zeta completeness and the external hold.

### 1. Literal map, published inputs, and complete theorem

- Define patched inversion, span update, tail, recurrence, zeta, and counting
  constants `L,P,Q,S,R,F`.
- State the two direct published inputs before the theorem and explicitly
  assign them zero credit.
- State one complete theorem: rank transitions, height/depth/image formulas,
  recurrent and cycle census, zeta, all-time fibres, component graph.

### 2. Rank growth and the inverse of a plane

- Prove rank monotonicity by cardinality.
- Show equality makes patched inversion exactly fill the output and hence
  gives a one/two-cycle.
- Re-state the published equality classification only at the required
  strength.
- Give the self-contained denominator-clearing proof of the inverse-line span
  rank, while saying that its projective geometry is already known.

### 3. Sharp time and recurrent core

- Derive the complete transition table and prove the binary/odd sharp height.
- Count all subspaces and recurrent states by Gaussian coefficients.
- Reduce the recurrent map to inversion on cyclic scalar quotients.
- Derive fixed counts, two-cycles, fixed iterates, zeta, depth enumerator, and
  image stabilization.

### 4. Every-target fibres and component graph

- Use rank monotonicity to exclude all unlisted incoming edges.
- Prove `J(lambda A)=lambda^(-1)J(A)`.
- Use trace hyperplanes to prove scalar transitivity; divide `30` binary
  source planes uniformly among `15` hyperplanes.
- State the complete positive-time fibre atlas and the resulting component
  graph.

### 5. Exact controls and scope

- Give checked rows for `p=2,3,5`.
- Describe the standalone standard-library verifier and frozen 32,754-check
  transcript as falsification evidence, not proof.
- Repeat the prime/degree-four restriction, direct-owner subtraction, and
  `HOLD_EXTERNAL` status.

## Figure and table plan

No external figure is needed.  The paper-figure phase resolves to two compact
LaTeX tables:

| ID | Type | Purpose | Source |
|---|---|---|---|
| Table 1 | theorem transition table | shows the only branch producing the binary extra level | analytic partition of subspaces |
| Table 2 | exact control table | compares `p=2,3,5` state/image/cycle/depth/fibre data | frozen verifier output |

A graph drawing would duplicate Table 1 and become less legible as `p`
varies.  No prior-bound table is appropriate: the cited papers own geometric
inputs rather than a competing temporal/fibre theorem.

## Citation plan

- Patched inverse-image classification: `KolomeecBykov2024`.
- Inverse-line normal-rational-curve geometry: `FainaEtAl2002`,
  `LavrauwZanella2014`.
- Inverse-closed/equal-dimensional subspace context: `Mattarei2007`,
  `Csajbok2013`.
- Periodic-point zeta terminology: `ArtinMazur1965`.

All six records are checked against primary publisher or DOI metadata.  The
bibliography will contain only these cited entries.

## Round boundary

The independent pre-paper hostile gate fixes the theorem ceiling but is not a
manuscript review.  No hostile review is created in Round 0.  The frozen PDF
remains `HOLD_EXTERNAL` and is not an external-release artifact.

## Completion checklist

- [x] complete anonymous manuscript
- [x] visible zero-credit treatment of both direct geometric inputs
- [x] standalone verifier and byte-identical frozen output
- [x] verified six-entry bibliography
- [x] canonical and preserved Round-0 PDFs
- [x] two source-only cold builds matching the canonical PDF
- [x] font, metadata, anonymity, text, and visual QA
- [x] paper-local integrity manifest
