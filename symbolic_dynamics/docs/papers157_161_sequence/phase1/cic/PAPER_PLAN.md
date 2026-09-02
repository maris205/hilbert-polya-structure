# Paper plan — cut-intersection collapse

Target form: anonymous AMS probability/combinatorics short note, 4–5 pages.

## Abstract

Define the repeated-cut intersection process.  State the complementary-word
encoding, exact absorption CDF, every-target fibre, corrected image boundary,
and image EGF.  Mention exact falsification without suggesting simulation.

## 1. Process, owner boundary, and main theorem

- Fix labels, fairness, independence, and starting state `K_n`.
- Define `R`, `A_R`, `r(H)`, and `z(H)` with all zero-size conventions.
- State temporal and target parts together.
- Print the `n=5,t=2` two-edges-plus-isolate nonimage.

## 2. Complement histories and one-sided occupancy

- Prove the pathwise edge criterion.
- Derive `(2e^x-1)^R` by distinguished complementary pairs.
- Expand to the finite inclusion–exclusion expression.

## 3. Absorption law

- Identify emptiness with one-sided occupancy.
- Give CDF, first hits, one-edge tail, almost-sure absorption, and exact mean
  series.
- Keep the elementary union bound in a supporting role.

## 4. Every-target fibres and image enumeration

- Prove component necessity and unique bipartition up to orientation.
- Reserve an injection of pairs and orient each component.
- Count isolates on unused pairs.
- Prove sufficiency and uniqueness of decoding.
- Derive the image EGF with a separate isolate-free top-resource term.

## 5. Exact controls and scope

- Explain enumeration of every possible graph, not just observed targets.
- Report 35,278 assertions and canonical hash.
- Subtract biclique, bicluster, and random-intersection neighbourhoods.
- Preserve `HOLD_EXTERNAL`.
